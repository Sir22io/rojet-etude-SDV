import streamlit as st
from fpdf import FPDF
from io import BytesIO
import json
from modules.base import BaseModule, ModuleRegistry
class ReportingModule(BaseModule):
    def __init__(self):
        super().__init__("Reporting","reporting"); ModuleRegistry.register(self)
    def render(self):
        st.header("Reporting")
        if st.button("PDF"):
            pdf=FPDF(); pdf.add_page(); pdf.set_font("Courier",size=10)
            txt=json.dumps(st.session_state.results, indent=2)
            pdf.multi_cell(0,5,txt)
            buf=BytesIO(); pdf.output(buf); st.download_button("Download PDF", buf.getvalue(), "report.pdf","application/pdf")
ReportingModule()