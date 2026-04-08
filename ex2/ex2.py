
hrs = input('enter hours:')
hrs = float(hrs)
rate= input('enter rate:')
rate= float(rate)

if hrs <= 40:
  normalpay = hrs * rate 
  print(normalpay)

elif hrs > 40:
    normalpay = 40 * rate
    overtimepay = (hrs - 40) * rate * 1.5
    totalpay = normalpay + overtimepay
    print(totalpay)