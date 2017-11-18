##Base da dados
from math import sqrt

'''avaliacoes = {'Ana': 
		{'Freddy x Jason': 2.5, 
		 'O Ultimato Bourne': 3.5,
		 'Star Trek': 3.0, 
		 'Exterminador do Futuro': 3.5, 
		 'Norbit': 2.5, 
		 'Star Wars': 3.0},
	 
	  'Marcos': 
		{'Freddy x Jason': 3.0, 
		 'O Ultimato Bourne': 3.5, 
		 'Star Trek': 1.5, 
		 'Exterminador do Futuro': 5.0, 
		 'Star Wars': 3.0, 
		 'Norbit': 3.5}, 

	  'Pedro': 
                {'Freddy x Jason': 2.5, 
		 'O Ultimato Bourne': 3.0,
		 'Exterminador do Futuro': 3.5, 
		 'Star Wars': 4.0},
			 
	  'Claudia': 
		{'O Ultimato Bourne': 3.5, 
		 'Star Trek': 3.0,
		 'Star Wars': 4.5, 
		 'Exterminador do Futuro': 4.0, 
		 'Norbit': 2.5},
				 
	  'Adriano': 
		{'Freddy x Jason': 3.0, 
		 'O Ultimato Bourne': 4.0, 
		 'Star Trek': 2.0, 
		 'Exterminador do Futuro': 3.0, 
		 'Star Wars': 3.0,
		 'Norbit': 2.0}, 

	  'Janaina': 
	     {'Freddy x Jason': 3.0, 
	      'O Ultimato Bourne': 4.0,
	      'Star Wars': 3.0, 
	      'Exterminador do Futuro': 5.0, 
	      'Norbit': 3.5},
			  
	  'Leonardo': 
	    {'O Ultimato Bourne':4.5,
             'Norbit':1.0,
	     'Exterminador do Futuro':4.0}
}'''

##Base de dados invertida
avaliacoes = {'Freddy x Jason': 
		{'Ana': 2.5, 
		 'Marcos:': 3.0 ,
		 'Pedro': 2.5, 
		 'Adriano': 3.0, 
		 'Janaina': 3.0 },
	 
	 'O Ultimato Bourne': 
		{'Ana': 3.5, 
		 'Marcos': 3.5,
		 'Pedro': 3.0, 
		 'Claudia': 3.5, 
		 'Adriano': 4.0, 
		 'Janaina': 4.0,
		 'Leonardo': 4.5 },
				 
	 'Star Trek': 
		{'Ana': 3.0, 
		 'Marcos:': 1.5,
		 'Claudia': 3.0, 
		 'Adriano': 2.0 },
	
	 'Exterminador do Futuro': 
		{'Ana': 3.5, 
		 'Marcos:': 5.0 ,
		 'Pedro': 3.5, 
		 'Claudia': 4.0, 
		 'Adriano': 3.0, 
		 'Janaina': 5.0,
		 'Leonardo': 4.0},
				 
	 'Norbit': 
		{'Ana': 2.5, 
		 'Marcos:': 3.0 ,
		 'Claudia': 2.5, 
		 'Adriano': 2.0, 
		 'Janaina': 3.5,
		 'Leonardo': 1.0},
				 
	 'Star Wars': 
		{'Ana': 3.0, 
		 'Marcos:': 3.5,
		 'Pedro': 4.0, 
		 'Claudia': 4.5, 
		 'Adriano': 3.0, 
		 'Janaina': 3.0}
}

##Função da distância euclidiana
def distancia_euclidiana(user1, user2):
    si = {}
    for item in avaliacoes[user1]: ##Retorna todos os itens que o user assistiu
        if item in avaliacoes[user2]: ##Se o user2 tambem assistiu os mesmos filmes
            si [item] = 1
    if len(si) == 0:
        return 0

    ##Faz o somatório apenas para os filmes em comum entre os usuários
    soma = sum([pow(avaliacoes[user1][item] - avaliacoes[user2][item],2)
                for item in avaliacoes[user1] if item in avaliacoes[user2]])

    return 1/(1+sqrt(soma))

##Função que retorna a similaridade entre usuário
def getSimilares(user):
    similaridade = [(distancia_euclidiana(user, outro), outro)
                    for outro in avaliacoes if outro != user]
    similaridade.sort()
    similaridade.reverse()
    return similaridade

##Função de recomendação
def getRecomendacoes(user):
    totais={}
    somaSimilaridades={}

    for outro in avaliacoes:
        if outro == user:
            continue
        similaridade = distancia_euclidiana(user,outro)
        
        if similaridade <= 0:
            continue
        
        ##Percorre os filmes que o outro usuário
        for item in avaliacoes[outro]:
            ##Verifica se o filme não foi assistido pelo usuário
            if item not in avaliacoes[user]:
                ##Inicializa. Key: item, valor: 0
                totais.setdefault(item,0)
                totais[item] += avaliacoes[outro][item] * similaridade
                somaSimilaridades.setdefault(item,0)
                somaSimilaridades[item] += similaridade

    rankings=[(total / somaSimilaridades[item], item) for item, total in totais.items()]
    rankings.sort()
    rankings.reverse()
    return rankings




