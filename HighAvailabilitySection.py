from Section import Section
from CommandButton import CommandButton

class HighAvailabilitySection(Section):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, "High Availability", *args, **kwargs)
        commands = {
            'Check HA Status':'get sys ha status',
            'Manage HA Nodes':'exec ha manage [input] [input]',
            'View HA Event History':'diag sys ha history read',
            'Monitor HA Uptime':'diag sys ha reset-uptime', 
            'HA Debug Application':'diag debug app ike -1', 
            'Bypass HA Revision Check':'exec ha ignore-hardware-revision status / enable / disable',
            'Check Failover Status':'exec ha failover status',
            'Trigger HA Failover':'exec ha failover set [input]',
            # ... Add more high availability commands here
        }
        self.create_buttons(commands)

    def create_buttons(self, commands):
        for desc, command_str in commands.items():
            CommandButton(self, text=desc, command_str=command_str).pack(anchor='w', fill='x')