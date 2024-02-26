import pyperclip
import logging
from tkinter import messagebox

class InvalidStateException(Exception):
    pass

def generate_config(state_entry):
    state = state_entry.get().upper()

    region1 = ['AK', 'WA', 'MT', 'OR', 'ID', 'WY', 'NV', 'CA', 'UT', 'CO', 'NM', 'AZ']
    region2 = ['TX', 'OK', 'AR', 'LA', 'MS', 'TN', 'AL', 'GA', 'SC', 'NC', 'FL']
    region3 = ['ND', 'SD', 'NE', 'KS', 'MN', 'IA', 'MO', 'WI', 'MI', 'IN', 'IL', 'KY', 'OH', 'PA', 'WV']
    region4 = ['ME', 'VT', 'NH', 'MA', 'CT', 'RI', 'NY', 'PA', 'NJ', 'DE', 'DC', 'MD', 'VA']

    try:
        if state in region1:
            regional_apn = 'WE01.VZWSTATIC'
        elif state in region2:
            regional_apn = 'SO01.VZWSTATIC'
        elif state in region3:
            regional_apn = 'MW01.VZWSTATIC'
        elif state in region4:
            regional_apn = 'NE01.VZWSTATIC'
        else:
            raise InvalidStateException(f"Invalid state entered: {state}") 

        config_template = f"""
configure
pdp-profile "VZ-Static"
apn-id "1"
apn {regional_apn}
back
mobile-country-code "311"
mobile-network-code "480"
back
commit
main"""
        pyperclip.copy(config_template)
        messagebox.showinfo("Config Generated", "Configuration copied to clipboard.")

    except InvalidStateException as e:
        logging.error(f"Invalid state entered: {state} - {e}")
        messagebox.showerror("Invalid State", str(e))
