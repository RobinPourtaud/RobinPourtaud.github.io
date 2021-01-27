---
title: 'Parcours d&rsquo;un arbre binaire'
author: Robin Pourtaud
type: post
date: 2021-01-05T20:19:41+00:00
url: /sciences/informatique/robin/4914/
featured_image: /wp-content/uploads/2020/12/Images-KeskeC-4-1568x882.png
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
  - Arbre Binaire
categories:
  - Informatique
tags:
  - Arbre Binaire

---
Cet article présente les différents parcours d&rsquo;un arbre binaire : les plus communs. Les différents algorithmes de parcours ainsi qu&rsquo;un exemple y seront explicités. 

## Différents parcours : 

Commentaire : Par abus de langage, nous utiliserons le mot Arbre pour désigner une arborescence. 

Soit Arbre, une structure telle que pour un arbre A: 

  * A.e est l&rsquo;élément du noeud de l&rsquo;arbre
  * A.g est le fils gauche de A
  * A.d est le fils droit de A

### Parcours préfixe

L&rsquo;algorithme de parcours préfixe est le suivant : 

<pre class="wp-block-code" aria-describedby="shcb-language-131" data-shcb-language-name="HTML, XML" data-shcb-language-slug="xml"><div>
  <code class="hljs language-xml">Procédure préfixe(Arbre A) : 
  Début : 
     Afficher(A.e)
     Si A.g != null : 
        préfixe(A.g)
     FinSi
     Si A.d != null : 
        préfixe(A.d)
     FinSi
  Fin</code>
</div>

<small class="shcb-language" id="shcb-language-131"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">HTML, XML</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">xml</span><span class="shcb-language__paren">)</span></small></pre>

### Parcours infixe

L&rsquo;algorithme de parcours infixe est le suivant : 

<pre class="wp-block-code" aria-describedby="shcb-language-132" data-shcb-language-name="HTML, XML" data-shcb-language-slug="xml"><div>
  <code class="hljs language-xml">Procédure infixe(Arbre A) : 
  Début : 
     Si A.g != null : 
        infixe(A.g)
     FinSi
     Afficher(A.e)
     Si A.d != null : 
        infixe(A.d)
     FinSi
  Fin</code>
</div>

<small class="shcb-language" id="shcb-language-132"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">HTML, XML</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">xml</span><span class="shcb-language__paren">)</span></small></pre>

### Parcours suffixe

L&rsquo;algorithme de parcours suffixe est le suivant : 

<pre class="wp-block-code" aria-describedby="shcb-language-133" data-shcb-language-name="HTML, XML" data-shcb-language-slug="xml"><div>
  <code class="hljs language-xml">Procédure suffixe(Arbre A) : 
     Si A.g != null : 
        suffixe(A.g)
     FinSi
     Si A.d != null : 
        suffixe(A.d)
     FinSi
     Afficher(A.e)</code>
</div>

<small class="shcb-language" id="shcb-language-133"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">HTML, XML</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">xml</span><span class="shcb-language__paren">)</span></small></pre>

### Parcours en largeur

L&rsquo;algorithme de parcours en largeur est le suivant :

<pre class="wp-block-code" aria-describedby="shcb-language-134" data-shcb-language-name="HTML, XML" data-shcb-language-slug="xml"><div>
  <code class="hljs language-xml">Procédure largeur(Arbre A) : 
     Données : File-vide f, Arbre i
     Début : f.ajouter(A)
             Tantque (!f.estVide()) : 
                i = f.prendre()
                Afficher(i.e) 
                Si (i.g != null) : 
                   f.ajouter(i.g)
                FinSi
                Si (i.d != null) :
                   f.ajouter(i.d)
                FinSi
             FinTantque
     Fin
     </code>
</div>

<small class="shcb-language" id="shcb-language-134"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">HTML, XML</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">xml</span><span class="shcb-language__paren">)</span></small></pre>

## Exemple 

Soit l&rsquo;ABR suivant : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-32.png" alt="" class="wp-image-5100" width="258" height="232" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-32.png 562w, https://keskec.fr/wp-content/uploads/2020/12/image-32-300x270.png 300w" sizes="(max-width: 258px) 100vw, 258px" /><figcaption>Exemple : arbre binaire</figcaption></figure>
</div>

  * Parcours préfixe : + \* 1 7 \* 3 2
  * Parcours suffixe ou postfixe : 1 7 \* 3 2 \* +
  * Parcours symétrique ou infixe : 1 \* 7 + 3 \* 2
  * Parcours en largeur : + \* \* 1 7 3 2

## Commentaire : 

Le résultat obtenu par le parcours suffixe de l&rsquo;arbre binaire est similaire à la notion de « notation polonaise inversé » ou « notation post-fixé », notamment utilisée dans le passé dans certaines calculatrices HP. Cette notation présentait plusieurs intérêts. 

Si vous êtes intéressé pour en savoir plus, le sujet de la notation polonaise inverse est introduite dans cette vidéo de Computerphile :<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">

<div class="wp-block-embed__wrapper">
</div></figure> 

## Sources : 

  1. [Parcours d&rsquo;arbre &#8211; irif.fr][1]{.rank-math-link}
  2. [Parcours d’un arbre binaire &#8211; Irem de Lyon][2]{.rank-math-link}
  3. [Notation Polonaise Inverse &#8211; Wikipédia][3]{.rank-math-link}
  4. [Notations infixée, préfixée, polonaise et postfixée &#8211; Wikipédia][4]{.rank-math-link}

 [1]: https://www.irif.fr/~carton/Enseignement/Algorithmique/LicenceMathInfo/Programmation/Tree/parcours.html
 [2]: http://math.univ-lyon1.fr/irem/IMG/pdf/parcours_arbre_avec_solutions-2.pdf
 [3]: https://fr.wikipedia.org/wiki/Notation_polonaise_inverse
 [4]: https://fr.wikipedia.org/wiki/Notations_infix%C3%A9e,_pr%C3%A9fix%C3%A9e,_polonaise_et_postfix%C3%A9e