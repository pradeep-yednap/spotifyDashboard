import streamlit as st
from streamlit.logger import get_logger
from component.metrics import show_metrics
from component.search import searchArtistSong
from component.top_10 import top_10_tracks, top_10_artists, top_10_charts_spotify
import component.sidebar as sb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Spotify Dashboard",
        page_icon="🎵",
        layout="wide",
    )

    st.write("## Spotify-2023 Dashboard!")
  
    @st.cache_data
    def load_data():
        return pd.read_pickle('./rsc/spotify2023.pkl')

    main_df = load_data()
    
    df = sb.show_sidebar(main_df)
    
    #Main Window
    with st.expander("Data Preview"):
        st.dataframe(df)
    
    tab1, tab2, tab3 = st.tabs(["Data Metrics", "Data Comparison", "Song Analysis"])
    
    with tab1:    
        show_metrics(df)
        
        st.markdown("<hr>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            top_10_tracks(df)
            
        with col2:
            top_10_artists(df)
                
        st.subheader("Top Charts")
        with st.container(border=True):
            top_10_charts_spotify(df)
    
    with tab2:

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
            ).properties(
                height=600,
                width=200
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
                        
                        
    with tab3:
        searchArtistSong(df)        
          
    
if __name__ == "__main__":
    run()
