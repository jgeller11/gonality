package javaImplementation;

import java.util.Iterator;

class DegreeIterator implements Iterator<int[]> {
    private int[] current;
    private int max;

    public DegreeIterator(int degree, int length) {
        current = new int[length];
        max = degree;
        current[length - 1] = degree-1;
        current[0] = 1;
    }

    public boolean hasNext() {
        return current[0] != max;
    }

    public int[] next() {
        int msi = -1;
        for (int i = current.length - 1; i >= 0; i--) {
            if (current[i] != 0) {
                msi = i - 1;
                break;
            }
        }
        current[msi] += 1;
        current[current.length - 1] = current[msi + 1] - 1;
        if (msi + 1 != current.length - 1) {
            current[msi + 1] = 0;
        }
        return current;
    }
}