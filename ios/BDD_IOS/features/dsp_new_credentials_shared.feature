Feature: New credentials shared page
  Scenario: Verify Email confirming acceptance of identity credentials
    Given user has received an email
    Then user verifies the subject of an email
    Then user verifies the content of email is matched
    Then user verifies the user name in the email


  Scenario: Verify splash screen
    Given user is on splash screen
    Then user verifies the splash screen content nhs logo
    Then user verifies the nhs logo
    Then user verifies the version number
    Then user is landed on home page
    When user provide wrong face
    Then user gets an error message

  Scenario: Verify error for wrong face
    Given user is on splash screen
    When user provide wrong face
    Then user gets an error message
