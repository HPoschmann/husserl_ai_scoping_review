# husserl_ai_scoping_review
Contains publicly available research data relating to a review paper on Husserl and AI

## Review protocol and procedural documentation

[Review protocol](review_protocol.md), version 1.1, consolidates the written eligibility criteria, API search specification, screening procedures, and charting rules used in the review. It was assembled from the existing documentation during the second revision on 6 September 2026, after completion of the formal review, and updated on 2 October 2026 for the third revision. It is a retrospective consolidation, not a prospectively deposited or registered protocol. No registration number exists.

The document links to the original screening workbooks, codebook and scripts and distinguishes the formal review from the later external check. It also documents the supplementary “Edmund Husserl” name-variant query: all of its records were also retrieved by a primary query, so it does not change the flow counts.

## Raw retrieval export

[rohdaten_combined_20251205_141147.csv](rohdaten_combined_20251205_141147.csv) is the combined Semantic Scholar export (5,594 rows) underlying the reported flow, including query labels and run-file provenance. [verify_external_title_check.py](verify_external_title_check.py) reproduces the normalized-title check reported in Section 4.8 of the manuscript (`python verify_external_title_check.py`; requires openpyxl).

## Supplementary external check

The nine PhilPapers publications are documented separately from the formal 32-publication corpus:

- [External-check report](external_PhilPapers_review/external_check_round2.md)
- [Charting workbook and abstracts](external_PhilPapers_review/external_check_round2.xlsx)
- [CSV export](external_PhilPapers_review/external_check_round2.csv)

The source-level codes remain unchanged. The corresponding author performed the external charting; an AI tool set up the workbook, transcribed the published abstracts, and proposed page locators, which the corresponding author verified against the full texts. Statements in the earlier external-check materials about the absence of a standalone protocol describe the repository before the new protocol document was added. The protocol consolidates access to the procedural record; it does not claim prospective registration or an independent second coding.
