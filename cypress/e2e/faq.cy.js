Cypress.Commands.add('deletedatabase', () => {
    cy.exec('python delete_database.py', { failOnNonZeroExit: false })
});

describe ('Como usuário/artista gostaria de ter acesso ao FAQ/suporte no "marketoon', () => {
    it('indo ao faq e visualizar as principais duvidas', () => {
        cy.visit('/');
        cy.get('.support-button').click();
        cy.get(':nth-child(2) > h2').click();
        cy.get(':nth-child(3) > h2').click();
        cy.get(':nth-child(4) > h2').click();
        cy.get(':nth-child(5) > h2').click();
})

})