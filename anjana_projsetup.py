

''' This module provides functions for creating a series of project folders. '''

import pathlib
import time
project_path = pathlib.Path.cwd()

print( "my project path is " + str(project_path))


def delete_empty_folders():
    '''Delete all empty folders from the working directory.'''
    # Create a Path object for the current working directory
    project_path = pathlib.Path.cwd()

    # Iterate through each item in the directory
    for item in project_path.iterdir():
        # Check if item is a directory and empty
        if item.is_dir() and not any(item.iterdir()):
            # Delete the empty folder
            item.rmdir()
            print(f"Empty folder deleted: {item}")

# Call the function to delete empty folders
delete_empty_folders()

print("empty folders deleted")

def create_folders_for_range(start_year,end_year):
    ''' to create folders for a range of years'''
    project_path=pathlib.Path.cwd()
    for years in range(start_year,end_year+1):
        my_path=project_path.joinpath(str(years))
        my_path.mkdir(exist_ok=False)

#create_folders_for_range(2001, 2004)

def create_folders_from_list(folder_list):
    ''' to create folders from a list of names'''
    project_path=pathlib.Path.cwd()
    for folder_name in folder_list:
        folder_path=project_path.joinpath(folder_name)
        folder_path.mkdir(exist_ok=False)



list= ["excel", "json", "csv"]
my_prefix= "data-"
'''
create_folders_from_list(list)
'''
def create_prefixed_folders(folderlist, prefix):
    ''' to create folders with prefix'''
    project_path=pathlib.Path.cwd()
    for folder_name in folderlist:
        folder_path=project_path.joinpath(prefix + folder_name)
        folder_path.mkdir(exist_ok=False)

#create_prefixed_folders(list, my_prefix)


def create_folders_periodically(duration, num_folders):
    '''Create folders periodically at intervals of duration seconds.'''
    # Create a Path object for the current working directory
    project_path = pathlib.Path.cwd()

    # Counter for the number of folders created
    num_folders_created = 0

    # Loop to create folders
    while num_folders_created < num_folders:
        # Generate folder name based on current time
        folder_name = time.strftime("%Y-%m-%d_%H-%M-%S")
        
        # Create folder path
        folder_path = project_path / folder_name
        
        # Create the folder
        folder_path.mkdir(parents=True, exist_ok=True)
        
        print(f"Folder created: {folder_path}")
        
        # Increment the counter
        num_folders_created += 1

        # Wait for the specified duration before creating the next folder
        time.sleep(duration)

# Example usage
duration_seconds = 5  # Duration between folder creations
num_folders = 5  # Number of folders to create
#create_folders_periodically(duration_seconds, num_folders)


def create_folders_from_list_v2(folder_list, to_lowercase=False, remove_spaces=False):
    '''Create folders from a list of names, with options to remove spaces and force lowercase.'''
    # Create a Path object for the current working directory
    project_path = pathlib.Path.cwd()

    # Iterate through each folder name in the list
    for folder_name in folder_list:
        # Apply options to remove spaces and force lowercase
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(' ', '')
        
        # Create folder path
        folder_path = project_path / folder_name
        
        # Create the folder
        folder_path.mkdir(parents=True, exist_ok=True)
        
        print(f"Folder created: {folder_path}")

# Example usage
#folders = ['Folder 1', 'Folder 2', 'Folder 3']
#create_folders_from_list(folders, to_lowercase=True, remove_spaces=True)

def main():
    ''' Main function to demonstrate module capabilities. '''

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2024)

    # Call function 2 to create folders given a list
    folder_names = ['csv', 'excel', 'json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs, 5) ##Five folders will be created

    # Add options to force lowercase and remove spaces to function 2
    continents = [
        "North America",
        "South America",
        "Asia",
        "Europe",
        "Antarctica",
        "Africa"       
    ]
    create_folders_from_list_v2(continents, to_lowercase=True, remove_spaces=True) ##lower case and space removed. Created a new function

if __name__ == "__main__":
    main()


