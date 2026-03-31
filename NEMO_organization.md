# About this data
The Neuroscience Multi-Omic Archive (NeMO Archive; nemoarchive.org) serves as the primary repository for genomics data from the BRAIN Initiative. Our data is a curated resource containing transcriptomic and epigenomic data from over 50 million brain cells, including single-cell genomic data from major regions of adult and prenatal human and mouse brains, as well as substantial single-cell genomic data from non-human primates.

## Directory structure

At our top level bucket, 

[s3://nemo-public-preview.s3.us-east-1.amazonaws.com](s3://nemo-public-preview.s3.us-east-1.amazonaws.com)

we have:

```
README.txt
data/
metadata/
docs/
```

Next, let's introduce some terms:

**PROGRAM:** A program is a coordinated, multi-institution research effort funded under a common strategic initiative (typically by NIH or another funding agency) to address a broad scientific objective. A program encompasses multiple independently led projects that collectively contribute to shared goals, standards, and deliverables. Programs often span multiple institutions and laboratories, and include multiple principal investigators (PIs).

**PROJECT:** A project is a defined research effort within a program, typically led by a principal investigator or investigator team, focused on a specific scientific question, dataset, or technical objective. Projects operate semi-independently but align with the broader goals and standards of the program.

There are two important caveats to the project definition: 
- For legacy reasons "grant" and "project" are used interchangeably. 
- Multiple funded efforts can be agregated into one project. 

The intention is that our heirarchical directory tree reflects this aggregation:
```
Program (e.g., bican)
├── Project A (PI-led)
├── Project B (PI-led)
├── Project C (multi-institution)
│   ├── Project C.1 (PI-led)
│   └── Project C.2 (PI-led)
└── Project D (PI-led)
```

The first tier of the directory structure reflects the program:
```
bican/
biccn/
other/
```

Then what you see here is that "grant" is showing a collection of projects, with the term "rf1_macosko" reflecting the project name, as in: 

```
biccn/
    grant/
        rf1_macosko/
```

In some cases there are grant-projects nested under the top-level program, e.g.: 

```
bican/
    grant/
        BICAN_Dev_Mouse/
            aibs/
        BICAN_Dev_Multiomics/
            ucla_luo/
```

Further down the heirarchical, several sequencing modalities are used for these projects, such as transcriptome, epigenome, multimodal and are reflected in the naming structure of next tier of the directory tree. Under each of these trees we have listed directories that contain the sequence information, e.g.: 

```
bican/
    grant/
        BICAN_Dev_Mouse/
            aibs/
                transcriptome/
                    cells/
                        SEQUENCE_DIRECTORIES:296
```

This document provides the entire NeMO human and mammalian brain atlas with the truncated sequence directories: [nemo_tree_pruned.txt](nemo_tree_pruned.txt)

This document provides the entire NeMO human and mammalian brain atlas along with listed sequence directories.  

**Caution, this file is 58M**: nemo_public_tree_full.txt

The file nemo_public_tree_full.txt does NOT include the sequence files themselves, it simply lists the directories that contain those files. The file formats used in the sequence directories are described here: 

[https://github.com/nemoarchive/documentation/blob/master/file_extensions.md](https://github.com/nemoarchive/documentation/blob/master/file_extensions.md)

