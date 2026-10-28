"""Create a short extractive summary from an EULA stored in CSV or text format."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import networkx as nx
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DEFAULT_TEXT_COLUMN = "Description"


def split_sentences(text: str) -> list[str]:
    """Return non-empty sentences without downloading an NLP model."""
    return [sentence.strip() for sentence in re.split(r"(?<=[.!?])\s+", text) if sentence.strip()]


def read_document(input_path: str | Path, text_column: str = DEFAULT_TEXT_COLUMN) -> str:
    """Read a plain-text document or the selected text column from a CSV file."""
    path = Path(input_path)
    if path.suffix.lower() == ".txt":
        return path.read_text(encoding="utf-8")
    if path.suffix.lower() != ".csv":
        raise ValueError("Input must be a .csv or .txt file.")

    dataframe = pd.read_csv(path)
    if text_column not in dataframe.columns:
        available = ", ".join(map(str, dataframe.columns))
        raise ValueError(f"Column '{text_column}' was not found. Available columns: {available}")
    return " ".join(dataframe[text_column].dropna().astype(str))


def summarize_text(text: str, sentence_count: int = 12) -> list[str]:
    """Rank sentences by TF-IDF cosine similarity and return the best ones in document order."""
    if sentence_count < 1:
        raise ValueError("sentence_count must be at least 1.")

    sentences = split_sentences(text)
    if not sentences:
        return []
    if len(sentences) <= sentence_count:
        return sentences

    vectors = TfidfVectorizer(stop_words="english").fit_transform(sentences)
    similarity = cosine_similarity(vectors)
    np.fill_diagonal(similarity, 0)

    scores = nx.pagerank(nx.from_numpy_array(similarity))
    best_indexes = sorted(sorted(scores, key=scores.get, reverse=True)[:sentence_count])
    return [sentences[index] for index in best_indexes]


def summarize_file(
    input_path: str | Path,
    sentence_count: int = 12,
    text_column: str = DEFAULT_TEXT_COLUMN,
) -> list[str]:
    """Read and summarize a supported document."""
    return summarize_text(read_document(input_path, text_column), sentence_count)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create an extractive summary from an EULA CSV or text file."
    )
    parser.add_argument("input_file", type=Path, help="Path to a .csv or .txt document")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("outputs/summary.txt"),
        help="Where to save the summary (default: outputs/summary.txt)",
    )
    parser.add_argument(
        "--sentences",
        type=int,
        default=12,
        help="Number of sentences in the summary (default: 12)",
    )
    parser.add_argument(
        "--column",
        default=DEFAULT_TEXT_COLUMN,
        help="CSV column containing EULA text (default: Description)",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    summary = summarize_file(args.input_file, args.sentences, args.column)
    if not summary:
        raise ValueError("The input document contains no sentences to summarize.")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n\n".join(summary) + "\n", encoding="utf-8")
    print(f"Saved {len(summary)} sentences to {args.output}")


if __name__ == "__main__":
    main()
