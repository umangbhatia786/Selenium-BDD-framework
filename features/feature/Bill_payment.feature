Feature: Excalibur Web Bill Payment

@BP
Scenario Outline: For Bill Payment
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We open Bill Payment 

Examples:
    | CTN          | 
    | xxxxxxxxxx  |