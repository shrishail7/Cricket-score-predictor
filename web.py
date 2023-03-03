import pickle
import numpy as np
import pandas as pd
import streamlit as st
import xgboost

pipe = pickle.load(open('train.pkl','rb'))

teams = ['South Africa', 'India', 'Pakistan', 'West Indies', 'New Zealand',
       'Australia', 'England', 'Afghanistan', 'Sri Lanka', 'Bangladesh']

city = ['Port Elizabeth', 'Durban', 'St Lucia', 'Nottingham', 'Dharmasala',
       'Mount Maunganui', 'Sydney', 'Johannesburg', 'St Kitts',
       'Chandigarh', 'Colombo', 'Basseterre', 'Jamaica', 'Bloemfontein',
       'Dhaka', 'Bristol', 'Wellington', 'Dubai', 'Hobart', 'Kanpur',
       'Cardiff', 'London', 'Victoria', 'Mirpur', 'Napier', 'Lucknow',
       'Chittagong', 'Adelaide', 'Barbados', 'Auckland', 'Pune',
       'Cape Town', 'Birmingham', 'Perth', 'Southampton', 'Centurion',
       'Christchurch', 'Nagpur', 'Brisbane', 'Trinidad', 'Karachi',
       'Hamilton', 'Harare', 'Rajkot', 'Chennai', 'Lauderhill',
       'Bangalore', 'Cuttack', 'Lahore', 'Manchester', 'Mumbai', 'Delhi',
       'Providence', 'Hambantota', 'Pallekele', 'King City', 'Antigua',
       'St Vincent', 'Melbourne', 'Carrara', 'Abu Dhabi', 'Dehradun',
       'Hyderabad', 'Nairobi', 'Guyana', 'Ranchi', 'Nelson', 'Bengaluru',
       'Visakhapatnam', 'Kolkata', 'Chester-le-Street', 'Canberra',
       'East London', 'Kandy', 'Ahmedabad', 'Thiruvananthapuram',
       'Sylhet', 'Potchefstroom', 'Indore', 'Gros Islet', 'Dharamsala',
       'Dominica', 'Sharjah', 'Chattogram', 'Paarl', 'Taunton']

st.title("First Innings Score Predictor for T20 International Cricket Matches")

col1,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select Batting team",sorted(teams))

with col2:
    bowling_team = st.selectbox("Select Bowling team",sorted(teams))

city = st.selectbox("Select City" , sorted(city))

col3,col4,col5 = st.columns(3)

with col3 :
    curr_score = st.number_input("Current Score")

with col4 :
    over_done = st.number_input("Over done (works for over > 5)")

with col5:
    wickets = st.number_input("Wickets")

last_five = st.number_input("Run scored in previous five overs")

if st.button('Predict'):
    balls_left = 120 - (over_done*6)
    wickets_left = 10 - wickets
    crr = curr_score/over_done

    input_df = pd.DataFrame(
        {'batting_team': [batting_team], 'bowling_team': [bowling_team],'current_score': [curr_score],
         'balls_left': [balls_left], 'wickets_left': [wickets_left], 'crr': [crr], 'last_five': [last_five], 'city': [city]})
    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))


