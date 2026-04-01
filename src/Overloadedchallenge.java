public class Overloadedchallenge {
    public static void main(String[] args) {
        System.out.println("5ft,2in="+converttoCentimeters(5,2)+ " centimeters");
        System.out.println("10in="+converttoCentimeters(10)+ " centimeters");

    }
    public static double converttoCentimeters(int inches){
        return inches*2.54;
    }
    public static double converttoCentimeters(int feet,int inches){
        //return ((feet*12)+inches)*2.54;
        //return converttoCentimeters((feet*12)+inches);
        int feettoinches = feet*12;
        int totalInches=feettoinches+inches;
        Double result= converttoCentimeters(totalInches);
        return result;

    }

}
