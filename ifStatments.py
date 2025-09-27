# IF statement 
# if :
# x
# else:
# y

age = int(input("How old are you? "))

if age >= 100: 
  print("You are to old to sign up")
elif age >= 18:
  print("You are now signed up")
elif age < 0:
  print("You haven't been born yet!") 
else:
  print("You must be 18+ to sign up")