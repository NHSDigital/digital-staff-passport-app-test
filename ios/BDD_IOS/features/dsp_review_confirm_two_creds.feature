# Created by BabuKoya at 24/02/2025
Feature: Review and confirm two credentials
  Background: user is on credentials page
    Given the ios app is launched with the specified activity
    When click on continue button on finger recognition page
    Then user enters the pin and click on continue
    Then user verify the welcome message on the homepage
    Then user is on credentials page with dates

  Scenario: Verify back link on credentials page
    When user clicks on back link
    Then user navigate back to home page with 2 credentials ready to review
    And user clicks on 2 credentials ready to review
    Then user navigates to credentials page

  Scenario: Verify credentials page
    Then user verifies question mark icon is present
    Then user verifies user account icon is present
    Then user verifies Home button is displayed
    Then user verifies credentials button is displayed
    Then user verifies credentials to confirm heading
    Then user verifies credentials to confirm has Professional registration credential listed with action required
    Then user verifies credentials to confirm has Employment assignment credential listed with action required
    Then user verifies confirmed credentials heading
    Then user verifies confirmed credentials has DBS supporting information credential listed in confirmed creds
    Then user verifies confirmed credentials has Right to work credential listed in confirmed creds
    Then user verifies confirmed credentials has identity credential listed in confirmed creds

  Scenario: Verify action to confirm professional registration credential
    When user clicks on Professional registration credential to confirm
    Then user verifies professional registration heading
    Then user verifies details heading
    Then user verifies details body section
    Then user verifies staff member section
    Then user verifies expiry date section
    Then user verifies status section
    Then user verifies registration date section
    Then user verifies link something is not right
    When user clicks confirm credential button
    Then user see Confirming credential spinner
    Then user lands on credentials confirmed page
    Then user verifies the text on the page
    When user clicks on Back to my credentials button
    Then user lands on credentials page
    Then user verifies professional registration cred is removed from credentials to confirm
    Then user verifies professional registration cred is listed under confirmed credentials

  Scenario: Verify action to confirm employment assignment credential
    When user clicks on employment assignment credential to confirm
    Then user verifies employment assignment heading
    Then user verifies emp assign details heading
    Then user verifies employer section
    Then user verifies department section
    Then user verifies job title section
    Then user verifies assignment category section
    Then user verifies assignment status section
    Then user verifies assignment effective start date section
    Then user verifies employment assignment number section
    Then user verifies link something is not right
    When user clicks confirm credential button
    Then user see Confirming credential spinner
    Then user lands on credentials confirmed page
    Then user verifies the text on the page
    When user clicks on Back to my credentials button
    Then user lands on credentials page
    Then user verifies employment assignment cred is removed from credentials to confirm
    Then user verifies employment assignment cred is listed under confirmed credentials
