#!/usr/bin/env python3
# Copyright (C) 2024  Coombszy
################################################################################
from exceptions import MissingScriptsKey
from spinner import Spinner
from config import Config
from classifier import Classifier
from runner import Runner
import subprocess
import os

# Globals
config_path = "config/config.json"
example_config_path = config_path + ".example"


def cli():
    print("You've called the CLI!")
    print("      ... Yeah i'll implement this at somepoint")


def run():
    hooks_repo_path = os.path.dirname(os.path.realpath(__file__))
    config = Config().get_config()
    runners = {}  # All script runners
    exit_code = 0

    with Spinner("Analysing repo..."):
        all_file_extensions = get_all_file_extensions(get_working_repo_path())
        for target, target_config in config["targets"].items():
            if not target_config["enabled"]:
                continue
            c = Classifier(target, target_config["classifiers"], all_file_extensions)
            if c.resolve():
                if "scripts" not in target_config:
                    raise MissingScriptsKey(
                        f"target {target} is missing a `scripts` key in the config"
                    )
                if target not in runners:
                    runners[target] = []
                for script in target_config["scripts"]:
                    script_path = os.path.join(
                        hooks_repo_path, "scripts", target, script
                    )
                    r = Runner(script, script_path)
                    runners[target].append(r)

    with Spinner("Running scripts..."):
        # Start them all
        for target, target_runners in runners.items():
            for r in target_runners:
                r.start()
        # Wait for them all to finish
        for target, target_runners in runners.items():
            for r in target_runners:
                r.finish()

    for target, target_runners in runners.items():
        for r in target_runners:
            print(f"[{target}] {r.script_name} ", end="")
            if r.exit_code != 0:
                exit_code = r.exit_code
                print("FAILED!")
                print(r.stdout)
            else:
                print("OK!")

    return exit_code


if __name__ == "__main__":
    cli()


def get_all_file_extensions(directory):
    file_extensions = []
    for _, _, files in os.walk(directory):
        for file in files:
            file_extension = os.path.splitext(file)[1]
            if file_extension not in file_extensions:
                file_extensions.append(file_extension)
    return file_extensions


# If any elements of a list are in another list
def list_contains_any(list1, list2):
    for element in list1:
        if element in list2:
            return True
    return False


# Get working repo path
def get_working_repo_path():
    return (
        subprocess.run(
            ["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE, check=False
        )
        .stdout.decode("utf-8")
        .strip()
    )
