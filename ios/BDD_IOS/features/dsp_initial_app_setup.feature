# Created by BabuK at 18/02/2025
Feature: DSP App initial setup
  # Pre-requisites - successful HR email verification and DSP app installation

  Scenario: Validate initial app setup and navigate to Prove your identity page
    Given the ios app is launched with the specified activity
    When user validates the first page and taps Continue
    Then create PIN page appears with external links
    And user sets and confirms a new PIN
    Then app allows the user to proceed with the PIN setup
    And user views the Fingerprint page and taps Continue
    Then user navigates to the Prove who you are page and checks the content
    And user taps Continue on the Prove who you are page
    Then user sees Prove your identity page explaining the verification process
    And user can choose to Continue to verify their identity digitally

