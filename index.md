# What is MMComponents?
The Molecular Mechanics Components (MMComponents) project is a standard for input and output of programs for defining the scientific and computational stages of classical MM pipelines specifying the I/O, but the leaving the implementation up to a developer or user. We define the "what" of the scientific stages without restricting the "how". We define only the input and output the implementation must conform to so that end-users can swap out different implementations with minimal effort in their existing pipelines, or workflow tools of their preference. The components themselves allow users to speed up most of their pipelines by integrating the expertise from component developers, letting them focus on the parts of their research they are experts in.

This allows reproducibility from statically defined and shareable components, experimentation to find a quality series of components for specific problems and systems, and a mechanism for quality methodological assessment rather than scientist expertise.

<p align="center">
    <img src="https://github.com/MolSSI/MMComponents/blob/master/mmcomponents/data/imgs/mm_component_hierarchy.png?raw=true" width="500">
</p>

We construct an abstract Base Component that is inherited by all MMComponent blueprints. For each scientific problem, a blueprint is defined that specifies what the component seeks to achieve, along with the necessary inputs and outputs. This component is implemented to satisfy the scientific problem by any number of users/developers.

# Components under development

## Engines
- [Autodock vina](https://github.com/MolSSI/MMComponents_autodock): molecular docking engine based on [Autodock Vina](http://vina.scripps.edu) 

[![stability-experimental](https://img.shields.io/badge/status-experimental-orange.svg?style=for-the-badge)](https://github.com/emersion/stability-badges#experimental)
- [AutoMartini](https://github.com/MolSSI/MMComponents_automartini): automatic generation of Martini ff parameters for small molecules 

[![stability-none](https://img.shields.io/badge/status-none-red.svg?style=for-the-badge)](https://github.com/emersion/stability-badges#experimental)
- [NAMD](https://github.com/MolSSI/MMComponents_namd): molecular dynamics engine based on the [NAMD](https://www.ks.uiuc.edu/Research/namd) simulator 

[![stability-none](https://img.shields.io/badge/status-none-red.svg?style=for-the-badge)](https://github.com/emersion/stability-badges#experimental)

## Translators
- [RDKit](https://github.com/MolSSI/MMElemental/blob/master/mmelemental/components/rdkit_component.py): RDKit to/from MMSchema converter 

[![stability-experimental](https://img.shields.io/badge/status-experimental-orange.svg?style=for-the-badge)](https://github.com/emersion/stability-badges#experimental)
- [ParmEd](https://github.com/MolSSI/MMElemental/blob/master/mmelemental/components/parmed_component.py): ParmEd to/from MMSchema converter 

[![stability-experimental](https://img.shields.io/badge/status-experimental-orange.svg?style=for-the-badge)](https://github.com/emersion/stability-badges#experimental)
- [MDAnalysis](https://github.com/MolSSI/MMElemental/blob/master/mmelemental/components/mdanalysis_component.py): MDAnalysis to/from MMSchema converter 

[![stability-none](https://img.shields.io/badge/status-none-red.svg?style=for-the-badge)](https://github.com/emersion/stability-badges#experimental)

