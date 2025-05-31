Cypress.Commands.add('deletedatabase', () => {
  cy.exec('python delete_database.py', { failOnNonZeroExit: false });
});

describe('Fluxo: cadastrar produto e adicionar na wishlist', () => {

  before(() => {
    cy.deletedatabase();
  });

  it('deve cadastrar um produto, adicionar na wishlist e visualizar na página wishlist', () => {
    cy.visit('/cadastro/');
    cy.get('#nome').type('teste lista desejos');
    cy.get('#email').type('testelista@email.com');
    cy.get('#telefone').type('82999999999');
    cy.get('#descricao').type('Descrição do produto para wishlist');
    cy.get('#preco').type('100');
    cy.get('#imagem').selectFile('media/produtos/lofiwall1.jpg');
    cy.get('button[type="submit"]').click(); 

    cy.url().should('eq', 'http://127.0.0.1:8000/');

    cy.contains('.product-card strong', 'teste lista desejos')
      .parents('.product-card')
      .find('button.wishlist-add-btn')
      .click();

    cy.visit('/wishlist/');

    cy.url().should('include', '/wishlist/');

    cy.contains('teste lista desejos').should('exist');
  });

});
