Cypress.Commands.add('deletedatabase', () => {
    cy.exec('python delete_database.py', { failOnNonZeroExit: false })
});

describe ('Como artista gostaria de poder lançar meus produtos na plataforma', () => {
    it('cadastrando produto', () => {
        cy.visit('/');
        cy.deletedatabase();
        cy.get('[href="/cadastro/"] > button').click();
        cy.get('#nome').type('nada importante');
        cy.get('#email').type('nadaimportante@semail.com');
        cy.get('#telefone').type('81999999999');
        cy.get('#descricao').type('nada importante');
        cy.get('#preco').type('120');
        cy.get('#imagem').selectFile('media/produtos/lofiwall1.jpg');
        cy.get('button').click();

        cy.get('a[href="/compra/45"]').click();


        //cy.url().should('eq', 'http://127.0.0.1:8000/');
       //cy.contains('nada importante').should('exist');
})
// it('cadastro de produto dando errado(sem nome e email)', () => {
//     cy.visit('/');
//     cy.deletedatabase();
//     cy.get('[href="/cadastro/"] > button').click();
//     cy.get('#nome')
//     cy.get('#email');
//     cy.get('#telefone').type('81999999999');
//     cy.get('#descricao').type('nada importante');
//     cy.get('#preco').type('120');
//     cy.get('#imagem').selectFile('media/produtos/lofiwall1.jpg');
//     cy.get('button').click()

//     cy.url().should('eq', 'http://127.0.0.1:8000/cadastro/');
//     cy.focused().should('have.attr', 'id', 'nome');
// })

 })