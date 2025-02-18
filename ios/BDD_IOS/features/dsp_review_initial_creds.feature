Feature: Review and confirm initial three credentials
  Background: user is on credentials page

  Scenario: Verify Credentials page
    Then user verifies the page heading
    Then user verifies question mark icon is present
    Then user verifies user account icon is present
    Then user verifies Home button is displayed
    Then user verifies credentials button is displayed
    Then user verifies credentials to confirm has identity credential listed with action required
    Then user verifies credentials to confirm has right to work credential listed with action required
    Then user verifies credentials to confirm has DBS supporting documents listed with action required
    Then user verifies confirmed credentials has "No credentials yet"

  Scenario: Verify identity page
    When user click identity credential
    Then user verifies the page heading
    Then user verifies provided by Trust
    Then user verifies the identity credential details - Name,DOB, Legal gender, Nationality, issued on
    Then user verifies link something is not right
    When user clicks confirm credential button
    Then user see Confirming credential spinner
    Then user lands on credentials confirmed page
    Then user verifies the text on the page
    When user clicks on Back to my credentials button
    Then user lands on credentials page
    Then user verifies identity credential is removed from credentials to confirm
    Then user verifies identity is listed under confirmed credentials

  Scenario: Verify Right to work page
    When user click right to work credential
    Then user verifies the page heading
    Then user verifies the right to work credential details - Photo of your face, name, DOB, Biometric page, passport expiry date
    Then user verifies link something went wrong
    Then use click confirm credential button
    Then user see a spinner page with confirming credential
    Then user lands on credentials confirmed page
    Then user verifies the text on the page
    When user clicks on Back to my credentials button
    Then user lands on credentials page
    Then user verifies right to work credential is removed from credentials to confirm
    Then user verifies right to work is listed under confirmed credentials

  Scenario: Verify DBS supporting information
    When user click DBS supporting documents
    Then user verifies the page heading
    Then user verifies the DBS supporting documents details - Name, Date of birth, Verified current address, Resident from, Passport number, Passport nationality,Passport issue date, Confirm credential button
    Then user verifies link something went wrong
    Then user click confirm credential button
    Then user see a spinner page with confirming credential
    Then user lands on credentials confirmed page
    Then user verifies the text on the page
    When user clicks on Back to my credentials button
    Then user lands on credentials page
    Then user verifies DBS supporting documents is removed from credentials to confirm
    Then user verifies DBS supporting documents is listed under confirmed credentials


