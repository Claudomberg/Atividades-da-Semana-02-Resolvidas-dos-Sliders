senhax = "python123"
t = 0

while t < 3:
    senha = input("Digite a senha: ")
    t += 1
    
    if senha == senhax:
        print("Acesso liberado!")
        break
else:
    print("Sistema bloqueado após 3 erros.")