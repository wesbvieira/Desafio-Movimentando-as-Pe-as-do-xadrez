class Peca:
    def __init__(self, cor):
        self.cor = cor

    def movimento_valido(self, origem, destino):
        raise NotImplementedError

class Rei(Peca):
    def movimento_valido(self, origem, destino):
        dx = abs(destino[0] - origem[0])
        dy = abs(destino[1] - origem[1])
        return dx <= 1 and dy <= 1

class Rainha(Peca):
    def movimento_valido(self, origem, destino):
        dx = abs(destino[0] - origem[0])
        dy = abs(destino[1] - origem[1])
        return dx == dy or origem[0] == destino[0] or origem[1] == destino[1]

class Torre(Peca):
    def movimento_valido(self, origem, destino):
        return origem[0] == destino[0] or origem[1] == destino[1]

class Bispo(Peca):
    def movimento_valido(self, origem, destino):
        dx = abs(destino[0] - origem[0])
        dy = abs(destino[1] - origem[1])
        return dx == dy

class Cavalo(Peca):
    def movimento_valido(self, origem, destino):
        dx = abs(destino[0] - origem[0])
        dy = abs(destino[1] - origem[1])
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

class Peao(Peca):
    def movimento_valido(self, origem, destino):
        dx = destino[0] - origem[0]
        dy = abs(destino[1] - origem[1])
        if self.cor == 'branco':
            return dx == -1 and dy == 0
        else:
            return dx == 1 and dy == 0
