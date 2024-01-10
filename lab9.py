setMediaPath("C:/Users/alano/OneDrive/Music/mediasources-4ed")

def task(sound): 
  counter = 0 
  size = getLength(sound)
  canvas = makeEmptySound(size)
  for sample in range (0 , size, 2 ): 
      S = getSampleValueAt(sound ,sample)
      setSampleValueAt(canvas,counter,S)
      counter = counter + 1
  play(canvas)    
  
  
  
def task2(sound): 
  counter = 0 
  size = getLength(sound)*2
  canvas = makeEmptySound(size)
  for sample in range (0,size):
      S = getSampleValueAt(sound,int(sample + 0.5))
      setSampleValueAt(canvas,counter,S)
      
  play(canvas)   