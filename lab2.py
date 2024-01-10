def Write():
 #open
 program=pickAFile()
 #use
 file=open(program,"wt")
 file.write("Welcome to Jython programing language! This is Lab 2*** Happy to be here")
 #close
 file.close()


def findPart(key): 
 #open
 program=pickAFile()
 #use
 file=open(progarm,"rt")
 part=file.read()
 #close
 file.close()
 #find the sentence
 partLoc=part.find(key)
 Start = part.find("! this")
 end = part.find("2***")
  #open
 program=pickAFile()
 #use
 file2=open(progarm,"wt")
 part=file2.write(partLoc)
 #close
 file.close()
 
 
 