import streamlit as st, requests
from modules.base import BaseModule, ModuleRegistry
class OsintModule(BaseModule):
    def __init__(self):
        super().__init__("OSINT","osint"); ModuleRegistry.register(self)
    def render(self):
        st.header("OSINT")
        q=st.text_input("Keyword")
        if st.button("Search"):
            r=requests.get(f"https://api.github.com/search/repositories?q={q}&per_page=5").json()
            st.json(r)
OsintModule()