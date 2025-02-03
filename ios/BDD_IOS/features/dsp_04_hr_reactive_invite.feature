Feature: Invite DSP user with reactive flow
  Scenario: Invitation from HR User - Single Passport Invite
    Given Browser is open and user clicks on HR login link
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    Then Click on the Identity & Access Tab with HR Portal
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
    Then Verify the status of the request under Identity & access search form