Feature: Excalibur Web Billing Validation

@BV
Scenario Outline: For Billing Validation
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We open Bill 

Examples:
    | CTN          | 
    | xxxxxxxxxxx  |