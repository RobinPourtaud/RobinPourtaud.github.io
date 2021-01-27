---
title: Coefficient binomial (k parmi n)
author: Robin Pourtaud
type: post
date: 2021-01-15T21:17:49+00:00
url: /sciences/mathematiques/denombrement/robin/5172/
featured_image: /wp-content/uploads/2021/01/Images-KeskeC-9-1568x882.png
rank_math_seo_score:
  - "82"
ads-for-wp-visibility:
  - show
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_primary_category:
  - "353"
rank_math_focus_keyword:
  - Coefficient Binomial
categories:
  - Dénombrement
  - Mathématiques
tags:
  - Coefficients binomiaux

---
Cet article présente la notion de coefficient binomial, illustrée d&rsquo;exemples et d&rsquo;exercices corrigés. Un niveau de 1ère/Terminale est préférable pour pouvoir suivre cet article. Un rappel sur la notion de factoriel y sera explicité. 

## Prérequis : 



La notion de factoriel est nécessaire pour pouvoir suivre cet article. Noté « ! », le factoriel de n est le produit (usuellement) des entiers naturels de 1 à n. Autrement dit : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-50b4a2bd4fe00006b87c12f7082e6ae3_l3.svg" class="ql-img-inline-formula " alt="&#110;&#33;&#32;&#61;&#32;&#92;&#80;&#105;&#95;&#123;&#107;&#61;&#49;&#125;&#94;&#123;&#110;&#125;&#107;&#32;&#61;&#32;&#49;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#50;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#92;&#108;&#100;&#111;&#116;&#115;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#40;&#110;&#45;&#49;&#41;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#40;&#110;&#41;" title="Rendered by QuickLaTeX.com" height="21" width="355" style="vertical-align: -6px;" />
</p>

Pour prendre plusieurs exemples : 

  *<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-28d24af35e6b6f562356aeadee3f4fd9_l3.svg" class="ql-img-inline-formula " alt="&#50;&#33;&#32;&#61;&#32;&#49;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#50;" title="Rendered by QuickLaTeX.com" height="15" width="86" style="vertical-align: 0px;" /> 
  *<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-db9c36876f16c84358330edd4ea5b421_l3.svg" class="ql-img-inline-formula " alt="&#53;&#33;&#32;&#61;&#32;&#49;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#50;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#51;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#52;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#53;&#32;&#61;&#32;&#49;&#50;&#48;" title="Rendered by QuickLaTeX.com" height="15" width="247" style="vertical-align: 0px;" /> 

Pour finir, prenez en compte que 0! = 1. Vous pouvez en savoir plus ici si vous êtes curieux : 

<p class="has-text-align-center">
  <a class="rank-math-link" href="https://keskec.fr/sciences/mathematiques/robin/4272/">Pourquoi 0 factoriel est égale à 1 ? &#8211; KeskeC</a>
</p>

## Définition 

En dénombrement, on définit le coefficient binomial comme le nombre de parties à « k » éléments dans un ensemble à « n » éléments, « k » et « n » étant des entiers naturels avec k inférieur ou égal à n. 

On note le coefficient binomial par la formule : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-50c7eb45a3c85ede4b9f231b3ed842bf_l3.svg" class="ql-img-inline-formula " alt="&#92;&#98;&#105;&#110;&#111;&#109;&#123;&#110;&#125;&#123;&#107;&#125;&#32;&#61;&#32;&#67;&#94;&#107;&#95;&#110;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#110;&#33;&#125;&#123;&#107;&#33;&#40;&#110;&#45;&#107;&#41;&#33;&#125;" title="Rendered by QuickLaTeX.com" height="30" width="165" style="vertical-align: -11px;" />
</p>

Un ensemble de propriétés faisant intervenir les coefficients binomiaux est trouvable sur [Wikipédia][1].

## Exemple

### Graphiquement 

On retrouve ce coefficient un peu partout en dénombrement, probabilité ou statistique. Pour prendre un exemple, dans le cadre d&rsquo;une succession d&rsquo;épreuves de Bernoulli, le coefficient binomial est utilisé pour calculer le nombre de k succès parmi n épreuves. 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2021/01/image-5.png" alt="" class="wp-image-5178" width="188" height="181" srcset="https://keskec.fr/wp-content/uploads/2021/01/image-5.png 516w, https://keskec.fr/wp-content/uploads/2021/01/image-5-300x290.png 300w" sizes="(max-width: 188px) 100vw, 188px" /><figcaption>Succession de n épreuves de Bernoulli </figcaption></figure>
</div>

Visiblement, selon cette arborescence, il y a : 

  * 1 façon d&rsquo;obtenir 2 succès (2 parmi 2 = 1)
  * 2 façons d&rsquo;obtenir 1 succès (1 parmi 2 = 2)
  * 1 façon d&rsquo;obtenir 0 succès (0 parmi 2 = 1)

Cette symétrie dans les résultats se retrouvera bien sûr des arborescences plus grandes. 

### Avec un ensemble 

Soit un ensemble E = {a,b,c}. 

Calculons l&rsquo;ensemble des parties de E : 

<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-a9cb1321db585dbad077e0cee1938e47_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#80;&#125;&#40;&#69;&#41;&#32;&#61;&#32;&#92;&#123;&#92;&#118;&#97;&#114;&#110;&#111;&#116;&#104;&#105;&#110;&#103;&#44;&#32;&#92;&#123;&#97;&#92;&#125;&#44;&#32;&#92;&#123;&#98;&#92;&#125;&#44;&#32;&#92;&#123;&#99;&#92;&#125;&#44;&#32;&#92;&#123;&#97;&#44;&#32;&#98;&#92;&#125;&#44;&#32;&#92;&#123;&#97;&#44;&#32;&#99;&#92;&#125;&#44;&#32;&#92;&#123;&#98;&#44;&#32;&#99;&#92;&#125;&#44;&#32;&#92;&#123;&#97;&#44;&#98;&#44;&#99;&#92;&#125;&#92;&#125;" title="Rendered by QuickLaTeX.com" height="20" width="467" style="vertical-align: -5px;" /> . 

Il y a : 

  * 1 élément à 0 élément (0 parmi 3 = 1)
  * 3 éléments à 1 élément (0 parmi 3 = 3)
  * 3 éléments à 2 éléments (0 parmi 3 = 3)
  * 1 élément à 3 éléments (0 parmi 3 = 1)

Commentaire : L&rsquo;ensemble des parties d&rsquo;un ensemble E a pour cardinal<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-b00048f1d5b51cf84860e357287c90a0_l3.svg" class="ql-img-inline-formula " alt="&#50;&#94;&#123;&#92;&#35;&#69;&#125;" title="Rendered by QuickLaTeX.com" height="17" width="35" style="vertical-align: 0px;" /> , ce qui correspond à la somme des cardinaux des parties à k éléments. Par exemple, nous avons bien pour cet exemple 1+3+3+1=2^3. Pour en savoir plus, [c&rsquo;est ici][2]{.rank-math-link}. 

## Exercice corrigé 

Afin de voir si vous avez bien compris cette notion, je vous propose un petit exercice d&rsquo;introduction : 

### Enoncé

Un ami me propose de prendre 3 cartes dans un paquet de 52 cartes.  
Si j&rsquo;obtiens le 5;6 et 7 de cœur (sans prendre en compte l&rsquo;ordre), il m&rsquo;a dit qu&rsquo;il me donnerait 100€. 

  1. Combien y a-t-il de tirages possibles ? 
  2. Quelle est la probabilité d&rsquo;obtenir ces 100€ ? 

### Correction 

On veut obtenir 3 cartes spécifiques parmi un paquet de 52 cartes. 

Si vous essayez de calculer ce chiffre « à la main », vous allez vite vous rendre compte que cette tâche va vite devenir compliquée. Utilisons donc notre formule ! 

Avec n = 52 et k = 3, nous obtenons :<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-d3c16a008a84fc0f9fb8aaddec4f2eda_l3.svg" class="ql-img-inline-formula " alt="&#92;&#98;&#105;&#110;&#111;&#109;&#123;&#53;&#50;&#125;&#123;&#51;&#125;" title="Rendered by QuickLaTeX.com" height="26" width="29" style="vertical-align: -7px;" /> . 

Ne calculez pas 52 factoriel à la main, 52 factoriel est égale à 8.0658175e+67.

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-2fa9202aca710f20024a8a2e975c262b_l3.svg" class="ql-img-inline-formula " alt="&#92;&#102;&#114;&#97;&#99;&#123;&#110;&#33;&#125;&#123;&#107;&#33;&#40;&#110;&#45;&#107;&#41;&#33;&#125;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#53;&#50;&#33;&#125;&#123;&#51;&#33;&#40;&#53;&#50;&#45;&#51;&#41;&#33;&#125;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#53;&#50;&#33;&#125;&#123;&#54;&#40;&#52;&#57;&#41;&#33;&#125;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#53;&#50;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#53;&#49;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#53;&#48;&#125;&#123;&#54;&#125;&#61;&#32;&#50;&#50;&#49;&#48;&#48;" title="Rendered by QuickLaTeX.com" height="30" width="406" style="vertical-align: -11px;" />
</p>

Il y a donc 22100 possibilités différentes. 

On veut obtenir une de ces possibilités parmi ces 22100, il y a donc une probabilité de réussite de<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-cbea4cecb72be7ed29728553761de442_l3.svg" class="ql-img-inline-formula " alt="&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#50;&#50;&#49;&#48;&#48;&#125;" title="Rendered by QuickLaTeX.com" height="25" width="40" style="vertical-align: -7px;" /> . C&rsquo;est à dire environ 0.004% de chance. 

## Sources : 

  * [Combinaison &#8211; Wikipédia][3]{.rank-math-link}
  * [Combinaison &#8211; approche][4]{.rank-math-link}
  * [Loi Binomial &#8211; Wikipédia][5]{.rank-math-link}
  * [Le coefficient binomial &#8211; jybaudot.fr][6]{.rank-math-link}

 [1]: https://fr.wikipedia.org/wiki/Coefficient_binomial#Formules%20faisant%20intervenir%20les%20coefficients%20binomiaux
 [2]: https://keskec.fr/sciences/mathematiques/robin/4073/
 [3]: https://fr.wikipedia.org/wiki/Combinaison_(math%C3%A9matiques)
 [4]: http://villemin.gerard.free.fr/Denombre/Cbingene.htm
 [5]: https://fr.wikipedia.org/wiki/Loi_binomiale
 [6]: http://www.jybaudot.fr/Probas/coeffbinomial.html