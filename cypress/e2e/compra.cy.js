Cypress.Commands.add('deletedatabase', () => {
  cy.exec('python delete_database.py', { failOnNonZeroExit: false });
});

function preencherFormularioCompra() {
  cy.get('#nome').type('Cliente Teste');
  cy.get('#email').type('cliente@email.com');
  cy.get('#cartao').type('4111111111111111');
  cy.get('#validade').type('2029-12');
  cy.get('#cvv').type('123');
  cy.get('button').contains('Finalizar Compra').click();
}

function cadastrarProduto(nomeProduto) {
  cy.visit('/cadastro/');
  cy.get('#nome').type(nomeProduto);
  cy.get('#email').type('teste@email.com');
  cy.get('#telefone').type('81999999999');
  cy.get('#descricao').type('Descrição do produto');
  cy.get('#preco').type('150');
  cy.get('#imagem').selectFile('media/produtos/lofiwall1.jpg');
  cy.get('button[type="submit"]').click();
  cy.url().should('eq', 'http://127.0.0.1:8000/');
  cy.wait(1000); 
}

describe('Fluxos completos de compra com cadastro e carrinho', () => {

  before(() => {
    cy.deletedatabase();  
  });

  it('Carrinho -> Comprar -> Direito Compartilhado', () => {
    const nomeProduto = `Teste carrinho ${Date.now()}`;
    cadastrarProduto(nomeProduto);
    cy.contains(nomeProduto)
      .closest('.product-card')
      .find('button.cart-button')
      .click();
    cy.contains('Comprar').click();
    cy.contains(/Direito compartilhado/i).click();
    cy.url().should('include', '/pagamento');
    preencherFormularioCompra();
  });

  it('Carrinho -> Comprar -> Direito Pleno e produto some da home', () => {
    const nomeProduto = `Teste carrinho ${Date.now()}`;
    cadastrarProduto(nomeProduto);
    cy.contains(nomeProduto)
      .closest('.product-card')
      .find('button.cart-button')
      .click();
    cy.contains('Comprar').click();
    cy.contains(/Direito pleno/i).click();
    cy.url().should('include', '/pagamento');
    preencherFormularioCompra();
    cy.wait(1500);
    cy.visit('/');
    cy.contains(nomeProduto).should('not.exist');
  });

  it('Comprar Direto -> Direito Compartilhado', () => {
    const nomeProduto = `Teste carrinho ${Date.now()}`;
    cadastrarProduto(nomeProduto);
    cy.contains(nomeProduto)
      .closest('.product-card')
      .within(() => {
        cy.contains('Comprar').click();
      });
    cy.contains(/Direito compartilhado/i).click();
    cy.url().should('include', '/pagamento');
    preencherFormularioCompra();
  });

  it('Comprar Direto -> Direito Pleno e produto some da home', () => {
    const nomeProduto = `Teste carrinho ${Date.now()}`;
    cadastrarProduto(nomeProduto);
    cy.contains(nomeProduto)
      .closest('.product-card')
      .within(() => {
        cy.contains('Comprar').click();
      });
    cy.contains(/Direito pleno/i).click();
    cy.url().should('include', '/pagamento');
    preencherFormularioCompra();
    cy.wait(1500);
    cy.visit('/');
    cy.contains(nomeProduto).should('not.exist');
  });

  it('Falha ao tentar finalizar compra sem preencher nome', () => {
    const nomeProduto = `Produto teste ${Date.now()}`;
    cadastrarProduto(nomeProduto);

    cy.contains(nomeProduto)
      .closest('.product-card')
      .within(() => {
        cy.contains('Comprar').click();
      });

    cy.contains(/Direito compartilhado/i).click();
    cy.url().should('include', '/pagamento');

    cy.get('#email').type('cliente@email.com');
    cy.get('#cartao').type('4111111111111111');
    cy.get('#validade').type('2029-12');
    cy.get('#cvv').type('123');

    cy.get('button').contains('Finalizar Compra').click();

    cy.get('#nome').then(($input) => {
      expect($input[0].checkValidity()).to.be.false;
      expect($input[0].validationMessage).to.match(/Preencha este campo./i);
    });
  });

  it('Falha ao tentar finalizar compra sem preencher email', () => {
    const nomeProduto = `Produto teste ${Date.now()}`;
    cadastrarProduto(nomeProduto);

    cy.contains(nomeProduto)
      .closest('.product-card')
      .within(() => {
        cy.contains('Comprar').click();
      });

    cy.contains(/Direito pleno/i).click();
    cy.url().should('include', '/pagamento');

    cy.get('#nome').type('Cliente Teste');
    cy.get('#cartao').type('4111111111111111');
    cy.get('#validade').type('2029-12');
    cy.get('#cvv').type('123');

    cy.get('button').contains('Finalizar Compra').click();

    cy.get('#email').then(($input) => {
      expect($input[0].checkValidity()).to.be.false;
      expect($input[0].validationMessage).to.match(/Preencha este campo./i);
    });
  });


});
