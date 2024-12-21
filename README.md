# ForensiX Chip

ForensiX is a versatile forensic tool designed for digital investigations. It supports the following workflows:

- **Validate Compromised**: Interview, live response commands, triage.
- **Collect Evidence**: Triage script collection, disk imaging, memory dumping.
- **Investigation and Analysis**: Log analysis, timeline building, memory inspection.
- **Reporting**: Generate a comprehensive forensic report.
- **Full Workflow**: Combine all tasks into a single process.

## Installation
1. Clone the repository.
2. Install dependencies: `pip install -r chip-requirements.txt`.
3. Refresh Navi chips: `navi chips refresh`.
4. Install the chip: `navi chip install ForensiX`.

## Usage
Run the following commands in Navi:
- `forensix -help`: Show available options.
- `forensix -validate`: Validate compromise.
- `forensix -collect`: Collect evidence.
- `forensix -investigate`: Analyze collected evidence.
- `forensix -report`: Generate a report.
- `forensix -full`: Run the full forensic workflow.

