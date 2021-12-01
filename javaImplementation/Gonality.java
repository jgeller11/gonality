package javaImplementation;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.HashSet;

class Gonality {
    public static void main(String[] args) {
        System.out.println("running");
        Gonality g = new Gonality();
        int[][] adj = new int[][] { { 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0 },
                { 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 },
                { 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0 },
                { 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0 },
                { 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1 },
                { 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1 },
                { 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1 },
                { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1 },
                { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0 } };
        Graph graph = new Graph(adj);
        graph.printAdjList();
        double startTime = System.currentTimeMillis();
        System.out.println(g.gonality(graph));
        double time = System.currentTimeMillis() - startTime;
        System.out.println("ran in " + time / 10 + " ms");
    }
    // il: ran in 3.6 - 3.8s
    // after optimization: ran in ~1.8s

    boolean checkQReducedWinnable(Graph g, int[] divisor, int i) {
        while (true) {
            LinkedList<Integer> l = new LinkedList<>();
            l.add(i);
            int[] adjBurned = new int[g.size()];
            HashSet<Integer> burnt = new HashSet<>();
            burnt.add(i);
            // burn the graph
            while (l.size() != 0) {
                int next = l.remove(0);
                for (Integer it : g.getNeighbors(next)) {
                    if (!burnt.contains(it)) {
                        if (divisor[it] <= adjBurned[it]) {
                            burnt.add(it);
                            adjBurned[it] = 0;
                            l.add(it);
                        } else {
                            adjBurned[it]++;
                        }
                    }
                }
            }
            // if not everything burns, then set fire
            // optimization: do it in one pass
            if (burnt.size() != g.size()) {
                for (int node = 0; node < g.size(); node++) {
                    if (adjBurned[node] > 0) {
                        // if node moves chips to q, divisor winnable
                        // optimization: can we move this check?
                        if (g.isAdjacent(node, i)) {
                            return true;
                        }
                        for (int neighbor : g.getNeighbors(node)) {
                            if (burnt.contains(neighbor)) {
                                divisor[neighbor]++;
                            }
                        }
                        divisor[node] -= adjBurned[node];
                    }
                }
            } else {
                return false;
            }
        }

    }

    // 3: [3, 0, 0, 0, 0, 0]
    // [0, 0, 0, 0, 0, 0]

    int gonality(Graph g) {

        int[] degreeList = g.degreeList();
        int deg = 1;
        int[] currentDivisor;
        while (true) {
            DegreeIterator d = new DegreeIterator(deg - 1, degreeList.length);
            while (d.hasNext()) {
                // optimization: keep 1 chip on vertex of max degree
                // just compute ordered pairs for n-1, then add to vertex of max degree
                // order vertices in graph from max to min degree
                // optimization: improve iterator to exclude divisiors
                // with more chips than degree of vertex
                currentDivisor = d.next();
                boolean found = true;
                for (int i = 0; i < currentDivisor.length; i++) {
                    if (currentDivisor[i] == 0) {
                        // pass in copy of divisor
                        int[] divisorCopy = new int[currentDivisor.length];
                        for (int m = 0; m < currentDivisor.length; m++) {
                            divisorCopy[m] = currentDivisor[m];
                        }
                        divisorCopy[0] += 1;
                        if (!checkQReducedWinnable(g, divisorCopy, i)) {
                            found = false;
                            break;
                        }
                    }
                }
                if (found) {
                    System.out.println(Arrays.toString(currentDivisor));
                    return deg;
                }
            }
            deg++;
        }
    }
}
