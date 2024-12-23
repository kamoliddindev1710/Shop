class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        key={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total=key[s[0]]

        for x in range(1,len(s)):
            if key[s[x]]>key[s[x-1]]:
                total+=key[s[x]]-key[s[x-1]]
                total-=key[s[x-1]]
            else:
                total+=key[s[x]]
        return total
        """bu misolni tushintiradigan bolsam avvalo key oraqil bitta dict yaratib oldik keyin esa shu dcit qiymatlarni berdik
        keyin rnage ni 1 dan boshladik chuk solishtirh ktish uchn keyin esa """