import os, toml
import streamlit as st
from modules.base import ModuleRegistry

# Autogenerate secrets file if missing
if not os.path.exists(".streamlit/secrets.toml"):
    os.makedirs(".streamlit", exist_ok=True)
    cfg = toml.load("secrets.toml.example")
    # inject real creds
    cfg['auth']['client_id'] = "8BAb9oH8YY8aaHWRk44lt32YGrtUHDvB"
    cfg['auth']['client_secret'] = "_dgDcOxV5Z6wGOWQKvMAY8TaigQJMMlmccfBkAcbD0dAHrVNAJTiKMj1pTRSdVy9"
    cfg['auth']['server_metadata_url'] = "https://dev-kpr0aaljq6domnhv.us.auth0.com/.well-known/openid-configuration"
    with open(".streamlit/secrets.toml","w") as f:
        toml.dump(cfg, f)

st.set_page_config(page_title="Pentest Toolbox", page_icon="🛠️", layout="wide")

# Auth
if not getattr(st, 'user', None) or not st.user.is_logged_in:
    st.title("Pentest Toolbox – Connexion requise")
    if st.button("Se connecter"): st.login()
    st.stop()

# Sidebar profile
with st.sidebar:
    st.markdown(f"👤 **{st.user.get('name','Utilisateur')}**")
    if st.button("Se déconnecter"): st.logout()

# Init
st.session_state.setdefault('results', {})

# UI
st.sidebar.image("assets/logo.png")
page = st.sidebar.radio("Module", ["Dashboard"] + ModuleRegistry.names())
if page=="Dashboard":
    st.write("Dashboard")
else:
    ModuleRegistry.get(page).render()
