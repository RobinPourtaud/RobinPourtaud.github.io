---
title: 'Exercice corrigé : Simplification de formules Booléennes'
author: Robin Pourtaud
type: post
date: 2020-11-24T09:11:49+00:00
url: /sciences/informatique/robin/4732/
featured_image: /wp-content/uploads/2020/11/Formule-Booleenne-1568x764.png
rank_math_seo_score:
  - "59"
ads-for-wp-visibility:
  - show
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_primary_category:
  - "8"
rank_math_focus_keyword:
  - Booléennes
categories:
  - Informatique
  - Mathématiques
tags:
  - Logique

---
A travers cet exercice, nous allons vous montrer comment simplifier une expression logique booléenne algébriquement, autrement dit sans avoir recours à un tableau de Karnaugh ou à la méthode de Quine. Pour pouvoir simplifier ces formules, vous devez avoir en tête un ensemble de propriétés sur les opérateurs logiques en plus du théorème de Morgan (que vous pouvez trouver facilement sur cette page : [L&rsquo;algèbre de Boole][1]{.rank-math-link}).

## Exercices : 

Simplifiez au maximum ces formules logiques algébriquement :

### Formule 1 



<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-38780f7befe9b0d4801f9a4ae531000d_l3.svg" class="ql-img-inline-formula " alt="&#65;&#66;&#67;&#43;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#43;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#67;&#125;" title="Rendered by QuickLaTeX.com" height="19" width="127" style="vertical-align: -2px;" />
</p>

### Formule 2 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-a4646b5ca385cbff7f488a642abac360_l3.svg" class="ql-img-inline-formula " alt="&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#66;&#43;&#67;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#68;&#43;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#66;&#125;&#43;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#68;&#125;" title="Rendered by QuickLaTeX.com" height="19" width="187" style="vertical-align: -2px;" />
</p>

### Formule 3 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-eed065b99172bd77953ec052f9af1861_l3.svg" class="ql-img-inline-formula " alt="&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#43;&#68;&#125;&#46;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#67;&#125;&#43;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#66;&#125;&#125;&#43;&#67;&#125;" title="Rendered by QuickLaTeX.com" height="27" width="159" style="vertical-align: -2px;" />
</p>

### Formule 4

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-d7498443af24c31ff22a001cbe7da627_l3.svg" class="ql-img-inline-formula " alt="&#40;&#65;&#43;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#66;&#125;&#43;&#67;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#66;&#125;&#41;&#40;&#65;&#43;&#66;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#43;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#66;&#125;&#41;" title="Rendered by QuickLaTeX.com" height="22" width="282" style="vertical-align: -5px;" />
</p>

### Formule 5 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-9ef6b4c3718712d9e9c00118c86aefc4_l3.svg" class="ql-img-inline-formula " alt="&#65;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#67;&#125;&#32;&#43;&#32;&#65;&#66;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#67;&#125;&#43;&#66;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#67;&#125;&#43;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#66;" title="Rendered by QuickLaTeX.com" height="19" width="214" style="vertical-align: -2px;" />
</p>

## Indices :

### Formule 1 

Il faut utiliser 2 fois la propriété :<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-6987d3f80328d73c5c276192858027d9_l3.svg" class="ql-img-inline-formula " alt="&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#43;&#65;&#66;&#32;&#61;&#32;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#43;&#66;" title="Rendered by QuickLaTeX.com" height="19" width="153" style="vertical-align: -2px;" /> . 

### Formule 2 

Il faut utiliser 2 fois la propriété<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-6987d3f80328d73c5c276192858027d9_l3.svg" class="ql-img-inline-formula " alt="&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#43;&#65;&#66;&#32;&#61;&#32;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#43;&#66;" title="Rendered by QuickLaTeX.com" height="19" width="153" style="vertical-align: -2px;" /> . 

Une fois<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-a42cb88e1e9653fa5e5ffa6e7e20d5b4_l3.svg" class="ql-img-inline-formula " alt="&#65;&#32;&#43;&#32;&#65;&#66;&#32;&#61;&#32;&#65;&#40;&#49;&#43;&#66;&#41;&#32;&#61;&#32;&#65;" title="Rendered by QuickLaTeX.com" height="20" width="220" style="vertical-align: -5px;" /> .

### Formule 3 

Ce développement a pour but de vous faire réviser le théorème de Morgan. Appliquez le en boucle. A un moment, vous devriez vous en sortir. 

### Formule 4 

Un triple développement n&rsquo;est pas nécessaire ! 

### Formule 5 

Vous avez quelque chose de trop ? Utilisez la propriété<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-5cd7008cbb04f29f9c7ef20ee85ab601_l3.svg" class="ql-img-inline-formula " alt="&#65;&#43;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#61;&#49;" title="Rendered by QuickLaTeX.com" height="19" width="90" style="vertical-align: -2px;" /> . 

## Correction : 

### Formule 1 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-3a3d2a623483b372f7e52b071e0bca31_l3.svg" class="ql-img-inline-formula " alt="&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#43;&#66;&#43;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#67;&#125;" title="Rendered by QuickLaTeX.com" height="19" width="96" style="vertical-align: -2px;" />
</p>

### Formule 2 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-d6353818a4aed16ddd3cf89bcf96c377_l3.svg" class="ql-img-inline-formula " alt="&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#43;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#66;&#125;&#43;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#68;&#125;" title="Rendered by QuickLaTeX.com" height="19" width="98" style="vertical-align: -2px;" />
</p>

### Formule 3 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-fe12f2d35193fe90e885f87481af1858_l3.svg" class="ql-img-inline-formula " alt="&#67;" title="Rendered by QuickLaTeX.com" height="14" width="16" style="vertical-align: 0px;" />
</p>

### Formule 4 

<p class="has-text-align-center">
  1
</p>

### Formule 5 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-0c85568e15937ddf421efb5e19de1a32_l3.svg" class="ql-img-inline-formula " alt="&#65;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#67;&#125;&#43;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#66;" title="Rendered by QuickLaTeX.com" height="19" width="86" style="vertical-align: -2px;" />
</p>

 [1]: https://fr.wikipedia.org/wiki/Alg%C3%A8bre_de_Boole_(logique)