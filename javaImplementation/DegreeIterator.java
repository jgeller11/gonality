package javaImplementation;

import java.util.Iterator;

class DegreeIterator implements Iterator<int[]> {
    private int[] current;
    private int max;
    private int[] degreeList;
    private boolean first;
    public DegreeIterator(int degree, int length, int[] degrees) {
        first = true;
        current = new int[length];
        max = degree;
        current[length - 1] = degree-1;
        current[0] = 1;
        degreeList = degrees;
    }

    public boolean hasNext() {
        if (first) return true;
        return current[0] != max;
    }

    public int[] next() {
        if (first) {
            first = false;
            return current;
        }
        boolean p = true;
        while (p) {
            p=false;
            int msi = -1;
            for (int i = current.length - 1; i >= 0; i--) {
                if (current[i] != 0) {
                    msi = i - 1;
                    break;
                }
            }
            
            current[current.length - 1] = current[msi + 1] - 1;
            
            if (msi + 1 != current.length - 1) {
                current[msi + 1] = 0;
            }
           
            if (++current[msi]>degreeList[msi]||(current[current.length-1]>degreeList[current.length-1])) {
                if (current[0]<max){
                    p=true;
                }
            }
            
        }
        return current;
    }
}