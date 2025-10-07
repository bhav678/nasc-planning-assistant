import streamlit as st
import boto3
from strands import Agent
from strands.models import BedrockModel

# Page config
st.set_page_config(
    page_title="NASC Labor Planning Assistant",
    page_icon="📊",
    layout="wide"
)

# Initialize AI Model
try:
    model = BedrockModel(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",
        temperature=0.7,
        region_name="us-west-2"
    )

    agent = Agent(
        model=model,
        tools=[],  # We'll add tools later
        system_prompt="""You are an AI assistant for NASC (North America Sort Centers) labor planning.
        Provide specific guidance about:
        - Flex Up/Down decisions (3-5 hour shifts)
        - VET/VTO considerations
        - Labor planning for different volumes
        - Required approvals and notifications
        Always consider NASC policies and SLA requirements."""
    )
    ai_initialized = True
except Exception as e:
    ai_initialized = False
    st.warning("AI features are initializing. Some features may be limited.")

# Title
st.title("NASC Sort Center Labor Planning Assistant")

# Create two columns for layout
col1, col2 = st.columns([2,1])

with col1:
    # Scenario selection
    scenario = st.selectbox(
        "What scenario are you planning for?",
        ["Select Scenario", "High Volume", "Low Volume", "Flex Up", "Flex Down"]
    )
    
    # Volume input
    volume = st.number_input("Expected Volume (packages):", 
                           min_value=0, 
                           value=50000, 
                           step=1000)
    
    # Add specific question input
    question = st.text_area(
        "Describe your situation or ask a specific question:",
        help="Provide details about your scenario or ask specific questions"
    )

    # Add two columns for response type selection
    guide_col1, guide_col2 = st.columns(2)
    
    with guide_col1:
        if st.button("Get Standard Guidance"):
            st.markdown("### Standard Guidelines:")
            # Your existing if-else logic for predefined responses
            if scenario == "High Volume":
                st.info("Your existing high volume response...")
                
    with guide_col2:
        if st.button("Get AI Guidance") and ai_initialized:
            st.markdown("### AI-Generated Guidance:")
            with st.spinner("AI is analyzing your scenario..."):
                try:
                    # Construct detailed prompt
                    prompt = f"""
                    Analyze this NASC labor planning scenario:
                    Scenario Type: {scenario}
                    Expected Volume: {volume} packages
                    Specific Question: {question}

                    Provide detailed guidance including:
                    1. Immediate actions needed
                    2. Staffing recommendations
                    3. Required approvals
                    4. Key considerations
                    5. Next steps
                    """
                    
                    response = agent(prompt)
                    st.write(response)
                except Exception as e:
                    st.error(f"AI Error: {str(e)}")

with col2:
    # Quick Reference Panel
    st.markdown("### Quick Reference")
    
    # Standard Guidelines
    st.info("""
    #### Standard Shift Guidelines
    - Base Shift: 4 hours
    - Flex Up Max: 5 hours
    - Flex Down Min: 3 hours
    """)
    
    # New AI Features Section
    st.markdown("### 🤖 AI Features")
    st.success("""
    This tool now offers:
    - Standard guidance
    - AI-powered analysis
    - Dynamic recommendations
    - Specific scenario handling
    
    Try both options to compare!
    """)

# Footer
st.markdown("---")
st.caption("NASC Labor Planning Assistant v2.0 (AI-Enhanced)")
