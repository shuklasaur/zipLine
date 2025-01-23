import glob
import os
import hashlib
import pandas as pd
 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, From the children of Planet Earth'

@app.route('/login')
def login():
    return 'login screen'

@app.route('/signup')
def signup():
    return 'signup screen.'

# directory = "."  #TODO: Modify Path before use
 
# print("app started")
# files_and_dirs = glob.glob(directory + "/**/*.*", recursive=True)
# files = [file for file in files_and_dirs if os.path.isfile(file)]
# hashSet = set()
# file_hash_dict = {}


# i = 0

# for file in files:
#     i = i + 1
#     print(file)
#     # print(open(file,'rb').read(1024*1024))
#     hashSet.add(hashlib.sha256(open(file, "rb").read(1024 * 1024)).hexdigest())
#     file_hash_dict[file] = (hashlib.sha256(open(file, "rb").read(1024 * 1024)).hexdigest())


# df = pd.DataFrame({"filename": file_hash_dict.keys(), "hash": file_hash_dict.values()})

# # print(df.hash.unique())
# print(df)

# print("app ended")

# # print(file_hash_dict)
