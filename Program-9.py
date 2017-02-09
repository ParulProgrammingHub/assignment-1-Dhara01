NASM=float(input(“Enter the marks: “))
OOAD=float(input(“Enter the marks: “))
DBMS=float(input(“Enter the marks: “))
MI=float(input(“Enter the marks: “))
CO=float(input(“Enter the marks: “))
mean = ( NASM + OOAD + DBMS + MI + CO ) / 5
percentage = ( mean  ) * 100
print (“Mean is %d”,%mean)
print (“Percentage is %d”,%percentage)
if percentage<35 :
       print “FAIL”
else:
       print “PASS”
