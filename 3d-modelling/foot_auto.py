import re
import os

def find(q,dr):
    x=1
    y=0
    drec=os.chdir(dr)
    dx=os.listdir(dr)
    address=dr+'\\'+dx[q]+'\\'+dx[q]+'.kml'
    f=open(address)
        
    for line in f:
        if re.search("<coordinates>",line):
            print('start in line 1')
            req_string=''

            if re.search("</coordinates>",line):
                    print 'end in line 1 all coos in same line'
                    y = 1
                    line = re.sub("<coordinates>",'',line)
                    line = re.sub("</coordinates>",'',line)
                    req_string = line.strip()
                    break

            if(len(line.strip())==13):
                print'no coords in <coo> line'
                y = 0
            else:
                print'coords in <coo> line'
                y = 1
                line = re.sub("<coordinates>",'',line)
                req_string = line.strip()
                
            for line in f:
                x = x+1
                y = y+1
                req_string = req_string + line.strip()
                if re.search("</coordinates>",line):
                    print 'end in line' ,x
                    if(len(line.strip())==14):
                        print'no coords in </coo> line'
                        y = y-1
                        req_string = re.sub("</coordinates>",'',req_string)
                        break
                    else:
                        print'coords in </coo> line'
                        req_string = re.sub("</coordinates>",'',req_string)
                        break
    return req_string
    print x
    print y

def store(req_string,q,dr):
    #req string without comma replacing space
    #f_w = open(r'C:\pSApp\input\build%d\build%d.txt'%(q,q),'w')
    #########
    drec=os.chdir(dr)
    dx=os.listdir(dr)
    address=dr+'\\'+dx[q]+'\\'+dx[q]+'.txt'
    f_w=open(address,'w')
    
    count1 = 0
    a = 0
    while(a!=-1):
        a = req_string.find(',',a+1)
        count1 = count1+1
    ########
    req_string = re.sub(' ',',',req_string)
    num_coo= (count1-1-2)/2
    print num_coo
    f_w.write('%s'%(num_coo))
    #height = 10
    #f_w.write('\t'+'%s'%(height))
    p = 0
    x = 0
    z = 0
    count = 0
    count1 = 1
    print req_string
    
    while(count<=(3*num_coo-1)):
        x = req_string.find(',',x+1)
        ##code segment removed
        print (req_string[z:x])
        if((count-2)%3!=0):
            f_w.write('\t'+req_string[z:x])
        p = x
        z = p+1
        count = count+1
            
if __name__ == "__main__":
    os.chdir(r'C:\pSApp\tempFiles')
    f=open("temp.txt")
    line_count=0
    
    for line in f:
        line_count=line_count+1
        if(line_count==1):
            l=line
            break
    
    os.chdir(l)
    num_dir=len(os.listdir(l))
    dir_list=os.listdir(l)
    for i in range(num_dir):
        x=find(i,l)
        store(x,i,l)
        
