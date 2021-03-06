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
description: "Cet article présente la démonstration de : la somme des k fois k parmi n = n fois 2 puissance (n moins 1)."
---
## Identité :

Une des célèbres formules utilisant les coefficients binomiaux est la suivante :

$$\sum^n_{k=1} k\binom{n}{k} = n \times 2^{n-1}$$

## Démonstration :

1. On commence par reprendre la formule du binôme de Newton :

$$\sum^n_{k=1} \binom{n}{k}a^{k}b^{n-k}=(a+b)^n$$

2. Soit $b = 1$, alors :

$$\sum^n_{k=1} \binom{n}{k}a^{k} = (a+1)^n$$

3. Dérivons l'équation selon $a$ comme ceci :

$$\frac{d}{da}(\sum^n_{k=1} \binom{n}{k}a^{k} = (a+1)^n)$$

4. Ce qui donne :

$$\sum^n_{k=1} \binom{n}{k}ka^{k-1} = n(a+1)^{n-1}$$

5. Nous pouvons maintenant prendre $a = 1$ et retrouver l'équation :

$$\sum^n_{k=1} k\binom{n}{k} = n \times 2^{n-1}$$

## D'autres identités ici :

- [Coefficient binomial - Wikipédia](https://fr.wikipedia.org/wiki/Coefficient_binomial)

## Une autre démonstration ?

- [Démonstration : Somme des k parmi n](/mathematiques/demonstration-somme-des-k-parmi-n)

- [L’intégrale de x^i dx](/mathematiques/integrale-de-xi-dx)
