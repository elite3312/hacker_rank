import shutil,glob,os
dirs=[
    "solutions"
]
for dir in dirs:
    files=glob.glob(dir+'/*.py')
    for file in files:
        _base_name=os.path.basename(file)
        _new_base_name=_base_name.replace(" ","_")
        os.rename(file,file.replace(_base_name,_new_base_name))