import calendar
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'zh_TW')
ano_atual = datetime.now().year
print(calendar.calendar(ano_atual))