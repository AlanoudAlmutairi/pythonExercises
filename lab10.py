
def makeMovie(directory):
  for num in range(1,30): #29 frames (1 to 29)
    canvas = makeEmptyPicture(300,200)
    addOval(canvas, 100, num*10, 50, 50, red)
    
    addOval(canvas, 200, 200-num *10, 50, 50, blue)
    #convert the number to a string
    numStr=str(num)
    if num < 10:
      writePictureTo(canvas,directory+"\\frame0"+numStr+".jpg")
    if num >= 10:
      writePictureTo(canvas,directory+"\\frame"+numStr+".jpg")
  movie = makeMovieFromInitialFile(directory+"\\frame00.jpg")
  return movie