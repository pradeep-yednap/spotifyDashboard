# SIDEBAR-YEAR        
import streamlit as st
import numpy as np   
def show_sidebar(df):
    st.sidebar.write("Filter:")

    # SIDEBAR-YEAR
    min_released_year = df['released_year'].min()
    max_released_year = df['released_year'].max()

    year_range = st.sidebar.slider("Year range:", min_released_year, max_released_year, (min_released_year, max_released_year))

    df = df[(df['released_year'] >= year_range[0]) & (df['released_year'] <= year_range[1])]
       

    # SIDEBAR-MONTH 
    month_name_list = ['All', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    sb_month_name = st.sidebar.selectbox("Month:", month_name_list, 0)
    
    if sb_month_name != 'All':
        sb_month = month_name_list.index(sb_month_name)
        df = df[df['released_month'] == sb_month]
    
    
    # SIDEBAR-MODE 
    sb_mode = st.sidebar.selectbox("Mode:", ['All'] + list(df['mode'].unique()))
    
    if sb_mode != 'All':
        df = df[df['mode'] == sb_mode]
    
    # SIDEBAR-KEY
    sb_key = st.sidebar.selectbox("Key:", ['All'] +  list(np.sort(df['key'].unique())))
    
    if sb_key != 'All':
        df = df[df['key'] == sb_key]
    
    # print("Select Year Range:",year_range)
    # print("Select Month:",sb_month_name)
    # print("Select Mode:",sb_mode)
    # print("Select Key:",sb_key)
    
    return df