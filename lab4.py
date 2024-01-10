def pic():
 file = pickAFile()
 pict=makePicture(file)
 #explore(pict)
 print(pict)
 print (getWidth(pict))
 print (getHeight(pict))
 pixel=getPixel(pict,0,0)
 print(pixel)
 print( "X=",getX(pixel))
 print("Y=" ,getY(pixel))
 pixels=getPixels(pict)
 print(pixels[0])
 
def modifyColor():
 file = pickAFile()
 pict=makePicture(file)
 show(pict)
 pixel = getPixel(pict, 0,0)
 print(getRed(pixel))
 setRed(pixel,255)
 print(getRed(pixel))
 ###########################
 color = getColor(pixel)
 print(color)
 newColor = makeColor(125,56,92)
 print(newColor)
 setColor(pixel,newColor)
 print(getColor(pixel))
 ###############################
 color2 = pickAColor()
 print(color2)
 setColor(pixel,color2)
 

def DecreaseRed(picture):
    for pix in getPixels(picture):
      value=getRed(pix)
      setRed(pix,value*0.5)
      

def Nigative():
   file = pickAFile()
   pict=makePicture(file)
   show(pict) 
   for pix in getPixels(pict):
     red = getRed(pix)
     green = getGreen(pix)
     blue = getBlue(pix)
     newColor = makeColor(255-red , 255- green , 255-blue)
     setColor(pix,newColor)
     
     #writePictureTo(pict,r"C:\Users\alano\OneDrive\Music\MediaSources-20230911T055159Z-001\MediaSources\arch.jpg")
   repaint(pict)
   

def Swap ():
 file = pickAFile()
 pic = makePicture(file)
 show(pic)

 for pix in getPixels(pic):
  red = getRed(pix)
  blue = getBlue(pix)
  setRed(pix,blue)
  setBlue(pix,red)
 repaint(pic)


       
   
                   
 
 
 
  