from Section import Section
from CommandButton import CommandButton

class SystemSection(Section):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, "System", *args, **kwargs)
        commands = {
            'View System Status': 'get system status',
            'Generate Support Report': 'exec tac report',
            'List CLI Commands': 'tree',
            'CLI Help Tips': '<command> ? / tab [filter]',
            'Filter CLI Outputs': '<command> | grep [filter]',
            'Monitor CLI WebGUI Changes': 'diag debug cli 8',
            'Check Performance Info': 'get system performance status',
            'View Process List': 'diag sys top [sec] [number]',
            'See Crash Log History': 'diag debug crashlog history',
            'Read Crash Log': 'diag debug crashlog read',
            # ... Add more system commands here
        }
        self.create_buttons(commands)

    def create_buttons(self, commands):
        for desc, command_str in commands.items():
            CommandButton(self, text=desc, command_str=command_str).pack(anchor='w', fill='x')