import os
import sys

src=sys.argv[1]
file_name=os.listdir(src)
c=1000

for files in file_name :
    
    #print files
    os.chdir(src)
    os.rename(files,'photo_'+str(c)+'.jpg')
    c=c+1
    
    
