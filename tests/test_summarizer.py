import unittest

from Code.summarizer import read_document, summarize_file, summarize_text


class SummarizerTests(unittest.TestCase):
    def test_returns_requested_number_of_sentences(self) -> None:
        text = "One sentence. Two related sentences. Three unrelated sentences. Four sentences."

        summary = summarize_text(text, sentence_count=2)

        self.assertEqual(len(summary), 2)
        self.assertTrue(all(sentence in text for sentence in summary))

    def test_reads_included_csv(self) -> None:
        document = read_document("Data-Files/ApacheEULA.csv")

        self.assertIn("License", document)
        self.assertEqual(len(summarize_file("Data-Files/ApacheEULA.csv", 3)), 3)


if __name__ == "__main__":
    unittest.main()
