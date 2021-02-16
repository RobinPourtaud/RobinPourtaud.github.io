---
title: "unordered_map en C++"
slug: "unordered_map-en-c"
date: "2020-05-07"
categories: 
  - "informatique"
tags: 
  - "c"
  - "complexite-asymptotique"
  - "unordered_map"
description: "Le conteneur unordered_map est un tableau associatif (ou table associative). Il permet l'association d'une clé du type de son choix à une valeur. Comme son nom l'indique, les éléments de l'unordered_map ne sont pas rangés, que ce soit par leurs clés ou par leurs valeurs associées (contrairement à map)."
---
## Intérêts :

L’intérêt principal de l'utilisation d'une unordered_map par rapport à un autre conteneur (notamement une map) est sa faible complexité asymptotique de recherche ou d'insertion moyenne (en O(1)).

## Exemple :

En tant qu'exemple, je vais créer un tableau associant un animal à son âge.

### Définition :

```
#include <iostream> //Cout, endl,etc
#include <string>
#include <unordered_map>
int main(){
   /*
    * Tableau associatif associant une clé de type string
    * à un int.
    * Concrètement, MaMap associant un animal à son âge
   */
   std::unordered_map<std::string,int> MaMap = {
                                      {"Chien",1},
                                      {"Chat",3},
                                      {"Rat",10},
                                      {"Chameau",3}
                                    };
   // Le reste des parties ce situent ici

   return 0;
}
```

### Insertion :

Complexité moyenne en O(1).

#### Méthode 1 : std::unordered_map::emplace

```
MaMap.emplace("Castor",2);
MaMap.emplace("Tortue",1);
//Avec make_pair
MaMap.emplace(std::make_pair("Oiseau",4));
```

#### Méthode 2 : std::unordered_map::insert

```
MaMap.insert({"Castor",2});

// Insert avec std::make_pair
MaMap.insert(std::make_pair<std::string,int>("Lézard",2));

// Insert plusieurs valeurs en même temps
MaMap.insert({{"Souris",1},{"Girafe",6}});
```

#### Méthode 3 : Operateur\[\]

```
// On insère dans MaMap la clé Cochon associée à 4
MaMap["Cochon"] = 4;
```

### Accéder/Rechercher :

Complexité moyenne en O(1), linéaire dans le pire cas.

#### Méthode 1 : Operateur\[\]

```
std::cout << "Ma Souris a " << MaMap["Souris"] << " an." << std::endl;

// Affichage : "Ma Souris a 1 an"
```

#### Méthode 2 : std::unoredered_map::at

```
std::cout << "Mon chat a " << MaMap.at("Chat") << " ans." << std::endl;

// Affichage : "Mon chat a 3 ans."
```

#### Méthode 3 : std::unoredered_map::find + iterator

Find permet en plus de tester si la clé est présente ou non dans l'unordered_map avec un itérateur.

```
std::string search = "Castor";

auto it = MaMap.find(search);
if (it == MaMap.end()){
  throw std::string("Pas de " + search);
}
else{
  std::cout << it->first << " a " << it->second << " ans." << std::endl;
}
// Affichage : "Castor a 2 ans."
```

### Modifier :

Complexité moyenne en O(1), linéaire dans le pire cas.

#### Méthode 1 : Operateur\[\]

```
MaMap["Castor"] = 3;
// Castor est maintenant associé à la valeur 3
```

#### Méthode 2 : std::unoredered_map::at

```
MaMap.at("Castor") += 6;
// Castor est maintenant associé à la valeur 9
MaMap.at("Castor") = 20;
// Castor est maintenant associé à la valeur 20
```

#### Méthode 3 : std::unoredered_map::find

```
std::string search = "Castor";

auto it = MaMap.find(search);
if (it == MaMap.end()){
  throw std::string("Pas de " + search);
}
else{
  it->second = 5;
}
// Castor est maintenant associé à la valeur 5
```

### Supprimer :

Complexité moyenne en O(1), linéaire dans le pire cas.

```
Mamap.erase("Castor");
//L'entrée Castor -> 3 est maintenant effacée
```

### Aspect mathématique :

On pourrait penser que **la relation associative** du conteneur est comparable à une fonction surjective non injective, mais elle est en faite une **fonction bijective**.

En effet, chaque clé (ensemble de départ) est **unique** et même si 2 clés peuvent avoir la même image, ces 2 images sont représentées dans **2 adresses mémoires différentes** (voir exemple ci-dessous). De plus, toute image possède un antécédent...

```
/* Chat et Chameau ont pour image 3, pourtant ils n'ont pas la même adresse mémoire */
std::cout << &MaMap.at("Rat") << std::endl;
std::cout << &MaMap.at("Chat") << std::endl;
std::cout << &MaMap.at("Chameau") << std::endl;

/* Retour Console : 
 * 0x5592cb6d1f48
 * 0x5592cb6d1f08
 * 0x5592cb6d1f88
*/
```

## Sources :

- [http://www.cplusplus.com/reference/unordered_map/unordered_map/count/](http://www.cplusplus.com/reference/unordered_map/unordered_map/count/)
- [http://www.cplusplus.com/reference/unordered_map/unordered_map/erase/](http://www.cplusplus.com/reference/unordered_map/unordered_map/erase/)
- [https://zestedesavoir.com/tutoriels/822/la-programmation-en-c-moderne/decoupons-tout-ca/de-nouvelles-structures-de-donnees/](https://zestedesavoir.com/tutoriels/822/la-programmation-en-c-moderne/decoupons-tout-ca/de-nouvelles-structures-de-donnees/)
- [https://fr.wikipedia.org/wiki/Fonction_multivalu%C3%A9e](https://fr.wikipedia.org/wiki/Fonction_multivalu%C3%A9e)
