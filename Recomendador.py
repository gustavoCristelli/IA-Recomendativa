# Importa a base de conhecimento de filmes do arquivo Database.py
from Database import base_conhecimento_filmes

# --- LÓGICA (Regra de Recomendação) ---
# A função de lógica permanece a mesma, pois a regra é independente da base de dados.

def recomendar_por_diretor(filme_gostado, base_de_conhecimento):
    """
    Função que aplica a regra de recomendação baseada no diretor.
    
    Argumentos:
    filme_gostado (str): O título do filme que o usuário gostou.
    base_de_conhecimento (dict): A base de dados com os frames dos filmes.
    
    Retorna:
    list: Uma lista de filmes recomendados.
    """
    
    dados_filme = base_de_conhecimento.get(filme_gostado)
    if not dados_filme:
        return []

    diretor_do_filme = dados_filme["diretor"]
    
    filmes_recomendados = []

    for titulo_filme, dados in base_de_conhecimento.items():
        if dados["diretor"] == diretor_do_filme and titulo_filme != filme_gostado:
            filmes_recomendados.append(titulo_filme)
            
    return filmes_recomendados

# --- EXECUÇÃO INTERATIVA DO SISTEMA ---
# A execução do programa agora utiliza a base de dados importada.

def main():
    """
    Função principal que interage com o usuário.
    """
    print("Olá! Bem-vindo ao nosso sistema de recomendação de filmes.")
    print("Por favor, escolha um filme da nossa lista e digite o nome completo:")
    
    lista_filmes_disponiveis = "\n -".join(base_conhecimento_filmes.keys())
    print(f"Filmes disponíveis: {lista_filmes_disponiveis}")

    filme_escolhido_pelo_usuario = input("\nDigite o nome do filme que você gostou: ")
    filme_escolhido_pelo_usuario = filme_escolhido_pelo_usuario.title()

    recomendacoes = recomendar_por_diretor(filme_escolhido_pelo_usuario, base_conhecimento_filmes)

    if recomendacoes:
        print("\nCom base na nossa regra, nós recomendamos os seguintes filmes:")
        for filme in recomendacoes:
            print(f"- {filme}")
    else:
        print(f"\nDesculpe, '{filme_escolhido_pelo_usuario}' não está na nossa base ou não temos recomendações para ele.")
        print("Tente outro filme da lista.")

if __name__ == "__main__":
    main()