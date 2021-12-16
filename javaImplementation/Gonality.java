package javaImplementation;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.Iterator;
import java.math.BigInteger;
import java.lang.Runtime;

class Gonality {
    public static void main(String[] args) throws Exception {
        System.out.println("running");
        Gonality g = new Gonality();
        // P3xP3xP3: 9
        // P3xP3xP4: 9
        // P3xP3xP5: 9
        // P3xP3xP6: 9
        // P3xP3xC3: 9
        // P3xC3xC3: 9
        // P3xP4xC3: 9
        // P3xP3xC4: 12
        // C3xC3xC3 >= 16
        // 196.247
        Graph graph = Graph.path(2).product(Graph.path(3).product(Graph.path(10)));

        double startTime = System.currentTimeMillis();
        System.out.println(g.parallelGonality(graph, 1, false));
        double time = System.currentTimeMillis() - startTime;
        System.out.println("ran in " + time / 1000 + " s");

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

    // generates a random simple graph's adjacency list on n vertices with m edges,
    // (n)(n-1)/2 > m > n
    // begins with a cycle to ensure graph is connected, then adds m-n more edges
    static int[][] randomGraph(int n, int m) {
        int[][] output = new int[n][n];
        for (int i = 0; i < n; i++) {
            output[i][(i + 1) % n] = 1;
            output[(i + 1) % n][i] = 1;
        }
        for (int i = 0; i < (m - n); i++) {
            boolean edgeBuilt = false;
            while (!edgeBuilt) {
                int v1 = (int) (Math.random() * n);
                int v2 = (int) (Math.random() * n);
                if ((v1 != v2) && (output[v1][v2] == 0)) {
                    output[v1][v2] = 1;
                    output[v2][v1] = 1;
                    edgeBuilt = true;
                }
            }
        }
        return output;
    }

    static int[][] gridGraph(int n1, int n2, int n3) {
        int[][] output = new int[n1 * n2 * n3][n1 * n2 * n3];
        for (int i = 0; i < n1 * n2 * n3; i++) {
            if (i % n1 != n1 - 1) {
                output[i][i + 1] = 1;
            }
            if (i % n1 != 0) {
                output[i][i - 1] = 1;
            }
            if ((i / (n1 * n2)) != 0) {
                output[i][i - n1 * n2] = 1;
            }
            if ((i / (n1 * n2)) != n3 - 1) {
                output[i][i + n1 * n2] = 1;
            }
            if ((i % (n1 * n2)) >= n1) {
                output[i][i - n1] = 1;
            }
            if ((i % (n1 * n2)) < n1 * (n2 - 1)) {
                output[i][i + n1] = 1;
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
        long count = 0;
        BigInteger totalNumDivisors = choose(g.size() + deg - 1, g.size());
        Iterator<int[]> d;
        while (true) {

            System.out.println(deg);

            if (sym) {
                d = new SymmetryDegreeIterator(deg, n, degreeList);
            } else {
                d = new DegreeIterator(deg, n, degreeList);
            }
            int i = 1;
            while (d.hasNext()) {
                // optimization?: order vertices in graph from max to min degree
                count++;
                if (count % 1000000 == 0) {
                    System.out
                            .println("degree: " + deg + ", " + "checked " + count + " divisors of " + totalNumDivisors);
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
                // int last = (n+i-1)%n;

                int last = ((n + i - 3) % (n - 1)) + 1;
                while (i != last) {
                    // for (int i = 1; i<n; i++){
                    if ((!pos[i]) && (divisorCopy[i] == 0)) {

                        if (!checkQReducedWinnable(g, divisorCopy, i, pos)) {
                            found = false;
                            break;
                        }
                    }
                    // i=(i+1)%n;

                    i = ((i) % (n - 1)) + 1;
                }
                if (found) {
                    System.out.println(Arrays.toString(currentDivisor));
                    return deg;
                }
            }
            count = 0;
            deg++;
            totalNumDivisors = choose(g.size() + deg - 1, g.size());
        }
    }

    int parallelGonality(Graph g, int deg, boolean sym) throws Exception {
        int numCores = Runtime.getRuntime().availableProcessors();
        int[] degreeList = g.degreeList();
        int n = degreeList.length;
        long count = 0;
        BigInteger totalNumDivisors = choose(g.size() + deg - 1, g.size());
        while (true) {
            System.out.println(deg);
            AtomicBoolean stopWork = new AtomicBoolean(false);
            Thread[] threads = new Thread[numCores];
            for (int i = 0; i < numCores; i++) {
                Iterator<int[]> d;
                if (sym) {
                    d = new SymmetryDegreeIterator(deg, n, degreeList);
                } else {
                    d = new DegreeIterator(deg, n, degreeList);
                }
                Thread next = new GonalityThread(i, numCores, d, stopWork, n, g, deg);
                next.start();
                threads[i] = next;
            }
            
            for (int i = 0; i < numCores; i++) {
                threads[i].join();
            }

            if (stopWork.get()) {
                return deg;
            }
            deg++;
            totalNumDivisors = choose(g.size() + deg - 1, g.size());
        }
    }

    private BigInteger choose(int n, int k) {
        if (n < k)
            return new BigInteger("-1");
        if (k == 0)
            return BigInteger.ONE;
        if (n == k)
            return BigInteger.ONE;
        return choose(n - 1, k - 1).multiply(BigInteger.valueOf(n)).divide(BigInteger.valueOf(k));
    }
}

class GonalityThread extends Thread {
    int offset;
    Iterator<int[]> iter;
    AtomicBoolean stopWork;
    int n;
    Graph g;
    int deg;
    int numCores;

    public GonalityThread(int offset, int numCores, Iterator<int[]> iter, AtomicBoolean stopWork, int n, Graph g,
            int deg) {
        this.offset = offset;
        this.iter = iter;
        this.stopWork = stopWork;
        this.n = n;
        this.g = g;
        this.deg = deg;
        this.numCores = numCores;
    }

    public void run() {
        Gonality obj = new Gonality();
        int[] currentDivisor = new int[n];
        for (int i = 0; i < offset; i++) {
            if (iter.hasNext()) {
                currentDivisor = iter.next();
            } else {
                return;
            }
        }
        while (iter.hasNext() && !stopWork.get()) {

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

                    if (!obj.checkQReducedWinnable(g, divisorCopy, i, pos)) {
                        found = false;
                        break;
                    }
                }
            }
            if (found) {
                System.out.println(Arrays.toString(currentDivisor));
                stopWork.set(true);
            }

            for (int i = 0; i < numCores; i++) {
                if (iter.hasNext() && !stopWork.get()) {
                    currentDivisor = iter.next();
                } else {
                    return;
                }
            }
        }
    }
}
