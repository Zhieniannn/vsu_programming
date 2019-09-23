x = float(input("x = "))
y = float(input("y = "))
 
if x > 0 and y > 0:
    print("I четверть")
elif x < 0 and y > 0:
    print("II четверть")
elif x < 0 and y < 0:
    print("III четверть")
elif x > 0 and y < 0:
    print("IV четверть")
else:
    print("На оси")
