---
title: "Convertir un entier non signé décimal en Binaire"
slug: "convertir-un-entier-non-signe-decimal-en-binaire"
date: "2020-04-15"
categories: 
  - "informatique"
  - "mathematiques"
tags: 
  - "binaire"
  - "conversion"
description: "Tous les systèmes informatiques actuels fonctionnent en binaire. Très grossièrement, on pourrait considérer que 0 représente un courant éteint et 1 un courant allumé. Ainsi, il est nécessaire de comprendre le fonctionnement de la représentation binaire pour pouvoir représenter des chiffres dans la mémoire d'un ordinateur."
---
> Le **système binaire** est le [système de numération](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_num%C3%A9ration) utilisant la [base](https://fr.wikipedia.org/wiki/Base_(arithm%C3%A9tique)) [2](https://fr.wikipedia.org/wiki/2_(nombre)). On nomme couramment [bit](https://fr.wikipedia.org/wiki/Bit) (de l'[anglais](https://fr.wikipedia.org/wiki/Anglais) _binary digit_, soit « chiffre binaire ») les [chiffres](https://fr.wikipedia.org/wiki/Chiffre) de la numération binaire positionnelle. Un bit peut prendre deux valeurs, notées par convention [0](https://fr.wikipedia.org/wiki/0_(chiffre)) et [1](https://fr.wikipedia.org/wiki/1_(nombre)).
> 
> [fr.wikipiedia.org](https://fr.wikipedia.org/wiki/Syst%C3%A8me_binaire)

Tous les systèmes informatiques actuels fonctionnent en binaire. Très grossièrement, on pourrait considérer que 0 représente un courant "éteint" et 1 un courant "allumé".

Ainsi, il est nécessaire de comprendre le fonctionnement de la représentation binaire pour pouvoir représenter des chiffres dans la mémoire d'un ordinateur.

## La représentation binaire:

Tout d'abord, il faut bien comprendre ce qu'est le système le plus courant, le système décimal.



Un nombre, 7803 par exemple peut être décomposé comme ceci:

$$7803_{10}=7\times1000+8\times100+0\times10+3\times1$$

Autrement dit: $7803_{10}=7\times10^3+8\times10^2+0\times10^1+3\times10^0$

Un nombre binaire sera donc décomposé de la même façon, mais avec une base de 2 et non de 10.

## Conversion Binaire-Décimal:

Prenons un nombre binaire assez grand et décomposons-le:

$$1011011101_2=1\times2^9+0\times2^8+1\times2^7+1\times2^6+0\times2^5+1\times2^4+1\times2^3+1\times2^2+0\times2^1+1\times2^0$$

Ainsi:

$$1011011101_2=512+128+64+16+8+4+1= 733_{10}$$

Voilà :). Vous pouvez maintenant essayer de convertir le nombre $10000101100010_2$ en binaire (solution: 8546).

## Conversion Décimal-Binaire:

Prenons le nombre 733, solution de la section précédente.

La méthode la plus connue pour convertir un nombre décimal en nombre binaire est la suivante:

733 = 2 \* 366 + 1

386 = 2 \* 183 + 0

183 = 2 \* 91 + 1

90 = 2 \* 45 + 1

45 = 2 \* 22 + 1

22 = 2 \* 11 + 0

11 = 2 \* 5 + 1

5 = 2 \* 2 + 1

2 = 2 \* 1 + 0

1 = 2 \* 0 + 1

Maintenant: prenez le reste de chaque opération de bas en haut. Ce qui donne:

$$733_10 =1011011101_2$$
