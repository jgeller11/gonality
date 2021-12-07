package javaImplementation;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Iterator;

class Gonality {
    public static void main(String[] args) {
        System.out.println("running");
        Gonality g = new Gonality();
        //P3xP3xP3: 9
        //P3xP3xP4: 9
        //P3xP3xP5: 9
        //P3xP3xC3: 9
        //P3xC3xC3: 9
        //
      

        Graph graph = Graph.cycle(3).product(Graph.cycle(3).product(Graph.cycle(3)));

        double startTime = System.currentTimeMillis();
        System.out.println(g.gonality(graph, 14, true));
        double time = System.currentTimeMillis() - startTime;
        System.out.println("ran in " + time / 1000 + " s");


        //square.printAdjList();
    }

    boolean checkQReducedWinnable(Graph g, int[] divisor, int i, boolean[] pos) {
        int n = g.size();

        while (true) {
            LinkedList<Integer> l = new LinkedList<>();
            l.add(i);

            int[] adjBurned = new int[n];
            int numBurnt = 1;
            boolean[] burnt = new boolean[n];
            burnt[i] = true;
            // burn the graph

            while ((l.size() != 0) && (numBurnt != n)) {
                int next = l.remove(0);

                for (Integer it : g.getNeighbors(next)) {
                    if (!burnt[it]) {
                        if (divisor[it] <= adjBurned[it]) {
                            if (++numBurnt == n) {
                                return false;
                            }
                            burnt[it] = true;
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

            for (int node = 0; node < n; node++) {
                if (adjBurned[node] > 0) {

                    for (int neighbor : g.getNeighbors(node)) {
                        if (burnt[neighbor]) {
                            if (++divisor[neighbor] == 1) {
                                pos[neighbor] = true;
                            }
                        }
                    }
                    divisor[node] -= adjBurned[node];
                }
            }
            if (divisor[i] > 0) {
                return true;
            }

        }

    }

    static int[][] harary(int n, int k) {
        int[][] output = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 1; j <= k; j++) {
                output[i][(i - j + n) % n] = 1;
                output[i][(i + j) % n] = 1;
            }
        }
        return output;
    }

    int gonality(Graph g) {
        return gonality(g, 1, false);
    }

    int gonality(Graph g, boolean sym) {
        return gonality(g, 1, sym);
    }

    int gonality(Graph g, int deg) {
        return gonality(g, deg, false);
    }

    int gonality(Graph g, int deg, boolean sym) {

        int[] degreeList = g.degreeList();
        int n = degreeList.length;
        int[] currentDivisor;
        int count = 0;
        Iterator<int[]> d;
        while (true) {
            System.out.println(deg);
            if (sym){
                d = new SymmetryDegreeIterator(deg, n, degreeList);
            } else {
                d = new DegreeIterator(deg, n, degreeList);
            }
            while (d.hasNext()) {
                // optimization?: order vertices in graph from max to min degree
                count++;
                if (count % 100000 == 0) {
                    System.out.println("checked " + count + " divisors");
                }
                currentDivisor = d.next();
                boolean found = true;
                // pass in copy of divisor

                boolean[] pos = new boolean[n];
                int[] divisorCopy = new int[n];
                for (int m = 0; m < n; m++) {
                    divisorCopy[m] = currentDivisor[m];
                    if (divisorCopy[m] > 0) {
                        pos[m] = true;
                    }
                }
                for (int i = 1; i < n; i++) {
                    if ((!pos[i]) && (divisorCopy[i] == 0)) {

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
            count = 0;
            deg++;
        }
    }
}


