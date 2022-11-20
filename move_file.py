import shutil
import sys
import os
if not os.path.exists('./'+sys.argv[1]+'.py'):
    shutil.copyfile('./main.py','./'+sys.argv[1]+'.py')
else:print('file exists')