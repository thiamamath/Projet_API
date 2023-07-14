import streamlit as st

st.title("Tableau de bord: PyThiam")
st.write("Welcom to my application !")

#Chargement des bases
import pandas as pd
impress = pd.read_csv("impressions.csv")
clics= pd.read_csv("clics.csv")
achat= pd.read_csv("achats.csv")

# jointure des bases
imp_clic=pd.merge(impress, clics, on='cookie_id')
imp_clic_achat=pd.merge(imp_clic, achat, on='cookie_id')
imp_clic_achat

#Route de l'API
#app=Flask(__name__)
#@app.route('/api/imp_clic_achat', methods=['GET'])
#def get_imp_clic_achat():
    #return jsonify(imp_clic_achat)

from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/imp_clic_achat', methods=['GET'])
def get_imp_clic_achat():
    return jsonify(imp_clic_achat)



#Chiffre d'affaire
chiffre_affaires =imp_clic_achat['price'].sum()
#st.write(f"Chiffre d'affaires : {chiffre_affaires} €")
st.write(f"<span style ='color:red; font-size:40px;'>Chiffre d'affaires:{chiffre_affaires} € </span>", unsafe_allow_html=True)

#Histogramme
import plotly.express as px
st.subheader('Prix en fonction du produit')
histo=px.histogram(imp_clic_achat, x='product_id', y='price')
st.plotly_chart(histo)

#boxplot
st.subheader('Age en fonction des produit')
box=px.box(imp_clic_achat, x='product_id', y='age')
st.plotly_chart(box)

#diagrammme circulaire
st.subheader('Répartition de la dépense par tête suivant le sexe')
circulaire=px.pie(imp_clic_achat, values='dept', names='gender')
st.plotly_chart(circulaire)



