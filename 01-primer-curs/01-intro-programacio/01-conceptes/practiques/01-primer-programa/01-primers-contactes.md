
La función principal *main()* es donde se ejecuta los comandos del programa. No obstante, se emplea las **funciones**, que son conjuntos de instrucciones para realizar tareas especificas, que en este caso permiten ventajas como la reutilización de código, resolución de problemas mayores reduciendo la magnitud, evitar repetición de líneas, facilitar la lectura, mantenimiento del programa, etc...

```c
#include <stdio.h>

void saludar(void){
	printf("Hola, mundo!\n");
}
```

Cuando definimos la función *saludar()*, tenemos que seguir la siguiente estructura:
- Tipo de retorno: indicamos qué tipo de valor va devolver nuestra función (entero, cadenas, etc...)
- Nombre de función: identificador con el cual vamos a llamar cada vez que queramos ejecutar la función, no puede contener otra cosa que no sea letras o ( __ ). 
- Tipo de parámetro: el valor que va a recibir la función para ejecutarse.
- Cuerpo: dentro de las llaves donde colocamos las instrucciones que realizan dicha función.
