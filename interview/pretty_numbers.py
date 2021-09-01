class PrettyNumbers:
    def __init__(self, *args):
        self.numbers = list(*args)
        self.pretty = []

    def calculate_power_both(self, number):
        power = 0
        self.pretty.append(number)
        while number % 2 == 0:
            number /= 2
            power += 1
        power1 = 0
        while number % 3 == 0:
            number /= 3
            power1 += 1
        return f"2^{power}*3^{power1}"

    def calculate_power(self, number, divider):
        power = 0
        self.pretty.append(number)
        while number % divider == 0:
            number /= 2
            power += 1
        return f"{divider}^{power}"

    def check_number(self):
        for number in self.numbers:
            if number % 2 == 0 and number % 3 == 0:
                print(self.calculate_power_both(number))
            elif number % 2 == 0:
                print(self.calculate_power(number, divider=2))
            elif number % 3 == 0:
                print(self.calculate_power(number, divider=3))

    def sorted_numbers(self):
        print(sorted(self.pretty))

    def sum_first100(self):
        sum_number = sum(self.pretty[:100])
        print(sum_number)
        print(len(str(sum_number)))


numbers = [3, 288, 4, 512, 81, 6, 64]
pretty_num = PrettyNumbers(numbers)
pretty_num.check_number()
pretty_num.sorted_numbers()
pretty_num.sum_first100()
