Ce dépôt git contient le code que j'ai utilisé pour analyser les données du grand débat.

Les fichiers json des données brutes peuvent être téléchargés à https://www.data.gouv.fr/fr/datasets/donnees-ouvertes-du-grand-debat-national/

Fichiers existants :
preprocess_text.py : traite le texte de chaque réponse et le transforme en liste de lemmes.
Utilise le modèle français de Spacy. La doc concernant l'installation de ce modèle est accessible à https://spacy.io/models/fr
Pour faire simple, il suffit de lancer la commande python -m spacy download fr_core_news_md et cela devrait installer le modèle.

generate_wordclouds.py : Génère un nuage de mot des réponses sous forme de listes de lemmes (sortie du fichier preprocess_text.py).
Un nuage de mots pour chaque thème, ainsi que pour chaque question est généré. Pour les réponses standardisées, cela est peu pertinent, mais pour les autres, c'est plus intéressant.


Le dossier img contient les nuages de mots générés par mon script (je pense ajouter l'intitulé des questions par la suite).

Idées d'analyse à faire :
Voir comment les lemmes des réponses ont évolués au cours du temps.
Voir comment les réponses varient en fonction du type de commune (rural, urbain, peri-urbain...). Se lier à la base de l'INSEE pour faire cela.

Améliorer la lemmatisation et la rendre plus précise/pertinente est aussi un axe important.
Par exemple, la plupart des mots sont remplacés par l'infinitif, ce n'est sûrement pas tout le temps pertinent...