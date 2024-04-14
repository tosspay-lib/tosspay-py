# donate
```py
import tosspay
tp = tosspay.TossPay("ur tossid")

payment = tp.donate(lambda data: print(data))
```