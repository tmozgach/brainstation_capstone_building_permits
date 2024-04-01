import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
import datetime
from sklearn.preprocessing import RobustScaler
import math

nltk.download('wordnet')
nltk.download('punkt')

# Initialize Porter Stemmer and WordNet Lemmatizer
stemmer = nltk.stem.PorterStemmer()
lemm = WordNetLemmatizer()

# Define English stopwords
ENGLISH_STOP_WORDS = set(stopwords.words('english'))

def my_tokenizer(sentence):
    # Replace newline characters with spaces
    sentence = sentence.replace('\r', ' ').replace('\n', ' ')
    
    # Remove punctuation marks and digits
    sentence = sentence.translate(str.maketrans('', '', string.punctuation + string.digits))
    
    # Tokenize the sentence
    listofwords = sentence.split(' ')
    
    # Initialize lists to store lemmatized and stemmed words
    listoflemmatize_words = []
    listofstemmed_words = []
    
    # Lemmatize each word and remove stopwords
    for word in listofwords:
        if word.lower() not in ENGLISH_STOP_WORDS and word != '':
            lemmatized_word = lemm.lemmatize(word, pos='v')  # Lemmatize verb forms
            listoflemmatize_words.append(lemmatized_word)
    
    # Stem each lemmatized word
    for word in listoflemmatize_words:
        stemmed_word = stemmer.stem(word)
        listofstemmed_words.append(stemmed_word)
    
    return listofstemmed_words


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

# Load the models from the file
with open('models/model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('models/bagofwords_ap_model.pkl', 'rb') as file:
    bagofwords_ap = pickle.load(file)

with open('models/bagofwords_pr_model.pkl', 'rb') as file:
    bagofwords_pr = pickle.load(file)
    
with open('models/robust_scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

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

st.title("Estimated Timeline for Building Permit Approval in Vancouver")

# Generate encoded DataFrames for each input
type_of_work_df = generate_encoded_df("Type Of Work", type_of_work_options, 'x0_')
property_use_df = generate_encoded_df("Property Use", property_use_options, 'x1_')
specific_use_category_df = generate_encoded_df("Specific Use Category", specific_use_category_options, 'x2_')
area_df = generate_encoded_df("Area", area_options, 'x3_')

today = datetime.date.today()
date = st.date_input("Date of Application", value=today)

# Create Pandas Series for various input fields including month, project value, project description, applicant, latitude, and longitude
month = pd.Series([date.month], name='Month')

# Calculate the sine and cosine of the month to encode cyclic behavior
month_sin = pd.Series([np.sin(2 * np.pi * month / 12)], name='Month_sin')
month_cos = pd.Series([np.cos(2 * np.pi * month / 12)], name='Month_cos')

project_value = pd.Series([st.number_input("Project Value (in dollars)", value=0)], name='ProjectValue')
project_description = pd.Series([st.text_area("Project Description (optional)")], name='ProjectDescription')
applicant = pd.Series([st.text_input("Applicant (optional)")], name='Applicant')
latitude = pd.Series([st.number_input("Latitude")], name='Latitude')
longitude = pd.Series([st.number_input("Longitude")], name='Longitude')

# Create a button to trigger predictions
predict_button = st.button('Calculate', key='predict_button')

if predict_button:
    # Combine all encoded features
    all_features = pd.concat([project_value, project_description, applicant, month_sin, month_cos,latitude,longitude, type_of_work_df, property_use_df, specific_use_category_df, area_df], axis=1)

    # Transform the 'ProjectDescription' text data into a bag-of-words representation using the 'bagofwords_pr' model
    X_test_pr = bagofwords_pr.transform(all_features["ProjectDescription"])
    
    # Drop the column
    columns_to_drop = ['ProjectDescription']

    # Drop multiple columns in-place
    all_features.drop(columns=columns_to_drop, inplace=True)

    # Add the prefix pd for ProjectDescription for columns
    cols = [f'pd_{word}' for word in bagofwords_pr.get_feature_names()]
    
    # Join the original test dataset and positive bag of words.
    X_test_pr = pd.DataFrame(columns=cols, data=X_test_pr.toarray())
    X_test_extended_with_pr = pd.concat([all_features, X_test_pr], axis=1)

    # Transform the 'Applicant' text data into a bag-of-words representation using the 'bagofwords_pr' model
    X_test_ap = bagofwords_ap.transform(X_test_extended_with_pr["Applicant"])
    
    # Drop the column
    columns_to_drop = ['Applicant']

    # Drop multiple columns in-place
    X_test_extended_with_pr.drop(columns=columns_to_drop, inplace=True)

    # Add the prefix ap for Applicant for columns
    cols = [f'ap_{word}' for word in bagofwords_ap.get_feature_names()]
    
    # Join the original test dataset and positive bag of words.
    X_test_ap = pd.DataFrame(columns=cols, data=X_test_ap.toarray())
    X_test_extended_with_ap = pd.concat([X_test_extended_with_pr, X_test_ap], axis=1)

    X_test_s = scaler.transform(X_test_extended_with_ap)

    # Make predictions
    prediction = model.predict(X_test_s)

    st.write('Estimated timeline:', math.ceil(prediction[0]), ' days')