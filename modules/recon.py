import streamlit as st, whois, requests
from modules.base import BaseModule, ModuleRegistry
class ReconModule(BaseModule):
    def __init__(self):
        super().__init__("Recon","recon"); ModuleRegistry.register(self)
    def render(self):
        st.header("Recon")
        d=st.text_input("Domain"); 
        if st.button("WHOIS") and d:
            st.json(whois.whois(d))
ReconModule()
