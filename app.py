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
        position: relative;
        
        background-color: #f2f5fb;
    }

    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        background-image: linear-gradient(rgba(242, 245, 251, 0.70), rgba(242, 245, 251, 0.70)), url("https://images.gc.miltonkeynesdonsfcservices.co.uk/fit-in/2400x1350/11054e00-315b-11ef-a1bb-31ab0db176a1.webp");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        z-index: -1;
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
        background: linear-gradient(135deg, #D9A00F 0%, #edb118 33%, #fcd45b 100%);
    }

    .social-links {
        display: flex;
        gap: 0.75rem;
        margin-top: 0.6rem;
    }

    .social-links a {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 42px;
        height: 42px;
        border-radius: 999px;
        background: #ffffff;
        border: 1px solid #d8e3f8;
        box-shadow: 0 6px 14px rgba(14, 35, 79, 0.12);
        transition: transform 0.15s ease, box-shadow 0.2s ease;
    }

    .social-links a:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 18px rgba(14, 35, 79, 0.18);
    }

    .social-links img {
        width: 22px;
        height: 22px;
    }

    .social-links .social-emoji {
        font-size: 21px;
        line-height: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===================== HEADER =====================
col1, col2 = st.columns([1, 6])

with col1:
    try:
        st.image("assets/mkdons_badge.png", width=160)
    except Exception:
        pass

with col2:
    st.markdown(
        """
        <h1 class='hub-title'>MK Dons Academy – Central Hub</h1>
        <div class='social-links'>
            <a href='https://x.com/MKDonsFCAcademy' target='_blank' aria-label='MK Dons Academy on X'>
                <img src='https://cdn.simpleicons.org/x/081a3a' alt='X logo'/>
            </a>
            <a href='https://www.youtube.com/@mkdonsacademyanalysis' target='_blank' aria-label='MK Dons Academy Analysis on YouTube'>
                <img src='https://cdn.simpleicons.org/youtube/FF0000' alt='YouTube logo'/>
            </a>
            <a href='https://www.instagram.com/mkdonsfcacademy/' target='_blank' aria-label='MK Dons Academy Analysis on Instagram'>
                <img src='https://cdn.simpleicons.org/instagram/FF0000' alt='Instagram logo'/>
            </a>
        </div>
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
            <h3>Welcome to the central hub for all MK Dons performance and coaching applications ⚽️</h3>
            <h4>Click on a tool to open it in a new tab 👈</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="tool-card">
            <h3>Central Intelligence Files 🗄️</h3>
            <p class="tool-desc">Access to the Central Intelligence folders on SharePoint.</p>
            <a class="hub-button button-gold" href="https://stadiummk.sharepoint.com/teams/CentralIntelligence/Shared%20Documents/Forms/AllItems.aspx?id=%2Fteams%2FCentralIntelligence%2FShared%20Documents%2FCentral%20Intelligence%20%2D%20MK%20Dons%20Academy&viewid=e7b75dc7%2D8452%2D4245%2Da735%2Def9d18208b9a' target='_blank' aria-label='MK Dons Academy SharePoint folder" target="_blank">
                Open SharePoint
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# ===================== COACH APPS =====================
st.markdown("---")
st.markdown(
        """
        <h3 class='hub-title'>Coaching</h3>
        """,
        unsafe_allow_html=True
    )

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="tool-card">
            <h3>Coaching Hub 👥</h3>
            <p class="tool-desc">Access to all coaching resources.</p>
            <a class="hub-button button-gold" href="https://mkdonscoaching.streamlit.app" target="_blank">
                Open Hub
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
            <a class="hub-button button-gold" href="https://cef-dashboard-mk.streamlit.app/" target="_blank">
                Open App
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# ===================== DATA APPS =====================
st.markdown("---")
st.markdown(
        """
        <h3 class='hub-title'>Data</h3>
        """,
        unsafe_allow_html=True
    )

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="tool-card">
            <h3>Academy Analysis Dashboard 📈</h3>
            <p class="tool-desc">Investigate key data, trends and benchmarking.</p>
            <a class="hub-button button-gold" href="https://mkdanalysisdashboard.streamlit.app" target="_blank">
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
            <h3>Performance Profiling 📊</h3>
            <p class="tool-desc">Track and input player performance data.</p>
            <a class="hub-button button-gold" href="https://mkdons-player-profiling.streamlit.app/Data_Input" target="_blank">
                Open App
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    
st.markdown("<div class='button-row-gap'></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="tool-card">
            <h3>Physical Performance Data 💪</h3>
            <p class="tool-desc">Analyse and interpret all player's physical data.</p>
            <a class="hub-button button-gold" href="https://mkapptest.streamlit.app/" target="_blank">
                Open App
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# ===================== ADMIN APPS =====================
st.markdown("---")
st.markdown(
        """
        <h3 class='hub-title'>Admin</h3>
        """,
        unsafe_allow_html=True
    )

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="tool-card">
            <h3>Season Calendar 📆</h3>
            <p class="tool-desc">Search for key dates and fixtures.</p>
            <a class="hub-button button-gold" href="https://mkapptest.streamlit.app/" target="_blank">
                Open Calendar
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
     st.markdown(
        """
        <div class="tool-card">
            <h3>MyConcern Reporting 🗳️</h3>
            <p class="tool-desc">Access all essential safeguarding tools.</p>
            <a class="hub-button button-gold" href="https://login.thesafeguardingcompany.com/" target="_blank">
                Open MyConcern
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# ===================== FOOTER =====================
st.caption("MK Dons Academy - Central Hub")
