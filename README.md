# Script para corregir y modificar archivos S4RiS JSON

Este script está diseñado para corregir y modificar archivos S4RiS JSON que son generados por el juez BOCA. Una vez corregidos, estos archivos pueden ser utilizados en https://neosaris.huronos.org/.

### Requisitos

Este script requiere tener instalado Python 3 en tu sistema.
### Uso

Puedes utilizar este script mediante la línea de comandos de la siguiente manera:

```
python S4RiS.py --p [ruta al archivo S4RiS JSON] --n [nombre de la maratón] --e [secuencia a eliminar de los nombres] --f [tiempo a congelar el tablero]
```

Los siguientes son los argumentos que puedes utilizar con este script:

- **--p**: Ruta al archivo S4RiS JSON. Es un argumento obligatorio.
- **--n**: Nombre de la maratón. Este argumento es opcional y por defecto es "Maratón".
- **--e**: Secuencia de caracteres a eliminar de los nombres. Este argumento es opcional y por defecto es una cadena vacía.
- **--f**: Tiempo a congelar el tablero. Este argumento es opcional y por defecto es 240. Debe ser un valor entre 0 y 300.
