public class Sortprac {

    static int load = 9;

    public static void printA(int[] A) {
        for (int i = 0; i < load; i++) {
            System.out.print(A[i] + " ");
        }
        System.out.println(" ");
    }

    public static void swapArr(int[] A, int i, int j) {
        int temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }
    public static void Insertion1(int[] A) {
        for (int i = 1; i < A.length; i++) {
            int temp = i;
            for (int j=i-1;j>=0;j--) {
                if (A[temp] < A[j]) {
                    swapArr(A, temp, j);
                    printA(A);
                    temp--;
                }
            }
        }
        System.out.println("asdasd");
    }
    public static void Insertion2(int[] A) {
        for (int i = 1; i < A.length; i++) {
            int temp = A[i];
            int j;
            for (j = i; j > 0 && A[j - 1] > temp; j--) {
                // Complete this meth od. Note the method swap is. provided.
                swapArr(A, j, j - 1);
                printA(A);
            }
        }
    }

        public static void main(String[] args){
            int[] A  = {45, 12, 89, 36, 64, 22, 75, 51, 9};
            Insertion1(A);
            Insertion2(A);
        }

    }
