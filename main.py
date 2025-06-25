import plotly.express as px
import streamlit as st

from backend import get_data

st.title("Weather Forecast for the Next X Days")
st.set_page_config("wide")

place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days.")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)
        dates = [index["dt_txt"] for index in filtered_data]

        if option == "Temperature":
            temps = [index["main"]["temp"] / 10 for index in filtered_data]
            figure = px.line(x=dates, y=temps, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            conditions = [index["weather"][0]["main"] for index in filtered_data]
            num_columns = 8
            cols = st.columns(num_columns)
            for i, condition in enumerate(conditions):
                date = dates[i]
                i = i if i < 8 else i % 8
                with cols[i]:
                    match condition:
                        case "Clear":
                            st.image("images/clear.png", width=75, caption=date)
                        case "Clouds":
                            st.image("images/cloud.png", width=75, caption=date)
                        case "Rain":
                            st.image("images/rain.png", width=75, caption=date)
                        case "Snow":
                            st.image("images/snow.png", width=75, caption=date)
    except KeyError:
        st.text(f"{place} is not a valid city.", )
