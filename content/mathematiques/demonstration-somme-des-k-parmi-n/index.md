---
title: "Démonstration : Somme des k parmi n"
slug: "demonstration-somme-des-k-parmi-n"
date: "2020-08-07"
categories: 
  - "mathematiques"
tags: 
  - "combinaison"
  - "demonstration"
description: "Cet article présente 2 démonstrations de l'égalité : somme des k parmi n = 2^k (2 puissance k). La première se servant de la formule du binôme, la deuxième se servant de la définition de l'ensembles des parties de E."
---
## Définition :

La somme des combinaisons de k=0 à n de k parmi n est égale à 2 à la puissance n.

$$\sum_{k=0}^n {n \choose k}= 2^n$$

## Démonstrations :

### Démonstration 1 :

Cette première démonstration est la plus rapide et directe. Elle s'appuiera sur la formule du binôme de Newton :

$\sum_{k=0}^n {n \choose k} x^{k} y^{n-k}=(x+y)^n$

Si nous prenons $x=1$ et $y=1$, alors obtenons l'égalité :

$\sum_{k=0}^n {n \choose k } 1^k1^{n-k}=(1+1)^n$

Ce qui nous donne :

$\sum_{k=0}^n {n \choose k}= 2^n$

### Démonstration 2 :

Cette deuxième démonstration s'appuie sur la définition exprimant le cardinal de l'ensemble des parties d'un ensemble quelconque comme étant égal à 2 à la puissance du cardinal de l'ensemble.

Soit un ensemble E de cardinal n, alors l'ensemble ayant pour éléments tous les sous-ensembles de E est appelé ensemble des parties de E, noté $\mathcal{P}(E)$.

**Par exemple :** 

Soit $E=\\{a,b,c\\}$, alors :
$n = \#E = 3$ et $\mathcal{P}(E)=\\\{\emptyset,\\\{a\\\},\\\{b\\\},\\\{c\\\},\\\{a,b\\\},\\\{a,c\\\},\\\{b,c\\\},\\\{a,b,c\\\}\\\}$.

L'ensemble des parties est constitué **par définition** d'1 partie à 0 élément, de n parties à 1 élément et ainsi de $ n \choose k$ parties à $k$ éléments...

Le cardinal de l'ensemble des parties est donc égal à $ \sum_{k=0}^n {n \choose k}$.

Or selon de [nombreuses démonstrations](https://fr.wikipedia.org/wiki/Ensemble_des_parties_d%27un_ensemble), on peut dire que $\#\mathcal{P}(E)=2^{\#E}$.

Nous retrouvons bien notre égalité de départ.
