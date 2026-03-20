## ENUNCIADO
Puede leer el enunciado de esta tarea en el archivo [enunciado.md](enunciado.md)

## SOLUCIÓN
### Casos de prueba
Los casos de prueba se pueden acceder en la carpeta `src/` que se encuentra en este directorio.

Los casos de prueba están escritos para Python 3.14.

Se puede usar el comando `uv sync` dentro de la carpeta `src/` para sincronizar el entorno virtual con este proyecto.

### Qué áreas podemos eliminar

System Imports:
- En general, no se permitirá importar paquetes descargados de repositorios o de internet, solo importar paquetes locales

Circular Imports:
- Los Circular Imports regulares causan error, entonces solo se podrán usar dentro de funciones como en los casos de prueba.

Modules:
- Una vez que un módulo se importa, las funcoines de este no se podrán asignar al namespace local si no se hizo a través de la línea de import. Es decir, no se podrá usar "nombre_local = modulo.funcion".
- No se podrá usar la función dir()

Packages:
- No se podrá hacer imports desde el mismo paquete "from . import ___"

Argumentos de función:
- No se podrá hacer automatic casting de variables. Es decir, si la función tiene usa el parámetro param para print(), no se podrá enviar un entero en param() sin hacerle casting antes.