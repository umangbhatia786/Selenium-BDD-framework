Feature: Excalibur Web Add ATP

@ATP
Scenario Outline: To add ATP 
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We open ATP Window 
  Then We give Sales Entity as <SE>
  Then WE add a device 

Examples:
    | CTN          | SE   |
    | xxxxxxxxxxxx | CUST |