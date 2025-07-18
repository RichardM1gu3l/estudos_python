'''
Calculo do primeiro digito do CPF

CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando de 10.

Ex: 746.824.890-70 (74682489070)
    10  9  8  7  6  5  4  3  2 
*   7   4  6  8  2  4  8  9  0 
    70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
 resultado é 0
contrário disso:
reultado é o valor da conta

O primeiro dígito do CPF é 7.
'''
#minha resolução --- inferrujado ----
'''
cpf = int(input("Digite o número do seu CPF: "))
num_inteiros_dig = list(str(cpf))
num_inteiros_dig[:9] 

nova_lista_int = [int(digito) for digito in num_inteiros_dig]

primeiros_dig = nova_lista_int[0] * 10
segundo_dig = nova_lista_int[1] * 9
terceiro_dig = nova_lista_int[2] * 8
quarto_dig = nova_lista_int[3] * 7
quinto_dig = nova_lista_int[4] * 6
sexto_dig = nova_lista_int[5] * 5
setimo_dig = nova_lista_int[6] * 4
oitavo_dig = nova_lista_int[7] * 3
nono_dig = nova_lista_int[8] * 2

resultado   =   primeiros_dig   +   segundo_dig +   terceiro_dig    +   quarto_dig  +   quinto_dig  +   sexto_dig   +   setimo_dig  +   oitavo_dig  +   nono_dig
resul_por_dez   =   resultado   *   10
sobra_resul =   resul_por_dez   %   11

print(sobra_resul)


#OOOoooooouuuuuuuuuuu resolução do professor


cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo = 10

resultado = 0
for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1
print(resultado * 10 % 11)



#para fazer o calcúlo do 2° digito adicionar o digito e o 11 na multiplicação


cpf = int(input("Digite o número do seu CPF: "))
num_inteiros_dig = list(str(cpf))
num_inteiros_dig[:9] 

nova_lista_int = [int(digito) for digito in num_inteiros_dig]

primeiros_dig = nova_lista_int[0] * 11
segundo_dig = nova_lista_int[1] * 10
terceiro_dig = nova_lista_int[2] * 9
quarto_dig = nova_lista_int[3] * 8
quinto_dig = nova_lista_int[4] * 7
sexto_dig = nova_lista_int[5] * 6
setimo_dig = nova_lista_int[6] * 5
oitavo_dig = nova_lista_int[7] * 4
nono_dig = nova_lista_int[8] * 3
decimo_dig = nova_lista_int[9] * 2

resultado   =   primeiros_dig   +   segundo_dig +   terceiro_dig    +   quarto_dig  +   quinto_dig  +   sexto_dig   +   setimo_dig  +   oitavo_dig  +   nono_dig    +   decimo_dig
resul_por_dez   =   resultado   *   10
sobra_resul =   resul_por_dez   %   11

print(sobra_resul)

#OOOoooooouuuuuuuuuuu resolução do professor
'''

cpf_enviado_usuario = '74682489070'
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1    =   (resultado_digito_1 * 10)   % 11
digito_1    =   digito_1    if  digito_1    <=  9   else    0

dez_digitos = nove_digitos  + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2  =   0
for digito  in  dez_digitos:
    resultado_digito_2  +=  int(digito) *   contador_regressivo_2
    contador_regressivo_2   -=  1
digito_2    = (resultado_digito_2   *   10) %   11
digito_2    =   digito_2    if  digito_2    <= 9    else    0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if  cpf_enviado_usuario ==  cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario}   é váliodo')
else:
    print('CPF inválido')