Cypress.Commands.add('deletedatabase', () => {
    cy.exec('python delete_database.py', { failOnNonZeroExit: false });
});

describe('Como artista, gostaria de poder lançar meus produtos na plataforma', () => {

    beforeEach(() => {
        cy.deletedatabase();
    });

    describe('Filtro por preço na home', () => {

        it('cadastra produto e filtra pelo preço corretamente', () => {
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

        it('produto não aparece quando filtro de preço é menor que o valor', () => {
            cy.visit('/cadastro/');
            cy.get('#nome').type('produto caro');
            cy.get('#email').type('caro@teste.com');
            cy.get('#telefone').type('81988888888');
            cy.get('#descricao').type('produto acima do limite');
            cy.get('#preco').type('500');
            cy.get('#imagem').selectFile('media/produtos/lofiwall1.jpg');
            cy.get('button').click();
            cy.url().should('eq', 'http://127.0.0.1:8000/');
            cy.get('input[name="preco_max"]').invoke('val', 300).trigger('input');
            cy.contains('Filtrar').click();
            cy.contains('produto caro').should('not.exist');
        });

        it('produto aparece quando filtro é exatamente igual ao preço', () => {
            cy.visit('/cadastro/');
            cy.get('#nome').type('preco igual');
            cy.get('#email').type('igual@teste.com');
            cy.get('#telefone').type('81977777777');
            cy.get('#descricao').type('produto com preco igual ao filtro');
            cy.get('#preco').type('250');
            cy.get('#imagem').selectFile('media/produtos/lofiwall1.jpg');
            cy.get('button').click();
            cy.url().should('eq', 'http://127.0.0.1:8000/');

            cy.get('input[name="preco_max"]').invoke('val', 250).trigger('input');
            cy.contains('Filtrar').click();
            cy.contains('preco igual').should('exist');
        });

    });
});


