mealCost = float(input().strip())
tipPercent = float(input().strip())
taxPercent = float(input().strip())

totalCost = mealCost + mealCost*tipPercent/100 + mealCost*taxPercent/100
print("The total meal cost is "+ str(round(totalCost,0)).split('.')[0] +" dollars.")