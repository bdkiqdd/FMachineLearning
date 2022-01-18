# Deploy with Streamlit

# imports
from ctypes import alignment
from statistics import mode
import time
import numpy as np
import pandas as pd
import streamlit as st
import sklearn.metrics
import sklearn.datasets
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

## Streamlit web app

# Title

st.write("*Formação Engenheiro de ML*")
st.write("*Deploy with Streamlit*")
st.title("Linear Regression")

## Streamlit Sidebar
# Information Side Bar

st.sidebar.header('Dataset and Hyperparemeters')
st.sidebar.markdown("""**Select your dataset**""")
Dataset = st.sidebar.selectbox('Dataset',('Iris','Wine','Breast Cancer'))
Split = st.sidebar.slider('Train and Test division (Default = 0.7/0.3):',0.1,0.9,0.70)
st.sidebar.markdown("""**Select some hyperparameters to Linear Regression Model**""")
Solver = st.sidebar.selectbox('Algorithm',('lbfgs','newton-cg','liblinear','sag'))
Penalty = st.sidebar.radio('Regularization: ',('none','l1','l2','elasticnet'))
Tol = st.sidebar.text_input('Stop Criterion Tolerance (Default = 1e-4) :',"1e-4")
Max_interation = st.sidebar.text_input('Interation number (Default = 50) :','50')

# Hyperparemeters dict
parameters = {'Penalty': Penalty,'Tol':Tol,'Max_iteration':Max_interation,'Solver':Solver}

## Def to use data
# Def to data load
def data_load(dataset):
    if dataset == 'Iris':
        data = sklearn.datasets.load_iris()
    elif dataset == 'Wine':
        data = sklearn.datasets.load_wine()
    elif dataset == 'Breast Cancer':
        data = sklearn.datasets.load_breast_cancer()
    return data

# Def to preaper data
def data_processing(data,split):

    # Train and test split
    X_train,X_test,Y_train,Y_test = train_test_split(data.data,data.target,test_size=float(split),random_state=42)

    # Scaler preaper 
    scaler = MinMaxScaler()

    # Fit and tranform train data
    X_train = scaler.fit_transform(X_train)

    # Transform on test data
    X_test = scaler.transform(X_test)

    return (X_train,X_test,Y_train,Y_test)

# Def to model construct

def model(parameters):

    # Train and Test data
    X_train,X_test,Y_train,Y_test = data_processing(Data,Split)

    # Creaing model
    model = LogisticRegression(penalty = parameters['Penalty']
                                ,solver= parameters['Solver']
                                ,max_iter= int(parameters['Max_iteration'])
                                ,tol= float(parameters['Tol']))

    # Training Model
    model.fit(X_train,Y_train)

    # Do predict
    predicted_y = model.predict(X_test)

    # Accuracy calc

    accuracy = sklearn.metrics.accuracy_score(Y_test,predicted_y)

    # Confusion matrix calc
    confusion = confusion_matrix(Y_test,predicted_y)

    # Results dict

    results = {
        'Model':model
        ,'Prediction':predicted_y
        ,'Confusion Matrix': confusion
        ,'Accuracy':accuracy
        ,'Y_real': Y_test
        ,'X_test': X_test
    }

    return(results)

### Streamlit body
# Data Resume
st.markdown("""Data Resume""")
st.write('Dataset name: ', Dataset)

# Load dataset

Data = data_load(Dataset)

# Targets extraction
targets = Data.target_names

# Preaper Dataframe

Dataframe = pd.DataFrame(Data.data, columns = Data.feature_names)
Dataframe['target'] = pd.Series(Data.target)
Dataframe['targets labels'] = pd.Series(targets[i] for i in Data.target)

# Show dataset on screen

st.write("Data Vision")
st.write(Dataframe)

## Button of model

if(st.sidebar.button('Train!')):
    
    ## Progression bar
    with st.spinner('Revising Dataset...'):
        time.sleep(1)

    # Success info
    st.success('Dataset revised')

    # Model
    model = model(parameters)

    # Progression Bar
    my_bar = st.progress(0)

    # Show conclusion percent on progression bar

    for percent_complet in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complet+1)

    # Info to user
    with st.spinner('Training model...'):
        time.sleep(1)

    # Success info
    st.success('Model trained')

    # Extract real labels
    real_labels = [targets[i] for i in model['Y_real']]

    # Extract predicted labels
    predicted_labels = [targets[i] for i in model['Prediction']]

    # Sub title
    st.subheader('Data test model predictions')

    # Show Results
    st.write(pd.DataFrame({"Real Value":model['Y_real']
                            ,"Real label": real_labels
                            ,"Predicted value":model['Prediction']
                            ,"Predicted label":predicted_labels}))
    
    # Metrics extration
    matrix = model["Confusion Matrix"]

    # Sub Title
    st.write("Confusion Matrix on test data", matrix)

    # Accuracy
    accuracy = model['Accuracy']
    
    # Show accuracy
    st.write('Model Accureacy',accuracy)

    st.write('Thank you for ur time!')