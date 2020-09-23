from pathlib import Path
import json
import os
import logging


logging.basicConfig()


class WebLogs:
    current_working_dir = str(Path.cwd())
    
    def __init__(self, json_path: str):
        self.json_path = json_path
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.__create_dir(self.current_working_dir)


    def __create_dir(self, current_working_dir):
        temp_dir = self.current_working_dir + "/templates"
        static_dir = self.current_working_dir + "/static"
        
        
        if self.__check_dir_exist(temp_dir):
            self.logger.error("Template folder could not be created as a folder with name \"templates\" already exists, \
                Please delete or rename the folder.")
        else:
            os.makedirs(temp_dir)
            self.logger.debug("The Template folder has been created")
            if self.__check_dir_exist(static_dir):
                self.logger.debug("The Template folder has been created")
            else:    
                self.logger.error("An attempt was made to create the \"templates\" folder but was unsuccesfull. Please make \
                    sure the directory has write permissions.")


        
        if self.__check_dir_exist(static_dir):
            self.logger.error("The static folder could not be created as a folder with name \"static\" already exists, \
                Please delete or rename the folder.")
        else:
            os.makedirs(static_dir)
            if self.__check_dir_exist(static_dir):
                self.logger.debug("The static folder has been created")
            else:    
                self.logger.error("An attempt was made to create the \"static\" folder but was unsuccesfull. Please make \
                    sure the directory has write permissions.")
                
            
        

    def __check_dir_exist(self, directory):
        return os.path.exists(directory)
        