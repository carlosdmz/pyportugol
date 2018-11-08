class Numero(object):

    def __init__(self, value):
        self.value = value

    def eval(self):

        return int(self.value)


class String(object):

    def __init__(self, value):
        self.value = value

    def eval(self):
        return str(self.value)


class Tipo(object):

    def __init__(self, value):
        self.value = value

    def eval(self):
        return str(self.value)


class Identificador(object):

    def __init__(self, nome, tipo, value=0):
        self.nome = nome
        self.value = value
        self.tipo = tipo

    def eval(self):

        return int(self.value)


class OpBinario(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(OpBinario):

    def eval(self):

        return self.left.eval() + self.right.eval()


class Sub(OpBinario):

    def eval(self):

        return self.left.eval() - self.right.eval()


class Mult(OpBinario):

    def eval(self):

        return self.left.eval() * self.right.eval()


class Div(OpBinario):

    def eval(self):

        return self.left.eval() / self.right.eval()


class Atribuicao(OpBinario):

    def eval(self):
        self.right.tipo = self.left.eval()

        return self.right


class Imprime(object):

    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())


class Leia(object):

    def __init__(self, ident):
        self.ident = ident

    def eval(self):
        new_value = int(input())

        return self.ident, new_value
