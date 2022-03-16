Feature: Excalibur Web change CC

@CHC
Scenario Outline: To change CC
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We open change_CC Window

Examples:
    | CTN          | 
    | xxxxxxxxxxx  |