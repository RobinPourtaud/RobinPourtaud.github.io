---
title: "Pourquoi 0!=1 ?"
slug: "pourquoi-01"
date: "2020-08-16"
categories: 
  - "mathematiques"
tags: 
  - "denombrement"
description: "3 factoriel est égal à 1*2*3; 2 factoriel est égal à 2*1; 1 factoriel est égal à 1. En suivant cette logique, pourquoi 0 factoriel ne serait pas égal à rien, soit 0 ? C'est ce qu'on va essayer de comprendre à travers cet article."
---

## Définition : "Factoriel"



En dénombrement, le factoriel d'un entier naturel "n" est égal au produit des entiers naturels appartenant à $\]0;n\]$. Autrement dit :

$ n! = \prod^n_{i=1} i = 1 \times 2 \times \ldots \times (n-1) \times n$

## Pourquoi 0! est égal à 1 ?

### Depuis la définition du factoriel

Repartons de la définition :

$n! = 1 \times \ldots \times (n-1) \times n!$

Autrement dit $n! = n \times (n-1)!$. Cependant, si on prend $n = 0$, nous obtenons l'égalité $ 0! = 0 \times (-1)!$. Le factoriel de -1 étant indéfini...

Néanmoins :

$n! = n \times (n-1)! \equiv (n-1)! = \frac{n!}{n}$.

Pour $n = 1$, alors :

$ (1-1) ! = \frac{1!}{1} = 0! = 1$

### Depuis la fonction Gamma

 On sait que :

$\forall n \in \mathbb{N}^\* : \Gamma(n) = (n–1)!=\int_0^{+\infty} t^{n-1} \times e^{-t}dt$

Ce qui nous donne :

$0! = (1-1)! = \Gamma(1) = \int_0^{+\infty} t^{1-1} e^{-t} dt$

Ou tout simplement : $ \int_0^{+\infty}e^{-t}dt$.

La primitive de $e^{-t}$ est $-e^{-t}$.

Ainsi :

$0! = (\lim_{t\to\infty} -e^{-t}) - (-e^0) = 0 + 1 = 1$.

### Depuis la définition des permutations d'un ensemble

En pratique, on peut utiliser le factoriel pour, par exemple, calculer le nombre de permutations d'un ensemble :

Si un ensemble $E = \{0,1\}$, alors cet ensemble peut être permuté $\#E$ fois (2 fois).

L'ensemble des permutations est donc : $\{(0,1),(1,0)\}$.

Si un ensemble $E = \{0,1,2\}$, alors cet ensemble peut être permuté 6 fois :

 Son ensemble de permutations étant $\{(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)\}$.

Donc, si un ensemble $E = \emptyset $, alors son cardinal est 0 et peut être permuté 1 fois. "Il existe une seule possibilité pour permuter 0 élément".

L'ensemble de ses permutations étant $\{\emptyset\}$.

## Sources

1. [Fonction Gamma](http://serge.mehl.free.fr/anx/gamma.html)
2. [Permutation - Wikipédia](https://fr.wikipedia.org/wiki/Permutation)
3. [Fonction Gamma - maths-france.fr](https://www.maths-france.fr/MathSpe/GrandsClassiquesDeConcours/Integration/Gamma.pdf)
