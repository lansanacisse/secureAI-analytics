import streamlit as st
from streamlit_option_menu import option_menu
from db import Database, LogDatabase
from views.analysis import analyze_logs  #
from views.data import explore_data  
from views.protocol import analyze_flows 
from views.upload import upload_page 
from views.machine_learning import machine_learning_page
from db import LogDatabase

PROJECT_NAME = "SecureIA Analytics"
PROJECT_TAGLINE = "Plateforme professionnelle d'analyse des logs et de détection d'intrusions par IA"
SUPPORT_EMAIL = "support@secureia-analytics.com"
GITHUB_URL = "https://github.com/lansanacisse/security_m2sise"


def user_page():


    # Sidebar navigation with streamlit-option-menu
    with st.sidebar:
        st.image("img/logo.png", use_container_width=True)
        st.markdown(f"<h1 style='text-align: center;'>{PROJECT_NAME}</h1>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; color: #555;'>{PROJECT_TAGLINE}</p>", unsafe_allow_html=True)
        # Navigation menu with icons
        selected_tab = option_menu(
            menu_title=None,  # Added menu_title parameter
            options=["Accueil", "Upload", "Analyse", "Datasets", "Protocol", "Machine Learning"],
            icons=["house", "arrow-up", "bar-chart", "search", "robot", "cpu"],
            menu_icon="cast",
            default_index=0,
            styles={
            "container": {"padding": "5px", "background-color": "#f0f2f6"},
            "icon": {"color": "orange", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "color": "black"},
            "nav-link-selected": {"background-color": "#4CAF50", "color": "white"},
            }
        )

    # Content based on selection
    if selected_tab == "Accueil":
        st.write(f"Bienvenue sur {PROJECT_NAME} !")
        st.markdown(f"""
            **{PROJECT_TAGLINE}**
            - Analysez vos logs de sécurité
            - Identifiez les anomalies réseau
            - Explorez les données opérationnelles
            - Appliquez des modèles de Machine Learning
        """)

    elif selected_tab == "Upload":
        upload_page()
    elif selected_tab == "Analyse":
        st.title("Analyse des logs de sécurité")
        analyze_logs()
        
    elif selected_tab == "Datasets":
        st.title("Exploration des données")
        explore_data()
    elif selected_tab == "Protocol":  # Fixed typo in "Protocol"
        st.title("Statistiques des flux réseau par Protocol")
        analyze_flows()

    elif selected_tab == "Machine Learning":
        machine_learning_page()
    
   # Quick links section after filters and content
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📄 À propos")
        st.write(f"Tableau de bord maintenu par l'équipe {PROJECT_NAME}.")
        st.write(f"Pour plus d'informations, visitez le [dépôt GitHub]({GITHUB_URL}).")
        st.write(f"Assistance : {SUPPORT_EMAIL}")

    with col2:
        st.markdown("### Collaborateurs")
        st.write("""
        - [Lansana Cisse](https://github.com/lansanacisse)
        - [Quentin Lim](https://github.com/QL2111)
        - [Juan Alfonso](https://github.com/jdalfons)
        - [Mariem Amirouch](https://www.linkedin.com/in/mariem-amirouch-b79a64256/)
        - [Riyad ISMAILI](https://github.com/riyadismaili)
        """)
