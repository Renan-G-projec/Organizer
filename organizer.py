from json import load # To parse the JSON data to a dictionary
from config import run_config # For running the config wizard if config.json was not found
from datetime import datetime # For parsing file's metadata
from shutil import move
import os


# Running the config file
if not os.path.exists("config.json"):
    run_config()

# Loading Data
config_file = open("config.json", "r")
config_data = load(config_file)
config_file.close()

# Colecting metadata
file_buffer = os.listdir("filebuffer")
file_buffer.pop(0) # pops at 0 for ignorating .gitkeep
file_buffer_adress = os.getcwd() + "/filebuffer"
file_buffer_dict = {}

for file in file_buffer:
    creation_time = datetime.fromtimestamp(os.stat(f"filebuffer/{file}").st_ctime)
    creation_time_array = [creation_time.year, creation_time.month, creation_time.day]
    file_buffer_dict[file] = creation_time_array

# Changing the current directory
os.chdir(config_data['path'])

# Iterating over each file to check folders
for file in file_buffer:
    year = file_buffer_dict[file][0]
    month = file_buffer_dict[file][1]
    day = file_buffer_dict[file][2]

    # Creating the folders if it does not exists
    if (not os.path.exists(str(year))):
        os.mkdir(str(year))

    if (not os.path.exists(str(year) + "/" + str(month))):
        os.mkdir(str(year) + "/" + str(month))

    # Moving the files
    starting_adress = file_buffer_adress + "/" + file
    destiny_adress = str(year) + "/" + str(month)
    move(starting_adress, destiny_adress)

    # Renaming the files
    extension = file.split(".")[-1]
    os.rename(f"{destiny_adress}/{file}", f"{destiny_adress}/{day}{config_data['sufix']}.{extension}")