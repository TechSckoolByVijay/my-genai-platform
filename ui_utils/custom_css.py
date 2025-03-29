import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        .log-box {
            background-color: #1e1e1e;
            color: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            white-space: pre-wrap;
        }
        .log-info { color: #00ff00; }
        .log-warning { color: #ffcc00; }
        .log-error { color: #ff0000; }
        </style>
    """, unsafe_allow_html=True)
