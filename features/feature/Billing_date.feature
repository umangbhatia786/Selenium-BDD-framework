Feature: Excalibur Web change BD

@BD
Scenario Outline: To change Billing date
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We open Billing date Window

Examples:
    | CTN          | 
    | xxxxxxxxxxxx |