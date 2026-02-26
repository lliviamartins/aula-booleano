'''
Construindo a lógica not
'''

var1= True
var2= False
print('var1 {} quando negada fica {}'.format(var1,not var1))
print('var2 {} quando negada fica {}'.format(var2,not var2))

''' 
Construindo a lógica do AND (E)
'''

var1_t= True
var1_f= False
var2_t= True
var2_f= False

print('Quando var1_t é {} E var2_t {} o resultado é {}'.format(var1_t,var2_t,var1_t and var2_t))
print('Quando var1_f é {} E var2_t {} o resultado é {}'.format(var1_f,var2_t,var1_f and var2_t))
print('Quando var1_t é {} E var2_f {} o resultado é {}'.format(var1_t,var2_f,var1_t and var2_f))
print('Quando var1_f é {} E var2_f {} o resultado é {}'.format(var1_f,var2_f,var1_f and var2_f))

'''
Construindo a logica do OR(ou)
'''

print('Quando var1_t é {} E var2_t {} o resultado é {}'.format(var1_t,var2_t,var1_t or var2_t))
print('Quando var1_f é {} E var2_t {} o resultado é {}'.format(var1_f,var2_t,var1_f or var2_t))
print('Quando var1_t é {} E var2_f {} o resultado é {}'.format(var1_t,var2_f,var1_t or var2_f))
print('Quando var1_f é {} E var2_f {} o resultado é {}'.format(var1_f,var2_f,var1_f or var2_f))

'''
Multiplas regras de lógica
'''

var_resultado=var1_t and var2_f or var1_f or var2_t and not var2_f
print ('O resultado da lógica é {}'.format(var_resultado))

