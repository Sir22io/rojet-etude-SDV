import streamlit as st,requests
from modules.base import BaseModule,ModuleRegistry
class OsintModule(BaseModule):
    def __init__(self): super().__init__("OSINT","osint"); ModuleRegistry.register(self)
    def _gh(self,q):
        try: return requests.get(f"https://api.github.com/search/repositories?q={q}&per_page=5",timeout=10).json()
        except Exception as e: return {"error":str(e)}
    def render(self):
        st.header("OSINT"); q=st.text_input("Keyword")
        if st.button("Search"): st.json(self.run_and_store(q,self._gh,q))
OsintModule()