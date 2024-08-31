package maingame;

import menu.pagestart;

import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

public class hardmode extends JPanel implements KeyListener , MouseListener {
    ball myball1,myball2,myball3;
    paddle mypaddle;
    public static boolean stop;
    public static JButton buttonresume;
    public static JButton buttonback ;
    public hardmode(){
        myball1 = new ball(650,300,3,3,20, Color.white,3);
        myball2 = new ball(500,200,3,3,20,Color.white,3);
        myball3 = new ball(200,200,3,3,20,Color.white,3);
        mypaddle = new paddle(0,200,20,70,Color.blue);
        buttonresume = new button("RESUME");
        buttonback = new button("BACK");
        setLayout(null);
        ((button) buttonresume).buttonresumesetbounds();
        ((button) buttonback).buttonbacksetbounds();
        addKeyListener(this);
        setFocusable(true);
        addMouseListener(this);
    }
    public void paintComponent(Graphics g){
        g.setColor(Color.black);
        g.fillRect(0,0,900,600);
        myball1.paint(g);
        myball2.paint(g);
        myball3.paint(g);
        mypaddle.paint(g);
    }
    public void logic(){
        myball1.ballmove();
        myball1.ballbounce1p();
        myball2.ballmove();
        myball2.ballbounce1p();
        myball3.ballmove();
        myball3.ballbounce1p();
        if (stop) {
            add(buttonresume);
            add(buttonback);
            repaint();
            pagestart.timer1.stop();
        }
        if(mypaddle.bounce(myball1)){myball1.reverseX();}
        if(mypaddle.bounce(myball2)){myball2.reverseX();}
        if(mypaddle.bounce(myball3)){myball3.reverseX();}
        reset();
    }
    public void reset(){
        if (myball1.getX()<0){
            myball1.setY(650);
            myball1.setX(450);
            myball1.setPy(3);
            myball1.setPx(3);
            myball1.setSpeed(3);
            myball1.setBounce(0);
        }
        if (myball2.getX()<0) {
            myball2.setX(500);
            myball2.setY(200);
            myball2.setPy(3);
            myball2.setPx(3);
            myball2.setSpeed(3);
            myball2.setBounce(0);
            myball1.setY(650);
            myball1.setX(450);
            myball1.setPy(3);
            myball1.setPx(3);
            myball1.setSpeed(3);
            myball1.setBounce(0);
        }
        if (myball3.getX()<0){
            myball3.setX(200);
            myball3.setY(200);
            myball3.setPx(3);
            myball3.setPy(3);
            myball3.setSpeed(3);
            myball3.setBounce(0);
            myball2.setX(500);
            myball2.setY(200);
            myball2.setPy(3);
            myball2.setPx(3);
            myball2.setSpeed(3);
            myball2.setBounce(0);
            myball1.setY(300);
            myball1.setX(650);
            myball1.setPy(3);
            myball1.setPx(3);
            myball1.setSpeed(3);
            myball1.setBounce(0);
        }
    }

    @Override
    public void keyTyped(KeyEvent e) {}
    @Override
    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode()==KeyEvent.VK_W) {
            mypaddle.moveup();
        }
        if (e.getKeyCode()==KeyEvent.VK_S){
            mypaddle.movedown();
        }
        if (e.getKeyCode()==KeyEvent.VK_P){
            stop = true;

        }
    }
    @Override
    public void keyReleased(KeyEvent e) {}

    @Override
    public void mouseClicked(MouseEvent e) {
        stop = true;
    }

    @Override
    public void mousePressed(MouseEvent e) {

    }

    @Override
    public void mouseReleased(MouseEvent e) {

    }

    @Override
    public void mouseEntered(MouseEvent e) {

    }

    @Override
    public void mouseExited(MouseEvent e) {

    }
}
