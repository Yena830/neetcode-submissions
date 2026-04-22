class Solution:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        #Initialize
        res = ''
        for s in strs:
            length = len(s)
            res += str(length)+"$"+s

        return res

        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        curr = 0
        res = []
        while(curr<len(s)):
            #Find the $
            dollar_index=s.find("$",curr)
            
            #Get the length of the string
            length = int(s[curr:dollar_index])
            
            #Read the string
            curr = dollar_index+1
            res.append(s[curr:curr+length])
            
            #Update the curr point
            curr += length

        return res
