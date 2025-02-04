Feature: Provide Complete Credentials
  Scenario: HR user review the request & provide the credentials
    Given Browser is open and user clicks on HR login link
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Pending Staff Passport Tab under HR Portal
    Then Enter the user details in the search button - Pending Staff Passport
    And Click on the Search button - Pending Staff Passport
    Then Result is displayed & click on the same - Pending Staff Passport
    And Click on Connect to ESR Link
    Then Enter the ESR Number & click on confirm button
    And Click on Connect to Passport Link & connect button
    Then Select Yes radio button & click on continue button
##    And Click on Provide Credentials Link
    Then Click on the back link to navigate back to passport page
    And Click on the Alert link w.r.t review Credentials request
    Then Click on Provide Credentials Button
    And Review the credentials request & select the provide radio button & Continue
    Then Confirm on Yes radio button w.r.t credential request & Click Continue
    Then Request reviewed successfully and message is displayed
