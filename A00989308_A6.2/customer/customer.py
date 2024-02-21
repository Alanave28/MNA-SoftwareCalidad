"""CRUD customer"""
import json
import os


class ObjCustomer:
    """CUSTOMER OBJECT"""

    DATA_FILE = "customer/customers.json"

    def __init__(self):
        """LOAD DATA SAVED"""
        self.customer_data = self.load_customer_data()

    def load_customer_data(self):
        """READ DATA OF JSON FILE"""
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        else:
            return {}

    def display_customers(self):
        """DISPLAY EACH CUSTOMER LIST"""
        try:
            if len(self.customer_data) > 0:
                print("\nCustomers Available:")
                for item in self.customer_data:
                    c_id = self.customer_data[item]['cust_id']
                    c_nm = self.customer_data[item]['name']
                    print(f"{c_id}. {c_nm}")
                    return 1

            print("\nNo customer created yet.")
            return 0

        except ValueError as e:
            print(f"Error: {e}")
            return 0

    def create_customer(self, name, email):
        """CREATE CUSTOMER REGISTRATION"""
        for item in self.customer_data:
            if self.customer_data[item]['name'] == name:
                return 0

        cust_id = self._generate_customer_id()
        self.customer_data[cust_id] = {'cust_id': cust_id,
                                       'name': name,
                                       'email': email}
        self._save_customer_data()
        return 1

    def delete_customer(self, cust_id):
        """DELETE CUSTOMER REGISTRATION"""
        for item in self.customer_data:
            if self.customer_data[item]['cust_id'] == cust_id:
                del self.customer_data[item]
                self._save_customer_data()
                return 1
        return 0

    def display_customer_info(self, cust_id):
        """DISPLAY CUSTOMER DATA BY ID"""
        for item in self.customer_data:
            if self.customer_data[item]['cust_id'] == cust_id:
                print(f"\nCustomer ID: {cust_id}")
                print(f"Name: {self.customer_data[item]['name']}")
                print(f"Email: {self.customer_data[item]['email']}")
                return 1
        return 0

    def modify_customer_info(self, cust_id, name, email):
        """MODIFY CUSTOMER INFORMATION"""
        for item in self.customer_data:
            if self.customer_data[item]['cust_id'] == cust_id:
                if name != '':
                    self.customer_data[item]['name'] = name
                if email != '':
                    self.customer_data[item]['email'] = email

                self._save_customer_data()
                return 1
        return 0

    def _generate_customer_id(self):
        """GENERATE NEW ID WHEN CREATE A CUSTOMER"""
        if not self.customer_data:
            return 1

        return len(self.customer_data) + 1

    def _save_customer_data(self):
        """SAVE DATA IN JSON FILE"""
        with open(self.DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(self.customer_data, file, indent=4)
