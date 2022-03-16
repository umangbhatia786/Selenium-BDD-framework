Feature: Excalibur Web CTN Refresh

@RF
Scenario Outline: To Refresh a CTN
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We open Refresh_CTN Window and Refresh with Reason as <reason> 

Examples:
    | CTN          | reason | 
    | xxxxxxxxxxx  | bbb    |
  