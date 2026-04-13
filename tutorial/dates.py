# 
# Filename: dates.py
# Author: Nina Nyback
# date: 15 Oct 2025
# description: Date class
# This is all my own work as per the College's
# Academic Integrity Policy (copied from Moodle)
# 
class DateOutOfRange(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)
class Date:
    def __init__(self, year: int, month:int, day:int) -> None:
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self) -> int:
        return self.__day
    
    @property
    def month(self) -> int:
        return self.__month
    
    @property
    def year(self) -> int:
        return self.__year
    
    @day.setter
    def day(self, day:int) -> None:
        try:
            day = int(day)
            if day <= 0 or day > 31:
                raise DateOutOfRange("Day must be between 1 and 31")
            self.__day = day
        except ValueError:
            raise ValueError("Day must be an integer")
        except Exception as e:
            raise e
    @month.setter
    def month(self, month:int) -> None:
        try:
            month = int(month)
            if month <= 0 or month > 12:
                raise DateOutOfRange("Month must be between 1 and 12")
            self.__month = month
        except ValueError:
            raise ValueError("Month must be an integer")
        except Exception as e:
            raise e
    @year.setter
    def year(self, year:int) -> None:
        try:
            year = int(year)
            if year <= 0:
                raise DateOutOfRange("Year must be larger than 0")
            self.__year = year
        except ValueError:
            raise ValueError("Year must be an integer")
        except Exception as e:
            raise e

        
    def __str__(self) -> str:
        year_str = str(self.year)
        month_str = str(self.month)
        day_str = str(self.day)
        if len(month_str) <= 1:
            month_str = "0" + month_str
        if len(day_str) <= 1:
            day_str = "0" + day_str

        return "-".join([year_str, month_str, day_str])


if __name__ == "__main__":
    date = Date(2025, 3, 4)
    print(date)
    date = Date(2025, "3", 4)
    print(date)
