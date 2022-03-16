Feature: Excalibur Web CTN Suspension

@RSP
Scenario: To Resume Suspension for a Suspended CTN
  Given I Navigate To BAN Window
  Then We enter the suspended CTN
  Then We Open Resume Suspend Window and Click Ok

  