---
title: "Démonstration - Théorème de Cantor"
date: "2021-04-20"
categories: 
  - "mathematiques"
tags: 
  - "Demonstration"
  - "Preuve"
description: "Cet article présente le théorème de Cantor ainsi que sa démonstration."
draft: true
---

## Définition

Soit $E$ un ensemble, il n'existe pas d'application bijective entre $E$ et $2^E$.

Cela implique ne nombreuses choses. Pour en savoir plus, [la page wikipédia](https://www.wikiwand.com/fr/Th%C3%A9or%C3%A8me_de_Cantor) sur le théorème de Cantor est très complète (paragraphe : "Conséquence du théorème"). 

## Démonstration 

Afin de démontrer cette propriété, raisonnons par l'absurde. 

Soit $ f : E \rightarrow 2^E$ une application bijective.

Posons $ X := \{e \in E : e \notin f(e) \}$.

> Autrement dit, $X$ est le sous-ensemble des éléments de E qui n'appartiennent pas à leur image par $f$. $f(x)$ est un sous-ensemble de $2^E$. 
>
> Nous cherchons à savoir ici si il existe ou non une sujection de $E$ sur $2^E$. Si $X$ n'a pas d'antécédent par $f$, alors $f$ (par définition), n'est pas sujective. 

Soit $y \in E$, alors $X = f(y)$. 

Nous avons 2 cas : 

- Si $y \in X$, alors, par définition de $X$, $y \notin f(y)$. Donc $y \notin X$, ce qui est contradictoire. 
- Si $y \notin X$, alors par définition de $X$, $y \in \bar{Z}^X$. Ainsi $y \in f(y)$, donc $y \in X$, ce qui est encore une fois contradictoire. 

Une telle application $f$ ne peut donc exister. Aucune fonction $f$ de $E$ dans $2^E$ n'est sujective donc bijective. D'où le théorème de Cantor. 

