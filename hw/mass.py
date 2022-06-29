class Generator:
    def __init__(self, name: str, index: str, value: str):
        self.name = name
        self.index = index
        self.value = value
    def get_name(self):
        return f"{self.name} {self.index} {self.value}"

ran = []
for i in range(1, 1001):
    ran.append(Generator(name=f"_{i}", index=f"{i}", value=f"_A{i}").get_name())
print(ran)
