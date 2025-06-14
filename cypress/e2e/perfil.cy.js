Cypress.Commands.add('deletedatabase', () => {
  cy.exec('python delete_database.py', { failOnNonZeroExit: false });
});

describe('Página de Perfil', () => {
  beforeEach(() => {
    cy.deletedatabase();
  });

  function cadastrarUsuario(email, username, senha) {
    cy.visit('/cadastrar/');
    cy.get('input[name="email"]').type(email);
    cy.get('input[name="username"]').type(username);
    cy.get('input[name="password1"]').type(senha);
    cy.get('input[name="password2"]').type(senha);
    cy.get('form').submit();
    cy.url().should('include', '/login');
  }

  function loginUsuario(username, senha) {
    cy.visit('/login/');
    cy.get('input[name="username"]').type(username);
    cy.get('input[name="password"]').type(senha);
    cy.get('form').submit();
  }

  it('Você pode se cadastrar e acessar a página de perfil', () => {
    const email = 'joao2@email.com';
    const username = 'joaouser1';  
    const senha = 'T3st3$egur0!A1';

    cadastrarUsuario(email, username, senha);

    loginUsuario(username, senha);

    cy.visit('/perfil/', { failOnStatusCode: false });
    cy.contains('Usuário').should('exist');
  });

  it('Você pode fazer login e acessar o perfil', () => {
    const email = 'usuario2@email.com';
    const username = 'usuario2';
    const senha = 'P@ssw0rd$2025';

    cadastrarUsuario(email, username, senha);
    loginUsuario(username, senha);

    cy.visit('/perfil/', { failOnStatusCode: false });
    cy.contains('Usuário').should('exist');
  });

  it('Você pode editar o campo nome', () => {
    const email = 'usuario3@email.com';
    const username = 'usuario3';
    const senha = 'S3nh@F0rt3#123';

    cadastrarUsuario(email, username, senha);
    loginUsuario(username, senha);

    cy.visit('/perfil/', { failOnStatusCode: false });
    cy.get('input[name="name"]').should('exist').and('be.visible');

    cy.get('input[name="name"]').clear().type('Ana Maria');
    cy.get('button.btn-salvar[type="submit"]').click();

    cy.reload();
    cy.get('input[name="name"]').should('have.value', 'Ana Maria');
  });

  it('Você pode ativar e desativar o modo vendedor e ver botão', () => {
    const email = 'usuario4@email.com';
    const username = 'usuario4';
    const senha = 'F0rt3!Senha@456';

    cadastrarUsuario(email, username, senha);
    loginUsuario(username, senha);

    cy.visit('/perfil/', { failOnStatusCode: false });
    cy.get('#toggle-vendedor').check({ force: true });
    cy.get('form').submit();

    cy.reload();
    cy.get('button[type="submit"]').should('exist');

    cy.get('#toggle-vendedor').uncheck({ force: true });
    cy.get('form').submit();

    cy.reload();
    cy.get('button[type="submit"]').should('exist');
  });

  it('Botão "Cadastrar Arte" aparece ao ativar modo vendedor e permite cadastrar produto', () => {
    const email = 'vendedor@email.com';
    const username = 'vendendorUser';
    const senha = 'V3nd3dor#Segur0!';

    cadastrarUsuario(email, username, senha);
    loginUsuario(username, senha);

    cy.visit('/perfil/', { failOnStatusCode: false });

    cy.get('#toggle-vendedor').check({ force: true });
    cy.get('form').submit();

    cy.reload();

    cy.get('#btnCadastrarArte').should('be.visible').click();

    cy.url().should('include', '/cadastro');

    cy.get('#nome').type('nada importante');
    cy.get('#email').type('nadaimportante@semail.com');
    cy.get('#telefone').type('81999999999');
    cy.get('#descricao').type('nada importante');
    cy.get('#preco').type('120');
    cy.get('#imagem').selectFile('media/produtos/lofiwall1.jpg', { force: true });
    cy.get('button[type="submit"]').click();

    cy.url().should('eq', 'http://127.0.0.1:8000/');
    cy.contains('nada importante').should('exist');
  });

  it('Campos do perfil mostram os dados atuais', () => {
    const email = 'abc@email.com';
    const username = 'abc';
    const senha = 'S3nh@F0rt3!789';

    cadastrarUsuario(email, username, senha);

    loginUsuario(username, senha);

    cy.visit('/perfil/', { failOnStatusCode: false });
    cy.contains('Usuário').should('exist');

    cy.get('input[name="email"]').should('have.value', email);
    cy.get('input[name="name"]').should('exist');
    cy.get('input[name="cpf"]').should('exist');
    cy.get('input[name="telefone"]').should('exist');
  });
});
