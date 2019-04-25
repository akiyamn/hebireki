import src.wareki as wa
from datetime import datetime

if __name__ == "__main__":

    """
    A new Wareki instance which acts as a wrapper for the current date
    A Wareki instance with no arguments when created defaults to the current time.
    Equivalent to: now = wa.Wareki(datetime.now())
    """
    now = wa.Wareki()

    ''' A default, long date format with kanji included '''
    print(str(now))

    """
    Or a custom representation of the time using our wrapper of datetime's strftime()
    print(now.strftime("%@e%@N/%m/%d (%@a)\n%-H:%M"))
    """
