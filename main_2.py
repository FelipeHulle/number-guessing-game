# Usar essa separação de Classes e responsabilidades como base pra construir o novo código

# | Class             | Responsability                                                                 |
# | ----------------- | ------------------------------------------------------------------------------ |
# | GameEngine        | Orquestra o jogo; controla o fluxo principal.                                  |
# | PlayerInterface   | Responsável pela interação com o usuário (input/output).                       |
# | Difficulty        | Representa os níveis de dificuldade e suas regras.                             |
# | Round             | Representa uma única rodada do jogo (lógica de adivinhação, tempo, resultado). |
# | HintSystem        | Lógica de dicas, acoplada de forma opcional à rodada.                          |
