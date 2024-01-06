nome = input('Qual o seu nome :')
altura = input('qual a sua altura: ')
peso = input('qual o seu peso: ')

altura =float(altura)
peso =float(peso)

imc = peso // (altura * altura)

#print(nome, 'sua altura é:', altura, 'seu peso é :', peso, 'seu imc é :', imc)

# usar ... serve para deixar em aberto um ponto do codigo que vai ser escrito mas sem gerar erros

#formatação do resultado usando f'

#formatação de print para diminuir a linha de resposta

resultado = f' {nome} sua altura é: {altura:.2f} , seu peso é : {peso} e seu imc é : {imc:.2f}'
print(resultado)

#no campo altura depois dos dois pontos, o termo .2f significa a quantidade de casas decimais que serão usadas, no caso duas.


