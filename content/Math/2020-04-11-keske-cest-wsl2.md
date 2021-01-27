---
title: Wsl2
author: Robin Pourtaud
type: post
date: 2020-04-11T12:00:02+00:00
url: /sciences/informatique/robin/78/
featured_image: /wp-content/uploads/2020/04/Capture-1-1-1568x800.png
post_views_count:
  - "38"
um_content_restriction:
  - 'a:8:{s:26:"_um_custom_access_settings";s:1:"0";s:14:"_um_accessible";s:1:"0";s:19:"_um_noaccess_action";s:1:"0";s:30:"_um_restrict_by_custom_message";s:1:"0";s:27:"_um_restrict_custom_message";s:0:"";s:19:"_um_access_redirect";s:1:"0";s:23:"_um_access_redirect_url";s:0:"";s:28:"_um_access_hide_from_queries";s:1:"0";}'
rank_math_primary_category:
  - "12"
rank_math_description:
  - Vous souhaitez savoir comment installer Windows Subsystem for Linux 2 ? Et avoir une distribution sous Linux? Voici un article pour vous guider.
rank_math_focus_keyword:
  - WSL
rank_math_robots:
  - 'a:1:{i:0;s:5:"index";}'
rank_math_internal_links_processed:
  - "1"
rank_math_seo_score:
  - "72"
rank_math_rich_snippet:
  - article
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
ampforwp-amp-on-off:
  - default
rank_math_schema_Article:
  - 'a:7:{s:5:"@type";s:7:"Article";s:8:"headline";s:11:"%seo_title%";s:13:"datePublished";s:20:"%date(Y-m-dTH:i:sP)%";s:12:"dateModified";s:24:"%modified(Y-m-dTH:i:sP)%";s:6:"author";a:2:{s:5:"@type";s:6:"Person";s:4:"name";s:14:"Robin Pourtaud";}s:11:"description";s:144:"Vous souhaitez savoir comment installer Windows Subsystem for Linux 2 ? Et avoir une distribution sous Linux? Voici un article pour vous guider.";s:8:"metadata";a:3:{s:5:"title";s:7:"Article";s:9:"isPrimary";b:1;s:4:"type";s:8:"template";}}'
rank_math_analytic_object_id:
  - "107"
categories:
  - Informatique
tags:
  - Linux
  - Tutoriel
  - Windows 10
  - WSL2

---
Vous souhaitez savoir comment installer Windows Subsystem for Linux 2 ? Et utiliser Debian ou Ubuntu comme distribution ? Voici un article pour vous guider.

<blockquote class="wp-block-quote">
  <p>
    <strong>Windows Subsystem for Linux (WSL)</strong>&nbsp;est une couche de compatibilité permettant d&rsquo;exécuter des&nbsp;<a href="https://fr.wikipedia.org/wiki/Fichier_ex%C3%A9cutable">exécutables binaires</a>&nbsp;<a href="https://fr.wikipedia.org/wiki/Linux">Linux</a>&nbsp;(au format&nbsp;<a href="https://fr.wikipedia.org/wiki/Executable_and_Linkable_Format">ELF</a>) de manière native sur&nbsp;<a href="https://fr.wikipedia.org/wiki/Windows_10">Windows 10</a>&nbsp;et&nbsp;<a href="https://fr.wikipedia.org/wiki/Windows_Server_2019">Windows Server 2019</a>.
  </p>
  
  <cite><a href="https://fr.wikipedia.org/wiki/Windows_Subsystem_for_Linux">fr.wikipedia.org</a></cite>
</blockquote>

En mai 2019, Microsoft lance WSL2, une mise à jours de WSL proposant de nombreuses nouveautés. 

Parmi celles-ci, on retrouve: 

  * La présence d&rsquo;un vrai noyau Linux au sein de Windows
  * Un temps d&rsquo;accès réduit
  * Un accès et une modification des fichiers plus fluides 
  * Un accès à internet et des ports plus rapide et intrinsèque à Windows

## Wsl, bénéfice? {.has-text-align-center}

Concrètement, WSL nous offre un accès à un système Linux à l&rsquo;intérieur de Windows via un terminal. Cela implique donc que toute application Linux sera maintenant exécutable depuis Windows 10. 

## Nécessaire à l&rsquo;installation: {.has-text-align-center}

  * Windows 10 builds 18917 ou plus (commande « winver » pour vérifier).
  * 30 min de votre temps :).

## Installation: {.has-text-align-center}

### Installation de WSL:

D&rsquo;abord, ouvrez le terminal PowerShell en Administrateur et tapez la commande: 

<pre class="wp-block-code" aria-describedby="shcb-language-16" data-shcb-language-name="PowerShell" data-shcb-language-slug="powershell"><div>
  <code class="hljs language-powershell">&lt;span class="hljs-built_in">Enable-WindowsOptionalFeature&lt;/span> &lt;span class="hljs-literal">-Online&lt;/span> &lt;span class="hljs-literal">-FeatureName&lt;/span> Microsoft&lt;span class="hljs-literal">-Windows&lt;/span>&lt;span class="hljs-literal">-Subsystem&lt;/span>&lt;span class="hljs-literal">-Linux&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-16"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">PowerShell</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">powershell</span><span class="shcb-language__paren">)</span></small></pre>

Ensuite, redémarrez l&rsquo;ordinateur.

### Activer la Machine Virtuel Windows

Aussi avec le terminal PowerShell en Administrateur, tapez la commande suivante:

<pre class="wp-block-code" aria-describedby="shcb-language-17" data-shcb-language-name="PowerShell" data-shcb-language-slug="powershell"><div>
  <code class="hljs language-powershell">dism.exe /online /&lt;span class="hljs-built_in">enable-feature&lt;/span> /featurename:Microsoft&lt;span class="hljs-literal">-Windows&lt;/span>&lt;span class="hljs-literal">-Subsystem&lt;/span>&lt;span class="hljs-literal">-Linux&lt;/span> /all /norestart</code>
</div>

<small class="shcb-language" id="shcb-language-17"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">PowerShell</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">powershell</span><span class="shcb-language__paren">)</span></small></pre>

puis:

<pre class="wp-block-code" aria-describedby="shcb-language-18" data-shcb-language-name="PowerShell" data-shcb-language-slug="powershell"><div>
  <code class="hljs language-powershell">dism.exe /online /&lt;span class="hljs-built_in">enable-feature&lt;/span> /featurename:VirtualMachinePlatform /all /norestart</code>
</div>

<small class="shcb-language" id="shcb-language-18"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">PowerShell</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">powershell</span><span class="shcb-language__paren">)</span></small></pre>

Redémarrez l&rsquo;ordinateur.

### Installer la distribution Linux de votre choix

Vous pouvez maintenant installer la distribution Linux souhaitée, [Ubuntu][1], [Debian][2]&#8230;. 

Vous avez juste à cliquer sur « Installer ».

Puis, suite au téléchargement, « ouvrez » la distribution choisie.

Patientez un peu, puis choisissez un nom d&rsquo;utilisateur UNIX et un mot de passe, sachant que ceux-ci peuvent être différents de vos identifiants Windows.

Vous avez maintenant accès à un vrai terminal Linux sous Windows&#8230;. sous WSL1.<figure class="wp-block-image size-large">

<img src="https://keskec.fr/wp-content/uploads/2020/04/Capture-1-1024x523.png" alt="" class="wp-image-79" /> <figcaption>Windows Subsystem for Linux </figcaption></figure> 

### Passer de WSL1 à WSL2

Pour passer votre distribution de WSL1 à WSL2, il suffit d&rsquo;abord de taper la commande suivante dans le terminal powershell:

<pre class="wp-block-code" aria-describedby="shcb-language-19" data-shcb-language-name="PowerShell" data-shcb-language-slug="powershell"><div>
  <code class="hljs language-powershell">wsl -&lt;span class="hljs-literal">-set&lt;/span>&lt;span class="hljs-literal">-version&lt;/span> &lt;Distro&gt; &lt;span class="hljs-number">2&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-19"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">PowerShell</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">powershell</span><span class="shcb-language__paren">)</span></small></pre>

Ensuite, remplacez <Distro> par le nom de votre distribution

<pre class="wp-block-code" aria-describedby="shcb-language-20" data-shcb-language-name="PowerShell" data-shcb-language-slug="powershell"><div>
  <code class="hljs language-powershell">wsl -&lt;span class="hljs-literal">-set&lt;/span>&lt;span class="hljs-literal">-version&lt;/span> &lt;span class="hljs-number">2&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-20"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">PowerShell</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">powershell</span><span class="shcb-language__paren">)</span></small></pre>

Si vous souhaitez que toutes vos futures distributions soit sous WSL2 par défaut&#8230;

La commande ci-dessous vous permet également de lister les noms des distribution Linux si besoin.

<pre class="wp-block-code" aria-describedby="shcb-language-21" data-shcb-language-name="PowerShell" data-shcb-language-slug="powershell"><div>
  <code class="hljs language-powershell">wsl &lt;span class="hljs-literal">-l&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-21"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">PowerShell</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">powershell</span><span class="shcb-language__paren">)</span></small></pre>

Vous avez enfin un système Linux opérationnel :).

### Petit + : Le nouveau Terminal Windows

Vous pouvez télécharger le nouveau terminal Windows à l&rsquo;adresse suivante:

<https://www.microsoft.com/fr-fr/p/windows-terminal-preview/9n0dx20hk701?activetab=pivot:overviewtab><figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">

<div class="wp-block-embed__wrapper">
</div></figure> 

## Sources:

  * <https://docs.microsoft.com/en-us/windows/wsl/wsl2-install>
  * <https://howto.lintel.in/wsl-vs-wsl-2-performance/>
  * <https://devblogs.microsoft.com/commandline/wsl2-will-be-generally-available-in-windows-10-version-2004/>

 [1]: https://www.microsoft.com/fr-fr/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab
 [2]: https://www.microsoft.com/fr-fr/p/debian/9msvkqc78pk6?activetab=pivot:overviewtab