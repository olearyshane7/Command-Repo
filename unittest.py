import unittest
from tkinter import Tk, ttk, messagebox
from myapp import IMEICommandGenerator
import pyperclip
from UpdateIPConfig import generate_ip_config

class TestUpdateIpConfig(unittest.TestCase):
    def test_generate_config(self):
        config_instance = generate_ip_config("eth0", "192.168.1.1/24", 100, "10.0.0.1", "172.16.0.0/24")
        generated_config = config_instance.generate_config()
        expected_config = """
interface ip eth0
ip-addr 192.168.1.1/24
back
-------------------------------------
vrf "public-vrf-100"
ip-route 0.0.0.0/0
gateway "10.0.0.1"
back
---------------------------------------
ip-route 172.16.0.0/24
interface "eth0"
back
back
--------------------------------------
applications
hybrid-wan
profile basic
interfaces
wan-port eth0
gateway-ip 10.0.0.1
commit
"""
        self.assertEqual(generated_config.strip(), expected_config.strip())

class TestIMEICommandGenerator(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = IMEICommandGenerator(self.root)
        self.app.update_ip_config = generate_ip_config("eth0", "192.168.1.1/24", 100, "10.0.0.1", "172.16.0.0/24")

    def tearDown(self):
        self.root.destroy()

    def test_update_values(self):
        # Test when all fields are filled
        self.app.ip_interface_entry.insert(0, "eth1")
        self.app.usable_cidr_entry.insert(0, "192.168.2.1/24")
        self.app.vrf_number_entry.insert(0, "200")
        self.app.gateway_ip_entry.insert(0, "10.0.0.2")
        self.app.network_cidr_entry.insert(0, "192.168.3.0/24")

        self.app.update_values()

        self.assertEqual(self.app.update_ip_config.ip_interface, "eth1")
        self.assertEqual(self.app.update_ip_config.usable_in_cidr, "192.168.2.1/24")
        self.assertEqual(self.app.update_ip_config.vrf_number, 200)
        self.assertEqual(self.app.update_ip_config.gw_ip, "10.0.0.2")
        self.assertEqual(self.app.update_ip_config.network_in_cidr, "192.168.3.0/24")

        # Test when some fields are empty
        self.app.ip_interface_entry.delete(0, 'end')
        self.app.vrf_number_entry.delete(0, 'end')
        self.app.network_cidr_entry.delete(0, 'end')

        with self.assertRaisesRegex(tkMessageBox, "All fields must be filled."):
            self.app.update_values()

    def test_ipupdate(self):
        # Insert values into Entry widgets
        self.app.ip_interface_entry.insert(0, "eth1")
        self.app.usable_cidr_entry.insert(0, "192.168.2.1/24")
        self.app.vrf_number_entry.insert(0, "200")
        self.app.gateway_ip_entry.insert(0, "10.0.0.2")
        self.app.network_cidr_entry.insert(0, "192.168.3.0/24")

        with self.subTest("Test successful ipupdate"):
            self.app.ipupdate()
            # Check if the generated configuration is copied to the clipboard
            self.assertNotEqual(pyperclip.paste(), "")
            # Check if a message box is displayed
            self.assertTrue(tkMessageBox.showinfo.called)

if __name__ == '__main__':
    unittest.main()