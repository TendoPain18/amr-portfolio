import streamlit as st

st.set_page_config(page_title="Amr Ashraf | Portfolio", layout="wide")

# Custom CSS for enhanced styling
st.markdown("""
<style>
    /* Fixed Header */
    header {
        background: #1a1a2e !important;
        border-bottom: 3px solid #16c784 !important;
        position: sticky;
        top: 0;
        z-index: 1000;
    }
    
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 40px;
        background: #1a1a2e;
        border-bottom: 3px solid #16c784;
        position: sticky;
        top: 0;
        z-index: 1000;
    }
    
    .header-title {
        font-size: 1.8em;
        font-weight: 700;
        color: #16c784;
        margin: 0;
    }
    
    .nav-buttons {
        display: flex;
        gap: 15px;
        flex-wrap: wrap;
    }
    
    .nav-btn {
        padding: 10px 25px;
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
    
    /* Main content with footer padding */
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
    
    /* Streamlit text */
    .stMarkdown {
        color: #e0e0e0 !important;
    }
    
    .stWrite {
        color: #e0e0e0 !important;
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
    
    /* Project cards */
    .project-card {
        background: #16213e;
        border: 2px solid #16c784;
        padding: 20px;
        margin: 20px 0;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        background: #0f3460;
        border-color: #16c784;
        box-shadow: 0 0 20px rgba(22, 199, 132, 0.3);
    }
    
    .project-card h3 {
        margin-top: 0;
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
    
    /* Metric styling */
    .metric-box {
        background: #16213e;
        border: 2px solid #16c784;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
        color: #16c784;
        font-weight: 600;
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
</style>
""", unsafe_allow_html=True)

# Initialize session state for current page
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# Fixed Header with Navigation Buttons
st.markdown("""
<div class="header-container">
    <div class="header-title">Amr Ashraf</div>
</div>
""", unsafe_allow_html=True)

# Navigation buttons
col1, col2, col3, col4 = st.columns(4)

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
    st.write("Explore my latest projects and technical work")
    st.markdown("---")
    
    # Internet Traffic Forecasting
    st.subheader("📊 Internet Traffic Forecasting")
    st.markdown("""
    <div class="project-card">
        <h3>Time Series Modeling for Network Load Prediction</h3>
        <p>Time series forecasting project using advanced statistical methods to predict network traffic patterns.</p>
        <p><strong>Key Highlights:</strong></p>
        <p>• Preprocessed time series data using STL decomposition and outlier handling</p>
        <p>• Built forecasting models: HW-ETS, SARIMA, ARIMA-based ensemble</p>
        <p>• Achieved best performance with HW-ETS (NRMSE: 10.07%)</p>
        <p style="color: #999;"><strong>📅 04/2025 – 05/2025</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Smart Security System
    st.subheader("🔒 Smart Security System")
    st.markdown("""
    <div class="project-card">
        <h3>Tiva C + ESP32 with FreeRTOS, Firebase, and Computer Vision</h3>
        <p>IoT-based security system with real-time alerts and intelligent threat detection.</p>
        <p><strong>Key Highlights:</strong></p>
        <p>• Developed FreeRTOS-based system with custom hardware-level APIs</p>
        <p>• Motion and sound detection with real-time Firebase alerts</p>
        <p>• Computer vision for face detection and human counting</p>
        <p>• Automatic photo logging to Google Drive</p>
        <p style="color: #999;"><strong>📅 04/2025</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Digital Wireless Communication System
    st.subheader("📡 Digital Wireless Communication System")
    st.markdown("""
    <div class="project-card">
        <h3>End-to-End USRP-Based Communication Using LabVIEW</h3>
        <p>Full digital communication system implementation with over-the-air transmission.</p>
        <p><strong>Key Highlights:</strong></p>
        <p>• Built with LabVIEW and USRP hardware</p>
        <p>• Encoded messages (text, voice, video) using divide-and-conquer algorithms</p>
        <p>• QPSK modulation for data transmission</p>
        <p>• Real-time encoding/decoding capabilities</p>
        <p style="color: #999;"><strong>📅 12/2024 – 01/2025</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Digital Circuits Design
    st.subheader("🔧 Digital Circuits Design Projects")
    st.markdown("""
    <div class="project-card">
        <h3>ALU, SAP-1 Simulation, and Pipelined ARM Processor</h3>
        <p>Low-level digital design projects from basic arithmetic to advanced processor architecture.</p>
        <p><strong>Key Highlights:</strong></p>
        <p>• Designed 4-bit ALU in Logisim with 3-bit selector lines</p>
        <p>• Implemented ALU in SystemVerilog</p>
        <p>• Simulated SAP-1 architecture with fetch-decode-execute visualization</p>
        <p>• Built pipelined ARM processor handling RAW, LDR, and control hazards</p>
        <p style="color: #999;"><strong>📅 11/2024 – 12/2024</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Neural Network for Tumor Detection
    st.subheader("🧠 Neural Network for Tumor Detection")
    st.markdown("""
    <div class="project-card">
        <h3>Breast Cancer Detection with Neural Networks</h3>
        <p>ML application for medical imaging analysis using microwave sensor data.</p>
        <p><strong>Key Highlights:</strong></p>
        <p>• Developed neural network model for tumor classification</p>
        <p>• Utilized microwave sensor data for non-invasive detection</p>
        <p>• Benchmarked against PyCaret's automated ML tools</p>
        <p>• High accuracy classification performance</p>
        <p style="color: #999;"><strong>📅 11/2024</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Hotel Network System
    st.subheader("🏨 Hotel Network System")
    st.markdown("""
    <div class="project-card">
        <h3>Multi-VLAN Enterprise Network Design in Cisco Packet Tracer</h3>
        <p>Complex enterprise network design with departmental segregation and routing.</p>
        <p><strong>Key Highlights:</strong></p>
        <p>• Multi-floor hotel network with IP subnetting</p>
        <p>• VLAN configuration for department isolation</p>
        <p>• DHCP and OSPF routing implementation</p>
        <p>• Internal DNS and web servers with access controls</p>
        <p style="color: #999;"><strong>📅 03/2024 – 04/2024</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # UWB Antenna Design
    st.subheader("📶 UWB Microstrip Antenna Design")
    st.markdown("""
    <div class="project-card">
        <h3>Compact Ultra-Wideband Antenna for 5G and WLAN</h3>
        <p>Antenna design and optimization for next-generation wireless communications.</p>
        <p><strong>Key Highlights:</strong></p>
        <p>• Designed UWB antenna (3.28–6.38 GHz) using CST Studio Suite</p>
        <p>• Performance tuning through DGS and slot modifications</p>
        <p>• Optimized S-parameters and Farfield patterns</p>
        <p>• Collaboration with original research paper authors</p>
        <p style="color: #999;"><strong>📅 03/2024 – 04/2024</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Charity Website
    st.subheader("💻 Charity Website and Database System")
    st.markdown("""
    <div class="project-card">
        <h3>Web Application for Charitable Organization Management</h3>
        <p>Full-stack web application for managing donations and beneficiaries.</p>
        <p><strong>Key Highlights:</strong></p>
        <p>• Built responsive UI with HTML5, CSS3, Bootstrap, and JavaScript</p>
        <p>• CRUD operations for donations, beneficiaries, and volunteers</p>
        <p>• User-friendly admin dashboard</p>
        <p>• Focus on accessibility and usability</p>
        <p style="color: #999;"><strong>📅 02/2023 – 04/2023</strong></p>
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
