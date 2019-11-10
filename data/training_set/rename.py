import os
path = "C://Users//Yamini Agrawal//Desktop//Trash_segr//data//training_set"
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))