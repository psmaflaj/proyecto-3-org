# proyecto-3-org
¡Qué más socio! Aquí te dejo las instrucciones exactas para que pruebes el Desensamblador (Punto 2) que armé:

1. Lo que necesitas tener a la mano:

Mi script de Python llamado HackDisassembler.py.

Cualquier archivo .hack de prueba (puedes usar uno de los que genere tu traductor o uno de los proyectos anteriores de Nand2Tetris).

Importante: Asegúrate de que ambos archivos estén guardados exactamente en la misma carpeta.

2. Cómo ejecutarlo en la consola:

Abre tu terminal (o el cmd en Windows) y navega hasta la carpeta donde guardaste los dos archivos.

Escribe el siguiente comando y presiona Enter:

Bash
python HackDisassembler.py -d nombre_del_archivo.hack
(Ojo: Recuerda cambiar "nombre_del_archivo.hack" por el nombre real del archivo binario que vayas a probar).

3. El resultado esperado:

Si todo sale bien, la terminal te mostrará un mensaje de éxito.

En esa misma carpeta aparecerá automáticamente un archivo nuevo que termina en Dis.asm.

Si abres ese archivo nuevo, verás que la secuencia de ceros y unos se convirtió de vuelta a las instrucciones originales de ensamblador (@20, D=M, etc.).
