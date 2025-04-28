/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/**
 *
 * @author quint
 */
import java.util.Scanner;

public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
           Scanner scanner = new Scanner(System.in);
           //Start
           System.out.println("*************************Welcome to the Unit Converter*************************");
           System.out.println("");
           System.out.println("What type of conversion would you like to do?");
           System.out.println("");
           //find what conversion type we are doing
           System.out.println("1 = Convert Temperature");
           System.out.println("2 = Convert Length");
           System.out.println("3 = Convert Weight");
           System.out.println("4 = Exit");
           String cType = scanner.nextLine();
           switch (cType){
               case "1":
                   Temp();
                   break;
               case "2":
                   Length();
                   break;
               case "3":
                   Weight();
                   break;
               case "e":
                   System.exit(0);
                   break;
           }
                   
           
    }
    public static void Temp(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("What would you like to convert?");
        System.out.println("1 = Farenheit to Celsius");
        System.out.println("2 = Celsius to Farenheit");
        System.out.println("4 = Exit");
        String tempType = scanner.nextLine();
        
        Convert(tempType);
    }
    public static void Length(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("What would you like to convert?");
        System.out.println("3 = Kilometers to Miles");
        System.out.println("5 = Miles to Kilometers");
        System.out.println("4 = Exit");
        String lengthType = scanner.nextLine();



        Convert(lengthType);
    }
    public static void Weight(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("What would you like to convert from?");
        System.out.println("6 = Kilogram to Pound");
        System.out.println("7 = Pound to Kilogram");
        System.out.println("4 = Exit");
        String weightType = scanner.nextLine();

       Convert(weightType);
    }
    public static void Convert( String conversion){
        Scanner scanner = new Scanner(System.in);
        System.out.println("");
        switch(conversion){
            case "1":
                System.out.println("How many degrees F");
                int val = scanner.nextInt();
                double result = val - 32;
                result = result * 5/9;
                System.out.println(result);
                
                break;
            case "2":
                System.out.println("How many degrees C");
                val = scanner.nextInt();
                result = val * 1.8;
                result = result +32;
                System.out.println(result);
                break;
            case "3":
                System.out.println("How many kilometers");
                val = scanner.nextInt();
                result = val * 0.621371;
                System.out.println(result);
                break;
            case "4":
                System.exit(0);
                break;
            case "5":
                System.out.println("How many miles");
                val = scanner.nextInt();
                result = val / 0.621371;
                System.out.println(result);
                break;
            case "6":
                System.out.println("How many kilograms");
                val = scanner.nextInt();
                result = val * 2.20462;
                System.out.println(result);
                break;
            case "7":
                System.out.println("How many pounds");
                val = scanner.nextInt();
                result = val / 2.20462;
                System.out.println(result);
                break;
                       
        }
    }

 
}

