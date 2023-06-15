#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 18:04:08 2022

@author: bunty
"""

import numpy as np 
import pickle            # for loading the saved model 
import streamlit as st   # for creating the web page




loaded_model = pickle.load(open('./trained_model.sav', 'rb'))

def predict_sentiment(text):
    tw = Tokenizer.texts_to_sequences([text])
    tw = pad_sequences(tw,maxlen=200)
    prediction = int(model.predict(tw).round().item())
    print("Predicted label: ", sentiment_label[1][prediction])
    print(prediction)
    
    return prediction



def main():
    #giving title to web page 
    st.title('Twitter Sentiment Analysis') 
    
    #getting text from the user
    tweet = st.text_input('Enter Twitter text')

    #code for Prediction
    diagnosis = ''

    #creating a button for predicton analysis
    if st.button('Prediction :'):
        diagnosis = predict_sentiment([tweet])
    
    st.success(diagnosis)



if __name__ == '__main__': 
    main() 