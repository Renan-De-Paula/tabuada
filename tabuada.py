# Laço infinito para continuar pedindo o número da tabuada até o usuário digitar 0 para parar
while True:
    # Solicita ao usuário qual valor deseja ver a tabuada
    n = int(input("Quer ver a tabuada de qual valor? [0 para parar]"))
    
    # Se o número for menor ou igual a zero, o programa é encerrado
    if n <= 0:
        break  # Sai do laço se o número for não positivo
    
    # Exibe uma linha para separar a tabuada
    print("-" * 30)
    
    # Laço que calcula e exibe a tabuada do número de 1 a 10
    for c in range(1, 11):
        print(f"{n} X {c} = {n * c}")  # Exibe a multiplicação da tabuada
        
        # c =+ 1 # Linha redundante, pois o 'for' já faz isso automaticamente.
    
    # Exibe uma linha de separação após a tabuada
    print("-" * 30)

# Exibe uma mensagem final indicando que o programa foi encerrado
print("Programa encerrado. Volte sempre!")