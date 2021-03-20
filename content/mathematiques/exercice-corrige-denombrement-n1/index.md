---
title: "Exercice corrigé - Dénombrement n°1"
slug: "exercice-corrige-denombrement-n1"
date: "2020-09-15"
categories: 
  - "denombrement"
tags: 
  - "crible"
  - "ensemble"
  - "loi-de-morgan"
description: "Exercice corrigé de dénombrement n°1. "
---Difficulté : Moyenne

## Liste d'exercice :

**(En cours)**

## Énoncé : Une histoire de pigeon

A Central Parc, il y a 250 oiseaux à 3 couleurs. Parmi eux se trouvent :

1. 68 oiseaux possédant des plumes magentas et blanches
2. 133 oiseaux possédant des plumes blanches
3. 192 oiseaux ne possédant pas de plumes blanches ou ne possédant pas de plumes vertes
4. 213 oiseaux possédant des plumes magentas ou vertes

Seuls les pigeons sont verts, magentas et blancs, **pouvez vous les dénombrer ?**

## Aide :



Pensez à la formule du crible de Poincaré puis aux lois de De Morgan !

Si vous ne les avez pas en tête, vous pouvez toujours essayer de faire un schéma :

![upload.wikimedia.org/wikipedia/commons/4/42/Inc...](https://upload.wikimedia.org/wikipedia/commons/4/42/Inclusion-exclusion.svg)

Source : [https://fr.wikipedia.org/wiki/Principe_d%27inclusion-exclusion](https://fr.wikipedia.org/wiki/Principe_d%27inclusion-exclusion)

## Correction :

On peut commencer par traduire les événements :

- V : "Oiseaux possédant des plumes vertes"
- B : "Oiseaux possédant des plumes blanches"
- M : "Oiseaux possédant des plumes magenta"

Ainsi, l'univers $\Omega = V\cup B \cup M$.

Nous avons 

1. $\#(M\cap B)=140$
2. $\#B=23$
3. $\#(\overline{B}\cup\overline{V})=75$
4. $\#(M\cup V)=32$

Selon la formule du crible de Poincaré

$$\#(M\cup V \cup B) = \#M + \#V + \#B - \#(M\cap V) - \#(M\cap B) - \#(V \cap B) + \#(M \cap V \cap B)$$

$$\#(M\cap V \cap B) = \#(M \cup V \cup B) - \#M - \#V - \#B + \#(M\cap V) + \#(M\cap B) + \#(V \cap B)$$

En utilisant une fois de plus la formule de Poincaré et une fois une loi de De Morgan

$$= \#\Omega - \#M - \#V - \#B + (\#M + \#V - \#(M\cup V)) + \#(M\cap B) + (\#\Omega - \#(\overline{V}\cup \overline{B}))$$

$$= 2 \times \#\Omega - \#B - \#(M\cup V)+ \#(M\cap B) - \#(\overline{V}\cup \overline{B})$$

Ainsi 

$$=500 - 133 - 213 + 68 - 192 = 30$$

Il y a donc dans Central Park **30 pigeons.**
