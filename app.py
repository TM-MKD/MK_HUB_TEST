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
    .stApp {
        background: radial-gradient(circle at top left, #f7fbff 0%, #eef4ff 40%, #f7f8fc 100%);
    }

    [data-testid="stSidebar"],
    [data-testid="collapsedControl"] {
        display: none;
    }

    .hub-title {
        margin: 0;
        padding: 0;
        color: #081a3a;
        letter-spacing: 0.3px;
        font-weight: 800;
    }

    .intro-copy {
        color: #2f3a56;
        font-size: 1.05rem;
    }

    .tool-card {
        background: rgba(255, 255, 255, 0.82);
        backdrop-filter: blur(4px);
        border: 1px solid #d8e3f8;
        border-radius: 16px;
        padding: 1rem 1rem 1.1rem;
        box-shadow: 0 12px 22px rgba(14, 35, 79, 0.08);
        min-height: 210px;
    }

    .tool-desc {
        color: #3a4768;
        margin-bottom: 1rem;
    }

    .hub-button {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        width: 100%;
        padding: 0.82rem 1rem;
        border-radius: 12px;
        border: none;
        color: #ffffff !important;
        text-decoration: none !important;
        font-size: 16px;
        font-weight: 600;
        letter-spacing: 0.2px;
        transition: transform 0.15s ease, box-shadow 0.2s ease, filter 0.2s ease;
        box-shadow: 0 8px 18px rgba(21, 46, 92, 0.22);
    }

    .hub-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 13px 22px rgba(14, 35, 79, 0.30);
        filter: saturate(1.1);
    }

    .button-gold {
        background: linear-gradient(135deg, #b8860b 0%, #d4a017 55%, #f2c94c 100%);
    }

    .button-gold-alt {
        background: linear-gradient(135deg, #9f7610 0%, #c9971c 55%, #e8bd45 100%);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===================== HEADER =====================
col1, col2 = st.columns([1, 6])

with col1:
    try:
        st.image("assets/mkdons_badge.png", width=130)
    except Exception:
        pass

with col2:
    st.markdown(
        "<h1 class='hub-title'>MK Dons – Central Hub</h1>",
        unsafe_allow_html=True
    )

st.markdown("---")

st.markdown(
    """
    <p class="intro-copy">
    Welcome to the central hub for all MK Dons performance and coaching applications.

    Click on a tool below to open it in a new tab.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ===================== BUTTON GRID =====================
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="tool-card">
            <h3>Performance Profiling 📊</h3>
            <p class="tool-desc">Track and input player performance data.</p>
            <a class="hub-button button-gold" href="https://mkdons-player-profiling.streamlit.app/Data_Input" target="_blank">
                Open App
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="tool-card">
            <h3>Coach Evaluation Framework 🧠</h3>
            <p class="tool-desc">Analyse and review coaching performance.</p>
            <a class="hub-button button-gold-alt" href="https://cef-sandbox.streamlit.app/" target="_blank">
                Open App
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# ===================== FOOTER =====================
st.caption("More tools coming soon...")
