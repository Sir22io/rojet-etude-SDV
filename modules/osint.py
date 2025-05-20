import streamlit as st
import requests
from modules.base import BaseModule, ModuleRegistry

class OsintModule(BaseModule):
    def __init__(self):
        super().__init__(name="OSINT", key_prefix="osint")
        ModuleRegistry.register(self)

    def _github_search(self, q: str):
        url = f"https://api.github.com/search/repositories"
        params = { 'q': q, 'per_page': 5 }
        try:
            return requests.get(url, params=params, timeout=10).json()
        except Exception as e:
            return {'error': str(e)}

    def render(self):
        st.header("🕵️ OSINT")
        q = st.text_input("Keyword", placeholder="cve-2025")
        if st.button("Search", key="osint_btn") and q:
            out = self.run_and_store(q, self._github_search, q)
            st.json(out)

OsintModule()
