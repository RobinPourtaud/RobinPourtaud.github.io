---
title: "Démonstration - Un ordre est bien fondé si et seulement si il est noethérien"
date: "2021-04-20"
categories: 
  - "mathematiques"
tags: 
  - "Demonstration"
  - "Preuve"
description: "Le raisonnement inductif est un classique des mathématiques, c'est pourquoi il est important de bien comprendre son fonctionnement pour ensuite bien l'appliquer. Cet article présente la démonstration du théorème de récurrence par l'absurde."
draft: True
---

## Définition 

### Ordre bien fondé 

Un ordre est dit bien fondé (BF) si toutes parties non vide admet au moins un élément minimal.


### Ordre noethérien

Un ordre est dit noethérien (No) si il ne possède pas de chaine infini décroissante.

## Propriété 

Un ordre est bien fondé si et seulement si il est noethérien. 

## Démonstration

Montrons que $BF \equiv No$.

### Bien fondé implique Noethérien

Par contraposé, nous avons $\bar{No}\Rightarrow \Bar{BF}$.
Soit $P = (V(P),\leq_p)$ un ordre non noethérien.
$\exist C \in 2^{V(p)}$ une chaine infini strictement décroissante dans P. 

$\forall x \in C, \exist y \in C$ tel que $y <_p x$. Comme $C$ est infini, $C \neq \emptyset$.
Or C ne peut posseder d'élément minimal. 

Donc $P$ est n'est pas bien fondé. 
Donc par contraposé ($BF\Rightarrow No$).

### Noethérien implique bien fondé

Par contraposé, nous avons $\bar{BF}\Rightarrow \Bar{No}$.

Soit $P$ un ordre n'étant bien bien fondé.
$\exist A \in 2^V(p)$ tel que A \neq \emptyset
