# 🛠️ Contribuindo com o MARKETOON

👋 **Bem-vindo(a)!**

Se você chegou até aqui, é provável que tenha interesse em contribuir com o **MARKETOON**, uma aplicação web desenvolvida em **Django**, criada para auxiliar um artista, que queira anunciar a venda do seu TOON (produto) e, assim, intermediar a compra do cliente com o vendedor.

Antes de começar a colaborar, leia este guia para entender como o projeto funciona e como você pode contribuir de forma efetiva.

---

## ✅ Como Contribuir

Você pode:

- Desenvolver novas funcionalidades  
- Corrigir bugs ou issues abertas (confira a aba **Issues** do repositório)  
- Sugerir melhorias no código, layout ou experiência do usuário  
- Ajudar na documentação ou testes automatizados  

---

## 📁 Configurando o Repositório

### 1️⃣ Fork

Clique em **Fork** no canto superior direito da página do repositório para criar uma cópia dele na sua conta GitHub.

### 2️⃣ Clone o repositório forkado

```bash
git clone https://github.com/SeuUsuario/MARKETOON.git
cd MARKETOON
```

### 3️⃣ Crie uma branch para suas alterações

```bash
git checkout -b minha-nova-funcionalidade
```

---

## 💻 Configurando o Ambiente de Desenvolvimento

### 1. Crie um ambiente virtual

```bash
python -m venv venv
```

### 2. Ative o ambiente virtual

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

### 3. Instale as dependências do Python

```bash
pip install -r requirements.txt
```

### 4. Aplique as migrações do banco de dados

```bash
python manage.py migrate
```

### 5. Rode o servidor local

```bash
python manage.py runserver
```

---

## 🧪 Executando os Testes

Caso você altere partes críticas do sistema, recomendamos rodar os testes automatizados para garantir que tudo continua funcionando.

### 1. Instale o Node.js (versão LTS)

https://nodejs.org/

### 2. Instale as dependências do frontend

```bash
npm ci
```

### 3. Rode os testes com Cypress

```bash
npx cypress run
```

---

## 📤 Submetendo sua Contribuição

Depois de terminar suas alterações:

### 1. Faça commit e envie para o seu fork

```bash
git add .
git commit -m "feat: breve descrição da alteração"
git push origin minha-nova-funcionalidade
```

### 2. Crie um Pull Request

- Vá até o seu repositório no GitHub  
- Clique em **Compare & pull request**  
- Escreva uma descrição clara do que você alterou e o motivo  
- Clique em **Create pull request**  

---

## 🔎 Revisão do Código

A equipe do projeto irá revisar seu PR. Se algo não estiver em conformidade com o projeto, entraremos em contato para que você possa ajustar seu código.

---

## 🙏 Agradecimentos

A equipe do **MARKETOON** agradece imensamente sua contribuição!  

Cada sugestão, melhoria e correção faz uma grande diferença para tornar nossa aplicação mais robusta, acessível e eficiente para todos os usuários.

Estamos animados para ver suas ideias em ação e trabalharmos juntos para transformar a experiência de marketing digital.

---

## 👥 Contato dos Mantenedores


- [Leo Gutzeitt](https://github.com/LeoGutzeitt)
- [Gabriel Victalino](https://github.com/GabrielVictalino)
- [Julia Ferreira](https://github.com/juliavfe)
- [Dávila Peixoto](https://github.com/davilapeixoto)
- [Aline Takakura](https://github.com/alinetakakura)
- [Lívia Almeida](https://github.com/liv553)

Se tiver qualquer dúvida, fique à vontade para abrir uma **Issue** ou entrar em contato com os responsáveis.

---
