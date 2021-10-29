import java.util.Scanner;
import java.lang.Math;
public class Main {
  public static void main(String[] args) {
    //triangleArea();
    midPointTable();
    //minuteYearConverter();
    //triangleVolume();
  }
  private static void triangleArea(){
    Scanner ui = new Scanner(System.in);

    System.out.println("Give Me the first x");
    double x1 = ui.nextDouble();

    System.out.println("Give Me the first y");
    double y1 = ui.nextDouble();

    System.out.println("Give Me the second x");
    double x2 = ui.nextDouble();

    System.out.println("Give Me the second y");
    double y2 = ui.nextDouble();

    System.out.println("Give Me the third x");
    double x3 = ui.nextDouble();

    System.out.println("Give Me the third y");
    double y3 = ui.nextDouble();

    double side1=(Math.sqrt(Math.pow((x2+x1),2)+Math.pow((y2+y1),2)));

    double side2=(Math.sqrt(Math.pow((x3+x2),2)+Math.pow((y3+y2),2)));

    double side3=(Math.sqrt(Math.pow((x3+x1),2)+Math.pow((y3+y1),2)));

    double s=((side1+side2+side3)/2);

    double area=(Math.sqrt(s*(s-side1)*(s-side2)*(s-side3)));

    System.out.println("The area of the triangle is "+area);
    ui.close();
  }
  private static void midPointTable(){
    System.out.println("  a\t  b\tMiddle Point");
    System.out.printf("(0,0)\t(2,1)\t%s\n",midPoint(0,0,2,1));

    System.out.printf("(1,4)\t(4,2)\t%s\n",midPoint(1,4,4,2));

    System.out.printf("(2,7)\t(6,3)\t%s\n",midPoint(2,7,6,3));

    System.out.printf("(3,9)\t(10,5)\t%s\n",midPoint(3,9,10,5));

    System.out.printf("(4,11)\t(12,7)\t%s\n",midPoint(4,11,12,7));
  }
  private static String midPoint(double x1,double x2,double y1,double y2){
    double deltaX=(x2-x1)/2+x2;
    double deltaY=(y2-y1)/2+y2;

    String output="("+deltaX+", "+deltaY+")";

    return output;
  }
  private static void minuteYearConverter(){
    Scanner ui = new Scanner(System.in);
    System.out.println("Enter the number of minutes");
    int minutes=ui.nextInt();
    int years=(minutes/525600);
    int rMinutes=(minutes%525600);
    int day=(rMinutes/1440);
    System.out.println(minutes+" minutes is approximately "+years+" years and "+day+" days.");
    ui.close();
  }

  private static void triangleVolume(){
    Scanner ui = new Scanner(System.in);
    System.out.println("Enter the length of the sides of the triangle");
    double sides=ui.nextDouble();
    double area=(((Math.sqrt(3))/4)*(Math.pow(sides,2)));
    double volume=(area*sides);
    System.out.println("area "+area);
    System.out.println("volume "+volume);
    ui.close();
  }
}