import streamlit as st
import nmap, subprocess, shlex
from modules.base import BaseModule, ModuleRegistry

class ScanningModule(BaseModule):
    def __init__(self):
        super().__init__(name="Scanning", key_prefix="scanning")
        ModuleRegistry.register(self)

    def _nmap_scan(self, target: str, args: str = "-sV -T4"):
        try:
            scanner = nmap.PortScanner()
            scanner.scan(target, arguments=args)
            return scanner[target]
        except Exception as e:
            return {'error': str(e)}

    def _nikto_scan(self, url: str):
        cmd = ["nikto", "-host", url]
        try:
            result = subprocess.run(cmd, text=True, capture_output=True, timeout=120)
            out = (result.stdout or "") + ("
" + result.stderr if result.stderr else "")
            return out.strip()
        except subprocess.TimeoutExpired as e:
            return f"Scan timed out after {e.timeout} seconds"
        except Exception as e:
            return str(e)

    def render(self):
        st.header("📡 Scanning")
        tab1, tab2 = st.tabs(["Nmap","Web Scan"])
        with tab1:
            tgt = st.text_input("IP or CIDR", key="scan_tgt")
            if st.button("Run Nmap", key="scan_btn") and tgt:
                out = self.run_and_store(tgt, self._nmap_scan, tgt)
                st.json(out)
        with tab2:
            url = st.text_input("URL", key="scan_url")
            if st.button("Run Web Scan", key="scan_web_btn") and url:
                out = self.run_and_store(url, self._nikto_scan, url)
                st.text(out)

ScanningModule()
