# **Paramétrage API GLPI**

 

## Pré requis :

Activer l’api dans la configuration de GLPI

Créer un client de l’api

Créer un compte super admin dédié à l’API et générer son jeton d’api

Lire la documentation officel :

https://qalglpi.xxxxx.net/apirest.php#glossary

Récupérer les informations d’identification, elles devront être passés dans votre script

// Roue dentee > Personnalisation > Jeton d'API
//$user_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";

// Configuration > Generale > API > click Nom api client > app_token
//$app_token = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy";


### Liste des champs :
```
"entities_id": "1",
        "name": "    ",
       // "date": "2016-10-06 17:34:28",
       // "closedate": "2016-10-15 14:50:02",
       // "solvedate": "2016-10-08 10:32:47",
       // "date_mod": "2016-10-15 14:50:02",
       // "users_id_lastupdater": "6",
       // "status": "6",
        "users_id_recipient": "9",
        "requesttypes_id": "2",
        "content": "description",
        "urgency": "3",
        "impact": "3",
        "priority": "3",
        "itilcategories_id": "1",
        "type": "2",

        "global_validation": "1",
        "slts_ttr_id": "0",
        "slts_tto_id": "0",
        "ttr_slalevels_id": "0",
        "_users_id_requester": "'.$id_demandeur.'"
       
//       "begin_waiting_date": "2016-10-08 10:32:47",
  //      "sla_waiting_duration": "0",
//       "waiting_duration": "142673",
  //      "close_delay_stat": "625061",
  //      "solve_delay_stat": "4826",
  //      "takeintoaccount_delay_stat": "934",
   //     "actiontime": "0",
        "is_deleted": "0",
        "locations_id": "1",
     //   "validation_percent": "0" 

 ```

 
* * *
Configuration sur https://glpi.xxxxxx.net

## Activation de l’API

Configuration >> Générale >> API


![Kiku](doc/2021-10-20-21_46_19-Clipboard.jpg)


### Ajout d’un client API 


![2021-10-20 21_49_25-Clipboard.jpg](doc/2021-10-20-21_49_25-Clipboard.jpg)


Administration >> Utilisateurs

### Nouvel utilisateur



![2021-10-20 21_53_13-Clipboard.jpg](doc/2021-10-20-21_53_13-Clipboard.jpg)

Ajuster les droits en fonction de vos besoins : Habillitations

![2021-10-20 21_53_48-Clipboard.jpg](doc/2021-10-20-21_53_48-Clipboard.jpg)

L’accès à l’api est régi par les droits sur les profils, un profil n’ayant pas accès a la gestion du matériel, ne pourra utiliser l’api /Computer.

### Préférences : 

![2021-10-20 21_54_35-Clipboard.jpg](doc/2021-10-20-21_54_35-Clipboard.jpg)

De base à la création du compte, les champs sont vides, il faut cliquer sur Regénerer et sauvegarder.

Pour l’accès à l’api, nous utilisons « Jeton d’API »