import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns

def mlb_stats():
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

    # Page title
    st.markdown("<h1 style='text-align: center; color: black;'> MLB Statistics </h1>", unsafe_allow_html=True)
    
    # Intro Paragraph
    st.markdown(
        """
        <div class="main">
            <p>
                Welcome to the MLB Statistics page, where you can dive into comprehensive baseball data and explore player
                and team trends over the years. This platform offers a dynamic way to analyze key statistics across multiple
                dimensions, including players, teams, positions, and seasons. With an intuitive interface, you can filter
                data based on your preferences, visualize critical stats like home runs, batting averages, and RBIs, and 
                compare player performances across different years and positions. Whether you're interested in trends for
                a specific team or comparing player performance over time, thisdashboard allows you to explore the data and
                uncover key insights. Use the filtering options to tailor your analysis, and discover how players stack up
                against each other in various statistical categories.
            </p>
        </div>

        """, unsafe_allow_html=True)

    # Load your data (modify the path as necessary)
    df = pd.read_csv('data\mlb_data.csv')

    # Showing the data frame 
    st.write(df)

    # Existing stats display (modify this section based on your existing code)
    # For example, display some general statistics or visualizations here

    # EDA Section
    st.header("Exploratory Data Analysis")

    # Filters
    teams = df['teamName'].unique()
    players = df['playerFullName'].unique()
    years = df['year'].unique()
    postion = df['position'].unique()
    stats_options = ['homeRuns', 'avg', 'obp', 'slg', 'rbi', 'runs', 'hits', 'strikeOuts']  # Relevant stats

    # User input for filtering
    selected_team = st.selectbox("Select Team:", options=['All'] + list(teams))
    selected_player = st.selectbox("Select Player:", options=['All'] + list(players))
    selected_year = st.selectbox("Select Year:", options=['All'] + list(years))
    selected_stat = st.selectbox("Select Stat to Visualize:", options=stats_options)
    selected_position = st.selectbox("Select Position for players to be compared:", options=['All'] + list(postion))

    # Filter Data placed into a DF based on selections
    filtered_df = df
    if selected_team != 'All':
        filtered_df = filtered_df[filtered_df['teamName'] == selected_team]
    if selected_player != 'All':
        filtered_df = filtered_df[filtered_df['playerFullName'] == selected_player]
    if selected_year != 'All':
        filtered_df = filtered_df[filtered_df['year'] == selected_year]
    if selected_position != 'All':
        filtered_df = filtered_df[filtered_df['position'] == selected_position]

    # Visualizations
    if not filtered_df.empty:
        # Trend Visualization
        trend_fig = px.line(filtered_df, x='year', y=selected_stat, color='playerFullName', title=f'Trends in {selected_stat} for Selected Players')
        st.plotly_chart(trend_fig)

        # Compare Players
        

        # Show key trends
        st.subheader(f"Key Trends for {selected_stat}:")
        trend_summary = filtered_df.groupby('year')[selected_stat].mean().reset_index()
        st.line_chart(trend_summary.set_index('year'))

    else:
        st.warning("No data available for the selected filters.")