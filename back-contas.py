a, b, c, d, e, f = 0, 0, 1, 0, -9, 3

def funcao(a, b, c, d, e, f, x):
    resultado = a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
    return resultado

def episilon(expoente):
    episilon = 1 / 10**expoente
    return episilon

def calcIntervalos(val1, val2):
    intervalo = range(val1, val2)
    intervalos = []
    resultados = []
    fdeX = funcao(a, b, c, d, e, f, intervalo)
    intervalos.append(intervalo)
    resultados.append(fdeX)

def definirIntervalos(intervalos)