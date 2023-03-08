title = 'Looking at unified numbering for MHC structures (exploration)'
week = 5
year = 2023
month = 2
day = 17
tags = 'sequence_alignments, structural_alignments, consistent_numbering, features, mhc_class_i, month_two'
===
This week I actually started work on a new feature/improvement to the data. This feels like a wonderful thing to do as it's now been a month since I started the fellowship. 

The feature in question is the one mentioned earlier around IMGT numbering of MHC Class I structures. The problem statement for this is as follows:

**When** people or tools  
**Are** trying to compare two MHC structures from species/loci with insertions/deletions  
**Then** they cannot easily see which residue number is comparable  
**This means** that comparison is hard, or scripts/tools are brittle  

I also filled out some entries on the first pass of the Knowledgeboard for this problem statement

<table width="100%" class="vertical-spacing-bottom">
<tr>
<td class="content">
<strong>What we know</strong><br />
<small>Things you know for certain, and why</small><br /><br />
<ul>
<li>A variety of residue numbering exists in PDB - both correct and incorrect</li>
<li>IMGT G-domain numbering scheme exists</li>
<li>Human, mouse and some other species map to IMGT G-domain numbering directly</li>
<li>Chicken has insertions and deletions</li>
<li>Marsupials have insertions</li>
<li>No tools currently exist for renumbering MHC structures/models✝︎</li>
</ul>
</td>
<td class="content">
<strong>What we think we know</strong><br/>
<small>Things you need more evidence for</small><br/><br/>
<ul>
<li>Multiple alignments can show points for insertions and deletions, will they work as pointers for IMGT numbering?</li>
<li>It is possible to create mapping tables? These can be brittle and will need to be created for each new species/non-classical molecule.</li>
</ul>
</td>
<td class="content">
<strong>What we don’t know</strong><br />
<small>Things you need to find out</small><br /><br />
<ul>
<li>Will MSAs help?</li>
<li>Will DASH guided MAFFT alignments improve placement of gaps?</li>
<li>Can distance matrices be used (either to create the mappings or to test them)?</li>
<li>Will variation in loop structures throw off the distance matrices?</li>
<li>Could an analysis of known variances in position location help reduce the diverse loop problem?§</li>
<li>Would a table of known corresponding important/invariantly positioned variables be a useful thing?</li>
</ul>
</td>
</tr>
</table>

Since the chicken MHC Class I molecules contain both insertions and deletions within the G-domains (what the IMGT call the alpha1 and alpha2 domains of Class I - G standing for Groove) these molecules feel like an interesting test case. 

The first thing to do was to spend some time in PyMol eyeballing a superimposed chicken structure and a human structure (the human structure numbering matches the IMGT numbering). What was immediately obvious was that the AB-turn (loop between A and B strand of the alpha1 domain beta sheet) deviates quite significantly between the chicken and human structures. Aligning all of the known chicken structures suggests this is potentially a common feature. An analysis of the differences in other species will be a key task added to the backlog. 

This deviation in the structure would make using a "nearest structural neighbour" approach for creating the  renumbered structure potentially difficult. This was confirmed by writing a quick piece of prototype code which indeed showed that the nearest neighbours for some of the chicken positions were not the ones relating to the IMGT numbering. This code however may be useful in looking at MHC molecules more generally and the peptides in particular. § One thing which is under consideration from the initial piece of analysis is creating a dataset about 3D variance in MHC molecule structures.

The second activity was around looking at sequence alignments between the chicken and human molecules. This was performed using [MAFFT](https://mafft.cbrc.jp/alignment/software/) with and without [DASH](https://sysimm.org/dash/) which includes information from structural homologs. The alignments with DASH seemed to better predict the correct places for the insertions and deletions. A method to parse these alignments and turn them into maps for renumbering is a task added to the backlog.

Finally, a closer look at the IMGT website shows that they have mapping tables for individual structures. An analysis of the usefulness of these tables has been added to the backlog. Whilst this is useful data it will only help for renumbering structures for which there are experimentally derived structures, and one goal for this feature is to be able to correctly number all structures, including those derived from structure prediction methods.

I also presented at the OpenTargets lab meeting and had a day of annual leave, so the week wasn't a complete one.
