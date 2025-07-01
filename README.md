# Untangling of multi-concern commits using SLM

## Tangled Dataset Naming Convention

Each dataset filename is structured to encode its key configuration.

**Format**: `c{N}_t{T}_s{S}_{u|m}_{types}.json`

#### Components
- `c{N}`: number of concerns per sample (e.g., `c2` = 2 concerns)
- `t{T}`: number of concern types available in dataset (e.g., `t4` = 4 types)
- `s{S}`: number of total samples (e.g., `s10` = 10 cases)
- `u` or `m`: concern composition strategy
	- `u`: unique types only (no repeated type in a sample)
	- `m`: mixed types allowed (types can repeat)
- `{types}`: ordered concern type abbreviations

#### Concern Type Abbreviations

The ranking of concern types is based on the classification performance of GPT-4, following the evaluation protocol from [this paper](https://dl.acm.org/doi/10.1145/3691620.3694999). Specifically, the F1 scores achieved by GPT-4 (G4) across concern categories are used to determine the prioritised order.

| Abbrev | Type   |
|--------|--------|
| `ci`   | cicd   |
| `bu`   | build  |
| `do`   | docs   |
| `te`   | test   |
| `fe`   | feat   |
| `fi`   | fix    |
| `re`   | refactor |
| `st`   | style  |

#### Filename Examples

| Filename                          | Description                                         |
| --------------------------------- | --------------------------------------------------- |
| `c2_t2_s10_u_ci_bu.json`          | 2 concerns, 2 types, 10 samples, unique types       |
| `c3_t4_s10_m_ci_bu_do_te.json`    | 3 concerns, 4 types, 10 samples, mixed types        |
| `c3_t5_s10_u_ci_bu_do_te_fe.json` | 3 concerns, 5 types, 10 samples, unique types       |

