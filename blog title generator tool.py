import streamlit as st
from pydantic import BaseModel
from typing import List

# Define a Pydantic model to validate the output
class Titles(BaseModel):
    titles: List[str]

# Function to generate blog titles (Placeholder for actual AI model integration)
def generate_titles(topic: str) -> List[str]:
    return [
        f"🚀 The Future of {topic}: What’s Next?",
        f"🔥 {topic} Hacks You Need to Know in 2025!",
        f"📚 How to Master {topic} in Just 30 Days",
        f"⚠️ Top 10 Mistakes to Avoid in {topic}",
        f"✅ The Ultimate {topic} Guide for Beginners"
    ]

# Streamlit UI setup
st.set_page_config(page_title="Blog Title Generator", layout="wide")

# Custom CSS for futuristic styling
st.markdown(
    """
    <style>
    /* Background Image */
    .main {
        background: url('https://source.unsplash.com/1600x900/?technology,ai,cyberpunk') no-repeat center center fixed;
        background-size: cover;
    }
    
    /* Title Styling */
    .title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        color: #ffcc00;
        text-shadow: 2px 2px 10px rgba(255, 204, 0, 0.8);
    }
    
    /* Subheader */
    .subheader {
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        color: #00eaff;
        text-shadow: 2px 2px 10px rgba(0, 234, 255, 0.8);
    }
    
    /* Input Box */
    .stTextInput>div>div>input {
        font-size: 18px !important;
        background: rgba(0, 0, 0, 0.6);
        color: #fff;
        border-radius: 8px;
        padding: 10px;
    }

    /* Generate Button */
    .stButton button {
        background: linear-gradient(45deg, #ff4b4b, #ffcc00);
        color: white;
        font-size: 18px;
        padding: 12px 25px;
        border-radius: 12px;
        transition: 0.3s;
        width: 100%;
        font-weight: bold;
    }
    
    .stButton button:hover {
        background: linear-gradient(45deg, #ffcc00, #ff4b4b);
        transform: scale(1.05);
        box-shadow: 0px 0px 15px rgba(255, 76, 76, 0.7);
    }

    /* Generated Titles */
    .generated-title {
        font-size: 20px;
        font-weight: bold;
        color: #00eaff;
        text-shadow: 1px 1px 8px rgba(0, 234, 255, 0.8);
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.markdown('<p class="title">🤖 AI-Powered Blog Title Generator</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Generate SEO-optimized and engaging blog titles instantly! 🚀</p>', unsafe_allow_html=True)
st.markdown("---")

# Input Section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    user_input = st.text_input("Enter your blog topic:", "Artificial Intelligence")

# Button Section
col4, col5, col6 = st.columns([1, 2, 1])
with col5:
    generate_button = st.button("✨ Generate Titles")

# Generate Titles
if generate_button:
    if user_input.strip():
        titles = generate_titles(user_input)
        
        # Display results
        st.markdown("### 🌟 Generated Blog Titles:")
        for idx, title in enumerate(titles, start=1):
            st.markdown(f'<p class="generated-title">{idx}. {title}</p>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter a valid topic.")

# Footer
st.markdown("---")
st.caption("🚀 Built with ❤️ using Streamlit | AI-Enhanced Creativity 💡")
