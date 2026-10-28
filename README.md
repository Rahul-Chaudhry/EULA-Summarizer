# EULA Summarizer

Create a short extractive summary of an end-user licence agreement (EULA).
The notebook ranks sentences using TF-IDF, cosine similarity, and PageRank.

> This project helps with reading long agreements; it is not legal advice.

## Start in JupyterLab

Clone the repository, create a virtual environment, and install JupyterLab:

    git clone https://github.com/Rahul-Chaudhry/EULA-Summarizer.git
    cd EULA-Summarizer
    python3 -m venv .venv
    source .venv/bin/activate
    python3 -m pip install jupyterlab
    jupyter lab

On Windows PowerShell, activate the environment with:

    .venv\Scripts\Activate.ps1

Open notebooks/summarize_eula.ipynb. It begins with a commented,
one-package-per-line install cell. If a package is missing, remove the
leading # from its line and run that cell once.

## Notebook workflow

1. Put a .csv or .txt agreement in data.
2. Change INPUT_FILE, TEXT_COLUMN, and SENTENCE_COUNT in the notebook.
3. Select Run All Cells.

The summary is saved as a text file in outputs. CSV inputs need a Description
column by default; change TEXT_COLUMN when your file uses a different name.

## Project layout

    data/          Sample and user-provided EULA source files
    outputs/       Generated summaries, ignored by Git
    notebooks/     All executable project workflows
    documentation/ Project report and reference material

## Original report

See the [project report](documentation/report.docx) for the original coursework context.
