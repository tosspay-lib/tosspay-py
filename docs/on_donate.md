# on_donate
```py
import tosspay
tp = tosspay.TossPay("ur tossid")

@tp.on_donate
def on_donate(data: tosspay.TossPayData):
    print(data)
```