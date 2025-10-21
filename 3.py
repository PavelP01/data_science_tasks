from datetime import date

def calc_diff(d1: date, d2: date):
   diff = (d2 - d1).days
   return abs(diff)

if __name__ == "__main__":
   dt1 = date(2025, 10, 11)
   dt2 = date(2025, 10, 1)
   print(calc_diff(dt1, dt2))