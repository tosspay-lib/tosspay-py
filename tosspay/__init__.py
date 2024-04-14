import requests
import json
import threading
import time
import random
from .tosspay_json import TossPayData

IS_RUNNING = False
RES = []
IDS = []

class TossPay:
    def __init__(self, name) -> None:
        global IS_RUNNING
        self.name = name
        if IS_RUNNING: return
        IS_RUNNING = True

        def fetch_toss_data():
            global RES
            while True:
                toss_response = requests.get(f"https://api-public.toss.im/api-public/v3/cashtag/transfer-feed/received/list?inputWord={self.name}")
                json_data = toss_response.json()
                if json_data["resultType"] != "FAIL":
                    RES = _get_data(json_data)
                else:
                    time.sleep(60)
                time.sleep(5)
        thread = threading.Thread(target=fetch_toss_data)
        thread.start()

    def on_donate(self, func):
        def wrapper():
            def on_donate_thread():
                old = []
                while True:
                    if RES:
                        datas = filter(lambda x: x not in old, RES)
                        # print("------", old, RES, "------", sep="\n")
                        if RES != old:
                            for data in datas:
                                func(data)
                        old = RES
                    time.sleep(2)

            thread = threading.Thread(target=on_donate_thread)
            thread.start()
        
        wrapper()
        return wrapper
    

    def on_payment(self, func):
        global IDS
        id = _gen_code()
        IDS.append(id)

        def wrapper():
            def on_payment_thread():
                old = []
                while True:
                    if RES:
                        datas = filter(lambda x: x not in old, RES)
                        # print("------", old, RES, "------", sep="\n")
                        if RES != old:
                            for data in datas:
                                if data.name == id:
                                    func(data)
                                    IDS.remove(id)
                                    break
                        old = RES
                    time.sleep(2)

            thread = threading.Thread(target=on_payment_thread)
            thread.start()
        
        wrapper()
        return wrapper
    

    def payment(self, func) -> str:
        global IDS
        id = _gen_code()
        IDS.append(id)
        def payment_thread():
            global IDS
            old = []
            while True:
                if RES:
                    datas = filter(lambda x: x not in old, RES)
                    if RES != old:
                        for data in datas:
                            if data.name == id:
                                func(data)
                                IDS.remove(id)
                                break
                    old = RES
                time.sleep(2)

        thread = threading.Thread(target=payment_thread)
        thread.start()
        return id

    def donate(self, func):
        def donate_thread():
            old = []
            while True:
                if RES:
                    datas = filter(lambda x: x not in old, RES)
                    if RES != old:
                        for data in datas:
                            func(data)
                    old = RES
                time.sleep(2)

        thread = threading.Thread(target=donate_thread)
        thread.start()
    
    def __str__(self) -> str:
        return f"https://toss.me/{self.name}"
    def __repr__(self) -> str:
        return f"TossPay(\"{self.name}\")"
    

def _get_data(data: dict):
    datas = []
    for i in data["success"]["data"]:
        datas.append(TossPayData(
            name=i["senderDisplayName"],
            mount=i["amount"],
            msg=i.get("message", "")
        ))
        
    return datas

def _gen_code() -> str:
    code = f"{random.randrange(10)}{random.randrange(10)}{random.randrange(10)}{random.randrange(10)}{random.randrange(10)}"
    if code in IDS:
        return _gen_code();
    return code