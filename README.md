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
│   ├── src/                    # Archivos fuente (.hdl)
│   ├── docs/                   # Documentación de diseño (design.txt)
│   └── test/                   # Scripts de prueba (.tst, .cmp)
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
