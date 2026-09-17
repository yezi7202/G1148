![[00-conceptes-basics.pdf]]

Un programa d'ordinador sorgeix de la necessitat de resoldre problemes concrets. La seva definició es pot dividir entre 2 conceptes:

**1. Conjunt d'instruccions i dades (informació) que poden ser executades per un ordinador de forma ordenada en temps, per tal de resoldre problemes.**

**2. Una successió d'estats definits pels valors que prenen d'unes dades.**

```cpp
int x = 2;
x = x + 2;
x = x * 2;
```

Ara bé, sovint podem confondre un programa amb un algorisme:

- Algorisme: és la idea o **pla abstracte** (conjunt de pasos lògics) de com resoldre un problema, mitjançant un **llenguatge algorítmic** (informal).
- Programa: és la **implementació d'un o diversos algorismes**, mitjançant un **llenguatge de programació**.

Un llenguatge de programació és una **llengua formal** (que segueix unes normes de sintaxi) per poder escriure programes d'ordinador, el qual l'interpreta i executa.

Paradigmes de programació: formes (filosofies) d'estructurar, conceptualitzar i escriure codi.
- Imperatiu i declaratiu. 
	- Llenguatges funcionals
	- Llenguatges orientats a objecte (OO)
	- Llenguatges lògics
	- ...

Les etapes generals de desenvolupament es poden classificar en 4 blocs:

1. Anàlisi i disseny: és important entendre el problema que s'ens planteja per tal de dissenyar una solució adequada, un codi font com a resultat.
2. Traducció i compilació: el codi font és transformat a una representació entesa per l'ordinador (llenguatge de baix nivell, binari), un codi objecte o equivalent.
3. Enllaçat: en cas que hi hagi més codis objectes, s'enllaçen aquestes per crear un programa executable (la qual podem córrer al nostre ordinador).
4. Execució, proves i depuració: és el procés on provem l'executable i fem les correccions adients per tal de resoldre els errors de codi (bugs). També poden sorgir noves versions amb noves implementacions i manteniment del nostre programa.

















