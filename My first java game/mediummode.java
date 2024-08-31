package maingame;

import menu.pagestart;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class mediummode extends JPanel implements KeyListener , MouseListener {
    ball myball1,myball2;
    paddle mypaddle;
    public static boolean stop;
    public static JButton buttonresume ;
    public static JButton buttonback ;
    public mediummode(){
        buttonresume = new button("RESUME");
        buttonback = new button("BACK");
        setLayout(null);
        ((button) buttonresume).buttonresumesetbounds();
        ((button) buttonback).buttonbacksetbounds();
        myball1 = new ball(450,300,3,3,20, Color.white,3);
        myball2 = new ball(500,200,3,3,20,Color.white,3);
        mypaddle = new paddle(0,200,20,80,Color.blue);
        addKeyListener(this);
        setFocusable(true);
        addMouseListener(this);
    }
    public void paintComponent(Graphics g){
        g.setColor(Color.black);
        g.fillRect(0,0,900,600);
        myball1.paint(g);
        myball2.paint(g);
        mypaddle.paint(g);
    }
    public void logic(){
        myball1.ballmove();
        myball1.ballbounce1p();
        myball2.ballmove();
        myball2.ballbounce1p();
        if (stop) {
            add(buttonresume);
            add(buttonback);
            repaint();
            pagestart.timer1.stop();
        }
        if(mypaddle.bounce(myball1)){myball1.reverseX();}
        if(mypaddle.bounce(myball2)){myball2.reverseX();}
        reset();
    }
    public void reset(){
        if (myball1.getX()<0){
            myball1.setY(300);
            myball1.setX(450);
            myball1.setPy(3);
            myball1.setPx(3);
            myball1.setSpeed(3);
            myball1.setBounce(0);
        }
        if (myball2.getX()<0){
            myball2.setX(500);
            myball2.setY(200);
            myball2.setPy(3);
            myball2.setPx(3);
            myball2.setSpeed(3);
            myball2.setBounce(0);
            myball1.setY(300);
            myball1.setX(450);
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
