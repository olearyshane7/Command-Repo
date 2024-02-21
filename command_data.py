# command_data.py
commands = {
    "Swap to Port 1": "maintenance lte-at IMEI AT!UIMS=0",
    "Swap to Port 2": "maintenance lte-at IMEI AT!UIMS=1",
    "Check APN Flex is using": "maintenance lte-at IMEI AT+CGDCONT\?",
    "Flush APN Flex is using": "maintenance lte-at IMEI AT+CGDCONT=1",
    "Reboot the LTE Modem": "maintenance lte-at IMEI AT+CFUN=6",
    "Check which sim slot is being used": "maintenance lte-at IMEI AT\!UIMS\?",
    "TMO/ATT Firmware Update": "maintenance lte-at IMEI AT!IMPREF=\"GENERIC\"",
    "Verizon Firmware Update": "maintenance lte-at IMEI AT!IMPREF=\"VERIZON\""
}
