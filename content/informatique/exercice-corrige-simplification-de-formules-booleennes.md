---
title: "Exercice corrigé : Simplification de formules Booléennes"
slug: "exercice-corrige-simplification-de-formules-booleennes"
date: "2020-11-24"
categories: 
  - "informatique"
  - "mathematiques"
tags: 
  - "logique"
no: ""
---

A travers cet exercice, nous allons vous montrer comment simplifier une expression logique booléenne algébriquement, autrement dit sans avoir recours à un tableau de Karnaugh ou à la méthode de Quine. Pour pouvoir simplifier ces formules, vous devez avoir en tête un ensemble de propriétés sur les opérateurs logiques en plus du théorème de Morgan (que vous pouvez trouver facilement sur cette page : [L'algèbre de Boole](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_de_Boole_(logique))).

## Exercices :

Simplifiez au maximum ces formules logiques algébriquement :

### Formule 1



{{< latex "ABC+\overline{A}+\overline{C}" >}}

### Formule 2

{{< latex "\overline{A}B+C\overline{A}D+\overline{B}+\overline{D}" >}}

### Formule 3

{{< latex "\overline{\overline{A+D}.\overline{\overline{C}+\overline{B}}+C}" >}}

### Formule 4

{{< latex "(A+\overline{AB}+C\overline{AB})(A+B\overline{A}+\overline{B})" >}}

### Formule 5

{{< latex "A\overline{C} + AB\overline{C}+B\overline{C}+\overline{A}B" >}}

## Indices :

### Formule 1

Il faut utiliser 2 fois la propriété : {{< latex "\overline{A}+AB = \overline{A}+B" >}}.

### Formule 2

Il faut utiliser 2 fois la propriété {{< latex "\overline{A}+AB = \overline{A}+B" >}}.

Une fois {{< latex "A + AB = A(1+B) = A" >}}.

### Formule 3

Ce développement a pour but de vous faire réviser le théorème de Morgan. Appliquez le en boucle. A un moment, vous devriez vous en sortir.

### Formule 4

Un triple développement n'est pas nécessaire !

### Formule 5

Vous avez quelque chose de trop ? Utilisez la propriété {{< latex "A+\overline{A}=1" >}}.

## Correction :

### Formule 1

{{< latex "\overline{A}+B+\overline{C}" >}}

### Formule 2

{{< latex "\overline{A}+\overline{B}+\overline{D}" >}}

### Formule 3

{{< latex "C" >}}

### Formule 4

1

### Formule 5

{{< latex "A\overline{C}+\overline{A}B" >}}
