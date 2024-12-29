import functools


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        desiredDict = {}

        for key in s1:
            if key in desiredDict:
                desiredDict[key] += 1
            else:
                desiredDict[key] = 1

        leftPointer = 0
        rightPointer = len(s1) - 1

        while True:
            dict = {}

            for i in range(leftPointer, rightPointer):
                dict[s2[i]] += 1 if s2[i] in dict else dict[s2[i]] = 1;
