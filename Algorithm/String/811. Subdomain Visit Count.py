#https://leetcode.com/problems/subdomain-visit-count/

#Source: https://leetcode.com/problems/subdomain-visit-count/discuss/121738/C%2B%2BJavaPython-Easy-Understood-Solution

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = collections.Counter()
        for cd in cpdomains:
            #split by space, so count and domain name separated.
            n, s = cd.split()
            #complete domain name and its count stored.
            count[s] += int(n)
            for i in range(len(s)):
                # domain name and its count stored, beside complete domain name.
                if s[i] == '.':
                    count[s[i + 1:]] += int(n)
        return ["%d %s" % (count[k], k) for k in count]