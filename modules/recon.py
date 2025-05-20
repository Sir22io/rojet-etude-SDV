import streamlit as st
import whois, requests
from datetime import datetime
from modules.base import BaseModule, ModuleRegistry

class ReconModule(BaseModule):
    def __init__(self):
        super().__init__("Recon", "recon")
        ModuleRegistry.register(self)

    def _whois(self, domain):
        try:
            return whois.whois(domain)
        except Exception as e:
            return {"error": str(e)}

    def _ip(self, ip):
        try:
            resp = requests.get(f"https://ipinfo.io/{ip}/json", timeout=10)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    def render(self):
        st.header("🔍 Reconnaissance")
        tab1, tab2 = st.tabs(["WHOIS", "IP Lookup"])
        with tab1:
            d = st.text_input("Domain", key="whois_domain")
            if st.button("Run WHOIS", key="whois_btn") and d:
                out = self.run_and_store(d, self._whois, d)
                st.json(out)
        with tab2:
            ip = st.text_input("IP", key="ip_domain")
            if st.button("Lookup IP", key="ip_btn") and ip:
                out = self.run_and_store(ip, self._ip, ip)
                st.json(out)
        st.caption(f"Last run: {datetime.utcnow():%Y-%m-%d %H:%M UTC}")

ReconModule()
