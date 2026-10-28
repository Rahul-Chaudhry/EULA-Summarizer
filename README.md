# EULA Summarizer

Create a short, extractive summary of an end-user licence agreement (EULA).
The project ranks sentences using TF-IDF, cosine similarity, and PageRank.

> This project helps with reading long agreements; it is not legal advice.

## Quick start

```bash
git clone https://github.com/Rahul-Chaudhry/EULA-Summarizer.git
cd EULA-Summarizer
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter lab
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Notebook workflow

1. Put a `.csv` or `.txt` agreement in `data/`.
2. Open `notebooks/summarize_eula.ipynb`.
3. Change `INPUT_FILE` and `SENTENCE_COUNT` if needed.
4. Select **Run All Cells**.

The summary is saved as a text file in `outputs/`.

## Command-line workflow

```bash
python src/summarizer.py data/ApacheEULA.csv --output outputs/apache_summary.txt
```

The CSV must contain a `Description` column. For a different column, pass its
name with `--column`. Plain-text inputs work too:

```bash
python src/summarizer.py data/terms.txt --sentences 8
```

## Project layout

```text
data/          # Sample and user-provided EULA source files
outputs/       # Generated summaries (ignored by Git)
notebooks/     # Beginner-friendly Jupyter workflow
src/           # Reusable command-line summarizer
documentation/ # Project report and reference material
requirements.txt
```

## Original report

See the [project report](documentation/report.docx) for the original coursework context.
