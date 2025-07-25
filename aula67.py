'''
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem 
ter valores padrão. Caso o valor padrão não seja
enviado para o parâmetro, o valor padrão será usado.
Refatorar: editar o seu código.
'''

def soma(x, y, z=None):    # ao colocarmos um None ou um zerovai dar como FALSE
    if  z  is not  None:      #ao declaramos isso, fica mais facíl evitarmos bug's.
        print(f'{x=}    {y=}    {z=}',  x   +   y   +   z)
    else:
        print(f'{x=}    {y=}',   x   +   y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9,  0)
soma(7, z=0,    y=9)   #podemos mudar a sequencia sem problemas desde que, os renomeamos.
#aqui lembramos da régrinha padrão, ao renomearmos 1, todos após terão que ser renomeados.