################################################################################
import sys
import threading
import itertools
import time


class Spinner:
    def __init__(self, message, delay=0.05, done_suffix="DONE!"):
        self.spinner = itertools.cycle(
            ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        )
        self.delay = delay
        self.busy = False
        self.spinner_visible = False
        self.done_suffix = done_suffix
        self.back_padding = len(done_suffix)
        sys.stdout.write(message)

    def write_next(self):
        with self._screen_lock:
            if not self.spinner_visible:
                sys.stdout.write(
                    " " + next(self.spinner) + (self.back_padding - 2) * " "
                )
                self.spinner_visible = True
                sys.stdout.flush()

    def remove_spinner(self, cleanup=False):
        with self._screen_lock:
            if self.spinner_visible:
                sys.stdout.write(self.back_padding * "\b")
                self.spinner_visible = False
                if cleanup:
                    sys.stdout.write(self.done_suffix)  # overwrite spinner with blank
                    sys.stdout.write("\r")  # move to next line
                sys.stdout.flush()

    def spinner_task(self):
        while self.busy:
            self.write_next()
            time.sleep(self.delay)
            self.remove_spinner()

    def __enter__(self):
        if sys.stdout.isatty():
            self._screen_lock = threading.Lock()
            self.busy = True
            self.thread = threading.Thread(target=self.spinner_task)
            self.thread.start()

    def __exit__(self, exc_type, exc_val, exc_traceback):
        _ = (exc_type, exc_val, exc_traceback)  # Do not use
        if sys.stdout.isatty():
            self.busy = False
            self.remove_spinner(cleanup=True)
        else:
            sys.stdout.write("\r")
        time.sleep(self.delay)
        print()
