# Created by parthp at 27/02/25
Feature: DSP End to End Flow

  Scenario: Validate no invite present in - app
    Given user clicks on continue button on first page no invite
    When user validate check your email popup
    Then user clicks on close app

  Scenario: Invitation from HR User - Single Passport Invite - mobile
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

  Scenario: Save the start now link provided in the email - notification
    Given user opens the received email from iphone notification
    When user scroll till start now and saves the start now link present
#     Then user clicks on the start now link

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
    Then use click confirm credential button
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

  Scenario: User validate that no credentials displayed in action on homepage
    When user clicks on back link
    Then user is on credentials page with dates
    Then User validates no credentials present
