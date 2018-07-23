package Codewars.java;

public class CureCancer {
    class JomoPipi {
        public static int[] mutationLocation(char[][] b) {
            char[] healthy = new String(b[0]).equals(new String(b[1])) ? b[0] : new String(b[0]).equals(new String(b[2])) ? b[0] : b[1];

            int i = 0;
            int cancer_cell_num = -1;
            char[] cancer = new char[0];
            for (char[] array : b) {
                if (!new String(healthy).equals(new String(array))) {
                    cancer = array;
                    cancer_cell_num = i;
                    break;
                }
                ++i;
            }
            if (cancer.length == 0) {
                return new int[0];
            }
            int num_in_cell = -1;
            for (int j = 0; j < healthy.length; ++j) {
                if (healthy[j] != cancer[j]) {
                    num_in_cell = j;
                    break;
                }
            }
            int[] a = new int[2];
            a[0] = cancer_cell_num;
            a[1] = num_in_cell;
            return a;
        }
    }
}
