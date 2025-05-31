Cypress.Commands.add('deletedatabase', () => {
    cy.exec('python delete_database.py', { failOnNonZeroExit: false });
});

describe('Fluxo de Login', () => {
  before(() => {
    cy.deletedatabase();  
  });
  before(() => {
    cy.visit('/cadastrar');

    cy.get('input[name="email"]').type('usuario@exemplo.com');
    cy.get('input[name="username"]').type('usuario_valido');
    cy.get('input[name="password1"]').type('senha_correta');
    cy.get('input[name="password2"]').type('senha_correta');
    cy.get('button[type="submit"]').click();

    cy.url().should('include', '/login');
  });

  beforeEach(() => {
    cy.visit('/login');
    cy.contains('Sign in');
  });

  it('Deve exibir o formulário de login corretamente', () => {
    cy.get('form').within(() => {
      cy.get('input[name="username"]').should('exist');
      cy.get('input[name="password"]').should('exist');
      cy.get('button[type="submit"]').should('contain.text', 'Sign in');
    });
  });

  it('Não deve permitir login com campos vazios', () => {
    cy.get('button[type="submit"]').click();
    cy.get('.error-message')
      .should('exist')
      .and('contain.text', 'Usuário ou senha inválidos');
  });

  it('Não deve permitir login com credenciais inválidas', () => {
    cy.get('input[name="username"]').type('usuario_invalido');
    cy.get('input[name="password"]').type('senhaerrada');
    cy.get('button[type="submit"]').click();

    cy.get('.error-message')
      .should('exist')
      .and('contain.text', 'Usuário ou senha inválidos');
  });

  it('Deve logar com credenciais válidas', () => {
    cy.get('input[name="username"]').type('usuario_valido');
    cy.get('input[name="password"]').type('senha_correta');
    cy.get('button[type="submit"]').click();

    cy.url().should('eq', 'http://127.0.0.1:8000/');
    cy.contains('Olá, usuario_valido').should('exist');
  });
});

