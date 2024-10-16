import streamlit as st
from datetime import datetime, timedelta
st.title("Welcome to this Milestone Calculator")
st.write("By Vincent")
# Function to calculate astrology sign based on the date of birth
def get_astrology_sign(birthdate):
    month = birthdate.month
    day = birthdate.day

    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return 'Capricorn'
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return 'Aquarius'
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return 'Pisces'
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return 'Aries'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return 'Taurus'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return 'Gemini'
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return 'Cancer'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return 'Leo'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return 'Virgo'
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return 'Libra'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return 'Scorpio'
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return 'Sagittarius'

# Function to calculate age and important day milestones
def calculate_milestones(birthdate):
    today = datetime.today().date()  # Convert datetime to date
    age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    days_alive = (today - birthdate).days  # Subtract date from date

    milestones = {
        '1000th day': birthdate + timedelta(days=1000),
        '5000th day': birthdate + timedelta(days=5000),
        '10000th day': birthdate + timedelta(days=10000),
        '30000th day': birthdate + timedelta(days=30000),
    }

    return age_years, days_alive, milestones

# Streamlit app title
st.title("Personal Milestones & Astrology App")

# Colors and layout customization
st.markdown(
    """
    <style>
    .big-font {font-size:20px !important; color: #2A9D8F;}
    .button { background-color: #264653; color: white; padding: 10px 20px; border-radius: 10px; }
    .highlight { background-color: #E9C46A; color: #264653; padding: 5px 10px; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# Collect user's name
name = st.text_input("Enter your name:")

# Calendar input for birthdate with expanded date range (since 1900)
birthdate = st.date_input(
    "Select your date of birth:", 
    min_value=datetime(1900, 1, 1), 
    max_value=datetime.today()
)

# Confirmation button to proceed
if st.button("OK"):
    if name and birthdate:
        # Calculate age and milestones
        age, days_alive, milestones = calculate_milestones(birthdate)
        astrology_sign = get_astrology_sign(birthdate)

        # Display user info with some colors
        st.write(f"Hello, <span class='highlight'>{name}</span>!", unsafe_allow_html=True)
        st.write(f"Your age is: <span class='big-font'>{age} years</span>", unsafe_allow_html=True)
        st.write(f"You have been alive for: <span class='big-font'>{days_alive} days</span>", unsafe_allow_html=True)
        st.write(f"Your astrology sign is: <span class='highlight'>{astrology_sign}</span>", unsafe_allow_html=True)

        # Display important milestones
        st.write("### Your Day Milestones:")
        for milestone, date in milestones.items():
            st.write(f"Your {milestone}: **{date.strftime('%Y-%m-%d')}**")
    else:
        st.warning("Please enter both your name and date of birth.")

