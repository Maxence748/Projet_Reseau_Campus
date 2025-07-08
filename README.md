# Projet_Reseau_Campus
 
# SAE2.01 : Conception et Déploiement d'une Infrastructure Réseau de Campus Universitaire

## Introduction

Ce projet, réalisé dans le cadre de la SAE2.01, porte sur la conception, l'implémentation et la sécurisation d'une infrastructure réseau complexe pour un campus universitaire multi-sites. L'objectif était de simuler un réseau d'envergure, capable de gérer de multiples départements et services, tout en assurant l'interconnectivité, l'optimisation des ressources et la sécurité des communications.

Ce dépôt contient l'ensemble des fichiers du projet, y compris le compte rendu détaillé, le cahier des charges, le plan Packet Tracer et un script Python d'aide à l'adressage.

## Objectifs du Projet

L'objectif principal était de construire un réseau informatique fonctionnel pour une petite structure de type universitaire, couvrant plusieurs aspects fondamentaux des réseaux :

* **Planification de l'adressage IP** (VLSM) pour optimiser l'utilisation des adresses.
* **Choix et déploiement du matériel réseau** (routeurs, commutateurs).
* **Segmentation logique du réseau** via les VLANs pour isoler les services et améliorer la sécurité.
* **Mise en place du routage dynamique** (RIP) pour assurer l'interconnexion entre les différents sites du campus.
* **Configuration du Network Address Translation (NAT)** pour permettre l'accès sécurisé au réseau WAN (Internet) et exposer les services internes.
* **Implémentation de listes de contrôle d'accès (ACLs)** pour filtrer le trafic et renforcer la sécurité.
* **Déploiement de services essentiels** tels qu'un serveur WEB et un serveur TFTP.

## Technologies Utilisées

* **Cisco Packet Tracer :** Outil de simulation réseau pour la conception et les tests de la topologie.
* **VLSM (Variable Length Subnet Masking) :** Pour la planification efficace des sous-réseaux.
* **VLANs (Virtual Local Area Networks) :** Pour la segmentation logique du réseau.
* **RIP (Routing Information Protocol) :** Protocole de routage dynamique pour l'interconnexion inter-sites.
* **NAT (Network Address Translation) :** Pour la traduction d'adresses IP.
* **ACLs (Access Control Lists) :** Pour le filtrage de sécurité du trafic.
* **Serveur WEB :** Apache (via XAMPP) pour l'hébergement de pages web internes.
* **Serveur TFTP :** Pour la gestion et la sauvegarde des configurations des équipements.
* **Python :** Script d'aide à la planification d'adressage IP.

## Comment Reproduire le Projet (Guide Étape par Étape)

Ce guide vous expliquera comment recréer l'infrastructure réseau du campus, étape par étape, en utilisant Cisco Packet Tracer.

### Prérequis

* **Cisco Packet Tracer :** Assurez-vous d'avoir la dernière version de Cisco Packet Tracer installée sur votre machine.
* **Fichiers du Dépôt :** Téléchargez ou clonez ce dépôt GitHub pour accéder au plan Packet Tracer (`.pkt`), au compte rendu et au cahier des charges.

### Étapes Clés de l'Implémentation :

1.  **Analyse du Cahier des Charges & Planification d'Adressage (VLSM)**
    * Lisez attentivement le `cahier_charges SAE21_fin_2023.pdf` pour comprendre les exigences du réseau.
    * Utilisez le `compte rendu.pdf` (Partie 1 : "Étude du plan d'adressage") pour comprendre la démarche de planification.
    * **Utilisez le script Python `import ipaddress vrai.py`** fourni dans ce dépôt pour vérifier les sous-réseaux nécessaires à votre plan d'adressage VLSM, en fonction du nombre d'hôtes requis par VLAN et par site.

2.  **Création de la Topologie dans Packet Tracer**
    * Ouvrez le fichier `Packet Tracer.pkt` (ou un nom similaire si vous l'avez renommé) inclus dans ce dépôt. Cela vous donnera la topologie complète comme point de départ.
    * Positionnez les routeurs (Routeurs Entreprise, Routeurs FAI) et les commutateurs (Switchs) nécessaires pour chaque bâtiment/LAN et pour l'interconnexion des sites.
    * Connectez les équipements selon le schéma logique.

3.  **Mise en place des VLANs (Segmentation Logique)**
    * Pour chaque commutateur dans les bâtiments, configurez les VLANs nécessaires (par exemple, 5 VLANs par site : Administration, Formations A, Formations B, Enseignants, Services, etc.).
    * Attribuez les ports des commutateurs aux VLANs appropriés.
    * Configurez les ports Trunk entre les commutateurs et vers les routeurs pour permettre le passage du trafic de tous les VLANs.

4.  **Configuration du Routage Inter-VLAN**
    * Sur le routeur d'entreprise de chaque site, implémentez le "Router-on-a-stick" ou une configuration de routage inter-VLAN similaire pour permettre la communication entre les différents VLANs du même site.

5.  **Mise en place du Routage Inter-Sites (RIP)**
    * Configurez le protocole de routage dynamique **RIPv2** sur tous les routeurs d'entreprise et les routeurs FAI.
    * Assurez-vous que les réseaux appropriés sont annoncés et que l'interconnexion entre les quatre sites du campus est fonctionnelle.
    * Vérifiez la convergence du routage et la capacité des postes d'un site à atteindre ceux d'un autre site via des `ping`.

6.  **Implémentation du NAT (Network Address Translation)**
    * Sur les routeurs FAI, configurez le NAT statique et/ou dynamique.
    * Le NAT statique est utilisé pour rendre des serveurs internes (comme le serveur WEB) accessibles depuis le WAN.
    * Le NAT dynamique permet aux utilisateurs du réseau interne d'accéder à Internet en utilisant un pool d'adresses publiques.

7.  **Configuration des Serveurs (WEB et TFTP)**
    * Dans Packet Tracer, ajoutez des serveurs et configurez-les avec les adresses IP appropriées dans leurs VLANs respectifs (par exemple, un serveur WEB dans le VLAN Services, un serveur TFTP dans le VLAN Administration).
    * Pour le serveur WEB, simulez l'installation d'Apache (XAMPP). Vérifiez l'accès à la page web depuis différents VLANs.
    * Pour le serveur TFTP, assurez-vous qu'il est accessible pour la sauvegarde/restauration de configurations (voir la section "Défis" pour les difficultés rencontrées).

8.  **Mise en place des ACLs (Access Control Lists)**
    * Définissez et appliquez des ACLs sur les interfaces des routeurs pour filtrer le trafic.
    * Exemples d'ACLs à implémenter :
        * Restreindre l'accès de certains VLANs à d'autres.
        * Contrôler l'accès aux serveurs internes depuis le WAN.
        * Bloquer certains types de trafic indésirables.

## Résultats et Succès du Projet

* **Plan d'Adressage Optimisé :** Mise en œuvre réussie d'un plan VLSM efficace pour quatre sites, permettant une allocation optimale des adresses IP et une gestion structurée du réseau.
* **Segmentation Réseau Robuste :** Configuration de 5 VLANs par site pour une isolation logique des services (administration, formations A/B, enseignants, services), améliorant la sécurité et la gestion du trafic.
* **Interconnexion Fluide :** Implémentation fonctionnelle du protocole RIP assurant une communication transparente et dynamique entre tous les sites du campus.
* **Accès WAN Sécurisé :** Configuration réussie du NAT statique et dynamique, permettant aux utilisateurs internes d'accéder au WAN et exposant les services web internes de manière contrôlée.
* **Haute Disponibilité :** Mise en place d'une topologie redondante avec le protocole STP (Spanning Tree Protocol) pour prévenir les boucles et garantir la continuité de service en cas de défaillance de lien.
* **Services Fonctionnels :** Validation de l'accès aux serveurs TFTP et Web depuis différents VLANs, confirmant la bonne connectivité et la configuration des services.

## Défis et Leçons Apprises

Ce projet a également présenté des défis, offrant des opportunités d'apprentissage précieuses :

* **Complexité du Filtrage par ACL :** Bien que des ACLs aient été implémentées pour gérer les flux inter-VLAN et WAN, leur configuration s'est avérée particulièrement délicate. L'affinement des règles de sécurité pour des communications complexes a nécessité une compréhension approfondie et des tests rigoureux, soulignant la difficulté de prévoir toutes les interactions de trafic, c'est pour cela que les ACL n'apparaissent pas dans ce projet.
* **Limitations avec TFTP :** Des difficultés persistantes ont été rencontrées lors de la tentative de sauvegarde des configurations des équipements via TFTP (`copy running-config tftp`). Les fichiers générés sur le serveur TFTP apparaissaient vides. Cela suggère un problème de droits d'accès ou de permissions non identifié ou non résolu dans l'environnement de simulation, mettant en lumière l'importance de la gestion des permissions dans un environnement réel.

Ces défis ont renforcé l'importance d'une planification minutieuse, de tests itératifs et d'une compréhension approfondie des mécanismes de sécurité réseau.

## Structure du Dépôt

* `compte rendu.pdf` : Le document détaillé du projet expliquant toutes les étapes, les configurations et les résultats.
* `cahier_charges SAE21_fin_2023.pdf` : Le document original spécifiant les exigences du projet.
* `import ipaddress vrai.py` : Un script Python utile pour la planification et la validation des adresses IP (VLSM).
* `Version mise en place du NAT(fonctionne).pkt` : Le fichier de simulation Cisco Packet Tracer contenant la topologie complète et les configurations.


## Contact

Pour toute question ou information supplémentaire sur ce projet, n'hésitez pas à me contacter via mon profil GitHub.

---
