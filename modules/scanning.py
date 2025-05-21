import streamlit as st,nmap,subprocess,shlex
from modules.base import BaseModule,ModuleRegistry
class ScanningModule(BaseModule):
    def __init__(self): super().__init__("Scanning","scanning"); ModuleRegistry.register(self)
    def render(self):
        st.header("Scanning"); t=st.text_input("Target")
        if st.button("Nmap"): st.json(self.run_and_store(t,lambda x: nmap.PortScanner().scan(x,"-sV") or {},t))
        u=st.text_input("URL"); 
        if st.button("Web"): st.text(self.run_and_store(u,lambda x: subprocess.run(["nikto","-host",x],text=True,capture_output=True,timeout=60).stdout,u))
ScanningModule()