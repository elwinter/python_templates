#!/usr/bin/env python


"""Template for a standalone Python  script.

This is a template for a standalone Python script. The function
primary_script_code() contains the main script logic, and it can be called
from other Python code.

Authors
-------
Eric Winter
"""


# Import standard modules.
import argparse
import copy
import sys

# Import 3rd-party modules.

# Import project modules.


# Program constants

# Program description
DESCRIPTION = "Template for standalone Python script."

# Default values for command-line arguments.
DEFAULT_ARGUMENTS = {
    "debug": False,
    "verbose": False,
    "positional_arg": None,
}


def create_command_line_parser():
    """Create the command-line parser.

    Create the parser for the command-line.

    Parameters
    ----------
    None

    Returns
    -------
    parser : argparse.ArgumentParser
        Command-line parser for this script.

    Raises
    ------
    None
    """
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "--debug", "-d",
        default=DEFAULT_ARGUMENTS["debug"],
        action="store_true",
        help="Print debugging output (default: %(default)s)."
    )
    parser.add_argument(
        "--verbose", "-v",
        default=DEFAULT_ARGUMENTS["verbose"],
        action="store_true",
        help="Print verbose output (default: %(default)s)."
    )
    parser.add_argument(
        "positional_arg",
        default=DEFAULT_ARGUMENTS["positional_arg"],
        help="First positional argument (default: %(default)s)"
    )
    return parser


def primary_script_code(**kwargs) -> int:
    """Primary code for this script.

    Primary code for this script. This structure allows this function to be
    called from other Python code.

    Parameters
    ----------
    kwargs : dict
        Dictionary of keyword arguments.

    Returns
    -------
    int 0 on success, otherwise Exception is raised by called code.

    Raises
    ------
    None
    """
    # Set defaults for command-line options, then update with values passed
    # from the caller.
    local_args = copy.deepcopy(DEFAULT_ARGUMENTS)
    local_args.update(kwargs)
    args = local_args

    # Local convenience variables.
    debug = args["debug"]
    verbose = args["verbose"]
    positional_arg = args["positional_arg"]
    if debug:
        print(f"debug = {debug}")
        print(f"verbose = {verbose}")
        print(f"positional_arg = {positional_arg}")

    # ------------------------------------------------------------------------

    # MAIN SCRIPT CODE GOES HERE.

    # ------------------------------------------------------------------------

    # Return normally.
    return 0


def main() -> None:
    """Driver for command-line version of code.

    This is the main function for the command-line version of this file. It
    processes the command-line arguments and calls the primary script code.

    Parameters
    ----------
    None

    Returns
    -------
    return_code : int
        Return code from primary script code.

    Raises
    ------
    None
    """
    # Create the command-line parser.
    parser = create_command_line_parser()

    # Parse the command-line arguments.
    args = parser.parse_args()
    if args.debug:
        print(f"args = {args}")

    # Convert the arguments from Namespace to dict.
    args = vars(args)

    # Call the main program code.
    return_code = primary_script_code(**args)
    sys.exit(return_code)


# This is the entry point for this file run as a standalone script.
if __name__ == "__main__":
    main()
