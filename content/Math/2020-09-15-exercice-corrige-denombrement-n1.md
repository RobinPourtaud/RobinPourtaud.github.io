---
title: Exercice corrigé – Dénombrement n°1
author: Robin Pourtaud
type: post
date: 2020-09-15T07:40:05+00:00
url: /sciences/mathematiques/denombrement/robin/4528/
featured_image: /wp-content/uploads/2020/09/pexels-photo-763197-1568x1043.jpeg
rank_math_seo_score:
  - "67"
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_primary_category:
  - "353"
rank_math_focus_keyword:
  - Dénombrement
rank_math_analytic_object_id:
  - "12"
categories:
  - Dénombrement
tags:
  - Crible
  - Ensemble
  - Loi de morgan

---
Exercice corrigé de dénombrement n°1.  
Difficulté : <span style="color:#fdae03" class="has-inline-color">Moyenne</span>

## Liste d&rsquo;exercice : 

<p class="has-text-align-center">
  <strong>(En cours)</strong>
</p>

## Énoncé : Une histoire de pigeon 

A Central Parc, il y a 250 oiseaux à 3 couleurs. Parmi eux se trouvent : 

  1. 68 oiseaux possédant des plumes magentas et blanches
  2. 133 oiseaux possédant des plumes blanches
  3. 192 oiseaux ne possédant pas de plumes blanches ou ne possédant pas de plumes vertes
  4. 213 oiseaux possédant des plumes magentas ou vertes

Seuls les pigeons sont verts, magentas et blancs, **pouvez vous les dénombrer ?** 

## Aide : 



Pensez à la formule du crible de Poincaré puis aux lois de De Morgan ! 

Si vous ne les avez pas en tête, vous pouvez toujours essayer de faire un schéma : 

<div class="wp-block-image">
  <figure class="aligncenter"><img src="https://upload.wikimedia.org/wikipedia/commons/4/42/Inclusion-exclusion.svg" alt="upload.wikimedia.org/wikipedia/commons/4/42/Inc..." /><figcaption>Source : <a class="rank-math-link" href="https://fr.wikipedia.org/wiki/Principe_d%27inclusion-exclusion">https://fr.wikipedia.org/wiki/Principe_d%27inclusion-exclusion</a></figcaption></figure>
</div>



## Correction : 

On peut commencer par traduire les événements : 

  * V : « Oiseaux possédant des plumes vertes »
  * B : « Oiseaux possédant des plumes blanches »
  * M : « Oiseaux possédant dans plumes magenta »

Ainsi, l&rsquo;univers<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-d91a072cc4aeb00098b60016c26011bb_l3.svg" class="ql-img-inline-formula " alt="&#92;&#79;&#109;&#101;&#103;&#97;&#32;&#61;&#32;&#86;&#92;&#99;&#117;&#112;&#32;&#66;&#32;&#92;&#99;&#117;&#112;&#32;&#77;" title="Rendered by QuickLaTeX.com" height="14" width="139" style="vertical-align: 0px;" /> .

Nous avons : 

  1.<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-d8b394c3fe52f91aa7f2056617ade1a6_l3.svg" class="ql-img-inline-formula " alt="&#92;&#35;&#40;&#77;&#92;&#99;&#97;&#112;&#32;&#66;&#41;&#61;&#49;&#52;&#48;" title="Rendered by QuickLaTeX.com" height="20" width="148" style="vertical-align: -5px;" /> 
  2.<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-cd756e0cbd1cf1e74eeacf0b3c43bfec_l3.svg" class="ql-img-inline-formula " alt="&#92;&#35;&#66;&#61;&#32;&#50;&#51;" title="Rendered by QuickLaTeX.com" height="18" width="79" style="vertical-align: -4px;" /> 
  3.<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-a8e1ed89db54ec0eb34d25b1bb6fbaf3_l3.svg" class="ql-img-inline-formula " alt="&#92;&#35;&#40;&#92;&#111;&#108;&#115;&#105;&#123;&#66;&#125;&#92;&#99;&#117;&#112;&#92;&#111;&#108;&#115;&#105;&#123;&#86;&#125;&#41;&#32;&#61;&#32;&#55;&#53;" title="Rendered by QuickLaTeX.com" height="20" width="131" style="vertical-align: -5px;" /> 
  4.<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-9bbe2a7c412bf1ad0164b1c7925183d8_l3.svg" class="ql-img-inline-formula " alt="&#92;&#35;&#40;&#77;&#92;&#99;&#117;&#112;&#32;&#86;&#41;&#61;&#51;&#50;" title="Rendered by QuickLaTeX.com" height="20" width="137" style="vertical-align: -5px;" /> 

Selon la formule du crible de Poincaré : 

<p class="has-text-align-left">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-726ffdd069797389fd1b1a103e8ea25e_l3.svg" class="ql-img-inline-formula " alt="&#92;&#35;&#40;&#77;&#92;&#99;&#117;&#112;&#32;&#86;&#32;&#92;&#99;&#117;&#112;&#32;&#66;&#41;&#32;&#61;&#32;&#92;&#35;&#77;&#32;&#43;&#32;&#92;&#35;&#86;&#32;&#43;&#32;&#92;&#35;&#66;&#32;&#45;&#32;&#92;&#35;&#40;&#77;&#92;&#99;&#97;&#112;&#32;&#86;&#41;&#32;&#45;&#32;&#92;&#35;&#40;&#77;&#92;&#99;&#97;&#112;&#32;&#66;&#41;&#32;&#45;&#32;&#92;&#35;&#40;&#86;&#32;&#92;&#99;&#97;&#112;&#32;&#66;&#41;&#32;&#43;&#32;&#92;&#35;&#40;&#77;&#32;&#92;&#99;&#97;&#112;&#32;&#86;&#32;&#92;&#99;&#97;&#112;&#32;&#66;&#41;" title="Rendered by QuickLaTeX.com" height="45" width="656" style="vertical-align: -5px;" />
</p>

<p class="has-text-align-left">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-b4ca481ac8c295708381ee4051778738_l3.svg" class="ql-img-inline-formula " alt="&#92;&#35;&#40;&#77;&#92;&#99;&#97;&#112;&#32;&#86;&#32;&#92;&#99;&#97;&#112;&#32;&#66;&#41;&#32;&#61;&#32;&#92;&#35;&#40;&#77;&#32;&#92;&#99;&#117;&#112;&#32;&#86;&#32;&#92;&#99;&#117;&#112;&#32;&#66;&#41;&#32;&#45;&#32;&#92;&#35;&#77;&#32;&#45;&#32;&#92;&#35;&#86;&#32;&#45;&#32;&#92;&#35;&#66;&#32;&#43;&#32;&#92;&#35;&#40;&#77;&#92;&#99;&#97;&#112;&#32;&#86;&#41;&#32;&#43;&#32;&#92;&#35;&#40;&#77;&#92;&#99;&#97;&#112;&#32;&#66;&#41;&#32;&#43;&#32;&#92;&#35;&#40;&#86;&#32;&#92;&#99;&#97;&#112;&#32;&#66;&#41;" title="Rendered by QuickLaTeX.com" height="45" width="657" style="vertical-align: -5px;" />
</p>

En utilisant une fois de plus la formule de Poincaré et une fois une loi de De Morgan : 

<p class="ql-center-displayed-equation" style="line-height: 22px;">
  <span class="ql-right-eqno"> &nbsp; </span><span class="ql-left-eqno"> &nbsp; </span><img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-139ca7499f1df933064d04b4388d46ae_l3.svg" height="22" width="655" class="ql-img-displayed-equation " alt="&#92;&#91;&#61;&#32;&#92;&#35;&#92;&#79;&#109;&#101;&#103;&#97;&#32;&#45;&#32;&#92;&#35;&#77;&#32;&#45;&#32;&#92;&#35;&#86;&#32;&#45;&#32;&#92;&#35;&#66;&#32;&#43;&#32;&#40;&#92;&#35;&#77;&#32;&#43;&#32;&#92;&#35;&#86;&#32;&#45;&#32;&#92;&#35;&#40;&#77;&#92;&#99;&#117;&#112;&#32;&#86;&#41;&#41;&#32;&#43;&#32;&#92;&#35;&#40;&#77;&#92;&#99;&#97;&#112;&#32;&#66;&#41;&#32;&#43;&#32;&#40;&#92;&#35;&#92;&#79;&#109;&#101;&#103;&#97;&#32;&#45;&#32;&#35;&#40;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#86;&#125;&#92;&#99;&#117;&#112;&#32;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#66;&#125;&#41;&#41;&#92;&#93;" title="Rendered by QuickLaTeX.com" />
</p>

<p class="has-text-align-left">
  <p class="ql-center-displayed-equation" style="line-height: 22px;">
    <span class="ql-right-eqno"> &nbsp; </span><span class="ql-left-eqno"> &nbsp; </span><img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-520610510c0e9160200a5ae023710bcf_l3.svg" height="22" width="468" class="ql-img-displayed-equation " alt="&#92;&#91;&#61;&#32;&#50;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#92;&#35;&#92;&#79;&#109;&#101;&#103;&#97;&#32;&#45;&#32;&#92;&#35;&#66;&#32;&#45;&#32;&#92;&#35;&#40;&#77;&#92;&#99;&#117;&#112;&#32;&#86;&#41;&#43;&#32;&#92;&#35;&#40;&#77;&#92;&#99;&#97;&#112;&#32;&#66;&#41;&#32;&#45;&#32;&#35;&#40;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#86;&#125;&#92;&#99;&#117;&#112;&#32;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#66;&#125;&#41;&#92;&#93;" title="Rendered by QuickLaTeX.com" />
  </p>
</p>

Ainsi : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-325ac3c5c5950655907b7138efb4b216_l3.svg" class="ql-img-inline-formula " alt="&#61;&#53;&#48;&#48;&#32;&#45;&#32;&#49;&#51;&#51;&#32;&#45;&#32;&#50;&#49;&#51;&#32;&#43;&#32;&#54;&#56;&#32;&#45;&#32;&#49;&#57;&#50;&#32;&#61;&#32;&#51;&#48;" title="Rendered by QuickLaTeX.com" height="16" width="305" style="vertical-align: -2px;" />
</p>

Il y a donc dans Central Park **30 pigeons.**