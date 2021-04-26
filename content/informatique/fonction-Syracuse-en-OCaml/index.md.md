
---
title: "Fonction Syracuse en Ocaml"
date: "2021-01-05"
categories: 
  - "informatique"
  - "mathematiques"
tags: 
  - "OCaml"
description: ""
---
## Définition de Syracuse
On définit la suite de syracuse récursivement $\forall n \in \mathbb{N}$ par : 
- $u_0=n$
- $\forall n \in \mathbb{N}^* : u_{n+1} = \begin{cases}\end{cases}$


## Implémentation en OCaml 
### La fonction
```ocaml
let rec syracuse n = 
	match n with 
	1 -> 1
	| n when n mod 2 = 0 -> syracuse 
```
### Calcul du temps de vol
### Calcul du temps de vol en altitude
### Calcul de l'altitude maximale
### Affichage de la suite 




<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ5ODQ3MTE4Nl19
-->