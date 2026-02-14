# PIVOTGRAM-92 Canonical Glyph Reference

**Source**: `glyphs/master/PIVOTGRAM_92_MASTER_SHEET_PRINT_LANDSCAPE.svg`  
**Unicode Range**: U+E100–U+E15B  
**Total Glyphs**: 92  
**Status**: Finalized  
**Design**: Audit-Safe · Non-Invertible · Compiler-Stable

---

## How to Read This Document

Each glyph entry contains:
- **Codepoint** — Unicode Private Use Area address
- **Name** — Canonical identifier used in code and audit logs
- **Axis** — Which of the four PIVOTGRAM dimensions this glyph primarily influences
- **Definition** — Fixed semantic scope (what the glyph measures, not what it means)

The four axes of the PIVOTGRAM-92 manifold:

| Axis | What It Measures |
|------|-----------------|
| **Temporal** | When meaning applies; time position and duration |
| **Orientation** | How intent is directed; perspective and agency |
| **Scope** | How broadly meaning applies; scale and reach |
| **Duty** | Whether normative force is claimed; obligation and constraint |

Glyphs influence one primary axis. Logical and error-handling glyphs are cross-axis operators.

---

## Block 1: Temporal Primitives (U+E100–U+E109)

| Codepoint | Name | Axis | Definition |
|-----------|------|------|------------|
| U+E100 | INSTANT | Temporal | A moment with no duration; a discrete point in time |
| U+E101 | DURATION | Temporal | A measured span between two instants |
| U+E102 | EPOCH | Temporal | A reference origin from which time is measured |
| U+E103 | SEQUENCE | Temporal | Ordered succession of events; A before B before C |
| U+E104 | SIMULTANEOUS | Temporal | Two or more events occupying the same instant |
| U+E105 | BEFORE | Temporal | Earlier in sequence relative to a reference point |
| U+E106 | AFTER | Temporal | Later in sequence relative to a reference point |
| U+E107 | DURING | Temporal | Contained within a duration; overlapping in time |
| U+E108 | SINCE | Temporal | From a past point continuing to the present |
| U+E109 | UNTIL | Temporal | From the present continuing to a future boundary |

---

## Block 2: Positional State (U+E10A–U+E10B)

| Codepoint | Name | Axis | Definition |
|-----------|------|------|------------|
| U+E10A | PAST_POSITION | Temporal | A semantic coordinate recorded at a prior instant |
| U+E10B | FUTURE_POSITION | Temporal | A semantic coordinate projected to a later instant |

---

## Block 3: Semantic Act Markers (U+E10C–U+E113)

| Codepoint | Name | Axis | Definition |
|-----------|------|------|------------|
| U+E10C | INTENT | Orientation | The directed purpose behind a semantic act |
| U+E10D | ARTIFACT | Orientation | A produced object carrying encoded meaning |
| U+E10E | ENCODE | Orientation | The act of transforming meaning into transmittable form |
| U+E10F | AGENCY | Orientation | The capacity to initiate a semantic act |
| U+E110 | BELIEF | Orientation | A held semantic position; not yet verified |
| U+E111 | EXPRESSION | Orientation | Externalization of an internal semantic state |
| U+E112 | OBSERVE | Orientation | Reception of meaning without transformation |
| U+E113 | MANIFEST | Orientation | Rendering meaning perceptible across substrate |

---

## Block 4: Scope Markers (U+E114–U+E123)

| Codepoint | Name | Axis | Definition |
|-----------|------|------|------------|
| U+E114 | PRIVATE | Scope | Restricted to a defined set of receivers |
| U+E115 | PUBLIC | Scope | Available to all receivers without restriction |
| U+E116 | SUBJECTIVE | Scope | Bound to a specific perspective or agent |
| U+E117 | OBJECTIVE | Scope | Independent of any specific perspective |
| U+E118 | ATOMIC | Scope | Indivisible semantic unit; cannot be decomposed |
| U+E119 | PHRASE | Scope | Composed unit; two or more atoms in relation |
| U+E11A | SENTENCE | Scope | Complete semantic unit with subject and predicate |
| U+E11B | PARAGRAPH | Scope | Organized collection of sentences sharing a theme |
| U+E11C | DOCUMENT | Scope | Complete structured artifact |
| U+E11D | CORPUS | Scope | Collection of documents treated as a unit |
| U+E11E | NARROW | Scope | Reduced scope; more specific application |
| U+E11F | EXPAND | Scope | Increased scope; broader application |
| U+E120 | LOCAL | Scope | Applies within a bounded context only |
| U+E121 | GLOBAL | Scope | Applies across all contexts without boundary |
| U+E122 | SPECIFIC | Scope | Refers to a particular instance |
| U+E123 | GENERAL | Scope | Refers to a class or category |

---

## Block 5: Governance and Duty (U+E124–U+E12F)

| Codepoint | Name | Axis | Definition |
|-----------|------|------|------------|
| U+E124 | PRIVACY | Duty | The claim that certain meaning is bounded from observation |
| U+E125 | TRANSPARENCY | Duty | The claim that meaning must be accessible to observers |
| U+E126 | AUTONOMY | Duty | The claim that an agent directs its own semantic acts |
| U+E127 | ACCOUNTABILITY | Duty | The claim that an agent answers for its semantic acts |
| U+E128 | DIGNITY | Duty | The claim of inherent, non-negotiable worth |
| U+E129 | AUDIT | Duty | The obligation to make a record available for verification |
| U+E12A | CONSENT | Duty | Agreement that enables a semantic act to proceed |
| U+E12B | DISCLOSURE | Duty | Obligation to make specific meaning known |
| U+E12C | PROTECTION | Duty | Obligation to prevent harm to a semantic state |
| U+E12D | RESPONSIBILITY | Duty | Assigned causal ownership of a semantic act |
| U+E12E | FREEDOM | Duty | Absence of constraint on a semantic act |
| U+E12F | CONSTRAINT | Duty | A defined limit on permissible semantic acts |

---

## Block 6: Logical Operators (U+E130–U+E13F)

| Codepoint | Name | Axis | Definition |
|-----------|------|------|------------|
| U+E130 | AND | Operator | Both conditions must hold simultaneously |
| U+E131 | OR | Operator | At least one condition must hold |
| U+E132 | NOT | Operator | Negation; the condition does not hold |
| U+E133 | IMPLIES | Operator | If first holds, second must hold |
| U+E134 | IFF | Operator | Both hold or neither holds; biconditional |
| U+E135 | XOR | Operator | Exactly one holds; exclusive disjunction |
| U+E136 | NAND | Operator | Not both; at least one fails |
| U+E137 | NOR | Operator | Neither holds |
| U+E138 | UNION | Operator | Combined set of all members |
| U+E139 | INTERSECTION | Operator | Members common to both sets |
| U+E13A | DIFFERENCE | Operator | Members of first not present in second |
| U+E13B | COMPLEMENT | Operator | All members not in the set |
| U+E13C | SUBSET | Operator | All members of first are in second |
| U+E13D | SUPERSET | Operator | First contains all members of second |
| U+E13E | MEMBER | Operator | An element belongs to a set |
| U+E13F | EMPTY | Operator | A set with no members |

---

## Block 7: Transformation Operators (U+E140–U+E146)

| Codepoint | Name | Axis | Definition |
|-----------|------|------|------------|
| U+E140 | PARAPHRASE | Orientation | Restate meaning in different words; form changes, coordinate preserved |
| U+E141 | TRANSLATE | Orientation | Move meaning across language substrates; coordinate preserved |
| U+E142 | SUMMARIZE | Scope | Reduce scope while preserving core coordinate |
| U+E143 | ELABORATE | Scope | Expand scope while preserving core coordinate |
| U+E144 | ADAPT | Orientation | Adjust meaning for a different context or receiver |
| U+E145 | SIMPLIFY | Scope | Reduce complexity while preserving semantic identity |
| U+E146 | FORMALIZE | Duty | Convert informal meaning into structured, verifiable form |

---

## Block 8: Audit Chain (U+E147–U+E14F)

| Codepoint | Name | Axis | Definition |
|-----------|------|------|------------|
| U+E147 | VERIFY | Duty | Confirm that a semantic coordinate matches its record |
| U+E148 | AUDIT_MARKER | Duty | A point in the chain where a snapshot was taken |
| U+E149 | SIGN | Duty | Cryptographic attestation of a semantic state |
| U+E14A | TIMESTAMP | Temporal | A bound record of the instant a semantic act occurred |
| U+E14B | VERIFY_HASH | Duty | Confirm that a hash matches the current state |
| U+E14C | ORIGIN | Temporal | The first recorded position in a semantic chain |
| U+E14D | DESTINATION | Temporal | The intended terminal position in a semantic chain |
| U+E14E | DELTA | Temporal | Measured displacement between two coordinates; ∇I |
| U+E14F | CHECKPOINT | Temporal | A verified snapshot within an ongoing sequence |

---

## Block 9: Governance Lifecycle (U+E150–U+E15B)

| Codepoint | Name | Axis | Definition |
|-----------|------|------|------------|
| U+E150 | CONSENSUS | Duty | Agreement among multiple agents on a coordinate |
| U+E151 | DISSENT | Duty | Recorded disagreement with a coordinate or decision |
| U+E152 | ESCALATE | Duty | Transfer of decision authority to a higher level |
| U+E153 | ARCHIVE | Temporal | Move a semantic state to long-term immutable storage |
| U+E154 | RETRIEVE | Temporal | Access a previously archived semantic state |
| U+E155 | ERROR | Operator | A detected failure in semantic processing |
| U+E156 | RETRY | Operator | Attempt the same semantic operation again |
| U+E157 | FALLBACK | Operator | Revert to a prior valid semantic state |
| U+E158 | ABORT | Operator | Terminate a semantic operation without committing |
| U+E159 | COMMIT | Duty | Finalize a semantic state into the permanent record |
| U+E15A | ROLLBACK | Temporal | Restore a prior checkpoint; reverse committed state |
| U+E15B | DRIFT_MEASURE | Temporal | The computed ∇I value between two audit markers |

---

## Axis Distribution

| Axis | Count |
|------|-------|
| Temporal | 26 |
| Scope | 18 |
| Duty | 21 |
| Orientation | 15 |
| Operator | 12 |
| **Total** | **92** |

---

## Design Properties

**Non-invertible** — A glyph cannot be decoded back to source text.
It records that a semantic act occurred and its coordinate position,
not the content of what was said.

**Compiler-stable** — Glyph identity is bound by PSH-256 topological
hashing. The hash survives rotation, scaling, and redrawing as long
as topology is preserved.

**Audit-safe** — No glyph carries personally identifiable information.
The system records semantic position, not identity.

**Axis-anchored** — Each glyph influences a defined axis in the
four-dimensional manifold. Composition produces a coordinate vector,
not a sentence.

---

## Relationship to PICTOGRAM-256

PIVOTGRAM-92 occupies a separate Unicode range from PICTOGRAM-256.
They are distinct systems with complementary roles.

| System | Range | Role |
|--------|-------|------|
| PICTOGRAM-256 | U+E000–U+E0FF | Expression — what meaning contains |
| PIVOTGRAM-92 | U+E100–U+E15B | Audit — how meaning moved |

PIVOTGRAM-92 does not replace PICTOGRAM-256.
It measures what happens to PICTOGRAM meaning during transformation.

---

## Source

Canonical master sheet:
`glyphs/master/PIVOTGRAM_92_MASTER_SHEET_PRINT_LANDSCAPE.svg`

All glyph names in this document match the labels in the master sheet
exactly. The master sheet is the authoritative reference.
Any discrepancy between this document and the master sheet
should be resolved in favor of the master sheet.
