import streamlit as st

pg = st.navigation([
        st.Page("creator_report_unifor/build.py", title="Semgrep Relatorio", icon="🎯"),
    ])

pg.run()