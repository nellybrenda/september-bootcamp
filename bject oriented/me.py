def calctax(income):
    pay = []
    for r in ranges:
        if all([income > r[0], income > r[1]]):
            pay.append((r[1]-r[0]) * r[2]/100)
        elif all([income > r[0], income <= r[1]]):
            pay.append((income-r[0]) * r[2]/100)
    if income > maxinc:
        pay.append((income-maxinc) * maxtax/100)
    return int(sum(pay))