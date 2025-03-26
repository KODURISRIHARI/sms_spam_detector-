
import streamlit as st
import pickle

st.title("SMS is Spam or not")
# Load the saved model
loaded_model = pickle.load(open('/content/model.pkl','rb'))

# Create input fields for the four variables`
# SepalLengthCm = st.number_input("Enter Sepal Length (cm):")
# SepalWidthCm = st.number_input("Enter Sepal Width (cm):")
# PetalLengthCm = st.number_input("Enter Petal Length (cm):")
# PetalWidthCm = st.number_input("Enter Petal Width (cm):")
enter_text = st.text_input("Enter text :")

# Create a button to trigger prediction
if st.button("Predict"):
    pkl_file = open('/content/vector.pkl' , 'rb')
    cv = pickle.load(pkl_file)
    enter_text = [enter_text]  # Wrap in a list before transforming
    enter_text = cv.transform(enter_text)
    output = loaded_model.predict(enter_text)  # No need for [[ ]] here anymore
    # st.write(f"The predicted output is: {output[0]}")
    if output == 0:
      st.write("Not Spam")
    else:
      st.write("Spam")
