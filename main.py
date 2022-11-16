import random

def fatorial(x):
    if x == 0:
        return 1
    res = x
    for i in range(x-1,0,-1) :
        res = res*i
    return res

def rolarDados(d, n):
    '''
    Rolador de dados
    d = quantidade de dados
    n = numero de faces
    retorna uma lista com os resultados
    '''
    dados = []
    for i in range(d):
        dado = random.randrange(1,n+1)
        dados.append(dado)
    return dados

def rolarSoma(d,n):
    '''
    soma do resultado dos dados
    d = a quantidade de dados
    n = o número de faces de cada dado
    retorna uma lista com os resultados dos dados e a soma dos resultados
    '''
    dados = rolarDados(d,n)
    res = 0
    for dado in dados:
        res += dado
    return [dados, res]

def pilhaDados(d,n,r):
    '''
    rola uma pilha de dados com resultado de quantos dados passaram na dificuldade
    e a lista do resultado dos dados
    d = quantidade de dados
    n = número de faces dos dados
    r = resultado alvo para contar como acerto
    retorna uma lista com os resultados dos dados e quantos dados passaram pelo resultado alvo
    '''
    dados = rolarDados(d,n)
    res = 0
    for dado in dados:
        if dado >= r :
            res += 1
    return [dados, res]

def probabilidadeDados(d,n,r):
    """
    It takes the number of dice, the number of faces on each die, and the number you're trying to roll,
    and returns the probability of rolling that number
    
    :param d: number of dice
    :param n: number of faces on the dice
    :param r: the number you're trying to roll
    :return: A dictionary with the number of dice, number of faces, target number, and the probability
    of success.
    """
    prob1 = ((n-r+1)/n)
    prob = prob1
    for _ in range(d-1):
        prob = prob*prob1
    return {'numero de dados': d,
            'número de faces': n,
            'nùmero alvo': r,
            'probabilidade de sucesso ': prob*100}

def probabilidadeDadosLimite(d,n,r,a,res=False):
    """
    It calculates the probability of rolling a number of dice with a number of sides, each of which must
    roll a number or higher, and returns the probability of success
    
    :param d: number of dice
    :param n: number of faces
    :param r: the number of faces that are considered a success
    :param a: number of successes
    :return: A dictionary with the number of dice, number of faces, number of target, and the
    probability of success.
    """
    prob = (fatorial(d)/(fatorial(0)*fatorial(d-0)))*(((n-r+1)/n)**0)*((1-((n-r+1)/n))**(d-0))
    for i in range(1,a,+1):
        prob = 1-prob
        comb = (fatorial(d)/(fatorial(i)*fatorial(d-i)))*(((n-r+1)/n)**i)*((1-((n-r+1)/n))**(d-i))
        print(prob, comb)
        prob = prob - comb
    if res:
        return {'numero de dados': d,
            'número de faces': n,
            'nùmero alvo': r,
            'probabilidade de sucesso ': prob*100}
    return round(prob*100, 2)

# lv100 = [probabilidadeDadosLimite(2,10,7,2),probabilidadeDadosLimite(3,10,7,2),
#         probabilidadeDadosLimite(4,10,7,2),probabilidadeDadosLimite(5,10,7,2),]
# lv101 = [probabilidadeDadosLimite(2,10,6,2),probabilidadeDadosLimite(3,10,6,2),
#         probabilidadeDadosLimite(4,10,6,2),probabilidadeDadosLimite(5,10,6,2),]
# lv102 = [probabilidadeDadosLimite(2,10,5,2),probabilidadeDadosLimite(3,10,5,2),
#         probabilidadeDadosLimite(4,10,5,2),probabilidadeDadosLimite(5,10,5,2),]
# lv103 = [probabilidadeDadosLimite(2,10,4,2),probabilidadeDadosLimite(3,10,4,2),
#         probabilidadeDadosLimite(4,10,4,2),probabilidadeDadosLimite(5,10,4,2),]
# dif10 = [lv103[0]-lv100[0],lv103[3]-lv100[3]]


# lv0 = [probabilidadeDadosLimite(2,6,5,2),probabilidadeDadosLimite(3,6,5,2),
#         probabilidadeDadosLimite(4,6,5,2),probabilidadeDadosLimite(5,6,5,2),]
# lv1 = [probabilidadeDadosLimite(2,6,4,2),probabilidadeDadosLimite(3,6,4,2),
#         probabilidadeDadosLimite(4,6,4,2),probabilidadeDadosLimite(5,6,4,2),]
# lv2 = [probabilidadeDadosLimite(2,6,3,2),probabilidadeDadosLimite(3,6,3,2),
#         probabilidadeDadosLimite(4,6,3,2),probabilidadeDadosLimite(5,6,3,2),]
# lv3 = [probabilidadeDadosLimite(2,6,2,2),probabilidadeDadosLimite(3,6,2,2),
#         probabilidadeDadosLimite(4,6,2,2),probabilidadeDadosLimite(5,6,2,2),]
# dif6 = [lv3[0]-lv0[0],lv3[3]-lv0[3]]


# lv200 = [probabilidadeDadosLimite(2,20,12,2),probabilidadeDadosLimite(3,20,12,2),
#         probabilidadeDadosLimite(4,20,12,2),probabilidadeDadosLimite(5,20,12,2),]
# lv201 = [probabilidadeDadosLimite(2,20,11,2),probabilidadeDadosLimite(3,20,11,2),
#         probabilidadeDadosLimite(4,20,11,2),probabilidadeDadosLimite(5,20,11,2),]
# lv202 = [probabilidadeDadosLimite(2,20,10,2),probabilidadeDadosLimite(3,20,10,2),
#         probabilidadeDadosLimite(4,20,10,2),probabilidadeDadosLimite(5,20,10,2),]
# lv203 = [probabilidadeDadosLimite(2,20,9,2),probabilidadeDadosLimite(3,20,9,2),
#         probabilidadeDadosLimite(4,20,9,2),probabilidadeDadosLimite(5,20,9,2),]
# dif20 = [lv203[0]-lv200[0],lv203[3]-lv200[3]]


# lv120 = [probabilidadeDadosLimite(2,12,8,2),probabilidadeDadosLimite(3,12,8,2),
#         probabilidadeDadosLimite(4,12,8,2),probabilidadeDadosLimite(5,12,8,2),]
# lv121 = [probabilidadeDadosLimite(2,12,7,2),probabilidadeDadosLimite(3,12,7,2),
#         probabilidadeDadosLimite(4,12,7,2),probabilidadeDadosLimite(5,12,7,2),]
# lv122 = [probabilidadeDadosLimite(2,12,6,2),probabilidadeDadosLimite(3,12,6,2),
#         probabilidadeDadosLimite(4,12,6,2),probabilidadeDadosLimite(5,12,6,2),]
# lv123 = [probabilidadeDadosLimite(2,12,5,2),probabilidadeDadosLimite(3,12,5,2),
#         probabilidadeDadosLimite(4,12,5,2),probabilidadeDadosLimite(5,12,5,2),]
# dif12 = [lv123[0]-lv120[0],lv123[3]-lv120[3]]


# lv1000 = [probabilidadeDadosLimite(2,100,52,2),probabilidadeDadosLimite(3,100,52,2),
#         probabilidadeDadosLimite(4,100,52,2),probabilidadeDadosLimite(5,100,52,2),]
# lv1001 = [probabilidadeDadosLimite(2,100,51,2),probabilidadeDadosLimite(3,100,51,2),
#         probabilidadeDadosLimite(4,100,51,2),probabilidadeDadosLimite(5,100,51,2),]
# lv1002 = [probabilidadeDadosLimite(2,100,50,2),probabilidadeDadosLimite(3,100,50,2),
#         probabilidadeDadosLimite(4,100,50,2),probabilidadeDadosLimite(5,100,50,2),]
# lv1003 = [probabilidadeDadosLimite(2,100,49,2),probabilidadeDadosLimite(3,100,49,2),
#         probabilidadeDadosLimite(4,100,49,2),probabilidadeDadosLimite(5,100,49,2),]
# dif100 = [lv1003[0]-lv1000[0],lv1003[3]-lv1000[3]]


# lv1030 = [probabilidadeDadosLimite(2,100,54,2),probabilidadeDadosLimite(3,100,54,2),
#         probabilidadeDadosLimite(4,100,54,2),probabilidadeDadosLimite(5,100,54,2),]
# lv1031 = [probabilidadeDadosLimite(2,100,51,2),probabilidadeDadosLimite(3,100,51,2),
#         probabilidadeDadosLimite(4,100,51,2),probabilidadeDadosLimite(5,100,51,2),]
# lv1032 = [probabilidadeDadosLimite(2,100,48,2),probabilidadeDadosLimite(3,100,48,2),
#         probabilidadeDadosLimite(4,100,48,2),probabilidadeDadosLimite(5,100,48,2),]
# lv1033 = [probabilidadeDadosLimite(2,100,45,2),probabilidadeDadosLimite(3,100,45,2),
#         probabilidadeDadosLimite(4,100,45,2),probabilidadeDadosLimite(5,100,45,2),]
# dif103 = [lv1033[0]-lv1030[0],lv1033[3]-lv1030[3]]

# print("d6")
# print(lv0)
# print(lv1)
# print(lv2)
# print(lv3)
# print(dif6)

# print("d10")
# print(lv100)
# print(lv101)
# print(lv102)
# print(lv103)
# print(dif10)

# print("d12")
# print(lv120)
# print(lv121)
# print(lv122)
# print(lv123)
# print(dif12)

# print("d20")
# print(lv200)
# print(lv201)
# print(lv202)
# print(lv203)
# print(dif20)

# print("d100")
# print(lv1000)
# print(lv1001)
# print(lv1002)
# print(lv1003)
# print(dif100)

# print("d100-3")
# print(lv1030)
# print(lv1031)
# print(lv1032)
# print(lv1033)
# print(dif103)