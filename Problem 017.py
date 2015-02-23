units = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens = [0,3,6,6,5,5,5,7,6,6]
hundreds = 7
thousand = 8
 
total = 0
for i in range(1,1000):
    # units
    c = i % 10

    #tens
    b = ((i % 100) - c) / 10

    #hundreds
    a = ((i % 1000) - (b * 10) - c) / 100
 
    if a != 0:
        # units[a] + hundred
        total += units[a] + hundreds
        
        # adding the "and"
        if b != 0 or c != 0: total += 3
    if b == 0 or b == 1:
        total += units[b * 10 + c]
    else: total += tens[b] + units[c]
 
total += units[1] + thousand
 
print "%s found in seconds" % (total)
