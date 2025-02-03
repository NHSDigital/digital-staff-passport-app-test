Feature: Create temporary credentials
  Scenario: HR user to create temporary placement credential
    Given Browser is open and user clicks on HR login link
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Pending Staff Passport Tab under HR Portal
    Then Enter the user details in the search button - Pending Staff Passport
    And Click on the Search button - Pending Staff Passport
    Then Result is displayed & click on the same - Pending Staff Passport
    And HR User clicked on Create temporary placement credential link
    Then HR User validate the next page header and proceed further
    And HR User adds the details in position title field
    Then HR user adds the details in position number field
    Then HR User adds the temporary placement credentials start date
    And HR User adds the temporary placement credentials end date
    And HR user adds the Brief description of work pattern
    Then HR user clicks on continue button for temp creation
    And HR user validates the page heading and select coventry as permanent employer option from dropdown
    Then HR user adds the details in department field
    And HR user adds the details in department contact name field
    Then HR user adds the details in department contact email address field
    Then HR user adds the details in Approved by field
    And HR User adds the details in HR contact field
    And HR user clicks on continue button for temp creation
    Then HR user verifies the Licence to attend heading and select yes radio button option
    And HR user clicks on continue button for temp creation
    Then HR user confirm details and provide credential heading and select yes radio button option
    And HR user clicks on continue button for temp creation
    Then HR user validates the Temporary placement credential provided success message
    Then HR user validates the passport history event details w.r.t temporary placement