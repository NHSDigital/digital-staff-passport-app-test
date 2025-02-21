Feature: NHS IOS App - Returning to app after drop out
  """In this feature we are validating Returning to app after drop out page"""

  Scenario: Verify app ID rejected Page
    Given the ios app is launched with the specified activity
    When Click on the continue button on prove your identity page
    Then User validates your identity could not be confirm message
    And User validates question mark present on page
    Then User validates HR team will contact message on Page

