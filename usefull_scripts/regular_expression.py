#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
 .
    any character except a newline
 ^
    the start of the string
 $
    the end of the string
 *
    match 0 or more repetitions
 +
    match 1 or more repetitions
 ?
    match 0 or 1 repetitions
 *? +? ??
    match in non-greedy fashion
 {m}
    match m repetitions
 {m,n}
    match from m to n repetitions, attempting to match as many repetitions
       as possible
 {m,n}?
    match from m to n repetitions, attempting to match as few repetitions
       as possible
 \
    either escapes special characters, or signals a special sequence
 []
    Used to indicate a set of characters.
        Characters can be listed individually. [ak] will match 'a', or 'k'.
        Ranges of characters can be indicated by giving two chararcters and
            separating them by a 'a'. [a-z], [0-5][0-9]. If '-' is escaped or
            placed at the first or last character, it matches a literal '-'.
        [(+*)] will match '(', '+', '*', or ')'.
        Character classes such as \w or \S are also accepted inside a set.
        If the first character of the set is '^', all the characters that are
            not in the set will be matched. [^5] will match any character
            except '5'.
        To match a literal ']' inside a set, precede it with a backslash, or
            place it at the beginning of the set. [][] and [[\]] equals.
 |
    A|B, match A either B. To match '|', use '\|'.
 (...)
    Matches whatever regular expression is inside the parentheses, and
        indicates the start and end of a group; the contents fo a group can be
        retrieved after a match has been performed, and can be matched later
        in the string with the '\number' special sequence.
 (?...)
 (?iLmsux)
 (?:...)
 (?P<name>...)
 (?P=name)
 (?#...)
 (?=...)
 (?!...)
 (?<=...)
 (?<!...)
 (?(id/name)yes-pattern|no-pattern)

 SPECIAL SEQUENCES
 \number
    Matches the contents of the group of the same number. Groups are numbered
        starting from 1. For example, '(.+) \1' matches 'the the', or '55 55'.
 \A
    Matches only at the start of the string.
 \b
    Matches the empty string, but only at the beginning or end of a word. A
        word is defined as a sequence of alphanumeric or underscore characters,
        so the end of a word is indicated by whitespace or a non-alphanumeric,
        non-underscore character. For example, r\bfoo\b matches 'foo', 'foo.',
        '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'.
 \B
    Matches the empty string, but only when it is not at the beginning or end of
        a word. This means that r'py\B matches 'python', 'py3', 'py2', but not
        'py', 'py.', 'py!'. \B is just the opposite of \b.
 \d
    Matches any decimal digit. This is equivalent to the set [0-9].
 \D
    Matches any non-digit character. This is equivalent to the set [^0-9].
 \s
    Matches any whitespace character. This is equivalent to the set
        [ \t\n\r\f\v].
 \S
    Matches any non-whitespace character. This is equivalent to the set
        [^ \t\n\r\f\v].
 \w
    Matches any alphanumeric character and the underscore. This is equivalent to
        the set [a-zA-Z0-9_].
 \W
    Matches any non-alphanumeric character. This is equivalent to the set
        [^a-zA-Z0-9_].
 \Z
    Matches the end of the string.

'''
import re

def p(r, t):
    m = re.search(r, t)
    print(m.group(0) if m else None)

def test():
    text = 'foobar'
    r = '.'
    p(r, text)

    r = 'bar'
    p(r, text)
    r = '^bar'
    p(r, text)

    r = 'foo'
    p(r, text)
    r = 'foo$'
    p(r, text)

    t = '<a>b<c>'
    r = '<.*>'
    p(r, t)
    r = '<.*?>'
    p(r, t)

    t = 'aababaaab'
    r = 'a{3}'
    p(r, t)
    r = 'a{1,3}'
    p(r, t)
    t = 'aaaaaa'
    p(r, t)
    r = 'a{1,3}?'
    p(r, t)

    t = '*?'
    r = '\\*'
    p(r, t)
    r = '\\\\'
    p(r, t)



if __name__ == '__main__':
    test()
