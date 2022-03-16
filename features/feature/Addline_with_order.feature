Feature: Addline with Order 

@UPGRADEwithorder
Scenario Outline: Verify User is able to Upgrade with order 
  Given We open the Application Information Window
  Then We enter form details as <app_type>, <conditions_no>, <sales_entity> and <account_type>
  Then Open Application Wizard and set CTN as <ctn>
  Then Set Postal Code as <postal_code>
  Then Fill Name+Address Form
  

Examples:
    | app_type | conditions_no | sales_entity | account_type | postal_code | ctn         |
    | ii     | 00            | hg         | ab           | cd      | xxxxxxxxxxx |


