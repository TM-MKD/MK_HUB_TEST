import streamlit as st

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="MK Dons – App Hub",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===================== HEADER =====================
col1, col2 = st.columns([1, 6])

with col1:
    try:
        st.image("assets/mkdons_badge.png", width=80)
    except:
        pass

with col2:
    st.markdown(
        "<h1 style='margin:0; padding:0;'>MK Dons – Central Hub</h1>", 
        unsafe_allow_html=True
    )

st.markdown("---")

st.markdown("""
Welcome to the central hub for all MK Dons performance and coaching applications.

Click on a tools below to open it in a new tab.
""")

st.markdown("---")

# ===================== BUTTON GRID =====================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Performance Profiling")
    st.markdown("Track and input player performance data.")
    st.markdown(
        """
        <a href="https://mkdons-player-profiling.streamlit.app/Data_Input" target="_blank">
            <button style="
                width: 100%;
                padding: 12px;
                background-color: #1f77b4;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                cursor: pointer;">
                Open App
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.subheader("Coach Evaluation Framework")
    st.markdown("Analyse and review coaching performance.")
    st.markdown(
        """
        <a href="https://cef-sandbox.streamlit.app/" target="_blank">
            <button style="
                width: 100%;
                padding: 12px;
                background-color: #1f77b4;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                cursor: pointer;">
                Open App
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# ===================== FOOTER =====================
st.caption("More tools coming soon...")
