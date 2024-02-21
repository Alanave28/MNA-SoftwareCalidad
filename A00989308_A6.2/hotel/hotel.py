"""CRUD Hotel"""
import json
import os


class ObjHotel:
    """HOTEL OBJECT"""

    DATA_FILE = "hotel/hotels.json"

    def __init__(self):
        """LOAD DATA SAVED"""
        self.hotels_data = self.load_hotels_data()

    def load_hotels_data(self):
        """READ DATA OF JSON FILE"""
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            return {}

    def display_hotels(self):
        """DISPLAY EACH HOTEL LIST"""
        try:
            if len(self.hotels_data) > 0:
                print("\nHotels Available:")
                for item in self.hotels_data:
                    print(f"{self.hotels_data[item]['hotel_id']}. {self.hotels_data[item]['name']}")
                return 1
            print("\nNo hotels created yet.")
            return 0

        except ValueError as e:
            print(f"Error: {e}")
            return 0

    def create_hotel(self, name, location, available_rooms, reserved_rooms=0):
        """CREATE HOTEL REGISTRATION"""
        for item in self.hotels_data:
            if self.hotels_data[item]['name'] == name:
                return 0

        hotel_id = self._generate_hotel_id()
        self.hotels_data[hotel_id] = {'hotel_id': hotel_id,
                                      'name': name,
                                      'location': location,
                                      'available_rooms': int(available_rooms),
                                      'reserved_rooms': reserved_rooms}
        self._save_hotel_data()
        return 1

    def delete_hotel(self, hotel_id):
        """DELETE HOTEL REGISTRATION"""
        for item in self.hotels_data:
            if self.hotels_data[item]['hotel_id'] == hotel_id:
                del self.hotels_data[item]
                self._save_hotel_data()
                return 1
        return 0

    def display_hotel_info(self, hotel_id):
        """DISPLAY HOTEL INFORMATION"""
        for item in self.hotels_data:
            if self.hotels_data[item]['hotel_id'] == hotel_id:
                print(f"\nHotel ID: {hotel_id}")
                print(f"Name: {self.hotels_data[item]['name']}")
                print(f"Location: {self.hotels_data[item]['location']}")
                print(f"Available Rooms: {self.hotels_data[item]['available_rooms']}")
                print(f"Reserved Rooms: {self.hotels_data[item]['reserved_rooms']}")
                return 1
        return 0

    def modify_hotel_info(self, hotel_id, name, location, rooms):
        """MODIFY HOTEL INFORMATION"""
        for item in self.hotels_data:
            if self.hotels_data[item]['hotel_id'] == hotel_id:
                if name != '':
                    self.hotels_data[item]['name'] = name
                if location != '':
                    self.hotels_data[item]['location'] = location
                if rooms != 0:
                    self.hotels_data[item]['available_rooms'] = rooms
                self._save_hotel_data()
                return 1
        return 0

    def reserve_room(self, hotel_id):
        """CANCEL RESERVATION ADD RESERVED, MINUS AVAILABLE"""
        for item in self.hotels_data:
            if self.hotels_data[item]['hotel_id'] == hotel_id:
                if self.hotels_data[item]['available_rooms'] > 0:
                    self.hotels_data[item]['available_rooms'] -= 1
                    self.hotels_data[item]['reserved_rooms'] += 1
                    self._save_hotel_data()
                    return 1
                return 2
        return 0

    def cancel_reservation(self, hotel_id):
        """CANCEL RESERVATION ADD AVAILABLE, MINUS RESERVED"""
        for item in self.hotels_data:
            if self.hotels_data[item]['hotel_id'] == hotel_id:
                if self.hotels_data[item]['reserved_rooms'] > 0:
                    self.hotels_data[item]['available_rooms'] += 1
                    self.hotels_data[item]['reserved_rooms'] -= 1
                    self._save_hotel_data()
                    return 1
                return 2
        return 0

    def _generate_hotel_id(self):
        """GENERATE NEW ID WHEN CREATE A HOTEL"""
        if not self.hotels_data:
            return 1

        return len(self.hotels_data) + 1

    def _save_hotel_data(self):
        """SAVE DATA IN JSON FILE"""
        with open(self.DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(self.hotels_data, file, indent=4)
