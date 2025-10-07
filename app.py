import streamlit as st

# Page config
st.set_page_config(
    page_title="NASC Labor Planning Assistant",
    page_icon="📊",
    layout="wide"
)

# Remove any default messages and set custom title
st.title("NASC Sort Center Labor Planning Assistant")

# Create two columns for layout
col1, col2 = st.columns([2,1])

with col1:
    # Main content area
    st.markdown("### Plan Your Labor Strategy")
    
    # Scenario selection with more context
    scenario = st.selectbox(
        "What scenario are you planning for?",
        ["Select Scenario", "High Volume", "Low Volume", "Flex Up", "Flex Down"],
        help="Choose a scenario to get specific guidance"
    )
    
    # Volume input (optional)
    volume = st.number_input("Expected Volume (packages):", 
                           min_value=0, 
                           value=50000, 
                           step=1000,
                           help="Enter expected package volume")
    
    # Additional context
    specific_question = st.text_area(
        "Any specific questions or concerns?",
        height=100,
        help="Enter any specific questions about your scenario"
    )
    
    # Get guidance button with styling
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
               - Calculate headcount needs for {volume:,} packages
               - Assess current roster availability
               - Consider labor share options
            
            3. **Required Approvals:**
               - Site leadership sign-off for flex changes
               - Document business justification
            
            4. **Communication Plan:**
               - Notify affected associates
               - Update shift planners
               - Monitor SLA impact
            """)
            
        elif scenario == "Low Volume":
            st.info("""
            #### Low Volume Plan:
            
            1. **Volume Management:**
               - Consider Flex Down to 3-hour shifts
               - Evaluate VTO opportunities
               - Review labor share possibilities
            
            2. **Optimization Steps:**
               - Calculate minimum headcount needed
               - Identify potential VTO candidates
               - Plan cross-training opportunities
            
            3. **Required Actions:**
               - Get site leadership approval
               - Document volume justification
               - Monitor productivity metrics
            """)
            
        elif scenario == "Flex Up":
            st.info("""
            #### Flex Up Implementation:
            
            1. **Guidelines:**
               - Maximum shift duration: 5 hours
               - Minimum notice: 24 hours preferred
               - Required approval: Site leadership
            
            2. **Process Steps:**
               - Document volume forecast
               - Calculate labor gap
               - Submit flex request
               - Communicate to associates
            
            3. **Best Practices:**
               - Consider impact on next shift
               - Monitor associate fatigue
               - Track productivity metrics
            """)
            
        elif scenario == "Flex Down":
            st.info("""
            #### Flex Down Implementation:
            
            1. **Guidelines:**
               - Minimum shift duration: 3 hours
               - Notice: As early as possible
               - Required approval: Site leadership
            
            2. **Key Steps:**
               - Verify volume reduction
               - Calculate optimal headcount
               - Get leadership approval
               - Communicate changes
            
            3. **Important Considerations:**
               - Maintain SLA coverage
               - Fair implementation across teams
               - Document all decisions
            """)
            
        else:
            st.warning("Please select a specific scenario to receive guidance.")

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
    - Labor share: Both sites
    """)
    
    # Key Metrics
    st.success("""
    #### Key Metrics to Monitor
    - Package volume vs plan
    - Labor hours vs volume
    - SLA performance
    - TPH (Throughput per Hour)
    """)
    
    # Additional Resources
    st.markdown("### Additional Resources")
    st.markdown("""
    - [NASC Labor Planning Guide](https://internal-link)
    - [Flex Guidelines](https://internal-link)
    - [VET/VTO Policies](https://internal-link)
    """)

# Footer
st.markdown("---")
st.caption("NASC Labor Planning Assistant v1.1 | Updated Oct 2025")
