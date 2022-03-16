Feature: Excalibur Web PORT IN 

@PORTIN
Scenario Outline: To port in
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We give PAC as <PAC> and Ported CTN as <PCTN>
 

Examples:
    | CTN          |  PAC        | PCTN        |
    | yyyyyyyyyyy  |  vvvvvvvvv  | xxxxxxxxxxx |