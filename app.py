import streamlit as st

st.set_page_config(page_title="Amr Ashraf | Portfolio", layout="wide")

# Custom CSS for enhanced styling
st.markdown("""
<style>
    /* Hide default header */
    [data-testid="stDecoration"] {
        display: none;
    }
    
    /* Navigation in top bar */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0;
        margin: 0;
    }
    
    .nav-title {
        font-size: 1.8em;
        font-weight: 700;
        color: #16c784;
    }
    
    .nav-buttons {
        display: flex;
        gap: 15px;
    }
    
    .nav-btn {
        padding: 8px 20px;
        border: 2px solid #16c784;
        background: transparent;
        color: #16c784;
        font-weight: 600;
        border-radius: 5px;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        font-size: 0.95em;
    }
    
    .nav-btn:hover {
        background: #16c784;
        color: #1a1a2e;
    }
    
    .nav-btn.active {
        background: #16c784;
        color: #1a1a2e;
    }
    
    /* Main content */
    .main {
        background: #0f0f1e;
        color: #e0e0e0;
        padding-bottom: 100px;
    }
    
    /* General text */
    body, p, div, span {
        color: #e0e0e0 !important;
    }
    
    h1 {
        color: #16c784 !important;
        font-size: 2.8em;
        font-weight: 700;
        margin-bottom: 15px;
    }
    
    h2 {
        color: #16c784 !important;
        font-weight: 600;
    }
    
    h3 {
        color: #16c784 !important;
        font-weight: 600;
    }
    
    /* Divider */
    hr {
        border: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, #16c784, transparent);
        margin: 2rem 0;
    }
    
    /* Experience item */
    .experience-item {
        background: #16213e;
        border-left: 4px solid #16c784;
        padding: 20px;
        margin: 20px 0;
        border-radius: 8px;
        color: #e0e0e0;
    }
    
    .experience-item h3 {
        color: #16c784 !important;
        margin-top: 0;
    }
    
    .experience-item p {
        color: #c0c0c0;
        margin: 8px 0;
    }
    
    /* Skill tags */
    .skill-tag {
        display: inline-block;
        background: #16c784;
        color: #1a1a2e;
        padding: 8px 16px;
        border-radius: 5px;
        margin: 5px;
        font-weight: 600;
        font-size: 0.9em;
    }
    
    /* Project Category Card */
    .project-category {
        background: #16213e;
        border: 2px solid #16c784;
        border-radius: 12px;
        padding: 20px;
        transition: all 0.3s ease;
        cursor: pointer;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    
    .project-category:hover {
        background: #0f3460;
        box-shadow: 0 0 30px rgba(22, 199, 132, 0.4);
        transform: translateY(-5px);
    }
    
    .category-title {
        color: #16c784 !important;
        font-size: 1.3em;
        font-weight: 600;
        margin: 0 0 15px 0;
        text-align: center;
    }
    
    .image-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
    }
    
    .grid-image {
        width: 100%;
        aspect-ratio: 1;
        background: #0f0f1e;
        border: 2px dashed #16c784;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #16c784;
        font-size: 2em;
    }
    
    /* Contact cards */
    .contact-card {
        background: #16213e;
        border: 2px solid #16c784;
        border-radius: 8px;
        padding: 30px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .contact-card:hover {
        background: #0f3460;
        box-shadow: 0 0 20px rgba(22, 199, 132, 0.3);
        transform: translateY(-5px);
    }
    
    .contact-card h3 {
        color: #16c784 !important;
        margin-bottom: 15px;
    }
    
    .contact-card p {
        color: #c0c0c0;
    }
    
    .contact-card a {
        color: #16c784 !important;
        text-decoration: none;
        font-weight: 600;
    }
    
    .contact-card a:hover {
        text-decoration: underline;
    }
    
    /* Info boxes */
    .stInfo {
        background-color: #16213e !important;
        border-color: #16c784 !important;
    }
    
    /* Button styling */
    .stLinkButton > button {
        background: #16c784 !important;
        color: #1a1a2e !important;
        border: none !important;
        font-weight: 600 !important;
        border-radius: 5px !important;
    }
    
    .stLinkButton > button:hover {
        background: #11a063 !important;
    }
    
    /* Fixed Footer */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #1a1a2e;
        border-top: 3px solid #16c784;
        padding: 20px 40px;
        text-align: center;
        color: #16c784;
        font-weight: 600;
        z-index: 999;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for current page
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# Navigation using columns
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 2])

with col1:
    if st.button("🏠 Home", use_container_width=True, key="btn_home"):
        st.session_state.current_page = "Home"

with col2:
    if st.button("👤 About Me", use_container_width=True, key="btn_about"):
        st.session_state.current_page = "About"

with col3:
    if st.button("🎯 Projects", use_container_width=True, key="btn_projects"):
        st.session_state.current_page = "Projects"

with col4:
    if st.button("📞 Contact", use_container_width=True, key="btn_contact"):
        st.session_state.current_page = "Contact"

with col5:
    st.markdown("<div style='text-align: right; padding-top: 8px; color: #16c784; font-weight: 600;'>Amr Ashraf</div>", unsafe_allow_html=True)

st.markdown("---")

# HOME PAGE
if st.session_state.current_page == "Home":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("Welcome! 👋")
        st.write("""
        I'm Amr Ashraf, a Senior Communications & Information Engineering student at Zewail City of Science and Technology.
        
        I'm passionate about **Machine Learning**, **Embedded Systems**, **Robotics**, and **Full-Stack Development**.
        With hands-on experience in building intelligent systems and end-to-end solutions, I transform complex problems 
        into innovative technological solutions.
        
        Recently awarded the **VEX U World Championship Judges Award** for outstanding engineering and innovation! 🏆
        """)
    
    with col2:
        st.markdown("""
        <div style="
            background: #16213e;
            border: 2px solid #16c784;
            border-radius: 8px;
            padding: 25px;
            text-align: center;
            color: #16c784;
        ">
            <h3 style="margin-top: 0;">📍 Cairo, Egypt</h3>
            <p style="color: #c0c0c0; margin: 10px 0;">📧 amr.gadalla01@gmail.com</p>
            <p style="color: #c0c0c0; margin: 10px 0;">📱 +201019702121</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("⚡ Highlights")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🤖 Projects", "12+", "Completed")
    with col2:
        st.metric("🏆 Awards", "1", "VEX World")
    with col3:
        st.metric("📚 GPA", "3.40", "ABET")
    with col4:
        st.metric("🌍 Competitions", "2", "2024-2025")
    
    st.markdown("---")
    
    st.subheader("🎯 Quick Links")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("📂 View My Projects", "#", use_container_width=True)
    with col2:
        st.link_button("👤 Learn More About Me", "#", use_container_width=True)
    with col3:
        st.link_button("📧 Get in Touch", "#", use_container_width=True)

# ABOUT ME PAGE
elif st.session_state.current_page == "About":
    st.title("About Me 👤")
    
    st.subheader("📚 Education")
    st.markdown("""
    <div class="experience-item">
        <h3>University of Science and Technology at Zewail City</h3>
        <p><strong>Bachelor of Communications and Information Engineering (CIE)</strong></p>
        <p>🎓 Cumulative GPA: 3.40 | Giza, Egypt | 09/2021 – 06/2026</p>
        <p style="color: #999;">ABET Accredited program with focus on ML, signal processing, and embedded systems</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("💼 Professional Experience")
    
    st.markdown("""
    <div class="experience-item">
        <h3>🏆 VEX U World Championship Participant</h3>
        <p><strong>Aquila ZC Robotics Team – Dallas, Texas, USA</strong></p>
        <p>📅 04/2025 – 05/2025</p>
        <p>• Designed optimized robot chassis for stability and modularity</p>
        <p>• Programmed VEX V5 Brain using C++ and PROS (manual control & autonomous navigation)</p>
        <p>• Developed autonomous routines for map navigation and obstacle handling</p>
        <p>• Authored detailed engineering notebook documenting design and improvements</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="experience-item">
        <h3>🤖 Minesweeper Robotics Competition Participant</h3>
        <p><strong>Ministry of Higher Education and Scientific Research</strong></p>
        <p>📅 10/2024 – 12/2024</p>
        <p>• Designed two PCB circuits using KiCad 8 for control and power management</p>
        <p>• Developed sensor fusion system integrating metal detection, GPR, and computer vision</p>
        <p>• Optimized for track width, current handling, and EMI mitigation</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="experience-item">
        <h3>🎤 AI Arabic Keyword Detection Model Internship</h3>
        <p><strong>University of Science and Technology at Zewail City</strong></p>
        <p>📅 06/2024 – 08/2024</p>
        <p>• Collected Arabic keyword dataset from YouTube videos using automated Python scripts</p>
        <p>• Applied audio preprocessing for voice sample cleaning</p>
        <p>• Achieved 92% accuracy on keyword detection evaluation set</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("🛠️ Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Programming Languages**")
        st.markdown("""
        <div>
            <span class="skill-tag">Python</span>
            <span class="skill-tag">C++</span>
            <span class="skill-tag">C#</span>
            <span class="skill-tag">MATLAB</span>
            <span class="skill-tag">SQL</span>
            <span class="skill-tag">JavaScript</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Data Science & ML**")
        st.markdown("""
        <div>
            <span class="skill-tag">Time Series</span>
            <span class="skill-tag">SARIMA</span>
            <span class="skill-tag">Deep Learning</span>
            <span class="skill-tag">CNNs</span>
            <span class="skill-tag">RNNs</span>
            <span class="skill-tag">Feature Eng.</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("**Tools & Platforms**")
        st.markdown("""
        <div>
            <span class="skill-tag">Git</span>
            <span class="skill-tag">TensorFlow</span>
            <span class="skill-tag">PyTorch</span>
            <span class="skill-tag">Firebase</span>
            <span class="skill-tag">LabVIEW</span>
            <span class="skill-tag">KiCad</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Frameworks**")
        st.markdown("""
        <div>
            <span class="skill-tag">Pandas</span>
            <span class="skill-tag">Scikit-learn</span>
            <span class="skill-tag">Matplotlib</span>
            <span class="skill-tag">Plotly</span>
            <span class="skill-tag">Keras</span>
            <span class="skill-tag">Linux</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("🏆 Awards & Recognition")
    st.markdown("""
    <div class="experience-item">
        <h3>🥇 VEX U World Championship Judges Award</h3>
        <p><strong>REC Foundation | 11/05/2025</strong></p>
        <p>Awarded for outstanding engineering documentation, innovation, and team professionalism 
        among over 2,400 teams from 50+ countries.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("🌐 Languages")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("🇸🇦 **Arabic** - Native")
    with col2:
        st.write("🇬🇧 **English** - Fluent")
    with col3:
        st.write("🇩🇪 **German** - Basic")

# PROJECTS PAGE
elif st.session_state.current_page == "Projects":
    st.title("🎯 Projects")
    st.write("Click on any category to explore projects")
    st.markdown("---")
    
    # Project Categories with 2x3 Grid
    col1, col2, col3 = st.columns(3)
    
    # Games Projects
    with col1:
        st.markdown("""
        <div class="project-category">
            <h3 class="category-title">🎮 Games Projects</h3>
            <div class="image-grid">
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # ML Projects
    with col2:
        st.markdown("""
        <div class="project-category">
            <h3 class="category-title">🤖 ML Projects</h3>
            <div class="image-grid">
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # DL Projects
    with col3:
        st.markdown("""
        <div class="project-category">
            <h3 class="category-title">🧠 DL Projects</h3>
            <div class="image-grid">
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("")
    col1, col2, col3 = st.columns(3)
    
    # Robotics Projects
    with col1:
        st.markdown("""
        <div class="project-category">
            <h3 class="category-title">🤖 Robotics Projects</h3>
            <div class="image-grid">
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # DSP Projects
    with col2:
        st.markdown("""
        <div class="project-category">
            <h3 class="category-title">📊 DSP Projects</h3>
            <div class="image-grid">
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Fabrication Projects
    with col3:
        st.markdown("""
        <div class="project-category">
            <h3 class="category-title">🔧 Fabrication Projects</h3>
            <div class="image-grid">
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("")
    col1, col2, col3 = st.columns(3)
    
    # Web Development Projects
    with col1:
        st.markdown("""
        <div class="project-category">
            <h3 class="category-title">💻 Web Development</h3>
            <div class="image-grid">
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Embedded Systems
    with col2:
        st.markdown("""
        <div class="project-category">
            <h3 class="category-title">⚙️ Embedded Systems</h3>
            <div class="image-grid">
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Network & Communication
    with col3:
        st.markdown("""
        <div class="project-category">
            <h3 class="category-title">📡 Networks & Comm</h3>
            <div class="image-grid">
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
                <div class="grid-image">📷</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# CONTACT PAGE
elif st.session_state.current_page == "Contact":
    st.title("📬 Get in Touch")
    st.write("Let's connect! Feel free to reach out through any of these channels.")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="contact-card">
            <h3>📧 Email</h3>
            <p><strong>amr.gadalla01@gmail.com</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="contact-card">
            <h3>💼 LinkedIn</h3>
            <p>
                <a href="https://www.linkedin.com/in/amrashraf18/" target="_blank">
                   Visit Profile →
                </a>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="contact-card">
            <h3>🐙 GitHub</h3>
            <p>
                <a href="https://github.com/TendoPain18" target="_blank">
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
            <h3>📱 Phone</h3>
            <p><strong>+201019702121</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="contact-card">
            <h3>📍 Location</h3>
            <p><strong>Cairo, Egypt</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("💬 Let's Work Together")
    st.write("""
    I'm always interested in learning about new projects and opportunities. 
    Whether you have a question or just want to say hello, feel free to reach out!
    
    I typically respond within 24 hours. Looking forward to connecting with you! 🚀
    """)

# Fixed Footer
st.markdown("""
<div class="footer">
    <p>© 2025 Amr Ashraf | Made with ❤️ | Data Scientist & ML Engineer</p>
</div>
""", unsafe_allow_html=True)
