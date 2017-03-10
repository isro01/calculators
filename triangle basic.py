import time
print "\t \t Welcome"
print "this is the radius of incircle and circumcircle of a triangle calculator"
def start():
    print "type in the three sides"
    s1=float(raw_input("side1:"))
    s2=float(raw_input("side2:"))
    s3=float(raw_input("side3:"))
    print "Radius of incircle or circumcircle??? Tyoe in C or I"
    ans=raw_input("")
    s=(s1+s2+s3)/2
    area=float((s*(s-s1)*(s-s2)*(s-s3))**0.5)
    print " \n calculating..."
    time.sleep(1)
    if ans=="C":
        calc=(float(s1*s2*s3))/(area*4)
        print calc
    elif ans=="I":
        calc=area/s
        print calc
    else:
        print "please type C orI only"
    print"want to give it another try...Y or N"
    ans1=raw_input("")
    if ans1=="Y":
        print "\n reloading..."
        time.sleep(0.5)
        start()
    elif ans1=="N":
        print "bye bye then"
    
start()
