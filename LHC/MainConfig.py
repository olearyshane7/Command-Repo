import tkinter as tk
from tkinter import scrolledtext, messagebox

class ConfigTemplate:
    def __init__(self):
        self.config_template = {
            "LHC Group": {
                "Router": "GFLEX-1000-4C8R-LTE",
                "Access Point": None,
                "Switch": None,
                "Switch2": None
            },
            "Western Shamrock": {
                "Router": "GFLEX-1000-4C8R-LTE",
                "Access Point": "AP33-US",
                "Switch": "EX2300-C-12P",
                "Switch2": "EX2300-24P"
            },
            "Hanger" : {
                "Router" : "GFLEX-1000-4C8R-LTE",
                "Access Point" : "AP34-US",
                "Switch" : "EX2300-48P" ,
                "Switch2" : "EX2300-24P" ,
            }
        }


#         self.config_template_IMEI = f"""
# configure
#     pdp-profile "VZ-Static"
#         apn-id "1"
#             apn {regional_apn}
#             back
#         mobile-country-code "311"
#         mobile-network-code "480"
#         back
#     commit
# main"""