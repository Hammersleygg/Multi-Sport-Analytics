import streamlit as st
import pandas as pd

def nfl_stats():
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

    # MLB Title
    st.markdown("<h1 style='text-align: center; color: black;'>NFL Data 🏈</h1>", unsafe_allow_html=True)


    # Intro Paragraph
    st.markdown(
        """
        <div class="main">
            <p>
                Welcome to the NFL Statistics page, where you can explore detailed football data and analyze 
                trends in player and team performance over the years. This platform allows you to filter by 
                players, teams, and seasons, providing insights into key metrics like touchdowns, rushing 
                yards, passing completions, and more. With intuitive visualizations, you can track trends like 
                touchdowns per season, compare player stats across different teams, and explore how players 
                have performed over time. Whether you're a fan following your favorite team's journey or an 
                analyst looking to dive deep into the numbers, this dashboard gives you the tools to break down 
                the data and reveal key insights about the game.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Loading in the Data

    ### FIGURE OUT WHAT I AM DOING WITH DATA FOR NFL