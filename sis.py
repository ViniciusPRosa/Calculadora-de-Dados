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
            'probabilidade de sucesso ': prob}

def probabilidadeDadosLimite(d,n,r,a):
    """
    It calculates the probability of rolling a number equal to or greater than a given number on a given
    number of dice with a given number of sides
    
    :param d: number of dice
    :param n: number of faces on the dice
    :param r: the number you're trying to roll
    :param a: number of dice
    :return: A dictionary with the number of dice, number of faces, target number, and the probability
    of success.
    """
    prob = 1
    for i in range(a):
        comb = (fatorial(d)/(fatorial(i)*fatorial(d-i)))*(((n-r+1)/n)**i)*((1-((n-r+1)/n))**(d-i))
        prob = prob - comb
    return {'numero de dados': d,
            'número de faces': n,
            'nùmero alvo': r,
            'probabilidade de sucesso ': prob*100}

print(probabilidadeDadosLimite(3,6,3,2))
print(probabilidadeDadosLimite(4,6,4,2))

