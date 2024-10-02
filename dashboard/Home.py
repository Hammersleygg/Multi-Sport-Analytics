import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_option_menu import option_menu
from sports import MLB, NBA, NFL

def show_home():
    st.markdown("""
        <style>
        .main-title {
            text-align: center;
            color: #9C9C9C;
            margin-bottom: 30px;
        }
        .stTab {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
        .sidebar .sidebar-content {
            background-image: linear-gradient(#2c3e50,#34495e);
        }
        .sidebar-text {
            color: #ecf0f1;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("<h1 class='main-title'>Multi-Sport Analytics Dashboard</h1>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["📌 Overview", "🔍 Features", "🛠️ Tech Stack", "📊 Demo"])

    with tab1:
        st.header("Project Overview")
        st.write("""
        Welcome to the cutting-edge Multi-Sport Analytics Dashboard! This revolutionary platform is designed to transform the way sports enthusiasts, analysts, and professionals interact with sports data. By leveraging advanced analytics and machine learning, we provide unprecedented insights into player performance, team dynamics, and game outcomes across the MLB, NBA, and NFL.

        Our dashboard goes beyond traditional statistics, offering a holistic view of sports performance that combines historical data with predictive analytics. Whether you're a fantasy sports player looking for an edge, a coach seeking to optimize team strategy, or a sports analyst diving deep into performance metrics, our platform offers the tools and insights you need to stay ahead of the game.
        """)

    with tab2:
        st.header("Key Features")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Data and Analysis")
            st.markdown("""
            - **Comprehensive Data Collection**: Real-time data from multiple leagues, ensuring you're always up-to-date.
            - **Advanced Exploratory Analysis**: Dive deep into performance trends with our interactive tools.
            - **Cross-League Comparisons**: Unique insights by comparing stats across different sports.
            - **Historical Performance Tracking**: Analyze how players and teams evolve over time.
            """)
        with col2:
            st.subheader("Intelligent Insights")
            st.markdown("""
            - **AI-Powered Recommendations**: Get personalized player and team suggestions based on your criteria.
            - **Predictive Modeling**: Forecast game outcomes and player performances with cutting-edge ML algorithms.
            - **Custom Metric Creation**: Design your own performance metrics to gain a competitive edge.
            - **Interactive Visualizations**: Bring your data to life with dynamic, customizable charts and graphs.
            """)

    with tab3:
        st.header("Tech Stack")
        st.write("""
        Our platform leverages a state-of-the-art tech stack to deliver unparalleled performance and insights:
        """)
        st.json({
            "Backend": ["Python 3.9+", "MySQL 8.0", "FastAPI"],
            "Frontend": ["Streamlit 1.10+", "React for custom components"],
            "Machine Learning": ["Scikit-learn 1.0+", "TensorFlow 2.6+", "XGBoost 1.5+"],
            "Data Processing": ["Pandas 1.3+", "NumPy 1.21+"],
            "Visualization": ["Plotly 5.3+", "Matplotlib 3.4+", "Seaborn 0.11+"],
            "Data Sources": ["Official MLB, NBA, NFL APIs", "Web scraping for additional insights"],
            "Deployment": ["Docker", "AWS for scalability"]
        })

    with tab4:
        st.header("Interactive Analytics Demo")
        st.write("""
        Experience the power of our analytics with this interactive demo. This visualization showcases team performance across multiple metrics, allowing you to explore the data and gain insights at a glance.
        """)
        metrics = ['Offensive Efficiency', 'Defensive Prowess', 'Player Synergy', 'Fan Engagement']
        teams = ['Warriors', 'Lakers', 'Celtics', 'Heat', 'Bucks']
        data = pd.DataFrame({
            'Team': teams * 4,
            'Metric': [m for m in metrics for _ in range(5)],
            'Score': [85, 82, 88, 79, 86, 78, 80, 85, 77, 82, 92, 89, 87, 90, 88, 76, 79, 74, 81, 77]
        })
        fig = px.scatter(data, x='Team', y='Score', size='Score', color='Metric',
                         title='Comprehensive Team Performance Analysis', size_max=60)
        st.plotly_chart(fig)

def main():
    # Sidebar 
    with st.sidebar:
        st.markdown("<h1 style='text-align: center; color: grey;'>Sports Leagues</h1>", unsafe_allow_html=True)
        st.sidebar.markdown("---")
        selected = option_menu(
            menu_title=None,
            options=["Home", "MLB Stats", "NBA Stats", "NFL Stats"],
            icons=["house", "person", "dribbble", "shield"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#9C9C9C"},
                "icon": {"color": "#00115C", "font-size": "25px"}, 
                "nav-link": {"color": "#ecf0f1", "font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#4a69bd"},
                "nav-link-selected": {"background-color": "#4a69bd"},
            }
        )
    
    # Display content based on selected page
    if selected == "Home":
        show_home()
    elif selected == "MLB Stats":
        st.title("MLB Statistics")
        MLB.mlb_stats()  # Load MLB stats 
    elif selected == "NBA Stats":
        st.title("NBA Statistics")
        NBA.nba_stats() # Load NBA Stats
    elif selected == "NFL Stats":
        st.title("NFL Statistics")
        st.write("NFL stats content coming soon!")

if __name__ == "__main__":
    st.set_page_config(page_title="Multi-Sport Analytics Dashboard", page_icon="🏆", layout="wide")
    main()