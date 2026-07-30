print("-------------------TICKETS BOOKING------------------------")
a=input("Enter the date that you want to travel : ")
train_no = int(input("Enter the train number : "))
from_current_location = input("Enter your current destination : ")
to_location = input("Enter your Destination : ")
quota = input("General Quota | Tatkal Quota | Senior Quota : ")
booking_type = input("Individual | Group : ")
name = input("Enter your Name : ")
age = int(input("Enter your Age : "))
gender = input("Enter your Gender : ")
preferences = input("Lower | Middle | Upper | Side-Lower | side-Upper : ")
cost = 0
select_class = input("Select class : --> Sleeper | 1AC | 2AC | 3AC : ")
if(select_class =="sleeper"):
    cost+=500
    print("-------------- TICKET STATUS----------------")
    print(f"Train No : {train_no}\n From : {from_current_location}    To : {to_location}\n Name : {name} , Age : {age} , Gender : {gender}\n Preference : {preferences} , Quota : {quota} , Booking_Type : {booking_type}\n Cost : {cost} , Status : booking")
elif (select_class == "1AC"):
    cost+=2550
    print("-------------- TICKET STATUS----------------")
    print(f"Train No : {train_no}\n From : {from_current_location}    To : {to_location}\n  Name : {name} , Age : {age} , Gender : {gender}\n Preference : {preferences} , Quota : {quota} , Booking_Type : {booking_type}\n Cost : {cost} , Status : booking")
    
elif(select_class == "2AC"):
    cost += 1520
    print("-------------- TICKET STATUS----------------")
    print(f"Train No : {train_no}\n From : {from_current_location}    To : {to_location}\n  Name : {name} , Age : {age} , Gender : {gender}\n Preference : {preferences} , Quota : {quota} , Booking_Type : {booking_type}\n Cost : {cost} , Status : booking")
elif(select_class == "3AC"):
    cost+= 1000
    print("-------------- TICKET STATUS----------------")
    print(f"Train No : {train_no}\n From : {from_current_location}    To : {to_location}\n  Name : {name} , Age : {age} , Gender : {gender}\n Preference : {preferences} , Quota : {quota} , Booking_Type : {booking_type}\n Cost : {cost} , Status : booking")


print("--------------TICKETS DETAILS-----------------")
print(f"Status : Ticket Booked from {from_current_location} to {to_location} on {a}\n  Name : {name}, Age : {age}, Gender : {gender}\n  Preference : {preferences} , Quota : {quota}")
