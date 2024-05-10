
'''Start a data analytics projects.'''

#start with imports from the python standard Library
import pathlib
from pathlib import Path

#import your own modules
def create_project_directory(directory_name: str) -> None:
    """
    Creates a project sub directory.
    :param directory_name: Name of the directory to be created, eg "test"
    """
    pathlib.Path(directory_name).mkdir(exist_ok=True)



#define your main function here

def main():
    create_project_directory('test')
    create_project_directory('docs')
    
#add module block at the bottom
if __name__ == '__main__':
    main()    