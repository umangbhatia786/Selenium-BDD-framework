Feature: Excalibur Web Replace sim

@RS
Scenario Outline: To Replace sim
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We open Replace sim and enter IMEI number as <IMEI1> 

Examples:
    | CTN          | IMEI1                 | 
    | xxxxxxxxxxxx  | mmmmmmmmmmmmmmmmmmmm  |