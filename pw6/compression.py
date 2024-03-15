import os
import pickle
import zipfile

def compress_data(data):
    with zipfile.ZipFile("data.pkl.zip", "w") as zipf:
        with zipf.open("data.pkl", "w") as f:
            pickle.dump(data, f)

def decompress_data():
    with zipfile.ZipFile("data.pkl.zip", "r") as zipf:
        with zipf.open("data.pkl", "r") as f:
            data = pickle.load(f)
    return data

def check_data_file():
    return "data.pkl.zip" in os.listdir()
