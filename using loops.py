def print_patte(height):
 for i in range(height):
     for j in range(height):
       if j == 0 or i == height-1:
         print("*",end="")
       else:
           print("",end="")
 print()
height = 5
print_patte(5)
