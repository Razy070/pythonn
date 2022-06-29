class MyCalculator:
    @staticmethod  # дакоратор который делает метод в классе статическим(без параметра селф и инициализации)
    def summ(val1: float, val2: float):
        return val1 + val2

    def subtraction(val1: float, val2: float):
        return val1 - val2

    def multiplication(val1: float, val2: float):
        return val1 * val2

    def division(val1: float, val2: float):
        if val2 != 0:
            return val1 / val2

MyCalculator.division(100, 2)
print(MyCalculator.division(100, 2))
