---
title: "Pourquoi 0!=1 ?"
slug: "pourquoi-01"
date: "2020-08-16"
categories: 
  - "mathematiques"
tags: 
  - "denombrement"
no: ""
---

3 factoriel est égal à 1\*2\*3; 2 factoriel est égal à 2\*1; 1 factoriel est égal à 1. En suivant cette logique, pourquoi 0 factoriel ne serait pas égal à rien, soit 0 ? C'est ce qu'on va essayer de comprendre à travers cet article.

## Définition : "Factoriel"



En dénombrement, le factoriel d'un entier naturel "n" est égal au produit des entiers naturels appartenant à {{< latex "\]0;n\]" >}}. Autrement dit :

{{< latex "\quicklatex{size=20} n! = \prod^n_{i=1} i = 1 \times 2 \times \ldots \times (n-1) \times n" >}}

## Pourquoi 0! est égal à 1 ?

### Depuis la définition du factoriel

Repartons de la définition :

{{< latex "\quicklatex{size=20}n! = 1 \times \ldots \times (n-1) \times n!" >}}

Autrement dit {{< latex "n! = n \times (n-1)!" >}}. Cependant, si on prend {{< latex "n = 0" >}}, nous obtenons l'égalité {{< latex " 0! = 0 \times (-1)!" >}}. Le factoriel de -1 étant indéfini...

Néanmoins :

{{< latex "\quicklatex{size=20}n! = n \times (n-1)! \equiv (n-1)! = \frac{n!}{n}" >}}.

Pour {{< latex "n = 1" >}}, alors :

{{< latex "\quicklatex{size=20} (1-1) ! = \frac{1!}{1} = 0! = 1" >}}

### Depuis la fonction Gamma

 On sait que :

{{< latex "\quicklatex{size=20}\forall n \in \mathbb{N}^\* : \Gamma(n) = (n–1)!=\int_0^{+\infty} t^{n-1} \times e^{-t}dt" >}}

Ce qui nous donne :

{{< latex "\quicklatex{size=20}0! = (1-1)! = \Gamma(1) = \int_0^{+\infty} t^{1-1} e^{-t} dt" >}}

Ou tout simplement : {{< latex "\quicklatex{size=20} \int_0^{+\infty}e^{-t}dt" >}}.

La primitive de {{< latex "e^{-t}" >}} est {{< latex "-e^{-t}" >}}.

Ainsi :

{{< latex "\quicklatex{size=20}0! = (\lim_{t\to\infty} -e^{-t}) - (-e^0) = 0 + 1 = 1" >}}.

### Depuis la définition des permutations d'un ensemble

En pratique, on peut utiliser le factoriel pour, par exemple, calculer le nombre de permutations d'un ensemble :

Si un ensemble {{< latex "E = \{0,1\}" >}}, alors cet ensemble peut être permuté {{< latex "\#E" >}} fois (2 fois).

L'ensemble des permutations est donc : {{< latex "\{(0,1),(1,0)\}" >}}.

Si un ensemble {{< latex "E = \{0,1,2\}" >}}, alors cet ensemble peut être permuté 6 fois :

 Son ensemble de permutations étant {{< latex "\{(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)\}" >}}.

Donc, si un ensemble {{< latex "E = \emptyset " >}}, alors son cardinal est 0 et peut être permuté 1 fois. "Il existe une seule possibilité pour permuter 0 élément".

L'ensemble de ses permutations étant {{< latex "\{\emptyset\}" >}}.

## Sources

1. [Fonction Gamma](http://serge.mehl.free.fr/anx/gamma.html)
2. [Permutation - Wikipédia](https://fr.wikipedia.org/wiki/Permutation)
3. [Fonction Gamma - maths-france.fr](https://www.maths-france.fr/MathSpe/GrandsClassiquesDeConcours/Integration/Gamma.pdf)
