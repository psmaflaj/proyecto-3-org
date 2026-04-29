# *********
# * HackDisassembler.py
# * Lee un archivo .hack (binario) y lo traduce a código ensamblador (.asm).
# * Autorres: santiago mafla y lucas saldarriaga
# *********

import sys
import os

# --- 1. DICCIONARIOS DE TRADUCCIÓN ---

COMP_DICT = {
    # Operaciones estándar con a=0
    "0101010": "0",
    "0111111": "1",
    "0111010": "-1",
    "0001100": "D",
    "0110000": "A",
    "0001101": "!D",
    "0110001": "!A",
    "0001111": "-D",
    "0110011": "-A",
    "0011111": "D+1",
    "0110111": "A+1",
    "0001110": "D-1",
    "0110010": "A-1",
    "0000010": "D+A",
    "0010011": "D-A",
    "0000111": "A-D",
    "0000000": "D&A",
    "0010101": "D|A",

    # Operaciones estándar con a=1 (se cambia A por M)
    "1110000": "M",
    "1110001": "!M",
    "1110011": "-M",
    "1110111": "M+1",
    "1110010": "M-1",
    "1000010": "D+M",
    "1010011": "D-M",
    "1000111": "M-D",
    "1000000": "D&M",
    "1010101": "D|M",

    # NUEVAS OPERACIONES SHIFT (Basadas en zx=0, nx=0, zy=0, ny=0, no=1)
    # Shift Left (f=0)
    "0000001": "A<<1", # a=0
    "1000001": "M<<1", # a=1
    
    # Shift Right (f=1)
    "0000011": "A>>1", # a=0
    "1000011": "M>>1", # a=1
}

DEST_DICT = {
    "000": "",
    "001": "M",
    "010": "D",
    "011": "MD",
    "100": "A",
    "101": "AM",
    "110": "AD",
    "111": "AMD"
}

JUMP_DICT = {
    "000": "",
    "001": "JGT",
    "010": "JEQ",
    "011": "JGE",
    "100": "JLT",
    "101": "JNE",
    "110": "JLE",
    "111": "JMP"
}

# --- 2. FUNCIONES DE DECODIFICACIÓN ---

def decode_a_instruction(line):
    # Toma desde el índice 1 hasta el final y lo convierte de base 2 a base 10
    address = int(line[1:], 2)
    return f"@{address}"

def decode_c_instruction(line):
    # Cortar el string en las partes que componen la instrucción C
    comp_bits = line[3:10]
    dest_bits = line[10:13]
    jump_bits = line[13:16]

    # Buscar en los diccionarios
    comp_mnemo = COMP_DICT.get(comp_bits, "ERROR_COMP")
    dest_mnemo = DEST_DICT.get(dest_bits, "")
    jump_mnemo = JUMP_DICT.get(jump_bits, "")

    # Ensamblar la instrucción final
    result = ""
    if dest_mnemo != "":
        result += f"{dest_mnemo}="
    
    result += comp_mnemo

    if jump_mnemo != "":
        result += f";{jump_mnemo}"

    return result

# --- 3. BUCLE PRINCIPAL (Lectura y Escritura) ---

def main():
    # Validar argumentos en la consola
    if len(sys.argv) < 3 or sys.argv[1] != "-d":
        print("Uso correcto: python HackDisassembler.py -d Archivo.hack")
        return

    input_file = sys.argv[2]
    output_file = input_file.replace(".hack", "Dis.asm")

    try:
        # Abrir el archivo de lectura y el de escritura al mismo tiempo
        with open(input_file, 'r') as file_in, open(output_file, 'w') as file_out:
            line_number = 1
            for line in file_in:
                # Quitar espacios y saltos de línea (\n)
                clean_line = line.strip()

                if not clean_line:
                    continue
                
                # Validar la regla de oro: exactamente 16 bits
                if len(clean_line) != 16:
                    print(f"Error en la línea {line_number}: La instrucción no tiene 16 bits.")
                    file_out.close()
                    os.remove(output_file)
                    return

                # Determinar el tipo de instrucción y decodificar
                if clean_line.startswith('0'):
                    asm_code = decode_a_instruction(clean_line)
                elif clean_line.startswith('111'):
                    asm_code = decode_c_instruction(clean_line)
                else:
                    print(f"Error en la línea {line_number}: Instrucción no reconocida (no empieza por 0 ni 111).")
                    file_out.close()
                    os.remove(output_file)
                    return

                # Escribir la línea decodificada en el nuevo archivo
                file_out.write(asm_code + "\n")
                line_number += 1
                
        print(f"¡Desensamblado completado exitosamente! Archivo guardado como: {output_file}")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{input_file}'")

if __name__ == "__main__":
    main()