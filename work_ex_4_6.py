#9/7/25
#s.n
def calculatePay(hours, rate) :
    print("In Calculate Pay", hours, rate)
    if hours > 40:
        regularPay = hours * rate
        overTimePay = (hours - 40) * (rate* 0.5)
        truePay = regularPay + overTimePay
    else:
        truePay = hours * rate
    return truePay

hoursW = input("Enter Hours Worked: ")
rateE = input("Enter Rate Earned: ")
#renames our input to be called
hw = float(hoursW)
re = float(rateE)
xp= calculatePay(hw,re)
print("Pay:",xp)

