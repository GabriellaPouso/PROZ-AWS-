def achar_elemento(arr):
    achou=False
    cumprimento=len(arr)    
    for i in range(cumprimento):
        print(arr[i])        
ordem=['Primeiro','Segundo','Terceiro']
achar_elemento(ordem)

def achar_elemento(arr):
    achou=False
    for i in range(len(arr)):
        print(arr[i])        
ordem=['Primeiro','Segundo','Terceiro']
achar_elemento(ordem)

def achar_elemento(elem,arr):
    achou=False
    for i in range(len(arr)):
        if(arr[i]==elem):
            achou=True
    if(achou==True):
        print("Achei o elemento:",elem)
    else:
        print("Não achei o elemento:",elem)
nomes=['Rafael','Luíza','Thiago','Karen','Júlia']
achar_elemento("Thiago",nomes)
achar_elemento("Luis",nomes)