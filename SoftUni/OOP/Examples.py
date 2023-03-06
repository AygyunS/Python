class Phone:
    def __init__(self, number, call_history=[]):
        self.number = number
        self.call_history = []

        def call(self, other_number):
            self.call_history.append(other_number)