import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import pickle
from PIL import Image
import time


# Appel à l'API pour récupérer les informations de vol
url = "https://imagedockerfu.azurewebsites.net/"
response = requests.get(url)
flights = response.json()
url1 = "https://imagedockerfu.azurewebsites.net/predict"


# Fonction pour la page "Ajouter"
def add_page():
    st.title("Caracteristique fleurale des iris")

    # Créer des widgets pour les mesures de la fleur
    sepal_length = st.number_input("Longueur du sépale", value=5.7, step=0.1)
    sepal_width = st.number_input("Largeur du sépale", value=3.1, step=0.1)
    petal_length = st.number_input("Longueur du pétale", value=4.9, step=0.1)
    petal_width = st.number_input("Largeur du pétale", value=2.2, step=0.1)



    if st.button("Ajouter Fleur", key="ajouter_fleur_button"):
        iris_data = {
                "sepal_length": sepal_length ,
                "sepal_width":sepal_width,
                "petal_length":petal_length,
                "petal_width":petal_width
            }

            # Envoyer les données à l'API
        response = requests.post(url1, json=iris_data)
            # Vérifier si la requête a réussi
        if response.ok:
                with st.spinner('Wait for it...'):
                    time.sleep(2)
                st.success("Les informations de votre fleur ont été ajouté avec succès !")
                prediction = response.json()['prediction']
                st.write(f'cette fleur est une iris: {prediction}')
                probability = response.json()['probability']
                st.write(f'Precision de la prediction : {probability} %')
        else:
                st.error("Erreur lors de l'ajout des informations de votre fleur.")

# Fonction pour la page "Métriques"
def metrics_page():
    st.title("Graphes")

#---------------------  Sidebar  ----------------------#
# Menu déroulant pour sélectionner la page à afficher
menu = ["iris", "Graphes"]
choice = st.sidebar.selectbox(" ", menu)

# Affichage de la page correspondant à la sélection du menu
if choice == "iris":
    add_page()
else:
    metrics_page()