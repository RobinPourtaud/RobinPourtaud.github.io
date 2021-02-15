---
title: "Récursivité terminale"
date: "2021-01-16"
categories: 
    - "Informatique"
tags: 
    - "factoriel"
description: ""
sources: 
    - ""
draft: "true"
---

## Définition
En informatique, une fonction f est dite récursive terminale 

Toute fonction récursive terminale peut être réécrit avec une boucle for (standard). Cependant toute fonction récursive non terminale n'est pas forcément réécrivable avec une boucle for, la fonction de ackermann en est un parfait exemple.
La fonction d'ackermann est malgrè réécrivable itérativement ! Avec une boucle while...

## Intéret
Dans de nombreux langages de programmation comme Python, c/c++, Ocaml ou même PHP, les fonctions présentant un caractère récursif terminale sont éxécuté comme une boucle itérative, ce qui permet de réduire le risque de "Stack Overflow". 

Pour en savoir plus : 
## Exemple

Pour illustrer la notion de terminalité, je vais vous présenter l'exemple classique de la fonction factoriel (en python). 

### Factoriel Récursif non terminale

Naivemant, nous pouvons implémenter récursivement la fonction factoriel de cette facon : 

```python
def fact(res):
    if res != 0: 
        return res * fact(res-1)
```
### Factoriel Récursif terminale

Pour transformer la fonction factoriel non terminale en terminale, la méthode usuele serait de rajouter un compteur en paramètre de la fonction : 

```python
def fact(res, i): 
    if i!=1:
        return a
    else: 
        return fact(res*i,i-1)
```

### Factoriel Itératif

```python
def fact(n): 
    res = 1
    for i in range(2,n+1):
        res*=i
    return res
```