## Notes

vim "fichero" (crear un fichero en vim)

Modos de vim:
- Normal: modo con el que inicia vim, no permite escribir texto ya que se interpreta las teclas como órdenes. Se usa la **tecla ESC** para entrar en el modo normal.
- Insertar: modo que permite escribir texto, se entra mediante la **tecla i**.

```c
#include <stdio.h> // bliblioteca estándar para comandos de entrada y salida

int main(void) { // función donde C empieza a ejecutar el programa, en este caso devuelve un número entero (int) y no recibe ningún parámetro (void).

	printf("Hola mundo\n") // "\n" es una nueva línea (como en cpp)
	return 0; // los camandos terminan en ;, devolvemos un 0 para decir al ordenador que nuestro programa ha ejecutado de forma correcta


} // las instrucciones empiezan y terminan en llaves
 
```

comando de compilación (crear fichero objeto):

```
gcc -std=c17 -Wall -Wextra -pedantic -c hello.c
```

-std=c17 (estándar de C que incluye correcciones y amplio soporte en compiladores, verisión estable).
-Wall (advertencias habituales de compilación)
-Wextra (advertencias adicionales)
-pedantic (comprobar que el programa sigue estrictamente los estándares)
-c "archivo" (compilar)

"archivo" -o "programa" (enlazar o compilar + enlazar los ficheros objecto, para crear el programa ejecutable)
## 1. Ayuda y comandos generales

```text
:h palabra        Abrir ayuda sobre una palabra/comando
:saveas archivo   Guardar con otro nombre
:close            Cerrar ventana actual
:terminal         Abrir terminal dentro de Vim
K                 Abrir el manual de la palabra bajo el cursor
```

---

# 2. Movimiento

## Movimiento básico

```text
h        izquierda
j        abajo
k        arriba
l        derecha
```

Puedes añadir un número:

```text
4j       bajar 4 líneas
3w       avanzar 3 palabras
```

## Por palabras

```text
w        inicio de la siguiente palabra
W        siguiente palabra ignorando puntuación

e        final de la palabra
E        final de palabra ignorando puntuación

b        inicio de palabra anterior
B        palabra anterior ignorando puntuación

ge       final de palabra anterior
```

## Dentro de una línea

```text
0        inicio de línea
^        primer carácter que no sea espacio
$        final de línea
g_       último carácter que no sea espacio
```

## Dentro del archivo

```text
gg       primera línea
G        última línea

5G       línea 5
5gg      línea 5
```

## Buscar caracteres en una línea

```text
fx       ir al siguiente carácter x
Fx       buscar x hacia atrás

tx       ir justo antes del siguiente x
Tx       equivalente hacia atrás

;        repetir búsqueda
,        repetir en dirección contraria
```

## Bloques

```text
}        siguiente párrafo/bloque
{        párrafo/bloque anterior

%        ir al par correspondiente
```

Por ejemplo:

```text
( )
{ }
[ ]
```

## Movimiento de pantalla

```text
H        parte superior de pantalla
M        centro
L        parte inferior

zz       centrar cursor en pantalla
zt       colocar cursor arriba
zb       colocar cursor abajo
```

```text
Ctrl+f   avanzar una pantalla
Ctrl+b   retroceder una pantalla

Ctrl+d   avanzar media pantalla
Ctrl+u   retroceder media pantalla
```

---

# 3. Modo Insert

```text
i        insertar antes del cursor
I        insertar al principio de línea

a        insertar después del cursor
A        insertar al final de línea

o        crear línea debajo
O        crear línea encima
```

Mientras escribes:

```text
Ctrl+h   borrar carácter anterior
Ctrl+w   borrar palabra anterior

Ctrl+t   aumentar sangría
Ctrl+d   disminuir sangría

Ctrl+n   siguiente opción de autocompletado
Ctrl+p   opción anterior
```

Salir de Insert:

```text
Esc
```

---

# 4. Edición

## Reemplazar

```text
r        reemplazar un carácter
R        modo reemplazo
```

## Cambiar

```text
cw       cambiar palabra
ciw      cambiar palabra completa

cc       cambiar línea completa

C        cambiar hasta final de línea
c$       igual que C
```

`c` significa cambiar: elimina el contenido seleccionado y entra en modo Insert.

## Unir líneas

```text
J        unir línea siguiente con la actual
```

## Mayúsculas/minúsculas

```text
gu       convertir a minúsculas
gU       convertir a mayúsculas
~        alternar mayúscula/minúscula
```

## Deshacer

```text
u        deshacer
Ctrl+r   rehacer

.        repetir última operación
```

---

# 5. Seleccionar texto

## Modo Visual

```text
v        seleccionar caracteres
V        seleccionar líneas completas
Ctrl+v   seleccionar bloque/columnas
```

Después puedes moverte normalmente:

```text
h j k l
w b
$ 0
```

Salir:

```text
Esc
```

## Selecciones útiles

```text
aw       palabra + espacio
iw       palabra solamente

ab       contenido con ()
ib       interior de ()

aB       contenido con {}
iB       interior de {}

at       etiqueta <>
it       interior de etiqueta
```

---

# 6. Qué hacer con una selección

Después de seleccionar:

```text
y        copiar
d        borrar/cortar

>        aumentar sangría
<        disminuir sangría

u        minúsculas
U        mayúsculas
~        alternar mayúsculas/minúsculas
```

---

# 7. Copiar, cortar y pegar

En Vim, copiar se llama **yank**.

## Copiar

```text
yy       copiar línea
2yy      copiar 2 líneas

yw       copiar desde cursor hasta siguiente palabra
yiw      copiar palabra completa

y$       copiar hasta final de línea
```

## Pegar

```text
p        pegar
P        pegar en la posición opuesta
```

## Cortar/borrar

```text
dd       cortar línea
2dd      cortar 2 líneas

dw       borrar hasta siguiente palabra
diw      borrar palabra completa
daw      borrar palabra + espacio

D        borrar hasta final de línea
d$       igual que D

x        borrar carácter
```

---

# 8. Registros y portapapeles

Ver registros:

```text
:registers
```

Guardar texto en un registro:

```text
"ay
```

Pegar registro:

```text
"ap
```

## Portapapeles del sistema

Copiar:

```text
"+y
```

Pegar:

```text
"+p
```

Muy útil para copiar entre **dos instancias distintas de Vim**.

Registros interesantes:

```text
"        último yank/delete
0        última copia
+        portapapeles del sistema
%        nombre del archivo actual
/        última búsqueda
:        último comando
.        último texto insertado
```

---

# 9. Buscar

Buscar hacia delante:

```text
/texto
```

Buscar hacia atrás:

```text
?texto
```

Después:

```text
n        siguiente resultado
N        resultado anterior
```

Quitar resaltado:

```text
:noh
```

---

# 10. Buscar y reemplazar

Cambiar primera coincidencia de la línea:

```text
:s/viejo/nuevo/
```

Todas en la línea:

```text
:s/viejo/nuevo/g
```

Todas en el archivo:

```text
:%s/viejo/nuevo/g
```

Preguntar antes de reemplazar:

```text
:%s/viejo/nuevo/gc
```

---

# 11. Sangría

```text
>>       mover línea a la derecha
<<       mover línea a la izquierda
```

Reindentar línea:

```text
==
```

Reindentar 3 líneas:

```text
3==
```

Reindentar bloque:

```text
=%
```

Reindentar todo el archivo:

```text
gg=G
```

Muy útil al programar en C.

---

# 12. Guardar y salir

```text
:w       guardar

:q       salir

:wq      guardar y salir
:x       guardar y salir
ZZ       guardar y salir

:q!      salir sin guardar
ZQ       salir sin guardar
```

Guardar todos los archivos y salir:

```text
:wqa
```

---

# 13. Trabajar con varios archivos

Abrir otro archivo:

```text
:e archivo.c
```

Si no existe, puedes crearlo:

```text
:e nuevo.c
```

y luego:

```text
:w
```

## Buffers

```text
:ls       mostrar archivos/buffers abiertos

:bn       siguiente buffer
:bp       buffer anterior

:bd       cerrar buffer
```

---

# 14. Dividir la pantalla

Horizontal:

```text
:split archivo.c
```

o:

```text
:sp archivo.c
```

Vertical:

```text
:vsplit archivo.c
```

o:

```text
:vs archivo.c
```

Cambiar entre ventanas:

```text
Ctrl+w w
```

Moverse directamente:

```text
Ctrl+w h     izquierda
Ctrl+w l     derecha
Ctrl+w j     abajo
Ctrl+w k     arriba
```

Cerrar ventana:

```text
Ctrl+w q
```

---

# 15. Pestañas

Abrir:

```text
:tabnew archivo.c
```

Cambiar:

```text
gt       pestaña siguiente
gT       pestaña anterior
```

Ir a una concreta:

```text
2gt
```

Cerrar:

```text
:tabclose
```

---

# 16. Marcas

Guardar una posición:

```text
ma
```

Esto crea la marca `a`.

Volver:

```text
`a
```

Ver marcas:

```text
:marks
```

Lista de saltos:

```text
:jumps
```

Moverse entre posiciones anteriores:

```text
Ctrl+o   posición anterior
Ctrl+i   posición siguiente
```

---

# 17. Macros

Grabar una macro en `a`:

```text
qa
```

Realizas las operaciones.

Detener:

```text
q
```

Ejecutar:

```text
@a
```

Repetir última macro:

```text
@@
```

---

# 18. Comandos especialmente útiles programando en C

```text
%        saltar entre (), [] o {}

ciw      cambiar palabra

diw      borrar palabra

dd       borrar línea

yy       copiar línea

p        pegar

>>       aumentar sangría

<<       disminuir sangría

gg=G     formatear/reindentar archivo

/texto   buscar

n        siguiente coincidencia

*        buscar palabra bajo el cursor
```

---

# 19. Los comandos que deberías memorizar primero

```text
i
Esc

h j k l

w
b

0
$

gg
G

dd
dw
diw

yy
p

u
Ctrl+r

v
V

/texto
n

:w
:q
:wq
:q!

:e archivo

"+y
"+p
```

## Idea fundamental de Vim

Vim funciona mucho mediante:

```text
operador + movimiento
```

Por ejemplo:

```text
d + w   = dw
```

Borrar hasta la siguiente palabra.

```text
d + $   = d$
```

Borrar hasta final de línea.

```text
y + w   = yw
```

Copiar hasta la siguiente palabra.

Y puedes añadir cantidades:

```text
3dd      borrar 3 líneas
5j       bajar 5 líneas
2w       avanzar 2 palabras
4yy      copiar 4 líneas
```


