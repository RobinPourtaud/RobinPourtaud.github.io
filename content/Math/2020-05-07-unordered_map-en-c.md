---
title: unordered_map en C++
author: Robin Pourtaud
type: post
date: 2020-05-07T13:00:00+00:00
url: /sciences/informatique/robin/1586/
featured_image: /wp-content/uploads/2020/05/codeC-1568x1045.jpg
rank_math_seo_score:
  - "71"
itemlist_item_1493:
  - 'a:0:{}'
music_composer_1493:
  - 'a:0:{}'
movie_actor_1493:
  - 'a:0:{}'
article_items_1493:
  - 'a:0:{}'
image_object_exif_data_1493:
  - 'a:0:{}'
blogposting_items_1493:
  - 'a:0:{}'
newsarticle_items_1493:
  - 'a:0:{}'
tech_article_items_1493:
  - 'a:0:{}'
product_reviews_1493:
  - 'a:0:{}'
feed_element_1493:
  - 'a:0:{}'
faq_question_1493:
  - 'a:0:{}'
performer_1493:
  - 'a:0:{}'
accepted_answer_1493:
  - 'a:0:{}'
suggested_answer_1493:
  - 'a:0:{}'
howto_supply_1493:
  - 'a:0:{}'
howto_tool_1493:
  - 'a:0:{}'
howto_step_1493:
  - 'a:0:{}'
announcement_location_1493:
  - 'a:0:{}'
music_playlist_track_1493:
  - 'a:0:{}'
music_album_track_1493:
  - 'a:0:{}'
apartment_amenities_1493:
  - 'a:0:{}'
additional_property_1493:
  - 'a:0:{}'
mc_cause_1493:
  - 'a:0:{}'
mc_symptom_1493:
  - 'a:0:{}'
mc_risk_factor_1493:
  - 'a:0:{}'
tvseries_actor_1493:
  - 'a:0:{}'
tvseries_season_1493:
  - 'a:0:{}'
trip_itinerary_1493:
  - 'a:0:{}'
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_primary_category:
  - "8"
rank_math_focus_keyword:
  - unordered_map
rank_math_analytic_object_id:
  - "82"
categories:
  - Informatique
tags:
  - C++
  - Complexité asymptotique
  - Unordered_map

---
Le conteneur unordered\_map est un tableau associatif (ou table associative). Il permet l&rsquo;association d&rsquo;une clé du type de son choix à une valeur. Comme son nom l&rsquo;indique, les éléments de l&rsquo;unordered\_map ne sont pas rangés, que ce soit par leurs clés ou par leurs valeurs associées (contrairement à « map »).

## Intérêts :

L’intérêt principal de l&rsquo;utilisation d&rsquo;une unordered_map par rapport à un autre conteneur (notamement une map) est sa faible complexité asymptotique de recherche ou d&rsquo;insertion moyenne (en O(1)). 

## Exemple : 

En tant qu&rsquo;exemple, je vais créer un tableau associant un animal à son âge.

### Définition : 

<pre class="wp-block-code" aria-describedby="shcb-language-46" data-shcb-language-name="C++" data-shcb-language-slug="cpp"><div>
  <code class="hljs language-cpp">&lt;span class="hljs-meta">#&lt;span class="hljs-meta-keyword">include&lt;/span> &lt;span class="hljs-meta-string">&lt;iostream&gt; //Cout, endl,etc&lt;/span>&lt;/span>
  &lt;span class="hljs-meta">#&lt;span class="hljs-meta-keyword">include&lt;/span> &lt;span class="hljs-meta-string">&lt;string&gt;&lt;/span>&lt;/span>
  &lt;span class="hljs-meta">#&lt;span class="hljs-meta-keyword">include&lt;/span> &lt;span class="hljs-meta-string">&lt;unordered_map&gt;&lt;/span>&lt;/span>
  &lt;span class="hljs-function">&lt;span class="hljs-keyword">int&lt;/span> &lt;span class="hljs-title">main&lt;/span>&lt;span class="hljs-params">()&lt;/span>&lt;/span>{
     &lt;span class="hljs-comment">/*
      * Tableau associatif associant une clé de type string
      * à un int.
      * Concrètement, MaMap associant un animal à son âge
     */&lt;/span>
     &lt;span class="hljs-built_in">std&lt;/span>::&lt;span class="hljs-built_in">unordered_map&lt;/span>&lt;&lt;span class="hljs-built_in">std&lt;/span>::&lt;span class="hljs-built_in">string&lt;/span>,&lt;span class="hljs-keyword">int&lt;/span>&gt; MaMap = {
                                        {&lt;span class="hljs-string">"Chien"&lt;/span>,&lt;span class="hljs-number">1&lt;/span>},
                                        {&lt;span class="hljs-string">"Chat"&lt;/span>,&lt;span class="hljs-number">3&lt;/span>},
                                        {&lt;span class="hljs-string">"Rat"&lt;/span>,&lt;span class="hljs-number">10&lt;/span>},
                                        {&lt;span class="hljs-string">"Chameau"&lt;/span>,&lt;span class="hljs-number">3&lt;/span>}
                                      };
     &lt;span class="hljs-comment">// Le reste des parties ce situent ici&lt;/span>
  
     &lt;span class="hljs-keyword">return&lt;/span> &lt;span class="hljs-number">0&lt;/span>;
  }</code>
</div>

<small class="shcb-language" id="shcb-language-46"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">C++</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">cpp</span><span class="shcb-language__paren">)</span></small></pre>

### Insertion : 

Complexité moyenne en O(1).

#### Méthode 1 : std::unordered_map::emplace

<pre class="wp-block-code" aria-describedby="shcb-language-47" data-shcb-language-name="C++" data-shcb-language-slug="cpp"><div>
  <code class="hljs language-cpp">MaMap.emplace(&lt;span class="hljs-string">"Castor"&lt;/span>,&lt;span class="hljs-number">2&lt;/span>);
  MaMap.emplace(&lt;span class="hljs-string">"Tortue"&lt;/span>,&lt;span class="hljs-number">1&lt;/span>);
  &lt;span class="hljs-comment">//Avec make_pair&lt;/span>
  MaMap.emplace(&lt;span class="hljs-built_in">std&lt;/span>::make_pair(&lt;span class="hljs-string">"Oiseau"&lt;/span>,&lt;span class="hljs-number">4&lt;/span>));</code>
</div>

<small class="shcb-language" id="shcb-language-47"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">C++</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">cpp</span><span class="shcb-language__paren">)</span></small></pre>

#### Méthode 2 : std::unordered_map::insert

<pre class="wp-block-code" aria-describedby="shcb-language-48" data-shcb-language-name="C++" data-shcb-language-slug="cpp"><div>
  <code class="hljs language-cpp">MaMap.insert({&lt;span class="hljs-string">"Castor"&lt;/span>,&lt;span class="hljs-number">2&lt;/span>});
  
  &lt;span class="hljs-comment">// Insert avec std::make_pair&lt;/span>
  MaMap.insert(&lt;span class="hljs-built_in">std&lt;/span>::make_pair&lt;&lt;span class="hljs-built_in">std&lt;/span>::&lt;span class="hljs-built_in">string&lt;/span>,&lt;span class="hljs-keyword">int&lt;/span>&gt;(&lt;span class="hljs-string">"Lézard"&lt;/span>,&lt;span class="hljs-number">2&lt;/span>));
  
  &lt;span class="hljs-comment">// Insert plusieurs valeurs en même temps&lt;/span>
  MaMap.insert({{&lt;span class="hljs-string">"Souris"&lt;/span>,&lt;span class="hljs-number">1&lt;/span>},{&lt;span class="hljs-string">"Girafe"&lt;/span>,&lt;span class="hljs-number">6&lt;/span>}});</code>
</div>

<small class="shcb-language" id="shcb-language-48"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">C++</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">cpp</span><span class="shcb-language__paren">)</span></small></pre>

#### Méthode 3 : Operateur[]

<pre class="wp-block-code" aria-describedby="shcb-language-49" data-shcb-language-name="C++" data-shcb-language-slug="cpp"><div>
  <code class="hljs language-cpp">&lt;span class="hljs-comment">// On insère dans MaMap la clé Cochon associée à 4&lt;/span>
  MaMap[&lt;span class="hljs-string">"Cochon"&lt;/span>] = &lt;span class="hljs-number">4&lt;/span>;</code>
</div>

<small class="shcb-language" id="shcb-language-49"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">C++</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">cpp</span><span class="shcb-language__paren">)</span></small></pre>

### Accéder/Rechercher : 

Complexité moyenne en O(1), linéaire dans le pire cas.

#### Méthode 1 : Operateur[]

<pre class="wp-block-code" aria-describedby="shcb-language-50" data-shcb-language-name="C++" data-shcb-language-slug="cpp"><div>
  <code class="hljs language-cpp">&lt;span class="hljs-built_in">std&lt;/span>::&lt;span class="hljs-built_in">cout&lt;/span> &lt;&lt; &lt;span class="hljs-string">"Ma Souris a "&lt;/span> &lt;&lt; MaMap[&lt;span class="hljs-string">"Souris"&lt;/span>] &lt;&lt; &lt;span class="hljs-string">" an."&lt;/span> &lt;&lt; &lt;span class="hljs-built_in">std&lt;/span>::&lt;span class="hljs-built_in">endl&lt;/span>;
  
  &lt;span class="hljs-comment">// Affichage : "Ma Souris a 1 an"&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-50"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">C++</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">cpp</span><span class="shcb-language__paren">)</span></small></pre>

#### Méthode 2 : std::unoredered_map::at

<pre class="wp-block-code" aria-describedby="shcb-language-51" data-shcb-language-name="C++" data-shcb-language-slug="cpp"><div>
  <code class="hljs language-cpp">&lt;span class="hljs-built_in">std&lt;/span>::&lt;span class="hljs-built_in">cout&lt;/span> &lt;&lt; &lt;span class="hljs-string">"Mon chat a "&lt;/span> &lt;&lt; MaMap.at(&lt;span class="hljs-string">"Chat"&lt;/span>) &lt;&lt; &lt;span class="hljs-string">" ans."&lt;/span> &lt;&lt; &lt;span class="hljs-built_in">std&lt;/span>::&lt;span class="hljs-built_in">endl&lt;/span>;
  
  &lt;span class="hljs-comment">// Affichage : "Mon chat a 3 ans."&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-51"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">C++</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">cpp</span><span class="shcb-language__paren">)</span></small></pre>

#### Méthode 3 : std::unoredered_map::find + iterator

Find permet en plus de tester si la clé est présente ou non dans l&rsquo;unordered_map avec un itérateur.

<pre class="wp-block-code" aria-describedby="shcb-language-52" data-shcb-language-name="C++" data-shcb-language-slug="cpp"><div>
  <code class="hljs language-cpp">&lt;span class="hljs-built_in">std&lt;/span>::&lt;span class="hljs-built_in">string&lt;/span> search = &lt;span class="hljs-string">"Castor"&lt;/span>;
  
  &lt;span class="hljs-keyword">auto&lt;/span> it = MaMap.find(search);
  &lt;span class="hljs-keyword">if&lt;/span> (it == MaMap.end()){
    &lt;span class="hljs-keyword">throw&lt;/span> &lt;span class="hljs-built_in">std&lt;/span>::&lt;span class="hljs-built_in">string&lt;/span>(&lt;span class="hljs-string">"Pas de "&lt;/span> + search);
  }
  &lt;span class="hljs-keyword">else&lt;/span>{
    &lt;span class="hljs-built_in">std&lt;/span>::&lt;span class="hljs-built_in">cout&lt;/span> &lt;&lt; it-&gt;first &lt;&lt; &lt;span class="hljs-string">" a "&lt;/span> &lt;&lt; it-&gt;second &lt;&lt; &lt;span class="hljs-string">" ans."&lt;/span> &lt;&lt; &lt;span class="hljs-built_in">std&lt;/span>::&lt;span class="hljs-built_in">endl&lt;/span>;
  }
  &lt;span class="hljs-comment">// Affichage : "Castor a 2 ans."&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-52"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">C++</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">cpp</span><span class="shcb-language__paren">)</span></small></pre>

### Modifier : 

Complexité moyenne en O(1), linéaire dans le pire cas.

#### Méthode 1 : Operateur[]

<pre class="wp-block-code" aria-describedby="shcb-language-53" data-shcb-language-name="C++" data-shcb-language-slug="cpp"><div>
  <code class="hljs language-cpp">MaMap[&lt;span class="hljs-string">"Castor"&lt;/span>] = &lt;span class="hljs-number">3&lt;/span>;
  &lt;span class="hljs-comment">// Castor est maintenant associé à la valeur 3&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-53"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">C++</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">cpp</span><span class="shcb-language__paren">)</span></small></pre>

#### Méthode 2 : std::unoredered_map::at

<pre class="wp-block-code" aria-describedby="shcb-language-54" data-shcb-language-name="C++" data-shcb-language-slug="cpp"><div>
  <code class="hljs language-cpp">MaMap.at(&lt;span class="hljs-string">"Castor"&lt;/span>) += &lt;span class="hljs-number">6&lt;/span>;
  &lt;span class="hljs-comment">// Castor est maintenant associé à la valeur 9&lt;/span>
  MaMap.at(&lt;span class="hljs-string">"Castor"&lt;/span>) = &lt;span class="hljs-number">20&lt;/span>;
  &lt;span class="hljs-comment">// Castor est maintenant associé à la valeur 20&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-54"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">C++</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">cpp</span><span class="shcb-language__paren">)</span></small></pre>

#### Méthode 3 : std::unoredered_map::find

<pre class="wp-block-code" aria-describedby="shcb-language-55" data-shcb-language-name="C++" data-shcb-language-slug="cpp"><div>
  <code class="hljs language-cpp">&lt;span class="hljs-built_in">std&lt;/span>::&lt;span class="hljs-built_in">string&lt;/span> search = &lt;span class="hljs-string">"Castor"&lt;/span>;
  
  &lt;span class="hljs-keyword">auto&lt;/span> it = MaMap.find(search);
  &lt;span class="hljs-keyword">if&lt;/span> (it == MaMap.end()){
    &lt;span class="hljs-keyword">throw&lt;/span> &lt;span class="hljs-built_in">std&lt;/span>::&lt;span class="hljs-built_in">string&lt;/span>(&lt;span class="hljs-string">"Pas de "&lt;/span> + search);
  }
  &lt;span class="hljs-keyword">else&lt;/span>{
    it-&gt;second = &lt;span class="hljs-number">5&lt;/span>;
  }
  &lt;span class="hljs-comment">// Castor est maintenant associé à la valeur 5&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-55"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">C++</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">cpp</span><span class="shcb-language__paren">)</span></small></pre>

### Supprimer : 

Complexité moyenne en O(1), linéaire dans le pire cas.

<pre class="wp-block-code" aria-describedby="shcb-language-56" data-shcb-language-name="C++" data-shcb-language-slug="cpp"><div>
  <code class="hljs language-cpp">Mamap.erase(&lt;span class="hljs-string">"Castor"&lt;/span>);
  &lt;span class="hljs-comment">//L'entrée Castor -&gt; 3 est maintenant effacée&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-56"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">C++</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">cpp</span><span class="shcb-language__paren">)</span></small></pre>

### Aspect mathématique : 

On pourrait penser que **la relation associative** du conteneur est comparable à une fonction surjective non injective, mais elle est en faite une **fonction bijective**. 

En effet, chaque clé (ensemble de départ) est **unique** et même si 2 clés peuvent avoir la même image, ces 2 images sont représentées dans **2 adresses mémoires différentes** (voir exemple ci-dessous). De plus, toute image possède un antécédent&#8230;

<pre class="wp-block-code" aria-describedby="shcb-language-57" data-shcb-language-name="CSS" data-shcb-language-slug="css"><div>
  <code class="hljs language-css">&lt;span class="hljs-comment">/* Chat et Chameau ont pour image 3, pourtant ils n'ont pas la même adresse mémoire */&lt;/span>
  &lt;span class="hljs-selector-tag">std&lt;/span>&lt;span class="hljs-selector-pseudo">::cout&lt;/span> &lt;&lt; &&lt;span class="hljs-selector-tag">MaMap&lt;/span>&lt;span class="hljs-selector-class">.at&lt;/span>("&lt;span class="hljs-selector-tag">Rat&lt;/span>") &lt;&lt; &lt;span class="hljs-selector-tag">std&lt;/span>&lt;span class="hljs-selector-pseudo">::endl&lt;/span>;
  &lt;span class="hljs-selector-tag">std&lt;/span>&lt;span class="hljs-selector-pseudo">::cout&lt;/span> &lt;&lt; &&lt;span class="hljs-selector-tag">MaMap&lt;/span>&lt;span class="hljs-selector-class">.at&lt;/span>("&lt;span class="hljs-selector-tag">Chat&lt;/span>") &lt;&lt; &lt;span class="hljs-selector-tag">std&lt;/span>&lt;span class="hljs-selector-pseudo">::endl&lt;/span>;
  &lt;span class="hljs-selector-tag">std&lt;/span>&lt;span class="hljs-selector-pseudo">::cout&lt;/span> &lt;&lt; &&lt;span class="hljs-selector-tag">MaMap&lt;/span>&lt;span class="hljs-selector-class">.at&lt;/span>("&lt;span class="hljs-selector-tag">Chameau&lt;/span>") &lt;&lt; &lt;span class="hljs-selector-tag">std&lt;/span>&lt;span class="hljs-selector-pseudo">::endl&lt;/span>;
  
  &lt;span class="hljs-comment">/* Retour Console : 
   * 0x5592cb6d1f48
   * 0x5592cb6d1f08
   * 0x5592cb6d1f88
  */&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-57"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">CSS</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">css</span><span class="shcb-language__paren">)</span></small></pre>

## Sources :

  * [http://www.cplusplus.com/reference/unordered\_map/unordered\_map/count/][1]
  * [http://www.cplusplus.com/reference/unordered\_map/unordered\_map/erase/][2]
  * <https://zestedesavoir.com/tutoriels/822/la-programmation-en-c-moderne/decoupons-tout-ca/de-nouvelles-structures-de-donnees/>
  * <https://fr.wikipedia.org/wiki/Fonction_multivalu%C3%A9e>

 [1]: http://www.cplusplus.com/reference/unordered_map/unordered_map/count/
 [2]: http://www.cplusplus.com/reference/unordered_map/unordered_map/erase/