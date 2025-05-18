# Casos de uso

## Gerenciar conta
### Ator: Usuário
#### Fluxo para criar conta:
1. Usuário acessa a tela de cadastro
2. Sistema solicita os dados obrigatórios para a criação da conta
3. Usuário preenche os dados e envia
4. Sistema valida os dados
5. Sistema cria a conta e exibe uma mensagem indicando que a operação foi bem sucedida
#### Fluxo para editar conta:
6. Usuário acessa a tela de edição de conta
7. Usuário modifica os campos que ele deseja
8. Sistema verifica se os novos dados são válidos
9. Sistema realiza as alterações e exibe uma mensagem indicando que a operação foi bem sucedida
#### Fluxo para excluir conta:
10. Usuário acessa a tela para exclusão da conta
11. Sistema pergunta se o usuário realmente deseja excluir a conta
12. Usuário clica em “SIM”
13. Sistema pede ao usuário para ele insira a senha da conta
14. Usuário insere a senha da conta
15. Sistema exclui a conta e exibe uma mensagem indicando que a operação foi bem sucedida
#### Extensões: 
- 4a. Se dados informados são inválidos, exibir erro e solicitar novos dados
- 8a. Se dados informados são inválidos, exibir erro e solicitar novos dados
- 12a. Se usuário clica em “NÃO”, sair da tela de exclusão de conta

## Efetuar login
### Ator: Usuário
#### Fluxo para efetuar login:
1. Usuário acessa a tela de login
2. Sistema pede ao usuário para inserir os dados “nome de usuário” e “senha”
3. Usuário preenche os dados e envia
4. Sistema verifica se o usuário existe e se a senha corresponde ao usuário
5. Sistema exibe a tela da conta
#### Extensões:
- 4a. Se o nome de usuário não existe, o sistema informa que o usuário não existe
- 4b. Se a senha não corresponde ao usuário, o sistema informa que a senha está incorreta

## Iniciar conversa
### Ator: Usuário
#### Fluxo para iniciar conversa:
1. Usuário acessa a tela de conversa
2. Usuário escolhe com quem deseja começar a conversa
3. Sistema abre a tela de conversa
4. Usuário escreve a mensagem e envia
5. A mensagem é exibida para o destinatário

## Visualizar progresso de um aluno
### Ator: Treinador
#### Fluxo normal:
1. Treinador acessa a tela progressos
2. Sistema exibe os alunos disponíveis para visualização
3. Treinador escolhe o aluno que deseja visualizar o progresso
4. Sistema exibe o progresso do aluno

## Gerenciar treino
### Ator: Treinador
#### Fluxo para criar treino:
1. Treinador acessa a tela para criar treino
2. Sistema exibe o formulário necessário para o novo treino
3. Treinador preenche o formulário(nome, descrição, etc.)
4. Sistema verifica se os dados são válidos
5. Sistema solicita os exercícios a serem adicionados
6. Treinador adiciona exercícios ao treino
7. Sistema cria o treino e exibe uma mensagem de sucesso
#### Fluxo para editar treino:
8. Treinador acessa a tela de editar treino
9. Sistema exibe treinos disponíveis para edição
10. Treinador seleciona treino que deseja editar
11. Sistema exibe os campos editáveis do treino selecionado
12. Treinador modifica os campos que ele deseja
13. Sistema verifica se os novos dados são válidos
14. Sistema realiza as alterações e exibe mensagem indicando que a operação foi bem sucedida
15. Sistema notifica os alunos atribuídos ao treino que ele foi modificado
#### Fluxo para excluir treino:
16. Treinador acessa a tela de excluir treino
17. Sistema pergunta se o Treinador realmente deseja excluir o treino
18. Treinador clica em “SIM”
19. Sistema exclui o treino e exibe uma mensagem de sucesso
#### Extensões:
- 4a. Se algum campo não for preenchido, o sistema exibe uma mensagem de erro, e solicita dados válidos
- 6a. Se nenhum exercício for selecionado, o sistema exibe uma mensagem de erro, e pede para que o treinador insira algum exercício

## Gerenciar vínculo de treino
### Ator: Treinador
#### Fluxo para adicionar vínculo:
1. Treinador acessa a tela dos alunos
2. Sistema exibe alunos disponíveis 
3. Treinador seleciona aluno
4. Sistema exibe treinos disponíveis para serem vinculados
5. Treinador seleciona treino
6. Sistema realiza uma confirmação da escolha
7. Sistema realiza o vínculo e exibe uma mensagem indicando que a operação foi bem sucedida
8. Sistema notifica aluno sobre a adição de vínculo no treino
#### Fluxo para remover vínculo:
9. Treinador acessa a tela dos alunos
10. Sistema exibe alunos disponíveis
11. Treinador seleciona aluno
12. Sistema exibe treinos disponíveis para serem desvinculados
13. Treinador seleciona treino
14. Sistema realiza uma confirmação da escolha
15. Sistema remove o vínculo e exibe uma mensagem indicando que a operação foi bem sucedida
#### Extensões: 
- 6a. Se treinador desistir de vincular treino ao aluno, sistema exibe treinos novamente
- 14a. Se treinador desistir de desvincular treino do aluno, sistema exibe treinos novamente

## Visualizar treino atribuído
### Ator: Aluno
#### Fluxo para visualizar:
1. Aluno acessa tela de treinos
2. Sistema exibe os treinos atribuídos ao aluno
3. Aluno seleciona o treino desejado
4. Sistema exibe os exercícios contidos no treino

## Gerenciar progresso
### Ator: Aluno
#### Fluxo para visualizar progresso:
1. Aluno acessa a tela gerenciar progresso
2. Sistema exibe as opções visualizar e marcar
3. Aluno seleciona visualizar
4. Sistema exibe um calendário com os dias do mês, com treinos feitos destacados
5. Aluno seleciona um dia específico
6. Sistema exibe detalhes do treino feito naquele dia
#### Fluxo para marcar progresso:
7. Aluno acessa a tela gerenciar progresso
8. Sistema exibe as opções visualizar e marcar
9. Aluno seleciona marcar
10. Sistema altera a opção para “marcado”
