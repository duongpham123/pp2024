import zipfile
import os

def compress_data():
    with zipfile.ZipFile("student.dat", "w") as zipf:
        zipf.write("C:\\Users\\DaiPQ\\pp2024\\pw5\\student.txt", "student.txt")
        zipf.write("C:\\Users\\DaiPQ\\pp2024\\pw5\\course.txt","course.txt")
        zipf.write("C:\\Users\\DaiPQ\\pp2024\\pw5\\mark.txt","mark.txt")
    
def decompress_data():
    with zipfile.ZipFile ("student.dat","r") as zipf:
        zipf.extractall()
        
def check_data_file():
    return "student.dat" in os.listdir()