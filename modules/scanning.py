import streamlit as st, nmap
from modules.base import BaseModule, ModuleRegistry
class ScanningModule(BaseModule):
    def __init__(self):
        super().__init__("Scanning","scanning"); ModuleRegistry.register(self)
    def render(self):
        st.header("Scanning")
        tgt=st.text_input("Target")
        if st.button("Scan") and tgt:
            sc=nmap.PortScanner(); sc.scan(tgt); st.json(sc[tgt])
ScanningModule()
