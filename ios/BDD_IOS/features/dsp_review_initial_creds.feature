Feature: Review and confirm initial three credentials
  Background: user is on credentials page
    Given the ios app is launched with the specified activity
    When click on continue button on finger recognition page
    Then user enters the pin and click on continue
    Then user verify the welcome message on the homepage
    Then user is on credentials page with dates

  Scenario: Verify back link is working on credentials page with dates
    When user clicks on back link
    Then user is on home page

  Scenario: Verify back link is working on identity credentials page
    When user clicks on identity credential
    And user clicks on back link
    Then user is on credentials page with dates

  Scenario: Verify back link working on right to work credential page
    When user clicks on right to work credential
    And user clicks on back link
    Then user is on credentials page with dates

  Scenario: Verify back link working DBS supporting information page
    When user clicks on DBS supporting documents
    And user clicks on back link
    Then user is on credentials page with dates

  Scenario: Verify Credentials page with dates
    Then user verifies the page heading
    Then user verifies back link is present
    Then user verifies question mark icon is present
    Then user verifies user account icon is present
    Then user verifies Home button is displayed
    Then user verifies credentials button is displayed
    Then user verifies credentials to confirm has identity credential listed with action required
    Then user verifies credentials to confirm has right to work credential listed with action required
    Then user verifies credentials to confirm has DBS supporting documents listed with action required
    Then user verifies confirmed credentials has "No credentials yet"

  Scenario Outline: Verify identity page
    When user click identity credential
    Then user verifies the page heading
    Then user verifies back link is present
    Then user verifies provided by Trust
    Then user verifies the identity credential details - "<Fields>"
    Then user verifies link something is not right
    When user clicks confirm credential button
    Then user see Confirming credential spinner
    Then user lands on credentials confirmed page
    Then user verifies the text on the page
    When user clicks on Back to my credentials button
    Then user lands on credentials page
    Then user verifies identity credential is removed from credentials to confirm
    Then user verifies identity is listed under confirmed credentials
    Examples:
      | Fields |
      | Name   |
      | DOB    |
      | Legal gender |
      | Nationality |
      | Issued on |

  Scenario Outline: Verify Right to work page
    When user click right to work credential
    Then user verifies the page heading
    Then user verifies back link is present
    Then user verifies the right to work credential details - "<Fields>"
    Then user verifies link something went wrong
    Then user click confirm credential button
    Then user see a spinner page with confirming credential
    Then user lands on credentials confirmed page
    Then user verifies the text on the page
    When user clicks on Back to my credentials button
    Then user lands on credentials page
    Then user verifies right to work credential is removed from credentials to confirm
    Then user verifies right to work is listed under confirmed credentials
    Examples:
      | Fields               |
      | Name                 |
      | DOB                  |
      | Passport expiry date |

  Scenario Outline: Verify DBS supporting information
    When user click DBS supporting documents
    Then user verifies the page heading
    Then user verifies back link is present
    Then user verifies the DBS supporting documents details - "<Fields>"
    Then user verifies link something went wrong
    Then user click confirm credential button
    Then user see a spinner page with confirming credential
    Then user lands on credentials confirmed page
    Then user verifies the text on the page
    When user clicks on Back to my credentials button
    Then user lands on credentials page
    Then user verifies DBS supporting documents is removed from credentials to confirm
    Then user verifies DBS supporting documents is listed under confirmed credentials
    Examples:
    | Fields |
    | Name |
    | DOB |
    | Verified current address |
    | Resident from |
    | Passport number |
    | Passport Nationality |
    | Passport issue date |

  Scenario: Verify account icon
    Then user click account icon
    Then user is accounts and settings page
    Then user see delete your NHS digital staff passport section and verifies the message inside
    Then user see security and privacy section and a link "terms of use and other policies" inside
    Then user see question icon


  Scenario: User validate that no credentials displayed in action on homepage
    When user clicks on back link
    Then user is on credentials page with dates
    Then User validates no credentials present


