import navi_internal
from tools import (
    validate_compromise,
    collect_evidence,
    investigate_analysis,
    reporting,
    full_analysis,
)

# Chip metadata
command = "ForensiX"
use = "A versatile chip for digital forensics tasks like evidence collection and reporting."
aliases = ['forensix', 'fx']

# Chip parameters and help
params = {
    '-help': 'Display help information',
    '-h': 'Display help information',
    '-validate': 'Run validation for compromise.',
    '-collect': 'Collect evidence (disk image, memory dump).',
    '-investigate': 'Perform analysis (timeline, log, memory).',
    '-report': 'Generate forensic report.',
    '-full': 'Run a complete forensic workflow.',
}
help_params = ('-help', '-h')


def print_params() -> None:
    """Prints available parameters for the chip."""
    print(f"{'Parameter':<10} | {'Description'}")
    print("-" * 40)
    for param, description in params.items():
        print(f"{param:<10} | {description}")


def run(arguments=None) -> None:
    """
    Entry point for the ForensiX chip.
    This function is invoked by Navi to execute the chip.
    """
    navi_instance = navi_internal.navi_instance
    user_name = navi_instance.get_user()
    navi_instance.print_message(f"Welcome to ForensiX, {user_name}!")

    if arguments:
        arg_array = arguments.text.split()
        if arg_array:
            arg_array.pop(0)

        if arg_array:
            for arg in arg_array:
                match arg:
                    case x if x in help_params:
                        print_params()
                        return
                    case '-validate':
                        validate_compromise.run()
                        return
                    case '-collect':
                        collect_evidence.run()
                        return
                    case '-investigate':
                        investigate_analysis.run()
                        return
                    case '-report':
                        reporting.run()
                        return
                    case '-full':
                        full_analysis.run()
                        return
                    case _:
                        navi_instance.print_message(f"Invalid parameter: {arg}")
                        return
        else:
            navi_instance.print_message("No parameters provided. Use '-help' to see available options.")
    else:
        navi_instance.print_message("No input received. Use '-help' for guidance.")
