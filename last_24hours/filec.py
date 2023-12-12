import os
import shutil
from datetime import datetime, timedelta

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def is_recently_modified(file_path):
    threshold_time = datetime.now() - timedelta(days=1)
    stat_info = os.stat(file_path)
    return datetime.fromtimestamp(stat_info.st_mtime) > threshold_time or datetime.fromtimestamp(stat_info.st_ctime) > threshold_time

def update_files(files):
    for file_name in files:
        file_path = os.path.join(os.getcwd(), file_name)
        with open(file_path, 'a') as file:
            file.write('\nUpdated at: ' + str(datetime.now()))

def create_last_24hours_folder():
    folder_name = 'last_24hours'
    folder_path = os.path.join(os.getcwd(), folder_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

def move_files(files):
    folder_name = 'last_24hours'
    for file_name in files:
        source_path = os.path.join(os.getcwd(), file_name)
        destination_path = os.path.join(os.getcwd(), folder_name, file_name)
        shutil.move(source_path, destination_path)

def main():
    current_directory = os.getcwd()

    
    files = list_files(current_directory)

 
    recent_files = [file for file in files if is_recently_modified(file)]

    if recent_files:
        
        update_files(recent_files)

       
        create_last_24hours_folder()

       
        move_files(recent_files)
        print("Files updated and moved to 'last_24hours' folder.")
    else:
        print("No files modified or created in the last 24 hours.")

if __name__ == "__main__":
    main()
Updated at: 2023-12-12 22:06:33.718716