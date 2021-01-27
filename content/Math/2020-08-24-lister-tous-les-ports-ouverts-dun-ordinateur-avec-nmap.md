---
title: 'Lister tous les ports ouverts d&rsquo;un ordinateur avec nmap'
author: Robin Pourtaud
type: post
date: 2020-08-24T13:53:42+00:00
url: /sciences/informatique/securite-informatique/robin/4366/
featured_image: /wp-content/uploads/2020/08/nmap.png
rank_math_primary_category:
  - "338"
rank_math_seo_score:
  - "68"
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_focus_keyword:
  - nmap
rank_math_analytic_object_id:
  - "18"
categories:
  - Sécurité Informatique
tags:
  - Linux
  - nmap

---
Pour des raisons de sécurité, de recherche ou tout simplement de curiosité, il peut être nécessaire de scanner une ip pour en extraire une liste de ports ouverts. Ce tutoriel présente la façon, à ma connaissance, la plus rapide et la plus simple d&rsquo;accomplir cette tâche grâce à nmap. 

## Installer nmap

Pour ce tutoriel, nous utiliserons le programme nmap. Pour l&rsquo;installer, rien de très compliqué : 

Sous une distribution basée sur Debian : 

<pre class="wp-block-code" aria-describedby="shcb-language-117" data-shcb-language-name="Bash" data-shcb-language-slug="bash"><div>
  <code class="hljs language-bash">sudo apt update
  sudo apt install nmap</code>
</div>

<small class="shcb-language" id="shcb-language-117"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Bash</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">bash</span><span class="shcb-language__paren">)</span></small></pre>

Sous ArchLinux : 

<pre class="wp-block-code" aria-describedby="shcb-language-118" data-shcb-language-name="Bash" data-shcb-language-slug="bash"><div>
  <code class="hljs language-bash">pacman -Sy nmap</code>
</div>

<small class="shcb-language" id="shcb-language-118"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Bash</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">bash</span><span class="shcb-language__paren">)</span></small></pre>

Sous plus de distributions ici : <https://nmap.org/download.html>{.rank-math-link}

## Lister les ports ouverts

En fonction des paramètres envoyés à nmap, la recherche de ports peut aussi bien être très rapide que très lente. 

Pour lister tous les ports ouverts pour une adresse ip ou domaine donné, je vous propose la commande suivante : 

<pre class="wp-block-code" aria-describedby="shcb-language-119" data-shcb-language-name="Bash" data-shcb-language-slug="bash"><div>
  <code class="hljs language-bash">sudo nmap -p- -v -sS DOMAINE_OU_IP</code>
</div>

<small class="shcb-language" id="shcb-language-119"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Bash</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">bash</span><span class="shcb-language__paren">)</span></small></pre>

L&rsquo;option -p- signifie « Tous les ports ».  
Pour scanner seulement certains ports, par exemple de 20 à 300, vous pouvez remplacer _« -p-« _ par _« -p 30-300 »_. 

L&rsquo;option -v pour « verbose » signifie qu&rsquo;on pourra avoir accès à l&rsquo;avance de la recherche en cours, le retour programme sera plus « verbeux ». 

L&rsquo;option -sS ou scan SYN est celui par défaut et le plus populaire pour de bonnes raisons. Il peut être exécuté rapidement et scanner des milliers de ports par seconde sur un réseau rapide lorsqu&rsquo;il n&rsquo;est pas entravé par des pare-feux. Le scan SYN est relativement discret et furtif, vu qu&rsquo;il ne termine jamais les connexions TCP. [2]

Pour prendre un exemple : 

<pre class="wp-block-code" aria-describedby="shcb-language-120" data-shcb-language-name="Bash" data-shcb-language-slug="bash"><div>
  <code class="hljs language-bash">sudo nmap -p- -v -sS google.fr</code>
</div>

<small class="shcb-language" id="shcb-language-120"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Bash</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">bash</span><span class="shcb-language__paren">)</span></small></pre>

En moins de 3 secondes on obtient 2 ports communs découverts : Le 80 et le 443 correspondants aux ports ouverts pour les protocoles HTTP et HTTPS : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/08/image-4-1024x583.png" alt="" class="wp-image-4367" width="660" height="376" srcset="https://keskec.fr/wp-content/uploads/2020/08/image-4-1024x583.png 1024w, https://keskec.fr/wp-content/uploads/2020/08/image-4-300x171.png 300w, https://keskec.fr/wp-content/uploads/2020/08/image-4-768x437.png 768w, https://keskec.fr/wp-content/uploads/2020/08/image-4.png 1250w" sizes="(max-width: 660px) 100vw, 660px" /><figcaption>nmap google.fr</figcaption></figure>
</div>

Avec un peu de patience, nous pouvons enfin avoir accès à ce magnifique tableau récapitulatif : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/08/image-5.png" alt="" class="wp-image-4372" width="640" height="201" srcset="https://keskec.fr/wp-content/uploads/2020/08/image-5.png 799w, https://keskec.fr/wp-content/uploads/2020/08/image-5-300x95.png 300w, https://keskec.fr/wp-content/uploads/2020/08/image-5-768x242.png 768w" sizes="(max-width: 640px) 100vw, 640px" /><figcaption>Listes des ports ouverts de google.fr</figcaption></figure>
</div>

## Sources

  1. [Téléchargement nmap &#8211; nmap.org][1]{.rank-math-link}
  2. [Techniques de scan de ports &#8211; nmap.org][2]{.rank-math-link}

 [1]: https://nmap.org/download.html
 [2]: https://nmap.org/man/fr/man-port-scanning-techniques.html