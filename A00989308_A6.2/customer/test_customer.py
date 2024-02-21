import unittest
from .customer import ObjCustomer

class TestCustomer(unittest.TestCase):

    def test_load_customer_data(self):
        """READ DATA OF JSON FILE"""
        self.cust = ObjCustomer()
        self.assertIsNotNone(self.cust.customer_data)

    def test_display_customers(self):
        """DISPLAY EACH CUSTOMER LIST"""
        self.cust = ObjCustomer()
        self.assertEqual(self.cust.display_customers(), 1)

    def test_create_customer(self):
        """CREATE CUSTOMER REGISTRATION"""
        name = "Avelino Juárez"
        email = "ave@gmail.com"

        self.cust = ObjCustomer()
        self.cust.create_customer(name, email)

        for item in self.cust.customer_data:
            if self.cust.customer_data[item]['name'] == name:
                self.assertEqual(self.cust.customer_data[item]['name'], name)
                self.assertEqual(self.cust.customer_data[item]['email'], email)
                break

    def test_modify_customer_info(self):
        """MODIFY CUSTOMER INFORMATION"""
        name = "Avelino Juárez"
        email = "avelino@gmail.com"
        c_id = 0

        self.cust = ObjCustomer()

        for item in self.cust.customer_data:
            if self.cust.customer_data[item]['name'] == name:
                c_id = self.cust.customer_data[item]['cust_id']

        self.cust.modify_customer_info(c_id, name, email)

        for item in self.cust.customer_data:
            if self.cust.customer_data[item]['name'] == name:
                self.assertEqual(self.cust.customer_data[item]['name'], name)
                self.assertEqual(self.cust.customer_data[item]['email'], email)
                break

    def test_display_customer_info(self):
        """DISPLAY CUSTOMER INFORMATION"""
        self.cust = ObjCustomer()
        self.assertEqual(self.cust.display_customer_info(1), 1)
        self.assertEqual(self.cust.display_customer_info(5), 0)

    def test_delete_customer(self):
        """DELETE CUSTOMER REGISTRATION"""
        name = "Avelino Juárez"

        self.cust = ObjCustomer()

        for item in self.cust.customer_data:
            if self.cust.customer_data[item]['name'] == name:
                c_id = self.cust.customer_data[item]['cust_id']

        self.assertEqual(self.cust.delete_customer(c_id), 1)

        for item in self.cust.customer_data:
            self.assertNotEqual(self.cust.customer_data[item]['cust_id'], c_id)

    def test__generate_customer_id(self):
        """GENERATE NEW ID WHEN CREATE A CUSTOMER"""
        self.cust = ObjCustomer()
        self.assertEqual(self.cust._generate_customer_id(), 3)
        self.assertNotEqual(self.cust._generate_customer_id(), 5)
                
                
if __name__ == '__main__':
    unittest.main()