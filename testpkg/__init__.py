from pathlib import Path
import os
import logging



class test:
    
    current_working_dir = str(Path.cwd())

    def __init__(self):
        self.__create_file(self.current_working_dir)

    def __create_file(self, current_working_dir):
        if os.path.exists(self.current_working_dir + "/templates"):
            print("templates exists")
        else:
            print("Does not exist")
