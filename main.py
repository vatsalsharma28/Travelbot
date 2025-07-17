import streamlit as st
from langgraph_flow import run_conversation
import re

st.set_page_config(page_title="TravelBot AI", layout="wide")

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .travel-form {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .result-box {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🚌 TravelBot AI - Smart Bus Booking Assistant</h1>', unsafe_allow_html=True)

st.markdown('<div class="travel-form">', unsafe_allow_html=True)
st.subheader("🎯 Find Your Perfect Bus Route")

# Two-column layout for destinations
col1, col2 = st.columns(2)

with col1:
    from_destination = st.text_input(
        "📍 From:",
        placeholder="e.g., Jaipur",
        help="Enter your starting destination"
    )

with col2:
    to_destination = st.text_input(
        "🎯 To:",
        placeholder="e.g., Delhi",
        help="Enter your destination"
    )

# Date selection
travel_date = st.date_input(
    "📅 Travel Date:",
    help="Select your preferred travel date"
)

st.markdown('</div>', unsafe_allow_html=True)

# Search button
if st.button("🔍 Search Buses", type="primary", use_container_width=True):
    if from_destination and to_destination:
        with st.spinner("🔍 Searching for buses..."):
            # Create a travel query
            query = f"bus from {from_destination} to {to_destination}"
            result = run_conversation(query)
            
            st.success("✅ Found bus options!")
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown(result)
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("❌ Please enter both source and destination!")

# Example queries
st.markdown("### 💡 Example Queries:")
examples = [
    "bus from Mumbai to Pune",
    "travel from Bangalore to Chennai",
    "bus booking from Jaipur to Delhi",
    "bus tickets from Hyderabad to Bangalore"
]

for example in examples:
    if st.button(f"🔍 {example}", key=example):
        with st.spinner("🔍 Searching for buses..."):
            result = run_conversation(example)
            st.success("✅ Found bus options!")
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.markdown(result)
            st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🚌 TravelBot AI - Your Smart Travel Companion</p>
    <p>Powered by LangGraph, Serper API, and AI</p>
</div>
""", unsafe_allow_html=True)