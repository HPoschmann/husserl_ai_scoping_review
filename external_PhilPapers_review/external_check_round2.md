# Supplementary external check of nine PhilPapers publications

A scoping review mapping the role of Husserlian phenomenology in artificial intelligence research

Hendrik Poschmann and Stefania Centrone | 6 September 2026

## Scope and procedure

This report charts the nine records identified in the first-revision PhilPapers check. It is supplementary external analysis, not an expansion of the formal 32-publication corpus. No additional systematic search was conducted, and the original PRISMA flow and quantitative tables remain unchanged. The publication identities are fixed by manuscript references [50] and [54]–[61].

All nine full texts were accessed as local publisher PDFs, including the complete 12-page Poljanšek chapter. Evidence is located by printed page and, where needed, PDF page number. The accompanying external_check_round2.xlsx workbook preserves every original codebook field relevant to external charting and includes additional provenance and reasoning columns. Eight published abstracts are transcribed from the source PDFs. Lopes’s proto-computationalism article has no published abstract in its PDF or publisher article page; this is recorded as an absence, without substituting a new summary.

The charting used the original Codebook and ValidationLists sheets in final_results.xlsx and the definitions in manuscript Sections 2.5 and 3.5. The corresponding author manually checked and confirmed the charting decisions against the codebook (human-in-the-loop). The codebook was not retuned to obtain agreement with the original result. The original workbook is retained as the basis of comparison, including its multi-valued Cibotaru entry. No independent second coding or inter-rater statistic was obtained.

## Applying the existing instrument

The mode field concerns the primary contribution of Husserl to AI research. Seven values are permitted; five occur in the original corpus. Conceptual translation rearticulates concepts; critique/limits challenges claims; agenda setting sets research priorities; methodological import transfers a procedure or structured investigative approach; design guidance specifies architectural or interaction requirements. These practical distinctions follow the existing manuscript. Evaluation guidance and other remain available, with zero assignments in this check.

The boundary is the contribution, not whether a source mentions a technical system. The original workbook codes both Tani temporal-robotics papers as conceptual translation, Beavers and Properzi as methodological import, and Incao et al. as design guidance. These cases provide calibration examples. A design proposal need not be implemented, and an empirical setting need not have been designed from Husserl. The method-application and evidence-type fields record these differences.

Multi-valued influence coding is retained where two substantial contributions require it. Lopes’s CNN article has critique/limits as its primary contribution and design_guidance as an additional sustained contribution. The other eight records have one counted mode. Broader possible readings are documented as coding alternatives, not silently added to the main distribution.

## Distribution and interpretation

| Mode | Formal corpus, n/32 | External check, n/9 |
| --- | --- | --- |
| Conceptual translation | 11 (34.4%) | 4 (44.4%) |
| Critique / limits | 8 (25.0%) | 2 (22.2%) |
| Agenda setting | 7 (21.9%) | 1 (11.1%) |
| Methodological import | 6 (18.8%) | 1 (11.1%) |
| Design guidance | 1 (3.1%) | 2 (22.2%) |
| Evaluation guidance | 0 | 0 |
| Other | 0 | 0 |

There are 33 and 10 mode assignments, respectively. Percentages use publications as denominators and therefore need not sum to 100%. Seven distinct corpus publications and three distinct external publications have methodological import or design guidance: 21.9% versus 33.3%. The external set does not establish stability of the quantitative distribution. It is purposively recovered and too small for population prevalence or database-recall estimation; no pooled 41-publication synthesis is performed.

The two sets overlap thematically, but thematic overlap cannot establish stability of mode frequencies. The revised manuscript therefore limits conceptual predominance to the retrieved corpus and removes the field-wide characterization of implementation-facing work as marginal. Mode counts also cannot establish successful implementation, reproducibility, or engineering effectiveness.

## Source-level chart

| ID / ref. | Publication | Counted mode(s) |
| --- | --- | --- |
| PP01 / [54] | Floriana Ferro (2022)<br>Meeting the Gaze of the Robot: A Phenomenological Analysis on Human–Robot Empathy | conceptual_translation |
| PP02 / [55] | Ingar Brinck; Christian Balkenius (2020)<br>Mutual Recognition in Human–Robot Interaction: A Deflationary Account | design_guidance |
| PP03 / [56] | Tom Poljanšek (2025)<br>Situation Cognition for Social Robotics | agenda_setting |
| PP04 / [57] | Patrick Grüneberg (2024)<br>Intentionality and performance: the phenomenology of gait initiation | methodological_import |
| PP05 / [58] | Jesse Lopes (2023)<br>Can Deep CNNs Avoid Infinite Regress/Circularity in Content Constitution? | critique/limits; design_guidance |
| PP06 / [59] | Jesse D. Lopes (2023)<br>Phenomenology as Proto-Computationalism: Do the Prolegomena Indicate a Computational Reading of the Logical Investigations? | conceptual_translation |
| PP07 / [60] | Dmytro Mykhailov; Nicola Liberati (2023)<br>A Study of Technological Intentionality in C++ and Generative Adversarial Model: Phenomenological and Postphenomenological Perspectives | conceptual_translation |
| PP08 / [61] | Galit Wellner (2022)<br>Digital Imagination, Fantasy, AI Art | conceptual_translation |
| PP09 / [50] | Zbigniew Orbik (2024)<br>Husserl’s concept of transcendental consciousness and the problem of AI consciousness | critique/limits |

### PP01 — Floriana Ferro (2022) [54]

Meeting the Gaze of the Robot: A Phenomenological Analysis on Human–Robot Empathy. Scenari 17, 215–229. https://doi.org/10.7413/24208914136

Assigned mode(s): conceptual_translation. Conceptual translation: Husserlian pairing explains HRI findings. Reviewing robot experiments does not itself constitute methodological import.

Evidence: pp. 218–224, especially Section 2 (pp. 218–222); PDF pp. 4–10. Interprets published HRI findings; no new experiment or implemented control procedure.

Qualification: Stein and Merleau-Ponty also substantially shape the account.

### PP02 — Ingar Brinck; Christian Balkenius (2020) [55]

Mutual Recognition in Human–Robot Interaction: A Deflationary Account. Philosophy & Technology 33, 53–70. https://doi.org/10.1007/s13347-018-0339-x

Assigned mode(s): design_guidance. Design guidance is primary because the paper specifies interaction components and requirements. Its use of existing empirical work is supporting evidence rather than a new study.

Evidence: pp. 62–67, Sections 3–6; especially p. 65 (components) and pp. 66–67 (Husserl); PDF pp. 10–15. Identification, confirmation, and regulated turn-taking are specified as components of mutual recognition; the paper does not report a newly implemented complete recognition system.

Qualification: Conceptual translation is present but subordinate to the explicit design-facing contribution; no additional mode counted.

### PP03 — Tom Poljanšek (2025) [56]

Situation Cognition for Social Robotics. Social Robots with AI: Prospects, Risks, and Responsible Methods, 493–504. https://doi.org/10.3233/FAIA241538

Assigned mode(s): agenda_setting. Agenda setting: the robotics contribution identifies opportunities and risks; its architectural suggestion remains an outlook.

Evidence: pp. 498–500 (Section 4 and beginning of Section 5); pp. 502–503 (Section 6); PDF pp. 6–8, 10–11. Adaptive situation lexicons are a future possibility; no implementation or calibration algorithm is supplied.

Qualification: Design guidance is a plausible broader reading. It is not counted here because the transfer remains underspecified.

### PP04 — Patrick Grüneberg (2024) [57]

Intentionality and performance: the phenomenology of gait initiation. Phenomenology and the Cognitive Sciences, advance-online PDF, 23 pages. https://doi.org/10.1007/s11097-023-09953-8

Assigned mode(s): methodological_import. Methodological import: distinct phenomenological categories are linked to an explicit report-and-score procedure in an actual robotic rehabilitation setting. This is stronger than citing a robot as an illustrative example.

Evidence: PDF pp. 2–7 (Introduction and Section 2), pp. 13–21 (Sections 4–5). Husserlian analysis is connected to previously reported HAL rehabilitation findings: 20 participants, a 26-item questionnaire, and comparison with FIM-M scores. The present article reanalyses prior findings rather than reporting a new trial or a robot designed from Husserl.

Qualification: The empirical findings predate this article. The code does not attribute a new experiment or autonomous subjectivity to HAL.

### PP05 — Jesse Lopes (2023) [58]

Can Deep CNNs Avoid Infinite Regress/Circularity in Content Constitution?. Minds and Machines 33, 507–524. https://doi.org/10.1007/s11023-023-09642-0

Assigned mode(s): critique/limits; design_guidance. Dual coding retains two sustained contributions: critique of content claims and a specified hybrid architectural response. Counting only critique would obscure the implementation-facing part at issue in the review request.

Evidence: pp. 507–510 (regress argument), pp. 516–519 (Section 3), pp. 519–523 (Section 4); PDF pp. 1–4, 10–17. Section 3 proposes a two-system model: statistical learning interacts with a discrete symbolic knowledge system via an update/attractor account. No new code, benchmark, or implemented hybrid is evaluated.

Qualification: The existing corpus already permits dual mode assignment (Cibotaru). A stricter single-primary-code scenario removes design_guidance here; it is reported separately.

### PP06 — Jesse D. Lopes (2023) [59]

Phenomenology as Proto-Computationalism: Do the Prolegomena Indicate a Computational Reading of the Logical Investigations?. Husserl Studies 39, 47–68. https://doi.org/10.1007/s10743-022-09315-3

Assigned mode(s): conceptual_translation. Conceptual translation: the principal contribution is an exegetical and metatheoretical argument. This follows the treatment of computational interpretation in Münch and Tani in the original workbook.

Evidence: pp. 47–50 (Introduction), pp. 64–66 (explanatory example and Conclusion); PDF pp. 1–4, 18–20. Reconstructs a descriptive-to-explanatory relation and uses systematicity as an example; does not implement a computational model or specify an empirical research protocol.

Qualification: A broader reading could code the descriptive-to-explanatory sequence as methodological import; a separate sensitivity scenario reports the resulting change.

### PP07 — Dmytro Mykhailov; Nicola Liberati (2023) [60]

A Study of Technological Intentionality in C++ and Generative Adversarial Model: Phenomenological and Postphenomenological Perspectives. Foundations of Science 28, 841–857. https://doi.org/10.1007/s10699-022-09833-5

Assigned mode(s): conceptual_translation. Conceptual translation: technology descriptions supply examples for a phenomenological account rather than a Husserl-derived construction procedure.

Evidence: pp. 841–843 (scope), pp. 847–852 (computer examples and Conclusion); PDF pp. 1–3, 7–12. C++ and generative adversarial models illustrate inner and outer horizons. The conceptual scheme redescribes technologies; no new GAN architecture, training procedure, or evaluation study is introduced.

Qualification: The inherited language_models field is used in the manuscript's broad language-model/generative-AI sense; this paper concerns GANs, not LLMs.

### PP08 — Galit Wellner (2022) [61]

Digital Imagination, Fantasy, AI Art. Foundations of Science 27, 1445–1451. https://doi.org/10.1007/s10699-020-09747-0

Assigned mode(s): conceptual_translation. Conceptual translation: the layered model clarifies AI-mediated imagination, with existing systems as examples; no procedural phenomenological study is reported.

Evidence: pp. 1445–1450, especially pp. 1446–1447 and pp. 1448–1450; PDF pp. 1–6. The layer/plateau account interprets Sketch RNN and GAN art. Rearranging layers is a conceptual account of variation, not a reported implementation of eidetic variation or a new experiment.

Qualification: Eligible through explicit attribution of Husserlian constructs, despite no direct primary citation. language_models retains the manuscript's generative-AI grouping, not an LLM claim.

### PP09 — Zbigniew Orbik (2024) [50]

Husserl’s concept of transcendental consciousness and the problem of AI consciousness. Phenomenology and the Cognitive Sciences 23, 1151–1170. https://doi.org/10.1007/s11097-024-09993-8

Assigned mode(s): critique/limits. Critique/limits: the dominant contribution examines the warrant for consciousness claims; advocating phenomenology does not supply an operational method.

Evidence: p. 1151 (Abstract), pp. 1165–1167 (discussion and Conclusion); PDF pp. 1, 15–17. Philosophical comparison; no architecture or consciousness test is implemented.

Qualification: The author's ontological position is recorded, not adopted as an eligibility premise.

## Illustrative coding sensitivity

| Scenario | Changed assignment | External methodological/design publications |
| --- | --- | --- |
| Main chart | PP05 has both critique and design; PP06 is conceptual translation | 3/9 (33.3%) |
| Single-primary reading of PP05 | Remove only PP05 design_guidance | 2/9 (22.2%) |
| Broader procedural reading of PP06 | Retain main chart and recode PP06 from conceptual_translation to methodological_import | 4/9 (44.4%) |
| Broader design reading of PP03 | Retain main chart and recode PP03 from agenda_setting to design_guidance | 4/9 (44.4%) |

These are one-change scenarios, not an exhaustive range, confidence interval, or additional findings. They show how contested boundaries can matter in a nine-record set. In particular, a conclusion about the rarity of implemented systems cannot be recovered simply by choosing a stricter primary influence code.

## Provenance and reproducibility

The source inventory, published abstracts, and full-text notes are supplied in external_check_round2.xlsx, with a tabular export in external_check_round2.csv. The original corpus comparison was recomputed from final_results.xlsx, Records sheet, by splitting semicolon-separated mode values. The nine publication titles were checked against rohdaten_combined_20251205_141147.csv and step1_title_screening_combined.xlsx using case- and punctuation-insensitive comparison; no matches were found. This does not establish absence from the Semantic Scholar database itself.

The public repository was inspected on 6 September 2026. It contains the workbooks, API specification, and retrieval scripts, but no standalone protocol file. No retrospective protocol is presented as prospective documentation. The full source texts are not part of the submission attachments.

Repository: https://github.com/HPoschmann/husserl_ai_scoping_review

Companion files: [charting workbook](external_check_round2.xlsx) and [CSV export](external_check_round2.csv).
