'''
Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'.
Each revision consists of digits and may contain leading zeros. Every revision contains at least one character.
Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on.
For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order.
Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal.
If a version number does not specify a revision at an index, then treat the revision as 0.
For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
'''
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")[::-1]
        v2 = version2.split(".")[::-1]

        while v1 or v2:
            v1_val = 0
            v2_val = 0
            if v1: v1_val = int(v1.pop())
            if v2: v2_val = int(v2.pop())

            if v1_val > v2_val:
                return 1
            if v1_val < v2_val:
                return -1

        return 0