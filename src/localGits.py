#!/usr/bin/env python3

import os

from parsers import setup_parser
from pretty_print import *
from pull import *
from push import *
from status import *


def run_status(args, gits):
    untracked = (
        not args.modified and not args.untracked and not args.check_remote
    ) or (args.untracked)

    modified = (
        not args.untracked and not args.modified and not args.check_remote
    ) or args.modified

    exit_code = 0
    for git_name, git_dir in gits:
        exit_code |= report_git_status(
            git_dir,
            git_name,
            args.verbose,
            args.all,
            untracked,
            modified,
            args.check_remote,
        )

    if exit_code == 0 and args.check_remote:
        print(success("No repos are behind their origin."))
    elif exit_code == 0:
        print(success("All repos are pushed."))
    else:
        print()
    return exit_code


def run_pull(args, gits):
    exit_code = 0
    for git_name, git_dir in gits:
        exit_code |= report_pull(
            git_dir,
            git_name,
            args.silent,
            args.all,
        )

    if exit_code == 0:
        print(success("All repos are uptodate."))
    else:
        print()

    return exit_code


def run_push(args, gits):
    untracked = (not args.modified and not args.untracked) or args.untracked
    modified = (not args.untracked and not args.modified) or args.modified

    print("Push")


def main():
    parser = setup_parser(run_push, run_pull, run_status)
    args = parser.parse_args()

    exclude = [] if args.exclude is None else args.exclude

    if env_exclude := os.environ.get("LOCAL_GITS_EXCLUDE_REPO"):
        exclude.extend(env_exclude.split(";"))

    exclude_dirs = os.environ.get("LOCAL_GITS_EXCLUDE_DIR", "").split(";")

    gits = get_git_dirs(args.root, exclude, exclude_dirs)

    if len(gits) == 0:
        print("No local github repos found")
        return 0

    gits.sort(key=lambda x: x[0])

    args.func(args, gits)
    return 0


if __name__ == "__main__":
    exit(main())
