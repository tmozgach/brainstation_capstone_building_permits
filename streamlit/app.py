# conda install streamlit , scikit-learn , pandas , matplotlib
import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

def generate_encoded_df(label, options, prefix):
    # UI input
    selected_option = st.selectbox(label, options=options, key=label)

    # Create DataFrame with dummy variables
    encoded_df = pd.DataFrame(np.zeros((1, len(options))), columns=options)

    # Set value for the selected option to 1
    encoded_df.loc[0, selected_option] = 1

    # Add prefix 'x0' to column names
    encoded_df.columns = [prefix + col for col in encoded_df.columns]

    return encoded_df

# Define options for each input
type_of_work_options = ['New Building', 'Salvage and Abatement', 'Addition / Alteration',
                        'Demolition / Deconstruction', 'Temporary Building / Structure',
                        'Outdoor Uses (No Buildings Proposed)']

property_use_options = ['Dwelling Uses', 'Office Uses', 'Institutional Uses',
                        'Service Uses', 'Retail Uses', 'Parking Uses',
                        'Manufacturing Uses', 'Cultural/Recreational Uses',
                        'Wholesale Uses', 'Transportation and Storage Uses',
                        'Office Uses,Retail Uses', 'Dwelling Uses,Retail Uses', 'Others']

specific_use_category_options = ['Laneway House', 'Single Detached House',
                                 'Single Detached House w/Sec Suite', 'General Office', 'Others',
                                 'Multiple Dwelling', 'Duplex', 'Retail Store', 'Dwelling Unit',
                                 'Multiple Conversion Dwelling', 'Hospital', 'Restaurant - Class 1',
                                 'Barber Shop or Beauty Salon', 'Health Care Office',
                                 'School - University or College', 'Financial Institution',
                                 'Park or Playground', 'Beauty and Wellness Centre',
                                 'Not Applicable', 'Infill Single Detached House',
                                 'School - Elementary or Secondary', 'Duplex w/Secondary Suite',
                                 'Wholesaling - Class A']

area_options = ['Victoria-Fraserview', 'Kensington-Cedar Cottage', 'Oakridge',
                'Sunset', 'Kitsilano', 'West End', 'Mount Pleasant', 'Kerrisdale',
                'West Point Grey', 'Dunbar-Southlands', 'Downtown', 'Riley Park',
                'Fairview', 'Marpole', 'Renfrew-Collingwood', 'Arbutus Ridge',
                'Strathcona', 'Hastings-Sunrise', 'Shaughnessy', 'Killarney',
                'Grandview-Woodland', 'South Cambie']

# Generate encoded DataFrames for each input
type_of_work_df = generate_encoded_df("Type Of Work", type_of_work_options, 'x0_')
property_use_df = generate_encoded_df("Property Use", property_use_options, 'x1_')
specific_use_category_df = generate_encoded_df("Specific Use Category", specific_use_category_options, 'x2_')
area_df = generate_encoded_df("Area", area_options, 'x3_')

# Display encoded DataFrames
st.subheader("Encoded Features - Type Of Work:")
st.write(type_of_work_df)

st.subheader("Encoded Features - Property Use:")
st.write(property_use_df)

st.subheader("Encoded Features - Specific Use Category:")
st.write(specific_use_category_df)

st.subheader("Encoded Features - Area:")
st.write(area_df)


project_value = st.number_input("Project Value (in dollars)", value=0)

applicant = st.text_input("Applicant (optional)")

project_description = st.text_area("Project Description (optional)")

latitude = st.number_input("Latitude")

longitude = st.number_input("Longitude")

# Combine all encoded features
all_features = pd.concat([type_of_work_df, property_use_df, specific_use_category_df, area_df], axis=1)


# Fill missing values
all_features.fillna(0, inplace=True)

st.subheader("Features for Prediction:")
st.write(all_features)


