To test locally, run:
$ jupyter notebook pc4covid19v6_local.ipynb


then the usual menu clicks:
  Cell -> Run All
(patiently wait for cells to be executed and the GUI to appear)


To actually run a sim, you'll need to compile /src (locally), then copy/mv "myproj" into ../bin, e.g.:
M1P~/git/pc4covid19_v6_test/src$ make -f Make-M1-local
g++-11 -fomit-frame-pointer -fopenmp -m64 -std=c++11  -c ./BioFVM/BioFVM_vector.cpp 
...
g++-11 -fomit-frame-pointer -fopenmp -m64 -std=c++11  -o myproj BioFVM_vector.o BioFVM_mesh.o BioFVM_microenvironment.o BioFVM_solvers.o BioFVM_matlab.o BioFVM_utilities.o BioFVM_basic_agent.o BioFVM_MultiCellDS.o BioFVM_agent_container.o   pugixml.o PhysiCell_phenotype.o PhysiCell_cell_container.o PhysiCell_standard_models.o PhysiCell_cell.o PhysiCell_custom.o PhysiCell_utilities.o PhysiCell_constants.o  PhysiCell_SVG.o PhysiCell_pathology.o PhysiCell_MultiCellDS.o PhysiCell_various_outputs.o PhysiCell_pugixml.o PhysiCell_settings.o custom.o external_immune.o submodel_data_structures.o internal_viral_dynamics.o internal_viral_response.o receptor_dynamics.o immune_submodels.o epithelium_submodel.o DC_history.o main.cpp 
Undefined symbols for architecture arm64:
  "__ZN9PhysiCell19PhysiCell_constants20necrosis_death_modelE", referenced from:
      __Z41__static_initialization_and_destruction_0ii in PhysiCell_constants.o
  "__ZN9PhysiCell19PhysiCell_constants21apoptosis_death_modelE", referenced from:
      __Z41__static_initialization_and_destruction_0ii in PhysiCell_constants.o
  "__ZN9PhysiCell19PhysiCell_constants22basic_Ki67_cycle_modelE", referenced from:
      __Z41__static_initialization_and_destruction_0ii in PhysiCell_constants.o
  "__ZN9PhysiCell19PhysiCell_constants22live_cells_cycle_modelE", referenced from:
      __Z41__static_initialization_and_destruction_0ii in PhysiCell_constants.o
  "__ZN9PhysiCell19PhysiCell_constants23cycling_quiescent_modelE", referenced from:
      __Z41__static_initialization_and_destruction_0ii in PhysiCell_constants.o
  "__ZN9PhysiCell19PhysiCell_constants25advanced_Ki67_cycle_modelE", referenced from:
      __Z41__static_initialization_and_destruction_0ii in PhysiCell_constants.o
  "__ZN9PhysiCell19PhysiCell_constants26flow_cytometry_cycle_modelE", referenced from:
      __Z41__static_initialization_and_destruction_0ii in PhysiCell_constants.o
  "__ZN9PhysiCell19PhysiCell_constants36flow_cytometry_separated_cycle_modelE", referenced from:
      __Z41__static_initialization_and_destruction_0ii in PhysiCell_constants.o
ld: symbol(s) not found for architecture arm64
collect2: error: ld returned 1 exit status
make: *** [all] Error 1
---------

Argh, OK, this is due to the macOS weirdness of the src/core/PhysiCell_constants.* files.
I keep a repo just for the different files. But for here, I just created src/core/PhysiCell_constants_macos.*
and modified src/Make-M1-local  accordingly. So, when testing locally on macOS, do:

M1P~/git/pc4covid19_v6_test/src$ make -f Make-M1-local 
then:
M1P~/git/pc4covid19_v6_test/src$ mv myproj ../bin





