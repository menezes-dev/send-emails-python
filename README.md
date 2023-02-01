# send-emails-python

Aplicação desenvolvida em python para automatizar o envio de emails e sms automáticos a partir de uma lista de dicionários, contendo as informações dos destinatários.

## Instalação

Primeiro, escolha um diretório local e inicie um repositório git como o seguinte comando: `git init`

Após isso, faça o clone do repositório: `git clone git@github.com:menezes-dev/send-emails-python.git`

Em seguida, no repositório atual, crie um ambiente virtual, para instalar as dependências da aplicação: `python -m venv venv`

Agora, entre no ambiente virtual criado como o comando: `.\venv\Scripts\activate`

Uma vez no ambiente virtual, instale as dependências do projeto: `pip install -r requirements.txt`

## Instruções

Após o ambiente configurado, renomeie o arquivo `.env.example` para `.env` e complete-o com as suas informações de conexão.

Faça o mesmo com o `receivers.py.example` para `receivers.py`. Nesse arquivo, você deverá preencher a lista com dicionários contendo as informações dos destinatários, nesse formato

```json
{ "name": "nome do destinatário", "email": "email do destinatário", "number": 00000000000 }
```

Para o envio dos SMS's, é utilizada a api [SMSDev](https://www.smsdev.com.br/envio-sms/).

## Execução

Após configurar o ambiente e suas varáveis, rode o comando `python app.py` e os Email's e SMS's serão enviados automaticamente. Note que dependendo do tamanho da sua lista, pode haver um delay.
