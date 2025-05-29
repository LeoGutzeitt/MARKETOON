Cypress.Commands.add('deletedatabase', () => {
    cy.exec('python delete_database.py', { failOnNonZeroExit: false })
});

describe ('como usuário gostaria de adicionar meus itens ao carrinho', () => {
    it('adicionando ao carrinho', () => {
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
        cy.get('[href="/carrinho/"] > button').click();
        
        

       // cy.url().should('eq', 'http://127.0.0.1:8000/');
       // cy.contains('nada importante').should('exist');
})
//it('carrinho vazio', () => {
  //  cy.visit('/');
    //cy.get('[href="/carrinho/"] > button').click();


    

   // cy.url().should('eq', 'http://127.0.0.1:8000/');
   // cy.contains('nada importante').should('exist');
})
    


