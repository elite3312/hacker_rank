import shutil
import sys
import os
if not os.path.exists('./solutions/'+sys.argv[1]+'.py'):
    shutil.copyfile('./main.py','./solutions/'+sys.argv[1]+'.py')
else:print('file exists')