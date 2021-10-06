#https://leetcode.com/problems/k-closest-points-to-origin/
#https://leetcode.com/problems/k-closest-points-to-origin/discuss/294389/Easy-to-read-Python-min-heap-solution-(-beat-99-python-solutions-)

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        return [(x,y) for (dist,x, y) in heap] 