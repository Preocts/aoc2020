"""
Preocts <preocts@preocts.com>
Preocts#8196
AOC Day 4 part b

I am purposely NOT using regex for this one
"""
import sys
from day04a import Passport_Validation


class Passport_Validation_v2(Passport_Validation):
    """Process a batch of passports

    Dev note: Version 2, you're welcome.

    Providing a batch file when declaring will process that batch file
    and populate the attributes.

    Note: Do not hack >:V

    Attributes:
        batch_file [str]: Batch of passports
        valid [int]     : # of passports that are valid
        invalid [int]   : # of passports that are invalid
        processed [bool]: Indicates if batch has been processed
    """

    def __init__(self, filename: str = "") -> None:
        super().__init__(filename)

    def process_batch(self, hacked: bool = False) -> None:
        """ Processes loaded batch file """
        self.reset()
        batch_file = self._split_file()
        for passport in batch_file:
            data = {}
            valid = []
            for seg in passport.strip().split(" "):
                data[seg.split(":")[0]] = seg.split(":")[1]
            valid.append(self._check_birth(data.get("byr", "")))
            valid.append(self._check_issue(data.get("iyr", "")))
            valid.append(self._check_expiry(data.get("eyr", "")))
            valid.append(self._check_height(data.get("hgt", "")))
            valid.append(self._check_hair(data.get("hcl", "")))
            valid.append(self._check_eye(data.get("ecl", "")))
            valid.append(self._check_id(data.get("pid", "")))
            if not hacked:
                valid.append(self._check_cid(data["cid"]))
            if all(valid):
                self.valid += 1
            else:
                self.invalid += 1
        self.processed = True
        return

    def _check_birth(self, byr: str) -> bool:
        """ int, 1920 >= bry <= 2002 """
        try:
            birthyr = int(byr)
        except ValueError:
            return False
        return True if (1920 <= birthyr) and (2002 >= birthyr) else False

    def _check_issue(self, iyr: str) -> bool:
        """ int, 2010 >= iyr <= 2020 """
        try:
            issueyr = int(iyr)
        except ValueError:
            return False
        return True if (2010 <= issueyr) and (2020 >= issueyr) else False

    def _check_expiry(self, eyr: str) -> bool:
        """ int, 2020 >= eyr <= 2030 """
        try:
            expiryyr = int(eyr)
        except ValueError:
            return False
        return True if (2020 <= expiryyr) and (2030 >= expiryyr) else False

    def _check_height(self, hgt: str) -> bool:
        """ cm 150-193 / in 59-76 """
        minmax = (150, 193) if hgt.endswith("cm") else (59, 76)
        if not (hgt.endswith("in") or hgt.endswith("cm")):
            return False
        try:
            height = int(hgt[0 : len(hgt) - 2])
        except ValueError:
            return False
        if (minmax[0] <= height) and (minmax[1] >= height):
            return True
        return False

    def _check_hair(self, hcl: str) -> bool:
        if not (hcl.startswith("#")):
            return False
        valid_chars = "0123456789abcdef"
        for char in hcl.replace("#", "", 1):
            if char not in valid_chars:
                return False
        return True

    def _check_eye(self, ecl: str) -> bool:
        """ amb blu brn gry grn hzl oth """
        if len(ecl) != 3:
            return False
        valid_eyes = "amb blu brn gry grn hzl oth".split()
        for valid in valid_eyes:
            if ecl in valid:
                return True
        return False

    def _check_id(self, pid: str) -> bool:
        """ length 9 and valid int """
        if len(pid) != 9:
            return False
        try:
            int(pid)
        except ValueError:
            return False
        return True

    def _check_cid(self, cid: str) -> bool:
        return True


def main():
    print("Passport Processing Software version 2.0")
    if len(sys.argv) != 2:
        print("Useage: python day04b.py [filename]")
        exit()
    print("Processing batches...")
    passports = Passport_Validation_v2()
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
