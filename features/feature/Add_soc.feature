Feature: Excalibur Web To add SOC

@ASOC
Scenario Outline: To add SOC
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We open add soc and enter SOC name <SOC>

Examples:
    | CTN          | SOC      |
    | xxxxxxxxxxx  | YCAP1000 |



@AF
Scenario Outline: To change Billing date
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We open add soc and enter Feature name <Feature>

Examples:
    | CTN          | Feature    |
    | xxxxxxxxxxx  | PREM       |
