# Operadores  /  Operação
#   ==           Igual a
#   !=           Diferente de
#   >            Maior que
#   <            Menor que
#   >=           Maior ou Igual a
#   <=           Menor ou Igual a

x = y = z = False

n1 = n2 = 0

# forma 1 de capturar o que foi digitado
print('Dugite um número: ')
n1 = int(input())

# forma 2 de capturar o que foi digitado
n2 = int(input('Digite outro número:\n'))

x = n1 == n2
print('São iguais?', x, '\n')


z = n1 > n2
print(n1, 'é maior que',n2,'?', z, '\n')


y = n1 != n2
print('São diferentes? ' + str(y))