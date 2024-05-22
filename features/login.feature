Feature: Will store all the tests related to login
  @tmta21
  Scenario: Wrong username / Wrong password
    Given I am on the login page
    When I insert an username "bogdan"
    When I insert a password "parolatmta21"
    When I click on the login button
    Then The banner is displayed
    Then The message is "Your username is invalid!"

  @tmtapositive @login
  Scenario: Positive scenario
    Given I am on the login page
    When I insert an username "tomsmith"
    When I insert a password "SuperSecretPassword!"
    When I click on the login button
    Then The banner is displayed
    Then The message is "You logged into a secure area!"