setMediaPath("C:/Users/alano/OneDrive/Music/mediasources-4ed/")

def Crop():
    src = makePicture("jenny-red.jpg")
    canvas = makeEmptyPicture(400 , 400)
    
    targetX =100
    for sourceX in range (109,202):
       targetY =100
       for sourceY in range (91,107):
          px = getPixel(src ,sourceX,sourceY)
          color = getColor (px)
          #color =getColor(getPixel(src,sourceX,sourceY))
          setColor(getPixel(canvas,targetX,targetY), color)
          targetY = targetY + 1
       targetX = targetX + 1
               
    show(canvas)
    
  
                                                      
def DrawHouse():
   pic2 = makeEmptyPicture(900 , 900)
   
            ## HOUSE ##
   homeColor = makeColor(195,118,138)
   addRectFilled(pic2,200,300,500,900,homeColor)
   addRect(pic2,200,300,500,900)
   
           ## WINDOW ##
   windowColor=makeColor(153 ,204 ,255)
   addRectFilled(pic2,250,400,100,100,windowColor)
   addRectFilled(pic2,550,400,100,100,windowColor)
   addRect(pic2,250,400,100,100)
   addRect(pic2,550,400,100,100)
   addLine(pic2,250,450,350,450)
   addLine(pic2,300,400,300,500)
   addLine(pic2,550,450,650,450)
   addLine(pic2,600,400,600,500)
   
             ## DOOR ##
   doorColor = makeColor(198 ,152,112)
   addRectFilled(pic2,400,680,100,200,doorColor)
   addRect(pic2,400,680,100,200)
   
            ## GROUND ##
   groundColor = makeColor(51 , 153 ,102)
   addRectFilled(pic2,0,880,900,20,groundColor)
   
            ## SUN ##
   sunColor = makeColor(299 , 182 ,53)
   addOvalFilled(pic2, 50, 80, 130, 130, sunColor)
   
   
   
       
   show(pic2)
                               