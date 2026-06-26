# import streamlit as st
# import time
# from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

# # ── Page config ──────────────────────────────────────────────────────────────
# st.set_page_config(
#     page_title="ResearchMind · AI Research Agent",
#     page_icon="🔬",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# # ── Custom CSS ────────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@300;400;500&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

# /* ── Reset & base ── */
# html, body, [class*="css"] {
#     font-family: 'DM Sans', sans-serif;
#     color: #e8e4dc;
# }

# .stApp {
#     background: #0a0a0f;
#     background-image:
#         radial-gradient(ellipse 80% 50% at 20% -10%, rgba(255,140,50,0.12) 0%, transparent 60%),
#         radial-gradient(ellipse 60% 40% at 80% 110%, rgba(255,80,30,0.08) 0%, transparent 55%);
# }

# /* ── Hide default streamlit chrome ── */
# #MainMenu, footer, header { visibility: hidden; }
# .block-container { padding: 2rem 3rem 4rem; max-width: 1200px; }

# /* ── Hero header ── */
# .hero {
#     text-align: center;
#     padding: 3.5rem 0 2.5rem;
#     position: relative;
# }
# .hero-eyebrow {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.7rem;
#     font-weight: 500;
#     letter-spacing: 0.25em;
#     text-transform: uppercase;
#     color: #ff8c32;
#     margin-bottom: 1rem;
#     opacity: 0.9;
# }
# .hero h1 {
#     font-family: 'Syne', sans-serif;
#     font-size: clamp(2.8rem, 6vw, 5rem);
#     font-weight: 800;
#     line-height: 1.0;
#     letter-spacing: -0.03em;
#     color: #f0ebe0;
#     margin: 0 0 1rem;
# }
# .hero h1 span {
#     color: #ff8c32;
# }
# .hero-sub {
#     font-size: 1.05rem;
#     font-weight: 300;
#     color: #a09890;
#     max-width: 520px;
#     margin: 0 auto;
#     line-height: 1.65;
# }

# /* ── Divider ── */
# .divider {
#     height: 1px;
#     background: linear-gradient(90deg, transparent, rgba(255,140,50,0.3), transparent);
#     margin: 2rem 0;
# }

# /* ── Input card ── */
# .input-card {
#     background: rgba(255,255,255,0.03);
#     border: 1px solid rgba(255,140,50,0.15);
#     border-radius: 16px;
#     padding: 2rem 2.5rem;
#     margin-bottom: 2rem;
#     backdrop-filter: blur(8px);
# }

# /* ── Streamlit input overrides ── */
# .stTextInput > div > div > input {
#     background: rgba(255,255,255,0.05) !important;
#     border: 1px solid rgba(255,140,50,0.25) !important;
#     border-radius: 10px !important;
#     color: #f0ebe0 !important;
#     font-family: 'DM Sans', sans-serif !important;
#     font-size: 1rem !important;
#     padding: 0.75rem 1rem !important;
#     transition: border-color 0.2s, box-shadow 0.2s !important;
# }
# .stTextInput > div > div > input:focus {
#     border-color: #ff8c32 !important;
#     box-shadow: 0 0 0 3px rgba(255,140,50,0.12) !important;
# }
# .stTextInput > label {
#     font-family: 'DM Mono', monospace !important;
#     font-size: 0.72rem !important;
#     letter-spacing: 0.15em !important;
#     text-transform: uppercase !important;
#     color: #ff8c32 !important;
#     font-weight: 500 !important;
# }

# /* ── Button ── */
# .stButton > button {
#     background: linear-gradient(135deg, #ff8c32 0%, #ff5a1a 100%) !important;
#     color: #0a0a0f !important;
#     font-family: 'Syne', sans-serif !important;
#     font-weight: 700 !important;
#     font-size: 0.95rem !important;
#     letter-spacing: 0.04em !important;
#     border: none !important;
#     border-radius: 10px !important;
#     padding: 0.7rem 2.2rem !important;
#     cursor: pointer !important;
#     transition: transform 0.15s, box-shadow 0.15s, opacity 0.15s !important;
#     box-shadow: 0 4px 20px rgba(255,140,50,0.3) !important;
#     width: 100%;
# }
# .stButton > button:hover {
#     transform: translateY(-2px) !important;
#     box-shadow: 0 8px 28px rgba(255,140,50,0.4) !important;
#     opacity: 0.95 !important;
# }
# .stButton > button:active {
#     transform: translateY(0) !important;
# }

# /* ── Pipeline step cards ── */
# .step-card {
#     background: rgba(255,255,255,0.03);
#     border: 1px solid rgba(255,255,255,0.07);
#     border-radius: 14px;
#     padding: 1.5rem 1.8rem;
#     margin-bottom: 1.2rem;
#     position: relative;
#     overflow: hidden;
#     transition: border-color 0.3s;
# }
# .step-card.active {
#     border-color: rgba(255,140,50,0.4);
#     background: rgba(255,140,50,0.04);
# }
# .step-card.done {
#     border-color: rgba(80,200,120,0.3);
#     background: rgba(80,200,120,0.03);
# }
# .step-card::before {
#     content: '';
#     position: absolute;
#     left: 0; top: 0; bottom: 0;
#     width: 3px;
#     border-radius: 14px 0 0 14px;
#     background: rgba(255,255,255,0.05);
#     transition: background 0.3s;
# }
# .step-card.active::before { background: #ff8c32; }
# .step-card.done::before   { background: #50c878; }

# .step-header {
#     display: flex;
#     align-items: center;
#     gap: 0.8rem;
#     margin-bottom: 0.3rem;
# }
# .step-num {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.68rem;
#     font-weight: 500;
#     letter-spacing: 0.15em;
#     color: #ff8c32;
#     opacity: 0.7;
# }
# .step-title {
#     font-family: 'Syne', sans-serif;
#     font-size: 0.95rem;
#     font-weight: 700;
#     color: #f0ebe0;
# }
# .step-status {
#     margin-left: auto;
#     font-family: 'DM Mono', monospace;
#     font-size: 0.68rem;
#     letter-spacing: 0.1em;
# }
# .status-waiting  { color: #555; }
# .status-running  { color: #ff8c32; }
# .status-done     { color: #50c878; }

# /* ── Result panels ── */
# .result-panel {
#     background: rgba(255,255,255,0.025);
#     border: 1px solid rgba(255,255,255,0.07);
#     border-radius: 14px;
#     padding: 1.8rem 2rem;
#     margin-top: 1rem;
#     margin-bottom: 1.5rem;
# }
# .result-panel-title {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.7rem;
#     font-weight: 500;
#     letter-spacing: 0.2em;
#     text-transform: uppercase;
#     color: #ff8c32;
#     margin-bottom: 1rem;
#     padding-bottom: 0.7rem;
#     border-bottom: 1px solid rgba(255,140,50,0.15);
# }
# .result-content {
#     font-size: 0.92rem;
#     line-height: 1.8;
#     color: #cdc8bf;
#     white-space: pre-wrap;
#     font-family: 'DM Sans', sans-serif;
# }

# /* ── Report & feedback panels ── */
# .report-panel {
#     background: rgba(255,255,255,0.025);
#     border: 1px solid rgba(255,140,50,0.2);
#     border-radius: 16px;
#     padding: 2rem 2.5rem;
#     margin-top: 1rem;
# }
# .feedback-panel {
#     background: rgba(255,255,255,0.025);
#     border: 1px solid rgba(80,200,120,0.2);
#     border-radius: 16px;
#     padding: 2rem 2.5rem;
#     margin-top: 1rem;
# }
# .panel-label {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.7rem;
#     letter-spacing: 0.2em;
#     text-transform: uppercase;
#     margin-bottom: 1.2rem;
#     padding-bottom: 0.7rem;
# }
# .panel-label.orange {
#     color: #ff8c32;
#     border-bottom: 1px solid rgba(255,140,50,0.15);
# }
# .panel-label.green {
#     color: #50c878;
#     border-bottom: 1px solid rgba(80,200,120,0.15);
# }

# /* ── Progress text ── */
# .stSpinner > div { color: #ff8c32 !important; }

# /* ── Expander ── */
# details summary {
#     font-family: 'DM Mono', monospace !important;
#     font-size: 0.75rem !important;
#     color: #a09890 !important;
#     letter-spacing: 0.1em !important;
#     cursor: pointer;
# }

# /* ── Section heading ── */
# .section-heading {
#     font-family: 'Syne', sans-serif;
#     font-size: 1.3rem;
#     font-weight: 700;
#     color: #f0ebe0;
#     margin: 2rem 0 1rem;
# }

# /* ── Toast-style notice ── */
# .notice {
#     font-family: 'DM Mono', monospace;
#     font-size: 0.72rem;
#     color: #605850;
#     text-align: center;
#     margin-top: 3rem;
#     letter-spacing: 0.08em;
# }
# </style>
# """, unsafe_allow_html=True)


# # ── Helper: render a step card ────────────────────────────────────────────────
# def step_card(num: str, title: str, state: str, desc: str = ""):
#     status_map = {
#         "waiting": ("WAITING", "status-waiting"),
#         "running": ("● RUNNING", "status-running"),
#         "done":    ("✓ DONE",   "status-done"),
#     }
#     label, cls = status_map.get(state, ("", ""))
#     card_cls = {"running": "active", "done": "done"}.get(state, "")
#     st.markdown(f"""
#     <div class="step-card {card_cls}">
#         <div class="step-header">
#             <span class="step-num">{num}</span>
#             <span class="step-title">{title}</span>
#             <span class="step-status {cls}">{label}</span>
#         </div>
#         {"<div style='font-size:0.82rem;color:#706860;margin-top:0.3rem;'>"+desc+"</div>" if desc else ""}
#     </div>
#     """, unsafe_allow_html=True)


# # ── Session state init ────────────────────────────────────────────────────────
# for key in ("results", "running", "done"):
#     if key not in st.session_state:
#         st.session_state[key] = {} if key == "results" else False


# # ── Hero ──────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="hero">
#     <div class="hero-eyebrow">Multi-Agent AI System</div>
#     <h1>Research<span>Mind</span></h1>
#     <p class="hero-sub">
#         Four specialized AI agents collaborate — searching, scraping, writing,
#         and critiquing — to deliver a polished research report on any topic.
#     </p>
# </div>
# <div class="divider"></div>
# """, unsafe_allow_html=True)


# # ── Layout: input left, pipeline right ───────────────────────────────────────
# col_input, col_spacer, col_pipeline = st.columns([5, 0.5, 4])

# with col_input:
#     st.markdown('<div class="input-card">', unsafe_allow_html=True)
#     topic = st.text_input(
#         "Research Topic",
#         placeholder="e.g. Quantum computing breakthroughs in 2025",
#         key="topic_input",
#         label_visibility="visible",
#     )
#     run_btn = st.button("⚡  Run Research Pipeline", use_container_width=True)
#     st.markdown('</div>', unsafe_allow_html=True)

#     # Example chips
#     st.markdown("""
#     <div style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-bottom:1.5rem;">
#         <span style="font-family:'DM Mono',monospace;font-size:0.68rem;color:#605850;letter-spacing:0.1em;">TRY →</span>
#     """, unsafe_allow_html=True)
#     examples = ["LLM agents 2025", "CRISPR gene editing", "Fusion energy progress"]
#     for ex in examples:
#         st.markdown(f"""
#         <span style="
#             background:rgba(255,255,255,0.04);
#             border:1px solid rgba(255,255,255,0.08);
#             border-radius:6px;
#             padding:0.25rem 0.7rem;
#             font-size:0.75rem;
#             color:#a09890;
#             font-family:'DM Sans',sans-serif;
#             cursor:default;
#         ">{ex}</span>
#         """, unsafe_allow_html=True)
#     st.markdown("</div>", unsafe_allow_html=True)

# with col_pipeline:
#     st.markdown('<div class="section-heading">Pipeline</div>', unsafe_allow_html=True)

#     r = st.session_state.results
#     done = st.session_state.done

#     def s(step):
#         if not r:
#             return "waiting"
#         steps = ["search", "reader", "writer", "critic"]
#         idx = steps.index(step)
#         completed = list(r.keys())
#         # figure out which steps are done
#         if step in r:
#             return "done"
#         # which step is running now (first not in r)
#         if st.session_state.running:
#             for i, k in enumerate(steps):
#                 if k not in r:
#                     return "running" if k == step else "waiting"
#         return "waiting"

#     step_card("01", "Search Agent",  s("search"), "Gathers recent web information")
#     step_card("02", "Reader Agent",  s("reader"), "Scrapes & extracts deep content")
#     step_card("03", "Writer Chain",  s("writer"), "Drafts the full research report")
#     step_card("04", "Critic Chain",  s("critic"), "Reviews & scores the report")


# # ── Run pipeline ──────────────────────────────────────────────────────────────
# if run_btn:
#     if not topic.strip():
#         st.warning("Please enter a research topic first.")
#     else:
#         st.session_state.results = {}
#         st.session_state.running = True
#         st.session_state.done = False
#         st.rerun()

# if st.session_state.running and not st.session_state.done:
#     results = {}
#     topic_val = st.session_state.topic_input

#     # ── Step 1: Search ──
#     with st.spinner("🔍  Search Agent is working…"):
#         search_agent = build_search_agent()
#         sr = search_agent.invoke({
#             "messages": [("user", f"Find recent, reliable and detailed information about: {topic_val}")]
#         })
#         results["search"] = sr["messages"][-1].content
#         st.session_state.results = dict(results)
#     st.rerun() if False else None   # keep inline for now

#     # ── Step 2: Reader ──
#     with st.spinner("📄  Reader Agent is scraping top resources…"):
#         reader_agent = build_reader_agent()
#         rr = reader_agent.invoke({
#             "messages": [("user",
#                 f"Based on the following search results about '{topic_val}', "
#                 f"pick the most relevant URL and scrape it for deeper content.\n\n"
#                 f"Search Results:\n{results['search'][:800]}"
#             )]
#         })
#         results["reader"] = rr["messages"][-1].content
#         st.session_state.results = dict(results)

#     # ── Step 3: Writer ──
#     with st.spinner("✍️  Writer is drafting the report…"):
#         research_combined = (
#             f"SEARCH RESULTS:\n{results['search']}\n\n"
#             f"DETAILED SCRAPED CONTENT:\n{results['reader']}"
#         )
#         results["writer"] = writer_chain.invoke({
#             "topic": topic_val,
#             "research": research_combined
#         })
#         st.session_state.results = dict(results)

#     # ── Step 4: Critic ──
#     with st.spinner("🧐  Critic is reviewing the report…"):
#         results["critic"] = critic_chain.invoke({
#             "report": results["writer"]
#         })
#         st.session_state.results = dict(results)

#     st.session_state.running = False
#     st.session_state.done = True
#     st.rerun()


# # ── Results display ───────────────────────────────────────────────────────────
# r = st.session_state.results

# if r:
#     st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
#     st.markdown('<div class="section-heading">Results</div>', unsafe_allow_html=True)

#     # Raw outputs in expanders
#     if "search" in r:
#         with st.expander("🔍 Search Results (raw)", expanded=False):
#             st.markdown(f'<div class="result-panel"><div class="result-panel-title">Search Agent Output</div>'
#                         f'<div class="result-content">{r["search"]}</div></div>', unsafe_allow_html=True)

#     if "reader" in r:
#         with st.expander("📄 Scraped Content (raw)", expanded=False):
#             st.markdown(f'<div class="result-panel"><div class="result-panel-title">Reader Agent Output</div>'
#                         f'<div class="result-content">{r["reader"]}</div></div>', unsafe_allow_html=True)

#     # Final report
#     if "writer" in r:
#         st.markdown("""
#         <div class="report-panel">
#             <div class="panel-label orange">📝 Final Research Report</div>
#         """, unsafe_allow_html=True)
#         st.markdown(r["writer"])   # render markdown natively
#         st.markdown("</div>", unsafe_allow_html=True)

#         # Download
#         st.download_button(
#             label="⬇  Download Report (.md)",
#             data=r["writer"],
#             file_name=f"research_report_{int(time.time())}.md",
#             mime="text/markdown",
#         )

#     # Critic feedback
#     if "critic" in r:
#         st.markdown("""
#         <div class="feedback-panel">
#             <div class="panel-label green">🧐 Critic Feedback</div>
#         """, unsafe_allow_html=True)
#         st.markdown(r["critic"])
#         st.markdown("</div>", unsafe_allow_html=True)


# # ── Footer ────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="notice">
#     ResearchMind · Powered by LangChain multi-agent pipeline · Built with Streamlit
# </div>
# """, unsafe_allow_html=True)


import streamlit as st
import time
from agent import build_reader_agent, build_search_agent, writer_chain, critic_chain

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResearchGuru | AI Agent",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS (Pure Dark Mode Theme) ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Fira+Code:wght@400;500&display=swap');

/* ── Base Styles ── */
html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
    color: #e4e4e7; /* Light gray text */
}

/* Deep Dark Background */
.stApp {
    background-color: #0a0a0c; 
    background-image: 
        radial-gradient(circle at 15% 50%, rgba(139, 92, 246, 0.03), transparent 25%),
        radial-gradient(circle at 85% 30%, rgba(6, 182, 212, 0.03), transparent 25%);
}

/* ── Typography & Headers ── */
h1, h2, h3, h4 {
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    color: #ffffff;
}

.title-container {
    text-align: center;
    margin-top: 4rem;
    margin-bottom: 2rem;
    animation: fadeIn 1s ease-in-out;
}

.main-title {
    font-size: 4rem;
    line-height: 1;
    margin-bottom: 0.5rem;
    background: linear-gradient(135deg, #a78bfa 0%, #22d3ee 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.sub-title {
    font-size: 1.1rem;
    color: #8f8f9d;
    font-weight: 300;
}

/* ── Input overrides ── */
.stTextInput > div > div > input {
    background: #121214 !important; /* Dark input box */
    border: 1px solid #27272a !important;
    border-radius: 12px !important;
    color: #ffffff !important;
    padding: 1rem 1.5rem !important;
    font-size: 1.1rem !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3) !important;
    transition: all 0.3s ease !important;
}

.stTextInput > div > div > input:focus {
    border-color: #22d3ee !important;
    box-shadow: 0 0 15px rgba(34, 211, 238, 0.15) !important;
}

/* ── Primary Button ── */
.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #0891b2) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.8rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
    transition: all 0.3s ease !important;
    width: 100%;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(124, 58, 237, 0.3) !important;
    filter: brightness(1.1);
}

/* ── Horizontal Pipeline ── */
.pipeline-wrapper {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #121214;
    border: 1px solid #27272a;
    border-radius: 16px;
    padding: 1.5rem 2rem;
    margin: 2rem 0;
}

.pipe-step {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    flex: 1;
    position: relative;
    z-index: 1;
}

.pipe-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    font-weight: bold;
    border: 2px solid #27272a;
    background: #0a0a0c;
    color: #52525b;
    transition: all 0.3s ease;
}

.pipe-label {
    font-size: 0.85rem;
    font-weight: 600;
    color: #71717a;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Connectors */
.pipe-step:not(:last-child)::after {
    content: '';
    position: absolute;
    top: 20px;
    left: 60%;
    width: 80%;
    height: 2px;
    background: #27272a;
    z-index: -1;
    transition: background 0.4s ease;
}

/* Status Classes */
.pipe-step.running .pipe-icon {
    border-color: #06b6d4;
    color: #06b6d4;
    box-shadow: 0 0 15px rgba(6, 182, 212, 0.2);
    animation: pulse 1.5s infinite;
}
.pipe-step.running .pipe-label { color: #06b6d4; }

.pipe-step.done .pipe-icon {
    border-color: #8b5cf6;
    background: #8b5cf6;
    color: white;
}
.pipe-step.done .pipe-label { color: #8b5cf6; }
.pipe-step.done:not(:last-child)::after { background: #8b5cf6; }

@keyframes pulse {
    0% { transform: scale(0.95); }
    50% { transform: scale(1.05); }
    100% { transform: scale(0.95); }
}

/* ── Content Panels ── */
.content-box {
    background: #121214;
    border: 1px solid #27272a;
    border-radius: 12px;
    padding: 2rem;
    margin-top: 1rem;
    font-family: 'Outfit', sans-serif;
    line-height: 1.7;
    color: #e4e4e7;
}

.code-font {
    font-family: 'Fira Code', monospace;
    font-size: 0.85rem;
    color: #a1a1aa;
    white-space: pre-wrap;
}

/* Tab Overrides */
.stTabs [data-baseweb="tab-list"] {
    background-color: transparent;
}
.stTabs [data-baseweb="tab"] {
    color: #a1a1aa;
}
.stTabs [aria-selected="true"] {
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session state init ────────────────────────────────────────────────────────
for key in ("results", "running", "done", "search_topic"):
    if key not in st.session_state:
        st.session_state[key] = {} if key == "results" else False if key != "search_topic" else ""

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🌌 Research Guru")
    st.markdown("<div style='font-size: 0.9rem; color: #8f8f9d; margin-bottom: 2rem;'>Collaborative AI agents that research, analyze, and deliver reliable insights in minutes.</div>", unsafe_allow_html=True)
    
    st.markdown("### Suggested Topics")
    suggestions = [
        "Quantum computing breakthroughs in 2025",
        "CRISPR gene editing commercialization",
        "Solid-state battery materials",
        "AGI safety alignments"
    ]
    
    for sug in suggestions:
        if st.button(sug, key=f"btn_{sug[:5]}", use_container_width=True):
            st.session_state.search_topic = sug

# ── Helper function for Dynamic Pipeline UI ───────────────────────────────────
def draw_pipeline(current_phase="waiting"):
    """
    Renders the HTML for the pipeline based on the current phase.
    Phases: 'waiting', 'search', 'reader', 'writer', 'critic', 'done'
    """
    phases = ["search", "reader", "writer", "critic", "done"]
    
    def get_status(step_name):
        if current_phase == "waiting":
            return "waiting"
        
        current_idx = phases.index(current_phase)
        step_idx = phases.index(step_name)
        
        if step_idx < current_idx:
            return "done"
        elif step_idx == current_idx:
            return "running"
        else:
            return "waiting"

    html = f"""
    <div class="pipeline-wrapper">
        <div class="pipe-step {get_status('search')}">
            <div class="pipe-icon">1</div>
            <div class="pipe-label">Search</div>
        </div>
        <div class="pipe-step {get_status('reader')}">
            <div class="pipe-icon">2</div>
            <div class="pipe-label">Read & Scrape</div>
        </div>
        <div class="pipe-step {get_status('writer')}">
            <div class="pipe-icon">3</div>
            <div class="pipe-label">Draft Report</div>
        </div>
        <div class="pipe-step {get_status('critic')}">
            <div class="pipe-icon">4</div>
            <div class="pipe-label">Critic Review</div>
        </div>
    </div>
    """
    return html

# ── Main Layout Logic ─────────────────────────────────────────────────────────

# If no search is active, show the "Google-style" centered landing page
if not st.session_state.running and not st.session_state.done:
    
    st.markdown("""
    <div class="title-container">
        <h1 class="main-title">Research Guru</h1>
        <p class="sub-title">Deploy a swarm of AI agents to investigate any topic.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        topic = st.text_input(
            "Research Query", 
            value=st.session_state.search_topic,
            placeholder="What would you like to research today?", 
            label_visibility="collapsed"
        )
        
        if st.button("🚀 Initialize Agents"):
            if not topic.strip():
                st.warning("Please enter a research topic first.")
            else:
                st.session_state.search_topic = topic
                st.session_state.results = {}
                st.session_state.running = True
                st.session_state.done = False
                st.rerun()

# If pipeline is active or completed, show compact top bar & UI
else:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"### 🔍 Investigating: <span style='color:#22d3ee;'>{st.session_state.search_topic}</span>", unsafe_allow_html=True)
    with col2:
        if st.button("🔄 New Research"):
            st.session_state.running = False
            st.session_state.done = False
            st.session_state.results = {}
            st.rerun()

    # Create an empty placeholder for the dynamic pipeline
    pipeline_container = st.empty()

    # If already done, render the completed pipeline immediately
    if st.session_state.done:
        pipeline_container.markdown(draw_pipeline("done"), unsafe_allow_html=True)

# ── Execution Logic ───────────────────────────────────────────────────────────
if st.session_state.running and not st.session_state.done:
    results = {}
    topic_val = st.session_state.search_topic

    # ── Step 1: Search ──
    pipeline_container.markdown(draw_pipeline("search"), unsafe_allow_html=True)
    with st.spinner("Search Agent is scraping the web..."):
        search_agent = build_search_agent()
        sr = search_agent.invoke({
            "messages": [("user", f"Find recent, reliable and detailed information about: {topic_val}")]
        })
        results["search"] = sr["messages"][-1].content
        st.session_state.results = dict(results)

    # ── Step 2: Reader ──
    pipeline_container.markdown(draw_pipeline("reader"), unsafe_allow_html=True)
    with st.spinner("Reader Agent is extracting deep context..."):
        reader_agent = build_reader_agent()
        rr = reader_agent.invoke({
            "messages": [("user",
                f"Based on the following search results about '{topic_val}', "
                f"pick the most relevant URL and scrape it for deeper content.\n\n"
                f"Search Results:\n{results['search'][:800]}"
            )]
        })
        results["reader"] = rr["messages"][-1].content
        st.session_state.results = dict(results)

    # ── Step 3: Writer ──
    pipeline_container.markdown(draw_pipeline("writer"), unsafe_allow_html=True)
    with st.spinner("Writer Chain is structuring the report..."):
        research_combined = (
            f"SEARCH RESULTS:\n{results['search']}\n\n"
            f"DETAILED SCRAPED CONTENT:\n{results['reader']}"
        )
        results["writer"] = writer_chain.invoke({
            "topic": topic_val,
            "research": research_combined
        })
        st.session_state.results = dict(results)

    # ── Step 4: Critic ──
    pipeline_container.markdown(draw_pipeline("critic"), unsafe_allow_html=True)
    with st.spinner("Critic Agent is finalizing quality checks..."):
        results["critic"] = critic_chain.invoke({
            "report": results["writer"]
        })
        st.session_state.results = dict(results)

    # ── Finish ──
    pipeline_container.markdown(draw_pipeline("done"), unsafe_allow_html=True)
    st.session_state.running = False
    st.session_state.done = True
    st.rerun()

# ── Tabbed Results Display ────────────────────────────────────────────────────
if st.session_state.done:
    r = st.session_state.results
    
    # Use native Streamlit tabs for a much cleaner layout
    tab_report, tab_feedback, tab_raw = st.tabs(["📝 Final Report", "🧐 Critic Feedback", "⚙️ Raw Data Logs"])
    
    with tab_report:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown(r.get("writer", "No report generated."))
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.download_button(
            label="⬇ Download Markdown (.md)",
            data=r.get("writer", ""),
            file_name=f"{st.session_state.search_topic.replace(' ', '_')}_report.md",
            mime="text/markdown",
            use_container_width=True
        )

    with tab_feedback:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("### Evaluation & Critique")
        st.markdown(r.get("critic", "No feedback generated."))
        st.markdown('</div>', unsafe_allow_html=True)

    with tab_raw:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Search Results Array")
            st.markdown(f'<div class="content-box code-font">{r.get("search", "N/A")}</div>', unsafe_allow_html=True)
        with col2:
            st.markdown("#### Scraped HTML/Text Data")
            st.markdown(f'<div class="content-box code-font">{r.get("reader", "N/A")}</div>', unsafe_allow_html=True)