import streamlit as st
from fpdf import FPDF
from io import BytesIO
import json, datetime
from modules.base import BaseModule, ModuleRegistry

class ReportingModule(BaseModule):
    def __init__(self):
        super().__init__("Reporting", "reporting")
        ModuleRegistry.register(self)

    class _PDF(FPDF):
        def header(self):
            self.set_font("Helvetica","B",16)
            self.cell(0,10,"Report",ln=True,align="C")
            self.ln(8)

    def _gen(self, data):
        pdf = self._PDF(); pdf.add_page(); pdf.set_font("Courier", size=10)
        for sec, itm in data.items():
            pdf.set_font("Courier","B",10); pdf.cell(0,8,f"[{sec.upper()}]",ln=True)
            pdf.set_font("Courier", size=10); pdf.multi_cell(0,5,json.dumps(itm, indent=2, default=str))
            pdf.ln(4)
        buf = BytesIO(); pdf.output(buf); return buf.getvalue()

    def render(self):
        st.header("📝 Reporting")
        t1,t2 = st.tabs(["View","PDF"])
        with t1:
            if not st.session_state.results: st.info("No data.")
            else: st.json(st.session_state.results)
        with t2:
            if st.button("Generate PDF", key="rep_btn") and st.session_state.results:
                pdf = self._gen(st.session_state.results)
                fn = datetime.datetime.utcnow().strftime("report_%Y%m%d_%H%M.pdf")
                st.download_button("DL PDF", pdf, file_name=fn, mime="application/pdf")

ReportingModule()
