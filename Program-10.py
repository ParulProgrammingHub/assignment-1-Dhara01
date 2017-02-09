p=float(raw_input(“Enter principle:”))
i=float (raw_input(“Enter the percentage of interest rate: “))
t=float(raw_input(“Enter time (in years): “))
def simple_interest(principle,rate,time):
               I=p*t*(i/100)
               print “Intereast is “,I 
simple_interest(principle=p,rate=r,time=t)
