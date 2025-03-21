# Created by BabuK at 18/02/2025
Feature: Validate initial app setup journey
  # Pre-requisites - successful HR email verification and DSP app installation

Scenario: Verify first page
  Given the ios app is launched with the specified activity
  When user verifies the question icon present
  Then user verifies the NHS logo
  Then user verifies the text on the “First page”
  And user clicks on “Continue” button
  Then user verifies “Create a PIN” opened

Scenario: Verify create a pin page
  When user verifies the question icon present
  Then user verifies term of use link present
  Then user verifies privacy notice link present
  Then user verifies terms link present
  Then user sets new PIN
  And user confirms new PIN
  Then user clicks on “Continue” button
  Then user verifies “Fingerprint” page opened

Scenario: Verify fingerprint page
  When user verifies the question icon present
#  Then user verifies account and setting icon present
  Then user clicks “Enable Fingerprint recognition” toggle to enable
  Then user clicks “Enable Fingerprint recognition” toggle to disable
  Then user clicks on “Continue” button
  Then user verifies “Prove who you are” page opened

Scenario: Verify prove who you are page
  When user verifies the question icon present
  Then user verifies the text on the “Prove who you are” page
  Then user clicks on “Continue” button
  Then user verifies “Prove your identity” page opened

Scenario: Verify prove your identity page
  Then user verifies what to expect heading
  Then user verifies what happens then heading
  Then user verifies my identity in person link present
  Then user clicks on “Continue” button
