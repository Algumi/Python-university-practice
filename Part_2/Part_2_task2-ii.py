class Polinom:
    __coef = []

    def __init__(self, coef):
        try:
            if not coef:
                raise Exception("Empty list of coefficients is not allowed")
            for i in coef:
                if type(i) != int and type(i) != float:
                    raise Exception("Only integer and float values of coefficients are allowed")
        except Exception as e:
            print(e)
        else:
            self.__coef = coef

    def __eq__(self, other):
        try:
            if type(other) != Polinom:
                raise Exception("Comparing polynomial with other types is prohibited.")
        except Exception as e:
            print(e)
        else:
            if self.get_degree() == other.get_degree():
                if self.__coef == other.get_coefficients():
                    return True
            return False

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        try:
            if type(other) != Polinom:
                raise Exception("Adding polynomial to other types is prohibited")
        except Exception as e:
            print(e)
        else:
            a, b = self.__coef, other.get_coefficients()
            l_a, l_b = len(a), len(b)
            if l_a < l_b:
                a += [0] * (l_b - l_a)
            else:
                b += [0] * (l_a - l_b)
            return Polinom([a[i] + b[i] for i in range(l_a)])

    def __neg__(self):
        map(float.__neg__, self.__coef)

    def __mul__(self, other):
        try:
            if type(other) != Polinom:
                raise Exception("Multiplying polynomial to other types is prohibited")
        except Exception as e:
            print(e)
        else:
            a = self.__coef
            b = other.get_coefficients()
            res = [0] * (len(a) + len(b) - 1)
            for a_num, a_val in enumerate(a):
                for b_num, b_val in enumerate(b):
                    res[a_num + b_num] += a_val * b_val
            return Polinom(res)

    def __str__(self):
        sign = lambda x: (" + ", " - ")[x < 0]
        res = ""
        for i in range(len(self.__coef) - 1, 0, -1):
            if self.__coef[i] != 0:
                res += str(abs(self.__coef[i])) + "x^" + str(i) + sign(self.__coef[i - 1])
        res += str(self.__coef[0])
        return res

    def value(self, x):
        try:
            if type(x) != int and type(x) != float:
                raise Exception("Only integer and float values are allowed in calculating value of polynomial")
        except Exception as e:
            print(e)
        else:
            res = 0
            for i, val in enumerate(self.__coef):
                res += val * x ** i
            return res

    def get_degree(self):
        return len(self.__coef) - 1

    def get_coefficients(self):
        return self.__coef

    def get_coefficient(self, i):
        return self.__coef[i]

    def set_coefficient(self, i, x):
        try:
            if type(x) != int and type(x) != float:
                raise Exception("Only integer and float values are allowed in calculating value of polynomial")
            if i > len(self.__coef):
                raise Exception("There is no such index in the list of coefficients")
        except Exception as e:
            print(e)
        else:
            self.__coef[i] = x

    def derivative(self):
        return Polinom([x * i for i, x in enumerate(self.__coef)][1:])

    def ind_integral(self):
        return Polinom([0] + [x / (i + 1) for i, x in enumerate(self.__coef)])


def test():
    p = Polinom([1, 0, -2, 4])
    print(p)
    print(p.value(2))
    print(p.get_degree())

    p2 = Polinom([3, 0, 2, 4])
    print(p * p2)
    print(p * p2 + p)
    print((p * p2).value(5))

    print(p == p2)
    print(p != p2)

    print(p2.get_coefficient(1))
    p2.set_coefficient(1, 19)
    print(p2)

    print(p2.derivative())
    print(p2.ind_integral())


test()
