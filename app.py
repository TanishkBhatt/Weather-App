import streamlit as st
from src.utils import fetch_data, plot_data

st.set_page_config(page_title="WEATHER APP")
st.title("WEATHER APP")
st.markdown("""
An **Python** based **Streamlit** supported Weather Application to Fetch and Plot some Insights of the Data Recived from the **OpenWeatherMap API**.
""")

with st.form(key='fetch_weather_data'):
    API_KEY: str = st.text_input("PUT YOUR OPENWEATHERMAP API KEY HERE")
    city: str = st.text_input("ENTER THE CITY NAME")
    submit: bool = st.form_submit_button("GET WEATHER DATA")

if submit:
    if not city.strip() and API_KEY.strip():
        st.warning("WARNING: ENTER THE DETAILS CAREFULLY")
    else:
        try:
            res = fetch_data(city, API_KEY)
            data = {
                "City": f"{res["name"]}",
                "Weather": f"{res["weather"][0]["main"]}",
                "Temperature": f"{res["main"]["temp"]} °C",
                "Feels Like": f"{res["main"]["feels_like"]} °C",
                "Humidity": f"{res["main"]["humidity"]} %",
                "Wind Speed": f"{res["wind"]["speed"]} m/s"
            }
            fig = plot_data(res)

        except Exception as error:
            st.error(f"ERROR: {error}")

        else:
            st.subheader("WEATHER REPORT")
            col1, col2 = st.columns(2)
            with col1:
                st.dataframe(data)
            with col2:
                st.pyplot(fig)

st.divider()
st.caption("MADE BY TANISHK - A STUDENT AND A PROGRAMMER")