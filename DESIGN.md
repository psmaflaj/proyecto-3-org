# Diseño

## Objetivo
Desensamblar instrucciones Hack binarias a su forma assembler, incluyendo la extensión de corrimiento (`<<1` y `>>1`).

## Estrategia
1. Leer línea por línea.
2. Validar que cada línea contenga exactamente 16 bits.
3. Identificar instrucción A si el bit más significativo es `0`.
4. Identificar instrucción C si empieza con `111`.
5. Para instrucciones C:
   - decodificar `comp`, `dest` y `jump`
   - si `comp` corresponde a shift, usar la tabla `BITS_TO_SHIFT_SRC`
6. Escribir el resultado como `ProgDis.asm`.

## Codificación de shift usada
Se asume la codificación acordada en `design.txt` del proyecto 2:
- `comp = 0000001` representa `<<1`
- `comp = 0000011` representa `>>1`
- los tres bits finales seleccionan la fuente del corrimiento (`D`, `A`, `M`)

## Manejo de errores
Ante cualquier línea inválida:
- se lanza `DisassemblyError`
- se reporta el número de línea
- se detiene el proceso sin dejar una salida incompleta
