# Projeto: Conversor XML para JSON Personalizado
## Descrição
Este projeto tem como objetivo converter arquivos XML em arquivos JSON formatados de forma personalizada, conforme as necessidades específicas da sua empresa. O JSON gerado é preparado para ser utilizado no Postman para inserir pedidos diretamente no sistema da empresa.

## Funcionalidades
Conversão de XML para JSON: Leitura de arquivos XML e conversão dos dados para JSON.
Formatação Personalizada: Adaptação do formato JSON conforme os requisitos específicos da empresa.
Preparação para Postman: Geração de arquivos JSON prontos para serem utilizados em requisições via Postman para inserção de pedidos.

## Tecnologias Utilizadas
* Linguagem de Programação:
    * Python

* Bibliotecas:

    * xmltodict (para processamento de XML)
    * json (para manipulação de JSON)
    * os (para manipulação de arquivos e diretórios)
    * Estrutura do Projeto
``` bash
/geradorJson
│
├── 1item.py                   # Script para converter XML com um item para JSON
├── 2+item.py                  # Script para converter XML com dois ou mais itens para JSON
└── README.md                  # Documentação do projeto
└── .gitignore                 # Arquivo .gitignore
``` 
## Instalação e Configuração

1. Clonar o Repositório:
``` bash
git clone https://github.com/seu-usuario/geradorJson.git
cd geradorJson
```

2.  Criar e Ativar um Ambiente Virtual:

``` bash
python -m venv venv
source venv/bin/activate   # No Windows, use `venv\Scripts\activate`
```
3. Instalar Dependências:

``` bash
pip install -r requirements.txt
```
4.  Executar o Script:

    * Para converter um XML com um item:

    ``` bash
    python 1item.py
    ```

    * Para converter um XML com dois ou mais itens:

    ``` bash
    python 2+item.py
    ```
## Contribuição
1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (git checkout -b feature/sua-feature)
3. Commit suas mudanças (git commit -m 'Adiciona nova feature')
4. Faça um Push para a Branch (git push origin feature/sua-feature)
5. Abra um Pull Request