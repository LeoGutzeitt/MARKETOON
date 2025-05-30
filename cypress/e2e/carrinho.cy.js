Cypress.Commands.add('deletedatabase', () => {
  cy.exec('python delete_database.py', { failOnNonZeroExit: false });
});

describe('Fluxo: cadastrar produto e adicionar ao carrinho', () => {

  before(() => {
    cy.deletedatabase();
  });

  it('deve cadastrar um produto, adicionar ao carrinho e visualizar no carrinho', () => {
    cy.visit('/cadastro/');
    cy.get('#nome').type('Teste carrinho');
    cy.get('#email').type('teste@email.com');
    cy.get('#telefone').type('81999999999');
    cy.get('#descricao').type('Descrição do produto');
    cy.get('#preco').type('150');
    cy.get('#imagem').selectFile('media/produtos/lofiwall1.jpg');
    cy.get('button').click();
    cy.url().should('eq', 'http://127.0.0.1:8000/');
    cy.contains('Teste carrinho')
      .parent() 
      .find('button.cart-button') 
      .click();
    cy.url().should('include', '/carrinho');
    cy.get('.carrinho-container').should('contain', 'Teste carrinho');

  });

});




