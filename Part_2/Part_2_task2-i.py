class Transport:
    __avg_speed = 0
    __fuel_type = "none"
    __creation_year = 0

    def __init__(self, speed, f_type, year):
        self.__avg_speed = speed
        self.__creation_year = year
        self.__fuel_type = f_type

    def get_avg_speed(self):
        return self.__avg_speed

    def get_fuel_type(self):
        return self.__fuel_type

    def get_creation_year(self):
        return self.__creation_year

    def print_info(self):
        print("Average speed: " + str(self.__avg_speed))
        print("Fuel type: " + self.__fuel_type)
        print("Year of creation: " + str(self.__creation_year))


class Car(Transport):
    __brand = "none"
    __car_number = "0"

    def __init__(self, speed, f_type, year, brand, number):
        Transport.__init__(self, speed, f_type, year)
        self.__brand = brand
        self.__car_number = number

    def get_brand(self):
        return self.__brand

    def get_car_number(self):
        return self.__car_number

    def print_info(self):
        print("This is car")
        Transport.print_info(self)
        print("Car number: " + self.__car_number)
        print("Brand: " + self.__brand + "\n")


class Train(Transport):
    __train_number = "0"
    __carriage_quantity = 0
    __passenger_carriage_quantity = 0

    def __init__(self, speed, f_type, year, tr_number, car_number, pas_car_number):
        Transport.__init__(self, speed, f_type, year)
        self.__train_number = tr_number
        self.__carriage_quantity = car_number
        self.__passenger_carriage_quantity = pas_car_number

    def get_train_number(self):
        return self.__train_number

    def get_carriage_quantity(self):
        return self.__carriage_quantity

    def get_passenger_carriage_quantity(self):
        return self.__passenger_carriage_quantity

    def add_carriage(self, num):
        self.__carriage_quantity += num
        return str(num) + " carriages has been added\n"

    def add_passenger_carriage(self, num):
        self.__passenger_carriage_quantity += num
        self.add_carriage(num)
        return str(num) + " passenger carriages has been added\n"

    def remove_carriage(self, num, is_passenger):
        if is_passenger:
            if num > self.__passenger_carriage_quantity:
                return "No enough carriages\n"
            else:
                self.__passenger_carriage_quantity -= num
                self.__carriage_quantity -= num
                return str(num) + " passenger carriages has been removed\n"
        else:
            if num > self.__carriage_quantity:
                return "No enough carriages\n"
            else:
                self.__carriage_quantity -= num
                return str(num) + " carriages has been removed\n"

    def print_info(self):
        print("This is train")
        Transport.print_info(self)
        print("Train number: " + self.__train_number)
        print("Number of carriages: " + str(self.__carriage_quantity))
        print("Number of passenger carriages: " + str(self.__passenger_carriage_quantity) + "\n")


def main():
    some_train = Train(200, "electricity", 2005, "A2421D", 10, 7)
    some_train.print_info()

    print(some_train.add_passenger_carriage(10))

    print("Attempt to remove 42 carriages:")
    print(some_train.remove_carriage(42, False))

    print(some_train.remove_carriage(5, True))
    some_train.print_info()

    some_car = Car(140, "diesel", 2010, "Т231ук", "BMW")
    some_car.print_info()


main()
