#funtions


def computepay(hrs , rate):
    if hrs > 40 :
      normalpay = 40 * rate
      overtimepay =  (hrs - 40) * rate * 1.5
      pay = overtimepay + normalpay
      return  pay
    elif hrs <= 40:
      pay = hrs * rate 
      return  pay


hrs = input("enter your hours:")
hrs = float(hrs)

rate = input("enter your rates:")
rate= float(rate)
result = computepay(hrs, rate)
print(result)
