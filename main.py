from art import logo
from replit import clear
print(logo)

operators={"+":"addition", "-":"subtraction", "*":"multiplication", "/":"division"}

def calculator(first_num, sec_num, operator):
  if operator=="+":
    result=first_num+sec_num
  elif operator=="-":
    result=first_num-sec_num
  elif operator=="*":
    result=first_num*sec_num
  elif operator=="/":
    result=first_num/sec_num
  return result

def calculation():
  print("Addition: + \nSubtraction: - \nMultiplication: * \nDivision: / \n")
  first_number=float(input("Enter first number: "))
  second_number=float(input("Enter second number: "))
  user_operator=input("Enter operator: ")
  final_result= calculator(first_number,second_number, user_operator)
  print(f"The result is {final_result}")
  ask_cont=input("Do you want to continue or not? Type 'Y' for Yes and 'N' for No: ")

  if ask_cont=="Y":
    while ask_cont=="Y":
      third_num=float(input("Enter the next number: "))
      next_operator=input("Enter next operator: ")
      final_result= calculator(final_result, third_num, next_operator)
      print(f"The result is {final_result}")
      ask_cont=input("Do you want to continue or not? Type 'Y' for Yes and 'N' for No: ")
    else:
      clear()
      calculation()
  elif ask_cont=="N":
      clear()
      calculation()

calculation()
