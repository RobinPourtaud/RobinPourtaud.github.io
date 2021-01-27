---
title: ISETL – Syntaxe des fonctions
author: Robin Pourtaud
type: post
date: 2020-07-24T16:16:00+00:00
url: /sciences/informatique/robin/3823/
featured_image: /wp-content/uploads/2020/07/ISETLW-1568x864.png
rank_math_seo_score:
  - "72"
rank_math_primary_category:
  - "8"
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_focus_keyword:
  - fonctions
rank_math_analytic_object_id:
  - "31"
categories:
  - Informatique
tags:
  - ISETL
  - Tutoriel

---
Interactive SET Language (ISETL) est un langage de programmation basé sur SETL. Développé par Garry Levin en 1988, il avait pour finalité&nbsp;**l’enseignement des mathématiques discrètes à l’université**. Possédant une syntaxe atypique, ISETL est un langage difficile à appréhender pour un néophyte. Dans ce tutoriel, nous introduirons le concept de fonction en ISETL, partant d&rsquo;une définition générale puis en prenant 3 exemples. 

## Fonction en ISETL 

### Définition : 

Comme dans d&rsquo;autres langages de programmation, une fonction dans ISETL est une entité informatique permettant l&rsquo;encapsulation d&rsquo;une partie de code. Elle peut prendre zéro, une ou plusieurs entrées et retourne une valeur (ou non, on parlera alors de procédures). 

### La syntaxe : 

En ISETL, la syntaxe des fonctions ne repose pas sur l&rsquo;indentation, ni sur des accolades :  
Une fonction commence par **func();** et se fini par **end func();**. Ainsi : 

<pre class="wp-block-code" aria-describedby="shcb-language-107" data-shcb-language-name="JavaScript" data-shcb-language-slug="javascript"><div>
  <code class="hljs language-javascript">VotreFonction := func(param1);
  &lt;span class="hljs-keyword">return&lt;/span> param1;
  end func; </code>
</div>

<small class="shcb-language" id="shcb-language-107"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">JavaScript</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">javascript</span><span class="shcb-language__paren">)</span></small></pre>

Pour exécuter cette fonction avec le paramètre 5 : 

<pre class="wp-block-code"><div>
  <code class="hljs">VotreFonction(5);</code>
</div></pre>

Vous devriez voir sur le terminal d&rsquo;exécution affiché « 5; ».

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/07/image-5.png" alt="" class="wp-image-3827" width="261" height="153" srcset="https://keskec.fr/wp-content/uploads/2020/07/image-5.png 606w, https://keskec.fr/wp-content/uploads/2020/07/image-5-300x176.png 300w, https://keskec.fr/wp-content/uploads/2020/07/image-5-150x88.png 150w" sizes="(max-width: 261px) 100vw, 261px" /><figcaption>ISETL &#8211; Syntaxe d&rsquo;une fonction</figcaption></figure>
</div>

## Exemples de fonctions 

### Exemple 1 : 



On souhaite créer une fonction retournant **le produit cartésien de 2 ensembles**.

On appelle produit cartésien de 2 ensembles<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-723e679f55a179fd190ab7037aa2f44e_l3.svg" class="ql-img-inline-formula " alt="&#101;&#95;&#49;" title="Rendered by QuickLaTeX.com" height="12" width="16" style="vertical-align: -3px;" /> et<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-6feb4d7d2bb5ccfbdb7414c92aa560eb_l3.svg" class="ql-img-inline-formula " alt="&#101;&#95;&#50;" title="Rendered by QuickLaTeX.com" height="12" width="16" style="vertical-align: -3px;" /> , l&rsquo;ensemble des couples (i,j) tel que<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-0192ae7c4acd9ba3c8be63f54cbf4d0c_l3.svg" class="ql-img-inline-formula " alt="&#105;&#92;&#105;&#110;&#32;&#101;&#95;&#49;" title="Rendered by QuickLaTeX.com" height="16" width="47" style="vertical-align: -3px;" /> et<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-39060ef41734297ec5a3d24fc2231c73_l3.svg" class="ql-img-inline-formula " alt="&#106;&#92;&#105;&#110;&#32;&#101;&#95;&#50;" title="Rendered by QuickLaTeX.com" height="17" width="51" style="vertical-align: -4px;" /> .

Si<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-cda5eb58c1ddaf41df794c462c85f2bd_l3.svg" class="ql-img-inline-formula " alt="&#101;&#95;&#49;&#32;&#61;&#32;&#92;&#123;&#120;&#44;&#121;&#92;&#125;" title="Rendered by QuickLaTeX.com" height="20" width="94" style="vertical-align: -5px;" /> et<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-64bd03e768e25d043c9f56831bb5f463_l3.svg" class="ql-img-inline-formula " alt="&#101;&#95;&#50;&#32;&#61;&#32;&#92;&#123;&#49;&#44;&#50;&#92;&#125;" title="Rendered by QuickLaTeX.com" height="20" width="93" style="vertical-align: -5px;" /> , alors<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-b9fe44ef83319ff3cd815b711128439f_l3.svg" class="ql-img-inline-formula " alt="&#101;&#95;&#49;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#101;&#95;&#50;&#32;&#61;&#32;&#92;&#123;&#40;&#120;&#44;&#49;&#41;&#59;&#40;&#120;&#44;&#50;&#41;&#59;&#40;&#121;&#44;&#49;&#41;&#59;&#40;&#121;&#44;&#50;&#41;&#92;&#125;" title="Rendered by QuickLaTeX.com" height="20" width="315" style="vertical-align: -5px;" /> .

Nous avons donc : 

<pre class="wp-block-code" aria-describedby="shcb-language-108" data-shcb-language-name="JavaScript" data-shcb-language-slug="javascript"><div>
  <code class="hljs language-javascript">cartesien := func(e1,e2);
  &lt;span class="hljs-keyword">return&lt;/span> {[x,y]:x &lt;span class="hljs-keyword">in&lt;/span> e1, y &lt;span class="hljs-keyword">in&lt;/span> e2};
  end func;</code>
</div>

<small class="shcb-language" id="shcb-language-108"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">JavaScript</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">javascript</span><span class="shcb-language__paren">)</span></small></pre>

La deuxième ligne se lit comme « retourner l&rsquo;ensemble de tous les couples (x,y) tel que x appartient à e1 et y à e2 ».

### Exemple 2 : 

Pour ce deuxième exemple, nous souhaitons prendre la somme de tous les éléments d&rsquo;un ensemble mais de **façon récursive**.

Par exemple pour l&rsquo;ensemble {1,2,3}, nous souhaitons retourner 6.

Je vous propose une fonction (plus complexe que nécessaire) pour vous familiariser avec la syntaxe ISETL. 

<pre class="wp-block-code" aria-describedby="shcb-language-109" data-shcb-language-name="Bash" data-shcb-language-slug="bash"><div>
  <code class="hljs language-bash">somme:=func(e);
  &lt;span class="hljs-built_in">local&lt;/span> x;
  &lt;span class="hljs-keyword">if&lt;/span> (&lt;span class="hljs-comment">#e = 1) then return arb(e);&lt;/span>
  &lt;span class="hljs-keyword">else&lt;/span>
    take x from e;
    &lt;span class="hljs-built_in">return&lt;/span> x + somme(e);
  end &lt;span class="hljs-keyword">if&lt;/span>;
  end func;</code>
</div>

<small class="shcb-language" id="shcb-language-109"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Bash</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">bash</span><span class="shcb-language__paren">)</span></small></pre>

_Note : « #e » est le cardinal de e, « arb(e) » est un nombre arbitraire contenu dans e, « take x from e » permet de retirer une valeur de e et de la stocker dans une variable x._

Comme escompté : 

<pre class="wp-block-code"><div>
  <code class="hljs">somme({8,6,9});</code>
</div></pre>

retourne « 23; ».

## Plus de tutoriels sur ISETL ici : 

<p class="has-text-align-center">
  <a href="https://keskec.fr/tag/isetl/" class="rank-math-link">Article sur ISETL de KeskeC</a>
</p>