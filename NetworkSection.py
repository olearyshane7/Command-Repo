# Content of NetworkSection.py
from Section import Section
from CommandButton import CommandButton

class NetworkSection(Section):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, "Network", *args, **kwargs)
        commands = {
            'List Interface IPs': 'diag ip address list',
            'Display IP Pool List': 'diag firewall ippool list',
            'Display IP Pool List': 'diag firewall ippool list',
            'Check Interface List': 'diag netlink interface list',
            'Retrieve ARP Table': 'diag ip arp list',
            'Clear ARP Table': 'exec clear system arp table',
            'Run Ping Test': 'exec ping x.x.x.x',
            'Perform Trace Route': 'exec traceroute x.x.x.x',
            'Start Telnet Utility': 'exec telnet x.x.x.x[port]',
            # ... Add more network commands here
            }
        self.create_buttons(commands)

    def create_buttons(self, commands):
        for desc, command_str in commands.items():
            CommandButton(self, text=desc, command_str=command_str).pack(anchor='w', fill='x')
