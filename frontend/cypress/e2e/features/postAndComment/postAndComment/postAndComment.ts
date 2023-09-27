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

When("Escrevo {string} no corpo do post", (body: string) => {
    cy.get('textarea[name="body"]').type(body);
});

Then("Minha review é publicada", () => {
    cy.get('button[type="submit"]').click()
});

Then("Eu vejo o post do usuário {string} com título {string}, com conteúdo {string} e tags {string}", (user: string, title: string, body: string, tag: string) => {
    cy.contains(user).should("be.visible");
    cy.contains(title).should("be.visible");
    cy.contains(body).should("be.visible");
    cy.contains(tag).should("be.visible");
});

When("Seleciono a opção de comentar no post", () => {
    cy.get('button[data-cy="comment-button"]').click();
});

When("Escrevo {string} no corpo do comentário", (c_body: string) => {
    cy.get('input[data-cy="comment-draft-body"]').type(c_body);
});

When("Seleciono a opção de publicar o comentário", () => {
    cy.get('button[data-cy="comment-submit"]').click()
});

Then("meu comentário foi publicado com o corpo sendo {string}, na página do post original", (c_body: string) => {
    cy.contains(c_body).should("be.visible");
});