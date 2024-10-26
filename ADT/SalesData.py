from multiArray import MultiArray 

#Total sales by store
def totalSalesByStore(salesData , store= any):
    s= store -1 
    total = 0
    for i in range(salesData.length(2)):
        for m in range(salesData.length(3)):
            total+=salesData[s,i,m]
    return total

#Total sales by Month
def totalSalesByMonth(salesData, month= any):
    m = month -1 
    total = 0
    for s in range(salesData.length(1)):
        for i in range(salesData.length(2)):
            total+=salesData[s,i,m]
    return total

#Total sales by Item
def totalSalesByItem(salesData, item= any):
    i = item -1 
    total = 0
    for s in range(salesData.length(1)):
        for m in range(salesData.length(3)):
            total+=salesData[s,i,m]
    return total
#monthly sales by store 
def monthlySalesByStore(salesdata , store ):
    s= store -1 
    totals = []*12
    for i in range(salesData.length(2)):
        sum = 0
        for m in range (salesData.length(3)):
            sum+=salesData[s,i,m]        
        totals[i] = sum
    return totals
salesData = MultiArray(8,100,12)

