describe('Página de Perfil', () => {
  beforeEach(() => {
    cy.exec('python delete_database.py', { failOnNonZeroExit: false });
  });

  it('Você pode se cadastrar e acessar a página de perfil', () => {
    cy.visit('/cadastrar/');
    cy.get('input[name="email"]').type('joao2@email.com');
    cy.get('input[name="username"]').type('joaouser1');  
    cy.get('input[name="password1"]').type('teste12342');
    cy.get('input[name="password2"]').type('teste12342');
    cy.get('form').submit();

    cy.url().should('include', '/login');

    cy.get('input[name="username"]').type('joaouser1');
    cy.get('input[name="password"]').type('teste12342');
    cy.get('form').submit();

    cy.visit('/perfil/', { failOnStatusCode: false });
    cy.contains('Usuário').should('exist');
  });

  it('Você pode fazer login e acessar o perfil', () => {
    cy.visit('/cadastrar/');
    cy.get('input[name="email"]').type('usuario_teste@email.com');
    cy.get('input[name="username"]').type('usuarioteste2');
    cy.get('input[name="password1"]').type('senha1232');
    cy.get('input[name="password2"]').type('senha1232');
    cy.get('form').submit();

    cy.visit('/login/');
    cy.get('input[name="username"]').type('usuarioteste2');
    cy.get('input[name="password"]').type('senha1232');
    cy.get('form').submit();

    cy.visit('/perfil/', { failOnStatusCode: false });
    cy.contains('Usuário').should('exist');
  });

  it('Você pode editar os campos de perfil', () => {
    cy.visit('/login/');
    cy.get('input[name="username"]').type('usuarioteste2');
    cy.get('input[name="password"]').type('senha1232');
    cy.get('form').submit();

    cy.visit('/perfil/', { failOnStatusCode: false });

    cy.get('input[name="name"]').should('exist').and('be.visible');

    cy.get('input[name="name"]').clear().type('Ana Maria');
    cy.get('input[name="cpf"]').clear().type('12345678901');
    cy.get('input[name="telefone"]').clear().type('11999999999');
    cy.get('form').submit();

    cy.contains('Perfil atualizado').should('exist');

    cy.reload();
    cy.get('input[name="name"]').should('have.value', 'Ana Maria');
    cy.get('input[name="cpf"]').should('have.value', '12345678901');
    cy.get('input[name="telefone"]').should('have.value', '11999999999');
  });
  it('Você pode ativar e desativar o modo vendedor e ver botão', () => {
    cy.visit('/login/');
    cy.get('input[name="username"]').type('usuarioteste');
    cy.get('input[name="password"]').type('senha123');
    cy.get('form').submit();

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

  it('Campos do perfil mostram os dados atuais', () => {
    cy.visit('/login/');
    cy.get('input[name="username"]').type('usuarioteste');
    cy.get('input[name="password"]').type('senha123');
    cy.get('form').submit();

    cy.visit('/perfil/', { failOnStatusCode: false });
    cy.get('input[name="email"]').should('have.value', 'usuario_teste@email.com');
    cy.get('input[name="name"]').should('exist');
    cy.get('input[name="cpf"]').should('exist');
    cy.get('input[name="telefone"]').should('exist');
  });
});



