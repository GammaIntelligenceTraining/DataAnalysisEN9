# while True:
#     print("I can't stop")

# while True:
#     name = input("Enter name (enter 'EXIT' to quit): ").strip()
#     if not name:
#         print("Name should not be empty")
#         continue
#     elif name.lower() == 'exit':
#         print('Good bye')
#         quit()
#     else:
#         print("Hello", name)
#         break

# print('My last message!')

# counter = 0
# while counter < 100:
#     counter += 1
#     print(counter)

while True:
    user_input = input('Choose:\n' \
                        '1.Say hello\n' \
                        '2.Say good bye\n' \
                        '3.Laugh\n' \
                        '0.Exit\n' \
                        '-> ')
    if user_input == '1':
        print("HELLO")
    elif user_input == '2':
        print("GOOD BYE")
    elif user_input == '3':
        print("HA HA HA")
    elif user_input == '0':
        print("Exiting...")
        quit()
    else:
        print("Choice is out of range")