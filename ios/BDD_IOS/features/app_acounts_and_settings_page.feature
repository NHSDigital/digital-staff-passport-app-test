Feature: NHS IOS App - Accounts and Settings page Flows
  """In this feature we are validating Accounts and Settings page of DSP app"""

  """In first scenario we are validating the incorrect pin message error on Sign in after initial setup page"""
  Scenario: Verify Accounts and Setting page of dsp app
    Given the ios app is launched with the specified activity
    When Click on the continue button on prove your identity page
    Then User clicks on accounts and settings tab
    And User validate accounts and settings page heading
    Then User Validate question mark icon on account and settings Page
    And User clicks on back link on account and settings page
    Then User clicks on accounts and settings tab
    And User validate delete your NHS digital staff passport on Page
    Then User clicks on terms of use and other policies link

