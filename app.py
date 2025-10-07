import streamlit as st

# Page config
st.set_page_config(
    page_title="NASC Labor Planning Assistant",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("NASC Sort Center Labor Planning Assistant")

# Add Sample Questions Section
st.markdown("### 🤔 Sample Questions You Can Ask:")
with st.expander("Click to see example questions"):
    st.markdown("""
    **Volume Planning:**
    - How many people do I need for 50,000 packages?
    - What's the process for handling unexpected high volume?
    - When should I consider flex up vs VET?
    
    **Flex Options:**
    - How much notice do I need for flex up?
    - What approvals do I need for flex down?
    - Can I flex down on the same day?
    """)

# Create two columns for layout
col1, col2 = st.columns([2,1])

with col1:
    # Main content area
    st.markdown("### Plan Your Labor Strategy")
    
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
    
    # Question input
    specific_question = st.text_area(
        "Any specific questions or concerns?",
        height=100
    )
    
    # Get guidance button
    if st.button("Get Planning Guidance", type="primary"):
        st.markdown("### Recommended Actions:")
        
        if scenario == "High Volume":
            st.info("""
            #### High Volume Plan:
            
            1. **Immediate Actions:**
               - Consider Flex Up to 5-hour shifts
               - Prepare VET postings (24-hour notice required)
               - Alert site leadership for approvals
            
            2. **Staffing Considerations:**
               - Calculate headcount for volume
               - Assess roster availability
               - Consider labor share options
            """)
            
        elif scenario == "Low Volume":
            st.info("""
            #### Low Volume Plan:
            
            1. **Volume Management:**
               - Consider Flex Down to 3-hour shifts
               - Evaluate VTO opportunities
               - Review labor share possibilities
            
            2. **Required Actions:**
               - Get site leadership approval
               - Document volume justification
               - Monitor productivity metrics
            """)
            
        elif scenario == "Flex Up":
            st.info("""
            #### Flex Up Guidelines:
            
            1. **Key Rules:**
               - Maximum 5-hour shifts
               - 24-hour notice preferred
               - Site leadership approval required
            
            2. **Process Steps:**
               - Document volume forecast
               - Calculate labor gap
               - Submit flex request
               - Communicate to associates
            """)
            
        elif scenario == "Flex Down":
            st.info("""
            #### Flex Down Guidelines:
            
            1. **Key Rules:**
               - Minimum 3-hour shifts
               - Notice: As early as possible
               - Site leadership approval required
            
            2. **Important Steps:**
               - Verify volume reduction
               - Calculate optimal headcount
               - Get leadership approval
               - Communicate changes
            """)
            
        else:
            st.warning("Please select a scenario to receive guidance.")

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
    
    # Approval Requirements
    st.warning("""
    #### Required Approvals
    - Flex changes: Site leadership
    - VET posting: 24-hour notice
    - VTO offering: Same-day OK
    """)
    
    # Key Metrics
    st.success("""
    #### Key Metrics to Monitor
    - Package volume vs plan
    - Labor hours vs volume
    - SLA performance
    - TPH (Throughput per Hour)
    """)

# Footer
st.markdown("---")
st.caption("NASC Labor Planning Assistant v1.1")
