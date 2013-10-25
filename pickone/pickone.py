"""
The MIT License (MIT)

Copyright (c) 2013 Riccardo Cagnasso

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__author__ = "Riccardo Cagnasso <riccardo@phascode.org>"

import collections as coll


class PickOne(object):
    """
        PickOne is a class that you use for asking the user to choose between
        some options

        Arguments:
        choiches --- the available options between the user can choose. It can
        be an array or a dictionary. In the first case the keys are int from 0
        to len-1.

        Keyword arguments:
        message (optional) --- the message to be displayed when asking for
        input. It's a template for "format" function and receives the
        "{choices}" and the {default} parameter.
        errormessage (optional) --- the message to be displayed when the user
        entered a incorrect answer
        default (optional) --- a default value to use if user provides no input
    """
    def __init__(self, choices,
        message="Choose one from [{choices}]{default}: ",
        errormessage="Invalid input", default=None):
        self.message = message
        self.errormessage = errormessage

        if type(choices) == list:
            self.choices = coll.OrderedDict(
                zip(map(str, range(0, len(choices))), choices))
        elif issubclass(choices.__class__, dict):
            self.choices = coll.OrderedDict([(str(k), v)
                for k, v in choices.items()])

        self.default = default

    def buildPrompt(self):
        choices = ["{key}={choice}".format(key=key, choice=choice)
            for key, choice in self.choices.items()]

        if self.default is not None:
            default = " (default={default})".format(default=self.default)
        else:
            default = ""

        return self.message.format(choices=" ".join(choices), default=default)

    def ask(self):
        """
            The ask method is used to get the input from users
        """
        while True:
            i = input(self.buildPrompt())

            if i == "" and self.default is not None:
                i = self.default

            if i in self.choices:
                return self.choices[i]
            else:
                for k, v in self.choices.items():
                    if i == str(v):
                        return self.choices[k]

            print(self.errormessage)


def ask(choices,
    message="Choose one from [{choices}]{default}: ",
    errormessage="Invalid input", default=None):
    """
        ask is a shorcut instantiate PickOne and use .ask method
    """

    return PickOne(choices, message, errormessage, default).ask()
