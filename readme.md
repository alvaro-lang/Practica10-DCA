# PRACTICA 10 DCA
[Enlace del repositorio](https://github.com/alvaro-lang/Practica10-DCA)

Calculadora de sumas, restas, multiplicaciones y divisiones hecha en python3.


## GIT BISECT:

He introducido un fallo en el commit '671fb6f7d0d184096edcbf13f71ef91c9018949c' con comentario 'cambiad comentarios del programa a español'. Este fallo era que cuando queriamos restar, en vez de restar hace una suma.

He comenzado con el siguiente comando el bisecting:
git bisect start
git bisect bad (indicamos que en el ultimo commit que estamos tenemos un bug)
git bisect good 3922e926e1c3a00faf681ebc8375026010da7d0b (indicamos el primer commit que hemos hecho en el repositorio)

Me aparece el siguiente mensaje:
Biseccionando: faltan 2 revisiones por probar después de esta (aproximadamente 2 pasos)
[671fb6f7d0d184096edcbf13f71ef91c9018949c] cambiad comentarios del programa a español

y comprobamos el programa con el comando de python: 'python3 Calculadora.py'. Me doy cuenta que aun persiste el fallo y le indico que el error aun sigue estando en este commit que me ha mandado por tanto escribo el comando:
git bisect bad.

Me muestra el siguiente mensaje:
Biseccionando: faltan 0 revisiones por probar después de esta (aproximadamente 1 paso)
[099a11723b8c7d716482d0eaa2bd0e743564b6c3] añadidos nuevos comentarios

y vuelvo a comprobar con python3 Calculadora.py

El error se ha solucionado, ahora si que funciona la resta, por tanto, le indico que este commit si que funciona con 'git bisect good' y me indica con el siguiente mensaje cual es el commit malo y toda la informacion.

671fb6f7d0d184096edcbf13f71ef91c9018949c is the first bad commit
commit 671fb6f7d0d184096edcbf13f71ef91c9018949c
Author: Alvaro Pastor <alvaropers96@gmail.com>
Date:   Mon Dec 19 16:09:45 2022 +0100

    cambiad comentarios del programa a español

 Calculadora.py | 19 ++++++++++---------
 1 file changed, 10 insertions(+), 9 deletions(-)

 
Para finalizar el bisecting, hago git bisect reset, con lo que, me devuelve el siguiente mensaje:

La posición previa de HEAD era 099a117 añadidos nuevos comentarios
Cambiado a rama 'master'
Tu rama está actualizada con 'origin/master'.

Observo cual es el error que he cometido en el commit '671fb6f7d0d184096edcbf13f71ef91c9018949c' que es el indicado por git bisect y lo arreglo haciendo un push a github.


## GIT HOOKS:

He añadido un archivo en .git/hooks llamado 'prepare-commit-msg.sh' que cuando se hace un commit, indica el nombre del usuario qe ha hecho ese commit.

He añadido tambien un archivo llamado 'pre-push.sh' que antes de hacer push se sube documentacion del push hehco
