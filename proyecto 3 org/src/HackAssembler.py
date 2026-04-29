# *********
# * HackAssembler.py
# * Descripción: Lee un archivo en ensamblador (.asm) y lo traduce a código máquina binario (.hack).
# * Autor 1: Pedro Santiago Mafla Jaramillo
# *********

import sys
import os

# --- 1. DICCIONARIOS DE TRADUCCIÓN ---

COMP_DICT = {
    "0": "0101010", "1": "0111111", "-1": "0111010", "D": "0001100",
    "A": "0110000", "!D": "0001101", "!A": "0110001", "-D": "0001111",
    "-A": "0110011", "D+1": "0011111", "A+1": "0110111", "D-1": "0001110",
    "A-1": "0110010", "D+A": "0000010", "D-A": "0010011", "A-D": "0000111",
    "D&A": "0000000", "D|A": "0010101",
    "M": "1110000", "!M": "1110001", "-M": "1110011", "M+1": "1110111",
    "M-1": "1110010", "D+M": "1000010", "D-M": "1010011", "M-D": "1000111",
    "D&M": "1000000", "D|M": "1010101",
    
    # NUEVOS COMANDOS SHIFT (Deben coincidir con el design.txt de su Proyecto 2)
    "A<<1": "0000001", "M<<1": "1000001", "D<<1": "0000101", 
    "A>>1": "0000011", "M>>1": "1000011", "D>>1": "0000111"
}

DEST_DICT = {
    "": "000", "M": "001", "D": "010", "MD": "011",
    "A": "100", "AM": "101", "AD": "110", "AMD": "111"
}

JUMP_DICT = {
    "": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
    "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"
}

# Tabla de Símbolos predefinidos
symbol_table = {
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
    "SCREEN": 16384, "KBD": 24576,
    "R0": 0, "R1": 1, "R2": 2, "R3": 3, "R4": 4, "R5": 5, "R6": 6, "R7": 7,
    "R8": 8, "R9": 9, "R10": 10, "R11": 11, "R12": 12, "R13": 13, "R14": 14, "R15": 15
}

# --- 2. FUNCIONES PRINCIPALES ---

def clean_file(file_path):
    """Lee el archivo, quita espacios y comentarios."""
    clean_lines = []
    with open(file_path, 'r') as file:
        for line in file:
            # Quitar comentarios
            if '//' in line:
                line = line[:line.index('//')]
            line = line.strip()
            if line: # Si la línea no está vacía
                clean_lines.append(line)
    return clean_lines

def pass_one(lines):
    """Primera pasada: Encuentra etiquetas (LOOP) y las guarda en la tabla de símbolos."""
    rom_address = 0
    instructions = []
    for line in lines:
        if line.startswith('(') and line.endswith(')'):
            label = line[1:-1]
            symbol_table[label] = rom_address
        else:
            instructions.append(line)
            rom_address += 1
    return instructions

def pass_two(lines, output_file):
    """Segunda pasada: Traduce instrucciones A y C a binario y maneja variables."""
    ram_address = 16
    
    with open(output_file, 'w') as file_out:
        for line_number, instr in enumerate(lines, 1):
            
            # --- INSTRUCCIÓN TIPO A (@) ---
            if instr.startswith('@'):
                value = instr[1:]
                if value.isdigit():
                    address = int(value)
                else:
                    # Si es una variable nueva o etiqueta
                    if value not in symbol_table:
                        symbol_table[value] = ram_address
                        ram_address += 1
                    address = symbol_table[value]
                
                # Convertir a binario de 16 bits y escribir
                binary_a = format(address, '016b')
                file_out.write(binary_a + '\n')

            # --- INSTRUCCIÓN TIPO C ---
            else:
                dest = ""
                comp = ""
                jump = ""
                
                # Parsear dest=comp;jump
                if '=' in instr:
                    dest, instr = instr.split('=', 1)
                if ';' in instr:
                    comp, jump = instr.split(';', 1)
                else:
                    comp = instr

                # Validar que los comandos existan en los diccionarios
                if comp not in COMP_DICT:
                    print(f"Error: Comando de cómputo '{comp}' no reconocido.")
                    return False
                    
                comp_bits = COMP_DICT[comp]
                dest_bits = DEST_DICT.get(dest, "000")
                jump_bits = JUMP_DICT.get(jump, "000")

                binary_c = "111" + comp_bits + dest_bits + jump_bits
                file_out.write(binary_c + '\n')
                
    return True

# --- 3. EJECUCIÓN ---

def main():
    if len(sys.argv) != 2:
        print("Uso correcto: python HackAssembler.py Archivo.asm")
        return

    input_file = sys.argv[1]
    
    if not input_file.endswith('.asm'):
        print("Error: El archivo de entrada debe tener extensión .asm")
        return

    output_file = input_file.replace('.asm', '.hack')

    try:
        # Limpiar el código
        clean_lines = clean_file(input_file)
        
        # Primera pasada: Etiquetas
        instructions = pass_one(clean_lines)
        
        # Segunda pasada: Traducción a archivo
        success = pass_two(instructions, output_file)
        
        if success:
            print(f"¡Traducción exitosa! Archivo binario guardado como: {output_file}")
        else:
            os.remove(output_file) # Eliminar archivo roto si hubo error
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{input_file}'")

if __name__ == "__main__":
    main()