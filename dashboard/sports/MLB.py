import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler

def load_data():
    return pd.read_csv('data/mlb_data.csv')

def visualize_home_runs_rbi(df):
    st.subheader("Home Runs vs RBIs")
    
    # User input for filtering
    selected_year = st.selectbox("Select Year:", options=['All'] + df['year'].unique().tolist(), key="hr_rbi_year")
    selected_team = st.selectbox("Select Team:", options=['All'] + df['teamName'].unique().tolist(), key="hr_rbi_team")
    
    # Filter Data
    filtered_df = df.copy()
    if selected_team != 'All':
        filtered_df = filtered_df[filtered_df['teamName'] == selected_team]
    if selected_year != 'All':
        filtered_df = filtered_df[filtered_df['year'] == selected_year]

    # Visualizations
    if not filtered_df.empty:
        bar_fig = px.bar(filtered_df, x='playerFullName', y=['homeRuns', 'rbi'], title='Home Runs and RBIs', barmode='group')
        st.plotly_chart(bar_fig)
    else:
        st.warning("No data available for the selected filters.")

def visualize_avg_ops_comparison(df):
    st.subheader("Player Average and OPS Comparison")
    
    # User input for filtering
    selected_players = st.multiselect("Select Players to Compare:", options=df['playerFullName'].unique().tolist(), default=df['playerFullName'].unique()[:2], key="avg_ops_players")
    
    if selected_players:
        filtered_df = df[df['playerFullName'].isin(selected_players)]
        avg_ops_fig = go.Figure()

        # Add a bar for batting average
        avg_ops_fig.add_trace(go.Bar(
            x=filtered_df['playerFullName'],
            y=filtered_df['avg'],
            name='Batting Average',
            marker_color='blue'
        ))

        # Add a bar for OPS
        avg_ops_fig.add_trace(go.Bar(
            x=filtered_df['playerFullName'],
            y=filtered_df['ops'],
            name='OPS',
            marker_color='lightBlue'
        ))

        avg_ops_fig.update_layout(
            title='Player Average and OPS Comparison',
            barmode='group',
            xaxis_title='Player',
            yaxis_title='Statistics',
            legend_title='Metrics'
        )
        
        st.plotly_chart(avg_ops_fig)
    else:
        st.warning("Please select at least one player for comparison.")

def visualize_player_comparison(df):
    st.subheader("Player Comparison Across Multiple Stats")
    
    stats_options = ['homeRuns', 'avg', 'obp', 'slg', 'rbi', 'runs', 'hits', 'strikeOuts']
    
    # User input for filtering
    selected_players = st.multiselect("Select Players to Compare:", options=df['playerFullName'].unique().tolist(), default=df['playerFullName'].unique()[:2], key="comparison_players")
    selected_stats = st.multiselect("Select Stats for Comparison:", options=stats_options, default=stats_options[:4], key="comparison_stats")
    
    if selected_players and selected_stats:
        # Normalize stats for comparison
        filtered_df = df[df['playerFullName'].isin(selected_players)]
        for stat in selected_stats:
            filtered_df[stat] = filtered_df[stat].astype(float)

        scaler = MinMaxScaler()
        normalized_stats = scaler.fit_transform(filtered_df[selected_stats])
        normalized_df = pd.DataFrame(normalized_stats, columns=selected_stats, index=filtered_df.index)

        # Create radar chart
        fig = go.Figure()
        for player in selected_players:
            player_data = normalized_df[filtered_df['playerFullName'] == player].mean()
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

def mlb_stats():
    st.markdown(
            """
            <style>
            .main {
                color: black;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
            }
            </style>
            """, unsafe_allow_html=True)

    # Page title
    st.markdown("<h1 style='text-align: center; color: black;'> MLB Statistics ⚾</h1>", unsafe_allow_html=True)
    
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
                a specific team or comparing player performance over time, this dashboard allows you to explore the data and
                uncover key insights. Use the filtering options to tailor your analysis, and discover how players stack up
                against each other in various statistical categories.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Load data
    df = load_data()
    
    # Show DataFrame
    st.dataframe(df)

    # EDA Section
    st.markdown("<h1 style='text-align: center; color: black;'> EDA Visualizations </h1>", unsafe_allow_html=True)
    
    # Call the visualizations
    visualize_player_comparison(df)
    visualize_home_runs_rbi(df)
    visualize_avg_ops_comparison(df)

# Run the app
if __name__ == "__main__":
    mlb_stats()
