# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 01:47:14 2019

@author: KRISHNA
"""

def predictSentiment(inReview,loadModel):
    ## first vectorizer,model
    vector,model = loadModel
    pred = model.predict(vector.transform([inReview]))[0]
    return pred
