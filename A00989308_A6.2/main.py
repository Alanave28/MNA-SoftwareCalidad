"""Reservation System"""
from datetime import datetime
from customer.customer import ObjCustomer as Cust
from hotel.hotel import ObjHotel as Hotel
from reservation.reservation import ObjReservation as Reserv

hotel_manager = Hotel()
cust_manager = Cust()
reserv_manager = Reserv()

print("Welcome to Reservation Hotel System")

while True:
    print("\nPlease select an option from our menu:")
    print("1 - Display Hotels")
    print("1.1 - Create Hotel")
    print("1.2 - Delete Hotel")
    print("1.3 - Display Hotel Information")
    print("1.4 - Modify Hotel Information")
    print("2 - Display Customers")
    print("2.1 - Create Customer")
    print("2.2 - Delete Customer")
    print("2.3 - Display Customer Information")
    print("2.4 - Modify Customer Information")
    print("3 - Display Reservations")
    print("3.1 - Create a Reservation")
    print("3.2 - Cancel a Reservation")
    print("10 - Quit")

    choice = input("Seleccione una opción: ")

    if choice == "1":
        hotel_manager.display_hotels()
    elif choice == "1.1":
        name = input("Write hotel name: ")
        location = input("Write hotel location: ")

        while True:
            try:
                num_rooms = input("Write Number of Rooms Available: ")
                num = int(num_rooms)
                FLAG = hotel_manager.create_hotel(name.upper(), location.upper(), num)

                if FLAG == 1:
                    print(f"Hotel '{name.upper()}' created successfully.")
                else:
                    print(f"Hotel {name.upper()} already exist.")
                    print("Please select another choice.")
                break
            except ValueError:
                print("\nWarning: Please enter a number\n")

    elif choice == "1.2":
        print("\nSelect a Hotel ID please")
        hotel_manager.display_hotels()
        while True:
            try:
                hotel_id = input("Enter a Hotel ID please: ")
                h_id = int(hotel_id)
                FLAG = hotel_manager.delete_hotel(h_id)

                if FLAG == 1:
                    print("Hotel deleted successfully.")
                else:
                    print("Please select another choice.")
                break
            except ValueError:
                print("\nNot is a Number. Do you want continue(1 - Yes, 2 - No):")
                try:
                    cont = input("Enter your choice: ")
                    decision = int(cont)
                    if decision == 1:
                        continue

                    break
                except ValueError:
                    print("\nWarning: Please enter a number\n")
                    break
    elif choice == "1.3":
        print("\nSelect a Hotel ID please")
        hotel_manager.display_hotels()

        while True:
            try:
                hotel_id = input("Enter a Hotel ID please: ")
                h_id = int(hotel_id)
                FLAG = hotel_manager.display_hotel_info(h_id)

                if FLAG == 0:
                    print("Hotel not identified.")
                break
            except ValueError:
                print("\nNot is a Number. Do you want continue(1 - Yes, 2 - No):")
                try:
                    cont = input("Enter your choice: ")
                    decision = int(cont)
                    if decision == 1:
                        continue

                    break
                except ValueError:
                    print("\nWarning: Please enter a number\n")
                    break
    elif choice == "1.4":
        print("\nSelect a Hotel ID please")
        hotel_manager.display_hotels()

        while True:
            try:
                hotel_id = input("Enter a Hotel ID please: ")
                h_id = int(hotel_id)
                FLAG = hotel_manager.display_hotel_info(h_id)
                if FLAG == 1:
                    try:
                        cont = input("Dou you want change Hotel name? (1 - Yes, 2 - No): ")
                        decision = int(cont)
                        if decision == 1:
                            NM = input("Enter new Hotel name: ")
                        else:
                            NM = ''

                        cont = input("Dou you want change Hotel location? (1 - Yes, 2 - No): ")
                        decision = int(cont)
                        if decision == 1:
                            LCT = input("Enter new Hotel location: ")
                        else:
                            LCT = ''

                        cont = input("Dou you want change Hotel number rooms? (1 - Yes, 2 - No): ")
                        decision = int(cont)
                        if decision == 1:
                            rms = input("Enter new Hotel number rooms: ")
                            N_R = int(rms)
                        else:
                            N_R = 0
                    except ValueError:
                        print("\nWarning: Please enter a number\n")
                        break
                else:
                    print("Hotel not identified.")
                    break

                if NM == '' and LCT == '' and N_R == 0:
                    FLAG = 0
                else:
                    FLAG = hotel_manager.modify_hotel_info(h_id, NM.upper(), LCT.upper(), N_R)

                if FLAG == 1:
                    print("Hotel modified successfully.")
                    hotel_manager.display_hotel_info(h_id)
                else:
                    print("Hotel not modified. Please enter another choice.")

                break
            except ValueError:
                print("\nNot is a Number. Do you want continue(1 - Yes, 2 - No):")
                try:
                    cont = input("Enter your choice: ")
                    decision = int(cont)
                    if decision == 1:
                        continue

                    break
                except ValueError:
                    print("\nWarning: Please enter a number\n")
                    break
    elif choice == "2":
        cust_manager.display_customers()
    elif choice == "2.1":
        name = input("Write customer name: ")

        while True:
            email = input("Write customer email: ")
            if '@' in email:
                break

            print("Please enter a valid email.")

        FLAG = cust_manager.create_customer(name.upper(), email.lower())

        if FLAG == 1:
            print(f"Customer '{name.upper()}' created successfully.")
        else:
            print(f"Customer {name.upper()} already exist.")
            print("Please select another choice.")
    elif choice == "2.2":
        print("\nSelect a Customer ID please")
        cust_manager.display_customers()

        while True:
            try:
                cust_id = input("Enter a Customer ID please: ")
                c_id = int(cust_id)
                FLAG = cust_manager.delete_customer(c_id)

                if FLAG == 1:
                    print("Customer deleted successfully.")
                else:
                    print("Please select another choice.")
                break
            except ValueError:
                print("\nNot is a Number. Do you want continue(1 - Yes, 2 - No):")
                try:
                    cont = input("Enter your choice: ")
                    decision = int(cont)
                    if decision == 1:
                        continue

                    break
                except ValueError:
                    print("\nWarning: Please enter a number\n")
                    break
    elif choice == "2.3":
        print("\nSelect a Customer ID please")
        cust_manager.display_customers()

        while True:
            try:
                cust_id = input("Enter a Customer ID please: ")
                c_id = int(cust_id)
                FLAG = cust_manager.display_customer_info(c_id)

                if FLAG == 0:
                    print("Customer not identified.")
                break
            except ValueError:
                print("\nNot is a Number. Do you want continue(1 - Yes, 2 - No):")
                try:
                    cont = input("Enter your choice: ")
                    decision = int(cont)
                    if decision == 1:
                        continue

                    break
                except ValueError:
                    print("\nWarning: Please enter a number\n")
                    break
    elif choice == "2.4":
        print("\nSelect a Customer ID please")
        cust_manager.display_customers()

        while True:
            try:
                cust_id = input("Enter a Customer ID please: ")
                c_id = int(cust_id)
                FLAG = cust_manager.display_customer_info(c_id)
                if FLAG == 1:
                    try:
                        cont = input("Dou you want change Customer name? (1 - Yes, 2 - No): ")
                        decision = int(cont)
                        if decision == 1:
                            NM = input("Enter new Customer name: ")
                        else:
                            NM = ''

                        cont = input("Dou you want change Customer email? (1 - Yes, 2 - No): ")
                        decision = int(cont)
                        if decision == 1:
                            while True:
                                ML = input("Enter new Customer email: ")
                                if '@' in ML:
                                    break

                                print("Please enter a valid email.")
                        else:
                            ML = ''

                    except ValueError:
                        print("\nWarning: Please enter a number\n")
                        break
                else:
                    print("Customer not identified.")
                    break

                if NM == '' and ML == '':
                    FLAG = 0
                    print("Customer not modified. Please enter another choice.")
                else:
                    FLAG = cust_manager.modify_customer_info(c_id, NM.upper(), ML.lower())

                if FLAG == 1:
                    print("Customer modified successfully.")
                    cust_manager.display_customer_info(c_id)

                break
            except ValueError:
                print("\nNot is a Number. Do you want continue(1 - Yes, 2 - No):")
                try:
                    cont = input("Enter your choice: ")
                    decision = int(cont)
                    if decision == 1:
                        continue

                    break
                except ValueError:
                    print("\nWarning: Please enter a number\n")
                    break
    elif choice == "3":
        reserv_manager.display_reservations()
    elif choice == "3.1":
        hotel_manager.display_hotels()
        while True:
            try:
                hotel_id = input("\nSelect Hotel ID: ")
                h_id = int(hotel_id)

                if str(h_id)not in list(hotel_manager.hotels_data.keys()):
                    print("\nWarning: Hotel ID not exist.\n")
                    continue

                break
            except ValueError:
                print("\nWarning: Please enter a number\n")

        cust_manager.display_customers()
        while True:
            try:
                cust_id = input("\nSelect Customer ID: ")
                c_id = int(cust_id)

                if str(c_id)not in list(cust_manager.customer_data.keys()):
                    print("\nWarning: Customer ID not exist.\n")
                    continue

                break
            except ValueError:
                print("\nWarning: Please enter a number\n")

        print("\nPlease use this format (aaaa-mm-dd)")
        DATEFORMATTER = "%Y-%m-%d"
        while True:
            try:
                fecha_ini = input("What is the entry date? ")
                f_ini = datetime.strptime(fecha_ini, DATEFORMATTER)
                break
            except ValueError:
                print("\nWarning: Please enter a valid date\n")

        while True:
            try:
                fecha_fin = input("What is the departure date? ")
                f_fin = datetime.strptime(fecha_fin, DATEFORMATTER)

                if f_fin.date() < f_ini.date():
                    print("\nWarning: Please enter a valid departure date\n")
                    continue

                break
            except ValueError:
                print("\nWarning: Please enter a valid date\n")

        FLAG = reserv_manager.create_reservation(c_id, h_id, f_ini, f_fin)

        if FLAG == 1:
            print("Reservation created successfully.")
        elif FLAG == 2:
            print("No rooms available.")
        else:
            print("Dates not available.")
    elif choice == "3.2":
        print("\nSelect reservation to cancel please")
        reserv_manager.display_reservations()

        while True:
            try:
                reserv_id = input("\nEnter a Reservation ID please: ")
                r_id = int(reserv_id)

                if str(r_id)not in list(reserv_manager.reservations_data.keys()):
                    print(f"Reservation {r_id} does not exist.")
                    continue

                FLAG = reserv_manager.cancel_reservation(r_id)

                if FLAG == 1:
                    print("\nReservation canceled successfully.")
                elif FLAG == 2:
                    print("\nReservation already canceled.")
                else:
                    print(f"\nReservation {r_id} does not exist.")
                break
            except ValueError:
                print("\nNot is a Number. Do you want continue(1 - Yes, 2 - No):")
                try:
                    cont = input("Enter your choice: ")
                    decision = int(cont)
                    if decision == 1:
                        continue

                    break
                except ValueError:
                    print("\nWarning: Please enter a number\n")
                    break

    elif choice == "10":
        print("\nSee you soon!\n")
        break
