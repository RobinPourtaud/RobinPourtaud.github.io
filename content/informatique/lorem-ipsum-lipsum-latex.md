---
title: "Lorem Ipsum (lipsum) - Latex"
slug: "lorem-ipsum-lipsum-latex"
date: "2021-01-05"
categories: 
  - "informatique"
tags: 
  - "latex"
description: "Cet article présente la façon la plus courante de générer un Lorem Ipsum (ou faux-texte) en Latex."
---

## Utilisation

### Importation de lipsum

Afin de générer ce faux-texte, vous devez avoir importé le package "lipsum" :

```
\usepackage{lipsum} 
```

### Exemple d'utilisation

La syntaxe de la commande utilisateur est la suivante :

```
\lipsum[<paragraph range>][<sentence range>]
```

- "Paragraph range" fait référence aux paragraphes du Lipsum souhaité (150 étant la valeur maximum).
- "Sentence range" fait référence aux phrases du Lipsum correspondant au paragraphe voulu. Ce paramètre nécessite une valeur non nulle du premier paramètre.

Les 2 paramètres sont optionnels.

#### Exemple 1

La commande "\lipsum" génère par défaut les paragraphes 1 à 7 du Lipsum :

```
\lipsum
```

#### Exemple 2

Pour générer un Lipsum contenant les 2 premiers paragraphes, vous pouvez utiliser la commande :

```
\lipsum[1-2]
```

![](images/image-20-1024x686.png)

2 premiers paragraphes lipsum

#### Exemple 3

Pour afficher la première phrase du premier paragraphe, vous pouvez utiliser la commande suivante :

```
\lipsum[1][1]
```

Le résultat étant le suivant :

![](images/image-22.png)

Lorem Ipsum première phrase

## Alternative :

Le paquet blindtext propose un résultat similaire :

```
\usepackage{blindtext}
...
\blindtext[1]
```

![](images/image-21-1024x414.png)

blindtext\[1\]

Pour en savoir plus : [Blindtext](https://www.ctan.org/pkg/blindtext)

## Sources :

- [Access to 150 paragraphs of Lorem Ipsum dummy text](https://distrib-coffee.ipsl.jussieu.fr/pub/mirrors/ctan/macros/latex/contrib/lipsum/lipsum.pdf)
- [Lorem Ipsum - Wikipédia](https://fr.wikipedia.org/wiki/Lorem_ipsum)

[D'autres tutoriel sur LaTeX ici](https://keskec.fr/tag/latex/)
