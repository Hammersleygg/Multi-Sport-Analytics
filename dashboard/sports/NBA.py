import streamlit as st
import pandas as pd


def nba_stats():
    # Page Style
    st.markdown(
            """
            <style>
            .main {
                color: black;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
            }
            """,
            unsafe_allow_html=True
        )

    # NBA Title
    st.markdown("<h1 style='text-align: center; color: black;'>NBA Data 🏀</h1>", unsafe_allow_html=True)

    # Intro Paragraph
    st.markdown(
        """
        <div class="main">
            <p>
                Welcome to the NBA Statistics page, your gateway to exploring in-depth basketball data and
                uncovering player and team trends throughout different seasons. This interactive platform 
                allows you to filter data by players, teams, positions, and years, providing a detailed look 
                at statistics such as points per game, assists, rebounds, and shooting percentages. With 
                powerful visualizations, you can track trends, compare player performance across seasons, 
                and analyze key metrics across the league. Whether you're a fan looking to see how your 
                favorite player performed over the years or an analyst interested in discovering patterns 
                in team performance, this dashboard provides the tools to break down the data and uncover 
                meaningful insights.
            </p>
        </div>

        """, unsafe_allow_html=True)

    # Loading in the Data
    def load_data():
        df = pd.read_csv("data/nba_data.csv")
        return df
    df = load_data()
    st.write(df)  # Displays the dataframe