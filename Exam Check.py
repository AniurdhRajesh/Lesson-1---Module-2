while True:
 x=input("Do you have Medical Certificate ? Yes or No(In CAPS)\n")
 if x=="YES":
  y=int(input("What is your Attenance Percentage : (No need for (%) symbol)"))
  if y>=75:
    print("You are permitted to retake exam")
  elif y<75:
    print("You Are NOT permitted to retake exam") 
  else:
   print("Please enter a valid answer")
 elif x=="NO":
  print("You Are NOT permitted to retake exam")
 else:
     print("Please enter a valid answer")