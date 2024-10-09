import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    return pd.read_csv('data/nba_data.csv')

def vizualize_points_vs_games(df):
    st.subheader("Player Points vs Games Played")

    # User Input for Filtering 
    selected_year = st.selectbox("Select Season:", options=['All'] + df['Season'].unique().tolist(), key="pts_game_year")
    selected_team = st.selectbox("Select Team:", options=['All'] + df['TEAM'].unique().tolist(), key="pts_game_team") 

    # Filtered Data
    filtered_df = df.copy()
    if selected_team != 'All':
        filtered_df = filtered_df[filtered_df['TEAM'] == selected_team]
    if selected_year != 'All':
        filtered_df = filtered_df[filtered_df['Season'] == selected_year]

    # Visualizations
    if not filtered_df.empty:
        bar_fig = px.bar(filtered_df, x='PLAYER', y=['PTS', 'GP'], title='Player Points vs Games Played', barmode='group')
        st.plotly_chart(bar_fig)
    else:
        st.warning("No data available for the selected filters.")

def fg_pct_over_season(df, selected_player=None):
    st.subheader("Field Goal PCT vs. Season")

    # User Input for Filtering 
    selected_season = st.selectbox("Select Season:", options=['All'] + df['Season'].unique().tolist(), key="fg_pct_year")
    selected_player = st.selectbox("Select Player:", options=['All'] + df['PLAYER'].unique().tolist(), key="fg_pct_player") 

    # Filtered Data
    filtered_df = df.copy()
    if selected_season != 'All':
        filtered_df = filtered_df[filtered_df['Season'] == selected_season]
    if selected_player != 'All':
        filtered_df = filtered_df[filtered_df['PLAYER'] == selected_player]

    plt.figure(figsize=(10, 6))

    if selected_player != 'All':
        # Filter data for selected player
        player_df = df[df['PLAYER'] == selected_player]
        sns.lineplot(x='Season', y='FG_PCT', data=player_df, marker='o', label=selected_player)
    else:
        # Group by Season and calculate the mean for FG_PCT
        avg_fg_pct = df.groupby('Season')['FG_PCT'].mean().reset_index()  # Convert to DataFrame
        sns.lineplot(x='Season', y='FG_PCT', data=avg_fg_pct, marker='o', label='Average FG%')

    plt.title('Field Goal Percentage Over Seasons')
    plt.xlabel('Season')
    plt.ylabel('Field Goal Percentage')
    plt.xticks(rotation=45)
    plt.legend()

    # Display the plot in Streamlit
    st.pyplot(plt)

def plot_fgm_vs_fga_comparison(df):
    st.subheader("Compare FGM vs FGA Across Multiple Players")

    # User Input for Filtering
    selected_season = st.selectbox("Select Season:", options=['All'] + df['Season'].unique().tolist(), key="fgm_vs_fga_season")
    selected_players = st.multiselect("Select Players:", options=df['PLAYER'].unique().tolist(), key="fgm_vs_fga_players")

    # Filtered Data by Season
    filtered_df = df.copy()
    if selected_season != 'All':
        filtered_df = filtered_df[filtered_df['Season'] == selected_season]

    # Filter by Selected Players
    if selected_players:
        filtered_df = filtered_df[filtered_df['PLAYER'].isin(selected_players)]

    # Plot FGM vs FGA for the selected players
    plt.figure(figsize=(10, 6))

    if selected_players:
        # Loop over the selected players and plot each one
        for player in selected_players:
            player_df = filtered_df[filtered_df['PLAYER'] == player]
            sns.scatterplot(x='FGA', y='FGM', data=player_df, marker='o', label=player)
    else:
        st.warning("Please select at least one player for comparison.")

    plt.title('Field Goals Made vs Field Goals Attempted - Player Comparison')
    plt.xlabel('Field Goals Attempted (FGA)')
    plt.ylabel('Field Goals Made (FGM)')
    plt.legend(title="Players")
    plt.grid(True)

    # Display the plot in Streamlit
    st.pyplot(plt)

def visualize_player_comparison(df):
    st.subheader("Player Comparison Across Multiple Stats")

    stats_options = ['MIN', 'FGM', 'FG_PCT', 'FG3M','FG3A','FG3_PCT','FTM','FTA','FT_PCT','OREB','DREB','REB','AST','STL','BLK','TOV','PTS']

    # User input for filtering
    selected_players = st.multiselect("Select Players to Compare:", options=df['PLAYER'].unique().tolist(), default=df['PLAYER'].unique()[:2], key="comparison_players")
    selected_stats = st.multiselect("Select Stats for Comparison:", options=stats_options, default=stats_options[:4], key="comparison_stats")


    if selected_players and selected_stats:
        # Normalize stats for comparison
        filtered_df = df[df['PLAYER'].isin(selected_players)]
        for stat in selected_stats:
            filtered_df[stat] = filtered_df[stat].astype(float)

        scaler = MinMaxScaler()
        normalized_stats = scaler.fit_transform(filtered_df[selected_stats])
        normalized_df = pd.DataFrame(normalized_stats, columns=selected_stats, index=filtered_df.index)

        # Create radar chart
        fig = go.Figure()
        for player in selected_players:
            player_data = normalized_df[filtered_df['PLAYER'] == player].mean()
            fig.add_trace(go.Scatterpolar(
                r=player_data,
                theta=selected_stats,
                fill='toself',
                name=player
            ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 1])),
            showlegend=True,
            title=f"Comparison of Selected Stats for {', '.join(selected_players)}"
        )

        st.plotly_chart(fig)
    else:
        st.warning("Please select at least one player and one stat for comparison.")

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
    st.markdown("<h1 style='text-align: center; color: black;'>NBA Statistics 🏀</h1>", unsafe_allow_html=True)

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
    
    df = load_data()

    st.dataframe(df)

    # EDA Section
    st.markdown("<h1 style='text-align: center; color: black;'> EDA Visualizations </h1>", unsafe_allow_html=True)
    
    # Call the visualizations
    visualize_player_comparison(df)
    vizualize_points_vs_games(df)
    fg_pct_over_season(df)
    plot_fgm_vs_fga_comparison(df)
