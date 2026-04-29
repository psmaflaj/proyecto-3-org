"""
/*********
* HackAssembler.py – Traduce un archivo .asm a código binario .hack,
* incluyendo soporte para la extensión de corrimiento del proyecto.
* Autor 1:
* Autor 2:
*********/
"""
from __future__ import annotations

import sys
from pathlib import Path

from common import (
    COMP_TO_BITS,
    DEST_TO_BITS,
    JUMP_TO_BITS,
    LABEL_RE,
    PREDEFINED_SYMBOLS,
    SHIFT_LEFT_COMP,
    SHIFT_RE,
    SHIFT_RIGHT_COMP,
    SHIFT_SRC_TO_BITS,
    SYMBOL_RE,
    strip_comment_and_space,
    write_text,
)


class AssemblyError(Exception):
    """Error semántico o sintáctico durante el ensamblado."""

    def __init__(self, line_no: int, message: str) -> None:
        super().__init__(f"Línea {line_no}: {message}")
        self.line_no = line_no
        self.message = message


class HackAssembler:
    """
    Ensamblador Hack con dos pasadas:
    1. recolecta etiquetas
    2. traduce instrucciones A y C a binario
    """

    def __init__(self) -> None:
        self.symbols = dict(PREDEFINED_SYMBOLS)
        self.next_variable_address = 16

    def assemble(self, input_path: Path) -> Path:
        if input_path.suffix.lower() != ".asm":
            raise ValueError("El archivo de entrada debe tener extensión .asm")
        if not input_path.exists():
            raise FileNotFoundError(f"No existe el archivo: {input_path}")

        raw_lines = input_path.read_text(encoding="utf-8").splitlines()
        parsed = [(i + 1, strip_comment_and_space(line)) for i, line in enumerate(raw_lines)]

        self._first_pass(parsed)

        machine_lines: list[str] = []
        for line_no, clean in parsed:
            if not clean:
                continue
            if LABEL_RE.fullmatch(clean):
                continue
            machine_lines.append(self._translate_instruction(line_no, clean))

        output_path = input_path.with_suffix(".hack")
        output_text = "\n".join(machine_lines)
        if machine_lines:
            output_text += "\n"
        write_text(output_path, output_text)
        return output_path

    def _first_pass(self, parsed_lines: list[tuple[int, str]]) -> None:
        rom_address = 0
        for line_no, clean in parsed_lines:
            if not clean:
                continue

            label_match = LABEL_RE.fullmatch(clean)
            if label_match:
                label = label_match.group(1)
                if label in self.symbols and label not in PREDEFINED_SYMBOLS:
                    raise AssemblyError(line_no, f"Etiqueta duplicada: {label}")
                self.symbols[label] = rom_address
                continue

            rom_address += 1

    def _translate_instruction(self, line_no: int, clean: str) -> str:
        if clean.startswith("@"):
            return self._translate_a_instruction(line_no, clean)
        return self._translate_c_instruction(line_no, clean)

    def _translate_a_instruction(self, line_no: int, clean: str) -> str:
        symbol = clean[1:]
        if not symbol:
            raise AssemblyError(line_no, "Instrucción A vacía")

        if symbol.isdigit():
            value = int(symbol)
        else:
            if not SYMBOL_RE.fullmatch(symbol):
                raise AssemblyError(line_no, f"Símbolo inválido: {symbol}")
            if symbol not in self.symbols:
                self.symbols[symbol] = self.next_variable_address
                self.next_variable_address += 1
            value = self.symbols[symbol]

        if not (0 <= value <= 32767):
            raise AssemblyError(line_no, f"Valor fuera de rango para instrucción A: {value}")

        return format(value, "016b")

    def _translate_c_instruction(self, line_no: int, clean: str) -> str:
        shift_match = SHIFT_RE.fullmatch(clean)
        if shift_match:
            dest = shift_match.group(1) or ""
            source = shift_match.group(2)
            operator = shift_match.group(3)

            comp_bits = SHIFT_LEFT_COMP if operator == "<<1" else SHIFT_RIGHT_COMP
            dest_bits = DEST_TO_BITS.get(dest)
            src_bits = SHIFT_SRC_TO_BITS.get(source)

            if dest_bits is None:
                raise AssemblyError(line_no, f"Destino inválido en shift: {dest}")
            if src_bits is None:
                raise AssemblyError(line_no, f"Fuente inválida en shift: {source}")

            return "111" + comp_bits + dest_bits + src_bits

        if "=" in clean:
            dest, remainder = clean.split("=", 1)
        else:
            dest, remainder = "", clean

        if ";" in remainder:
            comp, jump = remainder.split(";", 1)
        else:
            comp, jump = remainder, ""

        dest = dest.strip()
        comp = comp.strip()
        jump = jump.strip()

        if dest not in DEST_TO_BITS:
            raise AssemblyError(line_no, f"Destino inválido: {dest}")
        if jump not in JUMP_TO_BITS:
            raise AssemblyError(line_no, f"Salto inválido: {jump}")
        if comp not in COMP_TO_BITS:
            raise AssemblyError(line_no, f"Campo comp no reconocido: {comp}")

        return "111" + COMP_TO_BITS[comp] + DEST_TO_BITS[dest] + JUMP_TO_BITS[jump]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Uso: python HackAssembler.py Prog.asm", file=sys.stderr)
        return 1

    input_path = Path(argv[1])

    try:
        HackAssembler().assemble(input_path)
    except (AssemblyError, FileNotFoundError, ValueError) as exc:
        output_path = input_path.with_suffix(".hack")
        if output_path.exists():
            output_path.unlink()
        print(str(exc), file=sys.stderr)
        return 1

    # El enunciado pide no mostrar mensajes si todo sale bien.
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
