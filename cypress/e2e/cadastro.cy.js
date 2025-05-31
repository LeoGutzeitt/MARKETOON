Cypress.Commands.add('deletedatabase', () => {
  cy.exec('python delete_database.py', { failOnNonZeroExit: false });
});

describe('Como artista, gostaria de poder lançar meus produtos na plataforma', () => {

    before(() => {
    cy.deletedatabase(); 
    });

    it('cadastro de produto com sucesso', () => {
        cy.visit('/cadastro/');
        cy.get('#nome').type('nada importante');
        cy.get('#email').type('nadaimportante@semail.com');
        cy.get('#telefone').type('81999999999');
        cy.get('#descricao').type('nada importante');
        cy.get('#preco').type('120');
        cy.get('#imagem').selectFile('media/produtos/lofiwall1.jpg');
        cy.get('button').click();
        cy.url().should('eq', 'http://127.0.0.1:8000/');
        cy.contains('nada importante').should('exist');
    });

    it('erro ao tentar cadastrar sem nome', () => {
        cy.visit('/cadastro/');
        cy.get('#email').type('nadaimportante@semail.com');
        cy.get('#telefone').type('81999999999');
        cy.get('#descricao').type('nada importante');
        cy.get('#preco').type('120');
        cy.get('#imagem').selectFile('media/produtos/lofiwall1.jpg');
        cy.get('button').click();
        cy.url().should('eq', 'http://127.0.0.1:8000/cadastro/');
        cy.focused().should('have.attr', 'id', 'nome');
    });

    it('erro ao tentar cadastrar sem email', () => {
        cy.visit('/cadastro/');
        cy.get('#nome').type('nada importante');
        cy.get('#telefone').type('81999999999');
        cy.get('#descricao').type('nada importante');
        cy.get('#preco').type('120');
        cy.get('#imagem').selectFile('media/produtos/lofiwall1.jpg');
        cy.get('button').click();
        cy.url().should('eq', 'http://127.0.0.1:8000/cadastro/');
        cy.focused().should('have.attr', 'id', 'email');
    });
});
