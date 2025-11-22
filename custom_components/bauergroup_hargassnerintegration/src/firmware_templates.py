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
    # Boiler core parameters
    "ZK": "Boiler state",
    "O2": "O2 level",
    "O2soll": "O2 target",
    "TK": "Boiler temperature",
    "TKsoll": "Boiler temperature target",
    "TRL": "Return temperature",
    "TRLsoll": "Return temperature target",
    "Spreizung": "Temperature spread",
    "TRG": "Smoke gas temperature",
    "SZist": "Draft current",
    "SZsoll": "Draft target",

    # Buffer temperatures
    "TPo": "Buffer temperature top",
    "TPm": "Buffer temperature middle",
    "TPu": "Buffer temperature bottom",
    "TPmo": "Buffer temperature middle-top",
    "TPmu": "Buffer temperature middle-bottom",

    # Performance and power
    "Leistung": "Output power",
    "ESsoll": "Delivery rate target",
    "KeBrstScale": "Boiler scale",
    "ESRegler": "Delivery regulator",
    "max.Leist.P3F.HT": "Maximum power P3F HT",

    # Motor currents
    "I Es": "Delivery motor current",
    "I Sr": "Grate motor current",
    "I Rein": "Cleaning motor current",
    "I Ra": "Ash motor current",
    "I Aa": "Ash auger current",

    # Temperature sensors
    "Taus": "Outside temperature",
    "TA Gem.": "Mean outside temperature",
    "TFW": "Hot water temperature",
    "Tplat": "Circuit board temperature",
    "BRT": "BRT temperature",
    "T Spülung": "Cleaning temperature",
    "TVG": "TVG temperature",

    # BLDC motor
    "BLDC_ES ist": "BLDC delivery motor actual speed",
    "BLDC_ES soll": "BLDC delivery motor target speed",

    # Runtime and counters
    "LZ ES seit Füll.": "Runtime since refill",
    "LZ ES seit Ent.": "Runtime since ash removal",
    "LZ ES seit Entasch.": "Runtime since ash removal",
    "Anzahl Entasch.": "Ash removal count",
    "Anzahl SR Beweg.": "Grate movement count",

    # Lambda probe
    "Heiz P Lambda": "Lambda probe heating power",
    "Heiz U Lambda": "Lambda probe heating voltage",
    "Heiz I Lambda": "Lambda probe heating current",
    "Sens U Lambda": "Lambda probe sensor voltage",

    # Buffer
    "PuffZustand": "Buffer state",
    "Puffer_soll": "Buffer target temperature",
    "Puff Füllgrad": "Buffer fill level",

    # Pellet storage
    "Lagerstand": "Pellet stock",
    "Verbrauchszähler": "Pellet consumption",
    "UsePos": "Usage position",

    # Error handling
    "Störungs Nr": "Error code",
    "Störung": "Error flag",

    # Hot water circuits (Boiler/Warmwasser)
    "TBA": "Hot water A temperature",
    "TBs_A": "Hot water A target",
    "BoiZustand_A": "Hot water A state",
    "TB1": "Hot water 1 temperature",
    "TBs_1": "Hot water 1 target",
    "BoiZustand_1": "Hot water 1 state",
    "TB2": "Hot water 2 temperature",
    "TBs_2": "Hot water 2 target",
    "BoiZustand_2": "Hot water 2 state",
    "TB3": "Hot water 3 temperature",
    "TBs_3": "Hot water 3 target",
    "BoiZustand_3": "Hot water 3 state",

    # Heating circuits (Heizkreise) - Circuit A
    "TVL_A": "Flow A temperature",
    "TVLs_A": "Flow A target",
    "TRA_A": "Return A temperature",
    "TRs_A": "Return A target",
    "HKZustand_A": "Heating circuit A state",
    "FRA Zustand": "Room controller A state",

    # Heating circuits (Heizkreise) - Circuit 1-6
    "TVL_1": "Flow 1 temperature",
    "TVLs_1": "Flow 1 target",
    "TRA_1": "Return 1 temperature",
    "TRs_1": "Return 1 target",
    "HKZustand_1": "Heating circuit 1 state",
    "FR1 Zustand": "Room controller 1 state",

    "TVL_2": "Flow 2 temperature",
    "TVLs_2": "Flow 2 target",
    "TRA_2": "Return 2 temperature",
    "TRs_2": "Return 2 target",
    "HKZustand_2": "Heating circuit 2 state",
    "FR2 Zustand": "Room controller 2 state",

    "TVL_3": "Flow 3 temperature",
    "TVLs_3": "Flow 3 target",
    "TRA_3": "Return 3 temperature",
    "TRs_3": "Return 3 target",
    "HKZustand_3": "Heating circuit 3 state",
    "FR3 Zustand": "Room controller 3 state",

    "TVL_4": "Flow 4 temperature",
    "TVLs_4": "Flow 4 target",
    "TRA_4": "Return 4 temperature",
    "TRs_4": "Return 4 target",
    "HKZustand_4": "Heating circuit 4 state",
    "FR4 Zustand": "Room controller 4 state",

    "TVL_5": "Flow 5 temperature",
    "TVLs_5": "Flow 5 target",
    "TRA_5": "Return 5 temperature",
    "TRs_5": "Return 5 target",
    "HKZustand_5": "Heating circuit 5 state",
    "FR5 Zustand": "Room controller 5 state",

    "TVL_6": "Flow 6 temperature",
    "TVLs_6": "Flow 6 target",
    "TRA_6": "Return 6 temperature",
    "TRs_6": "Return 6 target",
    "HKZustand_6": "Heating circuit 6 state",
    "FR6 Zustand": "Room controller 6 state",

    # External heating circuit control
    "Ext.HK Soll": "External heating circuit target",
    "Ext.HK Soll_2": "External heating circuit 2 target",
    "Ext.HK Soll_3": "External heating circuit 3 target",

    # Heating circuit requests (Anforderungen)
    "Höchste Anf": "Highest request",
    "Anf. HKR0": "Heating circuit 0 request",
    "Anf. HKR1": "Heating circuit 1 request",
    "Anf. HKR2": "Heating circuit 2 request",
    "Anf. HKR3": "Heating circuit 3 request",
    "Anf. HKR4": "Heating circuit 4 request",
    "Anf. HKR5": "Heating circuit 5 request",
    "Anf. HKR6": "Heating circuit 6 request",
    "Anf. HKR7": "Heating circuit 7 request",
    "Anf. HKR8": "Heating circuit 8 request",
    "Anf. HKR9": "Heating circuit 9 request",
    "Anf. HKR10": "Heating circuit 10 request",
    "Anf. HKR11": "Heating circuit 11 request",
    "Anf. HKR12": "Heating circuit 12 request",
    "Anf. HKR13": "Heating circuit 13 request",
    "Anf. HKR14": "Heating circuit 14 request",
    "Anf. HKR15": "Heating circuit 15 request",

    # Cascade control
    "KaskSollTmp_1": "Cascade 1 target temperature",
    "KaskSollTmp_2": "Cascade 2 target temperature",

    # Differential regulation
    "DiffReg S1": "Differential regulator sensor 1",
    "DiffReg S2": "Differential regulator sensor 2",
    "DiffReg2 S3": "Differential regulator 2 sensor 3",
    "DiffReg2 S4": "Differential regulator 2 sensor 4",

    # Analog input and power supply
    "AIN17": "Analog input 17",
    "U Netzteil": "Power supply voltage",

    # Regulator
    "Regler K": "Regulator K",

    # Digital parameters
    "E": "Error digital flag",
    "Stb": "Standby",
    "Fuellstand": "Fill level sensor",
}
