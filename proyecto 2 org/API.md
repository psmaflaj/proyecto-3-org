# API

## `HackDisassembler`

Clase encargada de convertir un archivo binario Hack (`.hack`) en su representación assembler (`.asm`).

### Métodos

#### `disassemble(input_path: Path) -> Path`
Lee el archivo de entrada, valida que cada instrucción tenga 16 bits binarios y escribe el archivo `*Dis.asm`.

## `DisassemblyError`

Excepción usada para reportar errores de formato o codificación, incluyendo el número de línea.

## `common.py`

Contiene:
- tablas `BITS_TO_COMP`, `BITS_TO_DEST`, `BITS_TO_JUMP`
- codificación extendida de shift
- utilidades de escritura segura
