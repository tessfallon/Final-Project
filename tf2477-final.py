# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:43:41 2020

@author: tessf
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Hello():
    return render_template('index.html')

@app.route('/1006')
def _1006_():
    return render_template('1006.html')

@app.route('/columbia')
def columbia():
    return "Columbia!!"


if __name__ == '__main__':
    app.run()