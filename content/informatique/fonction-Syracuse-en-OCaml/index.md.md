
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
La fonction syracuse en elle-même ne comporte aucun piège. Notez que j'utilise un "match" ici. Une conditionnel "if-else" aurait très bien pu faire l'affaire.
```ocaml
let rec syracuse n = 
	match n with 
	1 -> 1
	| n when n mod 2 = 0 -> syracuse(n/2)
	| _ -> syracuse (3*n+1)
```
Conformément à la conjecture, cette fonction retourne à priori toujours la valeur 1 : 
```ocaml
syracuse 54;;
- : int = 1
```
### Calcul du temps de vol
### Calcul du temps de vol en altitude
### Calcul de l'altitude maximale
### Affichage de la suite 




<!--stackedit_data:
eyJoaXN0b3J5IjpbNjU3ODUzMjU0XX0=
-->