import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import streamlit as st

st.set_page_config(page_title="Automated Bug Detection",layout="centered")


# Function to tokenize and preprocess code snippets
def preprocess_code(code_snippet):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([code_snippet])
    sequence = tokenizer.texts_to_sequences([code_snippet])
    max_length = max([len(seq) for seq in sequence])
    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding='post', truncating='post')# Set max_length as needed
    return padded_sequence

# Load the model trained for bug classification
model = tf.keras.models.load_model(r"C:\Users\simra\Desktop\Projects\Bug Detection\cnn_model.h5")

# Function to predict the bug type
def code_prediction(code_snippet):
    preprocessed_code = preprocess_code(code_snippet)
    prediction = model.predict(preprocessed_code)
    predicted_class = np.argmax(prediction, axis=-1)[0]

    bug_types = ["NULL_DEREFERENCE", "RESOURCE_LEAK", "THREAD_SAFETY_VIOLATION"]
    predicted_bug_type = bug_types[predicted_class]
    return predicted_bug_type

# Streamlit UI
st.markdown("<h1 style='color: #0657b8;'>Automated Bug Detection</h1>", unsafe_allow_html=True)
code_input = st.text_area("Enter the code snippet:",height=200)
submit = st.button("Predict")

if submit:
    predicted_bug_type = code_prediction(code_input)
    st.markdown("<h2 style='color: #0657b8;'>Predicted Bug Type:</h2>", unsafe_allow_html=True)
    st.write(predicted_bug_type)
st.markdown("<h7 style='color: #0657b8;'>Made by: Simran Gurung @2024 </h7>", unsafe_allow_html=True)
   