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
    Then verify credential heading has identity and new starter information sub heading

  Scenario: Verify credentials data - DBS supporting information
    When user clicks on expand button for DBS supporting information
    Then user verify the credentials details should match
      | Attribute                       | Expected Value     |
      | dbs_first_name                  | JACOB SEBASTIAN    |
      | dbs_last_name                   | SMITH              |
      | dbs_dob                         | 6 July 1999        |
      | dbs_current_address_verified    | Active             |
      | dbs_current_address             | Admin              |
      | dbs_date_of_address_check       | New York           |
      | dbs_identity_verified           | USA                |
      | dbs_level_of_Assurance          | 10001              |
      | dbs_policy                      | 2025-03-26 12:30:00|
      | dbs_evidence_checked_by         | Premium            |
      | dbs_passport_date_of_birth      | 30                 |
      | dbs_evidence_profile            | Male               |
      | dbs_subject_id                  | English            |
      | dbs_origin                      | UTC-5              |
      | dbs_assurance_policy            | USD                |
      | dbs_assurance_outcome           | Active             |
      | dbs_provider                    | 150                |
      | dbs_verification_method         | REF12345           |
      | dbs_pedigree                    | 1995-05-15         |
      | dbs_last_refresh                | Gold               |

    Scenario: Verify credentials data - Identity
    When user clicks on expand button for DBS supporting information
    Then user verify the credentials details should match
      | Attribute                  | Expected Value     |
      | id_first_name              | JACOB SEBASTIAN    |
      | id_last_name               | SMITH              |
      | id_dob                     | 6 July 1999        |
      | id_legal gender            | Active             |
      | id_address                 | Admin              |
      | id_origin                  | New York           |
      | id_assurance policy        | USA                |
      | id_assurance outcome       | 10001              |
      | id_provider                | 2025-03-26 12:30:00|
      | id_verifier                | Premium            |
      | id_verification method     | 30                 |
      | id_pedigree                | Male               |
      | id_last_refresh            | English            |

  Scenario: Verify credentials data - right to work
    When user clicks on expand button for DBS supporting information
    Then user verify the credentials details should match
      | Attribute                   | Expected Value     |
      | rtw_legal_first_name              | JACOB SEBASTIAN    |
      | rtw_legal_surname               | SMITH              |
      | rtw_birth_date                     | 6 July 1999        |
      | rtw_identity_verified    | Active             |
      | rtw_evidence_checked_by             | Admin              |
      | rtw_gpg45_profile       | New York           |
      | rtw_origin           | USA                |
      | rtw_assurance_policy          | 10001              |
      | rtw_assurance_outcome                      | 2025-03-26 12:30:00|
      | rtw_provider         | Premium            |
      | rtw_verifier      | 30                 |
      | rtw_verification_method            | Male               |
      | rtw_pedigree                   | English            |
      | rtw_last_refresh               |     6 March 2025   |
