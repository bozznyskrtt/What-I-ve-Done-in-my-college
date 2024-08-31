package maingame;

import java.awt.*;

public class paddleinfo {
    protected int x,y,w,h;
    Color color;
    public paddleinfo(int x,int y,int w,int h,Color color){
        this.x=x;
        this.y=y;
        this.w=w;
        this.h=h;
        this.color=color;
    }
    public void moveup() {
        y -= 20;
    }
    public void movedown(){
        y+=20;

    }
    public void paint(Graphics g){
        g.setColor(color);
        g.fillRect(x,y,w,h);
    }
    public boolean bounce(ball b){
        if (b.getX()>=(x-b.getSize()) && b.getX()<=(x+w)){
            if (b.getY()>=y && b.getY()<=(y+h)){
                System.out.println("bounce");
                return true;
            }
        }
        return false;
    }

}
