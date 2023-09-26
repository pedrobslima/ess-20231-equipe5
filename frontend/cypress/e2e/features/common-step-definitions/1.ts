import { Given } from "@badeball/cypress-cucumber-preprocessor";

Given("que estou na página de criação de postagens", () => {
    cy.visit(`/post/new_post/`);
  });