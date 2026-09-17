
La funció principal **main()** és on s'executa els comandos del programa. No obstant això, s'empra les **funcions**, que són conjunts d'instruccions per a fer tasques especifiques, que en aquest cas permeten avantatges com la reutilització de codi, resolució de problemes majors reduint la magnitud, evitar repetició de línies, facilitar la lectura, manteniment del programa, etc...

```c
#*include <stdio.h>

*void saludar(*void){
	*printf("Hola, món!\n");
}
```

Quan definim la funció *saludar()*, hem de seguir la següent estructura:
- Tipus de retorn: indiquem quin tipus de valor va retornar la nostra funció (enter, cadenes, etc...)
- Nom de funció: identificador amb el qual cridarem cada vegada que vulguem executar la funció, no pot contenir una altra cosa que no sigui lletres o ( __ ). 
- Tipus de paràmetre: el valor que rebrà la funció per a executar-se.
- Cos: dins de les claus on col·loquem les instruccions que realitzen aquesta funció.


