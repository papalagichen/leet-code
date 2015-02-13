class Solution:
    def twoSum(self, num, target):
        mem = {}
        for i, n in enumerate(num):
            if n in mem:
                return mem[n] + 1, i + 1
            rest = target - n
            mem[rest] = i

if __name__ == '__main__':
    print("index1={}, index2={}".format(*Solution().twoSum((2, 7, 11, 15), 9)))
