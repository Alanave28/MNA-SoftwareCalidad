import unittest
from .hotel import ObjHotel

class TestHotel(unittest.TestCase):

    def test_load_hotels_data(self):
        """READ DATA OF JSON FILE"""
        self.hotel = ObjHotel()
        self.assertIsNotNone(self.hotel.hotels_data)

    def test_display_hotels(self):
        """DISPLAY EACH HOTEL LIST"""
        self.hotel = ObjHotel()
        self.assertAlmostEqual(self.hotel.display_hotels(), 1)

    def test_create_hotel(self):
        """CREATE HOTEL REGISTRATION"""
        name = "California"
        location = "Los Angeles"
        rooms = 27

        self.hotel = ObjHotel()
        self.hotel.create_hotel(name, location, rooms)

        for item in self.hotel.hotels_data:
            if self.hotel.hotels_data[item]['name'] == name:
                self.assertEqual(self.hotel.hotels_data[item]['name'], name)
                self.assertEqual(self.hotel.hotels_data[item]['location'], location)
                self.assertEqual(self.hotel.hotels_data[item]['available_rooms'], rooms)
                self.assertEqual(self.hotel.hotels_data[item]['reserved_rooms'], 0)
                break

    def test_modify_hotel_info(self):
        """MODIFY HOTEL INFORMATION"""
        name = "California"
        location = "Mexico"
        rooms = 28
        h_id = 0

        self.hotel = ObjHotel()

        for item in self.hotel.hotels_data:
            if self.hotel.hotels_data[item]['name'] == name:
                h_id = self.hotel.hotels_data[item]['hotel_id']

        self.hotel.modify_hotel_info(h_id, name, location, rooms)

        for item in self.hotel.hotels_data:
            if self.hotel.hotels_data[item]['name'] == name:
                self.assertEqual(self.hotel.hotels_data[item]['name'], name)
                self.assertEqual(self.hotel.hotels_data[item]['location'], location)
                self.assertEqual(self.hotel.hotels_data[item]['available_rooms'], rooms)
                self.assertEqual(self.hotel.hotels_data[item]['reserved_rooms'], 0)
                break

    def test_display_hotel_info(self):
        """DISPLAY HOTEL INFORMATION"""
        self.hotel = ObjHotel()
        self.assertEqual(self.hotel.display_hotel_info(2), 1)
        self.assertEqual(self.hotel.display_hotel_info(5), 0)

    def test_delete_hotel(self):
        """DELETE HOTEL REGISTRATION"""
        name = "California"

        self.hotel = ObjHotel()

        for item in self.hotel.hotels_data:
            if self.hotel.hotels_data[item]['name'] == name:
                h_id = self.hotel.hotels_data[item]['hotel_id']

        self.assertEqual(self.hotel.delete_hotel(h_id), 1)

        for item in self.hotel.hotels_data:
            self.assertNotEqual(self.hotel.hotels_data[item]['hotel_id'], h_id)

    def test__generate_hotel_id(self):
        """GENERATE NEW ID WHEN CREATE A HOTEL"""
        self.hotel = ObjHotel()
        self.assertEqual(self.hotel._generate_hotel_id(), 3)
        self.assertNotEqual(self.hotel._generate_hotel_id(), 5)

if __name__ == '__main__':
    unittest.main()