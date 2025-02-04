Feature: HR user perform identity review
  Scenario: HR user reviews the identity request & provides the ID & Access Key credentials
     Given Browser is open and user clicks on HR login link
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    Then Click on the Identity & Access Tab with HR Portal
    Then Enter the user details in the search button - Identity & Access
    And Click on the Search button - Identity & Access
    Then Result is displayed & click on the same - Identity & Access
    And Click on the Review Identity Link
#    Then Employment - Permanent details selected from dropdown list
    And Click on the Continue button - post selected Employment details
    Then Click on the confirm button for identity review
    And Click on the Continue button - post confirm button selected
    Then Gender - Male details selected from dropdown list
    And Nationality details selected from dropdown list
    Then Enter details in the address 1 field
    And Enter details in the address 2 field
    Then Enter details in the town field
    And Enter details in the Postcode field
    Then Enter details in the Country field
    And Click on the Continue button - post personal details entered
#    Then Click on the Confirm button to proceed for review
    And Click on the Continue button - post confirm review
    Then Request reviewed and success message is displayed