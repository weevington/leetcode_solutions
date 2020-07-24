class Solution {
public:
    /**
     * @brief enumerates all paths from node 0 to node N - 1 of a DAG.
     * @param graph
     *     std::vector<std::vector<int> >
     * @return paths
     *     std::vector<std::vector<int> >
     *     Unique paths from node 0 to node N - 1 where N is the number of
     *     of nodes in the DAG, and node N - 1 is taken to be the end node.
     * 
     * Given a directed, acyclic graph of N nodes represented using an 
     * adjacency list finds all possible paths from node 0 to node N-1, 
     * and returns them in any order.
     * 
     * This approach uses a depth-first search through recursion. A vector
     * of vectors is used to keep track of all the paths. A temporary vector
     * is used to store nodes that are visited during the depth-first search.
     * If the node is the end node (at index N - 1 in the adjacency list 
     * representation of the DAG), then the path is pushed back to the 
     * vector of vectors used to store all full paths from 0 to N - 1.
     * The vector is passed by value such that when the call stack
     * comes back out of the recursion, the number of elements in the path
     * at a given step is correct. This incurs a bit of overhead regarding
     * copying of the argument, but it is less error-prone than having to 
     * explicitly pop elements off the back of the vector.
     * 
     */
    void dfs(const std::vector<std::vector<int> >& graph, const int n,
             std::vector<int> path, std::vector<std::vector<int> >& result) {
        if (n < graph.size()){
            path.push_back(n);
        }
        
        if (n == graph.size() - 1) {
            result.push_back(path);
            return;
        }
        
        std::vector<int> neighbors = graph.at(n);
        for (int i = 0; i < neighbors.size(); ++i) {
            std::vector<int> tmp{path};
            dfs(graph, neighbors.at(i), tmp, result);
        }
        
    }
    
    vector<vector<int> > allPathsSourceTarget(vector<vector<int> >& graph) {
        std::vector<std::vector<int> > paths;
        std::vector<int> p;
        
        dfs(graph, 0, p, paths);
        
        return paths;
    }
};


class Solution {
public:
    /**
     * @brief enumerates all paths from node 0 to node N - 1 of a DAG.
     * @param graph
     *     std::vector<std::vector<int> >
     * @return paths
     *     std::vector<std::vector<int> >
     *     Unique paths from node 0 to node N - 1 where N is the number of
     *     of nodes in the DAG, and node N - 1 is taken to be the end node.
     * 
     * Given a directed, acyclic graph of N nodes represented using an 
     * adjacency list finds all possible paths from node 0 to node N-1, 
     * and returns them in any order.
     * 
     * This approach uses a breadth-first search with a queue data structure.
     * If the graph is not empty, then a vector with a single element is first
     * added to the queue. 
     * 
     * A while loop then proceeds to take elements out of the queue. While the 
     * queue is not empty, the front element is popped off the queue. If the
     * trailing element of the vector that was popped off the queue is not
     * the N - 1th element of the graph (the end element), then the elements
     * in the vector are processed. For each element, the neighbors are added
     * to a temporary vector , and each temporary vector is added to the queue.
     * As elements are continued to be popped off the queue, and the last
     * node of the vector popped off the queue is equal to the end node with
     * value N - 1, then the vector itself is pushed back to the result. The
     * function returns when all paths have been explored.
     */
    vector<vector<int> > allPathsSourceTarget(vector<vector<int> >& graph) {
        std::vector<std::vector<int> > paths;
        if (!graph.size()) {
            return paths;
        }
        
        std::queue<std::vector<int> > q;
        q.push(std::vector<int>{0});
        const int target_node = graph.size() - 1;
        
        while (q.size()) {
            std::vector<int> current = q.front();
            q.pop();

            const int back_node = current.at(current.size() - 1);
            if (back_node == target_node) {
                paths.push_back(current);
            } else {
                std::vector<int> neighbors = graph[back_node];
                
                for (int i = 0; i < neighbors.size(); ++i) {
                    std::vector<int> tmp = current;
                    tmp.push_back(neighbors[i]);
                    q.push(tmp);
                }
            }
        }
        
        return paths;
         
    }
};