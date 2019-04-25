import src.wareki as wa
from datetime import datetime

if __name__ == "__main__":
    now = wa.Wareki(datetime.now())
    print(now.strftime("%@EE%@N年%-m月%d日 (%@A)\n%-H時%M分%S秒"))
