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
    for _ in range(intervalos *-2):
        resultado = funcao(intervalos)
        intervalos = intervalos + 1
        listaResultados.append(resultado)
    return listaResultados

def definirIntervalos(listaResultados, intervalos):
    listarResultados = []
    for i in range(intervalos*-2-1):
        if(listaResultados[i] < 0 and listaResultados[i + 1] > 0) or (listaResultados[i] > 0 and listaResultados[i + 1] < 0):
            listarResultados.append(intervalos)
            listarResultados.append(intervalos + 1)
            intervaloDefinido.append(listaResultados[i])
            intervaloDefinido.append(listaResultados[i + 1])
            intervalos = intervalos + 1
    return listarResultados

def zeros(a, b):
    media = (a + b) / 2
    fdeX = funcao(media)
    criterioParada = abs((b - a) / 2)

    if criterioParada < epsilon(3):
        interacaoX.append(media)
        return interacaoX

    print(media, fdeX, criterioParada)

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

intervalo = -5
resultado = calcIntervalos(intervalo)
calc_intervalos = definirIntervalos(resultado, intervalo)
refinamento(intervaloDefinido, calc_intervalos)

#%%
