def mifun(valor):
    if type(valor) is int:
        if valor < 0: return abs(valor)
        return valor
    else:
        if type(valor) is float: return mifun(int(valor))
        return 0

lista = [22,"hola",-125, 12.33]
print(list(map(mifun,lista)))