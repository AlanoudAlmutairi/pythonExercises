setMediaPath("C:/Users/alano/OneDrive/Music/mediasources-4ed")

def normalize(sound):
  largest = 0
  for s in getSamples(sound):
    largest = max(largest,getSampleValue(s) )
  multiplier = 32767.0 / largest
  print "Largest sample value in original sound was",largest
  print "Multiplier is", multiplier

  for s in getSamples(sound):
    louder = multiplier * getSampleValue(s)
    setSampleValue(s,louder)

def merge():
  guzdialSound = makeSound("guzdial.wav")
  isSound = makeSound("is.wav")
  target = makeEmptySoundBySeconds(5)
  index = 0
# Copy in "Guzdial"
  for source in range(0,getLength(guzdialSound)):
    value = getSampleValueAt(guzdialSound,source)
    setSampleValueAt(target,index,value)
    index = index + 1
# Copy in 0.1 second pause (silence) (0)
  for source in range(0,int(0.1*getSamplingRate(target))):
    setSampleValueAt(target,index,0)
    index = index + 1
# Copy in "is"
  for source in range(0,getLength(isSound)):
    value = getSampleValueAt(isSound,source)
    setSampleValueAt(target,index,value)
    index = index + 1
  play(target)
  return target
  
def clip(source,start,end):
  target = makeEmptySound(end - start)
  targetIndex = 0
  for sourceIndex in range(start,end):
    sourceValue = getSampleValueAt(source,sourceIndex)
    setSampleValueAt(target,targetIndex,sourceValue)
    targetIndex = targetIndex + 1
  return target

def reverse(source):
  target = makeEmptySound(getLength(source))
  sourceIndex = getLength(source)-1
  for targetIndex in range(0,getLength(target)):
    sourceValue = getSampleValueAt(source,sourceIndex)
    setSampleValueAt(target,targetIndex,sourceValue)
    sourceIndex = sourceIndex - 1
  return target
  
###################--- TASK ---####################### 
def task():
   file = pickAFile()
   sound = makeSound(file)
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      if (value > 0 ):
        setSampleValue(sample, value/2)
      elif(value <= 0 ):
        setSampleValue(sample,value*2)
   play(sound)    

  
######################################################
def sound():
   file = pickAFile()
   sound = makeSound(file)
   print(sound)
   #play(sound)
   #explore(sound)
   print(getLength(sound))
   #----------------------------------#   
   print(getSampleValueAt(sound ,12))
   setSampleValueAt(sound ,12 , 0) 
   print(getSampleValueAt(sound ,12))
   #----------------------------------#
   print(getSamplingRate(sound))
   #----------------------------------#

######################################################

def increaseVolume(sound):
    for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample,value*2)
      

def increaseVolumeByRange(sound):
     for sampleInd in range (0 , getLength(sound)):
       value = getSampleValueAt(sound , sampleInd)
       setSampleValueAt(sound,sampleInd,value*2)
######################################################             
          
 