import unittest
from datetime import datetime
from .reservation import ObjReservation

class TestReservation(unittest.TestCase):

    def test_load_reservations_data(self):
        """READ DATA OF JSON FILE"""
        self.reserv = ObjReservation()
        self.assertIsNotNone(self.reserv.reservations_data)

    def test_display_reservations(self):
        """DISPLAY EACH RESERVATION LIST"""
        self.reserv = ObjReservation()
        self.assertEqual(self.reserv.display_reservations(), 1)

    def test_create_reservation(self):
        """CREATE RESERVATION REGISTRATION"""
        DATEFORMATTER = "%Y-%m-%d"
        f_ini = datetime.strptime('2023-03-20', DATEFORMATTER)
        f_fin = datetime.strptime('2023-03-22', DATEFORMATTER)

        self.reserv = ObjReservation()
        
        self.assertEqual(self.reserv.create_reservation(1, 1, f_ini, f_fin), 1)
        self.assertEqual(self.reserv.create_reservation(1, 1, f_ini, f_fin), 0)

        for item in self.reserv.reservations_data:
            if self.reserv.reservations_data[item]['arrival_date'] == str(f_ini):
                self.assertEqual(self.reserv.reservations_data[item]['cust_id'], 1)
                self.assertEqual(self.reserv.reservations_data[item]['hotel_id'], 1)
                self.assertEqual(self.reserv.reservations_data[item]['arrival_date'], str(f_ini))
                self.assertEqual(self.reserv.reservations_data[item]['departure_date'], str(f_fin))
                self.assertEqual(self.reserv.reservations_data[item]['estatus'], 'reserved')
                break

    def test_cancel_reservation(self):
        """CHANGE ESTATUS RESERVATION"""
        DATEFORMATTER = "%Y-%m-%d"
        f_ini = datetime.strptime('2023-12-10', DATEFORMATTER)
        f_fin = datetime.strptime('2023-12-11', DATEFORMATTER)
        r_id = 0

        self.reserv = ObjReservation()

        for item in self.reserv.reservations_data:
            if self.reserv.reservations_data[item]['arrival_date'] == str(f_ini):
                if self.reserv.reservations_data[item]['departure_date'] == str(f_fin):
                    r_id = self.reserv.reservations_data[item]['reserv_id']
        
        self.assertEqual(self.reserv.cancel_reservation(r_id), 1)
        self.assertEqual(self.reserv.cancel_reservation(r_id), 2)
        self.assertEqual(self.reserv.cancel_reservation(10), 3)

        for item in self.reserv.reservations_data:
            if self.reserv.reservations_data[item]['reserv_id'] == r_id:
                self.assertEqual(self.reserv.reservations_data[item]['estatus'], 'canceled')
                break

    def test__generate_reservation_id(self):
        """GENERATE NEW ID WHEN CREATE A RESERVATION"""
        self.reserv = ObjReservation()
        self.assertEqual(self.reserv._generate_reservation_id(), 4)
        self.assertNotEqual(self.reserv._generate_reservation_id(), 5)
                
if __name__ == '__main__':
    unittest.main()