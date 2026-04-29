# Diseño del Software - Proyecto 3

## Arquitectura General
El sistema está diseñado en Python y se divide en dos módulos independientes (`HackAssembler.py` y `HackDisassembler.py`). Se optó por un diseño modular y basado en scripts para aprovechar el manejo nativo de cadenas de texto (slicing) y diccionarios (HashMaps) que ofrece Python, garantizando una complejidad de tiempo O(1) en la traducción de instrucciones.

## Diseño del Traductor (Assembler)
El ensamblador implementa una arquitectura de **dos pasadas (Two-Pass Assembler)** para el correcto manejo de símbolos y variables:
1. **Primera Pasada (`pass_one`):** Recorre el código limpio buscando exclusivamente etiquetas de salto `(LOOP)`. Cuando encuentra una, registra la etiqueta en la `symbol_table` vinculándola a la dirección de memoria ROM de la siguiente instrucción real.
2. **Segunda Pasada (`pass_two`):** Traduce las instrucciones a binario. Si encuentra una variable `@variable` que no está en la tabla, le asigna la siguiente dirección de memoria RAM disponible (comenzando desde la posición 16).

Las instrucciones tipo C se separan en sus componentes (`dest=comp;jump`) y se traducen utilizando diccionarios estáticos predefinidos.

## Diseño del Desensamblador (Disassembler)
El desensamblador funciona con una lectura secuencial de una sola pasada. 
- Para las instrucciones tipo A (inician con `0`), extrae los 15 bits restantes y los convierte de base 2 a base 10 directamente.
- Para las instrucciones tipo C (inician con `111`), utiliza *slicing* para aislar los bits de control (`a+cccccc`, `ddd`, `jjj`) y realiza una búsqueda inversa en los diccionarios estáticos para reconstruir el mnemónico (`dest=comp;jump`).

## Integración del Shifter (Instrucciones Nuevas)
Para soportar los nuevos comandos de desplazamiento (`<<` y `>>`) implementados en la ALU del Proyecto 2, se extendieron los diccionarios de control en ambos programas. Se mapearon directamente los bits de control requeridos por la nueva ALU (`zx=0, nx=0, zy=0, ny=0, no=1`) con la variable `f` dictando la dirección (0 para izquierda, 1 para derecha).