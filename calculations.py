def calculateMileage(mileage):
        mileageCost = mileage.split(" ")[0].replace(",", "")
        return float(mileageCost)

def calculateExpense(sessions, cost, mileage):
        mileageCost = calculateMileage(mileage)
        return float(sessions) * (float(cost)+mileageCost)