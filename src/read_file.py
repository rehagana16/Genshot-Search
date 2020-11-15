import os
import codecs

def text_to_list_of_string(filename):
    fpath = os.path.join('txt_database', filename)
    file = open(fpath,"r")
    content = file.read()
    content_list = content.split(".")
    file.close()
    return(content_list)

def text_read(filename):
    fpath = os.path.join('txt_database', filename)
    file = codecs.open(fpath,"r", encoding = 'utf-8')
    content = file.read()
    file.close()
    return(content)
