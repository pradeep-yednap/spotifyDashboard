import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.graph_objects as go

def visualization(df):
    st.header("Spotify 2023 Dashboard")
    st.markdown(
        """
        The following table is the preview of the DataFrame used to build the spotify dashboard.
    """
    )
    

    col1, col2 = st.columns(2)

    # Showing top 10 most streamed song in the first column
    with col1:
        st.subheader("Top 10 Most streamed songs on Spotify")

        top_10 = df.nlargest(10, "streams")[["track_name", "streams"]]
        
        top_10.loc[top_10["track_name"] == "Sunflower - Spider-Man: Into the Spider-Verse", "track_name"] = "Sunflower: Into the Spider-Verse"

        top_10["streams"] = top_10["streams"].div(1000000000)

        plt.figure(figsize = (8,6))
        plt.xticks(rotation=45, ha = "right")
        plt.ticklabel_format(style='plain', axis='both', scilimits=(0,0))
        plot = sns.barplot(data = top_10, x = "track_name", y = "streams", color="#00A36C")
        plt.xlabel("Track name")
        plt.ylabel("Streams - billion")    
        st.pyplot(plot.get_figure())

    # Which artists has the most streamed songs in the second column
    with col2:
        st.subheader("Artists with the most streams on Spotify")

        played = df.groupby("artist_name")["streams"].agg("sum").sort_values(ascending=False)
        most_played = played.nlargest(10)
        plt.figure(figsize = (8,6))
        plt.xticks(rotation=45, ha = "right")
        plot = sns.barplot(x = most_played.index, y = (most_played/1000000000), color="#ffaa00")
        plt.xlabel("Artist")
        plt.ylabel("Streams - billion")
        st.pyplot(plot.get_figure())
        pass

        
    # Sort the dataframe by 'streams' and take the top 10
    st.subheader("Distribution of Top 10 Songs Across Various Music Charts")
    top_songs = df.sort_values('streams', ascending=False).head(10)

        # Melt the dataframe to long format
    melted_df = pd.melt(top_songs, id_vars=['track_name'], value_vars=['in_apple_charts', 'in_shazam_charts', 'in_spotify_charts', 'in_deezer_charts'])

        # Create a stacked column chart
    chart = alt.Chart(melted_df).mark_bar().encode(
            x='track_name:N',
            y='value:Q',
            color='variable:N',
            tooltip=['track_name', 'variable', 'value']
        )


    st.altair_chart(chart, use_container_width=True)

    #Scatter Plot to show different Visualizations
    st.subheader("Scatter Plot to visualize different characteristics")

    def create_scatter_plot(data, x_variables):
        scatter_plots = []

        for var in x_variables:
            scatter_plot = px.scatter(data, x=var, y='streams', title=f'Streams vs. {var}')
            scatter_plots.append(scatter_plot)

        return scatter_plots    

    # List of variables for scatter plots
    variables = ["bpm", "danceability", "valence", "energy", "acousticness", "instrumentalness", "liveness", "speechiness"]

    scatter_plots = create_scatter_plot(data=df, x_variables=variables)

    # Display the grid of scatter plots in Streamlit
    num_plots = len(scatter_plots)
    rows = (num_plots // 3) + (num_plots % 3 > 0)  # Calculate the number of rows

    for row in range(rows):
        cols = st.columns(3)
        for col in range(3):
            idx = row * 3 + col
            if idx < num_plots:
                with cols[col]:
                    st.plotly_chart(scatter_plots[idx], use_container_width=True)       