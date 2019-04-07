from enum import Enum

class TimeRanges(Enum):
    FIVE_YEARS = "5y"
    TWO_YEARS = "2y"
    ONE_YEAR = "1y"
    YEAR_TO_CURRENT_DATE = "ytd"
    SIX_MONTHS = "6m"
    THREE_MONTHS = "3m"
    ONE_MONTH = "1m"
    ONE_DAY = "1d"
    CUSTOM_DATE = "Fecha en formato YYYYMMDD"
    DYNAMIC = "dynamic"

    @classmethod
    def return_time_ranges(self):
        return [time.value for time in TimeRanges]

    @classmethod
    def check_if_range_exists(self, range):
        if range in self.return_time_ranges():
            return True
        else:
            return False