class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_memory(self):
        return self.__memory

    def set_memory(self, memory):
        self.__memory = memory

    def make_computations(self):
        if self.__cpu > 0 and self.__memory > 0:
            self.__cpu *= 2
            self.__memory *= 2
            print("Attributes multiplied.")
        else:
            print("CPU or memory is not set or has invalid values.")


class Phone:
    def __init__(self):
        self.__sim_cards_list = []

    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number, call_to_number):
        if sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Calling to {call_to_number} from {sim_card}")
        else:
            print("SIM card number is incorrect.")


class SmartPhone(Computer, Phone):
    def use_gps(self, location):
        print(f"Calculating route to {location} using GPS.")

    def __str__(self):
        return f"SmartPhone: CPU - {self.get_cpu()}, Memory - {self.get_memory()}, SIM cards - {self.get_sim_cards_list()}"


computer = Computer(4, 16)
print(computer.get_cpu())
print(computer.get_memory())

computer.set_cpu(8)
computer.set_memory(32)

print(computer.get_cpu())
print(computer.get_memory())

computer.make_computations()

print(computer.get_cpu())
print(computer.get_memory())

phone = Phone()
phone.set_sim_cards_list(["Beeline", "Megacom", "O!"])
print(phone.get_sim_cards_list())

phone.call(2, "+996 777 123456")

smartphone1 = SmartPhone("Snapdragon 855", 8)
smartphone1.set_sim_cards_list(["Beeline", "Megacom"])
print(smartphone1)
smartphone1.make_computations()