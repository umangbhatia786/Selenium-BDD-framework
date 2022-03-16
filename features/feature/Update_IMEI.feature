Feature: Excalibur Web Update IMEI

@UIMEI
Scenario Outline: To Update IMEI
  Given I Navigate To BAN Window
  Then We enter the CTN <CTN>
  Then We open IMEI Update tab
  Then We give Sales Entity as <SE>
  Then We open Update_IMEI Window give reason as <reason> and Enter IMEI <IMEI> 

Examples:
    | CTN          | SE     | reason    | IMEI           |
    | gggggggggg  | yyyyyy   | uuuuuuu      | guii|