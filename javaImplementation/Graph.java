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

    public void printAdjList() {
        System.out.println(Arrays.toString(nodes));
    }

}