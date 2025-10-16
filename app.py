import streamlit as st

st.set_page_config(page_title="Amr Ashraf | Portfolio", layout="wide")

# Custom CSS for enhanced styling
st.markdown("""
<style>
    /* Global Styles */
    .header-nav {
        display: flex;
        justify-content: center;
        gap: 30px;
        padding: 20px 0;
        border-bottom: 3px solid #667eea;
        margin-bottom: 40px;
        flex-wrap: wrap;
    }
    
    .nav-link {
        text-decoration: none;
        font-size: 1.1em;
        font-weight: 600;
        color: #2d3748;
        padding: 10px 20px;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .nav-link:hover {
        color: #667eea;
        background: #f0f0f0;
    }
    
    .nav-link.active {
        color: white;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Main container */
    .main {
        background: linear-gradient(180deg, #f8f9fa 0%, #ffffff 100%);
    }
    
    /* Project card styling */
    .project-card {
        transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
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
    
    h3 {
        color: #2d3748;
        font-weight: 600;
    }
    
    /* Button styling */
    .stLinkButton > button {
        border-radius: 10px;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
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
    
    /* Experience item */
    .experience-item {
        background: #f9fafb;
        border-left: 4px solid #667eea;
        padding: 20px;
        margin: 20px 0;
        border-radius: 8px;
    }
    
    /* Skill tags */
    .skill-tag {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        margin: 5px;
        font-weight: 500;
    }
    
</style>
""", unsafe_allow_html=True)

# Navigation
st.markdown("""
<div style="text-align: center; margin-bottom: 30px;">
    <h1 style="margin-bottom: 5px;">Amr Ashraf</h1>
    <p style="color: #667eea; font-size: 1.1em; font-weight: 500;">Data Scientist | ML Engineer | Full-Stack Developer</p>
</div>
""", unsafe_allow_html=True)

# Horizontal Navigation
page = st.selectbox(
    "Navigation",
    ["🏠 Home", "👤 About Me", "🎯 Projects", "📞 Contact"],
    label_visibility="collapsed"
)

st.markdown("---")

# HOME PAGE
if page == "🏠 Home":
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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            color: white;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        ">
            <h3>📍 Cairo, Egypt</h3>
            <p>📧 amr.gadalla01@gmail.com</p>
            <p>📱 +201019702121</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("⚡ Highlights")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🤖 Projects", "12+")
    with col2:
        st.metric("🏆 Awards", "VEX World Championship")
    with col3:
        st.metric("📚 GPA", "3.40")
    with col4:
        st.metric("🌍 Competitions", "2024-2025")
    
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
elif page == "👤 About Me":
    st.title("About Me 👤")
    
    st.subheader("📚 Education")
    st.markdown("""
    <div class="experience-item">
        <h3>University of Science and Technology at Zewail City</h3>
        <p><strong>Bachelor of Communications and Information Engineering (CIE)</strong></p>
        <p>🎓 Cumulative GPA: 3.40 | Giza, Egypt | 09/2021 – 06/2026</p>
        <p style="color: #666;">ABET Accredited program with focus on ML, signal processing, and embedded systems</p>
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
            <span class="skill-tag">Time Series Forecasting</span>
            <span class="skill-tag">SARIMA/ARIMA</span>
            <span class="skill-tag">Deep Learning</span>
            <span class="skill-tag">CNNs & RNNs</span>
            <span class="skill-tag">Feature Engineering</span>
            <span class="skill-tag">Data Preprocessing</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("**Tools & Platforms**")
        st.markdown("""
        <div>
            <span class="skill-tag">Git & GitHub</span>
            <span class="skill-tag">TensorFlow</span>
            <span class="skill-tag">PyTorch</span>
            <span class="skill-tag">Firebase</span>
            <span class="skill-tag">LabVIEW</span>
            <span class="skill-tag">Cisco Packet Tracer</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Frameworks & Libraries**")
        st.markdown("""
        <div>
            <span class="skill-tag">Pandas</span>
            <span class="skill-tag">Scikit-learn</span>
            <span class="skill-tag">Matplotlib</span>
            <span class="skill-tag">Plotly</span>
            <span class="skill-tag">Keras</span>
            <span class="skill-tag">KiCad</span>
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
elif page == "🎯 Projects":
    st.title("🎯 Projects")
    st.write("Explore my latest projects and technical work")
    st.markdown("---")
    
    # Internet Traffic Forecasting
    st.subheader("📊 Internet Traffic Forecasting")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        **Time Series Modeling for Network Load Prediction**
        
        Time series forecasting project using advanced statistical methods to predict network traffic patterns.
        """)
        st.write("""
        **Key Highlights:**
        - Preprocessed time series data using STL decomposition and outlier handling
        - Built forecasting models: HW-ETS, SARIMA, ARIMA-based ensemble
        - Achieved best performance with HW-ETS (NRMSE: 10.07%)
        """)
    with col2:
        st.info("📅 04/2025 – 05/2025")
    
    st.markdown("---")
    
    # Smart Security System
    st.subheader("🔒 Smart Security System")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        **Tiva C + ESP32 with FreeRTOS, Firebase, and Computer Vision**
        
        IoT-based security system with real-time alerts and intelligent threat detection.
        """)
        st.write("""
        **Key Highlights:**
        - Developed FreeRTOS-based system with custom hardware-level APIs
        - Motion and sound detection with real-time Firebase alerts
        - Computer vision for face detection and human counting
        - Automatic photo logging to Google Drive
        """)
    with col2:
        st.info("📅 04/2025")
    
    st.markdown("---")
    
    # Digital Wireless Communication System
    st.subheader("📡 Digital Wireless Communication System")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        **End-to-End USRP-Based Communication Using LabVIEW**
        
        Full digital communication system implementation with over-the-air transmission.
        """)
        st.write("""
        **Key Highlights:**
        - Built with LabVIEW and USRP hardware
        - Encoded messages (text, voice, video) using divide-and-conquer algorithms
        - QPSK modulation for data transmission
        - Real-time encoding/decoding capabilities
        """)
    with col2:
        st.info("📅 12/2024 – 01/2025")
    
    st.markdown("---")
    
    # Digital Circuits Design
    st.subheader("🔧 Digital Circuits Design Projects")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        **ALU, SAP-1 Simulation, and Pipelined ARM Processor**
        
        Low-level digital design projects from basic arithmetic to advanced processor architecture.
        """)
        st.write("""
        **Key Highlights:**
        - Designed 4-bit ALU in Logisim with 3-bit selector lines
        - Implemented ALU in SystemVerilog
        - Simulated SAP-1 architecture with fetch-decode-execute visualization
        - Built pipelined ARM processor handling RAW, LDR, and control hazards
        """)
    with col2:
        st.info("📅 11/2024 – 12/2024")
    
    st.markdown("---")
    
    # Neural Network for Tumor Detection
    st.subheader("🧠 Neural Network for Tumor Detection")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        **Breast Cancer Detection with Neural Networks**
        
        ML application for medical imaging analysis using microwave sensor data.
        """)
        st.write("""
        **Key Highlights:**
        - Developed neural network model for tumor classification
        - Utilized microwave sensor data for non-invasive detection
        - Benchmarked against PyCaret's automated ML tools
        - High accuracy classification performance
        """)
    with col2:
        st.info("📅 11/2024")
    
    st.markdown("---")
    
    # Hotel Network System
    st.subheader("🏨 Hotel Network System")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        **Multi-VLAN Enterprise Network Design in Cisco Packet Tracer**
        
        Complex enterprise network design with departmental segregation and routing.
        """)
        st.write("""
        **Key Highlights:**
        - Multi-floor hotel network with IP subnetting
        - VLAN configuration for department isolation
        - DHCP and OSPF routing implementation
        - Internal DNS and web servers with access controls
        """)
    with col2:
        st.info("📅 03/2024 – 04/2024")
    
    st.markdown("---")
    
    # UWB Antenna Design
    st.subheader("📶 UWB Microstrip Antenna Design")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        **Compact Ultra-Wideband Antenna for 5G and WLAN**
        
        Antenna design and optimization for next-generation wireless communications.
        """)
        st.write("""
        **Key Highlights:**
        - Designed UWB antenna (3.28–6.38 GHz) using CST Studio Suite
        - Performance tuning through DGS and slot modifications
        - Optimized S-parameters and Farfield patterns
        - Collaboration with original research paper authors
        """)
    with col2:
        st.info("📅 03/2024 – 04/2024")
    
    st.markdown("---")
    
    # Charity Website
    st.subheader("💻 Charity Website and Database System")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        **Web Application for Charitable Organization Management**
        
        Full-stack web application for managing donations and beneficiaries.
        """)
        st.write("""
        **Key Highlights:**
        - Built responsive UI with HTML5, CSS3, Bootstrap, and JavaScript
        - CRUD operations for donations, beneficiaries, and volunteers
        - User-friendly admin dashboard
        - Focus on accessibility and usability
        """)
    with col2:
        st.info("📅 02/2023 – 04/2023")

# CONTACT PAGE
elif page == "📞 Contact":
    st.title("📬 Get in Touch")
    st.write("Let's connect! Feel free to reach out through any of these channels.")
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
            <h3 style="color: #667eea; margin-bottom: 15px;">📍 Location</h3>
            <p style="color: #2d3748; font-size: 1.05em;">
                <strong>Cairo, Egypt</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("💬 Let's Work Together")
    st.write("""
    I'm always interested in learning about new projects and opportunities. 
    Whether you have a question or just want to say hello, feel free to reach out!
    
    I typically respond within 24 hours. Looking forward to connecting with you! 🚀
    """)
