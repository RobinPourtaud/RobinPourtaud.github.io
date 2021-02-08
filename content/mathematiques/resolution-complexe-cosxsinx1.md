---
title: "Résolution complexe : cos(x)sin(x)=1"
slug: "resolution-complexe-cosxsinx1"
date: "2020-07-07"
categories: 
  - "mathematiques"
tags: 
  - "analyse"
  - "analyse-complexe"
  - "trigonometrie"
no: ""
---

Cet article est un exercice avec solution présentant la solution réelle et complexe de cos(x)sin(x) = 1.

## Exercice :



Dans {{< latex "\mathbb{R}" >}} et dans {{< latex "\mathbb{C}" >}}, résoudre :

{{< latex "\cos x \sin x = 1" >}}

## Résolution :

### 1 - Recherche d'une solution dans R

Soit la formule de trigonométrie suivante :

{{< latex "2sin(x)cos(x)=sin(2x)" >}}

Alors :

{{< latex "sin(x)cos(x)=\frac{sin(2x)}{2}" >}}

Nous pouvons reprendre l'équation :

{{< latex "cos(x)sin(x)=1" >}}

Elle est donc équivalente à :

{{< latex "sin(2x) = 2" >}}

Comme {{< latex "\forall x \in \mathbb{R} & sin(x) \in \[0,1\]" >}}.

Cette équation n'admet donc pas de solution dans R.

### 2 - Introduction des formules d'Euler

Continuons dans {{< latex "\mathbb{C}" >}} :

Soit la formule d'Euler :

{{< latex "sin(\theta)=\frac{e^{i\theta}-e^{-i\theta}}{2i}" >}}

En effectuant le changement de variable {{< latex "\theta = 2x" >}}, nous nous retrouvons avec l'équation suivante :

{{< latex "\frac{e^{i2x}-e^{-i2x}}{2i} = 2" >}}

### 3 - Substitution

En multipliant le numérateur et le dénominateur par i, on a :

{{< latex "\frac{1}{2}ie^{-2ix}-\frac{1}{2}ie^{2ix}=2" >}}

{{< latex "\frac{1}{4\times \frac{-1}{2}ie^{2ix}}-\frac{1}{2}ie^{2ix}=2" >}}

Prenons maintenant {{< latex "y = \frac{-1}{2}ie^{2ix}" >}}.

Cela nous revient à résoudre le système :

\left\{ \begin{array}{rcr}  
\frac{-1}{2}ie^{2ix} & = & y \\  
\frac{1}{4y}+y & = &2 \\  
\end{array} \right.

### 4 - Recherche des solutions y

Soit :

{{< latex "\frac{1}{4y}+y = 2" >}}

En mettant sur le même dénominateur :

{{< latex "\frac{4y^2+1}{4y}=2" >}}

{{< latex "4y^2-8y+1=0" >}}

En utilisant les formule [du second degré](https://fr.wikipedia.org/wiki/%C3%89quation_du_second_degr%C3%A9). On trouve aisément que :

Son discriminant {{< latex "\Delta=64-16=48" >}}. Cette équation admet donc 2 solutions réelles :

{{< latex "y=1\pm\frac{\sqrt{3}}{2}" >}}

### 5 - Recherche de la première solution

Soit {{< latex "y=1 + \frac{\sqrt{3}}{2}" >}} :

En "dé-substituant" la variable y, nous nous retrouvons avec l'équation suivante :

{{< latex "\frac{-ie^{2ix}}{2}=1+\frac{\sqrt{3}}{2}" >}}

{{< latex "e^{2ix}=-\frac{2+\sqrt{3}}{i}" >}}

{{< latex "e^{2ix}=i(2+\sqrt{3})" >}}

Avec {{< latex "\forall k \in \mathbb{Z}" >}}, nos équations appartenant au plan complexe, nous avons donc **une infinité de solutions** :

{{< latex "e^{2ix+2ik\pi}=i(2+\sqrt{3})" >}}

{{< latex "2ix = ln(i(2+\sqrt{3})) - 2ik\pi" >}}

Le signe de {{< latex "2ik\pi" >}} n'a pas d'importance, k étant positif ou négatif. Ainsi nous obtenons **la première solution** :

{{< latex "x = \frac{ln(i(2+\sqrt{3}))}{2i} + k\pi" >}}

### 6 - Recherche de la deuxième solution

Soit {{< latex "y=1 - \frac{\sqrt{3}}{2}" >}} :

En dé-substituant la variable y, nous nous retrouvons avec l'équation suivante :

{{< latex "\frac{-ie^{2ix}}{2}=1-\frac{\sqrt{3}}{2}" >}}

{{< latex "e^{2ix}=-\frac{2-\sqrt{3}}{i}" >}}

{{< latex "e^{2ix}=i(2-\sqrt{3})" >}}

Avec {{< latex "\forall k \in \mathbb{Z}" >}}, nos équations appartenant au plan complexe, nous avons donc **une infinité de solutions** :

{{< latex "e^{2ix+2ik\pi}=i(2-\sqrt{3})" >}}

{{< latex "2ix = ln(i(2-\sqrt{3})) - 2ik\pi" >}}

Le signe de {{< latex "2ik\pi" >}} n'a pas d'importance, k étant positif ou négatif. Ainsi nous obtenons **la deuxième solution** :

{{< latex "x = \frac{ln(i(2-\sqrt{3}))}{2i} + k\pi" >}}
