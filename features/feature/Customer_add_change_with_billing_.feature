Feature: Excalibur Web change address

@CAB
Scenario Outline: To change CAB
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We open change CAB Window and enter new address <address>

Examples:
    | CTN          | address      |
    | xxxxxxxxxxxx | vvvvvvv      |



@BAC
Scenario Outline: To change BAC
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We open change BAC Window and enter new address <bill_address>

Examples:
    | CTN          | bill_address |
    | xxxxxxxxxxx  | vvvvvvv      |