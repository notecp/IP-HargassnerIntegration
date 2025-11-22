"""Firmware version templates for Hargassner boilers.

IMPORTANT: When adding a new firmware version:
1. Add the XML template to FIRMWARE_TEMPLATES below
2. Add the version string to FIRMWARE_VERSIONS in const.py
3. Run tools/parameter_validator.py to check consistency
4. Add parameter descriptions to PARAMETER_DESCRIPTIONS if needed
"""
from __future__ import annotations

from typing import Final

# XML templates for different firmware versions
# These define the structure and order of telnet message parameters
#
# To add support for a new firmware version:
# 1. Use tools/daq_parser.py to extract the DAQPRJ template from a DAQ file
# 2. Add it here with a descriptive version key (e.g., "NANO_V15X")
# 3. Update FIRMWARE_VERSIONS in const.py

FIRMWARE_TEMPLATES: Final[dict[str, str]] = {
    "V14_1HAR_q1": """<DAQPRJ><ANALOG><CHANNEL id='0' name='ZK' dop='0'/><CHANNEL id='1' name='O2' unit='%'/><CHANNEL id='2' name='Abgas' unit='°C'/><CHANNEL id='3' name='Kessel' unit='°C'/><CHANNEL id='4' name='Kesselsoll' unit='°C'/><CHANNEL id='5' name='Puff_o' unit='°C'/><CHANNEL id='6' name='Puff_u' unit='°C'/><CHANNEL id='7' name='Lambda' dop='2'/><CHANNEL id='8' name='Leist' unit='%'/><CHANNEL id='9' name='Außen' unit='°C'/><CHANNEL id='10' name='Saug' unit='mbar'/><CHANNEL id='11' name='Puffer_s_oben' unit='°C'/><CHANNEL id='12' name='Puffer_s_unten' unit='°C'/><CHANNEL id='13' name='Boiler' unit='°C'/><CHANNEL id='14' name='Boilersoll' unit='°C'/><CHANNEL id='15' name='Solar' unit='°C'/><CHANNEL id='16' name='Kollektor' unit='°C'/><CHANNEL id='17' name='Puff_aS_oben' unit='°C'/><CHANNEL id='18' name='Puff_aS_unten' unit='°C'/><CHANNEL id='19' name='Puff_Füllgrad' dop='0'/><CHANNEL id='20' name='Puffer_soll_oben' unit='°C'/><CHANNEL id='21' name='Puffer_soll_unten' unit='°C'/><CHANNEL id='22' name='Max_Anf_Kessel' unit='°C'/><CHANNEL id='23' name='HK1_VL' unit='°C'/><CHANNEL id='24' name='HK1_VLsoll' unit='°C'/><CHANNEL id='25' name='HK1_RT' unit='°C'/><CHANNEL id='26' name='HK1_RTsoll' unit='°C'/><CHANNEL id='27' name='HK2_VL' unit='°C'/><CHANNEL id='28' name='HK2_VLsoll' unit='°C'/><CHANNEL id='29' name='HK2_RT' unit='°C'/><CHANNEL id='30' name='HK2_RTsoll' unit='°C'/><CHANNEL id='31' name='HK3_VL' unit='°C'/><CHANNEL id='32' name='HK3_VLsoll' unit='°C'/><CHANNEL id='33' name='HK3_RT' unit='°C'/><CHANNEL id='34' name='HK3_RTsoll' unit='°C'/><CHANNEL id='35' name='Raumsoll_Set' unit='°C'/><CHANNEL id='36' name='HK4_VL' unit='°C'/><CHANNEL id='37' name='HK4_VLsoll' unit='°C'/><CHANNEL id='38' name='HK4_RT' unit='°C'/><CHANNEL id='39' name='HK4_RTsoll' unit='°C'/><CHANNEL id='40' name='HK1_Ventilpos' unit='%'/><CHANNEL id='41' name='HK2_Ventilpos' unit='%'/><CHANNEL id='42' name='HK3_Ventilpos' unit='%'/><CHANNEL id='43' name='HK4_Ventilpos' unit='%'/><CHANNEL id='44' name='Pellets_Vorrat_kg' unit='kg'/><CHANNEL id='45' name='Pellets_Verb_kg' dop='2' unit='kg'/><CHANNEL id='46' name='Austrag' unit='%'/><CHANNEL id='47' name='AN11' unit='°C'/><CHANNEL id='48' name='AN12' unit='°C'/><CHANNEL id='49' name='AN13' unit='°C'/><CHANNEL id='50' name='AN14' unit='°C'/><CHANNEL id='51' name='AN15' unit='°C'/><CHANNEL id='52' name='AN16' unit='°C'/><CHANNEL id='53' name='Netzteil' unit='V'/><CHANNEL id='54' name='Diff_HK1' dop='0'/><CHANNEL id='55' name='Diff_HK2' dop='0'/><CHANNEL id='56' name='Diff_HK3' dop='0'/><CHANNEL id='57' name='Diff_HK4' dop='0'/><CHANNEL id='58' name='HK1_PARTY' dop='0'/><CHANNEL id='59' name='HK1_FERIEN' dop='0'/><CHANNEL id='60' name='HK1_SPARBETRIEB' dop='0'/><CHANNEL id='61' name='HK2_PARTY' dop='0'/><CHANNEL id='62' name='HK2_FERIEN' dop='0'/><CHANNEL id='63' name='HK2_SPARBETRIEB' dop='0'/><CHANNEL id='64' name='HK3_PARTY' dop='0'/><CHANNEL id='65' name='HK3_FERIEN' dop='0'/><CHANNEL id='66' name='HK3_SPARBETRIEB' dop='0'/><CHANNEL id='67' name='HK4_PARTY' dop='0'/><CHANNEL id='68' name='HK4_FERIEN' dop='0'/><CHANNEL id='69' name='HK4_SPARBETRIEB' dop='0'/><CHANNEL id='70' name='BETRIEBSST' dop='0'/><CHANNEL id='71' name='FEHLERCODE' dop='0'/><CHANNEL id='72' name='STATUS_A' dop='0'/><CHANNEL id='73' name='STATUS_D' dop='0'/><CHANNEL id='74' name='Asche_KG' dop='1' unit='kg'/><CHANNEL id='75' name='PARTYTIME_HK1' dop='0'/><CHANNEL id='76' name='PARTYTIME_HK2' dop='0'/><CHANNEL id='77' name='PARTYTIME_HK3' dop='0'/><CHANNEL id='78' name='PARTYTIME_HK4' dop='0'/><CHANNEL id='79' name='SYSTEMZEIT_MIN' dop='0'/><CHANNEL id='80' name='SYSTEMZEIT_STD' dop='0'/><CHANNEL id='81' name='SYSTEMZEIT_TAG' dop='0'/><CHANNEL id='82' name='SYSTEMZEIT_MONAT' dop='0'/><CHANNEL id='83' name='SYSTEMZEIT_JAHR' dop='0'/><CHANNEL id='84' name='BETRIEBSST_TXT' unit='TEXT'/><CHANNEL id='85' name='Handy_Vorwahl' dop='0'/><CHANNEL id='86' name='Handy_Rufnummer' dop='0'/><CHANNEL id='87' name='TWW_Freigabe' dop='0'/><CHANNEL id='88' name='Kessel_Vorlauf' unit='°C'/><CHANNEL id='89' name='Kessel_Ruecklauf' unit='°C'/><CHANNEL id='90' name='Diff_HK5' dop='0'/><CHANNEL id='91' name='Diff_HK6' dop='0'/><CHANNEL id='92' name='Diff_HK7' dop='0'/><CHANNEL id='93' name='Diff_HK8' dop='0'/><CHANNEL id='94' name='HK5_VL' unit='°C'/><CHANNEL id='95' name='HK5_VLsoll' unit='°C'/><CHANNEL id='96' name='HK5_RT' unit='°C'/><CHANNEL id='97' name='HK5_RTsoll' unit='°C'/><CHANNEL id='98' name='HK6_VL' unit='°C'/><CHANNEL id='99' name='HK6_VLsoll' unit='°C'/><CHANNEL id='100' name='HK6_RT' unit='°C'/><CHANNEL id='101' name='HK6_RTsoll' unit='°C'/><CHANNEL id='102' name='HK7_VL' unit='°C'/><CHANNEL id='103' name='HK7_VLsoll' unit='°C'/><CHANNEL id='104' name='HK7_RT' unit='°C'/><CHANNEL id='105' name='HK7_RTsoll' unit='°C'/><CHANNEL id='106' name='HK8_VL' unit='°C'/><CHANNEL id='107' name='HK8_VLsoll' unit='°C'/><CHANNEL id='108' name='HK8_RT' unit='°C'/><CHANNEL id='109' name='HK8_RTsoll' unit='°C'/><CHANNEL id='110' name='MODBUS_STOERUNG' dop='0'/><CHANNEL id='111' name='Status' dop='0'/></ANALOG><DIGITAL><CHANNEL id='1000' name='M1_Kes_Ladepump' dop='0' bit='0'/><CHANNEL id='1001' name='M2_Boilerpumpe' dop='0' bit='1'/><CHANNEL id='1002' name='M3_Zubringer' dop='0' bit='2'/><CHANNEL id='1003' name='M4_Einschubmotor' dop='0' bit='3'/><CHANNEL id='1004' name='M5_Entaschung' dop='0' bit='4'/><CHANNEL id='1005' name='M6_E_Filter' dop='0' bit='5'/><CHANNEL id='1006' name='M7_Saugzug' dop='0' bit='6'/><CHANNEL id='1007' name='M8_Zündung' dop='0' bit='7'/><CHANNEL id='1008' name='M9_HK1_Pumpe' dop='0' bit='8'/><CHANNEL id='1009' name='M10_HK1_Mischer_Auf' dop='0' bit='9'/><CHANNEL id='1010' name='M11_HK1_Mischer_Zu' dop='0' bit='10'/><CHANNEL id='1011' name='M12_HK2_Pumpe' dop='0' bit='11'/><CHANNEL id='1012' name='M13_HK2_Mischer_Auf' dop='0' bit='12'/><CHANNEL id='1013' name='M14_HK2_Mischer_Zu' dop='0' bit='13'/><CHANNEL id='1014' name='M15_Pufferpumpe' dop='0' bit='14'/><CHANNEL id='1015' name='M16_Solar' dop='0' bit='15'/><CHANNEL id='1016' name='Stoerung' dop='0' bit='0'/><CHANNEL id='1017' name='Handbetrieb' dop='0' bit='1'/><CHANNEL id='1018' name='Automatik' dop='0' bit='2'/><CHANNEL id='1019' name='Heizen' dop='0' bit='3'/><CHANNEL id='1020' name='Boiler' dop='0' bit='4'/><CHANNEL id='1021' name='M17_HK3_Pumpe' dop='0' bit='5'/><CHANNEL id='1022' name='M18_HK3_Mischer_Auf' dop='0' bit='6'/><CHANNEL id='1023' name='M19_HK3_Mischer_Zu' dop='0' bit='7'/><CHANNEL id='1024' name='M20_HK4_Pumpe' dop='0' bit='8'/><CHANNEL id='1025' name='M21_HK4_Mischer_Auf' dop='0' bit='9'/><CHANNEL id='1026' name='M22_HK4_Mischer_Zu' dop='0' bit='10'/><CHANNEL id='1027' name='M23_Zirkulationspumpe' dop='0' bit='11'/><CHANNEL id='1028' name='HK1_Modus_Auto' dop='0' bit='12'/><CHANNEL id='1029' name='HK1_Modus_Party' dop='0' bit='13'/><CHANNEL id='1030' name='HK1_Modus_Ferien' dop='0' bit='14'/><CHANNEL id='1031' name='HK1_Modus_Sparbetrieb' dop='0' bit='15'/><CHANNEL id='1032' name='E1_Aschelade_Endschalter' dop='0' bit='0'/><CHANNEL id='1033' name='E2_Türkontaktschalter' dop='0' bit='1'/><CHANNEL id='1034' name='E3_Kesseltemp_Stoerung' dop='0' bit='2'/><CHANNEL id='1035' name='E4_Silo_Fuellstandsmelder' dop='0' bit='3'/><CHANNEL id='1036' name='E5_Ext_Anforderung' dop='0' bit='4'/><CHANNEL id='1037' name='E6_Funk_Raumthermostat' dop='0' bit='5'/><CHANNEL id='1038' name='E7_Stoermeldung_Kessel_gelb' dop='0' bit='6'/><CHANNEL id='1039' name='E8_Stoermeldung_Kessel_rot' dop='0' bit='7'/><CHANNEL id='1040' name='E9_Ext_HK1_Anforderung' dop='0' bit='8'/><CHANNEL id='1041' name='E10_Ext_HK2_Anforderung' dop='0' bit='9'/><CHANNEL id='1042' name='E11_Saugturbine_Stoerung' dop='0' bit='10'/><CHANNEL id='1043' name='E12_Fehlerstrom_Schutzschalter' dop='0' bit='11'/><CHANNEL id='1044' name='E13_Pufferspeicher_Anforderung' dop='0' bit='12'/><CHANNEL id='1045' name='E14_Ext_HK3_Anforderung' dop='0' bit='13'/><CHANNEL id='1046' name='E15_Ext_HK4_Anforderung' dop='0' bit='14'/><CHANNEL id='1047' name='E16_Pelletbehaelter_fast_leer' dop='0' bit='15'/><CHANNEL id='1048' name='HK2_Modus_Auto' dop='0' bit='0'/><CHANNEL id='1049' name='HK2_Modus_Party' dop='0' bit='1'/><CHANNEL id='1050' name='HK2_Modus_Ferien' dop='0' bit='2'/><CHANNEL id='1051' name='HK2_Modus_Sparbetrieb' dop='0' bit='3'/><CHANNEL id='1052' name='HK3_Modus_Auto' dop='0' bit='4'/><CHANNEL id='1053' name='HK3_Modus_Party' dop='0' bit='5'/><CHANNEL id='1054' name='HK3_Modus_Ferien' dop='0' bit='6'/><CHANNEL id='1055' name='HK3_Modus_Sparbetrieb' dop='0' bit='7'/><CHANNEL id='1056' name='HK4_Modus_Auto' dop='0' bit='8'/><CHANNEL id='1057' name='HK4_Modus_Party' dop='0' bit='9'/><CHANNEL id='1058' name='HK4_Modus_Ferien' dop='0' bit='10'/><CHANNEL id='1059' name='HK4_Modus_Sparbetrieb' dop='0' bit='11'/><CHANNEL id='1060' name='Stoerung_vorhanden' dop='0' bit='12'/><CHANNEL id='1061' name='M24_Reserve_1' dop='0' bit='13'/><CHANNEL id='1062' name='M25_Reserve_2' dop='0' bit='14'/><CHANNEL id='1063' name='M26_Reserve_3' dop='0' bit='15'/><CHANNEL id='1064' name='HK1_Abgesenkt' dop='0' bit='0'/><CHANNEL id='1065' name='HK1_Normal' dop='0' bit='1'/><CHANNEL id='1066' name='HK1_Party_Countdown' dop='0' bit='2'/><CHANNEL id='1067' name='HK1_Ferien_Programm' dop='0' bit='3'/><CHANNEL id='1068' name='HK1_Sommerzeit' dop='0' bit='4'/><CHANNEL id='1069' name='HK2_Abgesenkt' dop='0' bit='5'/><CHANNEL id='1070' name='HK2_Normal' dop='0' bit='6'/><CHANNEL id='1071' name='HK2_Party_Countdown' dop='0' bit='7'/><CHANNEL id='1072' name='HK2_Ferien_Programm' dop='0' bit='8'/><CHANNEL id='1073' name='HK2_Sommerzeit' dop='0' bit='9'/><CHANNEL id='1074' name='HK3_Abgesenkt' dop='0' bit='10'/><CHANNEL id='1075' name='HK3_Normal' dop='0' bit='11'/><CHANNEL id='1076' name='HK3_Party_Countdown' dop='0' bit='12'/><CHANNEL id='1077' name='HK3_Ferien_Programm' dop='0' bit='13'/><CHANNEL id='1078' name='HK3_Sommerzeit' dop='0' bit='14'/><CHANNEL id='1079' name='HK4_Abgesenkt' dop='0' bit='15'/><CHANNEL id='1080' name='HK4_Normal' dop='0' bit='0'/><CHANNEL id='1081' name='HK4_Party_Countdown' dop='0' bit='1'/><CHANNEL id='1082' name='HK4_Ferien_Programm' dop='0' bit='2'/><CHANNEL id='1083' name='HK4_Sommerzeit' dop='0' bit='3'/><CHANNEL id='1084' name='M27_HK5_Pumpe' dop='0' bit='4'/><CHANNEL id='1085' name='M28_HK5_Mischer_Auf' dop='0' bit='5'/><CHANNEL id='1086' name='M29_HK5_Mischer_Zu' dop='0' bit='6'/><CHANNEL id='1087' name='M30_HK6_Pumpe' dop='0' bit='7'/><CHANNEL id='1088' name='M31_HK6_Mischer_Auf' dop='0' bit='8'/><CHANNEL id='1089' name='M32_HK6_Mischer_Zu' dop='0' bit='9'/><CHANNEL id='1090' name='M33_HK7_Pumpe' dop='0' bit='10'/><CHANNEL id='1091' name='M34_HK7_Mischer_Auf' dop='0' bit='11'/><CHANNEL id='1092' name='M35_HK7_Mischer_Zu' dop='0' bit='12'/><CHANNEL id='1093' name='M36_HK8_Pumpe' dop='0' bit='13'/><CHANNEL id='1094' name='M37_HK8_Mischer_Auf' dop='0' bit='14'/><CHANNEL id='1095' name='M38_HK8_Mischer_Zu' dop='0' bit='15'/><CHANNEL id='1096' name='HK5_Modus_Auto' dop='0' bit='0'/><CHANNEL id='1097' name='HK5_Modus_Party' dop='0' bit='1'/><CHANNEL id='1098' name='HK5_Modus_Ferien' dop='0' bit='2'/><CHANNEL id='1099' name='HK5_Modus_Sparbetrieb' dop='0' bit='3'/><CHANNEL id='1100' name='HK6_Modus_Auto' dop='0' bit='4'/><CHANNEL id='1101' name='HK6_Modus_Party' dop='0' bit='5'/><CHANNEL id='1102' name='HK6_Modus_Ferien' dop='0' bit='6'/><CHANNEL id='1103' name='HK6_Modus_Sparbetrieb' dop='0' bit='7'/><CHANNEL id='1104' name='HK7_Modus_Auto' dop='0' bit='8'/><CHANNEL id='1105' name='HK7_Modus_Party' dop='0' bit='9'/><CHANNEL id='1106' name='HK7_Modus_Ferien' dop='0' bit='10'/><CHANNEL id='1107' name='HK7_Modus_Sparbetrieb' dop='0' bit='11'/><CHANNEL id='1108' name='HK8_Modus_Auto' dop='0' bit='12'/><CHANNEL id='1109' name='HK8_Modus_Party' dop='0' bit='13'/><CHANNEL id='1110' name='HK8_Modus_Ferien' dop='0' bit='14'/><CHANNEL id='1111' name='HK8_Modus_Sparbetrieb' dop='0' bit='15'/></DIGITAL></DAQPRJ>""",
}

# Complete parameter descriptions for all parameters in DAQPRJ templates
PARAMETER_DESCRIPTIONS: Final[dict[str, str]] = {
    # Boiler core parameters (analog 0-10)
    "ZK": "Boiler state",
    "O2": "O2 level",
    "Abgas": "Smoke gas temperature",
    "Kessel": "Boiler temperature",
    "Kesselsoll": "Boiler temperature target",
    "Puff_o": "Buffer temperature top",
    "Puff_u": "Buffer temperature bottom",
    "Lambda": "Lambda value",
    "Leist": "Output power",
    "Außen": "Outside temperature",
    "Saug": "Draft pressure",

    # Buffer temperatures (analog 11-22)
    "Puffer_s_oben": "Buffer setpoint top",
    "Puffer_s_unten": "Buffer setpoint bottom",
    "Boiler": "Hot water boiler temperature",
    "Boilersoll": "Hot water boiler target",
    "Solar": "Solar temperature",
    "Kollektor": "Solar collector temperature",
    "Puff_aS_oben": "Buffer alternative sensor top",
    "Puff_aS_unten": "Buffer alternative sensor bottom",
    "Puff_Füllgrad": "Buffer fill level",
    "Puffer_soll_oben": "Buffer target top",
    "Puffer_soll_unten": "Buffer target bottom",
    "Max_Anf_Kessel": "Maximum boiler request",

    # Heating circuits HK1-HK4 (analog 23-43)
    "HK1_VL": "Heating circuit 1 flow temperature",
    "HK1_VLsoll": "Heating circuit 1 flow target",
    "HK1_RT": "Heating circuit 1 room temperature",
    "HK1_RTsoll": "Heating circuit 1 room target",
    "HK2_VL": "Heating circuit 2 flow temperature",
    "HK2_VLsoll": "Heating circuit 2 flow target",
    "HK2_RT": "Heating circuit 2 room temperature",
    "HK2_RTsoll": "Heating circuit 2 room target",
    "HK3_VL": "Heating circuit 3 flow temperature",
    "HK3_VLsoll": "Heating circuit 3 flow target",
    "HK3_RT": "Heating circuit 3 room temperature",
    "HK3_RTsoll": "Heating circuit 3 room target",
    "Raumsoll_Set": "Room temperature setpoint",
    "HK4_VL": "Heating circuit 4 flow temperature",
    "HK4_VLsoll": "Heating circuit 4 flow target",
    "HK4_RT": "Heating circuit 4 room temperature",
    "HK4_RTsoll": "Heating circuit 4 room target",
    "HK1_Ventilpos": "Heating circuit 1 valve position",
    "HK2_Ventilpos": "Heating circuit 2 valve position",
    "HK3_Ventilpos": "Heating circuit 3 valve position",
    "HK4_Ventilpos": "Heating circuit 4 valve position",

    # Pellet storage (analog 44-46)
    "Pellets_Vorrat_kg": "Pellet stock",
    "Pellets_Verb_kg": "Pellet consumption",
    "Austrag": "Discharge rate",

    # Analog inputs (analog 47-53)
    "AN11": "Analog input 11",
    "AN12": "Analog input 12",
    "AN13": "Analog input 13",
    "AN14": "Analog input 14",
    "AN15": "Analog input 15",
    "AN16": "Analog input 16",
    "Netzteil": "Power supply voltage",

    # Heating circuit differences (analog 54-57)
    "Diff_HK1": "Heating circuit 1 differential",
    "Diff_HK2": "Heating circuit 2 differential",
    "Diff_HK3": "Heating circuit 3 differential",
    "Diff_HK4": "Heating circuit 4 differential",

    # Heating circuit modes (analog 58-69)
    "HK1_PARTY": "Heating circuit 1 party mode",
    "HK1_FERIEN": "Heating circuit 1 vacation mode",
    "HK1_SPARBETRIEB": "Heating circuit 1 economy mode",
    "HK2_PARTY": "Heating circuit 2 party mode",
    "HK2_FERIEN": "Heating circuit 2 vacation mode",
    "HK2_SPARBETRIEB": "Heating circuit 2 economy mode",
    "HK3_PARTY": "Heating circuit 3 party mode",
    "HK3_FERIEN": "Heating circuit 3 vacation mode",
    "HK3_SPARBETRIEB": "Heating circuit 3 economy mode",
    "HK4_PARTY": "Heating circuit 4 party mode",
    "HK4_FERIEN": "Heating circuit 4 vacation mode",
    "HK4_SPARBETRIEB": "Heating circuit 4 economy mode",

    # System status (analog 70-74)
    "BETRIEBSST": "Operating state",
    "FEHLERCODE": "Error code",
    "STATUS_A": "Status A",
    "STATUS_D": "Status D",
    "Asche_KG": "Ash weight",

    # Party time counters (analog 75-78)
    "PARTYTIME_HK1": "Heating circuit 1 party time remaining",
    "PARTYTIME_HK2": "Heating circuit 2 party time remaining",
    "PARTYTIME_HK3": "Heating circuit 3 party time remaining",
    "PARTYTIME_HK4": "Heating circuit 4 party time remaining",

    # System time (analog 79-84)
    "SYSTEMZEIT_MIN": "System time minutes",
    "SYSTEMZEIT_STD": "System time hours",
    "SYSTEMZEIT_TAG": "System time day",
    "SYSTEMZEIT_MONAT": "System time month",
    "SYSTEMZEIT_JAHR": "System time year",
    "BETRIEBSST_TXT": "Operating state text",

    # Phone settings (analog 85-87)
    "Handy_Vorwahl": "Mobile phone area code",
    "Handy_Rufnummer": "Mobile phone number",
    "TWW_Freigabe": "Hot water enable",

    # Boiler flow/return (analog 88-89)
    "Kessel_Vorlauf": "Boiler flow temperature",
    "Kessel_Ruecklauf": "Boiler return temperature",

    # Heating circuits HK5-HK8 differentials (analog 90-93)
    "Diff_HK5": "Heating circuit 5 differential",
    "Diff_HK6": "Heating circuit 6 differential",
    "Diff_HK7": "Heating circuit 7 differential",
    "Diff_HK8": "Heating circuit 8 differential",

    # Heating circuits HK5-HK8 temperatures (analog 94-109)
    "HK5_VL": "Heating circuit 5 flow temperature",
    "HK5_VLsoll": "Heating circuit 5 flow target",
    "HK5_RT": "Heating circuit 5 room temperature",
    "HK5_RTsoll": "Heating circuit 5 room target",
    "HK6_VL": "Heating circuit 6 flow temperature",
    "HK6_VLsoll": "Heating circuit 6 flow target",
    "HK6_RT": "Heating circuit 6 room temperature",
    "HK6_RTsoll": "Heating circuit 6 room target",
    "HK7_VL": "Heating circuit 7 flow temperature",
    "HK7_VLsoll": "Heating circuit 7 flow target",
    "HK7_RT": "Heating circuit 7 room temperature",
    "HK7_RTsoll": "Heating circuit 7 room target",
    "HK8_VL": "Heating circuit 8 flow temperature",
    "HK8_VLsoll": "Heating circuit 8 flow target",
    "HK8_RT": "Heating circuit 8 room temperature",
    "HK8_RTsoll": "Heating circuit 8 room target",

    # System status (analog 110-111)
    "MODBUS_STOERUNG": "Modbus error",
    "Status": "System status",

    # Digital outputs - Motors and pumps (digital 1000-1015)
    "M1_Kes_Ladepump": "Boiler charging pump",
    "M2_Boilerpumpe": "Hot water pump",
    "M3_Zubringer": "Feeder",
    "M4_Einschubmotor": "Insert motor",
    "M5_Entaschung": "Ash removal",
    "M6_E_Filter": "E-filter",
    "M7_Saugzug": "Induced draft fan",
    "M8_Zündung": "Ignition",
    "M9_HK1_Pumpe": "Heating circuit 1 pump",
    "M10_HK1_Mischer_Auf": "Heating circuit 1 mixer open",
    "M11_HK1_Mischer_Zu": "Heating circuit 1 mixer close",
    "M12_HK2_Pumpe": "Heating circuit 2 pump",
    "M13_HK2_Mischer_Auf": "Heating circuit 2 mixer open",
    "M14_HK2_Mischer_Zu": "Heating circuit 2 mixer close",
    "M15_Pufferpumpe": "Buffer pump",
    "M16_Solar": "Solar pump",

    # System states (digital 1016-1027)
    "Stoerung": "Error",
    "Handbetrieb": "Manual mode",
    "Automatik": "Automatic mode",
    "Heizen": "Heating",
    "Boiler": "Hot water mode",
    "M17_HK3_Pumpe": "Heating circuit 3 pump",
    "M18_HK3_Mischer_Auf": "Heating circuit 3 mixer open",
    "M19_HK3_Mischer_Zu": "Heating circuit 3 mixer close",
    "M20_HK4_Pumpe": "Heating circuit 4 pump",
    "M21_HK4_Mischer_Auf": "Heating circuit 4 mixer open",
    "M22_HK4_Mischer_Zu": "Heating circuit 4 mixer close",
    "M23_Zirkulationspumpe": "Circulation pump",

    # HK1 modes (digital 1028-1031)
    "HK1_Modus_Auto": "Heating circuit 1 mode auto",
    "HK1_Modus_Party": "Heating circuit 1 mode party",
    "HK1_Modus_Ferien": "Heating circuit 1 mode vacation",
    "HK1_Modus_Sparbetrieb": "Heating circuit 1 mode economy",

    # Digital inputs (digital 1032-1047)
    "E1_Aschelade_Endschalter": "Ash drawer limit switch",
    "E2_Türkontaktschalter": "Door contact switch",
    "E3_Kesseltemp_Stoerung": "Boiler temperature error",
    "E4_Silo_Fuellstandsmelder": "Silo level indicator",
    "E5_Ext_Anforderung": "External request",
    "E6_Funk_Raumthermostat": "Wireless room thermostat",
    "E7_Stoermeldung_Kessel_gelb": "Boiler error yellow",
    "E8_Stoermeldung_Kessel_rot": "Boiler error red",
    "E9_Ext_HK1_Anforderung": "External heating circuit 1 request",
    "E10_Ext_HK2_Anforderung": "External heating circuit 2 request",
    "E11_Saugturbine_Stoerung": "Induced draft fan error",
    "E12_Fehlerstrom_Schutzschalter": "Residual current circuit breaker",
    "E13_Pufferspeicher_Anforderung": "Buffer storage request",
    "E14_Ext_HK3_Anforderung": "External heating circuit 3 request",
    "E15_Ext_HK4_Anforderung": "External heating circuit 4 request",
    "E16_Pelletbehaelter_fast_leer": "Pellet container almost empty",

    # HK2-HK4 modes (digital 1048-1063)
    "HK2_Modus_Auto": "Heating circuit 2 mode auto",
    "HK2_Modus_Party": "Heating circuit 2 mode party",
    "HK2_Modus_Ferien": "Heating circuit 2 mode vacation",
    "HK2_Modus_Sparbetrieb": "Heating circuit 2 mode economy",
    "HK3_Modus_Auto": "Heating circuit 3 mode auto",
    "HK3_Modus_Party": "Heating circuit 3 mode party",
    "HK3_Modus_Ferien": "Heating circuit 3 mode vacation",
    "HK3_Modus_Sparbetrieb": "Heating circuit 3 mode economy",
    "HK4_Modus_Auto": "Heating circuit 4 mode auto",
    "HK4_Modus_Party": "Heating circuit 4 mode party",
    "HK4_Modus_Ferien": "Heating circuit 4 mode vacation",
    "HK4_Modus_Sparbetrieb": "Heating circuit 4 mode economy",
    "Stoerung_vorhanden": "Error present",
    "M24_Reserve_1": "Reserve output 1",
    "M25_Reserve_2": "Reserve output 2",
    "M26_Reserve_3": "Reserve output 3",

    # HK1-HK4 states (digital 1064-1083)
    "HK1_Abgesenkt": "Heating circuit 1 lowered",
    "HK1_Normal": "Heating circuit 1 normal",
    "HK1_Party_Countdown": "Heating circuit 1 party countdown",
    "HK1_Ferien_Programm": "Heating circuit 1 vacation program",
    "HK1_Sommerzeit": "Heating circuit 1 summer time",
    "HK2_Abgesenkt": "Heating circuit 2 lowered",
    "HK2_Normal": "Heating circuit 2 normal",
    "HK2_Party_Countdown": "Heating circuit 2 party countdown",
    "HK2_Ferien_Programm": "Heating circuit 2 vacation program",
    "HK2_Sommerzeit": "Heating circuit 2 summer time",
    "HK3_Abgesenkt": "Heating circuit 3 lowered",
    "HK3_Normal": "Heating circuit 3 normal",
    "HK3_Party_Countdown": "Heating circuit 3 party countdown",
    "HK3_Ferien_Programm": "Heating circuit 3 vacation program",
    "HK3_Sommerzeit": "Heating circuit 3 summer time",
    "HK4_Abgesenkt": "Heating circuit 4 lowered",
    "HK4_Normal": "Heating circuit 4 normal",
    "HK4_Party_Countdown": "Heating circuit 4 party countdown",
    "HK4_Ferien_Programm": "Heating circuit 4 vacation program",
    "HK4_Sommerzeit": "Heating circuit 4 summer time",

    # HK5-HK8 motors (digital 1084-1095)
    "M27_HK5_Pumpe": "Heating circuit 5 pump",
    "M28_HK5_Mischer_Auf": "Heating circuit 5 mixer open",
    "M29_HK5_Mischer_Zu": "Heating circuit 5 mixer close",
    "M30_HK6_Pumpe": "Heating circuit 6 pump",
    "M31_HK6_Mischer_Auf": "Heating circuit 6 mixer open",
    "M32_HK6_Mischer_Zu": "Heating circuit 6 mixer close",
    "M33_HK7_Pumpe": "Heating circuit 7 pump",
    "M34_HK7_Mischer_Auf": "Heating circuit 7 mixer open",
    "M35_HK7_Mischer_Zu": "Heating circuit 7 mixer close",
    "M36_HK8_Pumpe": "Heating circuit 8 pump",
    "M37_HK8_Mischer_Auf": "Heating circuit 8 mixer open",
    "M38_HK8_Mischer_Zu": "Heating circuit 8 mixer close",

    # HK5-HK8 modes (digital 1096-1111)
    "HK5_Modus_Auto": "Heating circuit 5 mode auto",
    "HK5_Modus_Party": "Heating circuit 5 mode party",
    "HK5_Modus_Ferien": "Heating circuit 5 mode vacation",
    "HK5_Modus_Sparbetrieb": "Heating circuit 5 mode economy",
    "HK6_Modus_Auto": "Heating circuit 6 mode auto",
    "HK6_Modus_Party": "Heating circuit 6 mode party",
    "HK6_Modus_Ferien": "Heating circuit 6 mode vacation",
    "HK6_Modus_Sparbetrieb": "Heating circuit 6 mode economy",
    "HK7_Modus_Auto": "Heating circuit 7 mode auto",
    "HK7_Modus_Party": "Heating circuit 7 mode party",
    "HK7_Modus_Ferien": "Heating circuit 7 mode vacation",
    "HK7_Modus_Sparbetrieb": "Heating circuit 7 mode economy",
    "HK8_Modus_Auto": "Heating circuit 8 mode auto",
    "HK8_Modus_Party": "Heating circuit 8 mode party",
    "HK8_Modus_Ferien": "Heating circuit 8 mode vacation",
    "HK8_Modus_Sparbetrieb": "Heating circuit 8 mode economy",
}
