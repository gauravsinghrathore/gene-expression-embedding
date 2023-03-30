from flask import Flask, render_template, request
import scanpy as sc
import pandas as pd

# load adata
adata = sc.read('path/to/adata.h5ad')

# create Flask app
app = Flask(__name__)

# define homepage
@app.route('/')
def index
