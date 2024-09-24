#Home.py
import streamlit as st
from sports import NBA, NFL, MLB

def show_home():
    st.markdown(
            """
            <style>
            .main {
                color: black;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
            }
            h1 {
                text-align: center;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    # Home page title
    st.markdown("<h1 style='text-align: center; color: black;'>Welcome to my Multi-Sport Analytics Dashboard!</h1>", unsafe_allow_html=True)
    
    # Home page info
    st.markdown(
        """
        <div class="main">
            <p>
                Due to my love for sport and data, I wanted to create something that could incorporate both.
                Here is my attempt at the creation of a dynamic web-based platform that allows users to explore
                and analyze player/team statistics across multiple sports (e.g., MLB, NBA, NFL) while
                incorporating predictive models for game outcomes and player performance. This dashboard will
                offer a comprehensive view of sports data, visualizations, and potentially an AI-based recommendation 
                system.
            </p>

        <h3>What this project includes:</h3>
        <ul>
            <li>Data collection</li>
            <li>Exploratory data analysis</li>
            <li>Player/Team comparisons</li>
            <li>Player Recommendations</li>
            <li>Analytics</li>
            <li>Past/Current Comparisons</li>
        </ul>

        <h3>Tech Stack</h3>
        <ul>
            <li><strong>Backend:</strong> Python, MySQL for data storage.</li>
            <li><strong>Frontend:</strong> Streamlit/Dash for the interactive dashboard.</li>
            <li><strong>Machine Learning:</strong> Scikit-learn, TensorFlow, or XGBoost for predictive models.</li>
            <li><strong>Visualization:</strong> Plotly, Matplotlib, or Seaborn for interactive graphs.</li>
            <li><strong>Data Sources:</strong> APIs for MLB, NBA, NFL, or any other sport to add.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    # Sidebar 
    st.sidebar.title("Sports Leagues")
    st.sidebar.markdown("---")

    selected_page = st.sidebar.radio("Select your page: ", options=[
        "🏠 Home",
        "⚾ MLB Stats",
        "🏀 NBA Stats",
        "🏈 NFL Stats"
    ])
    
    # Display content based on selected page
    if selected_page == "🏠 Home":
        st.sidebar.success("Multi-Sport Analytics Dashbaord!")
        show_home()  # Show home page content
        
    elif selected_page == "⚾ MLB Stats":
        st.sidebar.success("Welcome to MLB Stats page")
        MLB.mlb_stats()  # Load MLB stats content

    elif selected_page == "🏀 NBA Stats":
        st.sidebar.success("Welcome to NBA Stats page")
        NBA.nba_stats()  # Load NBA stats content

    elif selected_page == "🏈 NFL Stats":
        st.sidebar.success("Welcome to NFL Stats page")
        NFL.nfl_stats()  # Load NFL stats content

if __name__ == "__main__":
    st.set_page_config(page_title="Multi-Sport Data Analytics", page_icon="img\msad_logo.png", layout="wide")
    main()