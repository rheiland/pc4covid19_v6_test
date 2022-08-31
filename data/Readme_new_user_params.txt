Recall, we now have multiple .xml for regimes:
    regime_config = widgets.Dropdown(
        description='Regime',
        options = {"baseline":"baseline_v6.xml", "immune":"regime_immune.xml", "harmful":"regime_harmful.xml"},


So, when Michael adds new params to his core PhysiCell_settings.xml <user_parameters>, we need to:
- manually add them to baseline_v6.xml regime_immune.xml, regime_harmful.xml

then:
M1P~/git/pc4covid19_v6_test/data$ cp baseline_v6.xml PhysiCell_settings.xml

then:
M1P~/git/pc4covid19_v6_test/data$ python xml2jupyter.py PhysiCell_settings.xml
M1P~/git/pc4covid19_v6_test/data$ cp user_params.py ../bin/

