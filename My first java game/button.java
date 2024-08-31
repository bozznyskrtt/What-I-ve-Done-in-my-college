package maingame;
import javax.swing.*;
import java.awt.*;

public class button extends JButton{

    int width=200,hight = 100;
    public button(String text1){
        super(text1);
    }
    public void buttonresumesetbounds(){
        setBounds(350,100,width,hight);
    }
    public void buttonbacksetbounds(){
        setBounds(350,350,width,hight);
    }
   
}
