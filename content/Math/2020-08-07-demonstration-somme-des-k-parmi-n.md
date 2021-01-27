---
title: 'Démonstration : Somme des k parmi n'
author: Robin Pourtaud
type: post
date: 2020-08-07T14:58:20+00:00
url: /sciences/mathematiques/robin/4073/
featured_image: /wp-content/uploads/2020/08/ea62c826cc1d5956cdbf62274ab4d692.png
rank_math_seo_score:
  - "73"
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_primary_category:
  - "9"
rank_math_focus_keyword:
  - Somme
rank_math_analytic_object_id:
  - "25"
categories:
  - Mathématiques
tags:
  - Combinaison
  - Démonstration

---
Cet article présente 2 démonstrations de l&rsquo;égalité : somme des k parmi n = 2^k (2 puissance k). La première se servant de la formule du binôme, la deuxième se servant de la définition de l&rsquo;ensembles des parties de E.

## Définition : 



La somme des combinaisons de k=0 à n de k parmi n est égale à 2 à la puissance n. 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-37d380d1ff1d09f17ae47a0b431528eb_l3.svg" class="ql-img-inline-formula " alt="&#92;&#115;&#117;&#109;&#95;&#123;&#107;&#61;&#48;&#125;&#94;&#110;&#32;&#123;&#110;&#32;&#92;&#99;&#104;&#111;&#111;&#115;&#101;&#32;&#107;&#125;&#61;&#32;&#50;&#94;&#110;" title="Rendered by QuickLaTeX.com" height="24" width="126" style="vertical-align: -7px;" />
</p>

## Démonstrations : 

### Démonstration 1 : 

Cette première démonstration est la plus rapide et directe. Elle s&rsquo;appuiera sur la formule du binôme de Newton : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-84eeb38bb45a1d43ecc303d83e1dd38c_l3.svg" class="ql-img-inline-formula " alt="&#92;&#115;&#117;&#109;&#95;&#123;&#107;&#61;&#48;&#125;&#94;&#110;&#32;&#123;&#110;&#32;&#92;&#99;&#104;&#111;&#111;&#115;&#101;&#32;&#107;&#125;&#32;&#120;&#94;&#123;&#107;&#125;&#32;&#121;&#94;&#123;&#110;&#45;&#107;&#125;&#61;&#40;&#120;&#43;&#121;&#41;&#94;&#110;" title="Rendered by QuickLaTeX.com" height="28" width="279" style="vertical-align: -8px;" />
</p>

Si nous prenons<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-984c15b7b80271aebff4d7bb52e841be_l3.svg" class="ql-img-inline-formula " alt="&#120;&#32;&#61;&#32;&#49;" title="Rendered by QuickLaTeX.com" height="14" width="47" style="vertical-align: 0px;" /> et<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-2e65542e4faeccdc450a09d3eeb6c5c1_l3.svg" class="ql-img-inline-formula " alt="&#121;&#61;&#49;" title="Rendered by QuickLaTeX.com" height="18" width="46" style="vertical-align: -4px;" /> , alors obtenons l&rsquo;égalité : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-1333a2996b8fba1f07a4779ecf440a17_l3.svg" class="ql-img-inline-formula " alt="&#92;&#115;&#117;&#109;&#95;&#123;&#107;&#61;&#48;&#125;&#94;&#110;&#32;&#123;&#110;&#32;&#92;&#99;&#104;&#111;&#111;&#115;&#101;&#32;&#107;&#32;&#125;&#32;&#49;&#94;&#107;&#49;&#94;&#123;&#110;&#45;&#107;&#125;&#61;&#40;&#49;&#43;&#49;&#41;&#94;&#110;" title="Rendered by QuickLaTeX.com" height="28" width="275" style="vertical-align: -8px;" />
</p>

Ce qui nous donne : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-1cfb931530e726c90a43d009bdd2e97a_l3.svg" class="ql-img-inline-formula " alt="&#92;&#115;&#117;&#109;&#95;&#123;&#107;&#61;&#48;&#125;&#94;&#110;&#32;&#123;&#110;&#32;&#92;&#99;&#104;&#111;&#111;&#115;&#101;&#32;&#107;&#125;&#61;&#32;&#50;&#94;&#110;" title="Rendered by QuickLaTeX.com" height="28" width="147" style="vertical-align: -8px;" />
</p>

### Démonstration 2 : 

Cette deuxième démonstration s&rsquo;appuie sur la définition exprimant le cardinal de l&rsquo;ensemble des parties d&rsquo;un ensemble quelconque comme étant égal à 2 à la puissance du cardinal de l&rsquo;ensemble. 

Soit un ensemble E de cardinal n, alors l&rsquo;ensemble ayant pour éléments tous les sous-ensembles de E est appelé ensemble des parties de E, noté<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-5b9957c31d188002b6b0206abf507cff_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#80;&#125;&#40;&#69;&#41;" title="Rendered by QuickLaTeX.com" height="20" width="45" style="vertical-align: -5px;" /> .

<pre class="wp-block-verse"><strong>Par exemple : </strong>

Soit <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-37f018e7142fff228e6b6e5e8fdb582e_l3.svg" class="ql-img-inline-formula " alt="&#69;&#32;&#61;&#32;&#92;&#123;&#97;&#44;&#98;&#44;&#99;&#92;&#125;" title="Rendered by QuickLaTeX.com" height="20" width="108" style="vertical-align: -5px;" />, alors :
<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-19f4011f25ee4223f4c95ae3b293fa9e_l3.svg" class="ql-img-inline-formula " alt="&#110;&#32;&#61;&#32;&#92;&#35;&#69;&#32;&#61;&#32;&#51;" title="Rendered by QuickLaTeX.com" height="18" width="108" style="vertical-align: -4px;" /> et <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-048bd95f831793b7398105ba1bc9f70b_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#80;&#125;&#40;&#69;&#41;&#32;&#61;&#32;&#92;&#123;&#92;&#101;&#109;&#112;&#116;&#121;&#115;&#101;&#116;&#44;&#32;&#92;&#123;&#97;&#92;&#125;&#44;&#32;&#92;&#123;&#98;&#92;&#125;&#44;&#32;&#92;&#123;&#99;&#92;&#125;&#44;&#32;&#92;&#123;&#97;&#44;&#98;&#92;&#125;&#44;&#32;&#92;&#123;&#97;&#44;&#99;&#92;&#125;&#44;&#32;&#92;&#123;&#98;&#44;&#99;&#92;&#125;&#44;&#32;&#92;&#123;&#97;&#44;&#98;&#44;&#99;&#92;&#125;&#92;&#125;" title="Rendered by QuickLaTeX.com" height="21" width="461" style="vertical-align: -5px;" />.</pre>

L&rsquo;ensemble des parties est constitué **par définition** d&rsquo;1 partie à 0 élément, de n parties à 1 élément et ainsi de<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-55a80bfa1c15b09c445f6996eca17253_l3.svg" class="ql-img-inline-formula " alt="&#110;&#32;&#92;&#99;&#104;&#111;&#111;&#115;&#101;&#32;&#107;" title="Rendered by QuickLaTeX.com" height="24" width="23" style="vertical-align: -7px;" /> parties à<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-cffff0609b903f189b431ec705a6a188_l3.svg" class="ql-img-inline-formula " alt="&#107;" title="Rendered by QuickLaTeX.com" height="14" width="10" style="vertical-align: 0px;" /> éléments&#8230;

Le cardinal de l&rsquo;ensemble des parties est donc égal à<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-a6c3b6acb04d33eecdaaf3a742c07461_l3.svg" class="ql-img-inline-formula " alt="&#92;&#115;&#117;&#109;&#95;&#123;&#107;&#61;&#48;&#125;&#94;&#110;&#32;&#123;&#110;&#32;&#92;&#99;&#104;&#111;&#111;&#115;&#101;&#32;&#107;&#125;" title="Rendered by QuickLaTeX.com" height="24" width="78" style="vertical-align: -7px;" /> .

Or selon de [nombreuses démonstrations][1], on peut dire que<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-394ffb151e5f32df65f7ad05b7d123d4_l3.svg" class="ql-img-inline-formula " alt="&#92;&#35;&#92;&#109;&#97;&#116;&#104;&#99;&#97;&#108;&#123;&#80;&#125;&#40;&#69;&#41;&#61;&#50;&#94;&#123;&#92;&#35;&#69;&#125;" title="Rendered by QuickLaTeX.com" height="22" width="124" style="vertical-align: -5px;" /> .

Nous retrouvons bien notre égalité de départ.

 [1]: https://fr.wikipedia.org/wiki/Ensemble_des_parties_d%27un_ensemble