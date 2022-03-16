Feature: Excalibur Web Resume CTN Cancel

@RCAN
Scenario Outline: To Resume Cancel a CTN
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We open Resume_Cancel_CTN Window and Resume_Cancel with Reason as <reason>
  Then We give Sales Entity as <SE>

Examples:
    | CTN          | reason | SE     | 
    | vvvvvvvvvv  | jjjjjj   | ooooo   |   