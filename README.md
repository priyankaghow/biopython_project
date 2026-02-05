# Functional Sequence Characterization of a Hypothetical Protein

## Project Overview
This project performs functional characterization of a hypothetical protein sequence using bioinformatics approaches. The analysis includes sequence quality assessment, amino acid composition analysis, homology search using BLASTP, and functional annotation based on top BLAST hits.

The project is structured in a modular and reproducible manner suitable for academic coursework and introductory research-level bioinformatics projects.

---

## Objectives
- To analyze amino acid composition of the given protein sequence
- To assess sequence quality and suitability for downstream analysis
- To identify homologous proteins using BLASTP
- To infer potential functional annotation based on sequence similarity

---

## Tools and Libraries Used
- Python
- Biopython
- NCBI BLAST (BLASTP)
- VS Code

---

## Project Structure

Functional_Sequence_Characterization_Sequence2/
│
├── data/
│   └── input_hypothetical_sequence.fasta
│
├── analysis/
│   ├── sequence_qc.py
│   └── homology_analysis.py
│
├── results/
│   └── blast_results.xml
│
├── README.md
├── requirements.txt
└── .gitignore

---

## Methodology

### 1. Sequence Quality Analysis
The protein sequence is read using Biopython. Amino acid composition and sequence length are analyzed to determine whether the sequence is suitable for further bioinformatics analysis.

### 2. Homology Search
BLASTP is used to search the protein sequence against the NCBI non-redundant (nr) database. The BLAST results are stored in XML format.

### 3. Functional Annotation
The BLAST XML output is parsed to retrieve top sequence hits. Functional annotation is inferred based on similarity to known proteins.

---

## How to Run the Project

### Step 1: Install dependencies
pip install -r requirements.txt

### Step 2: Run sequence quality analysis
cd analysis
python sequence_qc.py

### Step 3: Run homology analysis
python homology_analysis.py

---

## Important Note on BLAST Execution
BLAST execution time depends on NCBI server availability and internet connectivity. In some cases, automated BLAST execution may take longer or fail due to network issues.

For academic purposes, BLAST can alternatively be performed using the NCBI BLAST web interface, and the results can be downloaded in XML format for downstream analysis.

---

## Output
- Amino acid composition summary
- Sequence quality validation
- BLAST homology results in XML format
- Functional annotation based on top BLAST hits

---

## Interpretation
The hypothetical protein sequence was subjected to systematic bioinformatics analysis to assess its quality and infer potential function. Sequence length and amino acid composition analysis confirmed that the protein is of sufficient length and structural complexity for reliable downstream analysis, with a diverse residue distribution and an appreciable presence of hydrophobic amino acids suggesting possible membrane-associated regions or conserved structural domains. Homology-based analysis using BLASTP against the NCBI non-redundant protein database identified multiple significant sequence similarities to characterized proteins, indicating evolutionary conservation. Functional inference based on top BLAST hits suggests that the protein may play a role in essential cellular processes, potentially related to enzymatic or transport-associated functions. Although experimental validation is required for definitive functional assignment, this computational analysis provides strong preliminary evidence supporting the biological relevance and conserved functional nature of the hypothetical protein.

---
## Author
Priyanka Ghow

