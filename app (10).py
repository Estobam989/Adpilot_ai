# app.py
import streamlit as st
st.set_page_config(
    page_title="AdPilot AI",
    page_icon="🚀",
    layout="wide"
)
# -----------------------------
# AI CONFIGURATION
# -----------------------------
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    API_KEY = st.text_input(
        "Enter Gemini API Key",
        type="password"
    )
if not API_KEY:
    st.warning("Enter your Gemini API key to start.")
    st.stop()
client = genai.Client(api_key=API_KEY)
# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🚀 AdPilot AI")
menu = st.sidebar.radio(
    "Choose a service",
    [
        "AI Ad Generator",
        "Social Media Post",
        "Content Calendar",
        "Campaign Strategy",
        "Audience Research",
        "Marketing Analytics"
    ]
)
# -----------------------------
# AI FUNCTION
# -----------------------------
def ask_ai(prompt):
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )
    return response.text
# -----------------------------
# AI AD GENERATOR
# -----------------------------
if menu == "AI Ad Generator":
    st.title("🎯 AI Advertisement Generator")
    business = st.text_input(
        "Business / Brand Name"
    )
    product = st.text_area(
        "What are you advertising?"
    )
    audience = st.text_input(
        "Target Audience"
    )
    platform = st.selectbox(
        "Advertising Platform",
        [
            "Facebook",
            "Instagram",
            "TikTok",
            "LinkedIn",
            "WhatsApp"
        ]
    )
    objective = st.selectbox(
        "Campaign Objective",
        [
            "Generate Leads",
            "Get Sales",
            "Build Awareness",
            "Drive Traffic",
            "Promote Investment",
            "Product Launch"
        ]
    )
    if st.button("✨ Generate Advertisement"):
        prompt = f"""
        You are an expert digital advertising strategist.
        Create a high-converting advertisement for:
        Brand: {business}
        Product/Service: {product}
        Target Audience: {audience}
        Platform: {platform}
        Objective: {objective}
        Produce:
        1. Primary advertisement copy
        2. Attention-grabbing headline
        3. Short version
        4. Call-to-action
        5. 5 advertising hooks
        6. 10 relevant hashtags
        7. Suggested creative concept
        8. Suggested audience targeting
        9. A WhatsApp version
        10. A TikTok/Reels version
        Make the advertisement persuasive,
        professional and suitable for the Nigerian market.
        """
        with st.spinner("Creating campaign..."):
            result = ask_ai(prompt)
        st.success("Advertisement generated!")
        st.markdown(result)
# -----------------------------
# SOCIAL MEDIA POST
# -----------------------------
elif menu == "Social Media Post":
    st.title("📱 AI Social Media Manager")
    brand = st.text_input("Brand")
    topic = st.text_area("What should the post be about?")
    platform = st.selectbox(
        "Platform",
        ["Instagram", "Facebook", "TikTok", "LinkedIn", "WhatsApp"]
    )
    tone = st.selectbox(
        "Tone",
        [
            "Professional",
            "Luxury",
            "Friendly",
            "Persuasive",
            "Educational",
            "Bold"
        ]
    )
    if st.button("Generate Post"):
        prompt = f"""
        Act as a professional social media manager.
        Brand: {brand}
        Topic: {topic}
        Platform: {platform}
        Tone: {tone}
        Create:
        - Strong hook
        - Main post
        - CTA
        - Hashtags
        - Short version
        - Engagement question
        """
        with st.spinner("Writing content..."):
            result = ask_ai(prompt)
        st.markdown(result)
# -----------------------------
# CONTENT CALENDAR
# -----------------------------
elif menu == "Content Calendar":
    st.title("📅 AI Content Calendar")
    brand = st.text_input("Brand name")
    industry = st.text_input("Industry")
    days = st.slider(
        "Number of days",
        7,
        30,
        7
    )
    if st.button("Create Content Calendar"):
        prompt = f"""
        Create a {days}-day social media content calendar.
        Brand: {brand}
        Industry: {industry}
        Create columns for:
        Day
        Content Pillar
        Topic
        Hook
        Caption
        CTA
        Platform
        Content Format
        Make the strategy focused on:
        awareness, engagement, leads and sales.
        """
        with st.spinner("Building content calendar..."):
            result = ask_ai(prompt)
        st.markdown(result)
# -----------------------------
# CAMPAIGN STRATEGY
# -----------------------------
elif menu == "Campaign Strategy":
    st.title("📈 AI Campaign Strategist")
    business = st.text_input("Business")
    product = st.text_area("Product / Service")
    budget = st.number_input(
        "Monthly Advertising Budget (₦)",
        min_value=0,
        value=100000
    )
    if st.button("Build Campaign"):
        prompt = f"""
        Act as a senior digital marketing strategist.
        Business: {business}
        Product: {product}
        Monthly budget: ₦{budget}
        Build a complete advertising strategy including:
        1. Campaign objective
        2. Target audience
        3. Customer personas
        4. Campaign funnel
        5. Ad campaign structure
        6. Budget allocation
        7. Creative strategy
        8. Copy strategy
        9. Lead generation strategy
        10. Retargeting strategy
        11. KPIs
        12. 30-day execution plan
        Optimize for the Nigerian market.
        """
        with st.spinner("Developing strategy..."):
            result = ask_ai(prompt)
        st.markdown(result)
# -----------------------------
# AUDIENCE RESEARCH
# -----------------------------
elif menu == "Audience Research":
    st.title("👥 AI Audience Research")
    product = st.text_area(
        "Describe your product or service"
    )
    if st.button("Research Audience"):
        prompt = f"""
        Analyze the target market for:
        {product}
        Identify:
        - Ideal customer
        - Age
        - Location
        - Income level
        - Interests
        - Pain points
        - Buying motivations
        - Objections
        - Customer desires
        - Advertising hooks
        - Content themes
        - Conversion strategy
        """
        with st.spinner("Analyzing audience..."):
            result = ask_ai(prompt)
        st.markdown(result)
# -----------------------------
# ANALYTICS
# -----------------------------
elif menu == "Marketing Analytics":
    st.title("📊 AI Marketing Analyst")
    data = st.text_area(
        "Paste your campaign statistics",
        height=250,
        placeholder="""
        Example:
        Impressions: 25,000
        Reach: 18,000
        Clicks: 1,200
        Leads: 85
        Sales: 12
        Ad Spend: ₦150,000
        """
    )
    if st.button("Analyze Campaign"):
        prompt = f"""
        Act as a digital marketing data analyst.
        Analyze this campaign:
        {data}
        Explain:
        - Campaign performance
        - Conversion rate
        - Lead quality
        - Possible problems
        - What is working
        - What should be changed
        - Budget recommendations
        - Next campaign strategy
        """
        with st.spinner("Analyzing campaign..."):
            result = ask_ai(prompt)
        st.markdown(result)
