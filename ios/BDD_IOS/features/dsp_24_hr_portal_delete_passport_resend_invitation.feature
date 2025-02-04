Feature: HR Portal - Delete Passport resend invitation journey
  Background: HR login & send a new invite and opens the user from identity and access tab
    Given Browser is open and user clicks on HR login link
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Identity & Access Tab with HR Portal

  Scenario: Validate if user select no then passport should not be deleted
    Then Click on invitation of Single Passport link
    And Select the single passport form radio button
    Then Click on Continue button w.r.t single passport form
    And Enter First name w.r.t single passport form
    Then Enter Last name w.r.t single passport form
    And Enter Day - DOB w.r.t single passport form
    Then Enter Month - DOB w.r.t single passport form
    And Enter Year - DOB w.r.t single passport form
    Then Enter Email address w.r.t single passport form
    And Enter Phone number w.r.t single passport form
    Then Select the Staff group dropdown w.r.t single passport form
    And Select the Emp Type dropdown w.r.t single passport form
    Then Select the Emp Status dropdown w.r.t single passport form
    And Click on continue button w.r.t single passport forms
    Then Select create passport radio button w.r.t single passport form
    And Click continue button button w.r.t create passport
    Then Enter the user details in the search button - Identity & Access
    And Click on the Search button - Identity & Access
    Then Result is displayed & click on the same - Identity & Access
    Then Click on the Delete passport from records link
    Then User selected no for delete staff passport from record button
    Then User clicks on Continue button on delete passport page
    Then Verify that user profile is visible

  Scenario: Validate if user select yes then passport should get deleted
    Then Enter the user details in the search button - Identity & Access
    And Click on the Search button - Identity & Access
    Then Result is displayed & click on the same - Identity & Access
    Then Click on the Delete passport from records link
    Then User selected yes for delete staff passport from record button
    And User clicks on Continue button on delete passport page
    Then Verify the confirmation message displayed w.r.t passport delete