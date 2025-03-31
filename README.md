# BetterFlights

Uma breve descrição sobre o que esse projeto faz e para quem ele é


## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/YanSardinha/BetterFlights.git
```

Entre no diretório do projeto

```bash
  cd BetterFlights
```

Instale o poetry, uma ferramenta para gerenciamento de dependências

```bash
  pip install poetry
```

Instale as dependências

```bash
  poetry install --no-root
```

# Contribuindo para BetterFlights

Obrigado por considerar contribuir para o projeto **BetterFlights**! A seguir, estão algumas diretrizes para garantir que o processo de contribuição seja suave e eficiente para todos.

## Como Contribuir

1. **Submeter um Pull Request**
   - Fork o repositório e clone-o para sua máquina local.
   - Crie uma nova branch para sua alteração: 
     ```bash
     git checkout -b nome-da-sua-branch
     ```
   - Realize suas alterações.
   - Certifique-se de que o código está formatado corretamente e de acordo com as convenções do projeto. Use `ruff` ou outra ferramenta de formatação para garantir a consistência do estilo de código:
     ```bash
     poetry run task ruff
     ```
   - Adicione testes, se possível, para verificar se a funcionalidade que você adicionou ou corrigiu está funcionando corretamente.
   - Certifique-se de que todos os testes existentes estão passando. Você pode rodar os testes utilizando o `pytest`:
     ```bash
     poetry run task test
     ```
   - Após revisar suas alterações, submeta um pull request detalhado explicando o que foi feito.

## Regras Básicas

- **Siga as convenções de estilo do Python** (PEP 8).
- **Não faça alterações que não estejam diretamente relacionadas ao problema ou melhoria**.
- **Escreva mensagens de commit claras e descritivas**, explicando o que foi alterado e por quê.
- **Evite fazer commits de código não relacionado**, isso facilita a revisão e o acompanhamento das mudanças.
- **Adicione testes para novas funcionalidades** sempre que possível.
- **Mantenha a compatibilidade com a versão atual do Python** que o projeto está utilizando (verifique o arquivo `pyproject.toml`, `requirements.txt` ou a documentação do projeto).
  
## Licença

Por favor, leia o arquivo [LICENSE](LICENSE) para entender os termos sob os quais o código está licenciado.

## Código de Conduta

Este projeto adere ao nosso [Código de Conduta](CODE_OF_CONDUCT.md). Ao contribuir, você concorda em seguir esse código.

---

Agradecemos pelo seu interesse em contribuir para o **BetterFlights**! Toda contribuição, grande ou pequena, é muito apreciada.

## Autores

- [@YanSardinha](https://www.github.com/yansardinha)


## Licença

[MIT](https://choosealicense.com/licenses/mit/)


## Instalação

Instale my-project com npm

```bash
  npm install my-project
  cd my-project
```
    