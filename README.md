# Organización de Computadores - Arquitectura Hack

Este repositorio contiene la implementación completa de la arquitectura de computadores Hack (basada en el curso Nand2Tetris), abarcando tanto el diseño de hardware (Proyecto 2) como el desarrollo del software de traducción (Proyecto 3).

**Institución:** Universidad EAFIT
**Asignatura:** Organización de Computadores  
**Periodo:** 2026-1  

## 👥 Integrantes del Equipo

| Nombre | Rol Principal |
| :--- | :--- |
| **Pedro Santiago Mafla Jaramillo** | Desarrollo de Software (Ensamblador y Desensamblador) |
| **Lucas Saldariaga Quintero** | Diseño de Hardware (ALU, Shifter, CPU, Memoria) |

---

## 📁 Estructura del Repositorio

El proyecto está dividido en dos grandes módulos, cada uno con su respectiva documentación y código fuente:

```text
/
├── proyecto2/                  # Hardware (Chips y Arquitectura)
│   ├── ALU.hdl                 # ALU extendida con soporte de shift
│   ├── ALU.md5                 # Hash MD5 del archivo ALU.hdl
│   ├── CPU.hdl                 # Implementación de la CPU Hack
│   ├── CPU.md5                 # Hash MD5 del archivo CPU.hdl
│   ├── Computer.hdl            # Integración CPU + Memory + ROM32K
│   ├── Computer.md5            # Hash MD5 del archivo Computer.hdl
│   ├── Memory.hdl              # Mapeo RAM16K / Screen / Keyboard
│   ├── Memory.md5              # Hash MD5 del archivo Memory.hdl
│   ├── Shifter.hdl             # Circuito de corrimiento izquierda/derecha
│   ├── Shifter.md5             # Hash MD5 del archivo Shifter.hdl
│   ├── design.txt              # Diseño de la extensión shift en la arquitectura
│   └── design.md5              # Hash MD5 del archivo design.txt
│
├── proyecto3/                  # Software (Ensamblador y Desensamblador)
│   ├── src/                    # Scripts de Python (.py) y firmas de seguridad (.md5)
│   ├── docs/                   # API.md, DESIGN.md y USER_GUIDE.md
│   └── test/                   # Archivos de prueba (.asm, .hack)
│
├── CONTRIBUTORS.md             # Tabla de aportes porcentuales por integrante
├── CHANGELOG.md                # Historial de cambios y versiones
├── LICENSE                     # Licencia del proyecto
└── README.md                   # Este archivo
