Feature: Publish Review
 As an user
 I want to post a review about a desired topic
 so that other users can interact with it

  Scenario: publish review
    Given I am on publish page
    And the user already signed in
    When I write my topic and content with no null values
    And Click to publish
    Then my post will be sent to another users according to the tags

  Scenario: write review
    Given I am on publish page

  