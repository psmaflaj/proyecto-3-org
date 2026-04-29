# HackAssembler / HackDisassembler

Proyecto 3 de Organización de Computadores.

## Contenido
- `src/HackDisassembler.py`: clase principal para desensamblar `.hack` a `.asm`
- `src/common.py`: tablas de decodificación compartidas
- `test/test_hackdisassembler.py`: pruebas unitarias
- `docs/API.md`: descripción de clases y funciones
- `docs/DESIGN.md`: decisiones de diseño
- `docs/USER_GUIDE.md`: instrucciones de uso

## Ejecución
```bash
python src/HackDisassembler.py programa.hack
```

Genera un archivo `programaDis.asm` en el mismo directorio del archivo de entrada.
