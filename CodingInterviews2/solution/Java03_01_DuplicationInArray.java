import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Java03_01_DuplicationInArray {

    public static int findDuplication(int[] ints) {
        Set<Integer> set = new HashSet<>();
        for (int anInt : ints) {
            if (set.contains(anInt)) {
                return anInt;
            }
            else {
                set.add(anInt);
            }
        }
        return 0;
    }

}