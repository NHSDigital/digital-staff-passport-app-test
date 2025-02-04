Feature: NHS IOS app install and launch POC
  Scenario: Launch the ios app and perform actions
    Given the ios app is launched with the specified activity
    When Click on the continue button on prove your identity page
    Then Click on the credentials that are ready to review
    And Click on credentials tab
    Then Click on connections tab
    And Click on messages tab