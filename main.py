import user
import flight
import booking
import admin

print("1. Register User")
print("2. Login User")
print("3. Delete User")
print("4. Update User")
print("5. Admin")
print("6. Quit")

num = int(input("Enter the Number of the choice : "))

while num != 5:
    
    if num == 1:
        user_id = input("Enter User ID : ")
        name = input("Enter Name : ")
        email = input("Enter E-Mail : ")
        password = input("Enter Password : ")
        phone = input("Enter Phone Number : ")
        
        user.register_user(user_id,name,email,password,phone)
        
    elif num == 2:
        
        email = input("Enter E-Mail : ")
        password = input("Enter Password : ")
        
        valid = user.login_user(email,password)
        
        if valid:
            while True:
                print("1. Flights Details")
                print("2. Booking Tickets of Flights")
                print("3. Payments")
                print("4. Quit")
                
                num_login = int(input("Enter the Choice : "))
                
                if num_login == 1:
                    while True:
                        print("1. List All Flights")
                        print("2. Get Flight Details")
                        print("3. Search Your Flight")
                        print("4. Quit")
                        
                        num_flight = int(input("Enter Number to Search Flight or Get Deatils of Flight :"))
                        
                        if num_flight == 1:
                            flight.list_All_flights()
                            
                        elif num_flight == 2:
                            flight.get_flight_details()
                            
                        elif num_flight == 3:
                            flight.search_your_flight()
                            
                        elif num_flight == 4:
                            print("Thank You !!!")
                            break
                elif num_login == 2:
                    while True:
                        print("1. Book Flight Tickets")
                        print("2. Cancel Booking")
                        print("3. See Booking History")
                        print("5. Quit")
                        
                        num_book = int(input("Enter the Number to View : "))
                        
                        if num_login == 1:
                            
                            booking.book_tickets()
                            
                        elif num_login == 2:
                            
                            booking.cancel_booking()
                        
                        elif num_login == 3:
                            booking.view_booking_history()
                            
                        elif num_login == 4:
                            
                            booking.modify_booking()
                        
                        elif num_login == 5:
                            
                            break
                        
                        else:
                            print("Invalid Number !!!!")
                elif num_login == 3:
                    flight.search_your_flight()
        
    
    elif num == 3:
        email = input("Enter E-Mail to Delete the user : ")
        user.delete_user(email)
        
    elif num == 4:
        user.update_profile()
    
    elif num == 5:
        
        print("1. To Add a Flight")
        print("2. To Modify the Flight Detail")
        print("3. Delete the Flight")
        print("4. View all Bookings")
        print("5. View all Users ")
        print("6. View all flights")
        print("7. Quit")
        
        admin_num = int(input("Enter The Number to View or Modify : "))
        
        if admin_num == 1:
            admin.add_flight()
        elif admin_num == 2:
            admin.update_flight_details()
        elif admin_num == 3:
            admin.delete_flight()
        elif admin_num == 4:
            admin.view_all_bookings()
        elif admin_num == 5:
            admin.view_all_users()
        elif admin_num == 6:
            admin.view_all_flights()
        elif admin_num == 7:
            break
        else:
            print("Invalid Number !!!")
            
            
    elif num == 6:
        break
    
    else:
        print("Invalid Number !!!")
    
