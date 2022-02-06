# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 07:17:46 2022

@author: ACER
"""

from flask import Flask,render_template,request,redirect,url_for

import pandas as pd 

'''the CORS module is used to allow the server to send data which in turn permits the browser about
loading of resources'''
from flask_cors import CORS

'''json if used for handling the json files retrived from url while urllib is used to request for the file'''
import json
import urllib3

'''defines the root of the app'''
app= Flask(__name__,template_folder='template')
CORS(app)

'''default route '''
@app.route('/',methods = ['GET'])
def show_index_html():
    return render_template('form.html')

if __name__=='__main__':
    '''allowing debugging in real time so that flask app doesnt need to be restarted every time to reflect
    change made by changing the code'''
    app.debug=True
    '''running the flask app on localhost'''
    app.run(host='127.0.0.1',port=5000)