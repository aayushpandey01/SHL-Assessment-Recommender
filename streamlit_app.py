"""
SHL Assessment Recommender - Streamlit UI
A clean, professional conversational interface for the recommender agent.
"""
from dotenv import load_dotenv
load_dotenv()
import os
import json
import requests
import streamlit as st

# ─────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────

from dotenv import load_dotenv
load_dotenv()

# Works both locally (.env) and on Streamlit Cloud (st.secrets)
try:
    API_URL = st.secrets["API_URL"]
except Exception:
    API_URL = os.getenv("API_URL", "http://localhost:8000")

TEST_TYPE_LABELS = {
    "A": "Ability & Aptitude",
    "B": "Behavioral Simulation",
    "C": "Competency",
    "D": "Development & 360",
    "E": "Assessment Exercise",
    "K": "Knowledge & Skills",
    "P": "Personality & Behavior",
    "S": "Situational Judgment",
}

TEST_TYPE_COLORS = {
    "A": "#2196F3",
    "B": "#FF9800",
    "K": "#4CAF50",
    "P": "#9C27B0",
    "S": "#F44336",
    "D": "#009688",
    "C": "#607D8B",
    "E": "#795548",
}

# ─────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="SHL Assessment Recommender",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# Custom CSS
# ─────────────────────────────────────────────

st.markdown("""
<style>
    /* SHL Brand Colors */
    :root {
        --shl-green: #6abf69;
        --shl-dark: #1a1a2e;
        --shl-gray: #f5f5f5;
    }

    .main-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        padding: 1.5rem 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        border-left: 5px solid #6abf69;
    }
    
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 1.8rem;
        font-weight: 700;
    }
    
    .main-header p {
        color: #a0aec0;
        margin: 0.3rem 0 0 0;
        font-size: 0.95rem;
    }

    .chat-user {
        background: #e8f5e9;
        border-left: 4px solid #6abf69;
        padding: 1rem 1.2rem;
        border-radius: 0 12px 12px 0;
        margin: 0.6rem 0;
    }

    .chat-assistant {
        background: #f8f9fa;
        border-left: 4px solid #2196F3;
        padding: 1rem 1.2rem;
        border-radius: 0 12px 12px 0;
        margin: 0.6rem 0;
    }

    .recommendation-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.06);
        transition: box-shadow 0.2s;
    }
    
    .recommendation-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    .type-badge {
        display: inline-block;
        padding: 2px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        color: white;
        margin-right: 6px;
    }

    .status-dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 6px;
    }
    
    .status-online { background-color: #4CAF50; }
    .status-offline { background-color: #f44336; }

    .stTextInput > div > div > input {
        border-radius: 25px !important;
        border: 2px solid #e2e8f0 !important;
        padding: 0.6rem 1.2rem !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #6abf69 !important;
        box-shadow: 0 0 0 3px rgba(106, 191, 105, 0.15) !important;
    }

    div[data-testid="stButton"] button {
        border-radius: 25px;
        font-weight: 600;
    }

    .sidebar-section {
        background: #f8f9fa;
        padding: 0.8rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }

    .quick-chip {
        display: inline-block;
        background: #e3f2fd;
        color: #1565c0;
        border-radius: 20px;
        padding: 4px 12px;
        font-size: 0.8rem;
        margin: 3px;
        cursor: pointer;
        border: 1px solid #90caf9;
    }

    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.8rem;
        border-radius: 8px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Session State
# ─────────────────────────────────────────────

if "messages" not in st.session_state:
    st.session_state.messages = []
if "all_recommendations" not in st.session_state:
    st.session_state.all_recommendations = []
if "conversation_ended" not in st.session_state:
    st.session_state.conversation_ended = False
if "api_status" not in st.session_state:
    st.session_state.api_status = None


# ─────────────────────────────────────────────
# API Helpers
# ─────────────────────────────────────────────

def check_api_health() -> bool:
    try:
        resp = requests.get(f"{API_URL}/health", timeout=5)
        return resp.status_code == 200
    except Exception:
        return False


def send_message(messages: list) -> dict:
    payload = {"messages": messages}
    resp = requests.post(f"{API_URL}/chat", json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()


# ─────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────

with st.sidebar:
    st.markdown("### 🎯 SHL Recommender")
    
    # API Status
    if st.button("Check API Status", use_container_width=True):
        st.session_state.api_status = check_api_health()
    
    if st.session_state.api_status is True:
        st.markdown('<span class="status-dot status-online"></span>API Online', unsafe_allow_html=True)
    elif st.session_state.api_status is False:
        st.markdown('<span class="status-dot status-offline"></span>API Offline', unsafe_allow_html=True)

    st.divider()

    # API Config
    st.markdown("#### ⚙️ Configuration")
    api_url_input = st.text_input("API URL", value=API_URL, key="api_url_input")
    if api_url_input != API_URL:
        API_URL = api_url_input

    st.divider()

    # Quick starters
    st.markdown("#### 💡 Quick Starters")
    quick_starters = [
        "I'm hiring a Java developer with 4 years of experience",
        "Looking for assessments for a senior sales manager",
        "Need tests for a data scientist role",
        "Hiring call center agents in bulk",
        "Looking for leadership assessments for C-suite",
        "Need a personality test for remote workers",
        "Assessing graduate applicants in finance",
        "Compare OPQ32r and Motivation Questionnaire",
    ]
    
    for qs in quick_starters:
        if st.button(f"📌 {qs[:45]}...", key=f"qs_{qs[:20]}", use_container_width=True):
            st.session_state["pending_message"] = qs
            st.rerun()

    st.divider()

    # Stats
    if st.session_state.all_recommendations:
        st.markdown("#### 📊 Session Stats")
        st.metric("Recommendations Given", len(st.session_state.all_recommendations))
        st.metric("Conversation Turns", len(st.session_state.messages) // 2)

    # Reset
    if st.button("🔄 New Conversation", use_container_width=True, type="secondary"):
        st.session_state.messages = []
        st.session_state.all_recommendations = []
        st.session_state.conversation_ended = False
        st.rerun()

    st.divider()
    
    # Test type legend
    st.markdown("#### 🔑 Test Type Legend")
    for code, label in TEST_TYPE_LABELS.items():
        color = TEST_TYPE_COLORS.get(code, "#666")
        st.markdown(
            f'<span class="type-badge" style="background:{color}">{code}</span> {label}',
            unsafe_allow_html=True
        )


# ─────────────────────────────────────────────
# Main Content
# ─────────────────────────────────────────────

# Header
st.markdown("""
<div class="main-header">
    <h1>🎯 SHL Assessment Recommender</h1>
    <p>Describe the role you're hiring for, and I'll recommend the right SHL assessments.</p>
</div>
""", unsafe_allow_html=True)

# Layout: Chat + Recommendations
col_chat, col_recs = st.columns([3, 2])

with col_chat:
    st.markdown("### 💬 Conversation")

    # Greeting if no messages
    if not st.session_state.messages:
        st.info(
            "👋 Hello! I'm your SHL Assessment Consultant. Tell me about the role you're hiring for "
            "and I'll recommend the most suitable assessments from the SHL catalog.\n\n"
            "**Try:** *\"I'm hiring a mid-level Java developer who works with stakeholders\"*"
        )

    # Render messages
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                f'<div class="chat-user"><strong>👤 You</strong><br>{msg["content"]}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="chat-assistant"><strong>🤖 SHL Assistant</strong><br>{msg["content"]}</div>',
                unsafe_allow_html=True
            )

    # Conversation ended banner
    if st.session_state.conversation_ended:
        st.success("✅ Recommendation complete! Start a new conversation or refine further.")

    # Input area
    # Auto-submit if quick starter was clicked
    pending = st.session_state.pop("pending_message", "")

    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input(
            "Your message",
            value=pending,
            placeholder="e.g. I need assessments for a Python developer, mid-level",
            label_visibility="collapsed",
        )
        submitted = st.form_submit_button("Send ➤", type="primary", use_container_width=True)

    # Auto-trigger if came from quick starter
    if pending and not submitted:
        submitted = True
        user_input = pending

    if submitted and user_input.strip():
        user_msg = {"role": "user", "content": user_input.strip()}
        st.session_state.messages.append(user_msg)

        with st.spinner("Thinking..."):
            try:
                result = send_message(st.session_state.messages)
                assistant_reply = result.get("reply", "Sorry, I couldn't generate a response.")
                recommendations = result.get("recommendations", [])
                end_of_conv = result.get("end_of_conversation", False)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_reply
                })

                if recommendations:
                    # Merge with existing (deduplicate by name)
                    existing_names = {r["name"] for r in st.session_state.all_recommendations}
                    st.session_state.all_recommendations = recommendations  # Replace (latest shortlist)

                st.session_state.conversation_ended = end_of_conv

            except requests.exceptions.ConnectionError:
                st.error("❌ Cannot connect to the API. Make sure the FastAPI server is running.")
            except requests.exceptions.Timeout:
                st.error("⏱️ Request timed out. The server took too long to respond.")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

        st.rerun()


with col_recs:
    st.markdown("### 📋 Recommended Assessments")

    if not st.session_state.all_recommendations:
        st.markdown("""
        <div style="text-align:center; padding: 3rem 1rem; color: #a0aec0;">
            <div style="font-size: 3rem;">🔍</div>
            <p style="margin-top: 1rem;">Recommendations will appear here once you describe the role.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        recs = st.session_state.all_recommendations
        st.markdown(f"**{len(recs)} assessment(s) recommended:**")

        for i, rec in enumerate(recs, 1):
            test_type = rec.get("test_type", "A")
            color = TEST_TYPE_COLORS.get(test_type, "#666")
            type_label = TEST_TYPE_LABELS.get(test_type, test_type)
            
            st.markdown(f"""
            <div class="recommendation-card">
                <div style="display:flex; align-items:flex-start; gap:10px;">
                    <div style="font-size:1.3rem; min-width:28px;">{i}.</div>
                    <div style="flex:1;">
                        <div style="font-weight:600; font-size:0.95rem; color:#1a1a2e;">{rec['name']}</div>
                        <div style="margin: 4px 0;">
                            <span class="type-badge" style="background:{color}">{test_type}</span>
                            <span style="font-size:0.75rem; color:#666;">{type_label}</span>
                        </div>
                        <a href="{rec['url']}" target="_blank" 
                           style="font-size:0.8rem; color:#2196F3; text-decoration:none;">
                           🔗 View in Catalog →
                        </a>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Export button
        st.divider()
        rec_json = json.dumps(recs, indent=2)
        st.download_button(
            label="📥 Export Recommendations (JSON)",
            data=rec_json,
            file_name="shl_recommendations.json",
            mime="application/json",
            use_container_width=True,
        )
        
        # Type breakdown
        if len(recs) > 1:
            st.divider()
            st.markdown("**Assessment Mix:**")
            type_counts = {}
            for r in recs:
                t = r.get("test_type", "?")
                type_counts[t] = type_counts.get(t, 0) + 1
            
            for t, count in sorted(type_counts.items()):
                color = TEST_TYPE_COLORS.get(t, "#666")
                label = TEST_TYPE_LABELS.get(t, t)
                st.markdown(
                    f'<span class="type-badge" style="background:{color}">{t}</span>'
                    f' {label}: **{count}**',
                    unsafe_allow_html=True
                )
