import streamlit as st
from fpdf import FPDF
from io import BytesIO
import json,datetime
from modules.base import BaseModule,ModuleRegistry
class ReportingModule(BaseModule):
    def __init__(self): super().__init__("Reporting","reporting"); ModuleRegistry.register(self)
    def render(self):
        st.header("Reporting"); data=st.session_state.results
        if st.button("PDF") and data:
            pdf=FPDF(); pdf.add_page(); pdf.set_font("Courier",size=10)
            for k,v in data.items():
                pdf.cell(0,8,k,ln=True); pdf.multi_cell(0,5,json.dumps(v,indent=2,default=str))
            b=BytesIO(); pdf.output(b); st.download_button("DL PDF",b.getvalue(),"report.pdf")
ReportingModule()