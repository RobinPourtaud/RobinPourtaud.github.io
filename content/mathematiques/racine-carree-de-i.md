---
title: "Racine carrée de i"
slug: "racine-carree-de-i"
date: "2020-11-18"
categories: 
  - "mathematiques"
tags: 
  - "analyse-complexe"
  - "cercle-trigonometrique"
description: "Cet article présente un moyen d'évaluer la racine carrée de i très simplement. Seules des connaissances de base sur les nombres complexes et de la trigonométrie sont nécessaires."
---

## La méthode :

Soit {{< latex "z=\sqrt{i}" >}}.

1. On réécrit z :

{{< latex "z=i^{\frac{1}{2}}" >}}

Cherchons à écrire i en écriture exponentielle :

Nous savons que {{< latex "e^{i \theta}=cos(\theta)+i sin(\theta)" >}}. Pour obtenir i, il faut donc que {{< latex "cos(\theta)" >}} et {{< latex "sin(\theta)" >}} soit respectivement égaux à 0 et 1.

![](images/image-1024x239.png)

Source : Cercle Trigonométrique - Wikipédia

En utilisant ce tableau, nous pouvons voir qu'un angle de {{< latex "\frac{\pi}{2}" >}} serait parfait ! (Utiliser un cercle trigonométrique ou partir de la forme algébrique aurait également été possible pour trouver la forme exponentielle de i).

Cependant, il ne faut pas oublier que cosinus et sinus sont des fonctions périodiques, de période {{< latex "2 \pi" >}}.

Ce qui nous donne {{< latex "\forall k \in \mathbb{N}" >}} : {{< latex "cos(\frac{\pi}{2}+2k\pi) + i \times sin(\frac{\pi}{2} + 2k\pi) = e^{i \frac{\pi}{2} + 2k\pi} = i" >}}.

Nous pouvons reprendre. En remplaçant i de z, nous avons donc :

{{< latex "z=i^{\frac{1}{2}} = (e^{i \frac{\pi}{2} + 2k\pi})^\frac{1}{2}" >}}.

Nous pouvons déjà voir qu'en factorisant par 1/2 dans l'exponentielle, et en utilisant une propriété des puissances, nous pouvons obtenir :

{{< latex "z=(e^{i \frac{\pi}{2} + 2k\pi})^\frac{1}{2}=(e^{\frac{1}{2}(i \pi + 4k\pi)})^\frac{1}{2} = (e^{i \pi + 4k\pi})^\frac{1}{4}) = \sqrt\[4\]{-1}" >}}

On peut y voir une récurrence... Mais on peut trouver mieux, essayons autre chose !

{{< latex "z=e^{i\frac{\pi}{4}+ k\pi}" >}}. Avoir "{{< latex "k\pi" >}}" implique qu'on aura 2 solutions. Si vous avez un doute, regardez un [cercle trigonométrique](https://fr.wikipedia.org/wiki/Cercle_trigonom%C3%A9trique).

{{< latex "z=e^{i\frac{\pi}{4}+ k\pi}=cos(\frac{\pi}{4}+ k\pi)+i sin(\frac{\pi}{4}+ k\pi)" >}}.

Nous avons donc enfin :

{{< latex "\frac{\sqrt{2}}{2}+ i \frac{\sqrt{2}}{2}" >}} ou {{< latex "-\frac{\sqrt{2}}{2}- i \frac{\sqrt{2}}{2}" >}}.

Ou si vous préférez, en multipliant par {{< latex "\sqrt{2}" >}} :

{{< latex "\frac{1}{\sqrt{2}}+ i \frac{1}{\sqrt{2}}" >}} ou {{< latex "-\frac{1}{\sqrt{2}}- i \frac{1}{\sqrt{2}}" >}}.



## Une autre méthode :

Vous pouvez trouver un autre moyen de parvenir à la réponse en suivant cette vidéo de Blackpenredpen ici :

https://www.youtube.com/watch?v=Z49hXoN4KWg

## Sources :

1. [Logarithme Complexe - Wikipédia](https://fr.wikipedia.org/wiki/Logarithme_complexe)
2. [Sqrt(i) - Wolfram Alpha](https://www.wolframalpha.com/input/?i=sqrt%28i%29+)
3. [Ln(-1) - Wolfram Alpha](https://www.wolframalpha.com/input/?i=ln%28-1%29+)
4. [Cercle Trigonométrique - Wikipédia](https://fr.wikipedia.org/wiki/Cercle_trigonom%C3%A9trique)
