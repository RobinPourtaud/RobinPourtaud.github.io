---
title: "Recevoir des notifications par mail en PHP grâce à IFTTT"
slug: "recevoir-des-notifications-depuis-depuis-php-grace-a-iftt"
date: "2020-04-23"
categories: 
  - "informatique"
tags: 
  - "iftt"
  - "mail"
  - "php"
latex: false
description: "Il existe de nombreuses méthodes pour recevoir les notifications de son site web grâce à PHP. Aujourd'hui je vais vous montrer comment recevoir des mails grâce à IFTTT en moins de 10 min."
---
## Paramétrer IFTTT :

1. Connectez-vous à l’adresse [https://ifttt.com/](https://ifttt.com/) .
2. Inscrivez-vous si ce n'est pas déjà fais.
3. Appuyez sur votre photo de profil en haut à gauche, puis appuyez sur "Create".
4. Appuyez sur "This" puis sélectionnez le service "Webhooks".
5. Choisissez l'Event Name de votre choix. Pour ma part, ce sera "iftttmessage".
6. Appuyez sur "That" puis sélectionnez "Email".
7. Personnalisez le body, le subject comme vous le souhaitez. Gardez juste bien en tête que "Value1" contiendra le message qu'on voudra envoyer.

![Contenu Message IFTTT](image-1-1.png#t3)


1. Appuyez sur "Finish"
2. Allez sur le lien suivant: [https://ifttt.com/maker_webhooks/settings](https://ifttt.com/maker_webhooks/settings)
3.  Devant URL, vous devriez pouvoir voir votre clé ! Gardez-la précieusement.
4.  Fini pour la configuration de IFTTT

## Création d'une fonction PHP :

```php
<?php
function msg($message){
 $msgmodify=rawurlencode($message); 
 $key="KEY"; //Ajouté votre clé
 $eventname="EVENT NAME"; //Ajouté votre nom d’événement 
 file_get_contents("https://maker.ifttt.com/trigger/$eventname/with/key/".$key."?value1=".$msgmodify."");
}
?>
```

En incluant cette fonction dans le reste de votre code, vous pourrez facilement envoyer des messages comme ceci :

```php
msg("Bonjour, voici un message");
```

## Résultat :

Si vous avez bien tout suivi, à l’exécution de la fonction msg, vous devriez recevoir un mail de "action@ifttt.com" de ce style :

<div style="margin:auto;"><table><tbody><tr><td>What: iftttmessage<br>When: April 27, 2020 at 11:08AM<br>Content: Bonjour, voici un message</td></tr></tbody></table></div>

Mail envoyé depuis un server Web
