
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
let not_ = fun v f = f;;
```
#### Porte logique "AND"
#### Porte logique "OR"



##  Arithmétiques 
### Définition de zéro
### Fonction successeur 
### Addition
### Multiplication 
### Exponentiel
### Itération de Knuth

## Interface entre notre lambda calcul et OCaml
### Les booléens
### Les entiers 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxMjA4NzMxMDRdfQ==
-->