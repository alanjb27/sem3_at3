print('###########################################################################')
print('##                                                                       ##')
print('##                         ESTE PROGRAMA CALCULA:                        ##')
print('##                  1) COMPRIMENTO DA CIRCUNFERÊNCIA                     ##')
print('##                  2) ÁREA DO CÍRCULO                                   ##')
print('##                  3) ÁREA DA ESFERA                                    ##')
print('##                  4) VOLUME DA ESFERA                                  ##')
print('##                                                                       ##')
print('###########################################################################')
print('')
raio = float(input('             Digite o raio para a realização dos calculos: '))
PI = 3.141592
comprimento =2*PI*raio
area_circulo = PI*raio**2
area_esfera = 4*PI*raio**2
vol_esfera = 4/3*PI*raio**3
print('Comprimento da circunferencia: %5.6f'%comprimento)
print('Área do círculo: %5.6f'%area_circulo)
print('Área da esfera: %5.6f'%area_esfera)
print('Volume dda esfera: %5.6f'%vol_esfera)
