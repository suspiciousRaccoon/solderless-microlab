from abc import ABC, abstractmethod

class GRBL:

    @abstractmethod
    def grblWrite(self, command, retries=3):
        """
        Writes the gcode command to grbl

        :param command:
            The raw gcode command string. Each command must end with a newline character
        :param retries:
            Number of times to retry the command should it fail.
            default is 3
        :return:
            None
        """
        pass
