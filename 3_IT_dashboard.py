import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import DatabaseManager

#verification process checks login
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.error("Please login first!")
    st.stop()

if st.session_state.role != 'it':
    st.error("Access Denied - IT team only!")
    st.stop()

st.title("IT Team Dashboard")
st.success(f"Welcome, {st.session_state.username}!")

#imports data
db = DatabaseManager()
incidents = db.read_it_tickets()

if incidents:
    df = pd.DataFrame(incidents, columns=[
        'id', 'incident_id', 'title', 'severity', 'category', 
        'status', 'created_date', 'resolved_date', 'resolution_time_hours', 'description'
    ])

    # 1. KPI METRICS SECTION (Top of page - 4 columns)
    st.subheader("Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Tickets", len(df))
    with col2:
        st.metric("Open Tickets", len(df[df['status'] == 'Open']))
    
    st.markdown("---")
    
    # 2. CHARTS SECTION (Full width, two columns side-by-side)
    st.subheader("Incident Analysis")
    
    # Create two equal columns for charts
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.markdown("**Incidents by Category**")
        st.bar_chart(df['category'].value_counts(), height=350)  # Increased height
    
    with chart_col2:
        st.markdown("**Incidents by Status**")
        st.bar_chart(df['status'].value_counts(), height=350)

#our data table
st.markdown("---")
st.subheader("All Security Incidents")
st.dataframe(
    df[['id', 'incident_id', 'title', 'severity', 'category']],
    use_container_width=True
)

