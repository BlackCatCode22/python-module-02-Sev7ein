## 9/6/25
# s.n

hoursWorked = input("Enter Hours Worked: ")
rateEarned = input("Enter Rate Earned: ")
# noinspection PyBroadException
try:
    #renames our input to be called
    hw = float(hoursWorked)
    re = float(rateEarned)
except:
    print("Invalid input, Please enter numeric input")
    quit()

print(hw, re)
if hw > 40.0:
    print("Overtime")
    rp = hw * re
    overTimePay = (hw - 40.0) * (re * 0.5)
    print(rp, overTimePay)
    xp = rp + overTimePay
else:
    print("Regular")
    xp = hw * re
print("Pay:", xp)
