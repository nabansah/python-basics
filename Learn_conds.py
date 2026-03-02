# elif  age
age = int(input("Enter your age: "))
day = int(input("Enter weekday (0=Monday, 6=Sunday): "))

ticket_price = 12 if age >= 18 else 8

if day >= 5: # weekend
        ticket_price -= 2

if(age <13 ):
    # print("You are a child.")
    print(ticket_price)
elif(age >= 13 and age <= 19):
    # print("You are a teenager.")
 print(ticket_price)
elif(age >= 20 and age <= 59):
    # print("You are an adult.")
    print(ticket_price)
elif(age >= 60):
    # print("You are a senior.")
    print(ticket_price)




