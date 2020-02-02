import sys
from typing import Dict
from typing import Tuple

sys.setrecursionlimit(2000)


# Recursive. Time: O(2^n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.helper(text1, text2, 0, 0)

    def helper(self, text1: str, text2: str, index1: int, index2: int) -> int:
        if index1 == len(text1) or index2 == len(text2):
            return 0

        if text1[index1] == text2[index2]:
            return 1 + self.helper(text1, text2, index1 + 1, index2 + 1)
        else:
            return max(self.helper(text1, text2, index1 + 1, index2), self.helper(text1, text2, index1, index2 + 1))


# Dynamic programming. Time: O(2^n)
class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.helper(text1, text2, 0, 0, {})

    def helper(self, text1: str, text2: str, index1: int, index2: int, mem: Dict[Tuple, int]) -> int:
        if index1 == len(text1) or index2 == len(text2):
            return 0

        key = (index1, index2)

        if key in mem:
            return mem[key]

        if text1[index1] == text2[index2]:
            mem[key] = 1 + self.helper(text1, text2, index1 + 1, index2 + 1, mem)
        else:
            mem[key] = max(
                self.helper(text1, text2, index1 + 1, index2, mem),
                self.helper(text1, text2, index1, index2 + 1, mem),
            )

        return mem[key]


# Bottom up dynamic programming. Time: O(nm), Space: O(nm)
class Solution3:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = ' ' + text1
        text2 = ' ' + text2
        mem = [[0] * len(text2) for _ in range(len(text1))]
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    mem[i][j] = mem[i - 1][j - 1] + 1
                else:
                    mem[i][j] = max(mem[i][j - 1], mem[i - 1][j])
        return mem[-1][-1]


# Bottom up dynamic programming. Time: O(nm), Space: O(min(n, m))
class Solution4:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = ' ' + text1
        text2 = ' ' + text2
        mem = [[0] * len(text2), [0] * len(text2)]
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    mem[i % 2][j] = mem[(i - 1) % 2][j - 1] + 1
                else:
                    mem[i % 2][j] = max(mem[i % 2][j - 1], mem[(i - 1) % 2][j])
        return mem[(len(text1) - 1) % 2][-1]


if __name__ == '__main__':
    import Test

    Test.test([
        Solution2().longestCommonSubsequence,
        Solution3().longestCommonSubsequence,
        Solution4().longestCommonSubsequence,
    ], [
        (('abcde', 'ace'), 3),
        (('abc', 'abc'), 3),
        (('abc', 'def'), 0),
        (('fcvafurqjylclorw', 'nohgdazargvalupe'), 3),
        ((
             "lcnqdmvsdopkvqvejijcdyxetuzonuhuzkpelmva",
             "bklgfivmpozinybwlovcnafqfybodkhabyrglsnen",
         ), 9),
        ((
             'fcvafurqjylclorwfoladwfqzkbebslwnmpmlkbezkxoncvwhstwzwpqxqtyxo',
             'nohgdazargvalupetizezqpklktojqtqdivcpsfgjopaxwbkvujilqbclehulatshehmjqhyfkpcfwxovajkvankjk',
         ), 20),
        ((
             "fcvafurqjylclorwfoladwfqzkbebslwnmpmlkbezkxoncvwhstwzwpqxqtyxozkpgtgtsjobujezgrkvevklmludgtyrmjaxyputqbyxqvupojutsjwlwluzsbmvyxifqtglwvcnkfsfglwjwrmtyxmdgjifyjwrsnenuvsdedsbqdovwzsdghclcdexmtsbexwrszihcpibwpidixmpmxshwzmjgtadmtkxqfkrsdqjcrmxkbkfoncrcvoxuvcdytajgfwrcxivixanuzerebuzklyhezevonqdsrkzetsrgfgxibqpmfuxcrinetyzkvudghgrytsvwzkjulmhanankxqfihenuhmfsfkfepibkjmzybmlkzozmluvybyzsleludsxkpinizoraxonmhwtkfkhudizepyzijafqlepcbihofepmjqtgrsxorunshgpazovuhktatmlcfklafivivefyfubunszyvarcrkpsnglkduzaxqrerkvcnmrurkhkpargvcxefovwtapedaluhclmzynebczodwropwdenqxmrutuhehadyfspcpuxyzodifqdqzgbwhodcjonypyjwbwxepcpujerkrelunstebopkncdazexsbezmhynizsvarafwfmnclerafejgnizcbsrcvcnwrolofyzulcxaxqjqzunedidulspslebifinqrchyvapkzmzwbwjgbyrqhqpolwjijmzyduzerqnadapudmrazmzadstozytonuzarizszubkzkhenaxivytmjqjgvgzwpgxefatetoncjgjsdilmvgtgpgbibexwnexstipkjylalqnupexytkradwxmlmhsnmzuxcdkfkxyfgrmfqtajatgjctenqhkvyrgvapctqtyrufcdobibizihuhsrsterozotytubefutaxcjarknynetipehoduxyjstufwvkvwvwnuletybmrczgtmxctuny",
             "nohgdazargvalupetizezqpklktojqtqdivcpsfgjopaxwbkvujilqbclehulatshehmjqhyfkpcfwxovajkvankjkvevgdovazmbgtqfwvejczsnmbchkdibstklkxarwjqbqxwvixavkhylqvghqpifijohudenozotejoxavkfkzcdqnoxydynavwdylwhatslyrwlejwdwrmpevmtwpahatwlaxmjmdgrebmfyngdcbmbgjcvqpcbadujkxaxujudmbejcrevuvcdobolcbstifedcvmngnqhudixgzktcdqngxmruhcxqxypwhahobudelivgvynefkjqdyvalmvudcdivmhghqrelurodwdsvuzmjixgdexonwjczghalsjopixsrwjixuzmjgxydqnipelgrivkzkxgjchibgnqbknstspujwdydszohqjsfuzstyjgnwhsrebmlwzkzijgnmnczmrehspihspyfedabotwvwxwpspypctizyhcxypqzctwlspszonsrmnyvmhsvqtkbyhmhwjmvazaviruzqxmbczaxmtqjexmdudypovkjklynktahupanujylylgrajozobsbwpwtohkfsxeverqxylwdwtojoxydepybavwhgdehafurqtcxqhuhkdwxkdojipolctcvcrsvczcxedglgrejerqdgrsvsxgjodajatsnixutihwpivihadqdotsvyrkxehodybapwlsjexixgponcxifijchejoxgxebmbclczqvkfuzgxsbshqvgfcraxytaxeviryhexmvqjybizivyjanwxmpojgxgbyhcruvqpafwjslkbohqlknkdqjixsfsdurgbsvclmrcrcnulinqvcdqhcvwdaxgvafwravunurqvizqtozuxinytafopmhchmxsxgfanetmdcjalmrolejidylkjktunqhkxchyjmpkvsfgnybsjedmzkrkhwryzan",
         ),
         323),
    ])
