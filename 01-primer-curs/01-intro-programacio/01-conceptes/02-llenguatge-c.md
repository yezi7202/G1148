
## Funcions

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

## Programar en mòduls

Mantenir un únic fitxer és útil només si es tracta d'un programa petit, ja que a mesura que el programa s'esdevé més gran, implica major complexitat per localitzar funcions i mantenir el codi organitzat.

Separar el programa en mòduls soluciona aquests problemes, ja que agrupa les funcions d'un tipus en un mateix fitxer, tenim diversos avantatges:
- Manteniment de codi facilitat
- Divisió de programa per treballar per separat.
- Reduir la responsabilitat d'un únic fitxer.
- Llegibilitat més neta.
- Reutilització de codi.
- ...

Generalment, un programa es divideix en els següents mòduls:

| Fitxer                    | Funció                                                                                                            |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Fitxer capçelera (.h)     | Declara un o més funcions disponibles.                                                                            |
| Fitxer implementació (.c) | Implementa les funcions declares al fitxer capçelera.                                                             |
| Fitxer main (.c)          | Conté la funció principal del programa, on cridem les funcions que hem declarat i implementat als altres fitxers. |

### Fitxer capçelera (.h)

Per tal d'evitar que un fitxer de capçelera sigui processat més d'una vegada fem servir  `#indef` `#define` `#endif` com a guarda d'inclusió (include guard).

```
#ifndef SALUTACIO_H // si la funció no està definida
#define SALUTACIO_H // definir la funció

void salutar(void); // declarem la funció (diem que existeix)

#endif // ignora el contingut si la funció ja està definit, evitant la redefinició
```

En aquest cas, el nom que li posem a la guarda d'inclusió sol ser la mateixa que el nom del fitxer per evitar confusions. Permet lletres, números i ( _ ). 

### Implementació del fitxer capçelera

Ara hem de crear un fitxer d'implementació per definir el codi de la funció declarada:

```
#include <stdio.h>
#include "salutacio.h" // fitxer de capçelera que conté la declaració de la funció

void saludar(void){
	printf("Hola, món!\n");
}
```

Quan fem servir fitxers de capçelera estàndars o bé instalats pel sistema, fem servir `<>` amb `#include` en comptes de les cometes si es tracten de fitxers capçelera propis del projecte (com és aquest cas).

### Programa principal

Finalment, escrivim el fitxer main:

```c
#include <stdio.h>
#include "salutacio.h"

int main(void){
	saludar();
	return 0;
}
```







