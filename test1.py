# def print_table():
#     number = input("Enter a numer for which you want to write a table: ")
#     if number.isdigit():
#         number = int(number)
#         if number <= 0:
#             print("The number should be greater than 0")
#             print_table()
#         else:
#             i = 1
#             for i in range(1, 11):
#                 print(f"{number} * {i} = {number * i}")
#     else:
#         print("You'r input should be a number!")
#         print_table()  

# print_table()

name = input("Enter your full-name: ")
def print_name(name):
    print(f"Hello {name}")
    username = name.lower()
    username = username.replace(" ","_")
    print(f"You'r username is ${username}")

print_name(name)