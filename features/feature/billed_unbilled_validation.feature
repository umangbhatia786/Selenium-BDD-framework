Feature: Excalibur Web Billed unbilled Validation

@BLU
Scenario Outline: For Billed unbilled Validation
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We open Billed calls

Examples:
    | CTN          | 
    | xxxxxxxxxxxxx  |