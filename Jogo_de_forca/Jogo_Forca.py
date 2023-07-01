secreto = 'comida'
digitadas = []
chances = 3
print('-=' *20)
print('        JOGO DA FORÇA PYTHON      ')
print('-=' *20)

while True:
    letra = str(input("digite uma letra: "))
    
    
    if len(letra)>1:
        print("Erro! Não vale digitar mais uma letra.")
        continue
    
    digitadas.append(letra)
    
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario = '*'
            
            
    if secreto_temporario == secreto:
        print('Você venceu e escapou da força. ')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
        
        
    if letra not in secreto:
        chances -= 1
        
    if chances <= 0:
        print('Você perdeu! ')
        break
    
    print(f'Você tem {chances} chances. ')
    print()
    