from . import (
    validate_compromise,
    collect_evidence,
    investigate_analysis,
    reporting,
)

def run():
    print("Starting full forensic workflow...")
    validate_compromise.run()
    collect_evidence.run()
    investigate_analysis.run()
    reporting.run()
    print("Full forensic workflow completed.")
