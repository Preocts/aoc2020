"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day 4 part a

I am purposely NOT using regex for this one
"""
import sys


class Passport_Validation(object):
    """Process a batch of passports

    Providing a batch file when declaring will process that batch file
    and populate the attributes.

    Note: Do not hack >:V

    Attributes:
        batch_file [str]: Batch of passports
        valid [int]     : # of passports that are valid
        invalid [int]   : # of passports that are invalid
        processed [bool]: Indicates if batch has been processed
    """

    def __init__(self, batch_file: str = "") -> None:
        """ Initialize """
        self.reset()
        self.batch_file = batch_file
        return None

    def __str__(self) -> str:
        return self.batch_file

    def __bool__(self) -> bool:
        return True if self.processed else False

    @property
    def batch_size(self) -> int:
        """ Number of passports in loaded batch """
        return len(self._split_file()) if self.processed else 0

    def process_batch(self, hacked: bool = False) -> None:
        """ Processes loaded batch file """
        self.reset()
        batch_file = self._split_file()
        validation = "byr iyr eyr hgt hcl ecl pid cid".split()
        if hacked:
            validation = "byr iyr eyr hgt hcl ecl pid".split()

        for passport in batch_file:
            valid = True
            for value in validation:
                if value not in passport:
                    valid = False
                    break
            if valid:
                self.valid += 1
            else:
                self.invalid += 1

        self.processed = True
        return None

    def _split_file(self) -> tuple:
        """ Split file by empty lines """
        split_file = []
        for line in self.batch_file.split("\n"):
            if not line:
                split_file.append("~")
                continue
            split_file.append(line)
        join_file = " ".join(split_file)
        return join_file.split("~")

    def reset(self) -> bool:
        """ Resets all findings and clears batch """
        self.invalid = 0
        self.valid = 0
        self.processed = False

    def load_from_file(self, filename: str) -> bool:
        """ Loads a batch from given file """
        self.reset()
        try:
            with open(filename, "r") as f:
                self.batch_file = f.read()
        except Exception:
            return False
        return True


def main():
    print("Passport Processing Software")
    if len(sys.argv) != 2:
        print("Useage: python day04a.py [filename]")
        exit()
    print("Processing batches...")
    passports = Passport_Validation()
    passports.load_from_file(sys.argv[1])
    passports.process_batch(hacked=True)
    if not passports:
        print("Issues were found loading the batch. Call Sammi")
        exit()
    print(f"Processing completed. {passports.batch_size} processed.")
    print(f"Valid passports: {passports.valid}")
    print(f"Invalid passports: {passports.invalid}")


if __name__ == "__main__":
    main()
