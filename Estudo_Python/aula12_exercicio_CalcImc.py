nome = input('Qual o seu nome :')
altura = input('qual a sua altura: ')
peso = input('qual o seu peso: ')

altura =float(altura)
peso =float(peso)

imc = peso // (altura * altura)

print(nome, 'sua altura é:', altura, 'seu peso é :', peso, 'seu imc é :', imc)

# usar ... serve para deixar em aberto um ponto do codigo que vai ser escrito mas sem gerar erros
