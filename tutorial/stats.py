# 
# Filename: stats.py
# Author: Nina Nyback
# date: 15 Oct 2025
# description: Statistics class
# This is all my own work as per the College's
# Academic Integrity Policy (copied from Moodle)
# 
class Statistics:
    def __init__(self, numbers = list())-> None:
        self.numbers = numbers
    @property
    def numbers(self) -> list:
        return self.__numbers
    @numbers.setter
    def numbers(self, numbers = list()) -> None:
        self.__numbers = numbers
        return None
    def length(self) -> int:
        return len(self.numbers)
    def sum(self) -> float:
        return sum(self.numbers)
    def min(self) -> float:
        return min(self.numbers)
    def max(self) -> float:
        return max(self.numbers)
    def mean(self) -> float:
        return self.sum() / self.length()
    def mid(self) -> float:
        return (self.min() + self.max()) / 2
    def median(self) -> float:
        length = self.length()
        self.numbers.sort()
        index = round(length / 2)
        if length % 2 == 0:
            return (self.numbers[index] + self.numbers[index - 1]) / 2
        else:
            return self.numbers[index -1]
    def append(self, number: float) -> None:
        self.numbers.append(number)
    def remove(self, number: float) -> None:
        self.numbers.remove(number)
    def remove_at(self, index: int) -> None:
        self.numbers.pop(index)
    
if __name__ == "__main__":
    stats = Statistics([2.0, 3.5, 4.5, 5, 6.0])
    print(stats.numbers)
    print("Length", stats.length())
    print("Min", stats.min())
    print("Max", stats.max())
    print("Sum", stats.sum())

    print("Mid", stats.mid())
    print("Mean", stats.mean())
    print("Median", stats.median())
    
    stats.append(1)
    print(stats.numbers)
    stats.remove(6)
    print(stats.numbers)
    stats.remove_at(2)
    print(stats.numbers)
