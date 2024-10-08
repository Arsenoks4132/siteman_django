class MonthNumberConverter:
    regex = r"\d{1,2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%02d" % value
