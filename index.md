# What is MMIC?
The Molecular Mechanics Interoperable Components (MMIC) project provides a standard for input and output of MM programs by defining the scientific and computational stages of classical MM pipelines, but leaving the implementation up to the developer/user. MMIC attempts to define the "what" of scientific stages without restricting the "how" i.e. MMIC defines only the input and output the implementation must conform to so that end-users can swap out different implementations with minimal effort in their existing pipelines, or workflow tools of their preference. The components themselves allow users to speed up most of their pipelines by integrating the expertise from component developers, letting them focus on the parts of their research they are experts in.

This allows reproducibility from statically defined and shareable components, experimentation to find a quality series of components for specific problems and systems, and a mechanism for quality methodological assessment without the need for deep scientific expertise.

<p align="center">
    <img src="https://github.com/MolSSI/MMIC/raw/master/mmcomponents/data/imgs/mm_component_hierarchy.png" width="500">
</p>

We construct an abstract Base Component that is inherited by all MMComponent blueprints. For each scientific problem, a blueprint is defined that specifies what the component seeks to achieve, along with the necessary inputs and outputs. This component is implemented to satisfy the scientific problem by any number of users/developers.

# Components being developed

## Simulators
- [Molecular Docking](https://github.com/MolSSI/MMComponents_docking): molecular docking engine based on [Autodock Vina](http://vina.scripps.edu)

[![stability-experimental](https://img.shields.io/badge/status-experimental-orange.svg?style=for-the-badge)](https://github.com/emersion/stability-badges#experimental)

- [Molecular Dynamics](https://github.com/MolSSI/MMComponents_dynamics): molecular dynamics engine based on the [NAMD](https://www.ks.uiuc.edu/Research/namd) simulator

[![stability-none](https://img.shields.io/badge/status-none-red.svg?style=for-the-badge)](https://github.com/emersion/stability-badges#experimental)

## Generators
- [ForceField](https://github.com/MolSSI/MMComponents_forcefield): automatic generation of Martini forcefield parameters for small organic molecules

[![stability-none](https://img.shields.io/badge/status-none-red.svg?style=for-the-badge)](https://github.com/emersion/stability-badges#experimental)

## Translators
| Code       	| Topology 	| Trajectory 	| ForceField 	|
|------------	|----------	|------------	|------------	|
| RDKit      	|<img src="https://img.shields.io/badge/EXP%20-%2314354C.svg?&style=flat&logo=python&logoColor=white"/>| N/A | N/A |
| MDAnalysis 	|<img src="https://img.shields.io/badge/EXP%20-%2314354C.svg?&style=flat&logo=python&logoColor=white"/>|<img src="https://img.shields.io/badge/EXP%20-%2314354C.svg?&style=flat&logo=python&logoColor=white"/>| N/A |
| ParmEd  	    |<img src="https://img.shields.io/badge/EXP%20-%2314354C.svg?&style=flat&logo=python&logoColor=white"/>| N/A |<img src="https://img.shields.io/badge/NONE%20-%2314354C.svg?&style=flat&logo=python&logoColor=white"/>|
| MDTraj        |<img src="https://img.shields.io/badge/NONE%20-%2314354C.svg?&style=flat&logo=python&logoColor=white"/>|<img src="https://img.shields.io/badge/NONE%20-%2314354C.svg?&style=flat&logo=python&logoColor=white"/>|<img src="https://img.shields.io/badge/EXP%20-%2314354C.svg?&style=flat&logo=python&logoColor=white"/>|
| OpenFFTk      |<img src="https://img.shields.io/badge/NONE%20-%2314354C.svg?&style=flat&logo=python&logoColor=white"/>| N/A | <img src="https://img.shields.io/badge/NONE%20-%2314354C.svg?&style=flat&logo=python&logoColor=white"/>|
| Gromacs       |<img src="https://img.shields.io/badge/NONE%20-%2314354C.svg?&style=flat&logo=python&logoColor=white"/>|<img src="https://img.shields.io/badge/NONE%20-%2314354C.svg?&style=flat&logo=python&logoColor=white"/>| <img src="https://img.shields.io/badge/NONE%20-%2314354C.svg?&style=flat&logo=python&logoColor=white"/>|
