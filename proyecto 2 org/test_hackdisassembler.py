"""
test_hackdisassembler.py – Pruebas unitarias del desensamblador Hack.

Autor 1:
Autor 2:
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from HackDisassembler import HackDisassembler, DisassemblyError


class HackDisassemblerTest(unittest.TestCase):
    def test_disassemble_standard_program(self) -> None:
        src = "\n".join([
            "0000000000000010",  # @2
            "1110110000010000",  # D=A
            "0000000000000011",  # @3
            "1110000010010000",  # D=D+A
            "0000000000000000",  # @0
            "1110001100001000",  # M=D
        ]) + "\n"
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "Add.hack"
            p.write_text(src, encoding="utf-8")
            out = HackDisassembler().disassemble(p)
            self.assertEqual(
                out.read_text(encoding="utf-8").splitlines(),
                ["@2", "D=A", "@3", "D=D+A", "@0", "M=D"],
            )

    def test_disassemble_shift_program(self) -> None:
        src = "\n".join([
            "1110000001010010",  # D=M<<1
            "1110000011101000",  # AM=D>>1
            "1110000001100001",  # A=A<<1
        ]) + "\n"
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "Shift.hack"
            p.write_text(src, encoding="utf-8")
            out = HackDisassembler().disassemble(p)
            self.assertEqual(
                out.read_text(encoding="utf-8").splitlines(),
                ["D=M<<1", "AM=D>>1", "A=A<<1"],
            )

    def test_invalid_binary_line_raises(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "Broken.hack"
            p.write_text("10101X\n", encoding="utf-8")
            with self.assertRaises(DisassemblyError):
                HackDisassembler().disassemble(p)


if __name__ == "__main__":
    unittest.main()
