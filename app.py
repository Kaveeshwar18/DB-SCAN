import streamlit as st
import pickle
import numpy as np

st.set_page_config(layout="wide")

# Load Model
model = pickle.load(open("kmeans_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ---------------- LUXURY CSS ---------------- #

st.markdown("""
<style>

.stApp {
    background-color: black;
}

/* Remove Streamlit padding */
.block-container {
    padding-top: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
}

/* HERO SECTION */
.hero {
    height: 100vh;
    background: linear-gradient(to right, rgba(0,0,0,0.9) 40%, rgba(0,0,0,0.4)),
                url("https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb");
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
    padding-left: 8%;
}

/* TEXT STYLING */
.hero-text h1 {
    font-size: 80px;
    color: white;
    font-family: serif;
}

.hero-text p {
    font-size: 24px;
    color: #c9a227;
    letter-spacing: 3px;
}

.hero-text button {
    margin-top: 20px;
    padding: 12px 30px;
    background-color: #c9a227;
    color: black;
    font-weight: bold;
    border: none;
    border-radius: 5px;
    transition: 0.3s;
}

.hero-text button:hover {
    background-color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ---------------- #

st.markdown("""
<div class="hero">
    <div class="hero-text">
        <p>INTRODUCING WINEFLIX</p>
        <h1>Refinement<br>in a bottle</h1>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- CONTENT SECTION ---------------- #

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<center><h2 style='color:#c9a227;'>Discover Your Wine Profile</h2></center>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    alcohol = st.number_input("Alcohol", 10.0, 15.0, 13.0)
    malic_acid = st.number_input("Malic Acid", 0.5, 5.0, 2.0)
    ash = st.number_input("Ash", 1.0, 3.5, 2.3)
    alcalinity = st.number_input("Alcalinity", 10.0, 30.0, 18.0)

with col2:
    magnesium = st.number_input("Magnesium", 70, 150, 100)
    total_phenols = st.number_input("Total Phenols", 0.5, 4.0, 2.5)
    flavanoids = st.number_input("Flavanoids", 0.1, 5.0, 2.0)
    nonflavanoid = st.number_input("Nonflavanoid Phenols", 0.1, 1.0, 0.3)

with col3:
    proanthocyanins = st.number_input("Proanthocyanins", 0.1, 4.0, 1.5)
    color_intensity = st.number_input("Color Intensity", 1.0, 15.0, 5.0)
    hue = st.number_input("Hue", 0.5, 2.0, 1.0)
    od280 = st.number_input("OD280/OD315", 1.0, 4.0, 2.5)
    proline = st.number_input("Proline", 200, 1700, 800)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("Reveal Category"):

    input_data = np.array([[alcohol, malic_acid, ash, alcalinity,
                            magnesium, total_phenols, flavanoids,
                            nonflavanoid, proanthocyanins,
                            color_intensity, hue, od280, proline]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    st.markdown("<center>", unsafe_allow_html=True)

    if prediction[0] == 0:
        st.image("https://images.unsplash.com/photo-1510626176961-4b57d4fbad03", width=300)
        st.success("Premium Red Wine")

    elif prediction[0] == 1:
        st.image("https://images.unsplash.com/photo-1524594154908-edd8e3d8e0b4", width=300)
        st.success("Classic White Wine")

    else:
        st.image("https://images.unsplash.com/photo-1604908177522-402de7ed0e77", width=300)
        st.success("Sparkling Wine")

    st.markdown("</center>", unsafe_allow_html=True)