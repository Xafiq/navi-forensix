import navi_internal
from forensix import (
    validate_compromise,
    collect_evidence,
    investigate_analysis,
    reporting,
    full_analysis,
)

# Metadata
command = "ForensiX"
use = "A versatile chip for digital forensics tasks."
aliases = ['forensix', 'fx']

# Parameters
params = {
    'validate': 'Validate compromised systems',
    'collect': 'Collect forensic evidence',
    'investigate': 'Analyze evidence',
    'report': 'Generate forensic reports',
    'full': 'Perform full forensic analysis',
    '-help': 'Display help',
    '-h': 'Display help',
}
help_params = ['-help', '-h']

def print_help():
    print("ForensiX Command Help")
    print("-" * 40)
    for param, description in params.items():
        print(f"{param:<15} - {description}")

def run(arguments=None):
    navi = navi_internal.navi_instance
    user = navi.get_user()
    navi.print_message(f"Welcome to ForensiX, {user}!")

    if not arguments:
        navi.print_message("No arguments provided. Use '-help' for usage.")
        return

    arg_array = arguments.text.split()
    if not arg_array:
        navi.print_message("No arguments provided. Use '-help' for usage.")
        return

    command = arg_array.pop(0)
    if command in help_params:
        print_help()
        return

    match command:
        case 'validate':
            validate_compromise.run()
        case 'collect':
            collect_evidence.run()
        case 'investigate':
            investigate_analysis.run()
        case 'report':
            reporting.run()
        case 'full':
            full_analysis.run()
        case _:
            navi.print_message(f"Unknown command: {command}")
