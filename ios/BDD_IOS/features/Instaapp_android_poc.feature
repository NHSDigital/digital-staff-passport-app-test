# Created by Babu1503738 at 07/11/2024
Feature: Instagram android app install and launch POC

  # Scenario to ensure the Uber app is not installed, then install it and verify
  Scenario: Installing fresh Instagram android app
    Given Uninstall the app if present
    When user install the app using APKs
    Then the app should be installed successfully

  # Scenario to launch, interact with elements, and close the app
  Scenario: Launch the android app, interact with its elements, and close
    Given the app is launched with the specified activity
    When the user logs in with username and password
    Then the user navigates to the home screen
    And searches for the NHS profile
    Then user attempt to close mobile app





