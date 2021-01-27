---
title: ISETL – Conditions If, ElseIf, Else
author: Robin Pourtaud
type: post
date: 2020-07-26T16:51:34+00:00
url: /sciences/informatique/robin/3860/
featured_image: /wp-content/uploads/2020/07/Capture-1568x986.png
rank_math_primary_category:
  - "8"
rank_math_seo_score:
  - "75"
rank_math_focus_keyword:
  - Conditions
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_analytic_object_id:
  - "30"
ads-for-wp-visibility:
  - show
categories:
  - Informatique
tags:
  - ISETL
  - Tutoriel

---
Interactive SET Language (ISETL) est un langage de programmation basé sur SETL. Développé par Garry Levin en 1988, il avait pour finalité&nbsp;**l’enseignement des mathématiques discrètes à l’université**_._ Cet article est à destination des étudiants voulant apprendre à rédiger des conditions en ISETL. 

## If, ElseIf et Else

En informatique, un « Si » permet d&rsquo;exécuter une partie de code conditionnellement.  
**Par exemple**, prenons une variable x. 

<pre class="wp-block-code" aria-describedby="shcb-language-110" data-shcb-language-name="JavaScript" data-shcb-language-slug="javascript"><div>
  <code class="hljs language-javascript">Si x &gt; &lt;span class="hljs-number">5&lt;/span>, alors on souhaite afficher &lt;span class="hljs-string">"nombre &gt; 5"&lt;/span>, 
  Sinon Si x = &lt;span class="hljs-number">5&lt;/span>, alors afficher &lt;span class="hljs-string">"nombre = 5"&lt;/span>, 
  Sinon, &lt;span class="hljs-string">"nombre &lt; 5"&lt;/span>. </code>
</div>

<small class="shcb-language" id="shcb-language-110"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">JavaScript</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">javascript</span><span class="shcb-language__paren">)</span></small></pre>

**En ISETL**, une structure conditionnelle se rédige de la façon suivante : 

<pre class="wp-block-code" aria-describedby="shcb-language-111" data-shcb-language-name="PHP" data-shcb-language-slug="php"><div>
  <code class="hljs language-php">&lt;span class="hljs-keyword">if&lt;/span> (condition) then .... 
  &lt;span class="hljs-keyword">elseif&lt;/span> (condition) then .....
  &lt;span class="hljs-keyword">else&lt;/span> .....
  end &lt;span class="hljs-keyword">if&lt;/span>; </code>
</div>

<small class="shcb-language" id="shcb-language-111"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">PHP</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">php</span><span class="shcb-language__paren">)</span></small></pre>

Comme vous pouvez le voir, **le « else » ne requiert pas de « then ».**

En reprenant notre exemple, nous avons donc

<pre class="wp-block-code" aria-describedby="shcb-language-112" data-shcb-language-name="PHP" data-shcb-language-slug="php"><div>
  <code class="hljs language-php">x:=&lt;span class="hljs-number">10&lt;/span>;
  &lt;span class="hljs-keyword">if&lt;/span> (x&lt;&lt;span class="hljs-number">5&lt;/span>) then 
          &lt;span class="hljs-keyword">print&lt;/span>(&lt;span class="hljs-string">"Nombre &lt; 5"&lt;/span>);
  &lt;span class="hljs-keyword">elseif&lt;/span> (x = &lt;span class="hljs-number">5&lt;/span>) then 
  	&lt;span class="hljs-keyword">print&lt;/span>(&lt;span class="hljs-string">"Nombre = 5"&lt;/span>);
  &lt;span class="hljs-keyword">else&lt;/span>
  	&lt;span class="hljs-keyword">print&lt;/span>(&lt;span class="hljs-string">"Nombre &gt; 5"&lt;/span>);
  end &lt;span class="hljs-keyword">if&lt;/span>;</code>
</div>

<small class="shcb-language" id="shcb-language-112"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">PHP</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">php</span><span class="shcb-language__paren">)</span></small></pre>

ISETL ne prenant pas en compte l&rsquo;indentation, il est aussi possible de rédiger ce code de cette façon : 

<pre class="wp-block-code" aria-describedby="shcb-language-113" data-shcb-language-name="PHP" data-shcb-language-slug="php"><div>
  <code class="hljs language-php">x:=&lt;span class="hljs-number">10&lt;/span>;
  &lt;span class="hljs-keyword">if&lt;/span> (x&lt;&lt;span class="hljs-number">5&lt;/span>) then &lt;span class="hljs-keyword">print&lt;/span>(&lt;span class="hljs-string">"Nombre &lt; 5"&lt;/span>);
  &lt;span class="hljs-keyword">elseif&lt;/span> (x = &lt;span class="hljs-number">5&lt;/span>) then &lt;span class="hljs-keyword">print&lt;/span>(&lt;span class="hljs-string">"Nombre = 5"&lt;/span>);
  &lt;span class="hljs-keyword">else&lt;/span> &lt;span class="hljs-keyword">print&lt;/span>(&lt;span class="hljs-string">"Nombre &gt; 5"&lt;/span>);
  end &lt;span class="hljs-keyword">if&lt;/span>;</code>
</div>

<small class="shcb-language" id="shcb-language-113"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">PHP</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">php</span><span class="shcb-language__paren">)</span></small></pre>

## Rédaction de conditions

Je vous propose un tableau récapitulatif présentant tous les opérateurs nécessaires à la rédaction de conditions en ISETL : 

x et y étant des nombres, A ou B étant des propositions.<figure class="wp-block-table">

<table>
  <tr>
    <td class="has-text-align-center" data-align="center">
      <strong>Opérateur ISETL </strong>
    </td>
    
    <td class="has-text-align-center" data-align="center">
      <strong>Description</strong>
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-center" data-align="center">
      x=y
    </td>
    
    <td class="has-text-align-center" data-align="center">
      x est égal à y
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-center" data-align="center">
      x\=y
    </td>
    
    <td class="has-text-align-center" data-align="center">
      x n&rsquo;est pas égal à y
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-center" data-align="center">
      x<y
    </td>
    
    <td class="has-text-align-center" data-align="center">
      x est inférieur à y
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-center" data-align="center">
      x<=y
    </td>
    
    <td class="has-text-align-center" data-align="center">
      x est inférieur ou égal à y
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-center" data-align="center">
      x>y
    </td>
    
    <td class="has-text-align-center" data-align="center">
      x est supérieur à y
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-center" data-align="center">
      x>=y
    </td>
    
    <td class="has-text-align-center" data-align="center">
      x est supérieur ou égal à y
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-center" data-align="center">
      A or B
    </td>
    
    <td class="has-text-align-center" data-align="center">
      Disjonction logique : A ou B
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-center" data-align="center">
      A and B
    </td>
    
    <td class="has-text-align-center" data-align="center">
      Conjonction logique : A et B
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-center" data-align="center">
      A impl B
    </td>
    
    <td class="has-text-align-center" data-align="center">
      Implication logique : A implique B
    </td>
  </tr>
  
  <tr>
    <td class="has-text-align-center" data-align="center">
      not A
    </td>
    
    <td class="has-text-align-center" data-align="center">
      Négation logique : Non A
    </td>
  </tr>
</table><figcaption>Tableau Récapitulatif Opérateurs Logiques ISETL</figcaption></figure> 

### Nota Bene 

Il faut bien prendre en compte que la condition d&rsquo;égalité en ISETL **s&rsquo;écrit avec un seul « égal »** contrairement au python, c++, java&#8230;. L&rsquo;affectation en ISETL étant « := ».

## Plus de tutoriels en ISETL 

<p class="has-text-align-center">
  <a href="https://keskec.fr/tag/isetl/" class="rank-math-link">ISETL &#8211; KeskeC</a>
</p>