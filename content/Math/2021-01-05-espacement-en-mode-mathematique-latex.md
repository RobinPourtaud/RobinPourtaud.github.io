---
title: Espacement en mode mathématique – Latex
author: Robin Pourtaud
type: post
date: 2021-01-05T20:21:18+00:00
url: /sciences/informatique/robin/5029/
featured_image: /wp-content/uploads/2021/01/Images-KeskeC-8-1568x882.png
rank_math_seo_score:
  - "70"
ads-for-wp-visibility:
  - show
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_focus_keyword:
  - espacement
rank_math_primary_category:
  - "8"
categories:
  - Informatique
  - Mathématiques
tags:
  - LaTeX

---
Cet article présente l&rsquo;ensemble des façons d&rsquo;effectuer un espacement dans vos formules mathématiques en Latex. 

## Tableau récapitulatif des espacements horizontaux : 

_Commentaire : Certains espacements sont exprimés en « mu » (math unit). 1 mu = 1/18 em = 0.2 mm environ (habituellement)._ 

<figure class="wp-block-table">

<table class="has-fixed-layout">
  <tr>
    <td class="has-text-align-left" data-align="left">
      <strong>Formule Latex</strong>
    </td>
    
    <td class="has-text-align-left" data-align="left">
      <strong>Résultat </strong>
    </td>
    
    <td class="has-text-align-left" data-align="left">
      <strong>Description</strong>
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-left" data-align="left">
      a \, b
    </td>
    
    <td class="has-text-align-left" data-align="left">
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-6a305df60f18e027c7eda507a4372d60_l3.svg" class="ql-img-inline-formula " alt="&#97;&#32;&#92;&#44;&#32;&#98;" title="Rendered by QuickLaTeX.com" height="14" width="23" style="vertical-align: 0px;" />
    </td>
    
    <td class="has-text-align-left" data-align="left">
      Taille = 3 mu
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-left" data-align="left">
      a \: b
    </td>
    
    <td class="has-text-align-left" data-align="left">
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-26ee781ec123c84c1d4f349a53b7a92c_l3.svg" class="ql-img-inline-formula " alt="&#97;&#32;&#92;&#58;&#32;&#98;" title="Rendered by QuickLaTeX.com" height="14" width="24" style="vertical-align: 0px;" />
    </td>
    
    <td class="has-text-align-left" data-align="left">
      Taille = 4 mu
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-left" data-align="left">
      a \;
    </td>
    
    <td class="has-text-align-left" data-align="left">
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-e30d3d6cfa0103ff714d287b224f4ba6_l3.svg" class="ql-img-inline-formula " alt="&#97;&#32;&#92;&#59;&#32;&#98;" title="Rendered by QuickLaTeX.com" height="14" width="25" style="vertical-align: 0px;" />
    </td>
    
    <td class="has-text-align-left" data-align="left">
      Taille = 5 mu
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-left" data-align="left">
      a \!
    </td>
    
    <td class="has-text-align-left" data-align="left">
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-d7ca331d773f1a7265fad6e772631b7f_l3.svg" class="ql-img-inline-formula " alt="&#97;&#32;&#92;&#33;&#32;&#98;" title="Rendered by QuickLaTeX.com" height="14" width="16" style="vertical-align: 0px;" />
    </td>
    
    <td class="has-text-align-left" data-align="left">
      Taille = -3 mu
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-left" data-align="left">
      a \ b
    </td>
    
    <td class="has-text-align-left" data-align="left">
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-5e06cd8b93befe489f77e038693d3973_l3.svg" class="ql-img-inline-formula " alt="&#97;&#32;&#92;&#32;&#98;" title="Rendered by QuickLaTeX.com" height="14" width="26" style="vertical-align: 0px;" />
    </td>
    
    <td class="has-text-align-left" data-align="left">
      Taille = 3 mu
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-left" data-align="left">
      a ~ b
    </td>
    
    <td class="has-text-align-left" data-align="left">
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-8c7041807e3e26acd6c9d48128748127_l3.svg" class="ql-img-inline-formula " alt="&#97;&#126;&#98;" title="Rendered by QuickLaTeX.com" height="14" width="26" style="vertical-align: 0px;" />
    </td>
    
    <td class="has-text-align-left" data-align="left">
      Taille = 3 mu (insécable)
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-left" data-align="left">
      a \quad b
    </td>
    
    <td class="has-text-align-left" data-align="left">
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-fe520dc1e2db0a8090dfe172d6520e4b_l3.svg" class="ql-img-inline-formula " alt="&#97;&#32;&#92;&#113;&#117;&#97;&#100;&#32;&#98;" title="Rendered by QuickLaTeX.com" height="14" width="40" style="vertical-align: 0px;" />
    </td>
    
    <td class="has-text-align-left" data-align="left">
      Taille = 18 mu
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-left" data-align="left">
      a \qquad b
    </td>
    
    <td class="has-text-align-left" data-align="left">
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-b7ebc5b0e61aca88362f384fe1c8b7d9_l3.svg" class="ql-img-inline-formula " alt="&#97;&#32;&#92;&#113;&#113;&#117;&#97;&#100;&#32;&#98;" title="Rendered by QuickLaTeX.com" height="14" width="60" style="vertical-align: 0px;" />
    </td>
    
    <td class="has-text-align-left" data-align="left">
      Taille = 36 mu
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-left" data-align="left">
      a \hspace{1cm} b
    </td>
    
    <td class="has-text-align-left" data-align="left">
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-f9e5a513b575f2de7a2daf67d236d7ff_l3.svg" class="ql-img-inline-formula " alt="&#97;&#32;&#92;&#104;&#115;&#112;&#97;&#99;&#101;&#123;&#49;&#99;&#109;&#125;&#32;&#98;" title="Rendered by QuickLaTeX.com" height="14" width="72" style="vertical-align: 0px;" />
    </td>
    
    <td class="has-text-align-left" data-align="left">
      Taille = 1 cm
    </td>
  </tr>
</table><figcaption>Espacements &#8211; Latex</figcaption></figure> 

## Sources : 

  1. [Line breaks and blank spaces &#8211; Overleaf][1]{.rank-math-link}
  2. [LaTeX Spaces and Boxes][2]{.rank-math-link}

 [1]: https://www.overleaf.com/learn/latex/Line_breaks_and_blank_spaces
 [2]: http://www.personal.ceu.hu/tex/spacebox.htm