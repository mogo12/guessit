#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
crc and idNumber properties
"""
from rebulk import Rebulk
import regex as re

from ..common.validators import seps_surround

CRC = Rebulk().regex_defaults(flags=re.IGNORECASE)
CRC.defaults(validator=seps_surround)

_DIGIT = 0
_LETTER = 1
_OTHER = 2


_idnum = re.compile(r'(?P<idNumber>[a-zA-Z0-9-]{20,})')  # 1.0, (0, 0))


def guess_idnumber(string):
    """
    Guess id number function
    :param string:
    :type string:
    :return:
    :rtype:
    """
    #pylint:disable=invalid-name
    match = _idnum.search(string)
    if match is not None:
        result = match.groupdict()
        switch_count = 0
        switch_letter_count = 0
        letter_count = 0
        last_letter = None

        last = _LETTER
        for c in result['idNumber']:
            if c in '0123456789':
                ci = _DIGIT
            elif c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                ci = _LETTER
                if c != last_letter:
                    switch_letter_count += 1
                last_letter = c
                letter_count += 1
            else:
                ci = _OTHER

            if ci != last:
                switch_count += 1

            last = ci

        # only return the result as probable if we alternate often between
        # char type (more likely for hash values than for common words)
        switch_ratio = float(switch_count) / len(result['idNumber'])
        letters_ratio = (float(switch_letter_count) / letter_count) if letter_count > 0 else 1

        if switch_ratio > 0.4 and letters_ratio > 0.4:
            return match.span()

CRC.functional(guess_idnumber, name='idNumber')

