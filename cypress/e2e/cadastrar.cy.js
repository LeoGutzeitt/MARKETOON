describe('Fluxo de Cadastro', () => {
  beforeEach(() => {
    cy.visit('/cadastrar');
  });

  it('Deve exibir o formulário de cadastro corretamente', () => {
    cy.get('form').within(() => {
      cy.get('input[name="email"]').should('exist').and('be.visible');
      cy.get('input[name="username"]').should('exist').and('be.visible');
      cy.get('input[name="password1"]').should('exist').and('be.visible');
      cy.get('input[name="password2"]').should('exist').and('be.visible');
      cy.get('button[type="submit"]').should('contain.text', 'Finalizar').and('be.visible');
    });
  });

  it('Não deve permitir cadastro com campos vazios', () => {
  cy.get('form').within(() => {
    cy.get('button[type="submit"]').click();
    
    cy.get('input[name="email"]').then($input => {
      expect($input[0].validationMessage).to.eq('Preencha este campo.');
      expect($input[0].checkValidity()).to.be.false;
    });
  });
});

  it('Não deve permitir cadastro com email inválido', () => {
  cy.get('form').within(() => {
    cy.get('input[name="email"]').type('abc');
    cy.get('input[name="username"]').type('usuarioTeste');
    cy.get('input[name="password1"]').type('senha12345');
    cy.get('input[name="password2"]').type('senha12345');
    cy.get('button[type="submit"]').click();

    cy.get('input[name="email"]').then($input => {
      expect($input[0].validationMessage).to.match(/inclua um "@"/i);
      expect($input[0].checkValidity()).to.be.false;
    });
  });
});

  it('Não deve permitir cadastro se as senhas não conferirem', () => {
    cy.get('form').within(() => {
      cy.get('input[name="email"]').type('usuario@exemplo.com');
      cy.get('input[name="username"]').type('usuarioTeste');
      cy.get('input[name="password1"]').type('senha12345');
      cy.get('input[name="password2"]').type('senhaErrada');
      cy.get('button[type="submit"]').click();
    });

    cy.contains(/As senhas não coincidem./i).should('be.visible');
  });

it('Deve cadastrar novo usuário com dados válidos', () => {
  const email = `usuario${Date.now()}@exemplo.com`;

  cy.get('form').within(() => {
    cy.get('input[name="email"]').type(email);
    cy.get('input[name="username"]').type('usuarioTeste23');
    cy.get('input[name="password1"]').type('senha1234565');
    cy.get('input[name="password2"]').type('senha1234565');
    cy.get('button[type="submit"]').click();
  });

  cy.url().should('include', '/login');

  cy.contains(/Conta criada com sucesso\. Faça login\./i).should('be.visible');
});
});

