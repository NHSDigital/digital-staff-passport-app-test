# Created by parthp at 14/02/25
Feature: Validate that home page for the DSP APP

  Scenario: Validate the waiting for org to review screen on appstart
    Given the ios app is launched with the specified activity
    When click on continue button on finger recognition page
    Then user enters the pin and click on continue
    And validate the trust name and waiting message
    Then validate receive an email message on screen
    And user validates if question icon is present


  Scenario: Validate the identity credentials accepted email
    # open notification, click on it, validate the email, minimize the screen, open the app

  Scenario: Launch the app and verify the home page of the app
    Given the ios app is launched with the specified activity
    When click on continue button on finger recognition page
    Then user enters the pin and click on continue
    Then user verify the welcome message on the homepage
    And user validates if question icon is present
    Then user validates if account icon is present
    And user validates if homepage has action section present
    Then user validate that new provided credentials are visible on homepage
    And user validate the tag present on the new credentials
    Then user validates if credentials tab is present
