---
title: 'Définition : NFF-Sat'
author: Robin Pourtaud
type: post
date: 2020-11-22T21:29:02+00:00
url: /sciences/mathematiques/robin/4792/
featured_image: /wp-content/uploads/2020/11/satisfiabilite-1568x768.png
rank_math_seo_score:
  - "74"
ads-for-wp-visibility:
  - show
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_primary_category:
  - "9"
rank_math_focus_keyword:
  - NFF
rank_math_analytic_object_id:
  - "4"
categories:
  - Informatique
  - Mathématiques
tags:
  - Complexité asymptotique

---
Un problème de satisfaction de contraintes booléennes, aussi appelé problème de satisfiabilité, consiste à déterminer, pour un ensemble de contraintes définies sur des variables booléennes, s’il existe une assignation de valeurs aux variables satisfaisant toutes les contraintes.

## Un peu de vocabulaire : 

### Définition : Forme normale négative

On dit d&rsquo;une formule logique, qu&rsquo;elle est en forme normale négative (FNN) si : 

  * Les négations se trouvent uniquement sur les littéraux.
  * En plus de l&rsquo;opérateur de négation, seul l&rsquo;opérateur de conjonction (« et ») et de disjonction (« ou ») est autorisé. 

Pour prendre un exemple : 



  *<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-fa3a1a131cb1f271e5f54b1cbd2573d5_l3.svg" class="ql-img-inline-formula " alt="&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#32;&#92;&#119;&#101;&#100;&#103;&#101;&#32;&#66;&#125;" title="Rendered by QuickLaTeX.com" height="17" width="54" style="vertical-align: 0px;" /> n&rsquo;est pas sous forme normale négative.
  *<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-e43b8f0cf6d716f78760555afb75856b_l3.svg" class="ql-img-inline-formula " alt="&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#92;&#119;&#101;&#100;&#103;&#101;&#32;&#66;" title="Rendered by QuickLaTeX.com" height="17" width="53" style="vertical-align: 0px;" /> est sous forme normale négative.

### Définition : Satisifiabilité 

On dit d&rsquo;une formule booléenne qu&rsquo;elle est satisfiable s&rsquo;il existe une assignation (ou valuation) des variables tel qu&rsquo;elle rende la formule « vrai ». 

Par exemple : 

  *<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-2e8e06717c2300529f7e74023b54aa38_l3.svg" class="ql-img-inline-formula " alt="&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#92;&#119;&#101;&#100;&#103;&#101;&#32;&#65;" title="Rendered by QuickLaTeX.com" height="17" width="52" style="vertical-align: 0px;" /> n&rsquo;est pas satisfiable
  *<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-f01572be8b92f3a4bb25383f9a5e29bc_l3.svg" class="ql-img-inline-formula " alt="&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#65;&#125;&#92;&#108;&#111;&#114;&#32;&#65;" title="Rendered by QuickLaTeX.com" height="17" width="52" style="vertical-align: 0px;" /> est satisfiable

Fun-Fact : Dans le deuxième cas, peu importe la valeur de notre seule variable A, notre formule est satisfiable, on peut dans ce cas parler de tautologie. 

## Le problème NFF-Sat : 

Le problème NFF-Sat, ou NegLit-Sat peut se présenter en 2 lignes : 

Soit<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-db21f99d521a59040b3c65ffce422b30_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#70;&#125;" title="Rendered by QuickLaTeX.com" height="16" width="17" style="vertical-align: -1px;" /> une formule booléenne telle que<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-db21f99d521a59040b3c65ffce422b30_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#70;&#125;" title="Rendered by QuickLaTeX.com" height="16" width="17" style="vertical-align: -1px;" /> est sous forme normale négative.

<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-db21f99d521a59040b3c65ffce422b30_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#70;&#125;" title="Rendered by QuickLaTeX.com" height="16" width="17" style="vertical-align: -1px;" /> est-elle satisfiable ? 

## Sources : 

  1. [Représentations de formules SAT pour la Résolution Séquentielle][1]{.rank-math-link}
  2. [Valuation Logic &#8211; Wikipédia][2]{.rank-math-link}
  3. [Satisfiability &#8211; Wikipédia][3]{.rank-math-link}
  4. [Negation normal form &#8211; Wikipédia][4]{.rank-math-link}

 [1]: http://www.univ-bejaia.dz/jspui/bitstream/123456789/9590/1/Representations%20de%20formules%20SAT%20pour%20la%20resolution%20sequentielle.pdf
 [2]: https://en.wikipedia.org/wiki/Valuation_(logic)
 [3]: https://en.wikipedia.org/wiki/Satisfiability
 [4]: https://en.wikipedia.org/wiki/Negation_normal_form?oldid=711179836