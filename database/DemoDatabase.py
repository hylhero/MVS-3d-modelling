import sqlite3
import os

f = open(r'C:\3d-Model\bin\curr_proj.txt','r')
pathDir = f.readline()
f.close()
os.chdir(pathDir)
paths = pathDir.split('\\')
index=len(paths)-1
projName = paths[index] + '.db'
conn= sqlite3.connect(projName)
 
cursor = conn.cursor()
 
# create a table
# cursor.execute('''CREATE TABLE information
                  #( Longitude text, Latitude text, 
                   #Elevation(WGS84) text, Type text, Ownership text,
                   #Population Count text, Males text, Females text
                   #Additional info text)''')


cursor.execute('''CREATE TABLE information
             (name text, latitude text, longitude text, altitude text)''')




          
