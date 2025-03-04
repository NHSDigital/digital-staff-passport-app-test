Feature: NHS IOS App - Sign in After Initial Setup Flows
  """In this feature we are validating scenarios on Sign in after initial setup page"""

  """In first scenario we are validating the incorrect pin message error on Sign in after initial setup page"""
  Scenario: Verify Incorrect Pin message
    Given the ios app is launched with the specified activity
    When User enters incorrect pin on enter your pin box
    Then User clicks on Continue button on log in page
    And User verifies Incorrect Pin error message on UI screen for 2 attempts remaining
    Then User re-enters incorrect pin on enter your pin box
    And User clicks on Continue button on log in page
    Then User verifies Incorrect Pin error message on UI screen for 1 attempts remaining
    And User re-enters incorrect pin on enter your pin box
    Then User clicks on Continue button on log in page
    And User verifies maximum number of login attempt exceeded

  """In Below scenario we are validating forgotton pin error message on UI screen"""
  Scenario: Launch the ios app and perform action
    Given the ios app is launched with the specified activity
    When User Click on I've forgotton my pin link
    Then User Verifies forgotten pin message is displaying

