import argparse 
from pathlib import Path
import json
import os
import logging
from shutil import copyfile


def main():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
  
    hello_parser = subparsers.add_parser('create')
    hello_parser.add_argument('path_to_json', help= " The path to Json file with details of logs")  # add the name argument
    
    args = parser.parse_args()


    # Variables
    json_path = args.path_to_json
    
    

    
    
    class WebLogs:
        current_working_dir = str(Path.cwd())
        root_dir = os.path.abspath(os.path.dirname(__file__))
        
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
                    
            
        def __create_files(self,current_working_dir):
            """ Copies the files from data folder in package to \
                users working directory"""

            current_working_dir = self.current_working_dir

            temp_dir_local = self.current_working_dir + "/templates"
            static_dir_local = self.current_working_dir + "/static"
            app_dir_local = self.current_working_dir 
            
            index_dir_root = self.__get_data("index.html")
            style_dir_root = self.__get_data("style.css")
            app_dir_root = self.__get_data("app.py")
            
            ## Copy index.html
            try:
                copyfile(index_dir_root, temp_dir_local)
            except:
                self.logger.error('An attempt was made to copy "index.html" file but was unsuccesfull. Please make \
                        sure the directory has write permissions.')

            ## Copy Style.css
            try:
                copyfile(style_dir_root, static_dir_local)
            except:
                self.logger.error('An attempt was made to copy "index.html" file but was unsuccesfull. Please make \
                        sure the directory has write permissions.')
            
            ## Copy App.py
            try:
                copyfile(app_dir_root, app_dir_local)
            except:
                self.logger.error('An attempt was made to copy "index.html" file but was unsuccesfull. Please make \
                        sure the directory has write permissions.')
            

        def __get_data(self, fileName):
            return os.path.join(self.root_dir, 'data', fileName)

        def __check_dir_exist(self, directory):
            return os.path.exists(directory)