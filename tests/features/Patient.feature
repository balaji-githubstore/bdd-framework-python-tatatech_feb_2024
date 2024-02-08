@patient
Feature: Patient
  In order to maintain the patients record
  as a user
  I want to add, edit, delete the patient details

  @addpatient
  Scenario Outline: Add Valid Patient Record
    Given I have browser with OpenEMR application
    When I enter username as "<username>"
    And I enter password as "<password>"
    And I click on login
    And I click on Patient menu
    And I click on New Search menu
    And I fill the patient details form
      | firstname | lastname   | dob   | gender   |
      | <fname>   | <lastname> | <dob> | <gender> |
    And I click on create new patient
    And I click on confirm create new patient
    And I handle the alert box
    And I close the birthday popup if available
    Then I should get the added patient record as "<expected_patient_name>"
    Examples:
      | username | password | fname | lastname | dob        | gender | expected_patient_name                |
      | admin    | pass     | john  | wick     | 2024-02-08 | Female | Medical Record Dashboard - john wick |
      | admin    | pass     | kim   | saul     | 2024-02-08 | Male   | Medical Record Dashboard - kim saul  |

#
#  @addpatient
#  Scenario: Add Valid Patient Record
#    Given I have browser with OpenEMR application
#    When I enter username as "admin"
#    And I enter password as "pass"
#    And I click on login
#    And I click on Patient menu
#    And I click on New Search menu
#    And I fill the patient details form
#      | firstname | lastname | dob        | gender |
#      | john      | wick     | 2024-02-08 | Male   |
#    And I click on create new patient
#    And I click on confirm create new patient
#    And I handle the alert box
#    And I close the birthday popup if available
#    Then I should get the added patient record as "Medical Record Dashboard - john wick"

