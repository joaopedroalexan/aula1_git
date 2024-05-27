# Etapa 1: Criar uma lista vazia chamada beatles
beatles = []
print("Etapa 1:", beatles)

# Etapa 2: Adicionar membros iniciais à lista
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Etapa 2:", beatles)

# Etapa 3: Adicionar membros adicionais à lista
print("Etapa 3: Solicitando membros adicionais...")
novos_membros = []
for i in range(2):
    novo_membro = input("Digite o nome de um novo membro da banda: ")
    novos_membros.append(novo_membro)

for membro in novos_membros:
    beatles.append(membro)
print("Etapa 3:", beatles)

# Etapa 4: Remover membros "Stu Sutcliffe" e "Pete Best" da lista
print("Etapa 4: Removendo membros 'Stu Sutcliffe' e 'Pete Best'...")
del beatles[-2:]  # Remove os dois últimos elementos da lista
print("Etapa 4:", beatles)

# Etapa 5: Adicionar Ringo Starr ao início da lista usando o método insert()
print("Etapa 5: Adicionando Ringo Starr ao início da lista...")
beatles.insert(0, "Ringo Starr")
print("Etapa 5:", beatles)

# Testando o tamanho da lista
print("O fabuloso número de membros dos Beatles:", len(beatles))
