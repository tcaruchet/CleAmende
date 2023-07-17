# CléAmende

![Illustration de l'application CléAmende](static/notice-paiement-perdue.png "Notice de paiement perdue - Illustration de l'application CléAmende")

CléAmende est une application web développée en Python avec le framework Streamlit. Elle permet de calculer le numéro de télépaiement et la clé de e-paiement à partir d'un numéro de contravention français.



## Fonctionnalités

- Calcul du numéro de télépaiement et de la clé de e-paiement pour une contravention classique.
- Validation du numéro de contravention en fonction du type de contravention (classique ou forfait post stationnement).

## Installation

Pour installer et exécuter CléAmende, vous devez d'abord installer Streamlit. Vous pouvez le faire avec la commande suivante :

```bash
pip install streamlit
```

Ensuite, vous pouvez cloner ce dépôt et exécuter le programme avec la commande suivante :

```bash
streamlit run nom_du_fichier.py
```

Remplacez `nom_du_fichier.py` par le nom du fichier Python contenant le code de l'application.

## Utilisation

Lorsque vous exécutez l'application, une fenêtre de navigateur s'ouvre automatiquement avec l'interface utilisateur de l'application. Vous pouvez sélectionner le type de contravention, entrer le numéro de contravention et cliquer sur "Calculer" pour obtenir le numéro de télépaiement et la clé de e-paiement.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

CléAmende est sous licence MIT. Voir le fichier `LICENSE` pour plus d'informations.