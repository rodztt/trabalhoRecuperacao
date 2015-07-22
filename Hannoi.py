from mauaserver import *

#Funcao hannoi com contador

def hannoi(n, org, dest, temp, count=0):
    if n == 1:
        count += 1
        #print('Mover de ', org, ' para destino ', dest, count)
    else:
        count = hannoi(n-1, org, temp, dest, count)
        count = hannoi(1, org, dest, temp, count)
        count = hannoi(n-1, temp, dest, org, count)
    return count

#Numero de testes

while True:
    try:
        l = int(raw_input("Digite quantos testes do hannoi deseja realizar: "))
        if (l>0 and l<=10):
            break
        else:
            print("Digite um numero maior que 0 e menor que 10")
    except ValueError:
        print "Digite um numero inteiro"

#p - lista de pecas

p=[]

#Pecas para cada teste

while (True):
    try:
        for i in range(l):
            while (True):
                x = int(raw_input(("Digite um numero de pecas maior que 0 e menor que 30. #%i:  ")%i))
                if (x>0 and x<=30):
                    break
            p.append(x)
        break
    except ValueError:
        print "Erro: Digite um numero de pecas maior que 0 e menor que 30:"
print p

#utilizando a funcao para cada item na lista de pecas

j=[]
for f in range(l):
    n=hannoi(p[f],1,2,3)
    j.append({'identificacao':'teste%i'%f,'movimentos':n})
f={'contador':l,'testes':j}
f_json=json.dumps(f)
print f_json
