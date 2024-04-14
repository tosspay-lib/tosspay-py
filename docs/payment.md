# donate
```py
import tosspay
tp = tosspay.TossPay("ur tossid")

payment = tp.payment(lambda data: print(data))
print(payment)
```