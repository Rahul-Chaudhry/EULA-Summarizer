# EULA Summarizer

Create a short, extractive summary of an end-user licence agreement (EULA).
The tool ranks sentences using TF-IDF, cosine similarity, and PageRank, then
writes the most representative sentences to a text file.

> This project helps with reading long agreements; it is not legal advice.

## Quick start

```bash
git clone https://github.com/Rahul-Chaudhry/EULA-Summarizer.git
cd EULA-Summarizer
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python Code/summarizer.py Data-Files/ApacheEULA.csv --output Summarized-Files/apache_summary.txt
```

On Windows PowerShell, activate the virtual environment with:

```powershell
.venv\Scripts\Activate.ps1
```

The command prints the saved location. Open the generated `.txt` file in
`Summarized-Files` to read the result.

## Use your own EULA

The summarizer accepts either:

- A `.csv` file with a `Description` column containing the agreement text.
- A plain `.txt` file.

Examples:

```bash
python Code/summarizer.py path/to/terms.txt --sentences 8
python Code/summarizer.py path/to/terms.csv --column "Agreement text" --sentences 10
```

`--output` changes where the summary is written. `--sentences` controls its
length; the default is 12 sentences.

## How it works

1. Read the EULA text and split it into sentences.
2. Convert sentences to TF-IDF vectors.
3. Measure cosine similarity between every pair of sentences.
4. Use PageRank to identify the most central sentences.
5. Keep the top-ranked sentences in their original document order.

Unlike the original script, this version does not download a multi-gigabyte
GloVe file or require a separate NLTK download before it can run.

## Project layout

```text
Code/
  summarizer.py       # Command-line summarizer
Data-Files/           # Example Apache and YouTube EULA CSV files
Summarized-Files/     # Generated summaries (ignored by Git)
tests/                # Small regression tests
requirements.txt      # Required Python libraries
```

## Test

```bash
python -m unittest discover -s tests
```

## Original report

See the [project report](REPORT.docx) for the original coursework context.
