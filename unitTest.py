import unittest
from tkinter import Tk
from command_generator import IMEICommandGenerator
from IMEICommandGenerator import IMEICommandGenerator


class TestIMEICommandGenerator(unittest.TestCase):
    def setUp(self):
        self.imei = "359820329511503"
        self.commands = {
            "maintenance lte-at IMEI AT!UIMS=0": f"maintenance lte-at {self.imei} AT!UIMS=0",
            # Add more commands and expected outputs here
        }
        self.root = Tk()
        self.generator = IMEICommandGenerator(self.root)
        self.generator.imei_entry.insert(0, self.imei)

    def tearDown(self):
        self.root.destroy()

    def test_generate_command(self):
        for action, command in self.commands.items():
            with self.subTest(command=command):
                output = self.generator.generate_command(action)
                expected_output = command.replace("IMEI", self.imei)
                self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
