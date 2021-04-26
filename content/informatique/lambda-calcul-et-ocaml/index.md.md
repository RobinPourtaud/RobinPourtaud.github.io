
---
title: "Lambda Calcul en OCaml"
date: "2020-08-24"
categories: 
  - "informatique"
tags: 
  - "Lambda Calcul"
  - "OCaml"
description: ""
---

## Logique en lambda calcul en OCaml
### Booléens
#### True
```ocaml
let true_ = fun v f = v;;
```
#### False
```ocaml
let false_ = fun v f = f;;
```
### Condition en OCaml

```ocaml
let ifthenelse_ = fun b v f = b v f;;
```
### Portes logiques
#### Porte logique "NOT"
```ocaml
let not_ = fun a = ifthenelse_ a false_ true_;;
```
#### Porte logique "AND"
```ocaml
let not_ = fun a = ifthenelse_ a false_ true_;;
```
#### Porte logique "OR"
```ocaml
let not_ = fun a = ifthenelse_ a false_ true_;;
```


##  Arithmétiques 
### Définition de zéro
```ocaml
let zero_ = fun a = ifthenelse_ a false_ true_;;
```
### Fonction successeur 
### Addition
### Multiplication 
### Exponentiel
### Itération de Knuth

## Interface entre notre lambda calcul et OCaml
### Les booléens
### Les entiers 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxODM4MTk3M119
-->