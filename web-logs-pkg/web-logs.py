import argparse 
from pathlib import Path
import json
import os
import logging


def main():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
  
    hello_parser = subparsers.add_parser('create')
    hello_parser.add_argument('path_to_json', help= " The path to Json file with details of logs")  # add the name argument
    
    args = parser.parse_args()


    # Variables
    json_path = args.path_to_json
    current_working_dir = str(Path.cwd())

    #Logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    create_dir(current_working_dir)


    def create_dir(current_working_dir):
        temp_dir = current_working_dir + "/templates"
        static_dir = current_working_dir + "/static"
        
        
        if check_dir_exist(temp_dir):
            logger.error("Template folder could not be created as a folder with name \"templates\" already exists, \
                Please delete or rename the folder.")
        else:
            os.makedirs(temp_dir)
            logger.debug("The Template folder has been created")
            if check_dir_exist(static_dir):
                logger.debug("The Template folder has been created")
            else:    
                logger.error("An attempt was made to create the \"templates\" folder but was unsuccesfull. Please make \
                    sure the directory has write permissions.")


        
        if check_dir_exist(static_dir):
            logger.error("The static folder could not be created as a folder with name \"static\" already exists, \
                Please delete or rename the folder.")
        else:
            os.makedirs(static_dir)
            if check_dir_exist(static_dir):
                logger.debug("The static folder has been created")
            else:    
                logger.error("An attempt was made to create the \"static\" folder but was unsuccesfull. Please make \
                    sure the directory has write permissions.")
    
    def check_dir_exist(directory):
        return os.path.exists(directory)







main()