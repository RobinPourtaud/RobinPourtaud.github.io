---
title: 'Déterminisation d&rsquo;un automate'
author: Robin Pourtaud
type: post
date: 2020-12-30T10:55:55+00:00
url: /sciences/informatique/robin/4956/
featured_image: /wp-content/uploads/2020/12/Images-KeskeC-1568x882.png
rank_math_seo_score:
  - "80"
ads-for-wp-visibility:
  - show
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_primary_category:
  - "8"
rank_math_focus_keyword:
  - Automate
categories:
  - Informatique
tags:
  - Automate

---
Cet article présente une méthode afin de convertir un automate fini non déterministe quelconque (AFN) en automate déterministe (AFD). Afin d&rsquo;illustrer cette méthode, un exercice corrigé sera utilisé comme support. Les étapes de l&rsquo;algorithme de conversion seront explicitées de façon tabulaire. 

## Définition : 

Un automate est dit déterministe s&rsquo;il respecte trois conditions :

  1. Il possède un unique état initial.
  2. Il ne possède pas d’epsilon-transitions.
  3. Pour chaque état de cet automate, il existe au maximum une transition issue de cet état possédant le même symbole.

Pour en savoir plus : [Différents types d’automates finis][1]{.rank-math-link}

## Méthode : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-18-1024x602.png" alt="" class="wp-image-4961" width="501" height="294" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-18-1024x602.png 1024w, https://keskec.fr/wp-content/uploads/2020/12/image-18-300x176.png 300w, https://keskec.fr/wp-content/uploads/2020/12/image-18-768x451.png 768w, https://keskec.fr/wp-content/uploads/2020/12/image-18.png 1435w" sizes="(max-width: 501px) 100vw, 501px" /><figcaption>Automate fini non déterministe</figcaption></figure>
</div>

La méthode permettant de passer d&rsquo;un automate fini quelconque à un automate déterministe va être illustrée par l&rsquo;exercice corrigé suivant : 

Soit, un automate fini X sur l&rsquo;alphabet {a,b} (le mot vide étant lambda) : 

Calculons l&rsquo;automate déterministe Y équivalent à X par la méthode des sous-ensembles d&rsquo;états. 

### Étape 1 : Construction du tableau

Soit le tableau à 4 entrées suivant : <figure class="wp-block-table">

<table class="has-fixed-layout">
  <tr>
    <td>
      <strong>Nouvel état</strong>
    </td>
    
    <td>
      <strong>Nouvel état initial, final ou non</strong>
    </td>
    
    <td>
      <strong>a</strong>
    </td>
    
    <td>
      b
    </td>
  </tr>
</table><figcaption>Colonnes du tableau</figcaption></figure> 

  1. « Nouvel état » correspond au futur état de notre automate déterministe.
  2. « Nouvel état initial, final ou non » correspond au type de l&rsquo;état de notre automate déterministe. 
  3. Le reste des colonnes correspond aux symboles des transitions partant de ce nouvel état. Il y a autant de colonnes que le cardinal de l&rsquo;alphabet de l&rsquo;automate. 

Commençons avec la première ligne : <figure class="wp-block-table">

<table class="has-fixed-layout">
  <tr>
    <td>
      <strong>Nouvel état</strong>
    </td>
    
    <td>
      <strong>Nouvel état initial, final ou non</strong>
    </td>
    
    <td>
      <strong>a</strong>
    </td>
    
    <td>
      <strong>b</strong>
    </td>
  </tr>
  
  <tr>
    <td>
      A={q0, q1}
    </td>
    
    <td>
      Initial
    </td>
    
    <td>
      {q0,q1} = A
    </td>
    
    <td>
      {q2,q4} = B
    </td>
  </tr>
  
  <tr>
    <td>
      B={q2,q4}
    </td>
    
    <td>
    </td>
    
    <td>
    </td>
    
    <td>
    </td>
  </tr>
</table><figcaption>Colonnes du tableau</figcaption></figure> 

NB : Les noms des nouveaux états sont purement arbitraires. 

#### 1) Recherche de l&rsquo;état initial : 

L&rsquo;état initial de X est q0. Une epsilon-transition de q0 vers q1 nous permet de réunir q0 et q1. 

#### 2) Initial ? Final ? 

q0 est l&rsquo;état initial de X, alors A contenant q0 le sera aussi. (c&rsquo;est l&rsquo;unique état initial)

A ne contient pas d&rsquo;état final, il ne le sera donc pas lui-même. 

#### 3) Transitions ? 

A partir de q0 ou de q1, il existe 2 transitions « a » se dirigeant vers q0, q1. Cet état existe. On s&rsquo;arrête. 

A partir de q0 ou de q1, il existe une transition « b » se dirigeant vers q2. Cet état n&rsquo;existe pas, créons-le. 

#### 4) Répétons les étapes

A partir de ces nouveaux états, recommencer depuis l&rsquo;étape 2 jusqu&rsquo;à ce qu&rsquo;il n&rsquo;y ait plus de nouveaux états à être créés: 

#### Résultat : <figure class="wp-block-table">

<table>
  <tr>
    <td>
      <strong>Nouvel état</strong>
    </td>
    
    <td>
      <strong>Nouvel état initial, final ou non</strong>
    </td>
    
    <td>
      <strong>a</strong>
    </td>
    
    <td>
      <strong>b</strong>
    </td>
  </tr>
  
  <tr>
    <td>
      A={q0, q1}
    </td>
    
    <td>
      Initial
    </td>
    
    <td>
      {q0,q1} = A
    </td>
    
    <td>
      {q2,q4} = B
    </td>
  </tr>
  
  <tr>
    <td>
      B={q2,q4}
    </td>
    
    <td>
      non
    </td>
    
    <td>
      {q1,q5,q7} = C
    </td>
    
    <td>
      <strong>Ø</strong>
    </td>
  </tr>
  
  <tr>
    <td>
      C = {q1,q5,q7}
    </td>
    
    <td>
      final
    </td>
    
    <td>
      {q1,q8} = D
    </td>
    
    <td>
      {q7,q4,q8} = E
    </td>
  </tr>
  
  <tr>
    <td>
      D = {q1,q8}
    </td>
    
    <td>
      final
    </td>
    
    <td>
      {q1,q8} = D
    </td>
    
    <td>
      {q4} = F
    </td>
  </tr>
  
  <tr>
    <td>
      E = {q7,q4,q8}
    </td>
    
    <td>
      final
    </td>
    
    <td>
      {q5,q8} = G
    </td>
    
    <td>
      {q7,q8} = H
    </td>
  </tr>
  
  <tr>
    <td>
      F = {q4}
    </td>
    
    <td>
      non
    </td>
    
    <td>
      {q5} = I
    </td>
    
    <td>
      <strong>Ø</strong>
    </td>
  </tr>
  
  <tr>
    <td>
      G ={q5,q8}
    </td>
    
    <td>
      final
    </td>
    
    <td>
      {q8} = J
    </td>
    
    <td>
      {q7} = K
    </td>
  </tr>
  
  <tr>
    <td>
      H = {q7,q8}
    </td>
    
    <td>
      final
    </td>
    
    <td>
      {q8} = J
    </td>
    
    <td>
      {q7,q8} = H
    </td>
  </tr>
  
  <tr>
    <td>
      I = {q5}
    </td>
    
    <td>
      non
    </td>
    
    <td>
      {q8} = J
    </td>
    
    <td>
      {q7}=k
    </td>
  </tr>
  
  <tr>
    <td>
      J = {q8}
    </td>
    
    <td>
      final
    </td>
    
    <td>
      {q8} = J
    </td>
    
    <td>
      <strong>Ø</strong>
    </td>
  </tr>
  
  <tr>
    <td>
      K = {q7}
    </td>
    
    <td>
      final
    </td>
    
    <td>
      <strong>Ø</strong>
    </td>
    
    <td>
      {q7,q8}=H
    </td>
  </tr>
</table></figure> 

q6 et q3 étant soit des états inaccessibles, soit des états stériles, ont été ignorés. 

### Étape 2 : Modélisation de l&rsquo;automate à partir du tableau

Afin de tracer l&rsquo;automate il nous suffit de créer des états de A à K, et de les relier en fonction de nos nouvelles transitions. 

Vous devriez obtenir cet automate : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-19-1024x491.png" alt="" class="wp-image-4962" width="690" height="331" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-19-1024x491.png 1024w, https://keskec.fr/wp-content/uploads/2020/12/image-19-300x144.png 300w, https://keskec.fr/wp-content/uploads/2020/12/image-19-768x368.png 768w, https://keskec.fr/wp-content/uploads/2020/12/image-19-1536x736.png 1536w, https://keskec.fr/wp-content/uploads/2020/12/image-19-2048x981.png 2048w, https://keskec.fr/wp-content/uploads/2020/12/image-19-1568x751.png 1568w" sizes="(max-width: 690px) 100vw, 690px" /><figcaption>Automate équivalent déterministe</figcaption></figure>
</div>

## Source : 

  1. [AUTOMATES À ÉTATS FINIS DÉTERMINISATION][2]{.rank-math-link}

 [1]: https://keskec.fr/sciences/informatique/robin/4870/
 [2]: https://perso.liris.cnrs.fr/sylvain.brandel/wiki/lib/exe/fetch.php?media=ens:liflf:liflf-cm04.pdf