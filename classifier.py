# Copyright (C) 2024  Coombszy
################################################################################
from exceptions import NoClassifierDefined


class Classifier:
    def __init__(self, target, classifiers, file_extensions):
        if classifiers is None:
            raise NoClassifierDefined(f"target {target} has no classifiers defined")
        self.target = target
        self.config = classifiers
        self.file_extensions = file_extensions

    def resolve(self):
        """Execute classifier(s) and returns true if target has been found"""
        if self.config == []:
            return True

        outputs = []
        for classifier in self.config:
            interim_outputs = []

            if "file_extensions" in classifier:
                interim_outputs.append(
                    self.__handle_file_extensions(classifier["file_extensions"])
                )

            # TODO(Liam): Implement folder in path

            if "not" in classifier:
                interim_classifier = Classifier(
                    self.target, classifier["not"], self.file_extensions
                )
                interim_outputs.append(not interim_classifier.resolve())

            outputs.append(all(interim_outputs))

        return any(outputs)

    def __handle_file_extensions(self, classifier_extensions):
        """Evaluate if file extension was found"""
        for ext in classifier_extensions:
            if ext in self.file_extensions:
                return True
        return False
