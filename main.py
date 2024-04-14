import tosspay
tp = tosspay.TossPay("wntjd0612")

@tp.on_donate
def haha(data: tosspay.TossPayData):
    print(data)
    ...

# payment = tp.donate(lambda data: print(data))