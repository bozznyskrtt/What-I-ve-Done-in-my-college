package maingame;
import java.awt.*;
public class ball  {
    static final int maxspeed = 8;
    private int x,y,size,bounce,speed,px,py,score1,score2;
    private Color color;

    public int getSize() {
        return size;
    }
    public ball(int x, int y , int px, int py,int size, Color color, int speed){
    this.x=x;
    this.y=y;
    this.px=px;
    this.py=py;
    this.size=size;
    this.color=color;
    this.speed=speed;
}
    public void paint(Graphics g){
        g.setColor(color);
        g.fillOval(x,y,size,size);
    }
    public void ballmove(){
        x+=px;
        y+=py;
        if (bounce==5) {
            spdincraese();
            bounce=0;
        }
        }
    public int getBounce() {
        return bounce;
    }
    public void spdincraese(){
        System.out.println(speed);
        if (speed<maxspeed){
            speed+=1;
            px=(px/Math.abs(px))*speed;
            py=(py/Math.abs(py))*speed;
        }
    }
    public void ballbounce2p(){
        if (y>550){
           reverseY();
           bounce+=1;
        }
        if (y<20){
            reverseY();
            bounce+=1;
        }
        if (x<0){
            score2+=1;
        }
        if (x>900){
            score1+=1;
        }
    }
    public void ballbounce1p(){
        if (y>550){
            reverseY();
            bounce+=1;
        }
        if (y<20){
            reverseY();
            bounce+=1;
        }
        if (x<=0){
            score2+=1;
        }
        if (x>=880){
           reverseX();
        }
    }
    public void reverseY(){py*=-1;}
    public void reverseX(){px*=-1;}
    public int getY() {return y;}
    public int getX() {return x;}
    public String getScore1() {return String.valueOf(score1);}
    public String getScore2() {
        return String.valueOf(score2);
    }
    public void setX(int x) {this.x = x;}
    public void setY(int y) {this.y = y;}
    public void setSpeed(int speed) {this.speed = speed;}
    public void setPx(int px) {this.px = px;}
    public void setPy(int py) {this.py = py;}
    public void setBounce(int bounce) {this.bounce = bounce;}
}
