import cs50
# ask for a float the convert to cents
while True:
    dollars = cs50.get_float("Change owed: ")
    if dollars > 0:
        break
c = dollars * 100
c = int(c)
# reset variables
q = 0
d = 0
n = 0
p = 0
t = 0

# calculate each type of coin
q = int(c / 25)
d = int((c % 25) / 10)
n = int(((c % 25) % 10) / 5)
p = int(((c % 25) % 10) % 5)
t = q + d + n + p
# print final amount
print(t)
