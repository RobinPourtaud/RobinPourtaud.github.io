---
title: "ISETL - Boucle While et boucle For"
slug: "isetl-boucle-while-et-boucle-for"
date: "2020-07-27"
categories: 
  - "informatique"
tags: 
  - "isetl"
  
description: "Interactive SET Language (ISETL) est un langage de programmation basé sur SETL. Développé par Garry Levin en 1988, il avait pour finalité l’enseignement des mathématiques discrètes à l’université. Cet article est à destination des étudiants voulant apprendre à rédiger des boucles While et For en ISETL."
---
## Boucle While

### Définition :

Une boucle "While", ou boucle "Tant Que" permet de répéter l'exécution d'une portion de code tant qu'une condition est "Vrai".

En ISETL, une boucle "While" se rédige de cette façon :

### Exemple :

On veut se compliquer la vie et afficher 3 fois "true" avec une boucle "While" :

```php
x := true;
i := 0;
while x do 
  i:=i+1;
  print(x);
  if i > 2 then 
    x:=false;
  end if
end while;
```

![Boucle While ISETL](image-15-1024x456.png#t5)



## Boucle For

### Définition :

Une boucle "For" est un type de boucle While se servant **d'un compteur et d'une condition** tel que ce compteur ne doit pas rendre cette **condition fausse.**

En ISETL, une boucle For se rédige de cette façon :

```php
for <variable> in <tuple> do
<code>
end for;
```

### Exemple :

On veut afficher tous les carrés des éléments de 0 à 9 d'un tuple :

```php
E:=[0..9];
for i in E do print(i**2);
end for;
```

![Carrés des valeurs d\'un tuple](image-14-1024x473.png#t5)

