#hw 7 problem 1#
import sys
#opens and closes#
def cleanHeader(fin, header_fout):
#gets the name of the play#
    firstLine = fin.readline()
    fout = header_fout
    a = 'of'
    b = 'by'
    
    name = firstLine.split(a)[-1].split(b)[0]
    fout.write(str(name+'\n'))
   
    lines = fin.readlines()
   
    act = False
 #only prints the part of the text after the play starts #   
    for line in lines:
        if 'ACT I' in line:
            
            act = True

        if act == True:
            fout.write(line)
        else:
            pass

    fout.close()
            

    

