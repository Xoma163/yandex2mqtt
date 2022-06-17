class Properties:
    def __init__(self, **kwargs):
        self.type = None
        self.retrievable = kwargs.get('retrievable', True)
        self.reportable = kwargs.get('reportable', False)
        self.parameters = {}

    def get_json(self):
        return {
            "type": self.type,
            "retrievable": self.retrievable,
            "reportable": self.reportable,
            "parameters": self.parameters
        }
