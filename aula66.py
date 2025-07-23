def trem(vagao1,    vagao2,    vagao3):
    #definição de função + parametros
    print(f'{vagao1=}    vagao2={vagao2}   {vagao3=}',  '|',    'vagao1 + vagao2 + vagao3', vagao1  +   vagao2  +   vagao3)

trem(15,    25, 35)
 #aqui demos os argumetos não nomeados

trem(15,   vagao2=25,   vagao3=40)
 #aqui argumentos nomeados, a partir do argumento que foi nomeado em diante: todos precisam ser nomeados ou ocorr um ERRO.

print(15,    25,    35, sep='-')
    #aqui apenas adicionamos aquela separação.