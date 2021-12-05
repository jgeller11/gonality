package javaImplementation;
import java.lang.Math;
import java.util.Iterator;

class SymmetryDegreeIterator implements Iterator<int[]> {
    private int[] current;
    private int max;

    public SymmetryDegreeIterator(int degree, int length) {
        current = new int[length];
        max = degree;
        current[0]=1;
        for (int i = current.length-1; i>current.length-degree; i--){
            current[i]=1;
        }
    }

    public boolean hasNext() {
        return current[0] != max;
    }

    public int[] next() {
        boolean p = true;
        while (p) {
            p = false;
            int msi = -1;
            for (int i = current.length - 1; i >= 0; i--) {
                if (current[i] != 0) {
                    msi = i - 1;
                    break;
                }
            }
            // current[msi] += 1;
            current[current.length - 1] = current[msi + 1] - 1;
            
            if (msi + 1 != current.length - 1) {
                current[msi + 1] = 0;
            }
            // if (>current[0])
            if (Math.max(++current[msi],current[current.length-1])>current[0]) {
                p=true;
            }
        }
        return current;
    }
}