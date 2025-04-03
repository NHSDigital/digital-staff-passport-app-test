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

  Scenario: Verify the pending credentials page elements
    Then verify back link is displayed
    Then verify the link - remind username to review credential
    Then verify withdraw link for dbs credentials
    Then verify withdraw link for identity credentials
    Then verify withdraw link for right to work credentials

  Scenario: Verify credentials data - DBS supporting information
    When user clicks on expand button for DBS supporting information
    Then user verify the credentials details should match
      | Attribute                       | Expected Value     |
      | dbs_first_name                  | JACOB SEBASTIAN    |
      | dbs_last_name                   | SMITH              |
      | dbs_dob                         | 6 July 1999        |
      | dbs_current_address_verified    | Yes                |
      | dbs_current_address             | 64, Derby Road, Belper DE56 4FL, United Kingdom|
      | dbs_date_of_address_check       | 30 January 2025    |
      | dbs_identity_verified           | Yes                |
      | dbs_level_of_Assurance          | H1A                |
      | dbs_policy                      | GPG 45             |
      | dbs_evidence_checked_by         | Digidentity B.V.   |
      | dbs_passport_date_of_birth      | 6 July 1999        |
      | dbs_evidence_profile            | H1A                |
      | dbs_subject_id                  | 61c8e895-d3a1-4e77-9050-cb4c98e54ad7|
      | dbs_origin                      | Digidentity B.V.   |
      | dbs_assurance_policy            | GPG 45             |
      | dbs_assurance_outcome           | H1A                |
      | dbs_provider                    | Unknown Org        |
      | dbs_verifier                    | Origin             |
      | dbs_verification_method         | Document Verification with Record Verification|
      | dbs_pedigree                    | Authoritative      |
      | dbs_last_refresh                | 6 March 2025       |

    Scenario: Verify credentials data - Identity
    When user clicks on expand button for identity
    Then user verify the credentials details should match
      | Attribute                  | Expected Value     |
      | id_first_name              | JACOB SEBASTIAN    |
      | id_last_name               | SMITH              |
      | id_dob                     | 6 July 1999        |
      | id_legal_gender            | Male               |
      | id_address                 | 64, Derby Road, Belper DE56 4FL, United Kingdom|
      | id_origin                  | Substantive NHS Employing Organisation|
      | id_assurance_policy        | GPG 45             |
      | id_assurance_outcome       | GPG 45 applied     |
      | id_provider                | NHS England        |
      | id_verifier                | Origin             |
      | id_verification_method     | Document Verification|
      | id_pedigree                | Sourced             |
      | id_last_refresh            | 6 March 2025 at 20:37|

  Scenario: Verify credentials data - right to work
    When user clicks on expand button for right to work
    Then user verify the credentials details should match
      | Attribute                   | Expected Value     |
      | rtw_legal_first_name        | JACOB SEBASTIAN    |
      | rtw_legal_surname           | SMITH              |
      | rtw_birth_date              | 6 July 1999        |
      | rtw_identity_verified       | Yes                |
      | rtw_evidence_checked_by     | Digidentity B.V.   |
      | rtw_gpg45_profile           | H1A                |
      | rtw_origin                  | Digidentity B.V.   |
      | rtw_assurance_policy        | GPG 45             |
      | rtw_assurance_outcome       | H1A                |
      | rtw_provider                | Unknown Org        |
      | rtw_verifier                | Digidentity B.V.   |
      | rtw_verification_method     | Document Verification with Record Verification|
      | rtw_pedigree                | Authoritative      |
      | rtw_last_refresh            | 6 March 2025       |
