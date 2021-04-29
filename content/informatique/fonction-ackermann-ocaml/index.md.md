---
title: "Affichage textuelle en OCaml"
date: "2020-12-21"
categories: 
  - "informatique"
tags: 
  - "OCaml"
description: "Cet article présente différentes façons d'afficher du contenu dans la sortie standard en OCaml."
---

## Définition formelle

## Implémentation en OCaml

Cet article étant destiné à un publique débutant en OCaml, je vous propose 3 façons d'implémenter la fonction d'Ackermann en OCaml. 

### Première version
OCaml se prêtant bien à l'implémentation de fonction récursive, l'implémentation de la fonction d'Ackermann est plutôt directe : 
```ocaml
let rec ackermann = function
  | 0, n -> n + 1
  | m, 0 -> ackermann (m - 1, 1)
  | m, n -> ackermann (m - 1, ackermann (m, n - 1));;
```
### Deuxième version
Vous pouvez également obtenir un résultat très similaire en utilisant un **match**. 

```

### Troisième version
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI2MzA4NzIzLDEwMzMxOTc0ODksMjI4MT
c4NzBdfQ==
-->