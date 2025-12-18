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

if st.session_state.role != 'cyber':
    st.error("Access Denied - Cyber team only!")
    st.stop()

st.title("Cybersecurity Dashboard")
st.success(f"Welcome, {st.session_state.username}!")

#imports data
db = DatabaseManager()
incidents = db.read_cyber_incidents()

if incidents:
    df = pd.DataFrame(incidents, columns=[
        'id', 'incident_id', 'title', 'severity', 'category', 
        'status', 'created_date', 'resolved_date', 'resolution_time_hours', 'description'
    ])
    
    #shows quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Incidents", len(df))
    with col2:
        st.metric("Open Incidents", len(df[df['status'] == 'Open']))
    with col3:
        st.metric("High Severity", len(df[df['severity'] == 'High']))
    with col4:
        st.metric("Critical", len(df[df['severity'] == 'Critical']))
    
    #total incieents by severity
    st.markdown("This graph shows the relation between Incidents and Severity")
    st.subheader("Incidents by Severity Level")
    
    #count incidents by severity
    severity_counts = df['severity'].value_counts()
    
    #simple bar graph
    st.bar_chart(severity_counts)
    #more graphs
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("This graph shows the relation between Incidents and Category")
        st.subheader("Incidents by Category")
        st.bar_chart(df['category'].value_counts())  #bar chart for incidents by category

    with col2:
        st.markdown("This graph shows the relation between Incidents and Status")
        st.subheader("Incidents by Status")    
        st.bar_chart(df['status'].value_counts())    #bar chart for incidents by status
        
        
        #our data table
st.markdown("---")
st.subheader("All Security Incidents")
st.dataframe(
    df[['incident_id', 'severity', 'category', 'status']],
    use_container_width=True
)
    


#form to add new insidents
st.markdown("---")
st.subheader("Report New Security Incident")
with st.form("new_incident_form"):
    incident_id = st.text_input("Incident ID*")
    title = st.text_input("Title*")
    severity = st.selectbox("Severity*", ["Low", "Medium", "High", "Critical"])
    category = st.selectbox("Category*", ["Phishing", "Malware", "DDoS", "Unauthorized Access"])
    status = st.selectbox("Status*", ["Open", "Investigating", "Resolved"])
    created_date = st.date_input("Incident Date*")
    description = st.text_area("Description")
    
    if st.form_submit_button("Report Incident"):
        if incident_id and title:
            db.create_cyber_incident(incident_id, severity, category, status)
            st.success("Incident reported!")
            st.rerun()