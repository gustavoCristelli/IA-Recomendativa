# --- 1. Representação do Conhecimento com FRAMES ---

# A base de dados continua a mesma, representando os filmes como dicionários (Frames).
base_conhecimento_filmes = {
    "Oppenheimer": {
        "diretor": "Christopher Nolan",
        "genero": ["Biografia", "Drama"],
        "atores": ["Cillian Murphy", "Emily Blunt"],
        "ano": 2023
    },
    "Interestelar": {
        "diretor": "Christopher Nolan",
        "genero": ["Ficção Científica", "Aventura"],
        "atores": ["Matthew McConaughey", "Anne Hathaway"],
        "ano": 2014
    },
    "Titanic": {
        "diretor": "James Cameron",
        "genero": ["Romance", "Drama"],
        "atores": ["Leonardo DiCaprio", "Kate Winslet"],
        "ano": 1997
    },
    "A Origem": {
        "diretor": "Christopher Nolan",
        "genero": ["Ficção Científica", "Ação"],
        "atores": ["Leonardo DiCaprio", "Elliot Page"],
        "ano": 2010
    }
}

# --- 2. Aplicação da LÓGICA (Regra de Recomendação) ---

# A função de lógica não muda. Ela ainda faz a busca dos filmes do mesmo diretor.
def recomendar_por_diretor(filme_gostado, base_de_conhecimento):
    """
    Função que aplica a regra de recomendação baseada no diretor.
    
    Argumentos:
    filme_gostado (str): O título do filme que o usuário gostou.
    base_de_conhecimento (dict): A base de dados com os frames dos filmes.
    
    Retorna:
    list: Uma lista de filmes recomendados.
    """
    
    # O método .get() é usado para evitar erros caso o filme não exista.
    dados_filme = base_de_conhecimento.get(filme_gostado)
    if not dados_filme:
        return []

    diretor_do_filme = dados_filme["diretor"]
    
    filmes_recomendados = []

    for titulo_filme, dados in base_de_conhecimento.items():
        if dados["diretor"] == diretor_do_filme and titulo_filme != filme_gostado:
            filmes_recomendados.append(titulo_filme)
            
    return filmes_recomendados

# --- 3. Execução Interativa do Sistema ---

def main():
    """
    Função principal que interage com o usuário.
    """
    print("Olá! Bem-vindo ao nosso sistema de recomendação de filmes.")
    print("Por favor, escolha um filme da nossa lista e digite o nome completo:")
    
    # Mostra a lista de filmes disponíveis para o usuário
    lista_filmes_disponiveis = ", ".join(base_conhecimento_filmes.keys())
    print(f"Filmes disponíveis: {lista_filmes_disponiveis}")

    # A entrada do usuário é capturada aqui, tornando o código interativo.
    filme_escolhido_pelo_usuario = input("\nDigite o nome do filme que você gostou: ")
    
    # Capitaliza a primeira letra de cada palavra para evitar erros de digitação.
    filme_escolhido_pelo_usuario = filme_escolhido_pelo_usuario.title()

    recomendacoes = recomendar_por_diretor(filme_escolhido_pelo_usuario, base_conhecimento_filmes)

    if recomendacoes:
        print("\nCom base na nossa regra, nós recomendamos os seguintes filmes:")
        for filme in recomendacoes:
            print(f"- {filme}")
    else:
        print(f"\nDesculpe, '{filme_escolhido_pelo_usuario}' não está na nossa base ou não temos recomendações para ele.")
        print("Tente outro filme da lista.")

# Chama a função principal para iniciar o programa
if __name__ == "__main__":
    main()