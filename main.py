def calendar(m):
    for i in range (0, 12):
        if m == mounths[i]:
            return i + 1
    return m + " is not a month"



mounths = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

print(calendar("hello"))
