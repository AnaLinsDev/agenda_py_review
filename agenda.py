
contatos = [
    {"name": "Maria",
     "telefone":  "83988664455",
     "email": "maria@gmail.com", 
     "favorito": True},
     {"name": "João",
     "telefone":  "83988664455",
     "email": "joao@gmail.com", 
     "favorito": False}
     ]


def get_contatos():
    print("\nContatos:")
    for index, contato in enumerate(contatos):
        fav = ""
        if (contato['favorito']):
            fav = "\u2605"
        print(index + 1, " - ", contato['name'], " - ", contato['telefone'] , " - ", contato['email'], " ",  fav)

def get_contatos_favoritos():
    print("\nContatos Favoritos :")
    for index, contato in enumerate(contatos):

        if (contato['favorito']):
            print(index + 1, " - ", contato['name'], " - ", contato['telefone'] , " - ", contato['email'], " \u2605")


def change_fav(id):
    contatos[id]["favorito"] = not contatos[id]["favorito"]

    if (contatos[id]["favorito"]):
        print("Contato inserido nos favoritos com sucesso !")
    else:
        print("Contato removido dos favoritos com sucesso !")

def add_contato(name, fone, email):
    contatos.append({"name": name,
                     "telefone":  fone,
                     "email": email,
                     "favorito": False})
    

def edit_contato(id, name, fone, email):
    
    if (name != ""):
        contatos[id]["name"] = name

    if (fone != ""):
        contatos[id]["telefone"] = fone

    if (email != ""):
        contatos[id]["email"] = email

    
def del_contato(id):
    del contatos[id]


def validate_id(id):
    try:
        contatos[id]
    except:
        raise Exception("Id inválido")


def agenda_gerenciamento():
    out = 1

    while(out):
        print("\n\n----- AGENDA ----- \n")
        print("1 - Visualizar\n2 - Adicionar\n3 - Editar\n4 - Deletar\n5 - Favoritar/Desfavoritar\n6 - Favoritos\n7 - Sair")
        resp = input("\nEscolha uma opção:\n")

        try:
            match resp:
                case '1':
                    get_contatos()
                case '2':
                    print("Adicione um novo contato:")
                    name = input("Nome: ")
                    fone = input("Telefone: ")
                    email = input("Email: ")

                    add_contato(name, fone, email)

                    print("\nAdicionado com sucesso !\n")

                    get_contatos()

                case '3':
                    get_contatos()
                    id = input("\nSelecione o id do contato para editar:\n")

                    id = int(id) - 1
                    validate_id(id)

                    print("Edite os campos que deseja, \ncaso não queira alterar o campo, apenas clique no Enter.")
                    name = input("Nome:")
                    fone = input("Telefone: ")
                    email = input("Email: ")

                    edit_contato(id, name, fone, email)
                case '4':
                    get_contatos()
                    id = input("\nSelecione o id do contato para deletar:\n")

                    id = int(id) - 1
                    validate_id(id)

                    del_contato(id)

                case '5':
                    print("Favoritar/Desfavoritar")
                    get_contatos()
                    id = input("\nSelecione o id do contato para favoritar ou desfavoritar:\n")

                    id = int(id) - 1
                    validate_id(id)

                    change_fav(id)
                case '6':
                    get_contatos_favoritos()
                case '7':
                    out = 0
                    print("\nAplicação será fechada, até logo.\n")
                case _:
                    raise Exception("Essa opção não existe.")
        except Exception as error:
            print("\n Ocorreu um erro, tente novamente.")
            print(f"Error: {error}")



agenda_gerenciamento()
