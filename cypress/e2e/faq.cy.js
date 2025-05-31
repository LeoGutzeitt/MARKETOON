Cypress.Commands.add('deletedatabase', () => {
    cy.exec('python delete_database.py', { failOnNonZeroExit: false });
});

describe('Acesso ao FAQ / Suporte', () => {
  before(() => {
    cy.deletedatabase();  
  });
  it('vai da home para a página de suporte e interage com o FAQ', () => {
    cy.visit('/');
    cy.get('.support-button').contains('Fale com o Suporte').click();
    cy.url().should('include', '/suporte');
    cy.get('h1').should('contain.text', 'FAQ / Suporte');
    cy.get('.faq-item').should('have.length', 4).each(($el) => {
      cy.wrap($el).find('h2').click();
      cy.wrap($el).should('have.class', 'active');
      cy.wrap($el).find('p').should('be.visible');
    });
    cy.get('.question-box textarea').should('be.visible');

    cy.on('window:alert', (str) => {
      expect(str).to.equal('Pergunta enviada! Em breve entraremos em contato.');
    });

    cy.get('.question-box button').click();
  });
});

