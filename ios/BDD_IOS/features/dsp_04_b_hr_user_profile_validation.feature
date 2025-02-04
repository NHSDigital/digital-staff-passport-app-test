Feature: HR Portal user profile data expected validation

  #incomplete
  # This automation in incomplete as discussed with devashish because we are unable to find fname, lname ...etc text

  Scenario: HR user - Check if the user profile data is expected
    Given Browser is open and user clicks on HR login link
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Pending Staff Passport Tab under HR Portal
    Then Enter the user details in the search button - Pending Staff Passport
    And Click on the Search button - Pending Staff Passport
    Then Result is displayed & click on the same - Pending Staff Passport
    Then Validate the passport status w.r.t pending credential
    And Click on the Show all detail by perform a scroll
    Then Verify that fname is displayed
    And Verify that lname is displayed
    And Verify that date of birth is displayed
    Then Verify that telephone number is displayed
    And Verify that email is displayed
    Then Verify that staff group is displayed
    And Verify that employment type is displayed
    Then Verify that employment status is displayed