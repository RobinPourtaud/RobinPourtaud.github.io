
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
>Tout au long de ce tutoriel, nous utiliserons une notation non conventionnel pour écrire nos fonctions lambda en OCaml. Toutes nos fonctions "lambda" débuterons par "_" (par exemple "_true").
## Logique en lambda calcul en OCaml
### Booléens
#### True
```ocaml
let _true = fun t f = t;;
```
#### False
```ocaml
let _false = fun t f = f;;
```
### Condition en OCaml

```ocaml
let _ifthenelse = fun b t f = b t f;;
```
### Portes logiques
#### Porte logique "NOT"
```ocaml
let not_ = fun a = _ifthenelse a false_ true_;;
```
#### Porte logique "AND"
```ocaml
let not_ = fun a = _ifthenelse a false_ true_;;
```
#### Porte logique "OR"
```ocaml
let not_ = fun a = _ifthenelse a false_ true_;;
```
## Couples
Afin de définir la fonction prédécesseur plus aisément, nous auront besoin de créer des couples de valeurs. 
### Création de la paire

### Accès à la première valeur
### Accès à la seconde valeur

##  Arithmétiques 
### Définition de zéro
```ocaml
let zero_ = fun a = ifthenelse_ a false_ true_;;
```

> Comme vous pouvez le constater, la définition du "zero" est analogue à la définition du "false"
### Fonction successeur 
### Addition
### Multiplication 
### Exponentiel
### Itération de Knuth



## Interface entre notre lambda calcul et OCaml
C'est pourquoi il est utile de définir 4 fonctions facilitant notre interaction avec nos autres fonctions. 
### Les entiers
#### "Nombre OCaml" vers "Nombre Lambda"
```ocaml 
let rec _ocamlToNumber n = if n = 0 then _zero else _succ (_ocamlToNumber (n-1));;
```
#### "Nombre Lambda" vers "Nombre OCaml"
```ocaml 
let  _numberToOcaml  c  = c succ 0 ;;
```
### Les booléens
#### "Booléens OCaml" vers "Booléens Lambda"
```ocaml 
let  _ocamlToBool (b  : bool) =  if b then _true else _false ;;
```
#### "Booléens Lambda" vers "Booléens OCaml"
```ocaml 
let _boolToOcaml (b = _ifthenelse b true false;;
```
## Exemple d'utilisation 

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg1MTkwMzc3XX0=
-->