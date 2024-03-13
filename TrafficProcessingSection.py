from Section import Section
from CommandButton import CommandButton

class TrafficProcessingSection(Section):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, "Traffic Processing", *args, **kwargs)
        commands = {
            'Realtime App Debugging': 'diag debug app [app] [level]',
            'App Layer Debugging': 'diag debug app [app] [level]',
            'Proxy Operation Monitor': 'diag test appl [app] [test_level]',
            'Toggle Timestamp in Console': 'diag debug console timestamp [enable|disable]',
            'Toggle Debug Output': 'diag debug [enable|disable]',
            'Reset Debug Levels': 'diag debug reset',
            'Filter Session List': 'diag sys session filter',
            'List Sessions': 'diag sys session list [expect]',
            'Clear Sessions': 'diag sys session clear',
            'Display Session Stats': 'diag sys session stat',
            'Lookup Firewall Policy': 'diag firewall iprope clear 100004 [<id>]',
            # ... Add more traffic processing commands here
        }
        self.create_buttons(commands)

    def create_buttons(self, commands):
        for desc, command_str in commands.items():
            CommandButton(self, text=desc, command_str=command_str).pack(anchor='w', fill='x')