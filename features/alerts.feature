Feature: all the tests related to alerts page
  Scenario: Ok alert
    Given I am on the alerts page
    When I click on Click for JS alert button
    When I accept OK alert
    Then The message for alerts page is "You successfully clicked an alert"