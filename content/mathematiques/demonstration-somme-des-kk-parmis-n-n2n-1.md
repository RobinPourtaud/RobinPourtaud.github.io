---
title: "Démonstration : Somme des k(k parmi n)"
slug: "demonstration-somme-des-kk-parmis-n-n2n-1"
date: "2020-04-23"
categories: 
  - "mathematiques"
tags: 
  - "coefficients-binomiaux"
  - "demonstration"
  - "somme"
no: ""
---

Cet article présente la démonstration de : _la somme des k fois k parmi n = n fois 2 puissance (n moins 1)_.

## Identité :

\[latexpage\]

Une des célèbres formules utilisant les coefficients binomiaux est la suivante :

$\\quicklatex{size=24} \\sum^n\_{k=1} k\\binom{n}{k} = n \\times 2^{n-1}$

## Démonstration :

1. On commence par reprendre la formule du binôme de Newton :

$\\quicklatex{size=24}\\sum^n\_{k=1} \\binom{n}{k}a^{k}b^{n-k}=(a+b)^n$

2. Soit $b = 1$, alors :

$\\quicklatex{size=24}\\sum^n\_{k=1} \\binom{n}{k}a^{k} = (a+1)^n$

3. Dérivons l'équation selon $a$ comme ceci :

$\\quicklatex{size=24}\\frac{d}{da}(\\sum^n\_{k=1} \\binom{n}{k}a^{k} = (a+1)^n)$

4. Ce qui donne :

$\\quicklatex{size=24}\\sum^n\_{k=1} \\binom{n}{k}ka^{k-1} = n(a+1)^{n-1}$

5. Nous pouvons maintenant prendre $a = 1$ et retrouver l'équation :

$\\quicklatex{size=24}\\sum^n\_{k=1} k\\binom{n}{k} = n \\times 2^{n-1}$

## D'autres identités ici :

[Coefficient binomial - Wikipédia](https://fr.wikipedia.org/wiki/Coefficient_binomial)

## Une autre démonstration ?

[Démonstration : Somme des k parmi n](https://keskec.fr/sciences/mathematiques/robin/4073/)

[L’intégrale de x^i dx](https://keskec.fr/sciences/mathematiques/robin/220/)
