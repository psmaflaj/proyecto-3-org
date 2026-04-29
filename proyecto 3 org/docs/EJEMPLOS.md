Ejemplo:

Bash
python HackAssembler.py Prog.asm
Resultado: Se generará un archivo llamado Prog.hack en el mismo directorio. Si hay errores de sintaxis en el código .asm, el programa se detendrá y mostrará un mensaje de error.

2. Uso del Desensamblador (Hack Disassembler)
Este programa toma un archivo binario de 16 bits (.hack) y lo decodifica de vuelta a su código ensamblador original (.asm).

Comando de ejecución:
Se debe incluir la bandera obligatoria -d antes del nombre del archivo.

Bash
python HackDisassembler.py -d [nombre_del_archivo.hack]
Ejemplo:

Bash
python HackDisassembler.py -d Prog.hack
Resultado: Se generará un archivo llamado ProgDis.asm con las instrucciones legibles.