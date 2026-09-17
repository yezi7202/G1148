
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

## 1. Ajuda i comandos generals

```*text
:h paraula Obrir ajuda sobre una paraula/comando
:*saveas arxivo Guardar amb un altre nom
:*close Tancar finestra actual
:terminal Obrir terminal dins de *Vim
K Obrir el manual de la paraula sota el cursor
```

---

# 2. Moviment

## Moviment bàsic

```*text
h esquerra
j a baix
k arriba
l dreta
```

Pots afegir un número:

```*text
*4j baixar 4 línies
*3w avançar 3 paraules
```

## Per paraules

```*text
w inicio de la següent paraula
W següent paraula ignorant puntuació

e final de la paraula
E final de paraula ignorant puntuació

b inicio de paraula anterior
B paraula anterior ignorant puntuació

ge final de paraula anterior
```

## Dins d'una línia

```*text
0 inici de línia
^ primer caràcter que no sigui espai
$ final de línia
g_ últim caràcter que no sigui espai
```

## Dins de l'arxiu

```*text
*gg primera línia
G última línia

5G línia 5
*5gg línia 5
```

## Buscar caràcters en una línia

```*text
*fx anar al següent caràcter x
*Fx buscar x cap enrere

*tx anar just abans del següent x
*Tx equivalent cap enrere

; repetir cerca
, repetir en direcció contrària
```

## Blocs

```*text
} següent paràgraf/bloc
{ paràgraf/bloc anterior

% anar al parell corresponent
```

Per exemple:

```*text
( )
{ }
[ ]
```

## Moviment de pantalla

```*text
H parteix superior de pantalla
M centro
L parteix inferior

*zz centrar cursor en pantalla
*zt col·locar cursor a dalt
*zb col·locar cursor a baix
```

```*text
*Ctrl+f avançar una pantalla
*Ctrl+b retrocedir una pantalla

*Ctrl+d avançar mitja pantalla
*Ctrl+o retrocedir mitja pantalla
```

---

# 3. Mode *Insert

```*text
i inserir abans del cursor
I inserir al principi de línia

a inserir després del cursor
A inserir al final de línia

o crear línia sota
O crear línia damunt
```

Mentre escrius:

```*text
*Ctrl+h esborrar caràcter anterior
*Ctrl+w esborrar paraula anterior

*Ctrl+t augmentar sagnia
*Ctrl+d disminuir sagnia

*Ctrl+n següent opció d'autocompletat
*Ctrl+p opció anterior
```

Sortir de *Insert:

```*text
*Esc
```

---

# 4. Edició

## Reemplaçar

```*text
r reemplaçar un caràcter
R mode reemplaço
```

## Canviar

```*text
*cw canviar paraula
*ciw canviar paraula completa

*cc canviar línia completa

C canviar fins a final de línia
c$ igual que C
```

`c` significa canviar: elimina el contingut seleccionat i entra en mode *Insert.

## Unir línies

```*text
J unir línia següent amb l'actual
```

## Majúscules/minúscules

```*text
*gu convertir a minúscules
*gU convertir a majúscules
~ alternar majúscula/minúscula
```

## Desfer

```*text
o desfer
*Ctrl+r refer

. repetir última operació
```

---

# 5. Seleccionar text

## Mode Visual

```*text
*v seleccionar caràcters
V seleccionar línies completes
*Ctrl+*v seleccionar bloc/columnes
```

Després pots moure't normalment:

```*text
h j k l
w b
$ 0
```

Sortir:

```*text
*Esc
```

## Seleccions útils

```*text
*aw paraula + espai
*iw paraula solament

*ab contingut amb ()
*ib interior de ()

*aB contingut amb {}
*iB interior de {}

*at etiqueta <>
*it interior d'etiqueta
```

---

# 6. Què fer amb una selecció

Després de seleccionar:

```*text
i copiar
d esborrar/tallar

> augmentar sagnia
< disminuir sagnia

o minúscules
O majúscules
~ alternar majúscules/minúscules
```

---

# 7. Copiar, tallar i pegar

En *Vim, copiar es diu ***yank**.

## Copiar

```*text
*yy copiar línia
*2yy copiar 2 línies

*yw copiar des de cursor fins a següent paraula
*yiw copiar paraula completa

i$ copiar fins a final de línia
```

## Pegar

```*text
p pegar
P pegar en la posició oposada
```

## Tallar/esborrar

```*text
*dd tallar línia
*2dd tallar 2 línies

*dw esborrar fins a següent paraula
*diw esborrar paraula completa
*daw esborrar paraula + espai

D esborrar fins a final de línia
d$ igual que D

x esborrar caràcter
```

---

# 8. Registres i portapapers

Veure registres:

```*text
:*registers
```

Guardar text en un registre:

```*text
"ai
```

Pegar registre:

```*text
"*ap
```

## Portapapers del sistema

Copiar:

```*text
"+i
```

Pegar:

```*text
"+p
```

Molt útil per a copiar entre **dues instàncies distintes de *Vim**.

Registres interessants:

```*text
" últim *yank/*delete
0 última copia
+ portapapers del sistema
% nomeni de l'arxiu actual
/ última cerca
: últim comando
. últim text inserit
```

---

# 9. Buscar

Buscar cap endavant:

```*text
/text
```

Buscar cap enrere:

```*text
?text
```

Després:

```*text
n següent resultat
N resultat anterior
```

Llevar ressaltat:

```*text
:*noh
```

---

# 10. Buscar i reemplaçar

Canviar primera coincidència de la línia:

```*text
:s/vell/nou/
```

Totes en la línia:

```*text
:s/vell/nou/g
```

Totes en l'arxiu:

```*text
:%s/vell/nou/g
```

Preguntar abans de reemplaçar:

```*text
:%s/vell/nou/*gc
```

---

# 11. Sagnia

```*text
>> moure línia a la dreta
<< moure línia a l'esquerra
```

*Reindentar línia:

```*text
==
```

*Reindentar 3 línies:

```*text
3==
```

*Reindentar bloc:

```*text
=%
```

*Reindentar tot l'arxiu:

```*text
*gg=G
```

Molt útil en programar en C.

---

# 12. Guardar i sortir

```*text
:w guardar

:q sortir

:*wq guardar i sortir
:x guardar i sortir
*ZZ guardar i sortir

:q! sortir sense guardar
*ZQ sortir sense guardar
```

Guardar tots els arxius i sortir:

```*text
:*wqa
```

---

# 13. Treballar amb diversos arxius

Obrir un altre arxiu:

```*text
:e arxivo.c
```

Si no existeix, pots crear-ho:

```*text
:e nou.c
```

i després:

```*text
:w
```

## *Buffers

```*text
:*ls mostrar arxius/*buffers oberts

:*bn següent *buffer
:*bp *buffer anterior

:*bd tancar *buffer
```

---

# 14. Dividir la pantalla

Horitzontal:

```*text
:*split arxiu.c
```

o:

```*text
:*sp arxiu.c
```

Vertical:

```*text
:*vsplit arxiu.c
```

o:

```*text
:*vs arxiu.c
```

Canviar entre finestres:

```*text
*Ctrl+w w
```

Moure's directament:

```*text
*Ctrl+w h esquerra
*Ctrl+w l dreta
*Ctrl+w j a baix
*Ctrl+w k a dalt
```

Tancar finestra:

```*text
*Ctrl+w q
```

---

# 15. Pestanyes

Obrir:

```*text
:*tabnew arxiu.c
```

Canviar:

```*text
*gt pestanya següent
*gT pestanya anterior
```

Anar a una concreta:

```*text
*2gt
```

Tancar:

```*text
:*tabclose
```

---

# 16. Marques

Guardar una posició:

```*text
dt.
```

Això crea la marca `a`.

Tornar:

```*text
`a
```

Veure marques:

```*text
:*marks
```

Llesta de salts:

```*text
:*jumps
```

Moure's entre posicions anteriors:

```*text
*Ctrl+o posició anterior
*Ctrl+i posició següent
```

---

# 17. *Macros

Gravar una macro en `a`:

```*text
*qa
```

Realitzes les operacions.

Detenir:

```*text
q
```

Executar:

```*text
@a
```

Repetir última macro:

```*text
@@
```

---

# 18. Comandos especialment útils programant en C

```*text
% saltar entre (), [] o {}

*ciw canviar paraula

*diw esborrar paraula

*dd esborrar línia

*yy copiar línia

p pegar

>> augmentar sagnia

<< disminuir sagnia

*gg=G formatar/*reindentar arxivo

/text buscar

n següent coincidència

* buscar paraula sota el cursor
```

---

# 19. Els comandos que hauries de memoritzar primer

```*text
i
*Esc

h j k l

w
b

0
$

*gg
G

*dd
*dw
*diw

*yy
p

o
*Ctrl+r

*v
V

/text
n

:w
:q
:*wq
:q!

:e arxivo

"+i
"+p
```

## Idea fonamental de *Vim

*Vim funciona molt mitjançant:

```*text
operador + moviment
```

Per exemple:

```*text
d + w = *dw
```

Esborrar fins a la següent paraula.

```*text
d + $ = d$
```

Esborrar fins a final de línia.

```*text
i + w = *yw
```

Copiar fins a la següent paraula.

I pots afegir quantitats:

```*text
*3dd esborrar 3 línies
*5j baixar 5 línies
*2w avançar 2 paraules
*4yy copiar 4 línies
```