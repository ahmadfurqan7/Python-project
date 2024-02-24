#print out christmas tree :)
#column = 13
#height/row = 7
# ------*------ 1 - space = 6*2= 12
# -----***----- 3 - space = 5*2= 10
# ----*****---- 5 - space = 4*2= 8
# ---*******--- 7 - space = 3*2= 6
# --*********-- 9 - space = 2*2= 4
# -***********- 11 - space = 1*2= 2
# ************* 13 - space = 0*2= 0

#((height*2-1)-star)/2

def  christmastree(height):  #create functtion
    stars = 1 #start with 1 star
    maxcolumn = height * 2 - 1 
    for row in range(height): #loop range for add star 
        space=(maxcolumn-stars)//2
        print(space * " " + stars * "*" + space * " ") #left and right space and star in the middle
        stars += 2 #

christmastree(11)
#Done :)