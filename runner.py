# Copyright (C) 2024  Coombszy
################################################################################
from multiprocessing import Process, Pipe
import os
import subprocess


class Runner:
    def __init__(self, script, target_script_path):
        self.script_name = script
        self.target = target_script_path
        self.exit_code = 0
        self.stdout = None

    def run_script(self, sender):
        os.system(f"chmod +x {self.target}")
        result = subprocess.run(
            self.target, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False
        )

        output = {"stdout": None, "exit_code": 0}
        output["stdout"] = result.stdout.decode("utf-8")
        if result.returncode != 0:
            output["exit_code"] = 1
        sender.send(output)

    def start(self):
        sender, receiver = Pipe()
        self.receiver = receiver
        self.proc = Process(target=self.run_script, args=(sender,))
        self.proc.start()

    def finish(self):
        self.proc.join()
        output = self.receiver.recv()
        self.exit_code = output["exit_code"]
        self.stdout = output["stdout"]
