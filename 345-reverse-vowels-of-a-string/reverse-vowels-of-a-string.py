class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'O','o', 'U', 'u'}

        vowel_in = []
        s = list(s)
        


        for char in s:
            if char in vowels:
                vowel_in.append(char)


        print(vowel_in)
        rever = vowel_in[::-1]
        j = 0
        for i in range(len(s)):
            if s[i] in vowels:
                print(s[i], rever[j])
                s[i] =rever[j]
                j+=1

        res = ''.join(s)

        return res

        