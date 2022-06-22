class ValidateInputUtils:
    @staticmethod
    def numberShouldBetween(low, high, input):
        if not input.isnumeric() or int(input)<low or int(input)>high:
            return None
        return int(input)
        