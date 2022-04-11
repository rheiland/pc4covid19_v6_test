cat default.xml epi.xml cd8.xml mac.xml neut.xml dc.xml cd4.xml fib.xml residual.xml >celldefs.xml

grep "<cell_def" celldefs.xml
-->
                <cell_definition name="default" ID="0">
        <cell_definition name="lung epithelium"  ID="1">
        <cell_definition name="CD8 Tcell"  ID="3">
        <cell_definition name="macrophage"  ID="4">
        <cell_definition name="neutrophil"  ID="5">
        <cell_definition name="DC"  ID="6">
        <cell_definition name="CD4 Tcell" ID="7">
        <cell_definition name="fibroblast"  ID="8">
                <cell_definition name="residual" ID="9">


cat pre-celldefs.xml celldefs.xml post-celldefs.xml >flat_manual.xml
cp flat_manual.xml ~/git/pc4covid19_v6_test/data/PhysiCell_settings.xml

- set folder=. and # cores=4

python create_cell_types.py flat_manual.xml

