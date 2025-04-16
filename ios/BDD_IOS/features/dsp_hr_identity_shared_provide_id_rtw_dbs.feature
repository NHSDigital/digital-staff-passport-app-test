Feature: HR user perform identity review
  Scenario: HR user reviews the identity request & provides the ID & Access Key credentials
    Given Browser is open and user clicks on HR login link
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    Then Click on the Identity & Access Tab with HR Portal
    Then Enter the user details in the search button - Identity & Access
    And Click on the Search button - Identity & Access
    Then Result is displayed & click on the same - Identity & Access
    Then identity and access page is opened for the user
    And Click on the Review Identity details
    Then Employment - Permanent details selected from dropdown list
    And Click on the Continue button - post selected Employment details
    Then user verifies the page title - Confirm identity
    Then user verify the credentials details should match
      | Attribute                  | Expected Value     |
      | id_first_name              | JACOB SEBASTIAN    |
      | id_last_name               | SMITH              |
      | id_dob                     | 6 July 1999        |
      | id_gender                  | Male               |
      | id_nationality             | British            |
      | id_address                 | 64, Derby Road, Belper DE56 4FL, United Kingdom|

    Then user selects yes radio button
    Then user clicks on continue button
    Then user verifies the page title - Provide right to work
    Then user selects yes radio button
    Then user clicks on continue button
    Then user verifies the page title - Provide DBS supporting information
    Then user see success page
    Then user verifies the credential status is confirmed and provided - identity
    Then user verifies the credential status is confirmed and provided - right to work
    Then user verifies the credential status is confirmed and provided - dbs

