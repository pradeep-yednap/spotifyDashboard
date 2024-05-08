import streamlit as st
import altair as alt

def top_10_tracks(df):
    
    st.subheader("Top 10 Tracks")
    grouped_df = df.groupby('track_name')['streams'].sum().reset_index()
    sorted_df = grouped_df.sort_values('streams', ascending=False).head(10)

    chart = alt.Chart(sorted_df).mark_bar().encode(
        x='streams',
        y=alt.Y('track_name', sort='-x',title='Track'),
    ).properties(
        width=600,
        height=400
    )
    st.altair_chart(chart)
    
def top_10_artists(df):
    st.subheader("Top 10 Artists")
    df['artist_name'] = df['artist_name'].str.split(',')
    df = df.explode('artist_name')

    df['artist_name'] = df['artist_name'].str.strip()

    # Group by artist_name and count unique track_name entries
    grouped_df = df.groupby('artist_name')['track_name'].nunique().reset_index()

    
    sorted_df = grouped_df.sort_values('track_name', ascending=False).head(10)

    chart = alt.Chart(sorted_df).mark_bar().encode(
        y=alt.Y('artist_name', sort='-x', title='Artist', axis=alt.Axis(labelOverlap=True)),
        x=alt.X('track_name', title='track'),
        
    ).properties(
        width=600,
        height=400
    )
    st.altair_chart(chart)
    
def top_10_charts_spotify(df):
    st.subheader("Spotify")
    grouped_df = df.groupby('track_name').agg({'in_spotify_charts': 'sum', 'in_spotify_playlists': 'sum', 'streams': 'sum'}).reset_index()

    non_zero_grouped_df = grouped_df[grouped_df['in_spotify_charts'] > 0]

    sorted_df = non_zero_grouped_df.sort_values('in_spotify_charts', ascending=True)
    sorted_df = sorted_df[sorted_df['in_spotify_charts'] == 1]

    melted_df = sorted_df.melt(id_vars='track_name', value_vars=['streams', 'in_spotify_playlists'])
    
    #stacked bar chart
    chart = alt.Chart(melted_df).mark_bar().encode(
        x=alt.X('value', scale=alt.Scale(type='log'), title='Value (Log Scale)'),
        y=alt.Y('track_name', sort='-x', title='Track'),
        color='variable',
        tooltip=['track_name', 'variable', 'value']
    ).properties(
        width=1000,
        height=500
    )
    st.altair_chart(chart)