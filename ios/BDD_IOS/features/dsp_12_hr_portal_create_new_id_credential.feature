Feature: Complete End to End Workflow - Create New Identity Credentials
  Scenario: HR user create a new identity credential
    Given Browser is open and user clicks on HR login link
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Pending Staff Passport Tab under HR Portal
    Then Enter the user details in the search button - Pending Staff Passport
    And Click on the Search button - Pending Staff Passport
    Then Result is displayed & click on the same - Pending Staff Passport
    And Click on create a new identity credential link on staff passport for user page
    Then Verify user details on page and click on continue
    And Confirm users details and select yes provide credential radio button and proceed
    Then User verify success message on webpage
    Then HR user validates the passport history event details w.r.t New Identity