def computepay(h , r):
    if h <= 40:
        return h * r
    else:
        return 40 * r + (h-40) * r * 1.5
h = input("Enter hours")
hour = float(h)
r = input("Enter rate")
rate = float(r)
pay = computepay(hour , rate)
print("Pay",pay)