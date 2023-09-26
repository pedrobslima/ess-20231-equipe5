import { When, Then } from "@badeball/cypress-cucumber-preprocessor";

//Given("que estou na página de criação de postagens", () => {
//  // Implemente a navegação para a página de criação de postagens
//  cy.visit(`/post/new_post/`);
//});

When("Seleciono o título de post {string}", (title: string) => {
  cy.get('input[name="title"]').type(title);
});

When("Escolho a tag {string}", (tag: string) => {
  cy.get('input[data-cy="input-tag"]').type(tag);
  cy.get('button[data-cy="input-tag-button"]').click();
});

When("Escrevo no corpo {string}", (body: string) => {
  cy.get('textarea[name="body"]').type(body);
});

Then("Minha review é publicada", () => {
  cy.get('button[type="submit"]').click()
});

Then("Eu vejo o post do usuário {string} com título {string} e conteúdo {string} e tags {string}", (user: string, title: string, body: string, tag: string) => {
  cy.contains(user).should("be.visible");
  cy.contains(title).should("be.visible");
  cy.contains(body).should("be.visible");
  cy.contains(tag).should("be.visible");
});