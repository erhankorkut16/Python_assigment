from operator import truediv


while True:
    vartime = (input( "Please enter a number " ))
    
    if vartime.isnumeric == False :
        print( "Your value is not a number " )
        continue
    
    if vartime == "exit":
        print( "good by" )
        break
    
    vartime = int(vartime)
    
    if vartime < 1:
        print("number is less than 1,Please enter greater than 1 ")
        continue
    

    if vartime >= 360000:
        h = vartime // 360000
        m = (vartime % 360000) // 60000
        s = ((vartime % 360000) % 60000) // 1000
    
        print("Input            Output")
        print("(milliseconds)   (Calculator)")
        print("-------------     ------------")
        print("{}         {} hour/s {} minute/s {} second/s".format(vartime,h,m,s))
        
    elif vartime >= 60000:
        
        m = vartime // 60000
        s = (vartime % 60000) // 1000 
        print("Input            Output")
        print("(milliseconds)   (Calculator)")
        print("-------------     ------------")
        print("{}            {} minute/s {} second/s".format(vartime,m,s))
        
    elif vartime >= 1000:
        s = vartime // 1000
        
        print("Input            Output")
        print("(milliseconds)   (Calculator)")
        print("-------------     ------------")
        print(f"{vartime}          {s} second/s")
    else:
        print(vartime)