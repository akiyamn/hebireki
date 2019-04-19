from datetime import *
from era import *
import string
import re


class Wareki:

    """
    A class which wraps around a datetime object (dt), extending functionality
    to work with the traditional Japanese calendar format as well as Japanese time and date formats
    """

    def __init__(self, dt=None):
        if dt is None:
            dt = date.fromtimestamp(0)
        self.dt = dt

    def __str__(self):
        """
        :return: Returns the string representation of the wrapped datetime object
        """
        return str(self.dt)

    def era(self):
        eras = [
            Era("令和", "Reiwa", date(2019, 5, 1), None),
            Era("平成", "Heisei", date(1989, 8, 1), date(2019, 4, 30)),
            Era("昭和", "Showa", date(1926, 12, 25), date(1989, 1, 7)),
            Era("大正", "Taisho", date(1912, 7, 30), date(1926, 12, 24)),
            Era("明治", "Meiji", date(1867, 2, 3), date(1912, 7, 29)),
        ]
        for era in eras:
            if self.dt.date() >= era.start:
                return era
        return eras[-1]

    def era_year(self, gannen=False):
        greg_year = self.dt.year
        japan_year = greg_year - self.era().start.year + 1
        if gannen:
            return "元" if japan_year == 1 else str(japan_year)
        else:
            return japan_year

    def strftime(self, format_spec):
        modifier = "%@"
        code_conversion = {
            "E": self.era().short_kanji,
            "EE": self.era().kanji,
            "e": self.era().letter,
            "ee": self.era().english,
            "n": self.era_year(),
            "N": self.era_year(True),
            "a": self.kanji_weekday(),
            "A": self.full_kanji_weekday()
        }
        new_string = self.dt.strftime(format_spec)
        for code, value in code_conversion.items():
            if len(code) == 1:
                new_string = re.sub(r"{1}{0}(?!{0})".format(code, modifier), str(value), new_string)
            else:
                new_string = new_string.replace(modifier + code, value)
        return new_string

    def kanji_weekday(self):
        weekdays = ["日", "月", "火", "水", "木", "金", "土"]
        return weekdays[self.dt.weekday()]

    def full_kanji_weekday(self):
        return self.kanji_weekday() + "曜日"


if __name__ == "__main__":
    test = Wareki(datetime.now())
    print(test.strftime("%@EE%@N年%-m月%d日 (%@A)\n%-H時%M分%S秒"))
