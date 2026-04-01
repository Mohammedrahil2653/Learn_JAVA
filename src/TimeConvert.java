public class TimeConvert {
    public static void main(String[] args) {
        System.out.println("10 min ="+getDuration(10));
        System.out.println("1hour 10 min ="+getDuration(1,10));
    }
    public static int getDuration(int minutes){

        return minutes*60;

    }
    public static int getDuration(int hour, int minutes){

        //return (hour*60 + minutes)*60; //direct menthod
        //easy to readable
       int newminutes = hour*60;
       int totalminutes = newminutes+minutes;
       int  TotalSeconds = totalminutes*60;
        return getDuration(TotalSeconds);

    }
}
