import argparse 
from pathlib import Path
import json
import os
import logging
from shutil import copyfile
from .weblogs import WebLogs
import pkg_resources

DATA_PATH = pkg_resources.resource_filename('weblogs', 'data')

def main():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
  
    hello_parser = subparsers.add_parser('create')
    hello_parser.add_argument('path_to_json', help= " The path to Json file with details of logs")  # add the name argument
    
    args = parser.parse_args()


    # Variables
    json_path = args.path_to_json

    json_file_txt = open(DATA_PATH + "/json_path.txt","w")
    json_file_txt.write(json_path)
    json_file_txt.close()


    print(json_path)

    WebLogs(json_path)
    
main()