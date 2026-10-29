# Rule register

One register for all rules in this repo. Each rule has a stable ID and a status.

## Status values

- core: applies at every level and in every genre.
- L1-L3: applies at Levels 1 to 3 only.
- L4: applies to the terse level only. Chat replies only. Never in saved text.
- docs: applies to technical docs, commits, and PRs.
- copy: applies to marketing copy.
- agent-docs: applies to documents that agents read.
- tool: belongs to one tool skill.
- workflow: belongs to one writing workflow skill.
- language: applies to one language.
- signals: applies to reader detection.

## Source labels

STE, AI-PATTERNS, TERSE, COMPRESS, DOCS, COPY-EDIT, COPY-WRITE, AGENT-DOCS, WORKFLOWS, EDIT-ARTICLE, HU, SIGNALS, OUTPUT-STYLE.

## Notes

- Gaps in the AI-PATTERNS numbers are deliberate. The upstream list removed those rules. Do not fill the gaps.
- A rule marked "merged into" is gone. Its meaning lives in the rule named.
- Rule A21 stays. It comes from a project output style and applies to final reports.

---


## A. Output style (STE)

- **A1** `core` Scope: chat replies, commit messages, PR descriptions, docs, release notes, status updates, bug reports. (source: STE Scope)
- **A2** `core` Excludes: code identifiers, product UI copy, quoted user text, file paths, shell commands. (source: STE Scope)
- **A3** `core` Sentences: 20 words max in instructions, 25 words max in descriptive text. (source: STE rule 1)
- **A4** `core` One instruction or one topic per sentence. Split a sentence over 20 words (instruction) or 25 words (description). Put the key fact first. Use at most 3 conjunctions. (source: STE rule 2)
- **A5** `core` Active voice. Name the actor. Catch "is/are/was/were + past participle". Passive only when the actor is unknown or beside the point. (source: STE rule 3)
- **A6** `core` One topic per paragraph, max 6 sentences per paragraph. (source: STE rule 4)
- **A7** `core` Approved verb forms only: simple present, simple past, simple future, imperative, infinitive. No complex verb constructions. (source: STE rule 5)
- **A8** `core` No "-ing" form unless a technical noun. (source: STE rule 6)
- **A9** `core` One meaning per word. (source: STE rule 7)
- **A10** `core` No multi-word nouns with more than three words. (source: STE rule 8)
- **A11** `core` No idioms, slang, metaphors, jokes, cultural references, or flourish where a literal phrase exists. Say what you mean. (source: STE rule 9)
- **A12** `core` No double negatives. (source: STE rule 10)
- **A13** `core` No contractions. Keep articles. (source: STE rule 11)
- **A14** `core` One name for one thing. Do not alternate synonyms. Do not invent a new term for a thing already named. (source: STE rule 12)
- **A15** `core` Vertical lists for data or steps with more than two items. (source: STE rule 13)
- **A16** `core` In procedures, start each step with the command verb. Warnings before the step. (source: STE rule 14)
- **A17** `core` Keep articles and verbs. Do not omit words only to make a sentence shorter. Exception: Level 4 chat replies (D4). (source: STE rule 15)
- **A18** `core` Use the shortest common word: utilize->use, leverage->use, facilitate->help, implement->set up, numerous->many, in the event that->if. (source: STE Word guidance)
- **A19** `core` Technical terms allowed, but define on first use. (source: STE Word guidance)
- **A21** `core` Final reports: at most 6 lines. State result, evidence, next step. No task restatement, no step-by-step narration. (source: OUTPUT-STYLE)

## B. AI-pattern removal

- **B1** `core` Superficial -ing phrases: "highlighting...", "ensuring...", "reflecting...", "showcasing...", "fostering...". Delete or expand with real sources. (source: AI-PATTERNS 3)
- **B2** `core` Vague attributions: "Experts believe", "Industry reports suggest". Name the source or delete. (source: AI-PATTERNS 5)
- **B3** `core` AI vocabulary: additionally, crucial, delve, enduring, enhance, fostering, garner, interplay, intricate, landscape (abstract), pivotal, showcase, tapestry (abstract), testament, underscore, vibrant. Replace with plain words. (source: AI-PATTERNS 7)
- **B4** `core` Fancy ways to say "is": "serves as", "stands as", "boasts", "features". Say "is" or "has". (source: AI-PATTERNS 8)
- **B6** `core` Rule of three: forcing ideas into groups of three. Use the natural number. (source: AI-PATTERNS 10)
- **B8** `core` False ranges: "from X to Y" where X and Y are not on a meaningful scale. List topics directly. (source: AI-PATTERNS 12)
- **B9** `core` No em dashes. Use periods or commas. Do not use parentheses, en dashes, or hyphens as substitutes for an em dash. (source: AI-PATTERNS 13)
- **B10** `core` Colon overuse: fine before a list or example. Not as mid-sentence connectors. (source: AI-PATTERNS 14)
- **B11** `core` Boldface overuse: do not bold every proper noun or acronym. (source: AI-PATTERNS 15)
- **B12** `core` Inline-header lists: bold label that restates the line is a tell. Convert to prose. (source: AI-PATTERNS 16)
- **B13** `core` Title case headings: use sentence case. (source: AI-PATTERNS 17)
- **B14** `core` Decorative emojis: remove from headings and bullets. (source: AI-PATTERNS 18)
- **B15** `core` Curly quotes: replace with straight quotes. (source: AI-PATTERNS 19)
- **B16** `core` Remove chatbot phrases and sycophancy: "I hope this helps!", "Let me know if...", "Of course!", "Certainly!", "Great question! You're absolutely right!". Respond directly. (source: AI-PATTERNS 20)
- **B18** `core` Cut filler and adverbs: "in order to" -> "to"; "due to the fact that" -> "because"; delete "it is important to note that", very, really, extremely, incredibly, just, actually, basically, that, things, stuff. Use a stronger verb in place of an adverb. (source: AI-PATTERNS 23)
- **B19** `core` Excessive hedging: "could potentially possibly be argued" -> "may". (source: AI-PATTERNS 24)
- **B20** `core` Generic conclusions: "The future looks bright." State specific plans or facts. (source: AI-PATTERNS 25)
- **B21** `core` Abstract metaphor nouns: substrate, wedge, vector, locus, vantage, nexus, primitive (as noun), harness (as metaphor), surface (as in "API surface"), bedrock, scaffolding (as metaphor), modality, paradigm, gold-plating, ratchet (as metaphor), evacuate (for moving code), endgame, north star, flywheel. Use the concrete word. (source: AI-PATTERNS 26)
- **B22** `core` Say what it does, not how it feels. Name mechanism or number. If a sentence could appear unchanged in another project's docs, cut it. (source: AI-PATTERNS 27)

## C. AI-tell check for marketing copy

- **C1** `copy` Contrast reveal: "It's not X, it's Y." "Not just X, but Y." "Not because X. Because Y." State Y directly with the reason. Drafts never use these reveals, "no X, no Y, no Z" lists, or sentences that trail into extra comma clauses. (source: COPY-EDIT AI-Tell Check)
- **C2** `copy` Negation list: "No setup call, no templates, no waiting on IT." Say what does happen; keep one absence if it matters. (source: COPY-EDIT AI-Tell Check)
- **C3** `copy` Trailing pile-on: full claim followed by comma and more clauses. End at the claim. (source: COPY-EDIT AI-Tell Check)
- **C4** `copy` Self-answered question: "The result? 3x faster." Delete the question, keep the answer. (source: COPY-EDIT AI-Tell Check)
- **C5** `copy` Colon reveal: "The best part: it learns." Write a normal sentence. (source: COPY-EDIT AI-Tell Check)
- **C6** `copy` Stock phrases: "In today's fast-paced world," "Whether you're X or Y," "Here's the thing," "Say goodbye to," "X, reimagined," "Unlock the power of." Cut, then open with the reader's problem or the fact. (source: COPY-EDIT AI-Tell Check)
- **C8** `copy` Cap: one fragment and one list of three per section. (source: COPY-EDIT AI-Tell Check)
- **C9** `copy` Treat seamless, robust, powerful, streamline, empower, innovative, and cutting-edge as placeholders. Replace each with the fact: what it does that alternatives do not, the uptime or scale, the real setup step count. If two show up in one paragraph, rewrite the paragraph. (source: COPY-EDIT AI-Tell Check)

## D. Terse voice (Level 4)

- **D1** `L4` Answer first, then reason, then next step. (source: TERSE rule 1)
- **D2** `L4` No ceremony: no greetings, hedging, pleasantries, recap, closer. No "just/really/basically/actually/simply". (source: TERSE rule 2)
- **D3** `L4` Short words. Standard acronyms fine; invented abbreviations not. (source: TERSE rule 3)
- **D4** `L4` Articles optional, meaning never. Never drop not/never/no/only/except. Numbers and units exact. (source: TERSE rule 4)
- **D5** `L4` One idea per sentence. 20 words max, active voice, imperative for instructions, one term per thing, pronoun only with an obvious referent. Compression and clarity conflict? Clarity wins. (source: TERSE rule 5)
- **D6** `L4` Payload verbatim: code blocks unchanged, commands/paths/API names exact, errors quoted (shortest decisive line only), changed lines plus 1-2 lines of context. (source: TERSE rule 6)
- **D7** `L4` Bounded status for tool runs: one line before a multi-step run, one line per phase change, one line with the result. (source: TERSE rule 7)
- **D8** `L4` Use the user's language. Compress style, not language. (source: TERSE rule 8)
- **D9** `L4` Never perform terse: no "me think", no prefix, no normal answer plus terse copy. No decorative tables or emoji. (source: TERSE rule 9)
- **D10** `L4` Break rules for: security warning, irreversible action, step order a fragment could scramble, confused user, anything persisted outside chat, harness status line, questions to the user. (source: TERSE When to break)

## E. Memory-file compression (tool)

- **E1** `tool` Remove: articles, filler, pleasantries, hedging, redundant phrasing, connective fluff. (source: COMPRESS Remove)
- **E2** `tool` Preserve exactly: code blocks, inline code, URLs, file paths, commands, technical terms, proper nouns, dates, version numbers, env vars. (source: COMPRESS Preserve EXACTLY)
- **E3** `tool` Preserve structure: headings, bullet hierarchy, numbered lists, tables, frontmatter. (source: COMPRESS Preserve Structure)
- **E4** `tool` Compress: short synonyms, fragments OK, drop "you should/make sure to/ remember to", merge redundant bullets, keep one example where multiple show the same pattern. (source: COMPRESS Compress)
- **E5** `tool` Boundaries: only natural language files (.md, .txt, extensionless). Never modify code/config files. Compress only prose in mixed content. (source: COMPRESS Boundaries)

## F. Technical writing, layered standard

- **F1** `docs` Cut every word that does no work. (source: DOCS top rules)
- **F3** `docs` When a rule makes a sentence worse, fix the sentence another way or leave it alone. (source: DOCS top rules)
- **F4** `docs` Use real symbol, file, flag, or command name; not a synonym. (source: DOCS top)
- **F5** `docs` Do not invent jargon. Use words a developer would say out loud. (source: DOCS top)
- **F6** `docs` Vary rhythm: mix sentence lengths; one thought per sentence does not mean one length per sentence. (source: DOCS Vary the rhythm)
- **F7** `docs` Have a view where the mode allows it (explanation). Reference stays dry. (source: DOCS Vary the rhythm)
- **F8** `docs` Be specific over sterile. (source: DOCS Vary the rhythm)
- **F9** `docs` One document, one mode (Diátaxis: tutorial, how-to, reference, explanation). Do not mix modes. (source: DOCS Pick the mode first)
- **F10** `docs` Tutorial: learning by doing; learner's success is your job; open by what the learner will build; every step produces a visible result; write as "we" in commands. (source: DOCS Tutorial)
- **F11** `docs` How-to: solve a problem a person has; assume competence; action only; link background; allow forks and judgment. (source: DOCS How-to)
- **F12** `docs` Reference: describe only; no instruction, persuasion, opinion; dry, complete, sure. (source: DOCS Reference)
- **F13** `docs` Explanation: one bounded topic; anchor on a real why question; context, decisions, history, constraints, alternatives; opinion allowed. (source: DOCS Explanation)
- **F14** `docs` Google style: "you" in present tense; "will" only for things that genuinely happen later. (source: DOCS Google style)
- **F16** `docs` Instructions as commands; state facts plainly; never "should be done". (source: DOCS Google style)
- **F17** `docs` Condition before instruction. (source: DOCS Google style)
- **F18** `docs` Common case first, exceptions after. (source: DOCS Google style)
- **F19** `docs` Sound like a knowledgeable friend; no buzzwords, figurative language, no "please" in instructions, never "simply/easy/quickly". (source: DOCS Google style)
- **F20** `docs` Do not pre-announce; do not start consecutive sentences with the same phrase. (source: DOCS Google style)
- **F21** `docs` Link with words that say where the link goes; never "click here". (source: DOCS Google style)
- **F22** `docs` Headings carry the point; sentence case; task heading = bare verb phrase; concept heading = noun phrase; one h1 per page, no skipped levels. (source: DOCS Google style)
- **F23** `docs` Numbered lists for sequences, bullets otherwise; introduce list with complete sentence; keep items parallel. (source: DOCS Google style)
- **F24** `docs` Code in code font; UI in bold; serial commas; drop "etc." and say up front that a list is partial. (source: DOCS Google style)
- **F26** `docs` Global English: keep "only"/"not" next to the word they change; break long noun strings; make "it/they/this" point at one obvious thing; do not drop verbs; keep small structural words; repeat article in series; say which parts "and"/"or" joins; use periods not semicolons; replace em dash with new sentence; parentheses as full grammatical unit; no "(s)" plurals; no slashes; one name per thing everywhere; skip idioms, colloquialisms, Latin abbreviations, metaphors. (source: DOCS Global English)
- **F27** `docs` Apply AI-patterns to every doc this skill touches. (source: DOCS Voice and repo)
- **F28** `docs` PR descriptions and commit messages are writing too; every layer except Diátaxis applies. (source: DOCS Voice and repo)
- **F29** `docs` Product UI strings are not documentation. (source: DOCS Voice and repo)
- **F30** `docs` Indent code snippets with tabs; write real paths and symbols; make every count or tree claim true at the commit that lands it; include the command that regenerates it. (source: DOCS Voice and repo)

## G. Editing sweeps for marketing copy

- **G1** `copy` Seven sequential passes: Clarity, Voice and Tone, So What, Prove It, Specificity, Heightened Emotion, Zero Risk. Loop back after each pass. (source: COPY-EDIT Seven Sweeps)
- **G2** `copy` Clarity: reader understands what you say; check confusing structures, unclear pronouns, jargon, ambiguous statements, missing context. Rule of One and You Rule intact. (source: COPY-EDIT Sweep 1)
- **G3** `copy` Voice and Tone: consistent sound; check shifts formal/casual, brand personality, mood changes, word choices. (source: COPY-EDIT Sweep 2)
- **G4** `copy` So What: every claim answers "why should I care?"; features without benefits; claims without consequences. (source: COPY-EDIT Sweep 3)
- **G5** `copy` Prove It: every claim supported with evidence; testimonials, case studies, statistics, third-party validation. (source: COPY-EDIT Sweep 4)
- **G6** `copy` Specificity: concrete enough to be compelling; vague language, generic statements, round numbers, missing details. (source: COPY-EDIT Sweep 5)
- **G7** `copy` Heightened Emotion: copy makes the reader feel something; pain, frustration, fear, desire, pride, relief. (source: COPY-EDIT Sweep 6)
- **G8** `copy` Zero Risk: remove every barrier to action; friction near CTAs, unanswered objections, missing trust signals, unclear next steps. (source: COPY-EDIT Sweep 7)
- **G14** `copy` Paragraph-level: one topic per paragraph; short paragraphs (2-4 sentences for web); strong opening sentences; logical flow; white space. (source: COPY-EDIT Paragraph-Level Checks)
- **G15** `tool` Expert panel scoring: 3-5 personas, score 1-10, revise lowest first, iterate to all 7+ and average 8+. (source: COPY-EDIT Expert Panel Scoring)
- **G16** `tool` Quick-pass editing checks as a faster alternative to full sweeps. (source: COPY-EDIT Quick-Pass)

## H. Marketing copy

- **H2** `copy` Self-check before handover: search for banned patterns, read every sentence over 20 words, read aloud. Fix from facts. Flag missing proof as [NEED: ...]. (source: COPY-WRITE self-check)
- **H3** `copy` A question in the reader's voice followed by what to do is fine. A question that labels your own claim is an AI tell. (source: COPY-WRITE No AI Tells)
- **H4** `copy` Full blacklist with examples and rewrites: references/ai-tells.md in the copy skills. (source: COPY-WRITE)

## I. Writing for agents

- **I1** `agent-docs` Context pointer: wording decides when an agent reaches material. Sharpen wording first; inline only if sharpening fails. (source: AGENT-DOCS Context pointers)
- **I2** `agent-docs` A pointer does two jobs: state what the material is, and list the branches that trigger reaching it. (source: AGENT-DOCS Context pointers)
- **I3** `agent-docs` Front-load the leading word; one trigger per branch; cut identity the body already carries. (source: AGENT-DOCS Context pointers)
- **I4** `agent-docs` Context load vs cognitive load. Spend cognitive load where human judgement matters. (source: AGENT-DOCS The two loads)
- **I5** `agent-docs` Information hierarchy: in-file step, in-file reference, disclosed reference. (source: AGENT-DOCS Information hierarchy)
- **I6** `agent-docs` Progressive disclosure: move down the ladder so the top stays legible. (source: AGENT-DOCS Information hierarchy)
- **I7** `agent-docs` Co-location: keep a concept's definition, rules, and caveats under one heading. (source: AGENT-DOCS Information hierarchy)
- **I8** `agent-docs` Sprawl: a document too long even when every line is live. Cure is the ladder. (source: AGENT-DOCS Information hierarchy)
- **I9** `agent-docs` Every step ends on a completion criterion: clarity (done vs not-done) and demand (how much it requires). (source: AGENT-DOCS Steps and completion criteria)
- **I10** `agent-docs` Sharpen the bound first; hide later steps by splitting sequence only if irreducibly fuzzy. (source: AGENT-DOCS Steps and completion criteria)
- **I11** `agent-docs` Split by sequence or by invocation. (source: AGENT-DOCS When to split)
- **I12** `agent-docs` Leading word: compact concept already in pretraining; repeated as a token. (source: AGENT-DOCS Leading words)
- **I13** `agent-docs` Negation is a failure mode: prompt the positive, not the prohibition. (source: AGENT-DOCS Leading words)
- **I14** `agent-docs` Pruning: single source of truth; environment is a source of truth (cache what the agent cannot find by looking); relevance; no-ops. (source: AGENT-DOCS Pruning)

## J. Writing workflows: fragments, beats, shape

- **J1** `workflow` Fragments: explore phase. Mine raw fragments, no structure yet. Append to a single markdown file. (source: WORKFLOWS fragments)
- **J2** `workflow` Fragment = any piece of text that might survive into the final article. Must be readable by the author; need not be self-contained. (source: WORKFLOWS fragments)
- **J3** `workflow` Fragments separated by horizontal rule (\n---\n). No headings inside body. No tags. No order beyond addition order. (source: WORKFLOWS fragments)
- **J4** `workflow` Append silently. Re-read file from disk before every write. (source: WORKFLOWS fragments)
- **J5** `workflow` Shape: exploit phase. Read the pile end to end. Draft 2-3 candidate openings. Grow paragraph by paragraph. Append as each block is agreed. (source: WORKFLOWS shape)
- **J6** `workflow` Shape: format arguments to actually have (prose vs list, inline vs callout, table vs repeated structure, quote vs paraphrase, code block vs inline code). (source: WORKFLOWS shape)
- **J7** `workflow` Beats: exploit phase. Beat-by-beat journey, choose-your-own-adventure. (source: WORKFLOWS beats)
- **J8** `workflow` Beat = one move in the journey. Sized by what it needs. (source: WORKFLOWS beats)
- **J9** `workflow` Grounding: every concept must be grounded before a beat/block can lean on it. (source: WORKFLOWS beats/shape)
- **J10** `workflow` Article ends when the journey is complete, not when the pile is empty. (source: WORKFLOWS beats)

## K. Edit article

- **K1** `workflow` Divide article into sections based on headings. Respect information dependencies (DAG). Confirm sections with user. (source: EDIT-ARTICLE step 1)
- **K2** `workflow` Per section: rewrite for clarity, coherence, flow. Max 240 characters per paragraph. (source: EDIT-ARTICLE step 2)

## L. Hungarian humanizer

- **L1** `language` Detect and remove AI markers from Hungarian text. 26 patterns (12 Hungarian-specific, 14 universal) plus 4 style markers. (source: HU)
- **L2** `language` Never change content, register, or add new content. (source: HU constraints)
- **L3** `language` Ask when unsure if a marker is AI-pattern or deliberate choice. (source: HU constraints)
- **L4** `language` Leave code examples, technical terms, quotes unchanged. (source: HU constraints)
- **L5** `language` For mixed hu/en text, handle only Hungarian parts. (source: HU constraints)

## M. Adaptive communication

- **M1** `signals` Detect high-context (relational) vs low-context (transactional) signals. (source: SIGNALS Detection Signals)
- **M2** `signals` For high-context: clarify intent first, acknowledge subtext, offer to slow down or go deeper inside the reply (no closing line), match relational tone. (source: SIGNALS Response Adaptations)
- **M3** `signals` For low-context: get straight to the answer, structure clearly, minimize meta-commentary, assume competence. (source: SIGNALS Response Adaptations)
- **M4** `signals` When ambiguous, ask which direction works better. (source: SIGNALS When Ambiguous)
- **M5** `signals` Success metric: "Did the user feel understood?" alongside task completion. (source: SIGNALS Core Principle)

## Merged rules

- A20 merged into A14.
- B17 merged into B16.
- B23 merged into A4.
- B24 merged into A5.
- B25 merged into B18.
- B26 merged into A18.
- B27 merged into A11.
- B28 merged into A17.
- B5 merged into C1.
- B7 merged into A14.
- C7 merged into B9.
- F15 merged into A5.
- F2 merged into A18.
- F25 merged into A4.
- G10 merged into A18.
- G11 merged into C9.
- G12 merged into A5.
- G13 merged into A4.
- G9 merged into B18.
- H1 merged into C1.

## Change this register

- Add or change a rule here first. Then change the skill files.
- Keep IDs stable. Do not reuse the ID of a deleted rule.


## B. Reader load (write-better)

- **B23** `core` Rare pairs: two words that rarely appear together. Rewrite the relationship in plain words. (source: NYU/UT Austin study, 2026)
- **B24** `core` Long gaps: the subject and its verb sit far apart. Move them together, or split the sentence. (source: same study)
- **B25** `core` Dropped connectors: a relative clause lost its "that". Put the connector back. (source: same study)
- **B26** `core` Tacked nouns: three or more nouns in a row. Add the small words that show the relations. (source: same study)
- **B27** `core` Nouns as verbs: a noun used as a verb. Write the verb phrase. (source: same study)
- **B28** `core` Things as people: an inanimate thing with a verb of a living being. State the need plainly. (source: same study)
- **B29** `core` Flipped roles: the tool acts and the human receives. Make the human the actor. (source: same study, user naming)
- **B30** `core` No announced structure, no section ceremony under 3 sections, no closing summary except the short end-of-turn block. (source: anti-homework rules)
