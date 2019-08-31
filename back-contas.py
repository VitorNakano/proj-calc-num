#%%
a, b, c, d, e, f = 0, 0, 1, 0, -9, 3
intervaloDefinido = []
interacaoX = []
interacaoFdeX = []
interacaoParada = []

# Metodo que irá definir os números da função
# Os parâmetros podem aceitar qualquer valor numérico
def numeros(a, b, c, d, e, f):
    self.a = a
    self.b = b
    self.c = c
    self.d = d
    self.e = e
    self.f = f

# Método que resolve a função
# O parâmetro irá definir o valor de x para o f(x)
def funcao(x):
    resultado = a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
    return resultado

# Método que define o Epsilon
# O parâmetro recebe um número, de preferência um inteiro,
# para calcular o valor de Epsilon
def epsilon(expoente):
    epsilon = 1 / 10**expoente
    return epsilon


def calcIntervalos(intervalos):
    listaResultados = []
    for _ in intervalos:
        resultado = funcao(intervalos)
        listaResultados.append(resultado)
    return listaResultados

def definirIntervalos(intervalos):
    listaDeResultados = []
    listaDeIntervalos = []
    resultadosDeIntervalos = []

    for i in range(intervalos *-1, intervalos + 1):
        resultado = funcao(i)
        listaDeResultados.append(resultado)
        listaDeIntervalos.append(i)
    
    for i in range(len(listaDeIntervalos)-1):
        if(listaDeResultados[i] < 0 and listaDeResultados[i + 1] > 0) or (listaDeResultados[i] > 0 and listaDeResultados[i + 1] < 0):
            print(i, listaDeResultados[i], listaDeResultados[i+1])
            resultadosDeIntervalos.append(listaDeIntervalos[i])
            resultadosDeIntervalos.append(listaDeIntervalos[i+1])

    return resultadosDeIntervalos


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

#%%
