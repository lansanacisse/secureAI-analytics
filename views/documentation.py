# pages/documentation.py
import streamlit as st

PROJECT_NAME = "SecureIA Analytics"
SUPPORT_EMAIL = "support@secureia-analytics.com"

st.set_page_config(page_title=f"Documentation {PROJECT_NAME}", page_icon="📄")

st.title(f"📄 Documentation {PROJECT_NAME}")
st.markdown(f"""
### Bienvenue dans la documentation de {PROJECT_NAME} !

Cette documentation vous guide à travers les fonctionnalités de l'application.

#### Sections disponibles :
1. **Accueil** : Vue d'ensemble du tableau de bord.
2. **Analyse** : Analyse des logs de sécurité.
3. **Datasets** : Exploration des jeux de données.
4. **Protocol** : Analyse des flux réseau.
5. **Machine Learning** : Modèles d'apprentissage automatique.

#### Comment utiliser l'application :
- Utilisez la sidebar pour naviguer entre les différentes sections.
- Appliquez des filtres pour explorer les données.
- Consultez les statistiques et visualisations pour mieux comprendre les tendances.

#### Support :
Pour toute question ou assistance, contactez l'équipe de support à [{SUPPORT_EMAIL}](mailto:{SUPPORT_EMAIL}).
""")