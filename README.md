<h1 align="center">
<br />
<img src="./app/static/img/icon.jpg" height="100">
<br />
<br />
CVI
</h1>

<p>CVI é o acrônimo de Controle de Visitas Imobiliárias. Trata-se de um trabalho acadêmico desenvolvido nas seguintes matérias: Tópicos Avançados em Análise e Desenvolvimento de Sistemas (professor Wanderson Pereira dos Santos) e Modelagem de Software Orientado a Objetos (professor Leomar Camargo de Souza). Dentre as funcionalidades da aplicação podemos citar:
<ul>
    <li>Login</li>
    <li>Envio de emails</li>
    <li>Manter corretores</li>
    <li>Manter imóveis</li>
    <li>Manter visitas</li>
</ul>
</p>

<br />
<div align="center">
<img src="https://lh3.googleusercontent.com/L3FbSQYbVWN-KxgWx8FxlIdQbwzAcRQutRsXzPHZooRUlPrfrAxjnYQtiGtTuPHKvY2OiO5azEvav98tTC-bFm0VOW4UngtXLubsPAUiWDTPaxH28ogXO7AMWw5uUFAQv0pMu10hKri0sdrxU8_m7E0p_I_44zzHRVEIsQCJvRFyiIYayPFeOkGL0UEDQdC12Z_rZHqYxOYna3Vp9o-wjr3dw-tF3gYipTelM-ii8LHQ_3pD-0JBcC5OMN71qyueC0Q6wU8lBKGnY-xncJ6A3aMKc64kruQUuAXrRwnrJQdXBKCt_h7A4Egr2FYWIRl-0JvvGtVXUJBjTD5Q3VR33pT0xOWUjZC3xV9db0CLLHmpestg4VT9a-ZtyvIzPz99_sLmPXC2ElEovY28yccsjVMZMopExkk1rIH0RbL0JgB64vh80dHnKzDWvYyEQH9myMD3nZmHnxHFGtVACr83HMc5YcFLi71tNNhiyYO2OqXrQR_78LhBVg8fNs8lG2IGXMq1PQW2emp9CCmbEZP0st5zf2IN94XWBRTpEbZ7iY5hqQUKpNWKxYy2k9R_vW0Heo5UcHhK2asbijHqqNE8m4M6bdKBG3Y6K3iTKNmfbSoOWUA1Z5WnRNe1KuYKYIhkwmVIph1xvLwPKe0pR2z-WC4eLr6Ru4yWKNxEk9pXqU5jngoWmC7a6LnDjtSy=w742-h362-no?authuser=0" height="250" width="500">
</div>

<br />
<br />

<hr />

<br />
<br />

## 🚀 Tecnologias

Essas foram as tecnologias utilizadas para desenvolver a aplicação:

- ✔️ Python

- ✔️ Flask

- ✔️ Flask SQLAlchemy (ORM)

- ✔️ JavaScript

- ✔️ MySQL

<br />
<br />

<hr />

<br />
<br />

## ⚙️ Configurando a aplicação
Alguns passos para configurar e rodar a aplicação no seu computador.

<br />

<h3>1º passo:</h3>
<span>Crie o banco. O arquivo com o banco está localizado no seguinte caminho.</span>

<br/>
<br/>

> /datase/db.sql

<br/>

<h3>2º passo:</h3>
<span>Acesse o arquivo abaixo e coloque e altere a linha 10 de acordo com as configurações do seu banco de dados</span>

<br/>
<br/>

> /app/__init_ _.py

<br/>

<h3>3º passo:</h3>
<span>Crie o arquivo de configuração no seguinte caminho.</span>

<br/>
<br/>

> /app/config.json

<br />
Conteúdo do arquivo
<br />
<br />

```
{
    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_PORT": 465,
    "MAIL_USERNAME": "email_robo@gmail.com",
    "MAIL_PASSWORD": "sua_senha",
    "MAIL_USE_TLS": false,
    "MAIL_USE_SSL": true
}
```

<br/>

<h3>4º passo:</h3>
<span>Crie os diretórios abaixo.</span>

<br/>
<br/>

> /app/static/uploads/capas

> /app/static/uploads/docs

> /app/static/uploads/fotos_interior

<br/>

<h3>5º passo:</h3>
<span>Acesse o arquivo abaixo, descomente da linha 34 até a linha 47 e coloque as informações de login da sua conta.</span>

<br/>
<br/>

> /app/controllers/login.py

<br />

<h3>6º passo:</h3>
<span>Abra o terminal, acesse a raiz do projeto e execute os comandos abaixo. (instale o pipenv antes caso ainda não tenha)</span>
<br/>
<br/>

```
pipenv shell
python .\main.py
```

<br>

<h3>7º passo:</h3>
<span>Acesse a rota abaixo</span>
<br/>
<br/>

```
http://localhost:5000/login/criar-usuario
```

<br>