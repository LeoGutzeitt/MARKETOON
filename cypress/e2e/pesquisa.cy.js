describe('Funcionalidade de Pesquisa de Produtos', () => {

  beforeEach(() => {
    cy.deletedatabase();
  });

  it('produto aparece ao pesquisar pelo nome completo', () => {
    cy.visit('/cadastro/');
    cy.get('#nome').type('Quadro Abstrato Azul');
    cy.get('#email').type('artista@exemplo.com');
    cy.get('#telefone').type('81999999999');
    cy.get('#descricao').type('Um quadro moderno.');
    cy.get('#preco').type('250');
    cy.get('#imagem').selectFile('media/produtos/lofiwall1.jpg');
    cy.get('button').click();
    cy.url().should('eq', 'http://127.0.0.1:8000/');

    cy.get('input[name="q"]').clear({ force: true }).type('Quadro Abstrato Azul{enter}', { force: true });
    cy.contains('Quadro Abstrato Azul').should('exist');
  });

  it('produto não aparece se pesquisar nome errado', () => {
    cy.visit('/cadastro/');
    cy.get('#nome').type('Pintura Solar');
    cy.get('#email').type('artista@solar.com');
    cy.get('#telefone').type('81999999999');
    cy.get('#descricao').type('Arte solar.');
    cy.get('#preco').type('300');
    cy.get('#imagem').selectFile('media/produtos/lofiwall1.jpg');
    cy.get('button').click();
    cy.url().should('eq', 'http://127.0.0.1:8000/');

    cy.get('input[name="q"]').clear({ force: true }).type('Luz da Lua{enter}', { force: true });
    cy.contains('Pintura Solar').should('not.exist');
    cy.contains('Nenhum produto encontrado').should('exist');
  });

  it('produto aparece se pesquisar parte do nome', () => {
    cy.visit('/cadastro/');
    cy.get('#nome').type('Escultura de Madeira');
    cy.get('#email').type('escultor@arte.com');
    cy.get('#telefone').type('81999999999');
    cy.get('#descricao').type('Peça artesanal.');
    cy.get('#preco').type('180');
    cy.get('#imagem').selectFile('media/produtos/lofiwall1.jpg');
    cy.get('button').click();
    cy.url().should('eq', 'http://127.0.0.1:8000/');

    cy.get('input[name="q"]').clear({ force: true }).type('Madeira{enter}', { force: true });
    cy.contains('Escultura de Madeira').should('exist');
  });
});

