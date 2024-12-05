print("________________SIP Calculator_______________")
while True:
    amount = int(input("Enter amount you want to invest(₹): "))
    if amount >=100:
        break
    print("Amount should be ₹100 or above, Please Enter Valid Amount ")

while True:
    interest_rate = float(input("Enter interest rate(%): "))
    if interest_rate >=1:
        break
    print("interest_rate should be above 1, Please Enter valid interest rate")

while True:
    years = int(input("How many years you want to invest: "))
    if years >=1:
        break
    print("Investment should be 1 or more Years, Please Enter valid investment Years")


percentage_cal = interest_rate /12 /100 # calculating the interest percentage into a simple number
monthly_installment : int = years * 12  #converting years into months


total_investment = amount * monthly_installment
future_Value = amount * (((pow((1+percentage_cal),monthly_installment))-1)/percentage_cal) * (1+percentage_cal)
Estimated_return = future_Value - total_investment

print("**************Investment and Return****************")
print(f"Your Total Investment over {years}year/s is {total_investment}")
print(f"Future Value for the investment is {future_Value:.2f}")
print(f"Estimated Returns for {years} year/s is {Estimated_return:.2f}")
