import os

def text_to_list_of_string(filename):
    fpath = os.path.join('txt_database', filename)
    file = open(fpath,"r")
    content = file.read()
    file.close()
    return(content)