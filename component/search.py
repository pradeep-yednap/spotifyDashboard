import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

def searchArtistSong(df):
    search_input = st.text_input("Search for an artist or track")
    
    search_button = st.button("Search")

    if search_button:
        search_input = search_input.lower()

        # Check if the input is a track name or artist name
        if search_input in df['track_name'].str.lower().values or search_input in df['artist_name'].str.lower().values:
            # Filter the dataframe based on the search input
            filtered_df = df[(df['artist_name'].str.lower().str.contains(search_input)) | (df['track_name'].str.lower().str.contains(search_input))]

            if not filtered_df.empty:
                # Sort the dataframe in decreasing order of streams
                sorted_df = filtered_df.sort_values('streams', ascending=False)
                # Display the dataframe
                st.header(f"Search results for '{search_input}'")
                st.subheader(f"Each Song Details of {search_input}")
                st.dataframe(sorted_df)

                # Create a spider plot for the searched artist in the sorted dataframe
                features = ["danceability", "valence", "energy", "acousticness", "instrumentalness", "liveness", "speechiness"]

                # INSTEAD OF PASSING MANUALLY THE FEATURES, WE CAN DO IT LIKE THIS
                
                mean_features = filtered_df[features].mean()
                    
                # Create a spider plot
                fig = go.Figure(data=go.Scatterpolar(
                    r=mean_features,
                    theta=features,
                    fill='toself'
                ))

                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            visible=True,
                            range=[0, 100]                        
                        )),
                    showlegend=False,
                    height=600,                         
                )
                st.header(f"Feature of songs of {search_input}")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.write("No results found for your search.")
        else:
            st.write("Please enter a valid search query.")