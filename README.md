# traffic_analyzer
## Analizador de Tráfico.

### REQUERIMIENTOS DE USO
- Para empezar autilizar el programa, es necesario contar con Python 3 o una versión superior.
- Para el uso efectivo de la aplicación, es necesario utilizar ésta como super usuario. (Utilizar sudo o desde root)
- La aplicación, de momento ha sido probada únicamente con sistemas operativos basados en Debian. Para utilizar en Windows, es necesario cambiar una constante de la biblioteca de sockets utilizada en la línea 34 de main.py.

### INSTRUCCIONES
#### Para correr el programa
- Estando en un sistema operativo basado en Debian, es necesario utilizar el comando `sudo python3 main.py` desde la terminal, si no se encuentra utilizando el sistema como el usuario root. Dado el caso, no es necesario incluir `sudo`.
- Insertar la contraseña del super usuario. (De ser necesario)
#### Utilizar el programa
- El programa preguntará si desea iniciar la captura, usted responderá con "S" para iniciar la captura, de lo contrario, insertar "N". El programa terminará su ejecución en el segundo caso.
- Seguido, verá los resultados del tráfico de red que pasen por su sistema.
#### Salir del programa
- Cuando desee que el programa pare, puede interrumpirlo con `Ctrl + C`, así el programa responderá con una salida deseada.

### TO-DO LIST:
- [x] Crear base para expander programa.
- [x] Crear documentación de programa.
- [ ] Crear una forma de filtrar la salida del programa. (Mediante banderas de entrada, probablemente)
- [ ] Crear una forma de monitoreo extenso. Esto puede hacerse temporalmente dirigiendo la salida al STDOUT del programa con `>>nombre_archivo.txt` e insertando "S" al iniciar el programa.
