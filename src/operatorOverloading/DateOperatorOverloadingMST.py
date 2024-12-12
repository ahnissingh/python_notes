class Date:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.__day = day
        self.__month = month
        self.__year = year

    def __eq__(self, other) -> bool:
        if not isinstance(other, Date):
            return False
        return (
                self.__day == other.__day and
                self.__month == other.__month and
                self.__year == other.__year
        )

    def __ne__(self, other) -> bool:
        """
        self == other uses your previously defined __eq__ method.
        By using not self == other, you are leveraging the existing
        logic in your __eq__ method to avoid code duplication.
        """
        return not self == other
