import streamlit as st
import xgboost as xgb
import numpy as np
from xgboost.sklearn import XGBClassifier


st.title("Fraud Detection in Digital Banks")
st.subheader("This is an interactive dashboard which utilizes ML algorithms to predict Fraud. ")

with st.form("form1",clear_on_submit=True):

    st.write("Choose the transaction type ")
    option = st.selectbox('',('CASH_OUT','PAYMENT','CASH_IN','TRANSFER','DEBIT'))

    dict = {'CASH_OUT':1,'PAYMENT':2,'CASH_IN':3,'TRANSFER':4,'DEBIT':5}
    feature1 = dict[option]

    
    st.write("Enter the amount of transaction ")
    feature2 = (st.text_input("",key="val2",value=0))

    st.write("Enter the balance before transaction ")
    feature3 = (st.text_input("",key="val3",value=0))

    st.write("Enter the the balance after transaction ")
    feature4 = (st.text_input("",key="val4",value=0))

    st.write("Enter the amount of recipient before transaction ")
    feature5 = (st.text_input("",key="val5",value=0))

    st.write("Enter the amount of recipient after transaction ")
    feature6 = (st.text_input("",key="val6",value=0))

    submit = st.form_submit_button("\n\nSubmit this form")

    if submit:
        xgb_model = XGBClassifier()
        xgb_model.load_model("model.h5")
        X = np.array([[feature1,int(feature2),int(feature3),int(feature4),int(feature5),int(feature6)]])
        val = xgb_model.predict(X)[0]
        if val == 1:
            st.error("WARNING : POSSIBILITY OF FRAUD.")
        if val == 0:
            st.subheader("NO FRAUD DETECTED.")
        
    








