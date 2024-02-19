class GroupConfig:
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
            # Add more groups as needed
        }

    def get_group_config(self, group):
        return self.config_template.get(group, {})