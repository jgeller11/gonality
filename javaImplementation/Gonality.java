package javaImplementation;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.HashSet;

class Gonality {
    public static void main(String[] args) {
        System.out.println("running");
        Gonality g = new Gonality();
        int[][] adj = new int[][] {{0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0}};
        Graph graph = new Graph(adj);
        double startTime = System.currentTimeMillis();
        System.out.println(g.gonality(graph));
        double time = System.currentTimeMillis() - startTime;
        System.out.println("ran in " + time /1000 + " s");
    }

    boolean checkQReducedWinnable(Graph g, int[] divisor, int i, boolean[] pos) {
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
            boolean wins = false;
            if (burnt.size() != g.size()) {
                for (int node = 0; node < g.size(); node++) {
                    if (adjBurned[node] > 0) {
                        // if node moves chips to q, divisor winnable
                        // optimization: can we move this check?
                        if (g.isAdjacent(node, i)) {
                            wins= true;
                        }
                        for (int neighbor : g.getNeighbors(node)) {
                            if (burnt.contains(neighbor)) {
                                if (++divisor[neighbor]==1){
                                    pos[neighbor]=true;
                                }
                            }
                        }
                        divisor[node] -= adjBurned[node];
                    }
                }
                if (wins){
                    return true;
                }
            } else {
                return false;
            }
        }

    }

    static int[][] harary(int n, int k) {
        int[][] output = new int[n][n];
        for(int i = 0; i < n; i++){
            for(int j=1; j<=k; j++){
                output[i][(i-j+n)%n]=1;
                output[i][(i+j)%n]=1;
            }
        }
        return output;
    }

    int gonality(Graph g) {
        return gonality(g, 1);
    }

    int gonality(Graph g, int deg) {

        int[] degreeList = g.degreeList();
        int n = degreeList.length;
        int[] currentDivisor;
        while (true) {
            System.out.println(deg);
            // DegreeIterator d = new DegreeIterator(deg, n);
            DegreeIterator d = new DegreeIterator(deg, n);
            while (d.hasNext()) {
                
                // optimization: keep 1 chip on vertex of max degree
                // just compute ordered pairs for n-1, then add to vertex of max degree
                // order vertices in graph from max to min degree
                // optimization: improve iterator to exclude divisiors
                // with more chips than degree of vertex
                currentDivisor = d.next();
                boolean found = true;
                // pass in copy of divisor
                
                boolean[] pos = new boolean[n];
                int[] divisorCopy = new int[n];
                for (int m = 0; m < n; m++) {
                    divisorCopy[m] = currentDivisor[m];
                    if (divisorCopy[m]>0) {
                        pos[m]=true;
                    }
                }
                for (int i = 1; i < n; i++) {
                    if ((!pos[i])&&(divisorCopy[i]==0)) {
                        
                        if (!checkQReducedWinnable(g, divisorCopy, i, pos)) {
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
