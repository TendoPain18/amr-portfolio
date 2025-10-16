import streamlit as st

st.set_page_config(page_title="Amr Ashraf | Portfolio", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "🎮 Games", "🤖 ML Projects", "📞 Contact"])

# HOME
if page == "🏠 Home":
    st.title("Hi, I'm Amr Ashraf 👋")
    st.write("""
    Welcome to my portfolio!  
    I'm a Data Scientist passionate about **Python**, **Machine Learning**, and **Game Development**.  
    Check out my projects below 👇
    """)

# GAMES
elif page == "🎮 Games":
    st.title("🎮 Game Projects")
    st.subheader("💰 Who Wants to Be a Millionaire")
    st.write("A Python Tkinter quiz game with audio, images, and dynamic questions.")
    st.link_button("📂 View Code on GitHub", "https://github.com/YOUR_USERNAME/millionaire-game")

# ML PROJECTS
elif page == "🤖 ML Projects":
    st.title("🤖 Machine Learning Projects")
    st.write("Coming soon...")

# CONTACT
elif page == "📞 Contact":
    st.title("📬 Get in Touch")
    st.write("📧 Email: your-email@example.com")
    st.write("[LinkedIn](https://linkedin.com/in/yourprofile)")
    st.write("[GitHub](https://github.com/YOUR_USERNAME)")
```

**Replace:**
- `YOUR_USERNAME` with your actual GitHub username
- `your-email@example.com` with your real email

---

**File 2: `requirements.txt`**

Just one line:
```
streamlit
