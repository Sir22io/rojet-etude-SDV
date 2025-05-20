import streamlit as st
import nmap, subprocess, shlex
from modules.base import BaseModule, ModuleRegistry

class ScanningModule(BaseModule):
    def __init__(self):
        super().__init__("Scanning", "scanning")
        ModuleRegistry.register(self)

    def _nmap(self, target, args="-sV -T4"):
        try:
            scanner = nmap.PortScanner()
            scanner.scan(target, arguments=args)
            return scanner[target]
        except Exception as e:
            return {"error": str(e)}

    def _nikto(self, url):
        cmd = ["nikto", "-host", url]
        try:
            res = subprocess.run(cmd, text=True, capture_output=True, timeout=120)
            out = (res.stdout or "") + ("
" + res.stderr if res.stderr else "")
            return out.strip()
        except Exception as e:
            return str(e)

    def render(self):
        st.header("📡 Scanning")
        tab1, tab2 = st.tabs(["Nmap", "Web Scan"])
        with tab1:
            tgt = st.text_input("Target", key="scan_tgt")
            if st.button("Run Nmap", key="scan_btn") and tgt:
                out = self.run_and_store(tgt, self._nmap, tgt)
                st.json(out)
        with tab2:
            url = st.text_input("URL", key="scan_url")
            if st.button("Run Web Scan", key="scan_web_btn") and url:
                out = self.run_and_store(url, self._nikto, url)
                st.text(out)

ScanningModule()
