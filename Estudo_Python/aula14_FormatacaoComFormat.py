#Formatação

a = 'A'
b = 'B'
c = 1.1
#            a    b    c adicionado  duas casas decimais com o :.2f
string = 'a={} b={} c={:.2f}'       # a primeira chave puxa o primeiro valor e assim sucessivamente
#indice     0    1     2        #pode se jogar o valor do indice dentro da chave , assim pode ser colocar a posição 
#                                dos elementos a,b e c em ordens diferentes

formato = string.format(a,b,c)  #puxou as variaveis para dentro do .format.
#indice                 0 1 2   esses indices vão ser puxados para os elementos da variavel string e só assim o print vai ser realizado

#parametro nomeado
formato = string.format(
    nome1=a, nome2=b, nome=c) # nesse caso os elementos da variavel string teriam que ter os nomes alterados para nome1 nome2 e etc..

#formato ='a={} b={} c={}' .format(a,b,c)  #puxou as variaveis para dentro do .format.

print(formato)