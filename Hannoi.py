from mauaserver import *

def hannoi(n, org, dest, temp, count=0):
    if n == 1:
        count += 1
        #print('Mover de ', org, ' para destino ', dest, count)
    else:
        count = hannoi(n-1, org, temp, dest, count)
        count = hannoi(1, org, dest, temp, count)
        count = hannoi(n-1, temp, dest, org, count)
    return count
a={}


b=hannoi(3,1,2,3)


a={'identificacao':'carlos', 'movimentos':b}

data_string=json.dumps(a)
url = "http://127.0.0.1:5000/conjunto/new"
p = requests.post(url, data=data_string)
