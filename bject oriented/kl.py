income_input = {"Alex": 500, "James": 20500, "Kinuthia": 70000}

def calculate_tax(income_input):
    for item in income_input:
        income = income_input[item]
        # print(income)

        if (income >= 0) and (income <= 1000):
            tax = (0*income)

        elif (income > 1000) and (income <= 10000):
            tax = (0.1 * (income-1000))

        elif (income > 10000) and (income <= 20200):
            tax = ((0.1*(10000-1000)) + (0.15*(income-10000)))

        elif (income > 20200) and (income <= 30750):
            tax = ((0.1*(10000-1000)) + (0.15*(20200-10000)) + (0.2*(income-20200)))

        elif (income > 30750) and (income <= 50000):
            tax = ((0.1*(10000-1000)) + (0.15*(20200-10000)) + (0.2*(30750-20200)) + (0.25*(income-30750)))

        elif (income > 50000):
            tax = ((0.1*(10000-1000)) + (0.15*(20200-10000)) + (0.2*(30750-20200)) + (0.25*(50000-30750)) + (0.3*(income-50000)))   
        else:
            pass
        income_input[item] = int(tax)
    return (calculate_tax(income_input))
 {'Kinuthia': 15352, 'James': 2490, 'Alex': 0}
    print(calculate_tax(income_input))
 