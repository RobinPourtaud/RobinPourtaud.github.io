---
title: Fonction Indicatrice / Fonction caractéristique – Latex
author: Robin Pourtaud
type: post
date: 2021-01-05T20:23:47+00:00
url: /sciences/informatique/robin/5130/
featured_image: /wp-content/uploads/2021/01/Images-KeskeC-7-1568x882.png
rank_math_seo_score:
  - "78"
ads-for-wp-visibility:
  - show
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_primary_category:
  - "8"
rank_math_focus_keyword:
  - indicatrice
categories:
  - Informatique
  - Mathématiques
tags:
  - LaTeX

---
Cet article présente un moyen de générer le symbole usuel de la fonction indicatrice (ou fonction caractéristique). Ce symbole peut aussi désigner la fonction identité. 

## Package requis 

Il existe plusieurs paquets permettant de générer un « 1 ajouré ». On peut retrouver dsfont notamment. Pour cet article, nous utiliserons le package bbold

<pre class="wp-block-code" aria-describedby="shcb-language-137" data-shcb-language-name="TeX" data-shcb-language-slug="tex"><div>
  <code class="hljs language-tex">&lt;span class="hljs-tag">\&lt;span class="hljs-name">usepackage&lt;/span>&lt;span class="hljs-string">{bbold}&lt;/span>&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-137"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">TeX</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">tex</span><span class="shcb-language__paren">)</span></small></pre>

_Le package amsfonts ne permet pas de générer un 1 ajouré, vous obtiendrez ce symbole :_ 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2021/01/image-1.png" alt="" class="wp-image-5143" width="43" height="39" /></figure>
</div>

## Code Latex 

Pour afficher le symbole de la fonction caractéristique, il faut utiliser la commande mathbb : 

<pre class="wp-block-code" aria-describedby="shcb-language-138" data-shcb-language-name="TeX" data-shcb-language-slug="tex"><div>
  <code class="hljs language-tex">&lt;span class="hljs-tag">\&lt;span class="hljs-name">mathbb&lt;/span>&lt;span class="hljs-string">{1}&lt;/span>&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-138"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">TeX</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">tex</span><span class="shcb-language__paren">)</span></small></pre>

## Résultat 

Nous obtenons ainsi : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2021/01/image.png" alt="" class="wp-image-5142" width="45" height="47" /></figure>
</div>

## D&rsquo;autres articles sur Latex

Retrouvez l&rsquo;ensemble de nos articles sur Latex ici : 

<p class="has-text-align-center">
  <a href="https://keskec.fr/tag/latex/" class="rank-math-link">Latex &#8211; KeskeC</a>
</p>

## Sources : 

  1. [Fonction caractéristique (théorie des ensembles) &#8211; Wikipédia][1]{.rank-math-link}
  2. [Bbold &#8211; Latex][2]{.rank-math-link}

 [1]: https://fr.wikipedia.org/wiki/Fonction_caract%C3%A9ristique_(th%C3%A9orie_des_ensembles)
 [2]: https://mirrors.chevalier.io/CTAN/fonts/bbold/bbold.pdf