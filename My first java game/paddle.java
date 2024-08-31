package maingame;

import maingame.ball;

import javax.swing.*;
import java.awt.*;
import javax.swing.JPanel.*;
public class paddle extends paddleinfo  {
    protected int x,y,w,h;
    Color color;

    public paddle(int x,int y,int w,int h,Color color){
        super(x,y,w,h,color);
    }
    public void paint(Graphics g){
        super.paint(g);

    }
    public void moveup(){
        super.moveup();

    }
    public void movedown(){
        super.movedown();

    }

    public boolean bounce(ball b){
        return super.bounce(b);
    }

}
