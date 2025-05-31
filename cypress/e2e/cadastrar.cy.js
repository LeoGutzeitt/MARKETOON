describe('Fluxo de Cadastro', () => {
  beforeEach(() => {
    cy.visit('/cadastro');
  });

  it('Deve exibir o formulário de cadastro corretamente', () => {
    cy.get('form').within(() => {
      cy.get('input[name="email"]').should('exist');
      cy.get('input[name="username"]').should('exist');
      cy.get('input[name="password1"]').should('exist');
      cy.get('input[name="password2"]').should('exist');
      cy.get('button[type="submit"]').should('contain', 'Finalizar');
    });
  });

  it('Não deve permitir cadastro com campos vazios', () => {
    cy.get('button[type="submit"]').click();
    cy.contains('Este campo é obrigatório').should('exist'); 
  });

  it('Não deve permitir cadastro com email inválido', () => {
    cy.get('input[name="email"]').type('email-invalido');
    cy.get('input[name="username"]').type('usuarioTeste');
    cy.get('input[name="password1"]').type('senha12345');
    cy.get('input[name="password2"]').type('senha12345');
    cy.get('button[type="submit"]').click();

    cy.contains('Informe um email válido').should('exist'); 
  });

  it('Não deve permitir cadastro se as senhas não conferirem', () => {
    cy.get('input[name="email"]').type('usuario@exemplo.com');
    cy.get('input[name="username"]').type('usuarioTeste');
    cy.get('input[name="password1"]').type('senha12345');
    cy.get('input[name="password2"]').type('senhaErrada');
    cy.get('button[type="submit"]').click();

    cy.contains('As senhas não conferem').should('exist'); 
  });

  it('Deve cadastrar novo usuário com dados válidos', () => {
    const email = `usuario${Date.now()}@exemplo.com`; 

    cy.get('input[name="email"]').type(email);
    cy.get('input[name="username"]').type('usuarioTeste');
    cy.get('input[name="password1"]').type('senha12345');
    cy.get('input[name="password2"]').type('senha12345');
    cy.get('button[type="submit"]').click();

    cy.url().should('eq', Cypress.config().baseUrl + '/dashboard'); 
    cy.contains('Bem-vindo').should('exist');
  });
});
