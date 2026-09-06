# Review protocol

## Consolidated documentation of the procedure followed

**Review:** A scoping review mapping the role of Husserlian phenomenology in artificial intelligence research  
**Review authors:** Hendrik Poschmann and Stefania Centrone  
**Corresponding author:** Hendrik Poschmann  
**Version:** 1.0 — 6 September 2026  
**Registration:** Not registered; no prospective registration number exists.

### 1. Status and documentary basis

This document brings together the written eligibility criteria, search specification, screening procedures, and charting rules used in the review. It was consolidated during the second revision, after the formal review had been completed, from the existing API specification, screening workbooks, codebook, retrieval scripts, and manuscript methods. It makes that procedure accessible as a standalone document; it is not a protocol deposited or registered before the search. The earlier manuscript describes the Husserlian-anchor criterion as fixed before abstract screening and the synthesis dimensions as defined in advance. This document retains that account without assigning undocumented dates to individual decisions or refinements.

The retained workbooks contain the operational rules and decisions. Earlier manuscript versions already describe a written, non-registered protocol. They do not preserve a complete, timestamped history of every procedural refinement. The post hoc PhilPapers check is therefore identified separately below as a revision-stage addition. Reporting is guided by [PRISMA-ScR](https://www.prisma-statement.org/scoping), including disclosure of protocol availability and registration status.

### 2. Purpose and review questions

The review maps substantive uptake of Husserlian phenomenology in AI and robotics. A scoping design accommodates philosophical arguments, conceptual frameworks, technical studies, and architectural proposals without treating them as commensurable intervention effects. It asks:

1. In what ways, and with what depth of engagement, do AI-related publications draw on Husserlian phenomenology?
2. Which Husserlian concepts are most frequently mobilized, and how are they translated into AI-relevant claims?
3. To what extent is phenomenological method presented as applicable to AI systems research, procedurally, evaluatively, or architecturally?
4. Which conceptual and methodological questions remain for further research, particularly in embodied AI, cognitive architectures, and human–robot interaction?

The resulting frequencies characterize the retrieved sample. The review does not presume either that technical performance establishes consciousness or that artificial intentionality is categorically impossible.

### 3. Eligibility

Eligibility follows the Concept–Context–Types of evidence framework recorded in the manuscript.

| Dimension | Rule used |
|---|---|
| Concept | Direct reference to Husserl or substantive, attributable use of distinctively Husserlian constructs. Generic phenomenological vocabulary or exclusive reliance on later traditions without a Husserlian anchor is insufficient. |
| Context | Substantive AI or robotics relevance, including system design, methodological reflection, evaluation, philosophical foundations, or human interaction with these technologies. |
| Contribution | Full-text inclusion requires use of Husserlian distinctions that informs the AI-related analysis; merely mentioning Husserl does not suffice. |
| Evidence types | Scholarly journal articles, conference papers, books, book chapters, and preprints. Non-scholarly material is excluded. |
| Language | English. Language is assessed during screening; it was not an API-level filter. |
| Publication window | 1989–2026, including early-online or indexed-ahead records carrying a 2026 year. This is the search window, not the observed year range of the included corpus. |

An unclear anchor may be resolved by full-text assessment. Attributed engagement through secondary scholarship can qualify when the use is substantive; a direct citation of a primary Husserl text is not the sole route to eligibility.

### 4. Information source and search specification

The formal retrieval uses the Semantic Scholar Academic Graph API. The most recent search date recorded in the API specification is **5 December 2025**. Eight primary conceptual combinations connect an AI/robotics term with a philosophical term:

| Query code | Primary query as documented in the API specification |
|---|---|
| ai_husserl | "artificial intelligence" AND "Husserl" |
| ai_epistemology | "artificial intelligence" AND "epistemology" |
| ai_phenomenology | "artificial intelligence" AND "phenomenology" |
| ai_consciousness | "artificial intelligence" AND "consciousness" |
| robotics_husserl | "robotics" AND "Husserl" |
| robotics_epistemology | "robotics" AND "epistemology" |
| robotics_phenomenology | "robotics" AND "phenomenology" |
| robotics_consciousness | "robotics" AND "consciousness" |

A supplementary query used the name variant **"Artificial Intelligence" AND "Edmund Husserl"**, as confirmed by the corresponding author during this consolidation. Eight records in the preserved combined export retain this additional label, alongside primary-query labels. Its separate execution time is not established by the retained files. Query capitalization and combined provenance labels in the raw export are preserved; the table above follows the written API specification.

The narrower Husserl queries retrieve explicitly anchored material, while the broader philosophical queries allow an anchor to be identified at abstract or full-text stage. The specification and retained script record:

| Setting | Recorded implementation |
|---|---|
| Endpoint and method | GET https://api.semanticscholar.org/graph/v1/paper/search |
| Parameters | query, year, limit, offset, fields |
| Year subranges | Five-year intervals from 1989–1993 through 2024–2026 |
| Page size and cap | 100 records per page; at most 1,000 results per query/year subrange in the retained script |
| Requested fields | title, year, venue, abstract, url, authors, externalIds; DOI extracted from externalIds.DOI |
| Rate handling | 1.05-second minimum delay; Retry-After handling and exponential backoff on HTTP 429, with the backoff variable capped at 60 seconds |
| Output | Timestamped CSV files; author names flattened and abstract line breaks normalized |

These settings describe the executed workflow as documented in [the API specification](API_Spec_and_PRISMA_Flow_Inputs.xlsx) and [the retained scraper](semscholarscraper.py). The script stops a subrange when no further results are returned, no next offset exists, the cap is reached, or a non-429 request error ends that subrange. Partitioning reduces the impact of the cap; it does not prove exhaustive retrieval. A later API run may return different records because the index and service change. Reproduction of the reported analysis should therefore start from the preserved screening and charting files.

### 5. Consolidation and deduplication

The retained [combine_results.py](combine_results.py) consolidates query CSVs, prioritizing a DOI-based key, then title plus year, then URL, with an individual-row fallback. Matching is case-normalized where specified in the script. Query and year-range provenance are joined; other metadata use the first non-empty value. Further duplicate checks use title, author, DOI, and content information, as recorded in the flow specification and screening material.

The preserved combined export contains 5,594 records and is the input count underlying the reported flow. It is not an independently established sum of every response from every API request. The reported 67 duplicate removals concern the subsequent review flow. The title workbook retains 44 rows explicitly marked as manually found duplicates; those rows belong to duplicate removal and are not counted again as substantive title exclusions. The remaining difference is not assigned a more detailed removal history than the files establish.

Record identifiers are retained, but local numeric identifiers are reused in the workbooks. Source identity should therefore be checked with title and DOI where available, together with workbook and row location, rather than inferred from record_id alone.

### 6. Screening and selection

Hendrik Poschmann conducted screening. The process used dedicated workbooks for title, abstract, and full-text assessment. No independent duplicate screening, adjudication between two screeners, or inter-rater reliability statistic is claimed.

Title screening was intended to remove clearly irrelevant or formally ineligible material. Abstract screening assessed substantive AI/robotics relevance and the Husserlian-anchor requirement. Sources whose relevance or anchoring required clarification could proceed to full-text assessment. Full-text decisions depended on substantive deployment of Husserlian concepts, distinctions, or methods within the AI-related contribution.

The decision field permits include, exclude, and maybe/seek_full_text. The codebook specifies exclusion categories for AI/robotics irrelevance, missing Husserlian anchoring, exclusively non-Husserlian phenomenology, topic scope, language, year range, insufficient information, duplicates, and other reasons. The completed workbooks also contain legacy spellings and some unfilled reason cells; those entries are preserved rather than retrospectively replaced with new judgments. Full-text exclusions have recorded reasons for all 26 excluded sources.

The authoritative decision files are [title screening](step1_title_screening_combined.xlsx), [abstract screening](step2_abstract_screening_with_decisions.xlsx), and [full-text screening](step3_fulltext_screening.xlsx). Notes and summary rows are not additional publications; flow counts use rows carrying actual include/exclude decisions and treat duplicate rows separately.

### 7. Data charting

Charting uses the existing **Codebook** and **ValidationLists** sheets. [final_results.xlsx](final_results.xlsx) contains the final formal-corpus records and the codebook used for comparison in the external check. The instrument covers:

| Field group | Variables and purpose |
|---|---|
| Identification | record_id, title, authors, year, venue, pub_type, doi, url: identify the source and its bibliographic form. |
| Retrieval and selection | abstract_present, full_text_access, search_string_origin, inclusion_stage, decision, exclusion_reason: document access, provenance, stage and decision. |
| Husserlian anchoring | husserl_anchor_type, husserl_work_cited, husserl_concepts_primary: identify the basis and substance of the attribution. |
| Conceptual role and depth | concept_role and depth_of_engagement: distinguish the function of the concepts and the extent of engagement. |
| Method | phen_method_applied and phen_method_elements: record whether and how phenomenological procedures are invoked or applied. |
| AI target | ai_domain and ai_object_of_analysis: identify the relevant AI/robotics domain and the object of analysis. |
| Influence | mode_of_influence: record the contribution of Husserl to the AI-related work. |
| Interpretive extraction | research_implications, proposed_operationalization, key_claims, evidence_type, limitations_noted_by_authors, coder_notes: retain implications, claims, proposals, evidential form and qualifications. |

The engagement scale runs from **0 (mention only), 1 (short discussion), 2 (substantive deployment), 3 (core driver), to 4 (method operationalized)**. Method application separately distinguishes no application, partial conceptual application, described procedural steps, implementation in study design, and unclear cases. Evidence type distinguishes theoretical argument, conceptual framework, empirical study, design prototype, review/position, and mixed contributions. A depth score or influence code alone does not establish implementation or effectiveness.

The influence vocabulary is conceptual_translation, methodological_import, design_guidance, evaluation_guidance, critique/limits, agenda_setting, and other. The field describes the primary contribution, but the retained records also use multiple assignments where warranted. Multi-valued constructs and domains preserve substantive overlap. Reasons and borderline interpretations belong in coder_notes; proposed operationalizations distinguish conceptual suggestions from procedures or experiments.

Seven additional columns in the Records sheets support abstract transcription and workflow handling: abstract manually added, source_file, title_norm, authors_norm, husserl_term_title, husserl_term_abstract, and noise_title_flag. They do not replace the substantive eligibility judgment. The Codebook and ValidationLists remain the reference for permitted values. The key_claims definition is worded more briefly in the full-text/final workbooks than in the title/abstract workbooks; the retained permitted-value lists are identical across these stages. No new coding categories are introduced by this consolidation.

### 8. Synthesis and interpretation

The manuscript identifies Husserlian construct, AI domain, and mode of influence as the principal synthesis dimensions. The analysis combines source-level interpretation with descriptive counts of publication characteristics, constructs, engagement, domains, and influence modes. It does not pool intervention effects or perform a formal risk-of-bias assessment across the heterogeneous material.

For multi-valued fields, a publication contributes to each assigned category; category totals may exceed the number of publications. Percentages use the relevant publication denominator. A union such as methodological import or design guidance counts each publication once. Conceptual interpretation, architectural guidance, implemented methods, and validation are considered separately, so code frequencies do not measure engineering maturity or field-wide prevalence. The constructive discussion is identified as the authors’ proposals rather than additional findings of the evidence map.

### 9. Revision-stage external check

The PhilPapers check was introduced after peer review and was not part of the original formal retrieval. It followed the eight primary conceptual combinations as closely as the interface permitted and recovered nine apparently eligible publications. It was a post hoc check, not a parallel systematic search; a complete query-to-record execution log is not retained.

During the second revision, these nine publications were charted from their full texts using the existing instrument. The corresponding author manually checked and confirmed the decisions against the codebook. No independent second coding is claimed. The records remain outside the formal 32-publication corpus and its PRISMA flow. They have their own influence-mode distribution and illustrative coding alternatives, with no pooled prevalence estimate. The accompanying [external-check report](external_PhilPapers_review/external_check_round2.md) and [workbook](external_PhilPapers_review/external_check_round2.xlsx) document the analysis.

The confirmed external chart has 10 influence assignments across 9 publications; the formal chart has 33 across 32. Methodological import or design guidance occurs in 3/9 and 7/32 distinct publications, respectively. These are completed-review results, not protocol eligibility targets. The external result qualifies quantitative interpretation of the formal sample and does not establish its stability across information sources.

### 10. Completed-workflow audit and document history

The following figures identify the completed workflow documented by this protocol. They were not target sample sizes fixed in advance.

| Flow step | Publications/records |
|---|---:|
| Preserved consolidated retrieval input | 5,594 |
| Additional duplicates removed in the reported review flow | 67 |
| Title-screening denominator | 5,527 |
| Title exclusions, excluding duplicate rows | 4,594 |
| Abstract-screening denominator | 933 |
| Abstract exclusions | 875 |
| Full-text assessments | 58 |
| Full-text exclusions | 26 |
| Formal included corpus | 32 |
| Separately charted external publications | 9 |

The API/flow workbook, the three screening workbooks, and final_results.xlsx provide the primary procedural and decision record. The local combined CSV, rohdaten_combined_20251205_141147.csv, supplies the preserved query labels and input count; that raw export was consulted locally and is not linked here as a public repository file. The retained scripts document retrieval and CSV consolidation. The repository materials were checked against snapshot [bb560f7](https://github.com/HPoschmann/husserl_ai_scoping_review/tree/bb560f721832bd7a99c6c4b37d9f678191f4b179) during preparation of this document. File modification metadata are not treated as proof that a particular rule was fixed on a particular day.

**Version history:** Version 1.0 was consolidated on 6 September 2026 for the second revision. It documents the original procedure, the separately identified external-check addition, and the supplementary name-variant query confirmed by the corresponding author. It does not rerun screening, change inclusion decisions, or register the review retrospectively. Earlier external-check materials describing the absence of a standalone protocol refer to the repository before this consolidation was added.
