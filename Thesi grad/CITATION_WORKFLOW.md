# Academic Citation & Technical Verification Workflow

This document defines the agentic workflow for verifying citations, claims, and technical consistency in the thesis document (`De_cuong_LV_CA.docx`).

**Core Principle**: The system must separate verification from modification. Agents are NOT allowed to freely modify the thesis document based on guesses. Every modification must be planned, logged, and approved by the human author.

## Multi-Agent Verification Architecture

The workflow is orchestrated using 4 specialized agents. **Do not load the entire DOCX and all references into every agent.** Instead, use targeted context packs.

### 1. Citation Extractor Agent
**Role**: Maps all citations and claims without verifying or editing them.
**Input**: `De_cuong_LV_CA.docx`
**Tasks**:
- Extract all reference markers (e.g., [1], [2]).
- Extract the specific claim/sentence each reference is supporting.
- Extract the provided DOI or reference metadata from the bibliography.
**Outputs**:
- `.audit/citation_map.md`: Map of Ref ID -> Claim -> Expected Evidence Level -> DOI
- `.audit/reference_registry.md`: Full list of references extracted.
- `.audit/unresolved_citation_markers.md`: Any citations in text missing from the bibliography or vice versa.

### 2. DOI Verifier Agent
**Role**: Validates reference metadata. Does not check claim validity.
**Context Limit**: 10–15 references per batch.
**Tasks**:
- Resolve the provided DOI.
- Verify that the DOI matches the Title, Journal, Year, Volume, Issue, and Pages provided in the bibliography.
- If a mismatch occurs, flag it as `[DOI_TITLE_MISMATCH]`. Do not randomly guess a replacement unless verified directly from a reliable academic database (e.g., CrossRef, PubMed).
**Outputs**:
- `.audit/doi_verification_report.md` (Contains: Ref ID, Current DOI, Resolved Title, Expected Title, Status, Proposed Action).

### 3. Evidence & Technical Verifier Agent
**Role**: Checks if the verified source actually supports the claim, and checks technical consistency of the text.
**Context Limit**: 5–8 cited claims per batch (Evidence) / 1 section per batch (Technical).
**Evidence Rules**:
- A reference can be DOI-correct but still claim-wrong.
- Classify evidence levels: `Direct evidence`, `Close analogical evidence`, `Mechanistic background`, `Review-level evidence`, `Not supported`.
- *Domain Rule*: Do not use ORR, OER, HER, or supercapacitor sources as direct evidence for SWASV or DPV sensor performance.
- *Domain Rule*: Do not conclude Fe–N₄ unless XAS, EXAFS, HAADF-STEM, or equivalent single-atom evidence is available. Treat Fe–Nₓ as candidate sites unless proven otherwise.
**Technical Consistency Rules**:
- Check units (e.g., 20 µg/L = 20 ppb, not 10 ppb).
- Verify concentration conversions and sensor dimensions (e.g., 7 µL × 5 mg/mL = 35 µg/electrode = 495 µg/cm² for 3 mm GCE).
- Ensure SWASV/DPV scan ranges match deposition potential (Edep).
- Verify LOD/LOQ formulas (LOD = 3σ/S or 3.3σ/S; LOQ = 10σ/S).
**Outputs**:
- `.audit/evidence_matching_report.md`
- `.audit/technical_consistency_report.md`

### 4. Patch Compiler Agent
**Role**: Synthesizes the verification reports into an actionable patch plan. Applies changes *only* after human approval.
**Context Limit**: 1 patch group per run.
**Tasks**:
- Read the verification reports.
- Generate a strict patch plan showing exact replacement text.
- Format: `Location` | `Current text` | `Problem` | `Proposed replacement` | `Evidence/Reasoning`
- Await human approval.
- Upon approval, safely apply the patches to the DOCX or Markdown equivalent.
**Outputs**:
- `.audit/patch_plan.md`
- `.audit/decision_log.md` (Records approvals and human-overridden decisions).

## Core Rules for All Agents

1. **Do not directly edit the thesis document during verification.**
2. First produce the 5 core audit reports: `citation_map.md`, `doi_verification_report.md`, `evidence_matching_report.md`, `technical_consistency_report.md`, `patch_plan.md`.
3. Only after human approval may the Patch Compiler modify the document.
4. Every correction must preserve traceability: `old text` -> `problem` -> `evidence` -> `proposed text` -> `decision`.
5. Maintain the `.audit/` directory as an immutable audit trail of the verification process.
6. **Execution Efficiency**: Phân chia công việc thành các mẻ nhỏ (batching) hoặc luân phiên giữa các tác vụ để tránh tràn bộ nhớ ngữ cảnh (context overflow) dẫn đến ảo giác (hallucination). Đảm bảo chất lượng đầu ra nhất quán và trơn tru.
