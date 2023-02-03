title = 'Prioritising first tasks'
week = 3
year = 2023
month = 2
day = 3
tags = 'starting, prioritising, month_one'
===
The PID template is still in the process of being refined but has been very useful to think through the possible places to start and understand which tasks/projects are dependent upon each other. From this analysis there are two clear first tasks which are quite foundational to work going forwards: 

### IMGT numbering of structures

The structures from the PDB have a variety of different residue numberings. The majority are numbered sequentially with residue 1 being the first residue after the signal peptide. Some structures however are numbered with residue 1 being the first amino acid of the signal peptide. The variety of numbering is further complicated by the MHC molecules of some species having deletions or insertions within the antigen-binding domains.

Fortunately, the IMGT has created a [numbering scheme](https://www.imgt.org/PDF/DCI/29_917-938_2005.pdf) to provide an elegant solution to this problem. This particular task is to develop an automated way to apply the IMGT numbering scheme to MHC Class I structures from the PDB and to develop an automated way to test/validate the assignment. 

### Looking at ways to link IPD/IMGT allele names to data within Open Targets

There is a wealth of information in OpenTargets and the GWAS catalogue which would provide disease association context for a future feature on "histo" which is a page for each allele, with information on polymorphism locations, motifs if known, immunopeptidome/epitopes and structural data/predictions. 

Currently, OpenTargets uses ENSEMBL ids as search criteria and stores information about potentially associated variants keyed against HGVS descriptions. This information is available on the [IPD-IMGT/HLA database (example for HLA-A*02:01)](https://www.ebi.ac.uk/cgi-bin/ipd/pl/hla/get_allele_hgvs.cgi?A*02:01:01:01) and this has potential to create linkages. One interesting opportunity that arises from this is to create ["SameAs"](https://schema.org/sameAs) type mappings and make them publicly available.