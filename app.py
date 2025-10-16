import streamlit as st

st.set_page_config(page_title="Amr Ashraf | Portfolio", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for enhanced styling
st.markdown("""
<style>
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
        color: white;
    }
    
    .css-1d391kg {
        color: white;
    }
    
    /* Radio button styling */
    [role="radio"] {
        accent-color: #667eea;
    }
    
    /* Main background */
    .main {
        background: linear-gradient(to bottom, #f8f9fa, #ffffff);
    }
    
    /* Title styling */
    h1, h2, h3 {
        color: #333333;
    }
    
    /* Card hover effect */
    .project-card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)

# Enhanced Sidebar
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: white;'>🧠 Amr Ashraf</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white; font-size: 14px;'>Data Scientist & Developer</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    page = st.radio(
        "Navigation",
        ["🏠 Home", "🎮 Games", "🤖 ML Projects", "📞 Contact"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("<p style='color: white; font-size: 12px; text-align: center;'>© 2025 All Rights Reserved</p>", unsafe_allow_html=True)

# HOME PAGE
if page == "🏠 Home":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("Welcome to My Portfolio 👋")
        st.markdown("""
        ### Hi, I'm **Amr Ashraf**
        
        I'm a passionate **Data Scientist** and **Python Developer** with expertise in:
        - 🧠 **EEG Signal Processing** & Machine Learning
        - 🎮 **Game Development** with Python
        - 📊 **Data Analysis** & Visualization
        - 🤖 **Deep Learning** & Neural Networks
        
        Explore my projects and feel free to reach out! 
        """)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            color: white;
        ">
            <h3>📊 Quick Stats</h3>
            <p><b>2</b> Game Projects</p>
            <p><b>∞</b> Learning</p>
            <p><b>100%</b> Passion</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("Featured Projects")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
            padding: 20px;
            color: white;
        ">
            <h3>💰 Millionaire Quiz Game</h3>
            <p>Interactive Tkinter game with audio and graphics</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("View Project", "https://github.com/TendoPain18/millionaire-game", use_container_width=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            border-radius: 10px;
            padding: 20px;
            color: white;
        ">
            <h3>🧠 EEG Classifier</h3>
            <p>Motor imagery classification with ML</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("View Project", "https://github.com/TendoPain18", use_container_width=True)

# GAMES PAGE
elif page == "🎮 Games":
    st.title("🎮 Game Projects")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            padding: 40px 20px;
            text-align: center;
            min-height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
        ">
            <h2>💰</h2>
            <h3>Who Wants to Be a Millionaire</h3>
            <p>Interactive Tkinter Quiz Game</p>
            <p style="font-size: 12px; margin-top: 15px;">🎯 Fully Featured Game with Audio & Images</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.link_button("📂 View Code on GitHub", "https://github.com/TendoPain18/millionaire-game", use_container_width=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            border-radius: 15px;
            padding: 40px 20px;
            text-align: center;
            min-height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        ">
            <h2>🎯</h2>
            <h3>Game 2</h3>
            <p>Coming Soon</p>
            <p style="font-size: 12px; margin-top: 15px;">🚀 Exciting project in development</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("Stay tuned for more games!", icon="⏳")
    
    with col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            border-radius: 15px;
            padding: 40px 20px;
            text-align: center;
            min-height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        ">
            <h2>🎨</h2>
            <h3>Game 3</h3>
            <p>Coming Soon</p>
            <p style="font-size: 12px; margin-top: 15px;">🚀 Next big project</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("More games coming soon!", icon="⏳")

# ML PROJECTS PAGE
elif page == "🤖 ML Projects":
    st.title("🤖 Machine Learning Projects")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            border-radius: 15px;
            padding: 40px 20px;
            text-align: center;
            min-height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        ">
            <h2>🧠</h2>
            <h3>EEG Classifier</h3>
            <p>Motor Imagery Classification</p>
            <p style="font-size: 12px; margin-top: 15px;">CNN & Feature-based Models</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.link_button("📂 View Code", "https://github.com/TendoPain18", use_container_width=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #30cfd0 0%, #330867 100%);
            border-radius: 15px;
            padding: 40px 20px;
            text-align: center;
            min-height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        ">
            <h2>📊</h2>
            <h3>Project 2</h3>
            <p>Coming Soon</p>
            <p style="font-size: 12px; margin-top: 15px;">Next ML project</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("Coming soon...", icon="⏳")
    
    with col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            border-radius: 15px;
            padding: 40px 20px;
            text-align: center;
            min-height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        ">
            <h2>🤖</h2>
            <h3>Project 3</h3>
            <p>Coming Soon</p>
            <p style="font-size: 12px; margin-top: 15px;">Future project</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("More projects coming!", icon="⏳")

# CONTACT PAGE
elif page == "📞 Contact":
    st.title("📬 Get in Touch")
    st.markdown("---")
    
    st.markdown("Feel free to reach out to me through any of these channels:")
    st.markdown("")
    
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        ">
            <h3>📧 Email</h3>
            <p style="word-break: break-all;"><b>amr.gadalla01@gmail.com</b></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        ">
            <h3>📱 Phone</h3>
            <p><b>+201019702121</b></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        ">
            <h3>💼 LinkedIn</h3>
            <p><a href="https://www.linkedin.com/in/amrashraf18/" target="_blank" style="color: white; text-decoration: underline;"><b>View Profile</b></a></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.link_button("🐙 GitHub Profile", "https://github.com/TendoPain18", use_container_width=True)
    
    with col2:
        st.link_button("📧 Send Email", "mailto:amr.gadalla01@gmail.com", use_container_width=True)
