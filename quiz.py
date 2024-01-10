
# alanoud Almutairi - 2105088 - 

def lightenedGrayscale():
    pic = makePicture("C:/Users/alano/OneDrive/Music/redMotorcycle(1).jpg")
    explore(pic)
    # x = 37 --> 540    y = 72 --> 430
    # for loop throw all pixels
    for x in range (0 , getWidth(pic)):
        for y in range (0 , getHeight(pic)):
    # show the position of the px if it is in the correct position    
            if ( 540 >= x >= 37) and ( 430 >= y >= 72): 
                # get the pixel      
                px = getPixel(pic , x, y)
                # get the red , green and blue color of the px and add 75 to them
                r = getRed(px)+ 75
                g = getGreen(px)+75
                b = getBlue(px)+75
                # find gray scal value
                total = (r + g + b )/3
                #see the value of gray sacal
                if total >255 :
                   total = 255 
                if total < 0 :
                   total = 0
                # make new color and set the color of the current px by the new color   
                color = makeColor( total , total , total)    
                setColor (px , color)
    show(pic) 
    
 
def swapSound():
    sound = makeSound("C:/Users/alano/OneDrive/Music/mediasources-4ed/thisisatest.wav")
    explore(sound)
    len = getLength(sound) / 2
    
    for s in range (0, len):
        # get the sample in the left part
        left = getSampleObjectAt(sound , s)
        # get The sample in the right part
        right = getSampleObjectAt(sound ,len+s)
        # get the values of 2 samples
        leftVal = getSampleValue(left)
        rightVal = getSampleValue(right)
        #swap between the samples 
        setSampleValueAt( sound , s , rightVal)
        setSampleValueAt(sound ,len+s ,leftVal)
    explore(sound)      
           
                            
                   
        
    