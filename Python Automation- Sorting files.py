
import os                                                           # importing os module
import shutil                                                       # importing shutil module

os.chdir('C:\\Users\\hp\\Downloads')                                # Setting the working directory
path = 'C:\\Users\\hp\\Downloads'
f_names = os.listdir()                                              # saving all the files in the given directory to a list "f_names"

for f in f_names:                                                   # iterating through the list
    f_name, f_type = os.path.splitext(f)                            # splitting the filename and extension from each files
    ext = f_type[1:]                                                # removing the '.' from the f_type and storing it in a new variable

    if ext == '':                                                   # if there exists a directory inside
        continue

    if os.path.exists(path + '\\' + ext):                           # if the path to destination directory already exists
        shutil.move(path + '\\' + f, path+ '\\' + ext +"\\"+ f)     # moves the file accordingly

    else:                                                           # if the path to the destination directory does not exist
        os.makedirs(path+ '\\' + ext)                               # a new destination directory is made
        shutil.move(path + '\\' + f, path + '\\' + ext + "\\" + f)  # moves the file accordingly
