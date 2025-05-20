import streamlit as st
from modules.base import ModuleRegistry

st.set_page_config(page_title="Pentest Toolbox", page_icon="🛠️", layout="wide")

# Auth OIDC
if not getattr(st, 'user', None) or not st.user.is_logged_in:
    st.title("Pentest Toolbox – Connexion requise")
    if st.button("Se connecter"):
        st.login()
    st.stop()

# Sidebar Profile
with st.sidebar:
    st.markdown(f"👤 **{st.user.get('name','Utilisateur')}**")
    if st.button("Se déconnecter"):
        st.logout()

# Init state
if 'results' not in st.session_state:
    st.session_state.results = {}

# Logo + module selection
st.sidebar.image('assets/logo.png', width=290)
page = st.sidebar.radio('Sélectionnez un module', ['Dashboard'] + ModuleRegistry.names())

if page == 'Dashboard':
    st.markdown("<h1 style='text-align:center;'>Dashboard</h1>", unsafe_allow_html=True)
    if not st.session_state.results:
        st.info("Aucun résultat. Lancez un module.")
    else:
        for sec, items in st.session_state.results.items():
            if items:
                for key,data in items.items():
                    with st.expander(f"{sec.capitalize()} – {key.split(':',1)[1] if ':' in key else key}"):
                        st.json(data) if data else st.warning("Pas de données.")
else:
    ModuleRegistry.get(page).render()

st.sidebar.info("💡 Sélectionnez un module pour commencer.")