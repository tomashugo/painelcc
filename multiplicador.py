def multiplicador(numero):
   digito1  = int(numero[0])
   digito2  = int(numero[1])
   digito3  = int(numero[2])
   digito4  = int(numero[3])
   digito5  = int(numero[4])
   digito6  = int(numero[5])
   digito7  = int(numero[6])
   digito8  = int(numero[7])
   digito9  = int(numero[8])
   digito10 = int(numero[9])

   multiplicacao = digito1*5 + digito2*4 + digito3*3 + digito4*2 + digito5*7 + digito6*6 + digito7*5 + digito8*4 + digito9*3 + digito10*2
   resto = multiplicacao % 11

   if resto == 0 or resto == 1:
      return 0
   else:
      return 11-resto

print multiplicador("3304003576")

