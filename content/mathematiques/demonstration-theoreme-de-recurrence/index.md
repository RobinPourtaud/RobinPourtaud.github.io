---
title: "Démonstration - Théorème de récurrence"
slug: "demonstration-theoreme-de-recurrence"
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

Soit $\mathbb{N}$ muni de son ordre usuel. 
Soit $A(n)$ une assertion définie $\forall n \in \mathbb{N}$ et vérifiant : 
- $A(n_0)$ vraie
- $\forall n \geq n_0$, $A(n)$ vraie $\Rightarrow A(n+1)$ vraie.

Alors $\forall n \geq n_0$, $A(n)$ vraie.

## Démonstration

Montrons ce théorème par l'absurde.

Soit $P \subseteq \mathbb{N}$ tel que $P = \{n\in (\mathbb{N},\leq _\mathbb{N}) \;| \; A(n) \,\text{vraie}\}$. 
**Montrons que** $P = \mathbb{N}$ : 
> Montrer que $P = \mathbb{N}$ reviens à montrer que A(n) est vrai pour tout n ! Son complémentaire dans $\mathbb{N}$ doit être vide ! Par l'absurde, supposons que son complémentaire ne l'est pas : 

Supposons que $\bar{P}^\mathbb{N} \neq \emptyset$ ($\bar{P}^\mathbb{N}$ est le complémentaire de $P$ dans $\mathbb{N}$).

Alors il existe un plus petit élément $p \in \bar{P}^\mathbb{N}$. 

Comme $n_0 \in P$, nécessairement, $n_0 \notin \bar{P}^\mathbb{N}$, donc $p\geq 1 + n_0$.

> Si $1 + n_0$ vous perturbe, replacez $n_0$ par 0, cela devrait vous aider. 

>Il était important de vérifier que $p-1 \geq n_0$ pour savoir si $p-1 \in \mathbb{N}$.

$p$ étant défini comme le plus petit élément de $\bar{P}^\mathbb{N}$, $p - 1 \notin \bar{P}^\mathbb{N}$ donc $p-1 \in P$. 

Nous pouvons donc dire que $A(p-1)$ est vraie. 
Par l'ordre usuel sur $\mathbb{N}$, $A(p)$ l'est aussi.

Nous ne pouvons avoir $p\in P$ et $p \in \bar{P}^\mathbb{N}$ : **Contradiction**

Nous avons donc bien $P = \mathbb{N}$ et donc le théorème de récurrence !  