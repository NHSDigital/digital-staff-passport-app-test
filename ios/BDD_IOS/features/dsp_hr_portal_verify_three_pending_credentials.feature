Feature: Verify pending credentials app

  Background: HR User navigates to pending credentials page
    Given Browser is open and user clicks on HR login link
    When Enter the credentials & click on login button
    Then Verify the HR portal homepage is displayed
    And Click on the Pending Staff Passport Tab under HR Portal
    Then Enter the user details in the search button - Pending Staff Passport
    And Click on the Search button - Pending Staff Passport
    Then Result is displayed & click on the same - Pending Staff Passport
    Then Click on view credential inside 3 pending credential banner

#  Scenario: Verify the pending credentials page elements
#    Then verify back link is displayed
#    Then verify the link - remind username to review credential
#    Then verify credential heading has identity and new starter information sub heading

  Scenario: Verify DBS supporting information credentials data
    When user clicks on expand button for DBS supporting information
    Then user verify the credentials details should match
    | attribute     | expected_value |
    | dbs_first_name    | JACOB SEBASTIAN|
    | dbs_last_name     | SMITH          |
#    | dbs_dob	| 6 July 1999    |
#    | Current_address_verified| Active                |
#    | Current_address          | Admin                 |
#    | Date of address check          | New York              |
#    | Identity verified       | USA                   |
#    | Level of Assurance      | 10001                 |
#    | Policy    | 2025-03-26 12:30:00   |
#    | Evidence_checked_by	  | Premium               |
#    | Passport_date_of_birth	           | 30                    |
#    | Evidence_Profile	        | Male                  |
#    | SubjectID      | English               |
#    | Origin      | UTC-5                 |
#    | Assurance_policy	      | USD                   |
#    | Assurance_outcome	  | Active                |
#    | Provider        | 150                   |
#    | Verification_method | REF12345              |
#    | Pedigree     | 1995-05-15            |
#    | Last_refresh    | Gold                  |
