---
title: Ensembles mathématiques usuels (majuscules ajourées) – Latex
author: Robin Pourtaud
type: post
date: 2021-01-05T20:23:06+00:00
url: /sciences/informatique/robin/5122/
featured_image: /wp-content/uploads/2021/01/Images-KeskeC-6-1568x882.png
rank_math_seo_score:
  - "75"
  - "75"
ads-for-wp-visibility:
  - show
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_primary_category:
  - "8"
rank_math_focus_keyword:
  - ensemble
categories:
  - Informatique
  - Mathématiques
tags:
  - LaTeX

---
Cet article présente la façon usuelle d&rsquo;afficher les symboles utilisés pour désigner certains ensembles mathématiques. Ces symboles, appelés « majuscule ajourées » serons explicités dans un tableau récapitulatif. 

## Ajourer une majuscule : 

Pour ajourer une majuscule (mettre une majuscule sous forme usuelle des ensembles) en Latex, il suffit d&rsquo;importer amsfonts : 

<pre class="wp-block-code" aria-describedby="shcb-language-135" data-shcb-language-name="TeX" data-shcb-language-slug="tex"><div>
  <code class="hljs language-tex">&lt;span class="hljs-tag">\&lt;span class="hljs-name">usepackage&lt;/span>&lt;span class="hljs-string">{amsfonts}&lt;/span>&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-135"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">TeX</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">tex</span><span class="shcb-language__paren">)</span></small></pre>

Vous pouvez ainsi via « mathbb » afficher les majuscules que vous souhaitez : 

<pre class="wp-block-code" aria-describedby="shcb-language-136" data-shcb-language-name="TeX" data-shcb-language-slug="tex"><div>
  <code class="hljs language-tex">&lt;span class="hljs-tag">\&lt;span class="hljs-name">mathbb&lt;/span>&lt;span class="hljs-string">{R}&lt;/span>&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-136"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">TeX</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">tex</span><span class="shcb-language__paren">)</span></small></pre>

Ce qui nous donne :



<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-edde9283654927ccdd1ba0a4a89794cd_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#82;&#125;" title="Rendered by QuickLaTeX.com" height="14" width="14" style="vertical-align: 0px;" />
</p>

## Tableau récapitulatif

Ce tableau liste quelques utilisation commune des majuscules ajourés en mathématique : <figure class="wp-block-table">

<table class="has-fixed-layout">
  <tr>
    <td>
      <strong>Ensemble</strong>
    </td>
    
    <td>
      <strong>Code Latex</strong>
    </td>
    
    <td>
      <strong>Affichage</strong>
    </td>
  </tr>
  
  <tr>
    <td>
      Biquaternion
    </td>
    
    <td>
      \mathbb{B}
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-802e3874f6782154ed20199d3f5c072e_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#66;&#125;" title="Rendered by QuickLaTeX.com" height="14" width="13" style="vertical-align: 0px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      Ensemble des nombres complexes
    </td>
    
    <td>
      \mathbb{C}
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-ec6b217576a8d45e956783f37ce4d158_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#67;&#125;" title="Rendered by QuickLaTeX.com" height="14" width="14" style="vertical-align: 0px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      Ensemble des nombres décimaux
    </td>
    
    <td>
      \mathbb{D}
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-682d08075081b975f96001712390c98f_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#68;&#125;" title="Rendered by QuickLaTeX.com" height="14" width="14" style="vertical-align: 0px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      Espérance mathématique
    </td>
    
    <td>
      \mathbb{E}
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-dd8d41cac6b7506d0984796e6aa24afd_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#69;&#125;" title="Rendered by QuickLaTeX.com" height="14" width="13" style="vertical-align: 0px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      Quaternion
    </td>
    
    <td>
      \mathbb{H}
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-f0caea126777b70f888509024c6f3651_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#72;&#125;" title="Rendered by QuickLaTeX.com" height="14" width="16" style="vertical-align: 0px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      Corps
    </td>
    
    <td>
      \mathbb{K}
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-4f01c05604edc797653571e0f679856b_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#75;&#125;" title="Rendered by QuickLaTeX.com" height="14" width="16" style="vertical-align: 0px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      Quaternion Hyperbolique
    </td>
    
    <td>
      \mathbb{M}
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-99b8a0b7bce2c647be00c0267fa8a7bc_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#77;&#125;" title="Rendered by QuickLaTeX.com" height="14" width="19" style="vertical-align: 0px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      Ensemble des entiers naturels
    </td>
    
    <td>
      \mathbb{N}
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-12dd35a2c29aa087abd0d0a4f7a401e3_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#78;&#125;" title="Rendered by QuickLaTeX.com" height="14" width="14" style="vertical-align: 0px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      Octonion
    </td>
    
    <td>
      \mathbb{O}
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-e4b4ab10a51a130df381ef5387002ded_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#79;&#125;" title="Rendered by QuickLaTeX.com" height="14" width="15" style="vertical-align: 0px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      Ensemble des nombres premiers / Probabilité
    </td>
    
    <td>
      \mathbb{P}
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-92e0cceedd583138741c4ed80c03701c_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#80;&#125;" title="Rendered by QuickLaTeX.com" height="14" width="12" style="vertical-align: 0px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      Ensemble des nombres rationnels
    </td>
    
    <td>
      \mathbb{Q}
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-cd6b133e88a741bbb673bc18cfd21428_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#81;&#125;" title="Rendered by QuickLaTeX.com" height="17" width="15" style="vertical-align: -3px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      Ensemble des nombres réels
    </td>
    
    <td>
      \mathbb{R}
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-edde9283654927ccdd1ba0a4a89794cd_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#82;&#125;" title="Rendered by QuickLaTeX.com" height="14" width="14" style="vertical-align: 0px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      Sédénion
    </td>
    
    <td>
      \mathbb{S}
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-dede24e7b248b3a91c741ab62e5c3eac_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#83;&#125;" title="Rendered by QuickLaTeX.com" height="14" width="11" style="vertical-align: 0px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      Ensembles des entiers relatifs
    </td>
    
    <td>
      \mathbb{Z}
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-5852eec9c2759c158ee7aae8cac3d26c_l3.svg" class="ql-img-inline-formula " alt="&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#90;&#125;" title="Rendered by QuickLaTeX.com" height="14" width="13" style="vertical-align: 0px;" />
    </td>
  </tr>
</table><figcaption>Majuscules ajourés</figcaption></figure> 

Toutes les lettres de l&rsquo;alphabet (latin ou grec) peuvent être prises en argument. 

_Commentaire : La fonction indicatrice ne peut pas être affichée avec amsfonts, il faut utiliser un autre package. Vous pouvez retrouver un article sur le sujet ici (fonction indicatrice &#8211; KeskeC)._

## D&rsquo;autres articles sur Latex

Retrouvez l&rsquo;ensemble de nos articles sur Latex ici : 

<p class="has-text-align-center">
  <a href="https://keskec.fr/tag/latex/" class="rank-math-link">Latex &#8211; KeskeC</a>
</p>

## Sources : 

  1. [Nombre Hypercomplexe &#8211; Wikipédia][1]{.rank-math-link}
  2. [amsmath &#8211; Latex][2]{.rank-math-link}

 [1]: https://fr.wikipedia.org/wiki/Nombre_hypercomplexe
 [2]: https://ctan.tetaneutral.net/macros/latex/required/amsmath/amsldoc.pdf