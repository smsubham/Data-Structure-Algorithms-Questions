#https://leetcode.com/problems/subdomain-visit-count/
#Time Complexity: O(N)O(N), where NN is the length of cpdomains, and assuming the length of cpdomains[i] is fixed.
#Space Complexity: O(N)O(N), the space used in our count.
#Source: https://leetcode.com/problems/subdomain-visit-count/discuss/121738/C%2B%2BJavaPython-Easy-Understood-Solution

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = collections.Counter()
        for cpdomain in cpdomains:
            #explanation of * => Extended Iterable Unpacking, Example: a, *b, c = range(5)
            # 1, [2,3,4], 5
            # https://www.python.org/dev/peps/pep-3132/
            #count then domain name in domains as list.
            count, *domains = cpdomain.replace(" ",".").split(".")
            for i in range(len(domains)):
                #domains has x,y,z for x.y.z domain, it includes x.y.z, y.x and x
                #by doing slicing in domains[i:], i in range(3)
                counter[".".join(domains[i:])] += int(count)
        return [" ".join((str(v), k)) for k, v in counter.items()]