# Created by parthp at 23/01/25
Feature: Manual & Automatic Archive credential : End to End Workflow

  Scenario: HR user review the request & provide the requested credential
      Given Browser is open and user clicks on HR login link
      When Enter the credentials & click on login button
      Then Verify the HR portal homepage is displayed
      And Click on the Pending Staff Passport Tab under HR Portal
      Then Enter the auto user details in the search button - Pending Staff Passport
      And Click on the Search button - Pending Staff Passport
      Then Result is displayed & click on the same - Pending Staff Passport
      And Click on the Alert link w.r.t review Credentials request
      Then Click on Provide Credentials Button
      And Review the credentials request & select the provide radio button & Continue
      Then Confirm on Yes radio button w.r.t credential request & Click Continue
      Then Request reviewed successfully and message is displayed

  Scenario: HR user manually archives the Fire safety credential
    Given Browser is open and user clicks on HR login link
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Pending Staff Passport Tab under HR Portal
    Then Enter the auto user details in the search button - Pending Staff Passport
    And Click on the Search button - Pending Staff Passport
    Then Result is displayed & click on the same - Pending Staff Passport
    And HR User clicked on Fire safety credential which needs to archive
    Then HR User validates the credential page header and click on archive this credential
    Then HR User validates credential archived heading and click on back to Users passport link
    And HR User clicks on Include archived credentials
    Then HR User clicks on Fire safety archived credential
    And Validates Fire safety archived message successfully
    Then Restore archived credentials and validate its success message

  Scenario: HR user review the request & provide the shared credentials
    Given Browser is open and user clicks on HR login link
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Pending Staff Passport Tab under HR Portal
    Then Enter the auto user details in the search button - Pending Staff Passport
    And Click on the Search button - Pending Staff Passport
    Then Result is displayed & click on the same - Pending Staff Passport
    And Click on the Alert link w.r.t review Shared Credentials request
    Then Confirm on Accept radio button w.r.t credential request & Click Continue
    Then Confirm on Yes radio button w.r.t Shared credential request & Click Continue
    And Shared cred request reviewed successfully and message is displayed

  Scenario: HR user validate auto archive status of Fire safety
    Given Browser is open and user clicks on HR login link
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Pending Staff Passport Tab under HR Portal
    Then Enter the auto user details in the search button - Pending Staff Passport
    And Click on the Search button - Pending Staff Passport
    Then Result is displayed & click on the same - Pending Staff Passport
    And HR User clicks on Include archived credentials
    Then HR User clicks on Fire safety auto archived credential
    And Validates Fire safety auto archived message successfully