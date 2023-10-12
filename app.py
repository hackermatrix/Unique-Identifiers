# from mitra import main
import hashlib
from text2img import create_img
import os

user = input("Enter the employee Name: ")
file_path = input("Enter the file path: ")


combine_file_path = './files/combine.png'
hash = hashlib.md5((user).encode('utf-8')).hexdigest()
create_img(hash,combine_file_path)


import subprocess
subprocess.run(['python3','./mitra/mitra.py','./files/combine.png',file_path],stdout=None)

print("COMBINE DONE!!!\n\n\n\n\n")


current_directory = os.getcwd()

for filename in os.listdir(current_directory):

    if filename.lower().endswith(".pdf"):

        new_filename = hash+'.pdf'

        current_file = os.path.join(current_directory, filename)
        new_file = os.path.join(current_directory, new_filename)

        # Rename the file
        try:
            os.rename(current_file, new_file)
            # print(f"Renamed {filename} to {new_filename}")
        except OSError as e:
            print(f"Error renaming {filename}: {str(e)}")


print(f"VERIFY {user}:{hash}")



