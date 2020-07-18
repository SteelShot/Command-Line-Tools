#! python3.8

__copyright__ = """
    Copyright (C) 2020 Džiugas Eiva

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

__license__ = "GPLv3"

import argparse
import secrets
import string
import sys
from abc import abstractmethod
from secrets import SystemRandom
from typing import final


@final
class RandApp:
    @final
    class __PosInt:
        def __call__(self, arg):
            try:
                num = int(arg)

                if num > 0:
                    return num
                else:
                    raise self.__exception()

            except ValueError:
                raise self.__exception()

        @staticmethod
        def __exception():
            return argparse.ArgumentTypeError("must be an integer greater than zero")

    class __Rand:
        def __init__(self, size):
            self.size = size

        @abstractmethod
        def generate(self):
            pass

    @final
    class __RandPass(__Rand):
        __complexities = [string.ascii_lowercase,
                          string.ascii_letters,
                          string.ascii_letters + string.digits,
                          string.ascii_letters + string.digits + "+_|@!#^*-?%$&=[](){}~:;"]

        def __init__(self, size, complexity):
            super().__init__(size if size >= 8 else 8)

            self.complexity = self.__complexities[complexity]

        def generate(self):
            complexity = list(self.complexity)

            SystemRandom().shuffle(complexity)

            return "".join([secrets.choice(complexity) for _ in range(self.size)])

    @final
    class __RandNum(__Rand):
        def __init__(self, size):
            super().__init__(size)

        def generate(self):
            return secrets.randbits(self.size)

    __types = ["password", "number"]
    __passc = ["weak", "moderate", "strong", "extreme"]

    def __init__(self):
        self.parser = argparse.ArgumentParser(prog="rand", description="Generate SECURE random passwords or numbers")
        self.rand = None

        self.__init_arguments()
        self.__parse_arguments()

    def __init_arguments(self):
        parser = self.parser

        parser.add_argument("-t", "--type", dest="a1", required=True, choices=self.__types,
                            help="Generate either a random password or a random number")

        parser.add_argument("-l", "--length", dest="a2", type=self.__PosInt(), default=8, metavar="LENGTH",
                            help="Defines either the password length or maximum possible random number value in "
                                 "'length' bits Note: Passwords will always be at least 8 characters long")

        parser.add_argument("-c", "--complexity", dest="a3", choices=self.__passc, default=self.__passc[2],
                            help="Complexity defines the inclusion of uppercase characters, numbers or symbols"
                                 " variability. Note: argument ignored when generating random numbers")

        parser.add_argument("-a", "--amount", dest="a4", type=self.__PosInt(), default=1, metavar="AMOUNT",
                            help="Controls how many random passwords or numbers to generate")

    def __parse_arguments(self):
        args = self.parser.parse_args()

        a1 = args.a1
        a2 = args.a2
        a3 = self.__passc.index(args.a3)
        a4 = args.a4

        if a1 == self.__types[0]:
            self.rand = self.__RandPass(a2, a3)
        else:
            self.rand = self.__RandNum(a2)

        if a4 == 1:
            print(self.rand.generate())
        else:
            for _ in range(a4):
                print(self.rand.generate())


if __name__ == '__main__':
    RandApp()

    sys.exit(0)
