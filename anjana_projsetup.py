''' This module provides functions for creating a series of project folders. '''

import pathlib
import time
import anjana_analyst_utils.py

# function1
def create_folders_for_range(start_year,end_year):
    ''' to create folders for a range of years'''
    project_path=pathlib.Path.cwd()
    for years in range(start_year,end_year+1):
        year_path=project_path.joinpath(str(years))
        year_path.mkdir(exist_ok=False)


# function2
def create_folders_from_list(folder_list,to_lowercase=False, remove_spaces=False):
    ''' to create folders from a list of names'''
    project_path=pathlib.Path.cwd()
    for folder_name in folder_list:
        if to_lowercase:
            folder_name=folder_name.lower()
        if remove_spaces:
            folder_name=folder_name.replace('','')
        folder_path=project_path.joinpath(folder_name)
        folder_path.mkdir(exist_ok=False)


# function 3
def create_prefixed_folders(folderlist, prefix):
    ''' to create folders with prefix'''
    project_path=pathlib.Path.cwd()
    for folder_name in folderlist:
        folder_path=project_path.joinpath(prefix + folder_name)
        folder_path.mkdir(exist_ok=False)

# function 4
def create_folders_periodically(duration, time_limit):
    ''' to create folders periodically with a time limit'''
    project_path=pathlib.Path.cwd()
    start_time=time.time() # to record the start time
    while time.time() - start_time < time_limit:
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
        pathlib.Path(timestamp).mkdir(parents=True, exist_ok=True)
        time.sleep(duration)


def main():
    ''' Main function to demonstrate module capabilities. '''

    # Print byline from imported module
    print(f"Byline: {anjana_analyst_utils.py.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

if __name__ == '__main__':
    main()
