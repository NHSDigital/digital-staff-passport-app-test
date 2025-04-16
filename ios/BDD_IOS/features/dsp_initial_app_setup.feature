# Created by BabuK at 18/02/2025
Feature: Validate initial app setup journey
  # Pre-requisites - successful HR email verification and DSP app installation

  Scenario: Verify first page - app
    Given user verifies the question icon present
    Then user verifies the NHS logo - on first page
    Then user verifies the text on the “First page”
    And user clicks on continue button on first page

  Scenario: Verify create a pin page
    Given user verifies the question icon present
    Then user verifies “Create a PIN” opened
    Then user verifies term of use link present
    Then user verifies privacy notice link present
    Then user verifies terms and condition link present
    Then user sets new PIN
    And user confirms new PIN
    Then user clicks on continue button on first page

  Scenario: Verify fingerprint page
    Given user verifies the question icon present
    Then user verifies “Fingerprint” page opened
    Then user verifies if fingerprint toggle is disable
    Then user clicks on continue button on first page

  Scenario: Verify prove who you are page
    Given user verifies the question icon present
    Then user verifies “Prove who you are” page opened
    Then user verifies the text on the “Prove who you are” page
    Then user clicks on continue button on first page

  Scenario: Verify prove your identity page
    Given user verifies what to expect heading
    Then user verifies “Prove your identity” page opened
    Then user verifies what happens then heading
    Then user verifies my identity in person link present
    Then user clicks on continue button on first page
