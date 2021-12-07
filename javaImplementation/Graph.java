package javaImplementation;
import java.util.LinkedList;
import java.util.Arrays;

public class Graph {
    private LinkedList<Integer>[] nodes;
    private int[][] adjacencyMatrix;
    private int[] degreeList;
    private int size;

    public Graph(LinkedList<Integer>[] nodes) {
        size = nodes.length;
        this.nodes = nodes;
        makeAdjacency();
        makeDegrees();
    }

    public Graph(int[][] adjacencyMatrix) {
        size = adjacencyMatrix.length;
        this.adjacencyMatrix = adjacencyMatrix;
        makeNodes();
        makeDegrees();
    }

    private void makeAdjacency() {
        adjacencyMatrix = new int[size][size];
        for (int i = 0; i < size; i++) {
            for (Integer j : nodes[i]) {
                adjacencyMatrix[i][j] = 1;
            }
        }
    }

    private void makeNodes() {
        nodes = new LinkedList[size];
        for (int i = 0; i < size; i++) {
            LinkedList<Integer> neighbors = new LinkedList<>();
            for (int j = 0; j < size; j++) {
                if (adjacencyMatrix[i][j] == 1) {
                    neighbors.add(j);
                }
            }
            nodes[i] = neighbors;
        }
    }

    public void makeDegrees() {
        degreeList = new int[size];
        for (int i = 0; i < size; i++) {
            degreeList[i] = nodes[i].size();
        }
    }

    public boolean isAdjacent(int node1, int node2) {
        if (adjacencyMatrix[node1][node2] == 1) {
            return true;
        }
        return false;
    }

    public LinkedList<Integer> getNeighbors(int n) {
        return nodes[n];
    }

    public int[] degreeList() {
        return degreeList;
    }

    public int size() {
        return size;
    }

    public String toString() {
        return Arrays.toString(nodes);
    }

    public Graph product(Graph g) {

        int size1 = this.size();
        int size2 = g.size();
        int[][] l3 = new int[size1 * size2][size1 * size2];
        for (int i = 0; i < size2; i++) {
            for (int x = 0; x < size1; x++) {
                for (int y = 0; y < size1; y++) {
                    if (this.isAdjacent(x, y)) l3[x + size1*i][y + size1*i] = 1;
                }
            }
        }
        for (int i = 0; i < size1; i++) {
            for (int x = 0; x < size2; x++) {
                for (int y = 0; y < size2; y++) {
                    if (g.isAdjacent(x, y)) l3[x*size1 + i][y*size1 + i] = 1;
                }
            }
        }
        return new Graph(l3);
    }

    //cycle graph on n vertices
    public static Graph cycle(int n) {
        int[][] cycleAdj = new int[n][n];
        for (int i = 0; i < n; i++) {
            cycleAdj[i][((i-1) + n) % n] = 1;
            cycleAdj[i][((i+1) + n) % n] = 1;
        }
        return new Graph(cycleAdj);
    }

    //path graph on n vertices
    public static Graph path(int n) {
        int[][] pathAdj = new int[n][n];
        if (n == 1) {
            pathAdj = new int[][] {{0}};
        }
        pathAdj[0][1] = 1;
        pathAdj[n-1][n-2] = 1;
        for (int i = 1; i < n - 1; i++) {
            pathAdj[i][((i-1) + n) % n] = 1;
            pathAdj[i][((i+1) + n) % n] = 1;
        }
        return new Graph(pathAdj);
    }

}