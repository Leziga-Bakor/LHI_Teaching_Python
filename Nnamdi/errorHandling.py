



try: 
    raise ZeroDivisionError('divide')
except (NameError,ZeroDivisionError) as e:
    print(e)
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception:
    print('there was an error')
else:
    pass
finally:
    pass

import datetime
day = datetime.date(2016,7,10)
print(day.weekday())