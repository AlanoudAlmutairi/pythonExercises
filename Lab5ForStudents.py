
setMediaPath("C:/Users/alano/OneDrive/Music/mediasources-4ed/")

def removeRedEye(pic,startX,startY,endX,endY,endColor):
    for px in getPixels(pic):
        x = getX(px)
        y = getY(px)
        if (startX <= x <= endX) and (startY <= y <= endY):
            if (distance(red,getColor(px)) < 165):
                setColor(px,endColor)
                
def luminance(pixel):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    return (r+g+b)/3

def edgedetect(source):
    for px in getPixels(source):
      x = getX(px)
      y = getY(px)
      if y < getHeight(source)-1 and x < getWidth(source)-1:
        botrt = getPixel(source,x+1,y+1)
        thislum = luminance(px)
        brlum = luminance(botrt)
        if abs(brlum-thislum) > 10:
            setColor(px,black)
        if abs(brlum-thislum) <= 10:
            setColor(px,white)
        
            
def swapBack(pict,bg,newBg):
  for px in getPixels(pict):
    x = getX(px)
    y = getY(px)
    bgPx = getPixel(bg,x,y)
    pxcol = getColor(px)
    bgcol = getColor(bgPx)
    if (distance(pxcol,bgcol)<15.0):
        newcol=getColor(getPixel(newBg,x,y))
        setColor(px,newcol)
        
def chromakeyBlue(source,bg):
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if (getRed(px) + getGreen(px) < getBlue(px)):
      bgpx = getPixel(bg,x,y)
      bgcol = getColor(bgpx)
      setColor(px,bgcol)
      
      

def decreaseRedHalf() : 
       file =pickAFile() 
       pic = makePicture(file)
       pixels=getPixels (pic)
       for index in range (0 , len(pixels)/2):
         pixel=pixels[index]
         red = getRed(pixel)
         setRed(pixel,red*0.5) 
       show(pic)         
       

def changeRedGreen(x,y):
    file = pickAFile()
    pic=makePicture(file)
    pixels = getPixels(pic)
    halfPart =getWidth(pic)/2
    for index in pixels:
       x=getX(index)
       if x>halfPart:
          green = getGreen(index)
          setGreen(index,green*y)
    
    for index in pixels:
      x=getX(index)
      if x<halfPart:
          red = getRed(index)
          setRed(index,red*x)           
    explore(pic) 
    
def changeGreen(x,y):              
    file = pickAFile()
    pic=makePicture(file)
    pixels = getPixels(pic)
    halfPart =getWidth(pic)/2
    for index in pixels:
       x=getX(index)
       if x>halfPart:
          green = getGreen(index)
          setGreen(index,green*x)
    
    for index in pixels:
      x=getX(index)
      if x<halfPart:
          green = getGreen(index)
          setGreen(index,green/y)           
    explore(pic) 
