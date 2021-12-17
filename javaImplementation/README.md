# Algorithms for Calculating Gonality

Included in this project are four classes, Graph, DegreeIterator, SymmetryDegreeIterator, and Gonality.

## Graph

A generic new graph can be initialized by using the constructor that takes an adjacency list. We have also included a few families of graphs that can be built from a variety of methods. Namely, `path(int n)` and `cycle(n)` create path and cycle graphs on n vertices, `harary(int n, int k)` returns the harary graph on `n` vertices, each of degree `2k`, randomGraph returns a randomly generated graph on `n` vertices with `m` total edges, and `product(Graph g)` returns the Cartesian product of two graphs.

```
// initializes g1 as the cycle on 5 vertices
Graph g1 = Graph.cycle(5);

// initializes g2 as the 3x3 grid graph
Graph g2 = Graph.path(3).product(Graph.path(3));
```

## DegreeIterator, SymmetryDegreeIterator

These classes are really only necessary in the process of calculating gonality, and wouldn't generally be especially useful to a user. `DegreeIterator(int degree, int length, int[] degrees)` constructs an iterator which will return divisors as int arrays of size `length`. Each divisor is distinct from the others, never has a larger value at position `i` than `degrees[i]`, and the sum of all the entries in each divisor is `degree`. Finally, every divisor `d` satisfies `d[0]≥1`. `SymmetryDegreeIterator` works in much the same way, except it does not accept `int[] degrees` since it doesn't turn out to offer much of a speedup in most cases, and all divisors returned will satisfy `d[0]≥d[i]` for all `i`.

## Gonality

This class contains all of the methods related to chip-firing. `gonality(Graph g, int deg, boolean sym)` returns the gonality of a graph g while providing progress updates. `deg` should be a known lower bound on the gonality of a graph so that it looks first at divisors of degree `deg`. Setting `sym` to `true` has the method use a `SymmetryDegreeIterator` rather than a `DegreeIterator`. As a result, `sym` should be set to `true` when and only when the graph is known to be vertex-transitive. Not providing `sym` and/or `deg` sets them to `false` and `1` by default.

`parallelGonality(Graph g, int deg, boolean sym)` works in essentially the same way, except it provides less detailed progress updates and uses multiple cores. This is the fastest method for calculating gonality, and should generally be used in place of `gonlity`, except for small graphs with gonalities which are especially easy to compute.

Both gonality methods print out a winning divisor when they eventually find one. Note that the divisor that is eventually printed out is not guaranteed to be the one that the `DegreeIterator` or `SymmetryDegreeIterator` returns, since that divisor is modified in the process of calculating gonality. The printed divisor will still be equivalent to that divisor though, and so it is still guaranteed to win the gonality game. 

```
// prints "[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]"
// prints "9"
Graph graph1 = Graph.path(4).product(Graph.path(3)).product(Graph.path(3));
System.out.println(g.gonality(graph1));

// prints "[1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 1, 0, 0, 0]"
// prints "8"
Graph graph2 = Graph.cycle(4).product(Graph.cycle(4));
System.out.println(g.parallelGonality(graph2, 6, true));

```

