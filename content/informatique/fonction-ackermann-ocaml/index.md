---
title: "Fonction de Ackermann - Ocaml"
date: "2021-04-21"
categories: 
  - "informatique"
tags: 
  - "OCaml"
  - "Ackermann"
description: "La fonction d'Ackermann est une fonction primitive terminale. Le langage de programmation OCaml se plit donc bien à ce genre d'exercice. Cet article présente donc différentes façons d'implémenter la fonction de Ackermann en OCaml."
draft: false
---

## Définition 
Sans paraphraser Wikipédia ([page que vous pouvez retrouver ici](https://en.wikipedia.org/wiki/Ackermann_function)), je vous rappelle la définition récursive de la fonction de Ackermann $\forall m,n \in \mathbb{N}$ : 
- $A(0,n) = n+1$
- $A(m,0) = A(m-1,1)$
- $A(m,n)=A(m-1,A(m,n-1)$

## Implémentation en OCaml

Cet article étant destiné à un publique débutant en OCaml, je vous propose 3 façons d'implémenter la fonction d'Ackermann. 

### Première version
OCaml se prêtant bien aux fonctions récursives, l'implémentation de la fonction d'Ackermann est, à partir de la définition, plutôt directe : 

```ocaml
let rec ackermann = function
  | 0, n -> n + 1
  | m, 0 -> ackermann (m - 1, 1)
  | m, n -> ackermann (m - 1, ackermann (m, n - 1));;
```
```ocaml
ackermann (3,4);;
```
Avec $m=3$ et $n=4$, nous avons bien 127 pour résultat. 

### Deuxième version
Vous pouvez également obtenir un résultat très similaire en utilisant un **match**. 
```ocaml
let rec ackermann2 m n = 
  match m,n with
  | 0, n -> n + 1
  | m, 0 -> ackermann2 (m - 1) 1
  | m, n -> ackermann2 (m - 1) (ackermann2 (m) (n - 1));;
```
```ocaml
ackermann 3 4;;
```
Avec $m=3$ et $n=4$, nous avons bien 127 pour résultat. 

### Troisième version
Si vous préférer l'utilisation de if-then-else, je vous propose cette fonction : 
```ocaml
let rec ackermann3 m n =
  if m = 0 then (n+1)
  else
    (if n = 0 then ackermann3 (m-1) 1
     else ackermann3 (m-1) (ackermann3 m (n-1)));;
```
```ocaml
ackermann3 3 4;;
```
Avec $m=3$ et $n=4$, nous avons bien 127 pour résultat. 