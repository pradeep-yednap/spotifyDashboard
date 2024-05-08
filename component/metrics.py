import streamlit as st

def show_metrics(df):
    total_songs = df.shape[0]
    total_artists = df['artist_name'].nunique()

    with open('styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    col1, col2  = st.columns(2)
    with col1:
        st.markdown(f'<div class="metricBox"><strong>Total Songs</strong><br><span class="metricValue">{total_songs}</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metricBox"><strong>Total Artists</strong><br><span class="metricValue">{total_artists}</span></div>', unsafe_allow_html=True)
    
    
    #for modes : major and mino"
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="metricBox metricMode"><strong>Major</strong><br><span class="metricValue">{df[df["mode"] == "Major"].shape[0]}</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metricBox metricMode"><strong>Minor</strong><br><span class="metricValue">{df[df["mode"] == "Minor"].shape[0]}</span></div>', unsafe_allow_html=True)
    
    
    #for keys A A# B C C# D D# E F F# G G#
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.markdown(f'<div class="metricBox metricKey"><strong>A</strong><br><span class="metricValue">{df[df["key"] == "A"].shape[0]}</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metricBox metricKey"><strong>A#</strong><br><span class="metricValue">{df[df["key"] == "A#"].shape[0]}</span></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metricBox metricKey"><strong>B</strong><br><span class="metricValue">{df[df["key"] == "B"].shape[0]}</span></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="metricBox metricKey"><strong>C</strong><br><span class="metricValue">{df[df["key"] == "C"].shape[0]}</span></div>', unsafe_allow_html=True)
    with col5:
        st.markdown(f'<div class="metricBox metricKey"><strong>C#</strong><br><span class="metricValue">{df[df["key"] == "C#"].shape[0]}</span></div>', unsafe_allow_html=True)
    with col6:
        st.markdown(f'<div class="metricBox metricKey"><strong>D</strong><br><span class="metricValue">{df[df["key"] == "D"].shape[0]}</span></div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.markdown(f'<div class="metricBox metricKey"><strong>D#</strong><br><span class="metricValue">{df[df["key"] == "D#"].shape[0]}</span></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metricBox metricKey"><strong>E</strong><br><span class="metricValue">{df[df["key"] == "E"].shape[0]}</span></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metricBox metricKey"><strong>F</strong><br><span class="metricValue">{df[df["key"] == "F"].shape[0]}</span></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="metricBox metricKey"><strong>F#</strong><br><span class="metricValue">{df[df["key"] == "F#"].shape[0]}</span></div>', unsafe_allow_html=True)
    with col5:
        st.markdown(f'<div class="metricBox metricKey"><strong>G</strong><br><span class="metricValue">{df[df["key"] == "G"].shape[0]}</span></div>', unsafe_allow_html=True)
    with col6:
        st.markdown(f'<div class="metricBox metricKey"><strong>G#</strong><br><span class="metricValue">{df[df["key"] == "G#"].shape[0]}</span></div>', unsafe_allow_html=True)
        
    