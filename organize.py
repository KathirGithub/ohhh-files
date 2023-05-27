import os
import shutil

from_dir='C:/Users/paran/Downloads'

to_dir='C:/Users/paran/Downloads/di'

listoffiles=os.listdir(from_dir)

#print(listoffiles)

for filename in listoffiles:
    root,extension=os.path.splitext(filename)
    #print(root)
    #print(extension)
    if extension=='':
        continue
    if extension in ['.txt', '.doc','.docx',' .pdf']:
        path1=from_dir+'/'+filename
        path2=to_dir+'/'+'documentFiles'
        path3=to_dir+'/'+'documentFiles'+'/'+filename
        if os.path.exists(path2):
            print('moving'+filename+'...')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('moving'+filename+'...')
            shutil.move(path1,path3)