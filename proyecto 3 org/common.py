"""
/*********
* common.py – Tablas y utilidades compartidas para traducir instrucciones
* Hack estándar y la extensión de corrimiento del proyecto.
* Autor 1: Lucas Saldarriaga
* Autor 2: Santiago Mafla
*********/
"""
from __future__ import annotations

import re
from pathlib import Path

PREDEFINED_SYMBOLS = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576,
    **{f"R{i}": i for i in range(16)},
}

DEST_TO_BITS = {
    "": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111",
}

JUMP_TO_BITS = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}

COMP_TO_BITS = {
    "0":   "0101010",
    "1":   "0111111",
    "-1":  "0111010",
    "D":   "0001100",
    "A":   "0110000",
    "!D":  "0001101",
    "!A":  "0110001",
    "-D":  "0001111",
    "-A":  "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M":   "1110000",
    "!M":  "1110001",
    "-M":  "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101",
}

# Extensión de shift usada por este proyecto:
# Instrucción: 111 + compShift(7) + dest(3) + src(3)
# compShift = 0000001 para <<1 ; 0000011 para >>1
SHIFT_LEFT_COMP = "0000001"
SHIFT_RIGHT_COMP = "0000011"
SHIFT_SRC_TO_BITS = {"D": "000", "A": "001", "M": "010"}

LABEL_RE = re.compile(r"^\(([A-Za-z_.$:][\w_.$:]*)\)$")
SYMBOL_RE = re.compile(r"^[A-Za-z_.$:][\w_.$:]*$")
SHIFT_RE = re.compile(r"^(?:(AMD|ADM|MAD|MDA|DAM|DMA|AD|DA|AM|MA|DM|MD|A|D|M)=)?(D|A|M)(<<1|>>1)$")


def strip_comment_and_space(line: str) -> str:
    return line.split("//", 1)[0].strip()


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")
