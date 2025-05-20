import streamlit as st
from modules.base import ModuleRegistry

st.set_page_config(page_title="Pentest Toolbox", page_icon="🛠️", layout="wide")

# Authentification
if not getattr(st, 'user', None) or not st.user.is_logged_in:
    st.title("Pentest Toolbox – Connexion requise")
    if st.button("Se connecter"):
        st.login()
    st.stop()

# Sidebar profile
with st.sidebar:
    st.markdown(f"👤 **{st.user.get('name','Utilisateur')}**")
    if st.button("Se déconnecter"):
        st.logout()

# State init
if 'results' not in st.session_state:
    st.session_state.results = {}

# UI
st.sidebar.image("assets/logo.png", width=200)
page = st.sidebar.radio("Module", ["Dashboard"] + ModuleRegistry.names())

if page == "Dashboard":
    st.markdown("<h1 style='text-align:center;'>Dashboard</h1>", unsafe_allow_html=True)
    if not st.session_state.results:
        st.info("Aucun résultat. Lancez un module.")
    else:
        for section, items in st.session_state.results.items():
            for key, data in items.items():
                with st.expander(f"{section} – {key}"):
                    st.json(data)
else:
    ModuleRegistry.get(page).render()
