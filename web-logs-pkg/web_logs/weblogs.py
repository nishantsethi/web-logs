from pathlib import Path
import os
import logging
from shutil import copyfile




class WebLogs:
    current_working_dir = str(Path.cwd())
    root_dir = os.path.abspath(os.path.dirname(__file__))
    
    def __init__(self, json_path: str):
        self.json_path = json_path
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.__create_dir()
        self.__create_files()
        


    def __create_dir(self):
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
                
        
    def __create_files(self):
        """ Copies the files from data folder in package to \
            users working directory"""

        current_working_dir = self.current_working_dir

        temp_dir_local = current_working_dir + "/templates"
        static_dir_local = current_working_dir + "/static"
        app_dir_local = current_working_dir 
        
        index_dir_root = self.__get_data("index.html")
        style_dir_root = self.__get_data("style.css")
        app_dir_root = self.__get_data("app.py")
        
        ## Copy index.html
        try:
            copyfile(index_dir_root, temp_dir_local)
            self.logger.debug("The Index.html has been created")
        except:
            self.logger.error('An attempt was made to copy "index.html" file but was unsuccesfull. Please make \
                    sure the directory' + temp_dir_local + ' has write permissions.')

        ## Copy Style.css
        try:
            copyfile(style_dir_root, static_dir_local)
            self.logger.debug("The style.css file has been created")
        except:
            self.logger.error('An attempt was made to copy "Style.css" file but was unsuccesfull. Please make \
                    sure the directory ' + static_dir_local + ' has write permissions.')
        
        ## Copy App.py
        try:
            copyfile(app_dir_root, app_dir_local)
            self.logger.debug("The file app.py has been created")
        except:
            self.logger.error('An attempt was made to copy "app.py" file but was unsuccesfull. Please make \
                    sure the directory' + app_dir_local + ' has write permissions.')
        

    def __get_data(self, fileName):
        return os.path.join(self.root_dir, 'data', fileName)

    def __check_dir_exist(self, directory):
        return os.path.exists(directory)