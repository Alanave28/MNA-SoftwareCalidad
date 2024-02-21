# pylint: disable=E0401
"""Create and cancel a Reservation"""
import json
import os
from datetime import datetime
from hotel.hotel import ObjHotel as Hotel
from customer.customer import ObjCustomer as Cust


class ObjReservation:
    """RESERVATION OBJECT"""
    DATA_FILE = "reservation/reservation_data.json"

    def __init__(self):
        """LOAD DATA SAVED"""
        self.reservations_data = self.load_reservations_data()

    def load_reservations_data(self):
        """READ DATA OF JSON FILE"""
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            return {}

    def display_reservations(self):
        """DISPLAY EACH CUSTOMER LIST"""
        try:
            if len(self.reservations_data) > 0:
                print("\nReservation ID. Hotel, Customer, Arrival date, Departure Date, Estatus:")
                for item in self.reservations_data:
                    htl = Hotel()
                    cst = Cust()
                    r_id = self.reservations_data[item]['reserv_id']
                    h_id = self.reservations_data[item]['hotel_id']
                    c_id = self.reservations_data[item]['cust_id']

                    for hotel in htl.hotels_data:
                        if htl.hotels_data[hotel]['hotel_id'] == h_id:
                            htl = htl.hotels_data[hotel]['name']
                            break

                    for custo in cst.customer_data:
                        if cst.customer_data[custo]['cust_id'] == c_id:
                            cstm = cst.customer_data[custo]['name']
                            break

                    ar_date = self.reservations_data[item]['arrival_date']
                    dp_date = self.reservations_data[item]['departure_date']
                    stts = self.reservations_data[item]['estatus']

                    print(f"{r_id}. {htl}, {cstm}, {ar_date[:10]}, {dp_date[:10]}, {stts}")
                    return 1

            print("\nNo reservations created yet.")
            return 0

        except ValueError as e:
            print(f"Error: {e}")
            return 0

    def create_reservation(self, customer_id, htl_id, arrival_date, departure_date):
        """CREATE RESERVATION REGISTRATION"""
        date_formatter = "%Y-%m-%d"
        a_date = datetime.strptime(str(arrival_date)[:10], date_formatter).date()
        d_date = datetime.strptime(str(departure_date)[:10], date_formatter).date()

        for item in self.reservations_data:
            if self.reservations_data[item]['cust_id'] == customer_id:
                if self.reservations_data[item]['hotel_id'] == htl_id:
                    if self.reservations_data[item]['estatus'] == 'reserved':
                        fec_res_in = self.reservations_data[item]['arrival_date']
                        f_res_in = datetime.strptime(fec_res_in[:10], date_formatter).date()
                        fec_res_fn = self.reservations_data[item]['departure_date']
                        f_res_fn = datetime.strptime(fec_res_fn[:10], date_formatter).date()

                        if f_res_in <= a_date <= f_res_fn:
                            return 0
                        if f_res_in <= d_date <= f_res_fn:
                            return 0

        htl = Hotel()
        flag = htl.reserve_room(htl_id)

        if flag == 1:
            reservation_id = self._generate_reservation_id()
            self.reservations_data[reservation_id] = {'reserv_id': reservation_id,
                                                      'cust_id': customer_id,
                                                      'hotel_id': htl_id,
                                                      'arrival_date': str(arrival_date),
                                                      'departure_date': str(departure_date),
                                                      'estatus': 'reserved'}
            self._save_reservation_data()
            return 1
        return 2

    def cancel_reservation(self, r_id):
        """CHANGE ESTATUS RESERVATION"""
        for item in self.reservations_data:
            if self.reservations_data[item]['reserv_id'] == r_id:
                if self.reservations_data[item]['estatus'] == 'canceled':
                    return 2

                h_id = self.reservations_data[item]['hotel_id']
                htl = Hotel()
                flag = htl.cancel_reservation(h_id)

                if flag == 1:
                    self.reservations_data[item]['estatus'] = 'canceled'
                    self._save_reservation_data()
                    return 1
        return 3

    def _generate_reservation_id(self):
        """GENERATE NEW ID WHEN CREATE A RESERVATION"""
        if not self.reservations_data:
            return 1
        return len(self.reservations_data) + 1

    def _save_reservation_data(self):
        """SAVE DATA IN JSON FILE"""
        with open(self.DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(self.reservations_data, file, indent=4)
