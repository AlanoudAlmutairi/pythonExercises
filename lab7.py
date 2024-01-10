def MedianFillter() : 
  file = pickAFile()
  pic = makePicture(file)
  
  pixle=[None]*9
  
  for i in range(1,getWidth(pic)-1):
    for j in range(1,getHeight(pic)-1):
      pixle[0] = luminance(pic.getPixel(i-1,j-1))
      pixle[1] = luminance(pic.getPixel(i-1,j))
      pixle[2] = luminance(pic.getPixel(i-1,j+1))
      pixle[3] = luminance(pic.getPixel(i,j+1))
      pixle[4] = luminance(pic.getPixel(i+1,j+1))
      pixle[5] = luminance(pic.getPixel(i+1,j))
      pixle[6] = luminance(pic.getPixel(i+1,j-1))
      pixle[7] = luminance(pic.getPixel(i,j-1))
      pixle[8]= luminance(pic.getPixel(i,j))
      
      pixle.sort()
      
      color = makeColor(pixle[4],pixle[4],pixle[4])
      pic.getPixel(i,j).setColor(color)
      
  show(pic)
      
  
  
  ###NOT completed

def luminance(pixel):
    r = getRed(pixel)
    g = getGreen(pixel)
    b = getBlue(pixel)
    return (r+g+b)/3


def LaplacianFillter():
  file = pickAFile()
  pic = makePicture(file)
  pic2 = makeEmptyPicture(getWidth(pic) , getHeight(pic))
  
 
  
  sum = 0 
  pixle=[None]*9
  
  for i in range(1,getWidth(pic)-1):
    for j in range(1,getHeight(pic)-1):
      pixle[0] = luminance(pic.getPixel(i-1,j-1))*1
      pixle[1] = luminance(pic.getPixel(i-1,j))*1
      pixle[2] = luminance(pic.getPixel(i-1,j+1))*1
      pixle[3] = luminance(pic.getPixel(i,j+1))*1
      pixle[4] = luminance(pic.getPixel(i+1,j+1))*1
      pixle[5] = luminance(pic.getPixel(i+1,j))*1
      pixle[6] = luminance(pic.getPixel(i+1,j-1))*1
      pixle[7] = luminance(pic.getPixel(i,j-1))*1
      pixle[8]= luminance(pic.getPixel(i,j))*-8
      sum =pixle[0]+pixle[1]+pixle[2]+pixle[3]+pixle[4]+pixle[5]+pixle[6]+pixle[7]+pixle[8]
      if sum > 255: 
       sum = 255
      elif sum < 0 :
       sum =0
      color = makeColor(sum,sum,sum)
      pic2.getPixel(i,j).setColor(color)
  show(pic2) 
  


def LaplacianFillter2():
  file = pickAFile()
  pic = makePicture(file)
  pic2 = makeEmptyPicture(getWidth(pic) , getHeight(pic))
  
 
  
  sum = 0 
  pixle=[None]*9
  
  for i in range(1,getWidth(pic)-1):
    for j in range(1,getHeight(pic)-1):
      pixle[0] = luminance(pic.getPixel(i-1,j-1))*-1
      pixle[1] = luminance(pic.getPixel(i-1,j))*-1
      pixle[2] = luminance(pic.getPixel(i-1,j+1))*-1
      pixle[3] = luminance(pic.getPixel(i,j+1))*-1
      pixle[4] = luminance(pic.getPixel(i+1,j+1))*-1
      pixle[5] = luminance(pic.getPixel(i+1,j))*-1
      pixle[6] = luminance(pic.getPixel(i+1,j-1))*-1
      pixle[7] = luminance(pic.getPixel(i,j-1))*-1
      pixle[8]= luminance(pic.getPixel(i,j))*8
      sum =pixle[0]+pixle[1]+pixle[2]+pixle[3]+pixle[4]+pixle[5]+pixle[6]+pixle[7]+pixle[8]
      if sum > 255: 
       sum = 255
      elif sum < 0 :
       sum =0
      color = makeColor(sum,sum,sum)
      pic2.getPixel(i,j).setColor(color)
  show(pic2)        
                                          
                                                  
                                          
                  
    
