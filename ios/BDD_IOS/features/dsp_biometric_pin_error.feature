# Created by parthp at 18/02/25
Feature: Validation on pin creation and error cases

  Scenario Outline: Validate pin error
    Given the ios app is launched with the specified activity
    When user verifies the question icon present
    Then user verifies the NHS logo
    Then user verifies the text on the “First page”
    And user clicks on “Continue” button
    Then user enter "<pin1>" & "<pin2>" that does not match
    And user clicks on continue button - create a pin page
    Then user validates the error "<message>"

    Examples:
      | pin1   | pin2   | message                                |
      | 141995 | 141996 | PIN doesn’t match                      |
      |        |        | Empty input fields                     |
      | abc123 | def456 | Enter alpha numeric                    |
      | {ab@(} | {%20%} | Enter special character                |
      | 123456 | 123456 | Cannot use sequential PIN              |
      | 654321 | 654321 | Cannot use reverse sequential as well |
      | 111111 |        | PIN not repeated                       |
      |        | 111111 | PIN not repeated vice versa            |
      |  1993  |  1993  | PIN not 6 digits                       |
