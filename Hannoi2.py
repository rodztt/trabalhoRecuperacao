#Para usar este modulo deve se importar este modulo e usar a funcao
#Enviajson(n) sendo n uma lista de numeros inteiros onde 0 corresponde o final
#da lista

#from mauaserver import *

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

#Funcao Enviajson

def Enviajson(n):
    j=[]
    l=len(n)
    for f in range(l):
        if n[f]==0:
            break
        y=hannoi(n[f],1,2,3)
        j.append({'identificacao':'teste%i'%f,'movimentos':y})
    k={'contador':l-1,'testes':j}
    url = 'http://127.0.0.1:5000/conjunto/new'
    payload = k
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print ("dados enviados: ")
    print json.dumps(payload)
