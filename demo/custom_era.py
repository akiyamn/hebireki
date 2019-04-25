from src import *
from datetime import datetime

if __name__ == "__main__":

    new_era = Era("新時代", "New Era", datetime(2019, 6, 1), datetime(2020, 8, 20))

    now = Wareki(datetime.now())
    print(now.strftime("%@EE%@N年%-m月%d日 (%@A)\n%-H時%M分%S秒"))
