Feature: Review and add 30 credentials into MS Authenticator Wallet & Validate the Passport Status as Active

  Scenario: Validate the passport status in both profile page & reviewed staff passport tab
    Given Browser is open and user clicks on HR login link
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Pending Staff Passport Tab under HR Portal
    Then Enter the user details in the search button - Pending Staff Passport
    And Click on the Search button - Pending Staff Passport
    Then Result is displayed & click on the same - Pending Staff Passport
    Then User clicks on the complete credential required & validate the same
    And Click on the Reviewed Staff Passport Tab under HR Portal
    Then Enter the user details in the search button - Reviewed Staff Passport
    And Click on the Search button - Reviewed Staff Passport
    Then Validate the passport status - Reviewed Staff Passport
    And  Click on the passport user - Reviewed Staff Passport
    Then Validate the passport status w.r.t complete credential