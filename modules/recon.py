import streamlit as st
import whois, requests
from datetime import datetime
from modules.base import BaseModule, ModuleRegistry

class ReconModule(BaseModule):
    def __init__(self):
        super().__init__(name="Recon", key_prefix="recon")
        ModuleRegistry.register(self)

    def _whois_lookup(self, domain: str):
        try: return whois.whois(domain)
        except Exception as e: return {'error': str(e)}

    def _ip_lookup(self, ip: str):
        try:
            resp = requests.get(f"https://ipinfo.io/{ip}/json", timeout=10)
            resp.raise_for_status()
            return resp.json()
        except Exception as e: return {'error': str(e)}

    def render(self):
        st.header("🔍 Reconnaissance")
        tab1, tab2 = st.tabs(["WHOIS / Domain", "IP Lookup"])
        with tab1:
            domain = st.text_input("Domain", key="whois_domain")
            if st.button("Run WHOIS", key="whois_btn") and domain:
                data = self.run_and_store(domain, self._whois_lookup, domain)
                st.json(data)
        with tab2:
            ip = st.text_input("IP address", key="ip_btn")
            if st.button("Lookup IP", key="ip_btn") and ip:
                data = self.run_and_store(ip, self._ip_lookup, ip)
                st.json(data)
        st.caption(f"Last run: {datetime.utcnow():%Y-%m-%d %H:%M UTC}")

ReconModule()
