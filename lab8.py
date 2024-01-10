def task():
   file = pickAFile()
   sound = makeSound(file)
   for sample in getSamples(sound)):
      value=getSampleValue(sample)
      if (value > 0 ):
        setSampleValue(sound, s/2)
      if(value < 0 ):
        setSampleValue(sound, s*2)
   play(sound)       