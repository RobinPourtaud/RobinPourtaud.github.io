---
title: "Convertir un nombre décimal en Float"
slug: "keske-cest-convertir-un-nombre-decimal-en-float"
date: "2020-04-12"
categories: 
  - "informatique"
  - "mathematiques"
tags: 
  - "binaire"
  - "conversion"
  - "float"
  - "float32"
no: ""
---

La **virgule flottante** (float) est une méthode d'écriture de [nombres réels](https://fr.wikipedia.org/wiki/Nombre_r%C3%A9el) fréquemment utilisée dans les [ordinateurs](https://fr.wikipedia.org/wiki/Ordinateur). (Wikipédia)

En mémoire, un nombre peut être codé par de nombreux schémas différents:

- int (entier sur 16 bits en c++)
- uint64\_t (entier sur 64 bits en c++)
- float32 (réel sur 32 bits)
- float64 (réel sur 64 bits)
- .....

## Nécessaire :

Pour suivre ce tutoriel, vous devez savoir convertir des entiers décimaux en binaires. Si jamais vous avez un doute, vous pouvez checker mon article sur cette conversion :

[Convertir un entier non signé décimal en Binaire](https://keskec.fr/sciences/informatique/robin/267/)

## Rappel :

\[latexpage\]

Un nombre réel peut s'écrire avec une notation appelé notation scientifique. Par exemple: $74632 = 7.4632 \\times 10^4$

## Représentation en Virgule flottante :

_Pour réduire la difficulté de cet exercice, les exemples utilisés et expliqués seront en float32 et non en float64._

Un float32 est composé de 3 parties: une partie signe, une partie exposant et une partie mantisse:

![Float example.svg](images/2880px-Float_example.svg.png)

Nombre en Virgule flottante

1. Le signe est représenté sur 1 bit (0 pour un nombre positif, 1 pour un nombre négatif).
2. L'exposant est représenté sur 8 bits.
3. La mantisse est représenté sur 23 bits (fraction sur le schéma ci-dessus).

## Exemple: -12,4375 en float32 :

### Conversion de 12 en binaire :

$12\_{10}=1100\_2$

Si vous ne savez pas comment faire, retournez sur mon précédent article [(ici)](https://keskec.fr/index.php/2020/04/12/convertir-un-entier-non-signe-decimal-en-binaire/).

### Conversion de 0.4375 en binaire :

La méthode pour ce calcul est la suivante :

$0.4375 \\times 2 = 0 + 0.875$

$0.875 \\times 2 = 1 + 0.75$

$0.75 \\times 2 = 1 + 0.5$

$0.5 \\times 2 = 1 + 0$

On choisis de s'arrêter là car le reste est égale à 0.

Maintenant, en lisant de haut en bas, nous pouvons voir que $0.4375 = 0.0111$.

### Déplacez la virgule :

$12.4375{10}$ donne $1100.0111\_{2}$.

Pour une représentation en float32, nous devons représenter ce nombre en écriture scientifique :

$1100.0111 = 1.1000111 \\times 10^3$

Pour calculer la mantisse, il suffit de relever la partie décimal et de la compléter avec 0 pour avoir 23 bits).

On sait maintenant que la mantisse est égale à $10001110000000000000000$.

### Calcul de l’exposant :

On sait que [le biais est de 127 pour un float32.](https://en.wikipedia.org/wiki/Exponent_bias)

$1.1000111 \\times 10^3$ a pour exposant $3$.

Ainsi, l’exposant biaisé est $127 + 3$, ce qui est égale à $130\_{10}=10000010\_2$.

### Signe:

\-12,4375 étant un nombre négatif, ainsi, son bit de signe sera 1.

### Résultat:

En regroupant le tout (dans l'ordre Signe\-Exposant\-Mantisse).

La représentation float32 de -12,4375 est donc:

11000001010001110000000000000000
