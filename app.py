import streamlit as st
import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier

st.write("Prototype Titanic Form - Pickle")

with st.form("my_form"):
    st.write("Inside the form")

    pClass = st.radio("Class Passanger", ["1", "2", "3"])

    age = st.number_input("Age", min_value=0)

    sibling = st.number_input("siblings", min_value=0)

    parch = st.number_input("parch", min_value=0)

    fare = st.number_input("Fare")

    sex = st.radio("Sex", ["male", "female"])

    embarked = st.radio("Embarked", ["Q", "S", "Other"])

    if sex == "male":
        sex = True
    else:
        sex = False

    if (embarked == "Q"):
        embarked_Q = True
        embarked_S = False
    elif (embarked == "S'"):
        embarked_Q = False
        embarked_S = True
    else:
        embarked_Q = False
        embarked_S = False

    data = {
        "Pclass": [pClass],
        "Age": [age],
        "SibSp": [sibling],
        "Parch": [parch],
        "Fare": [fare],
        "Sex_male": [sex],
        "Embarked_Q": [embarked_Q],
        "Embarked_S": [embarked_S]
    }
    user_input = pd.DataFrame(data)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        # Carregando o modelo
        with open('model_.pkl', 'rb') as f:
            loaded_model = pickle.load(f)

        st.write(loaded_model.predict(user_input))
