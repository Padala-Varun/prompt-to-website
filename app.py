import streamlit as st
from gemini_utils import generate_website_code
from templates.download_zip import create_zip_from_files
import os
import time
import json

# Enhanced page config with custom theme
st.set_page_config(
    page_title="AI Website Forge", 
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🚀"
)

# Custom CSS for extraordinary styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global styles */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Animated background */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(120, 219, 255, 0.3) 0%, transparent 50%);
        z-index: -1;
        animation: floating 20s ease-in-out infinite;
    }
    
    @keyframes floating {
        0%, 100% { transform: scale(1) rotate(0deg); }
        50% { transform: scale(1.1) rotate(180deg); }
    }
    
    /* Main container */
    .main-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        animation: slideUp 0.8s ease-out;
    }
    
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Title styling */
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #ffffff 0%, #f0f0f0 100%);
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 0 0 30px rgba(255, 255, 255, 0.5);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 20px rgba(255, 255, 255, 0.5); }
        to { text-shadow: 0 0 40px rgba(255, 255, 255, 0.8); }
    }
    
    .hero-subtitle {
        text-align: center;
        color: rgba(255, 255, 255, 0.8);
        font-size: 1.2rem;
        margin-bottom: 3rem;
        font-weight: 300;
    }
    
    /* Input area styling */
    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 2px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 16px !important;
        color: white !important;
        font-size: 1.1rem !important;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .stTextArea textarea:focus {
        border-color: rgba(255, 255, 255, 0.5) !important;
        box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.1) !important;
        transform: scale(1.02);
    }
    
    .stTextArea textarea::placeholder {
        color: rgba(255, 255, 255, 0.6) !important;
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%) !important;
        border: none !important;
        border-radius: 50px !important;
        color: white !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 20px rgba(238, 90, 36, 0.3) !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    
    .stButton button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 20px 40px rgba(238, 90, 36, 0.4) !important;
        background: linear-gradient(135deg, #ff7675 0%, #fd79a8 100%) !important;
    }
    
    .stButton button:active {
        transform: translateY(-1px) !important;
    }
    
    /* Success message */
    .stSuccess {
        background: linear-gradient(135deg, #00b894 0%, #00cec9 100%) !important;
        border: none !important;
        border-radius: 16px !important;
        color: white !important;
        animation: pulse 1s ease-in-out;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    /* Preview section */
    .preview-container {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 1.5rem;
        margin: 2rem 0;
        backdrop-filter: blur(10px);
        animation: fadeIn 1s ease-out 0.5s both;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Download section */
    .download-section {
        background: rgba(0, 0, 0, 0.2);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        animation: slideIn 0.8s ease-out 0.8s both;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    
    /* Download buttons */
    .download-btn {
        background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%) !important;
        border: none !important;
        border-radius: 12px !important;
        color: white !important;
        font-weight: 500 !important;
        margin: 0.25rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 5px 15px rgba(116, 185, 255, 0.3) !important;
    }
    
    .download-btn:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 25px rgba(116, 185, 255, 0.4) !important;
    }
    
    /* Section headers */
    .section-header {
        color: white;
        font-size: 1.8rem;
        font-weight: 600;
        margin: 2rem 0 1rem 0;
        text-align: center;
        position: relative;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 50%;
        transform: translateX(-50%);
        width: 60px;
        height: 3px;
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        border-radius: 2px;
    }
    
    /* Loading animation */
    .loading-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 3rem;
    }
    
    .loading-spinner {
        width: 60px;
        height: 60px;
        border: 4px solid rgba(255, 255, 255, 0.3);
        border-top: 4px solid #ff6b6b;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Metrics cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #ff6b6b;
        display: block;
    }
    
    .metric-label {
        color: rgba(255, 255, 255, 0.8);
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generation_count' not in st.session_state:
    st.session_state.generation_count = 0
if 'total_lines' not in st.session_state:
    st.session_state.total_lines = 0

# Hero section
st.markdown("""
<div class="main-container">
    <h1 class="hero-title">✨ AI Website Forge</h1>
    <p class="hero-subtitle">Transform your ideas into stunning websites with the power of AI</p>
</div>
""", unsafe_allow_html=True)

# Metrics row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
    <div class="metric-card">
        <span class="metric-value">{st.session_state.generation_count}</span>
        <div class="metric-label">Websites Generated</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <span class="metric-value">{st.session_state.total_lines:,}</span>
        <div class="metric-label">Lines of Code</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <span class="metric-value">⚡</span>
        <div class="metric-label">Lightning Fast</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <span class="metric-value">🎨</span>
        <div class="metric-label">AI Powered</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Input section with enhanced styling
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Enhanced prompt examples
example_prompts = [
    "🎨 Portfolio site for a creative designer with dark theme and smooth animations",
    "🏢 Modern corporate landing page with contact form and testimonials",
    "🍕 Restaurant website with menu, gallery, and online ordering",
    "💻 Tech startup homepage with hero section and feature showcase",
    "📚 Educational platform with course listings and student dashboard",
    "🎵 Music artist portfolio with audio player and tour dates"
]

selected_example = st.selectbox(
    "💡 Get inspired by these examples:",
    [""] + example_prompts,
    format_func=lambda x: "Choose an example..." if x == "" else x
)

prompt = st.text_area(
    "🚀 Describe your dream website",
    height=150,
    placeholder="Describe your vision in detail... The more specific you are, the better the AI can bring your ideas to life!",
    value=selected_example if selected_example else ""
)

# Enhanced generation button with loading states
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate_btn = st.button("🚀 Generate My Website", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

if generate_btn and prompt.strip():
    # Enhanced loading animation
    with st.container():
        st.markdown("""
        <div class="loading-container">
            <div class="loading-spinner"></div>
        </div>
        """, unsafe_allow_html=True)
        
        # Simulate progress with messages
        progress_messages = [
            "🧠 AI is analyzing your requirements...",
            "🎨 Designing the perfect layout...",
            "💻 Writing clean, modern code...",
            "✨ Adding finishing touches..."
        ]
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, message in enumerate(progress_messages):
            status_text.text(message)
            progress_bar.progress((i + 1) / len(progress_messages))
            time.sleep(0.8)  # Simulate processing time
        
        # Generate the actual website
        site_code = generate_website_code(prompt)
        
        # Clear loading elements
        progress_bar.empty()
        status_text.empty()
    
    # Save the files
    os.makedirs("generated_sites", exist_ok=True)
    html_content = site_code.get("html", "")
    css_content = site_code.get("css", "")
    js_content = site_code.get("js", "")
    
    with open("generated_sites/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    with open("generated_sites/styles.css", "w", encoding="utf-8") as f:
        f.write(css_content)
    with open("generated_sites/script.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    
    # Update metrics
    st.session_state.generation_count += 1
    st.session_state.total_lines += len(html_content.split('\n')) + len(css_content.split('\n')) + len(js_content.split('\n'))
    
    # Success message with animation
    st.success("🎉 Your website has been crafted to perfection!")
    
    # Enhanced preview section
    st.markdown('<div class="preview-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">🌐 Live Preview</h2>', unsafe_allow_html=True)
    
    # Full website preview
    st.components.v1.html(
        f"""
        <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>{css_content}</style>
            </head>
            <body>
                {html_content}
                <script>{js_content}</script>
            </body>
        </html>
        """, 
        height=700,
        scrolling=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # Enhanced download section
    st.markdown('<div class="download-section">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">📦 Download Your Website</h2>', unsafe_allow_html=True)
    
    # Individual file downloads with enhanced styling
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with open("generated_sites/index.html", "rb") as f:
            st.download_button(
                "📄 HTML File",
                f,
                file_name="index.html",
                mime="text/html",
                use_container_width=True
            )
    
    with col2:
        with open("generated_sites/styles.css", "rb") as f:
            st.download_button(
                "🎨 CSS Styles",
                f,
                file_name="styles.css",
                mime="text/css",
                use_container_width=True
            )
    
    with col3:
        with open("generated_sites/script.js", "rb") as f:
            st.download_button(
                "⚡ JavaScript",
                f,
                file_name="script.js",
                mime="application/javascript",
                use_container_width=True
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Main ZIP download
    zip_file = create_zip_from_files("generated_sites")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.download_button(
            "🏆 Download Complete Website (ZIP)",
            zip_file,
            file_name="my-awesome-website.zip",
            mime="application/zip",
            use_container_width=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)

