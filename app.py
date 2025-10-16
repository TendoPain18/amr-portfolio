import streamlit as st

st.set_page_config(page_title="Amr Ashraf | Portfolio", layout="wide")

# Custom CSS for enhanced styling
st.markdown("""
<style>
    /* Global Styles */
    :root {
        --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --text-color: #1a1a1a;
        --bg-light: #f8f9fa;
    }
    
    /* Main container */
    .main {
        background: linear-gradient(180deg, #f8f9fa 0%, #ffffff 100%);
    }
    
    /* Card hover effect */
    .project-card {
        transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        transform: translateY(0);
    }
    
    .project-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 16px 32px rgba(0, 0, 0, 0.15) !important;
    }
    
    /* Title styling */
    h1 {
        color: #1a1a1a;
        font-size: 3em;
        font-weight: 700;
        margin-bottom: 10px;
    }
    
    h2 {
        color: #2d3748;
        font-weight: 600;
    }
    
    /* Button styling */
    .stLinkButton > button {
        border-radius: 10px;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Sidebar styling */
    .sidebar .stRadio > label {
        font-size: 1.1em;
        font-weight: 500;
    }
    
    /* Contact cards */
    .contact-card {
        background: linear-gradient(135deg, #ffffff 0%, #f7f7f7 100%);
        border: 2px solid #e0e0e0;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }
    
    .contact-card:hover {
        border-color: #667eea;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.15);
        transform: translateY(-5px);
    }
    
    /* Divider */
    hr {
        border: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 2rem 0;
    }
    
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🎯 Navigation")
st.sidebar.markdown("---")
page = st.sidebar.radio("Go to:", ["🏠 Home", "🎮 Games", "🤖 ML Projects", "📞 Contact"])

# HOME PAGE
if page == "🏠 Home":
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("Hi, I'm Amr Ashraf 👋")
        st.write("""
        Welcome to my portfolio!  
        I'm a passionate **Data Scientist** skilled in **Python**, **Machine Learning**, and **Game Development**.  
        Explore my creative projects and technical work below 👇
        """)
    
    st.markdown("---")
    st.subheader("✨ Quick Navigation")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("🎮 View Games", "#", use_container_width=True)
    with col2:
        st.link_button("🤖 View ML Projects", "#", use_container_width=True)
    with col3:
        st.link_button("📧 Contact Me", "#", use_container_width=True)
    
    st.markdown("---")
    st.subheader("📊 About Me")
    st.write("""
    I'm dedicated to creating innovative solutions through data science and game development. 
    With expertise in machine learning algorithms, neural networks, and interactive applications, 
    I love turning ideas into reality.
    """)

# GAMES PAGE
elif page == "🎮 Games":
    st.title("🎮 Game Projects")
    st.markdown("Explore my interactive game creations")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 20px;
            padding: 40px 30px;
            text-align: center;
            height: 320px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
            transition: all 0.3s ease;
        ">
            <h2 style="margin: 0; font-size: 2em;">💰 Who Wants to Be a Millionaire</h2>
            <p style="margin-top: 15px; font-size: 1.05em; opacity: 0.95;">Interactive Tkinter Quiz Game</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.link_button("🎮 Play Game", "https://YOUR_GAME_LINK.streamlit.app", use_container_width=True)
        st.link_button("📂 View Code", "https://github.com/TendoPain18/millionaire-game", use_container_width=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            border-radius: 20px;
            padding: 40px 30px;
            text-align: center;
            height: 320px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            box-shadow: 0 10px 30px rgba(245, 87, 108, 0.3);
        ">
            <h2 style="margin: 0; font-size: 2em;">🎯 Coming Soon</h2>
            <p style="margin-top: 15px; font-size: 1.05em; opacity: 0.95;">Game 2 - Stay Tuned!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("🚀 Coming soon...")
    
    with col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            border-radius: 20px;
            padding: 40px 30px;
            text-align: center;
            height: 320px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            box-shadow: 0 10px 30px rgba(79, 172, 254, 0.3);
        ">
            <h2 style="margin: 0; font-size: 2em;">🎨 Coming Soon</h2>
            <p style="margin-top: 15px; font-size: 1.05em; opacity: 0.95;">Game 3 - Stay Tuned!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("🚀 Coming soon...")

# ML PROJECTS PAGE
elif page == "🤖 ML Projects":
    st.title("🤖 Machine Learning Projects")
    st.markdown("Cutting-edge AI and ML applications")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            border-radius: 20px;
            padding: 40px 30px;
            text-align: center;
            height: 320px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            box-shadow: 0 10px 30px rgba(250, 112, 154, 0.3);
        ">
            <h2 style="margin: 0; font-size: 2em;">🧠 EEG Classifier</h2>
            <p style="margin-top: 15px; font-size: 1.05em; opacity: 0.95;">Motor Imagery Classification</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.link_button("🌐 Live Demo", "https://YOUR_EEG_APP.streamlit.app", use_container_width=True)
        st.link_button("📂 View Code", "https://github.com/TendoPain18/eeg-classifier", use_container_width=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #30cfd0 0%, #330867 100%);
            border-radius: 20px;
            padding: 40px 30px;
            text-align: center;
            height: 320px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            box-shadow: 0 10px 30px rgba(48, 207, 208, 0.3);
        ">
            <h2 style="margin: 0; font-size: 2em;">📊 Coming Soon</h2>
            <p style="margin-top: 15px; font-size: 1.05em; opacity: 0.95;">Project 2 - Stay Tuned!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("🚀 Coming soon...")
    
    with col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            border-radius: 20px;
            padding: 40px 30px;
            text-align: center;
            height: 320px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            box-shadow: 0 10px 30px rgba(168, 237, 234, 0.3);
        ">
            <h2 style="margin: 0; font-size: 2em;">🤖 Coming Soon</h2>
            <p style="margin-top: 15px; font-size: 1.05em; opacity: 0.95;">Project 3 - Stay Tuned!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("🚀 Coming soon...")

# CONTACT PAGE
elif page == "📞 Contact":
    st.title("📬 Get in Touch")
    st.markdown("Feel free to reach out to me on any of these platforms:")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="contact-card">
            <h3 style="color: #667eea; margin-bottom: 15px;">📧 Email</h3>
            <p style="font-size: 1.05em; color: #2d3748; word-break: break-all;">
                <strong>amr.gadalla01@gmail.com</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="contact-card">
            <h3 style="color: #0077b5; margin-bottom: 15px;">💼 LinkedIn</h3>
            <p>
                <a href="https://www.linkedin.com/in/amrashraf18/" target="_blank" 
                   style="color: #0077b5; text-decoration: none; font-weight: 600;">
                   Visit Profile →
                </a>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="contact-card">
            <h3 style="color: #333; margin-bottom: 15px;">🐙 GitHub</h3>
            <p>
                <a href="https://github.com/TendoPain18" target="_blank" 
                   style="color: #333; text-decoration: none; font-weight: 600;">
                   Visit GitHub →
                </a>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="contact-card">
            <h3 style="color: #25d366; margin-bottom: 15px;">📱 Phone</h3>
            <p style="font-size: 1.1em; color: #2d3748;">
                <strong>+201019702121</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="contact-card">
            <h3 style="color: #667eea; margin-bottom: 15px;">💬 Say Hello!</h3>
            <p style="color: #666;">
                Don't hesitate to reach out for collaborations or opportunities.
            </p>
        </div>
        """, unsafe_allow_html=True)
