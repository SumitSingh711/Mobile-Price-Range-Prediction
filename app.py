import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv('dataset.csv')

X = df.drop('price_range', axis=1)
y = df['price_range']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

preprocessor = joblib.load('preprocessor.joblib')
model = joblib.load('model.joblib')

cost_mapping = {
    0: 'Low cost',
    1: 'Medium cost',
    2: 'High cost',
    3: 'Very high cost'
}

# web application
st.set_page_config(
    page_title='Mobile Phone Price Predictor',
    page_icon='📱'
)
st.title("Mobile Phone Price Predictor")

st.info('This app predicts mobile phone price')

battery_power = st.number_input(
    "**Battery power** *(mAh)*",
    min_value=100,  # Minimum year
    max_value=2000,  # Maximum year
    value=1000,      # Default value
    step=10         # Step value
)

blue = st.selectbox(
     '**Bluetooth** *(Yes=1 or No=0)*',
     options=X_train.blue.unique()
)

clock_speed = st.number_input(
    "**Clock speed** *(GHz)*",
    min_value=0.5,  # Minimum year
    max_value=5.0,  # Maximum year
    value=3.0,      # Default value
    step=0.5       # Step value
)

dual_sim = st.selectbox(
     '**Dual sim** *(Yes=1 or No=0)*',
     options=X_train.dual_sim.unique()
)

fc = st.number_input(
    "**Front camera** *(MP)*",
    min_value=0,  # Minimum year
    max_value=40,  # Maximum year
    value=16,      # Default value
    step=2       # Step value
)

four_g = st.selectbox(
     '**4G** *(Yes=1 or No=0)*',
     options=X_train.four_g.unique()
)

int_memory = st.number_input(
    "**Internal memory** *(GB)*",
    min_value=2,  # Minimum year
    max_value=256,  # Maximum year
    value=32,      # Default value
    step=8         # Step value
)

m_dep = st.number_input(
    "**Mobile thickness** *(cm)*",
    min_value=0.1,  # Minimum year
    max_value=1.5,  # Maximum year
    value=0.5,      # Default value
    step=0.1       # Step value
)

mobile_wt = st.number_input(
    "**Mobile weight** *(gm)*",
    min_value=0,  # Minimum year
    max_value=250,  # Maximum year
    value=100,      # Default value
    step=5       # Step value
)

n_cores = st.number_input(
    "**Number of cores**",
    min_value=0,  # Minimum year
    max_value=8,  # Maximum year
    value=4,      # Default value
    step=2       # Step value
)

pc = st.number_input(
    "**Rear camera** *(MP)*",
    min_value=0,  # Minimum year
    max_value=40,  # Maximum year
    value=16,      # Default value
    step=2       # Step value
)

px_height = st.number_input(
    "**Pixel resolution height**",
    min_value=0,  # Minimum year
    max_value=2000,  # Maximum year
    value=500,      # Default value
    step=50       # Step value
)

px_width = st.number_input(
    "**Pixel resolution width**",
    min_value=300,  # Minimum year
    max_value=2000,  # Maximum year
    value=500,      # Default value
    step=50       # Step value
)

ram = st.number_input(
    "**RAM** *(MB)*",
    min_value=256,  # Minimum year
    max_value=4000,  # Maximum year
    value=500,      # Default value
    step=50       # Step value
)

sc_h = st.number_input(
    "**Mobile screen height** *(cm)*",
    min_value=5,  # Minimum year
    max_value=20,  # Maximum year
    value=10,      # Default value
    step=2       # Step value
)

sc_w = st.number_input(
    "**Mobile screen width** *(cm)*",
    min_value=0,  # Minimum year
    max_value=20,  # Maximum year
    value=10,      # Default value
    step=2       # Step value
)

talk_time = st.number_input(
    "**Battery life** *(hours)*",
    min_value=2,  # Minimum year
    max_value=20,  # Maximum year
    value=10,      # Default value
    step=2       # Step value
)

three_g = st.selectbox(
     '**3G** *(Yes=1 or No=0)*',
     options=X_train.three_g.unique()
)

touch_screen = st.selectbox(
     '**Touch screen** *(Yes=1 or No=0)*',
     options=X_train.touch_screen.unique()
)

wifi = st.selectbox(
     '**Wifi** *(Yes=1 or No=0)*',
     options=X_train.wifi.unique()
)

X_new = pd.DataFrame(dict(
	battery_power = [battery_power],
	blue = [blue],
	clock_speed	=[clock_speed],
	dual_sim=[dual_sim],
	fc=[fc],
    four_g = [four_g],
	int_memory = [int_memory],
	m_dep	=[m_dep],
	mobile_wt=[mobile_wt],
	n_cores=[n_cores],
    pc = [pc],
	px_height = [px_height],
	px_width	=[px_width],
	ram=[ram],
	sc_h=[sc_h],
    sc_w = [sc_w],
	talk_time = [talk_time],
	three_g	=[three_g],
	touch_screen=[touch_screen],
	wifi=[wifi]
))


if st.button('Predict Price Range'):

    scaled = preprocessor.transform(X_new)
    pred = model.predict(scaled)

    cost_category = cost_mapping[pred[0]]

    st.success(f"The predicted mobile phone cost category is: **{cost_category}**")

