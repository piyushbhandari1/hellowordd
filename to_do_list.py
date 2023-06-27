def usdtogbp(x):
    gbp = x/1.27
    return gbp

def gbptousd(y):
    usd = y * 1.27
    return usd

print("USD "+ str(gbptousd(100)))
print("GBP " + str(usdtogbp(50)))