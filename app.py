import streamlit as st
import random

# Page config
st.set_page_config(page_title="NASC Labor Planning Assistant", page_icon="📊", layout="wide")

# Title
st.title("NASC Sort Center Labor Planning Assistant")

# Sample Questions Section
with st.expander("🤔 Click to see example questions you can ask"):
    st.markdown("""
    **Volume Planning:**
    - How many people do I need for 50,000 packages?
    - What's the process for handling unexpected high volume?
    - When should I consider flex up vs VET?
    
    **Flex Options:**
    - How much notice do I need for flex up?
    - What approvals do I need for flex down?
    - Can I flex down on the same day?
    
    **Labor Management:**
    - What's the process for posting VET?
    - How do I handle low volume days?
    - When should I consider labor share?
    """)

# Main layout
col1, col2 = st.columns([2,1])

with col1:
    scenario = st.selectbox("What scenario are you planning for?",
                            ["Select Scenario", "High Volume", "Low Volume", "Flex Up", "Flex Down"])
    
    volume = st.number_input("Expected Volume (packages):", min_value=0, value=50000, step=1000)
    
    question = st.text_area("Describe your situation or ask a specific question:",
                            help="Provide details about your scenario or ask specific questions")

    guide_col1, guide_col2 = st.columns(2)
    
    with guide_col1:
        if st.button("Get Standard Guidance"):
            st.markdown("### Standard Guidelines:")
            if scenario == "High Volume":
                st.info("""
                #### High Volume Plan:
                1. Consider Flex Up to 5-hour shifts
                2. Prepare VET postings (24-hour notice required)
                3. Alert site leadership for approvals
                4. Calculate headcount for volume
                5. Assess roster availability
                """)
            elif scenario == "Low Volume":
                st.info("""
                #### Low Volume Plan:
                1. Consider Flex Down to 3-hour shifts
                2. Evaluate VTO opportunities
                3. Get site leadership approval
                4. Document volume justification
                5. Monitor productivity metrics
                """)
            else:
                st.warning("Please select a specific scenario for guidance.")
                
    with guide_col2:
        if st.button("Get AI Guidance"):
            st.markdown("### AI-Generated Guidance:")
            with st.spinner("AI is analyzing your scenario..."):
                ai_responses = [
                    f"For your {scenario.lower()} scenario with {volume} packages, consider the following:",
                    "1. Immediate Action: " + random.choice(["Flex Up staff", "Offer VET", "Implement Flex Down", "Assess labor share options"]),
                    "2. Staffing Recommendation: " + random.choice(["Increase headcount by 10%", "Reduce shifts to 3 hours", "Maintain current staffing", "Cross-train associates"]),
                    "3. Required Approvals: Site leadership sign-off needed for " + random.choice(["flex changes", "VET postings", "VTO offerings", "labor share"]),
                    "4. Key Consideration: " + random.choice(["Monitor SLA impact", "Balance associate satisfaction", "Optimize productivity", "Ensure fair VET/VTO distribution"]),
                    f"5. Next Steps: Review this plan with your team and implement based on the {volume} package volume forecast."
                ]
                st.write("\n\n".join(ai_responses))

with col2:
    st.markdown("### Quick Reference")
    
    st.info("""
    #### Standard Shift Guidelines
    - Base Shift: 4 hours
    - Flex Up Max: 5 hours
    - Flex Down Min: 3 hours
    """)
    
    st.markdown("### 🤖 AI Features (Simulated)")
    st.success("""
    This tool offers:
    - Standard guidance
    - Simulated AI-powered analysis
    - Dynamic recommendations
    - Specific scenario handling
    
    Try both options to compare!
    """)

# Footer
st.markdown("---")
st.caption("NASC Labor Planning Assistant v2.1 (AI-Simulated with Sample Questions)")
