Feature: Share credential with different organisation

  Scenario: HR user reviews the identity request - Share Journey
    Given Browser is open and user clicks on STH HR login link - share journey
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Identity & Access Tab with HR Portal
    Then Enter the user details in the search button - Identity & Access
    And Click on the Search button - Identity & Access
    Then Result is displayed & click on the same - Identity & Access
    And Click on the Review Identity Link
    Then Employment - Permanent details selected from dropdown list
    And Click on the Continue button - post selected Employment details
    And Click on the Continue button - post confirm review
    Then Request reviewed and success message is displayed

  Scenario: HR user accepts all shared credentials
    Given Browser is open and user clicks on STH HR login link - share journey
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Pending Staff Passport Tab under HR Portal
    Then Enter the user details in the search button - Pending Staff Passport
    And Click on the Search button - Pending Staff Passport
    Then Result is displayed & click on the same - Pending Staff Passport
    And Review shared credential and click accept all checkbox
    Then HR selects continue button on review shared credential page
    And HR review heading and select Yes confirm radio button
    Then HR selects continue button on review shared credential page
    Then HR validates success message for shared credential

  Scenario: HR user validate the shared credentials
    Given Browser is open and user clicks on STH HR login link - share journey
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Pending Staff Passport Tab under HR Portal
    Then Enter the user details in the search button - Pending Staff Passport
    And Click on the Search button - Pending Staff Passport
    Then Result is displayed & click on the same - Pending Staff Passport
    Then HR user verifies the identity credentials
    Then HR user verifies the employment checks credentials
    Then HR user verifies the Core skills training information

  Scenario: HR user cannot revoke credentials by non issuing organisation
    Given Browser is open and user clicks on STH HR login link - share journey
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Pending Staff Passport Tab under HR Portal
    Then Enter the user details in the search button - Pending Staff Passport
    And Click on the Search button - Pending Staff Passport
    Then Result is displayed & click on the same - Pending Staff Passport
    Then HR User clicks conflict resolution credential
    Then HR user verifies that the conflict resolution should have Reject shared credentials link

  Scenario: HR user deletes the passport record - Share Journey
    Given Browser is open and user clicks on STH HR login link - share journey
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Pending Staff Passport Tab under HR Portal
    Then Enter the user details in the search button - Pending Staff Passport
    And Click on the Search button - Pending Staff Passport
    Then Result is displayed & click on the same - Pending Staff Passport
    And Click on Manage Passport Link
    Then Click on Delete Passport Link
    And Click on Delete Passport Continue button
    Then Click on Delete Passport data button
    And Verify the message is displayed w.r.t Delete passport