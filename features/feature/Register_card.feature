Feature: Excalibur Web Register cards

@RC
Scenario Outline: To Register cards
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We open Register cards Window and enter Card number 

Examples:
    | CTN          |     
    | xxxxxxxxxxx  |