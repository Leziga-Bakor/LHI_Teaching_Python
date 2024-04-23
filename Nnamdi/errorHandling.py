



try: 
    raise ZeroDivisionError('divide')
except (NameError,ZeroDivisionError) as e:
    print(e)
except Exception:
    print('there was an error')
else:
    pass
finally:
    pass