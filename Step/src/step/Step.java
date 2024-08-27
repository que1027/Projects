/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package step;

/**
 *
 * @author quint
 */


 import java.io.FileWriter;
 import java.io.IOException;
import java.io.BufferedWriter;
import java.io.IOException;

 import javax.swing.Box;
 import javax.swing.BoxLayout;
 import javax.swing.JButton;
 import javax.swing.JFrame;
 import javax.swing.JLabel;
 import javax.swing.JPanel;
 import javax.swing.JTextField;
 import javax.swing.SwingUtilities;
 
 import java.awt.GridBagConstraints;
 import java.awt.GridBagLayout;
 import java.awt.Insets;
 import java.awt.Font;
 import java.awt.*;
 import java.awt.event.*;
 
public class Step {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //create a JFrame instance
         JFrame Window = new JFrame();
         //create panel
             JPanel Canvas = new JPanel();
         //make elements go under each other
         Canvas.setLayout(new BoxLayout(Canvas, BoxLayout.Y_AXIS));
         //give the window a name
            Window.setTitle("Step");
            //set window size
            Window.setSize(400, 400);
           //auto size
 //           Window.pack();
            //allow X to close window
            Window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
 
            //thigs to go inside the canvas
            //labels
            JLabel tasksLabel = new JLabel("Tasks");
            tasksLabel.setFont(new Font("Serif",Font.BOLD, 20));
            //add Task label to canvas
            Canvas.add(tasksLabel);
            
            
            JButton newTask = new JButton("+");
            Canvas.add(newTask);
              //finished label
                  JLabel finished = new JLabel("Finished");
                 finished.setFont(new Font("Serif",Font.BOLD, 20));
                 Canvas.add(finished);
                 
                 
                  //adds canvas to the window
            Window.add(Canvas);
          
                //make the window visible
            Window.setVisible(true);
            
            //managing events
            //new task button press
            //creates event listener and overrides default action in one
          newTask.addActionListener((ActionEvent e) -> {
              
              JFrame createNewTask = new JFrame();
              
              JPanel CnpCnvs = new JPanel( );
              
              JTextField taskName = new JTextField(10);
              JTextField endDate = new JTextField(5);
              JTextField endTime = new JTextField(5);
              JButton createTask = new JButton("Create Task");
                //give the window a name
            createNewTask.setTitle("Create New Task");
            //set window size
            createNewTask.setSize(400, 400);
            CnpCnvs.add(taskName);
            CnpCnvs.add(endDate);
            CnpCnvs.add(endTime);
            CnpCnvs.add(createTask);
            
            createNewTask.add(CnpCnvs);
            createNewTask.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            createNewTask.setVisible(true);
                // create a new task
              createTask.addActionListener((ActionEvent er) -> {
                  //create a new task
                try(BufferedWriter writer = new BufferedWriter(new FileWriter("Tasks.txt", true))){
                  writer.write("test");
                  writer.newLine();
                }catch(IOException error){
                  System.out.println("error writing to file");
                }
                  
              });
          });
          
}
}
