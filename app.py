import streamlit as st

st.set_page_config(page_title="Amr Ashraf | Portfolio", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "🎮 Games", "🤖 ML Projects", "📞 Contact"])

# HOME PAGE
if page == "🏠 Home":
    st.title("Hi, I'm Amr Ashraf 👋")
    st.write("""
    Welcome to my portfolio!  
    I'm a Data Scientist passionate about **Python**, **Machine Learning**, and **Game Development**.  
    Explore my projects below 👇
    """)
    
    st.markdown("---")
    st.subheader("Quick Links")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("🎮 View Games", "#")
    with col2:
        st.link_button("🤖 View ML Projects", "#")
    with col3:
        st.link_button("📧 Contact Me", "#")

# GAMES PAGE
elif page == "🎮 Games":
    st.title("🎮 Game Projects")
    
    # Create 3 columns for game cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        ">
            <h2>💰 Who Wants to Be a Millionaire</h2>
            <p>Interactive Tkinter Quiz Game</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.link_button("🎮 Play Game", "https://YOUR_GAME_LINK.streamlit.app", use_container_width=True)
        st.link_button("📂 View Code", "https://github.com/YOUR_USERNAME/millionaire-game", use_container_width=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        ">
            <h2>🎯 Game 2</h2>
            <p>Coming Soon</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("Coming soon...")
    
    with col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        ">
            <h2>🎨 Game 3</h2>
            <p>Coming Soon</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("Coming soon...")

# ML PROJECTS PAGE
elif page == "🤖 ML Projects":
    st.title("🤖 Machine Learning Projects")
    
    # Create 3 columns for ML project cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        ">
            <h2>🧠 EEG Classifier</h2>
            <p>Motor Imagery Classification</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.link_button("🌐 Live Demo", "https://YOUR_EEG_APP.streamlit.app", use_container_width=True)
        st.link_button("📂 View Code", "https://github.com/YOUR_USERNAME/eeg-classifier", use_container_width=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #30cfd0 0%, #330867 100%);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        ">
            <h2>📊 Project 2</h2>
            <p>Coming Soon</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("Coming soon...")
    
    with col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        ">
            <h2>🤖 Project 3</h2>
            <p>Coming Soon</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("Coming soon...")

# CONTACT PAGE
elif page == "📞 Contact":
    st.title("📬 Get in Touch")
    
    st.write("Feel free to reach out to me on any of these platforms:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="
            background: #f0f0f0;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        ">
            <h3>📧 Email</h3>
            <p>your-email@example.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="
            background: #f0f0f0;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        ">
            <h3>💼 LinkedIn</h3>
            <p><a href="https://linkedin.com/in/yourprofile" target="_blank">Visit Profile</a></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="
            background: #f0f0f0;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        ">
            <h3>🐙 GitHub</h3>
            <p><a href="https://github.com/YOUR_USERNAME" target="_blank">Visit GitHub</a></p>
        </div>
        """, unsafe_allow_html=True)
