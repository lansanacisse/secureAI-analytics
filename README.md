# SecureIA Analytics

![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)  

Plateforme professionnelle d'analyse des logs et de détection d'intrusions réseau par Intelligence Artificielle.  
**Déploiement recommandé :** Docker ou Hugging Face Spaces.

---

## Description

SecureIA Analytics est une solution de sécurité opérationnelle conçue pour analyser des flux de logs réseau, détecter des comportements anormaux et produire des rapports exploitables.

### Objectifs
- Analyser les journaux d'événements réseau et de pare-feu.
- Détecter les anomalies à l'aide de modèles de Machine Learning.
- Surveiller les attaques potentielles et les schémas d'intrusion.
- Gérer l'import de fichiers **Parquet** et **CSV**.

---

## Fonctionnalités clés

- ✅ **Exploration interactive** des logs réseau.
- ✅ **Détection d'anomalies** avec Isolation Forest.
- ✅ **Analyse de la structure des données** avec ACP.
- ✅ **Visualisations avancées** des protocoles, ports et flux.
- ✅ **Import dynamique** de données Parquet/CSV.
- ✅ **Prêt pour le cloud** : Docker et déploiement Hugging Face Spaces.

---

## Technologies utilisées

- Python
- Streamlit
- Pandas / Polars
- Scikit-learn
- Plotly / Matplotlib / Seaborn
- SQLAlchemy
- Docker

---

## Installation locale

### Prérequis
- Python 3.11
- Docker (optionnel)
- Fichiers de logs en format **Parquet** ou **CSV**

### 1. Cloner le dépôt
```bash
git clone https://github.com/lansanacisse/security_m2sise.git
cd security_m2sise
```

### 2. Créer un environnement virtuel
```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer l'application
```bash
streamlit run app.py
```

### 5. Ouvrir l'application
Accédez à :

http://localhost:8501

---

## Déploiement Docker

```bash
docker build -t secureia-analytics .
docker run -p 7860:7860 secureia-analytics
```

---

## Déploiement cloud

Cette application est compatible avec Hugging Face Spaces et d'autres environnements Docker.

---

## Contacts

- **Lansana Cisse** : [GitHub](https://github.com/lansanacisse)
- **Quentin Lim** : [GitHub](https://github.com/QL2111)
- **Juan Alfonso** : [GitHub](https://github.com/jdalfons)
- **Mariem Amirouch** : [LinkedIn](https://www.linkedin.com/in/mariem-amirouch-b79a64256/)
- **Riyad ISMAILI** : [GitHub](https://github.com/riyadismaili)
