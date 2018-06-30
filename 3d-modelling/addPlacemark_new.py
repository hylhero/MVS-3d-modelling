import os

placemarkStr = ''

def placemark(filename,values,lat,longi,altitude): #values is a list of values to be filled in the placemark file
    global placemarkStr
    f = open(filename,'r')
    linesCol = f.readlines()
    totalLength = len(linesCol)
    f.close()

    
    placemarkStr += '<Placemark>\n\
        <ExtendedData>\n'
    placemarkStr += '<Data name="Name">\n\
            <value>'+values[0]+'</value>\n\
          </Data>\n'
    for i in range(totalLength):
        placemarkStr += '<Data name="'+(linesCol[i])[:-1]+'">\n\
            <value>'+values[i+1]+'</value>\n\
          </Data>\n'
    placemarkStr += '<Data name="Height:">\n\
            <value>'+altitude+'</value>\n\
          </Data>\n'
    placemarkStr += '</ExtendedData>\n\
        <Point>\n\
          <coordinates>'+lat+','+longi+','+altitude+'</coordinates>\n\
              <altitudeMode>relativeToGround</altitudeMode>\n\
              <extrude>1</extrude>\n\
        </Point>\n\
    </Placemark>\n'

if __name__== '__main__':
    global placemarkStr
    f = open(r'C:\3d-Model\bin\curr_proj.txt','r')
    pathDir = f.readline()
    f.close()

    os.chdir(pathDir)
    fw = open(r'dblist.txt','w')

    print placemarkStr
    f = open(r'C:\3d-Model\bin\3d-modelling\Placemark.kml','r') #reading from the previously created Placemark file
    linespp = f.readlines()
    temp = len(linespp)
    f.close()
    placemarkStr += linespp[0]
    placemarkStr += linespp[1]
    placemarkStr += linespp[2]
    shortPath = '\\input'
    
    os.chdir(pathDir + shortPath)
    for dir1 in os.listdir('.'):
        os.chdir(pathDir + shortPath + '\\' + dir1)

        fHeight = open('heights.txt','r')
        hstr = fHeight.readline()
        fHeight.close()

        tempList = hstr.split('\t')
        num_floors = len(tempList) - 1

        fcoord = open(dir1+'.txt','r')
        cstr = fcoord.readline()
        fcoord.close()
        lat = (cstr.split('\t'))[1]
        longi = (cstr.split('\t'))[2]
        height = 0.0
        for i in range(num_floors):
            filename = (dir1 + '_' + '%s' %(i+1))
            fdetail = open(filename+'.txt','r')
            lines = fdetail.readlines()
            temp = len(lines)
            fdetail.close()
            values=[]
            for j in range(temp):
                tempStr = (lines[j])[:-1]
                values.append(tempStr)
            
            print values
            height += float(tempList[i+1])
            altitude = str(height)
            print altitude
            print lat
            print longi
            
            filename1 = filename+'db.txt'
            fptr = open(filename1,'w')
            fptr.writelines(values[0]+'\n')
            fptr.writelines(lat+'\n')
            fptr.writelines(longi+'\n')
            fptr.writelines(altitude+'\n')
            for i in range(temp-1):
                fptr.writelines(values[i+1]+'\n')
            fptr.close()
            fw.write(filename1+'\n')
            placemark(pathDir+'\\column.txt',values,lat,longi,altitude)
    placemarkStr += linespp[3]
    placemarkStr += linespp[4]
    print placemarkStr
    fw.close()
    
    f = open(r'C:\3d-Model\bin\curr_proj.txt','r')
    pathDir = f.readline()
    f.close()
    shortPath = '\\output'
    filenmP = pathDir + shortPath + '\\Placemark.kml'
    
    
    '''f = open(filenmP,'r') #reading from the newly created Placemark file
    linesP = f.readlines()
    tempP = len(linesP)
    f.close()'''
    
    #filenmT = pathDir + shortPath + '\\temp.kml'
    fw = open(filenmP,'w')
    fw.writelines(placemarkStr)
    fw.close()
    #os.remove(filenmP)
    #os.rename(filenmT,filenmP)
