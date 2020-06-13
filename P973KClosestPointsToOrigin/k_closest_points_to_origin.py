class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    """
    Given a list of (x, y) points on the plane, returns the K-closest points 
    to the origin (0, 0).
    
    Here, the distance between two points on a plane is the Euclidean distance,
    sqrt(x * x + y * y). 

    The answer is returned without any particular order.

    The input may be sorted according to distance, but the time complexity of
    such a solution is O(n * log(n)), where n is the number of points given in
    the input list.

    An alternative approach is to use a max heap of K elements. A max heap will 
    keep the elements sorted in a particular order such that the largest of the
    K points will appear at the top.

    Consider the example [[3,3],[5,-1],[-2,4]], K = 2

    Visually, it's possible to see that the points with the two smallest 
    distances is [3, 3] (distance = sqrt(18)), and 
    [-2, 4] (distance = sqrt(20)). Using the approach above, we want to keep
    2 elements in our heap at all times, and these should be sorted with the
    max heap property such that the element at the top of the heap is the 
    element with the largest distance to the origin out of the K elements in 
    the heap.

    The Python module heapq by default implements a min heap, so it does not
    easily have functionality for a max heap. The way around this is to store 
    the negative of the distance, such that the largest positive distance 
    will appear at the top of the min heap (i.e., the smallest **negative**
    distance).

    Before looping through the array, we have: 

    points = [[3,3],[5,-1],[-2,4]], K = 2 , heap = []

    If the heap is empty, or there are less than K elements in our heap, we 
    insert the element into the heap.

    i = 0 : [[3,3],[5,-1],[-2,4]], K = 2 , heap = [()]
              i
            
            distance = 3 * 3 + 3 * 3 = 18
    
    The heap has fewer than K = 2 elements in it, so we insert the negative of
    the distance and the index at which this value occurs
            [[3,3],[5,-1],[-2,4]], K = 2 , heap = [(-18, 0)]
              i
            
    For i = 1, we also insert the element into the heap 
    i = 1: [[3,3],[5,-1],[-2,4]], K = 2 , heap = [(-18, 0)]
                     i
            
            distance = 5 * 5 + (-1) * (-1) = 26
    And we insert into our min heap with the negative distance and the index
    at which this value occurs

            [[3,3],[5,-1],[-2,4]], K = 2 , heap = [(-26, 1), (-18, 0)]
                     i
    
    For i = 2, now we must compare the distance to the top distance of the
    max heap. In Python heap[0] will contain the minimum element, so there is 
    no need to use a peek() method. We calculate the distance
    
    i = 2: [[3,3],[5,-1],[-2,4]], K = 2 , heap = [(-26, 1), (-18, 0)]
                            i
            distance = (-2) * (-2) + (4) * (4) = 20
    
    Since 20 is closer to 0 than 26 (remember when comparing distances to use 
    only positive values), we pop the value (-26, 1) off the top of the heap
    and insert (-20, 2) into the heap to give

            [[3,3],[5,-1],[-2,4]], K = 2 , heap = [(-20, 1), (-18, 0)]
                            i
    
    At this stage, the heap has values [(-20, 1), (-18, 0)]. To get the 
    original x, y, pairs back, we pop elements off the heap while it is not 
    empty.
    
    k_closest_points = []                     max_heap = [(-20, 1), (-18, 0)]
    k_closest_points = [[(-20, 1)]]           max_heap = [(-18, 0)]  
     ...
    k_closest_points = [[(-20, 1), (-18, 0)]] max_heap = []

    The time complexity is O(n * log(K)), where n is the number of points given
    in the list and K is the number of closest points to return.

    The space complexity is O(K).

    Parameters
    ----------
    points : List[List[int]]
        List of x, y pairs representing points in a two-dimensional plane. 
    K : int
        Number of closest points to return.

    Returns
    -------
    k_closest_points : List[List[int]]
        K closest points to the origin [0, 0]

    Examples
    --------
    Input : points = [[1,3],[-2,2]], K = 1
    Output : [[-2,2]]

    Input : points = [[3,3],[5,-1],[-2,4]], K = 2
    Output : [[3,3],[-2,4]]

    Input :[[5,1], [5,8], [-1, 3], [4,4], [6,-3], [1, 1], [-1,1]], K = 4
    Output : [[5,1],[-1,3],[1,1],[-1,1]]
    """
        k_closest_points = []
        max_heap = []
        
        for i, p in enumerate(points):
            # Do not need to store a floating point number. Comparison between
            # integers is preffered to comparison of floating point numbers.
            distance = p[0]**2 + p[1]**2
            if len(max_heap) < K:
                 heapq.heappush(max_heap, (-distance, i))
            else:
                # Once the heap holds K elements, compare the current distance
                # to the top element in the max heap. If the current element
                # is closer i.e. |current distance| < |max_heap[0]|, then 
                # popo the top element from the heap, and push the new distance
                # index pair.
                if distance < -1 * max_heap[0][0]:
                    heapq.heappushpop(max_heap, (-distance, i))
        
        # Continue to pop elements off the heap until it is empty. The second
        # value in the pair that is returned is the index of the x, y pair 
        # which has that distance from the origin. Append the x, y pair at that
        # index.                  
        while max_heap:
            distance, index = heapq.heappop(max_heap)
            k_closest_points.append(points[index])
        
        return k_closest_points