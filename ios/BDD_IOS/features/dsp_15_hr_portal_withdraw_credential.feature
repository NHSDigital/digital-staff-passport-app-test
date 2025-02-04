# Created by Parth162853 at 11/26/2024
Feature: # Enter feature name here
  Scenario: HR user review the request & provide that particular credential
    Given Browser is open and user clicks on HR login link
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Pending Staff Passport Tab under HR Portal
    Then Enter the user details in the search button - Pending Staff Passport
    And Click on the Search button - Pending Staff Passport
    Then Result is displayed & click on the same - Pending Staff Passport
    And Click on the Alert link w.r.t review Credentials request
    Then Click on Provide Credentials Button
    And Review the credentials request & select the provide radio button & Continue
    Then Confirm on Yes radio button w.r.t credential request & Click Continue
    Then Request reviewed successfully and message is displayed

  Scenario: HR user to withdraw credential
    Given Browser is open and user clicks on HR login link
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Pending Staff Passport Tab under HR Portal
    Then Enter the user details in the search button - Pending Staff Passport
    And Click on the Search button - Pending Staff Passport
    Then Result is displayed & click on the same - Pending Staff Passport
    And HR User clicked on view credentials link on staff passport page
    And HR User clicked on withdraw credential link which needs to withdraw
    And HR user clicks on Yes withdraw credential radio button
    Then HR User selects updated information to be provided option from dropdown
    And HR User clicked on continue button for withdraw credential
    Then HR User validates credential withdraw heading and click on back to Users passport link
    And HR User clicks on passport history page link and validates page heading
    Then HR user validates withdraw credential event details on passport history page