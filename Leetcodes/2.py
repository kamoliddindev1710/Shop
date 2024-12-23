class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        reversedX=int(str(x)[::-1])
        if reversedX == x:
            return True
        else:
            return False
""""Togriri boshida bynday missolarni ishlay olmayapman lekin harajat qilyapman chnbn i boshida tushindik lekin stringgga otkazib olishni tushnnmadim
lekin keyin tushundium lekin endi tushundun qanmday ishlash kerakiligin """