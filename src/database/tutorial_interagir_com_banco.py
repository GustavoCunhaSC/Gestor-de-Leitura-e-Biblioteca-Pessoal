import sqlite3 # serve para importar Sistema de Gerenciamento de banco de dados sqlite

# serve para conectar o seu arquivo.py com o banco de dados que eu criei chamado gerenciador_de_leitura.db
import os 
CAMINHO_BANCO = os.path.join(os.path.dirname(__file__), 'gerenciador_de_leitura.db')
conexao = sqlite3.connect(CAMINHO_BANCO)
cursor = conexao.cursor()

#serve para importar para o seu arquivo.py essas bibliotecas contém as funções que criei

from funcoes_insercao import * #essa biblioteca contem as funções de inserção, ela serve para adicionar dados no banco 
from funcoes_consulta import * #essa biblioteca contem as funcões de consulta, elas servem para ver os dados no banco
from funcoes_edicao import *   #essa biblioteca contem as funções de edição, ela serve para editar dados no banco
from funcoes_exclusao import * #essa biblioteca contem as funções de exclusão, ela serve para excluir dados no banco de dados

#ABAIXO VOU COLOCAR TODAS AS FUNÇÕES E EXPLICAR PARA QUE CADA UMA SERVE

#FUNÇÃO PARA INSERÇÃO DE DADOS

inserir_livro() #server para inserir um novo livro ao banco de dados, ele recebe 3 dados entre os parênteses
                #inserir_livro("titulo do livro", "nome do autor", status do livro) obs: os status do livro é um INT, voce digita 1 para "lido", 2 para "lendo", ou 3 para "quero ler"
                #exemplo: inserir_livro("Turma da Monica", "Mauricio de Sousa", 2)

#FUNÇÕES PARA CONSULTA DE DADOS

consultar_livros() #serve para consultar todos os dados do bancos de dados 
                   #mostra todos os livros que estão registrados no banco de dados junto com o nome do autor e status de leitura

consultar_por_autor() #serve para consultar os livros de determinado autor no banco de dados, ele recebe o nome do autor entre os parênteses
                      #mostra todos os livros escritos por aquele autor que você escreveu junto com o status de leitura
                      #consultar_por_autor("nome do autor")
                      #exemplo: consultar_por_autor("Mauricio de sousa")

consultar_por_titulo() #serve para consultar um livro especifico pelo nome dele, ele recebe o nome do livro entre os parênteses
                       #mostra o livro que você escreveu o titulo junto com o autor e status de leitura
                       #consultar_por_titulo("titulo do livro")
                       #exemplo: consultar_por_titulo("Turma da Monica")

consultar_por_status() #serve para consultar livros pelo status que vc digitar, ele recebe o numero referente status de leitura entre os parênteses
                       #ele mostra todos os livros que estão no status de leitura que você digitou
                       #consultar_por_status("1 para lidos, 2 para lendo ou 3 para quero ler)")
                       #exemplo : consultar_por_titulo(3)

consultar_livros_apenas() #serve para mostrar apenas os livros 
                          #mostra uma lista de todos os livros cadastrados no banco

consultar_autores_apenas() #serve para mostrar apenas os autores 
                           #mostra uma lista de todos os autores cadastrados no banco


#FUNÇÕES PARA EDIÇÃO DE DADOS

editar_titulo_livro() #serve para editar o titulo do livro, ela recebe 2 dados entre os parênteses 
                      #editar_titulo_livro(id do livro que vc quer mudar o nome, "novo nome do livro")
                      #exemplo: editar_titulo_livro(2, "Chico Bento")
                      #obs: caso você não saiba o id do livro é so chamar a função consultar_livros_apenas(), ela mostra o nome e id de todos os livros

editar_nome_autor() #serve para editar o nome do autor, ele recebe 2 dados entre os parênteses 
                    #editar_nome_autor(id do auto que voce quer mudar o nome, "novo nome do autor")
                    #exemplo: editar_nome_autor(3, "Monteiro Lobato") 
                    # obs: se vc não sabe o id do autor é so chamar a função consultar_autores_apenas(), ela mostra o nome e id de todos os autores

editar_status_livro() #serve para editar o status de um livro, recebe 2 dados entre os parênteses
                      #editar_status_livro(id do livro que você quer mudar, numero do status de leitura para o qual voce quer mudar (1 para lido, 2 para lendo, 3 para quero ler) )
                      #exemplo editar_status_livro(2, 3)
                      #obs: caso você não saiba o id do livro é so chamar a função consultar_livros_apenas(), ela mostra o nome e id de todos os livros

#FUNÇÕES PARA EXCLUSÃO DE DADOS

excluir_livro_por_id() #serve para excluir um livro pelo id do livro, ele recebe o id do livro entre os parênteses
                       #excluir_livro_por_id(id do livro que você quer excluir)
                       #exemplo: excluir_livro_por_id(3)
                       #se voce não sabe o id do livro que quero excluir, é so chamar a função consultar_livros_apenas(),  ela mostra o nome e id de todos os livros

excluir_livro_por_titulo() #serve para excluir um livro pelo titulos do livro, ele recebe o titulo do livro entre os parênteses
                           #excluir_livro_por_titulo("nome do livro que você quer excluir")
                           #exemplo: excluir_livro_por_titulo("Turma da Monica")
  
excluir_livro_por_status() #serve para excluir livros pelo status de leitura, ele recebe o numero referente ao status entre os parênteses
                            #excluir_livro_por_status(numero do status que você quer excluir (1 para lido, 2 para lendo ou 3 para quero ler))
                            #exemplo excluir_livro_por_status(1)
                            #obs: essa função irá excluir todos os livros no status de leitura que você definir, no caso do exemplo exclui todos os livros com status de lido

excluir_livros_por_autor() #serve para excluir todos os livros de um autor, ele recebe o nome do autor entre os parenteses 
                           #excluir_livro_por_autor("nome do autor que vc quer excluir os livros")
                           #exemplo: excluir_livro_por_autor("Mauricio de Sousa")
                           #obs: essa função excluirá todos os livros relacionados ao autor que voce definir

excluir_todos_livros() #serve para excluir todos os dados do banco
                        #Se você chamar it's over zera tudo e o banco fica vazio sem nenhum dado




