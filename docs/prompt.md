- Create a claude skill for writing infectious disease mathematical, statistical, and machine learning modelling papers by learning from the examples of papers with good writing styles in `writing_styles/papers.csv`.

- First, summarise the writing style of each paper into a dedicated .md file and place them in `writing_styles/`, then consolidate all the styles into a single `skill.md`.

- Each paper's writing style summary should include the following:
    - Structural patterns — How they organize sections, flow between ideas, typical subsection headings
    - Methodology conventions — How they present algorithms, mathematical notation, assumptions
    - Results storytelling — How they interpret findings, frame significance, connect back to research questions
    - Literature integration — Citation style, how they position their work relative to prior work, density of references
    - Voice & tone — Formality level, technical depth, clarity vs. precision trade-offs
    - Domain-specific conventions — Any supervised learning-specific practices (train/test splits discussed, cross-validation choices, etc.)

- The skill should be a consolidation of learnings from the writing styles in `writing_styles/*.md`.
- Where necessary, provide concrete examples. For example, if the model is an SIR model, define what S, I, and R mean and how individuals move between compartments. 