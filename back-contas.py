# %%
a, b, c, d, e, f = 1, 2, 1, 4, -9, 3
intervaloDefinido = []
interacaoX = []
interacaoFdeX = []
interacaoParada = []

# Metodo que irá definir os números da função.
# Os parâmetros podem aceitar qualquer valor numérico.
def numeros(a, b, c, d, e, f):
    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.e = e
    self.f = f

# Método que resolve a função.
# O parâmetro irá definir o valor de x para o f(x).
#
# return Será o resultado da função.
def funcao(x):
    resultado = a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
    return resultado

# Método que define o Epsilon.
# O parâmetro recebe um número, de preferência um inteiro, 
# para calcular o valor de Epsilon.
# 
# return Devolve o valor calculado de Epsilon.
def epsilon(expoente):
    epsilon = 1 / 10**expoente
    return epsilon


def calcIntervalos(intervalos):
    listaResultados = []
    for _ in intervalos:
        resultado = funcao(intervalos)
        listaResultados.append(resultado)
    return listaResultados

# Método que irá mostrar os intervalos existentes dentro da função.
# Parâmetro dois valores que serão estipulados como os intervalos
# de um valor x até um valo y.
#
# return Será uma lista com todos os intervalos encontrados.
def definirIntervalos(val1, val2):
    listaDeResultados = []
    listaDeIntervalos = []
    resultadosDeIntervalos = []
    intervalo = []

    for i in range(val1, val2 + 1):
        resultado = funcao(i)
        listaDeResultados.append(resultado)
        listaDeIntervalos.append(i)
        print(resultado)

    for i in range(len(listaDeIntervalos) - 1):
        if(listaDeResultados[i] < 1 and listaDeResultados[i + 1] > -1) or (listaDeResultados[i] > -1 and listaDeResultados[i + 1] < 1):
            resultadosDeIntervalos.append(listaDeIntervalos[i])
            resultadosDeIntervalos.append(listaDeIntervalos[i+1])

    for i in range(len(resultadosDeIntervalos)):
        if (i % 2 == 0):
            arrTemp = []
            arrTemp.append(resultadosDeIntervalos[i])
            arrTemp.append(resultadosDeIntervalos[i + 1])
            intervalo.append(arrTemp)

    return intervalo


def zeros(a, b):
    media = (a + b) / 2
    fdeX = funcao(media)
    criterioParada = abs((b - a) / 2)

    print(media, fdeX, criterioParada)

    if criterioParada < epsilon(3):
        interacaoX.append(media)
        return interacaoX

    interacaoX.append(media)
    interacaoFdeX.append(fdeX)
    interacaoParada.append(criterioParada)

    if fdeX < 0:
        zeros(a, media)
    if fdeX > 0:
        zeros(media, b)


def refinamento(intervaloDefinido, calcIntervalo):
    array = len(calcIntervalo)
    for i in range(0, array, 2):
        if intervaloDefinido[i] > 0:
            print(calcIntervalo[i], calcIntervalo[i + 1])
            zeros(calcIntervalo[i], calcIntervalo[i + 1])
        else:
            print(calcIntervalo[i], calcIntervalo[i + 1])
            zeros(calcIntervalo[i], calcIntervalo[i + 1])

# %%
