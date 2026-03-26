# Workflow Diagram

```mermaid
flowchart TD
  U[User and client materials]

  subgraph F["Foundation"]
    W01[01-strategy-foundation]
    W02[02-audience-positioning]
    W03[03-content-direction]
  end

  subgraph C["Content and visual direction"]
    W04[04-messaging-framework]
    W05[05-copywriting]
    W06[06-visual-direction]
  end

  subgraph D["Structure and design"]
    W07[07-information-architecture-and-wireframes]
    W08[08-design-system]
    W09[09-high-fidelity-design]
  end

  subgraph I["Implementation and QA"]
    W10[10-technical-architecture]
    W11[11-ai-first-development]
    W12[12-qa-launch-handoff]
  end

  U --> W01
  W01 --> W02
  W01 --> W03
  W02 --> W03
  W02 --> W04
  W03 --> W04
  W03 --> W05
  W04 --> W05
  W01 --> W06
  W04 --> W06
  W05 --> W06
  W03 --> W07
  W05 --> W07
  W06 --> W07
  W06 --> W08
  W07 --> W08
  W05 --> W09
  W07 --> W09
  W08 --> W09
  W03 --> W10
  W08 --> W10
  W09 --> W10
  W05 --> W11
  W08 --> W11
  W09 --> W11
  W10 --> W11
  W11 --> W12
  W01 -. validation reference .-> W12
  W05 -. validation reference .-> W12
  W08 -. validation reference .-> W12
  W09 -. validation reference .-> W12
  W10 -. validation reference .-> W12
```

## Notes

- `03-content-direction` and `06-visual-direction` each pause for user approval before their approved downstream artifacts are finalized.
- `12-qa-launch-handoff` also reviews earlier approved strategy, copywriting, design-system, high-fidelity-design, and technical outputs as validation references.
