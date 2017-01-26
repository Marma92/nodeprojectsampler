#This file will contains all the functions used by the generator. May be coupled to other functions files in the future. Enjoy.

def create_file (filename, path) :
    #taking the desired filename, and the path to generate a file

def create_folder (foldername, path):
    #same as previously, but for a folder

def file_filler (filepath, content):
    #fill a file with sampled code

def server_generator(port):
    #generating the server.js file, that will listen to the defined port

def routes_generator(route, *routes):
    #generating routes asked to the app

def config_generator(database, passport):
    #generating default config files if a db or passport are used.
