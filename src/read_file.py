import os
import codecs

def text_read(filename):
    fpath = os.path.join('txt_database', filename)
    file = codecs.open(fpath,"r", encoding = 'utf-8')
    content = file.read()
    file.close()
    return(content)
