import streamlit as st
from modules.base import ModuleRegistry

st.set_page_config(page_title="Pentest Toolbox", layout="wide")
if not getattr(st, 'user', None) or not st.user.is_logged_in:
    st.title("Connexion requise")
    if st.button("Login"): st.login()
    st.stop()
with st.sidebar:
    st.write(f"👤 {st.user.get('name')}")
    if st.button("Logout"): st.logout()
if 'results' not in st.session_state: st.session_state.results={}
st.sidebar.image('assets/logo.png')
page = st.sidebar.radio("Module", ["Dashboard"] + ModuleRegistry.names())
if page=="Dashboard":
    st.write("Dashboard")
else:
    ModuleRegistry.get(page).render()