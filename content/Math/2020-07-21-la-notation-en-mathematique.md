---
title: 'La notation « ? » en mathématique : Termial'
author: Robin Pourtaud
type: post
date: 2020-07-20T23:06:14+00:00
url: /sciences/mathematiques/robin/3786/
featured_image: /wp-content/uploads/2020/07/c8a0615ec8a491deffc23b86e818e7bc.png
rank_math_seo_score:
  - "75"
rank_math_primary_category:
  - "9"
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_focus_keyword:
  - ?
rank_math_analytic_object_id:
  - "34"
categories:
  - Mathématiques
tags:
  - Notation

---
Dans son livre « The Art of Computer Science », l&rsquo;informaticien Donald Knuth introduisit la notation « ? ». Appelé Termial en anglais, la notation point d&rsquo;interrogation n? représente la somme de tous les entiers naturels inférieurs ou égales à n. 

## Nota Bene : 

  1. Il faut savoir que cette notation **n&rsquo;est pas couramment employée** et se doit donc d&rsquo;être utilisée dans le bon contexte.
  2. La notation point d&rsquo;interrogation est distincte de la [fonction de Minkowski][1]{.rank-math-link}.
  3. Je n&rsquo;ai pas trouvé de traduction pour « Termial » en français. 

## Définition : 

Le Termial est présenté par Knuth comme une fonction analogue à la fonction factorielle « ! ». 



La fonction factorielle étant définie<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-0695ea1300ab18701f051fd5df32c7d5_l3.svg" class="ql-img-inline-formula " alt="&#92;&#102;&#111;&#114;&#97;&#108;&#108;&#32;&#110;&#32;&#92;&#105;&#110;&#32;&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#78;&#125;" title="Rendered by QuickLaTeX.com" height="15" width="62" style="vertical-align: -1px;" /> par : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-bc8e463d361ccbcbf01c2c7df62c765f_l3.svg" class="ql-img-inline-formula " alt="&#110;&#33;&#61;&#92;&#112;&#114;&#111;&#100;&#94;&#110;&#95;&#123;&#105;&#61;&#49;&#125;&#105;&#61;&#32;&#49;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#50;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#92;&#108;&#100;&#111;&#116;&#115;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#40;&#110;&#45;&#49;&#41;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#110;" title="Rendered by QuickLaTeX.com" height="29" width="449" style="vertical-align: -8px;" />
</p>

La fonction « termial » se définie par : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-7e69bba7fc583f52ae3d09ec31a768c2_l3.svg" class="ql-img-inline-formula " alt="&#110;&#63;&#61;&#92;&#115;&#117;&#109;&#94;&#110;&#95;&#123;&#105;&#61;&#49;&#125;&#105;&#32;&#61;&#32;&#49;&#32;&#43;&#32;&#50;&#32;&#43;&#32;&#92;&#108;&#100;&#111;&#116;&#115;&#32;&#43;&#32;&#40;&#110;&#45;&#49;&#41;&#32;&#43;&#32;&#110;" title="Rendered by QuickLaTeX.com" height="29" width="457" style="vertical-align: -8px;" />
</p>

Cette série est grossièrement divergente. 

## Extension pour n non entier : 

Comme pour la fonction factorielle avec la fonction gamma, il est possible d&rsquo;étendre la fonction « Termial » à des valeurs non entières en prenant : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-9589ac58ba5a8211321053c5c87c0d1a_l3.svg" class="ql-img-inline-formula " alt="&#110;&#63;&#61;&#92;&#115;&#117;&#109;&#94;&#110;&#95;&#123;&#105;&#61;&#49;&#125;&#105;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#110;&#40;&#110;&#43;&#49;&#41;&#125;&#123;&#50;&#125;" title="Rendered by QuickLaTeX.com" height="37" width="244" style="vertical-align: -9px;" />
</p>

Ainsi : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-34ad9ae55211792419415c819fe64d29_l3.svg" class="ql-img-inline-formula " alt="&#48;&#46;&#53;&#63;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#48;&#46;&#53;&#40;&#48;&#46;&#53;&#43;&#49;&#41;&#125;&#123;&#50;&#125;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#51;&#125;&#123;&#56;&#125;" title="Rendered by QuickLaTeX.com" height="37" width="229" style="vertical-align: -9px;" />
</p>

## Sources : 

  1. [DONALD (« DON ») ERVIN KNUTH][2]
  2. Donald E. Knuth (1997).&nbsp;_The Art of Computer Programming: Volume 1: Fundamental Algorithms_. 3rd Ed. Addison Wesley Longman, U.S.A. p. 48.
  3. [en.wikipedia.org &#8211; Termial][3]{.rank-math-link}

 [1]: https://fr.wikipedia.org/wiki/Fonction_point_d%27interrogation
 [2]: https://amturing.acm.org/award_winners/knuth_1013846.cfm
 [3]: https://en.wikipedia.org/wiki/Termial