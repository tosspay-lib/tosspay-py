
class TossPayData:
    name: str
    mount: int
    msg: str

    def __init__(
            self,
            name: str = "",
            mount: int = 0,
            msg: str = ""
        ) -> None:
        self.name = name
        self.mount = mount
        self.msg = msg

    def __str__(self) -> str:
        return f"{self.name}님이 {self.mount}원을 후원했습니다. {f'({self.msg})' if self.msg else ''}"
    
    def __repr__(self) -> str:
        return f"TossPayData(name={self.name}, mount={self.mount}{f', msg={self.msg}' if self.msg else ''})"
    
    def __eq__(self, value: object) -> bool:
        if type(value) != TossPayData: return False
        return self.name == value.name and self.mount == value.mount and self.msg == value.msg

