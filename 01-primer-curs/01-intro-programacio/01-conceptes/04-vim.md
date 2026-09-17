
vim "fitxer" (crear un fitxer en vim desde consola)

Modes de *vim:
- Normal: mode amb què inicia vim, no permet escriure text ja que s'interpreta les tecles com a ordres. S'usa la *tecla ESC* per a entrar en el mode normal.
- Inserir: mode que permet escriure text, s'entra mitjançant la **tecla i**.

```c
#*include <stdio.h> // *bliblioteca estàndard per a comandos d'entrada i sortida

*int *main(*void) { // funció on C comença a executar el programa, en aquest cas retorna un nombre enter (*int) i no rep cap paràmetre (*void).

	*printf("Hola món\n") // "\n" és una nova línia (com en *cpp)
	*return 0; // els *camandos acaben en ;, retornem un 0 per a dir a l'ordinador que el nostre programa ha executat de manera correcta


} // les instruccions comencen i acaben en claus
 
```

comando de compilació (crear fitxer objecte):

```
*gcc -*std=*c17 -*Wall -*Wextra -*pedantic -c *hello.c
```

-std=c17 (estàndard de C que inclou correccions i ampli suport en compiladors, verisión estable).
-Wall (advertiments habituals de compilació)
-Wextra (advertiments addicionals)
-pedantic (comprovar que el programa segueix estrictament els estàndards)
-c "arxiu" (compilar)

"arxiu" -o "programa" (enllaçar o compilar + enllaçar els fitxers objecto, per a crear el programa executable)