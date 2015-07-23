# trabalhoRecuperacao
18-07-2015: Pesquisas sobre o jogo de Hanoi e estrutrando servidor.
19-07-2015: Pesquisas sobre o jogo de Hanoi e estrutrando servidor.
20-07-2015: Algoritimo para de Hannoi finalizado.
21-07-2015: Testando o programa Hannoi.py. No cygwin aparece "POST" 200 mas nada é gravado no banco de dados.
22-07-2015: O programa grava os testes no banco de dados. Alterações no mauaserver no model e no hannoi.
23-07-2015: Trabalho finalizado.

Rodrigo Tanure Tricarico R.A: 12.01517-2

                                                          TESTE HANNOI  

Este trabalho consiste de:

- um seridor web (mauaserver.py) que foi constriudo com o framework FLASK e está preparado para gravar e listar informações (do tipo JSON) de um banco de dados (SQLalchemy), que deve ter sido previamente criado, que se chama testes.db .  As rotas e suas respectivas funções do servidor são:

      	    Lista os testes: http://localhost:5000/testes (método GET)
	
	    Link para postar os testes: http://localhost:5000/medida/new (método POST)
		
	    Lista os conjuntos: http://localhost:5000/conjuntos (método GET)

- um cliente chamado Hannoi.py onde o usuário informa pelo prompt quantos testes deseja realizar e quantas peças cada teste terá. O programa faz os calculos de quantos movimentos serão nescessários para cada teste e envia as informações para o servidor no seguinte formato e.g:
- {
    "contador": 4,
    "testes": [
        {
            "movimentos": 1023,
            "identificacao": "teste0"
        },
        {
            "movimentos": 32767,
            "identificacao": "teste1"
        },
        {
            "movimentos": 1023,
            "identificacao": "teste2"
        },
        {
            "movimentos": 7,
            "identificacao": "teste3"
        }
    ]
}
  (obs: a lista testes pode conter mais ou menos informacoes dependendo do usuario)

- um cliente chamado Hannoi2.py que contem uma função chamada Enviajson(n) onde n é uma lista de números inteiros que representam a quantidade de peças em cada teste. O programa faz os calculos de quantos movimentos serão nescessários para cada teste e envia as informações (do mesmo tipo acima) para o servidor.

