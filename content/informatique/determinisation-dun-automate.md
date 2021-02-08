---
title: "Déterminisation d'un automate"
slug: "determinisation-dun-automate"
date: "2020-12-30"
categories: 
  - "informatique"
tags: 
  - "automate"
no: ""
---

Cet article présente une méthode afin de convertir un automate fini non déterministe quelconque (AFN) en automate déterministe (AFD). Afin d'illustrer cette méthode, un exercice corrigé sera utilisé comme support. Les étapes de l'algorithme de conversion seront explicitées de façon tabulaire.

## Définition :

Un automate est dit déterministe s'il respecte trois conditions :

1. Il possède un unique état initial.
2. Il ne possède pas d’epsilon-transitions.
3. Pour chaque état de cet automate, il existe au maximum une transition issue de cet état possédant le même symbole.

Pour en savoir plus : [Différents types d’automates finis](https://keskec.fr/sciences/informatique/robin/4870/)

## Méthode :

![](images/image-18-1024x602.png)

Automate fini non déterministe

La méthode permettant de passer d'un automate fini quelconque à un automate déterministe va être illustrée par l'exercice corrigé suivant :

Soit, un automate fini X sur l'alphabet {a,b} (le mot vide étant lambda) :

Calculons l'automate déterministe Y équivalent à X par la méthode des sous-ensembles d'états.

### Étape 1 : Construction du tableau

Soit le tableau à 4 entrées suivant :

<table class="has-fixed-layout"><tbody><tr><td><strong>Nouvel état</strong></td><td><strong>Nouvel état initial, final ou non</strong></td><td><strong>a</strong></td><td>b</td></tr></tbody></table>

Colonnes du tableau

1. "Nouvel état" correspond au futur état de notre automate déterministe.
2. "Nouvel état initial, final ou non" correspond au type de l'état de notre automate déterministe.
3. Le reste des colonnes correspond aux symboles des transitions partant de ce nouvel état. Il y a autant de colonnes que le cardinal de l'alphabet de l'automate.

Commençons avec la première ligne :

<table class="has-fixed-layout"><tbody><tr><td><strong>Nouvel état</strong></td><td><strong>Nouvel état initial, final ou non</strong></td><td><strong>a</strong></td><td><strong>b</strong></td></tr><tr><td>A={q0, q1}</td><td>Initial</td><td>{q0,q1} = A</td><td>{q2,q4} = B</td></tr><tr><td>B={q2,q4}</td><td></td><td></td><td></td></tr></tbody></table>

Colonnes du tableau

NB : Les noms des nouveaux états sont purement arbitraires.

#### 1) Recherche de l'état initial :

L'état initial de X est q0. Une epsilon-transition de q0 vers q1 nous permet de réunir q0 et q1.

#### 2) Initial ? Final ?

q0 est l'état initial de X, alors A contenant q0 le sera aussi. (c'est l'unique état initial)

A ne contient pas d'état final, il ne le sera donc pas lui-même.

#### 3) Transitions ?

A partir de q0 ou de q1, il existe 2 transitions "a" se dirigeant vers q0, q1. Cet état existe. On s'arrête.

A partir de q0 ou de q1, il existe une transition "b" se dirigeant vers q2. Cet état n'existe pas, créons-le.

#### 4) Répétons les étapes

A partir de ces nouveaux états, recommencer depuis l'étape 2 jusqu'à ce qu'il n'y ait plus de nouveaux états à être créés:

#### Résultat :

<table><tbody><tr><td><strong>Nouvel état</strong></td><td><strong>Nouvel état initial, final ou non</strong></td><td><strong>a</strong></td><td><strong>b</strong></td></tr><tr><td>A={q0, q1}</td><td>Initial</td><td>{q0,q1} = A</td><td>{q2,q4} = B</td></tr><tr><td>B={q2,q4}</td><td>non</td><td>{q1,q5,q7} = C</td><td><strong>Ø</strong></td></tr><tr><td>C = {q1,q5,q7}</td><td>final</td><td>{q1,q8} = D</td><td>{q7,q4,q8} = E</td></tr><tr><td>D = {q1,q8}</td><td>final</td><td>{q1,q8} = D</td><td>{q4} = F</td></tr><tr><td>E = {q7,q4,q8}</td><td>final</td><td>{q5,q8} = G</td><td>{q7,q8} = H</td></tr><tr><td>F = {q4}</td><td>non</td><td>{q5} = I</td><td><strong>Ø</strong></td></tr><tr><td>G ={q5,q8}</td><td>final</td><td>{q8} = J</td><td>{q7} = K</td></tr><tr><td>H = {q7,q8}</td><td>final</td><td>{q8} = J</td><td>{q7,q8} = H</td></tr><tr><td>I = {q5}</td><td>non</td><td>{q8} = J</td><td>{q7}=k</td></tr><tr><td>J = {q8}</td><td>final</td><td>{q8} = J</td><td><strong>Ø</strong></td></tr><tr><td>K = {q7}</td><td>final</td><td><strong>Ø</strong></td><td>{q7,q8}=H</td></tr></tbody></table>

q6 et q3 étant soit des états inaccessibles, soit des états stériles, ont été ignorés.

### Étape 2 : Modélisation de l'automate à partir du tableau

Afin de tracer l'automate il nous suffit de créer des états de A à K, et de les relier en fonction de nos nouvelles transitions.

Vous devriez obtenir cet automate :

![](images/image-19-1024x491.png)

Automate équivalent déterministe

## Source :

1. [AUTOMATES À ÉTATS FINIS DÉTERMINISATION](https://perso.liris.cnrs.fr/sylvain.brandel/wiki/lib/exe/fetch.php?media=ens:liflf:liflf-cm04.pdf)
