#lets us create web applications using python
import streamlit as st

#aesthetics of the application
st.set_page_config(
    page_title="Multi-Domain Intelligence Platform", 
    layout="wide"
)

#main title
st.title("Multi-Domain Intelligence Platform")
#markdown text 
st.markdown("""
### Welcome to your Unified Intelligence Platform!

This platform serves:
- **Cybersecurity Analysts** - Monitor and manage security incidents  
- **IT Administrators** - Track support tickets and system performance

**Use the sidebar to navigate to different dashboards!**
""")

#creates columns
col1, col2 = st.columns(2)  
with col1: 
    st.metric("Security Domain", "Cyber", "Incident Management")
with col2:
    st.metric("IT Domain", "Operations", "Support Tickets")


st.success("Please login to access Cyber & IT dashboards")