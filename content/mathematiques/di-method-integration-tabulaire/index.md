---
title: "DI Method / Intégration tabulaire"
slug: "di-method-integration-tabulaire"
date: "2020-08-08"
categories: 
  - "mathematiques"
tags: 
  - "integrale"
description: "L' intégration par partie est une étape essentielle à la recherche de primitive. Il est facile de mal interpréter la formule, c'est pourquoi il existe une méthode appelée Intégration tabulaire (ou DI method) permettant d'éviter ce procédé classique et donc de s'épargner de nombreuses erreurs potentielles... Elle aurait été introduite dans le film 'Stand and Deliver' [1]."
---


Pour introduire la DI Method, nous nous servirons de 2 exemples :

## Exemple 1

On souhaite résoudre l'intégrale :

$$\int cos(x) x^2 dx$$

#### Création du tableau

Comme pour l'intégration par partie, nous choisissons quel facteur de l'intégrale nous souhaitons intégrer et quel facteur nous souhaitons dériver. Dans notre cas, nous dériverons $x^2$ et intégrerons $cos(x)$.

<table><tbody><tr><td><strong>Ligne</strong></td><td><strong>Signe</strong></td><td><strong>D</strong></td><td><strong>I</strong></td></tr><tr><td>1</td><td>+</td><td>$x^2$</td><td>$cos(x)$</td></tr><tr><td>2</td><td>-</td><td>$2x$</td><td>$sin(x)$</td></tr><tr><td>3</td><td>+</td><td>$2$</td><td>$-cos(x)$</td></tr><tr><td>4</td><td>-</td><td>$0$</td><td>$-sin(x)$</td></tr></tbody></table>

Tableau de la méthode d'intégration tabulaire

Dans la colonne signe, nous alternons le signe positif et négatif.

Dans la colonne D, nous dérivons ligne par ligne tant que le facteur reste différente de 0.

Dans la colonne I, nous intégrons l'expression ligne par ligne.

_**Note** : Il faut savoir qu'on peut continuer ou arrêter le tableau à la ligne que l'on souhaite. Cependant, dans notre cas, l'arrêter avant la fin laisserait une intégrale à évaluer, et continuer rajouterait des produits égaux à 0._

### Utilisation du tableau

Nous pouvons dès maintenant évaluer cette intégrale avec ce tableau.

Nous commençons par additionner pour toutes les lignes de 1 à 3 le produit de D avec le I de la ligne suivante, en multipliant chaque produit par le signe qui lui est associé.

Pour la dernière ligne, nous ajoutons l'intégrale du produit D - I multipliée par le signe.

_Autrement dit, nous dérivons en diagonale jusqu'à l'avant dernière ligne, puis on intègre la dernière ligne._

Cela nous donne directement la solution :

$$\int cos(x) x^2 dx = + (x^2 \times sin(x)) - (2x \times -cos(x)) + (2 \times -sin(x)) - (\int 0 \times -sin(x) dx)$$

Ce qui nous donne bien :

$$\int cos(x) x^2 dx = 2 \times cos(x) + (-2 + x^2) sin(x)$$

Vous pouvez retrouver la même chose sur [Wolfram Alpha](https://www.wolframalpha.com/input/?i=int+x%5E2+cosx+dx).

![Intégrale x^2 cosx dx - Wolfram Alpha](image-1024x366.png#t4)



## Exemple 2 

Dans un autre article, pour résoudre [l'intégrale de x à la puissance i](https://keskec.fr/sciences/mathematiques/robin/220/), j'ai dû effectuer une intégration par partie pour l'intégrale :

$$\int cos(u) e^u du$$

### Création du tableau

<table><tbody><tr><td>Ligne</td><td>Signe</td><td>D</td><td>I</td></tr><tr><td>1</td><td>+</td><td>$e^u$</td><td>$cos(u)$</td></tr><tr><td>2</td><td>-</td><td>$e^u$</td><td>$sin(u)$</td></tr><tr><td>3</td><td>+</td><td>$e^u$</td><td>$-cos(u)$</td></tr></tbody></table>

Comme nous pouvons le voir, la dérivé ne sera jamais égale à 0 contrairement à l'exemple 1. Dans ce cas là, nous pouvons nous arrêter si on arrive à une répétition :  
Nous avons $cos(u)$ en ligne 1 et 3.

### Utilisation du tableau

De façon analogue à l'exemple 1, nous avons :

$$\int cos (u) e^u = + (e^u \times sin(u)) - (e^u \times -cos(u)) + (\int e^u \times -cos(u))$$

En reformulant, nous avons :

$$2 \int cos u e^u = + (e^u \times sin(u)) - (e^u \times -cos(u))$$

$$\int cos u e^u = \frac{1}{2} \times e^u \times (sin(u)-cos(u))$$

Encore une fois, vous pouvez trouver le même résultat sur Wolfram Alpha.

![Intégrale cos u sin^u du - Wolfram Alpha](image-1-1024x354.png#t4)



## En vidéo

Si vous êtes à l'aise avec l'**anglais**, je ne peux que vous recommander la chaine de blackpenredpen. Il présente de manière concise et claire la méthode tabulaire.

{{< youtube "2I-_SV8cwsw" >}}

Intégration par partie - DI method en Anglais

## Sources :

1. [Intégration par parties - Integration by parts](https://fr.qwe.wiki/wiki/Integration_by_parts#Tabular_integration_by_parts)
2. [Tabular Integration Method sin(ln(x)) DI ou présentation tabulaire.](https://maths1024.blogspot.com/2017/12/tabular-integration-method-sinlnx-di-ou.html)
3. [integration by parts, DI method, VERY EASY - blackpenredpen - Youtube](https://www.youtube.com/watch?v=2I-_SV8cwsw)
