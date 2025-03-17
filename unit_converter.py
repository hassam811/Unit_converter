import streamlit as st   # streamlit is a library for building web app

# function to convert units based on predefined conversion factors or farmulas
def convert_units(value, unit_from, unit_to):

    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000
    }


    key = f"{unit_from}_{unit_to}"  # generate a key based on the input and output units
    
    # logic to convert units
    if key in conversions:
        conversions = conversions[key]
        return value * conversions
    else: 
        return "conversion not supported" # return a massege if the conversion is not supported
    
st.title("unit converter")  # set the title of the web app

# user input: numerical value to convert
value = st.number_input("Enter the value:", min_value=1.0, step=1.0)

# dropdown to select unit to convert from
unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])

# dropdown to select unit to convert to
unit_to = st.selectbox("convert to:", ["meters", "kilometers", "grams", "kilograms"])

#  button to trigger the conversion
if st.button("convert"):
    result = convert_units(value, unit_from, unit_to) #call the conversion function
    st.write(f"converted value{result}")
    