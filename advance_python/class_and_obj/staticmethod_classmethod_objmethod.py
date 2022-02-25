"""
类方法、静态方法、实例方法：

"""
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 实例方法
    def tomorrow(self):
        self.day += 1

    # 静态方法
    @staticmethod
    def parse_from_str(data_str):
        year, month, day = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(day))

    # 类方法
    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(day))

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"

if __name__ == '__main__':
    date_str = "2022-02-22"
    new_day = Date.parse_from_str(date_str)
    print(new_day)
    new_day.tomorrow()
    print(new_day)