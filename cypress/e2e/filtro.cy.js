describe('Filtro por preço na home', () => {
  it('cadastra produto e filtra pelo preço', () => {
    cy.visit('/cadastro/');
    cy.get('#nome').type('teste filtro');
    cy.get('#email').type('nadaimportante@semail.com');
    cy.get('#telefone').type('81999999999');
    cy.get('#descricao').type('nada importante');
    cy.get('#preco').type('120');
    cy.get('#imagem').selectFile('media/produtos/lofiwall1.jpg');
    cy.get('button').click();
    cy.url().should('eq', 'http://127.0.0.1:8000/');
    cy.get('input[name="preco_max"]').invoke('val', 150).trigger('input');
    cy.contains('Filtrar').click();
    cy.contains('teste filtro').should('exist');
  });
});

