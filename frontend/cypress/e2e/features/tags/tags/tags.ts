import { When, Then } from "@badeball/cypress-cucumber-preprocessor";

//Given("que estou na página de criação de postagens", () => {
//  // Implemente a navegação para a página de criação de postagens
//  cy.visit(`/post/new_post/`);
//});

When("eu adiciono a tag {string}", (tag: string) => {
  // Implemente a lógica para adicionar a tag
  cy.get('input[data-cy="input-tag"]').type(tag);
  cy.get('button[data-cy="input-tag-button"]').click();
});

Then("as tags {string} e {string} devem ser exibidas", (t1: string, t2: string) => {
  const tagList: string[] = [t1, t2];
  tagList.forEach((tag) => {
    cy.contains(tag).should("be.visible");
  });
});

When("eu removo a tag {string}", (tag: string) => {
  cy.contains(tag)
    .children('button[data-cy="remove-tag"]')
    .click();
});

Then("a tag {string} não deve mais estar visível", (tag: string) => {
  cy.contains(tag).should("not.exist");
});
