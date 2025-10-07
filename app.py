import streamlit as st
import random

# Page config
st.set_page_config(page_title="NASC Labor Planning Assistant", page_icon="📊", layout="wide")

# Function to generate contextual AI response
def generate_ai_response(scenario, volume, question):
    # Base responses for different scenarios
    scenario_responses = {
        "High Volume": {
            "actions": [
                "Implement Flex Up to 5-hour shifts immediately",
                "Post VET opportunities with 24-hour notice",
                "Activate labor share from nearby sites",
                "Split shifts to maximize coverage"
            ],
            "staffing": [
                f"Based on {volume} packages, recommend increasing headcount by 20%",
                "Utilize VET to cover additional labor hours",
                "Consider split shifts to maximize coverage",
                "Activate cross-trained associates from other areas"
            ],
            "considerations": [
                "Monitor SLA impact closely",
                "Track productivity metrics hourly",
                "Ensure adequate supervision coverage",
                "Balance labor hours across shifts"
            ]
        },
        "Low Volume": {
            "actions": [
                "Implement Flex Down to 3-hour shifts",
                "Prepare VTO offerings",
                "Consolidate operations areas",
                "Optimize staff allocation"
            ],
            "staffing": [
                f"For {volume} packages, consider reducing headcount by 15%",
                "Offer VTO strategically",
                "Redistribute staff to other areas",
                "Use time for cross-training"
            ],
            "considerations": [
                "Maintain minimum staffing for SLAs",
                "Balance VTO distribution fairly",
                "Keep core operations running efficiently",
                "Use downtime for training"
            ]
        }
    }

    # Generate response based on question content
    response = [f"Analyzing your scenario: {scenario} with {volume} packages"]
    
    if "flex" in question.lower():
        if "High Volume" in scenario:
            response.append("Flex Analysis: Recommend immediate Flex Up to 5 hours with leadership approval")
        else:
            response.append("Flex Analysis: Consider Flex Down to 3 hours after leadership approval")
    
    if "vet" in question.lower() or "vto" in question.lower():
        if "High Volume" in scenario:
            response.append("Labor Planning: Post VET opportunities with 24-hour notice")
        else:
            response.append("Labor Planning: Consider strategic VTO offerings")
    
    if "headcount" in question.lower() or "staff" in question.lower():
        response.append(f"Staffing Analysis: Based on {volume} packages:")
        if "High Volume" in scenario:
            response.append("- Need additional headcount through VET or labor share")
        else:
            response.append("- Current headcount can be optimized through Flex Down")

    # Add scenario-specific responses
    if scenario in scenario_responses:
        response.append("\nRecommended Actions:")
        response.append("- " + random.choice(scenario_responses[scenario]["actions"]))
        response.append("- " + random.choice(scenario_responses[scenario]["staffing"]))
        response.append("\nKey Considerations:")
        response.append("- " + random.choice(scenario_responses[scenario]["considerations"]))
    
    response.append("\nNext Steps:")
    response.append("1. Review this plan with site leadership")
    response.append("2. Document business justification")
    response.append("3. Implement approved changes")
    response.append("4. Monitor metrics and adjust as needed")
    
    return "\n".join(response)

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
    scenario = st.selectbox(
        "What scenario are you planning for?",
        ["Select Scenario", "High Volume", "Low Volume", "Flex Up", "Flex Down"]
    )
    
    volume = st.number_input(
        "Expected Volume (packages):", 
        min_value=0, 
        value=50000, 
        step=1000
    )
    
    question = st.text_area(
        "What specific guidance do you need?",
        placeholder="Example: How should I handle staffing for this volume?"
    )

    if st.button("Get AI Guidance", type="primary"):
        if scenario != "Select Scenario":
            st.markdown("### AI-Generated Guidance:")
            with st.spinner("Analyzing your scenario..."):
                response = generate_ai_response(scenario, volume, question)
                st.write(response)
        else:
            st.warning("Please select a scenario to get guidance.")

with col2:
    st.markdown("### Quick Reference")
    
    st.info("""
    #### Standard Guidelines
    - Base Shift: 4 hours
    - Flex Up Max: 5 hours
    - Flex Down Min: 3 hours
    """)
    
    st.warning("""
    #### Required Approvals
    - Flex changes: Site leadership
    - VET posting: 24-hour notice
    - VTO offering: Same-day OK
    """)
    
    st.success("""
    #### Key Metrics
    - Package volume vs plan
    - Labor hours vs volume
    - SLA performance
    - TPH (Throughput per Hour)
    """)

# Footer
st.markdown("---")
st.caption("NASC Labor Planning Assistant v2.2 (Enhanced AI Simulation)")
