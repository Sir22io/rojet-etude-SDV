import streamlit as st,whois,requests
from datetime import datetime
from modules.base import BaseModule,ModuleRegistry
class ReconModule(BaseModule):
    def __init__(self): super().__init__("Recon","recon"); ModuleRegistry.register(self)
    def render(self):
        st.header("Recon"); d=st.text_input("Domain"); 
        if st.button("WHOIS"): st.json(self.run_and_store(d,whois.whois,d))
        ip=st.text_input("IP"); 
        if st.button("IP Lookup"): st.json(self.run_and_store(ip,lambda x: requests.get(f"https://ipinfo.io/{x}/json",timeout=5).json(),ip))
        st.caption(f"Last run: {datetime.utcnow():%Y-%m-%d %H:%M UTC}")
ReconModule()