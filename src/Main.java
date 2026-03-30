//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        Calculatescore("Rahil",200);
        Calculatescore(800);
        Calculatescore(580,209);

    }
    public static int Calculatescore(String name,int score){
        System.out.println("Name:"+name+"\nScore:"+score);
        return score + 100;
    }
    public static int Calculatescore(int score){
        System.out.println("Score:"+score);
        return score + 160;
    }
    public static int Calculatescore(int rollno,int score){
        System.out.println("name:"+rollno+"\nScore:"+score);
        return score + 140;
    }
}