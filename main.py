import streamlit as st

conversion_factors = {
    "Nautical mile": {"Kilometre": 1.852, "Metre": 1852, "Centimetre": 185200, "Millimetre": 1852000, "Micrometre": 1852000000, "Nanometre": 1852000000000, "Mile": 1.15078, "Yard": 2025.37, "Foot": 6076.12, "Inch": 72913.4},
    "Kilometre": {"Metre": 1000, "Centimetre": 100000, "Millimetre": 1000000, "Micrometre": 1000000000, "Nanometre": 1000000000000, "Mile": 0.621371, "Yard": 1093.61, "Foot": 3280.84, "Inch": 39370.1},
    "Metre": {"Kilometre": 0.001, "Centimetre": 100, "Millimetre": 1000, "Micrometre": 1000000, "Nanometre": 1000000000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701},
    "Centimetre": {"Metre": 0.01, "Kilometre": 0.00001, "Millimetre": 10, "Micrometre": 10000, "Nanometre": 10000000, "Mile": 0.00000621371, "Yard": 0.0109361, "Foot": 0.0328084, "Inch": 0.393701},
    "Millimetre": {"Metre": 0.001, "Kilometre": 0.000001, "Centimetre": 0.1, "Micrometre": 1000, "Nanometre": 1000000, "Mile": 0.000000621371, "Yard": 0.00109361, "Foot": 0.00328084, "Inch": 0.0393701},
    "Mile": {"Metre": 1609.34, "Kilometre": 1.60934, "Centimetre": 160934, "Millimetre": 1609340, "Micrometre": 1609340000, "Nanometre": 1609340000000, "Yard": 1760, "Foot": 5280, "Inch": 63360},
    "Foot": {"Metre": 0.3048, "Kilometre": 0.0003048, "Centimetre": 30.48, "Millimetre": 304.8, "Micrometre": 304800, "Nanometre": 304800000, "Mile": 0.000189394, "Yard": 0.333333, "Inch": 12},
    "Inch": {"Metre": 0.0254, "Kilometre": 0.0000254, "Centimetre": 2.54, "Millimetre": 25.4, "Micrometre": 25400, "Nanometre": 25400000, "Mile": 0.0000157828, "Yard": 0.0277778, "Foot": 0.0833333}
}

# Unit Descriptions
unit_info = {
    "Nautical mile": "Used in aviation & maritime navigation.",
    "Kilometre": "Commonly used for measuring road distances.",
    "Metre": "Standard unit of length in the metric system.",
    "Centimetre": "Used for small measurements like height & width.",
    "Millimetre": "Used for very small lengths, like paper thickness.",
    "Mile": "Mainly used in the US and UK for road distances.",
    "Foot": "Commonly used for measuring height & room dimensions.",
    "Inch": "Used in the US for screens, papers, & small objects."
}
def convert_length(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    return value * conversion_factors.get(from_unit, {}).get(to_unit, 1)

st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("Unit Converter📏")

value = st.number_input("Enter Value", min_value=0.0, value=1.0)
from_unit = st.selectbox("From", list(conversion_factors.keys()))
to_unit = st.selectbox("To", list(conversion_factors.keys()))

converted_value = convert_length(value, from_unit, to_unit)
st.success(f"✏ {value} {from_unit} = {converted_value} {to_unit}")

conversion_factor = conversion_factors.get(from_unit, {}).get(to_unit, 1)
if conversion_factor >= 1:
    formula = f"Multiply the length value by {conversion_factor}"
else:
    formula = f"Divide the length value by {1/conversion_factor}"

st.markdown(f"**Formula**: {formula}")

with st.expander("ℹ️ More about selected units"):
    st.write(f"**{from_unit}:** {unit_info.get(from_unit, 'No information available.')}")
    st.write(f"**{to_unit}:** {unit_info.get(to_unit, 'No information available.')}")