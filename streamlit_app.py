import streamlit as st
import geopandas as gpd


if __name__ == "__main__":
    st.set_page_config(page_title="Streamlit Template",
                    page_icon='✅',
                    initial_sidebar_state='collapsed')
    st.title('🔨 Streamlit Template')
    st.markdown("""
        This app is only a template for a new Streamlit project. <br>

        ---
        """, unsafe_allow_html=True)

    st.balloons()
    df = gpd.read_file('cities.geojson')
    df['lon'] = df.geometry.x  # extract longitude from geometry
    df['lat'] = df.geometry.y  # extract latitude from geometry
    df = df[['lon','lat']]  # only keep longitude and latitude
    st.write(df.head())  # show on table for testing only
    st.map(df)  # show on map
