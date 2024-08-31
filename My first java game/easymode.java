package maingame;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

import menu.pagestart;

public class easymode extends JPanel implements KeyListener, MouseListener {
    ball myball;
    paddle mypaddle;
    public static boolean stop;
    public static JButton buttonresume = new JButton();
    public static JButton buttonback ;
    public easymode(){
        buttonresume = new button("RESUME");
        buttonback = new button("BACK");
        setLayout(null);
        ((button) buttonresume).buttonresumesetbounds();
        ((button) buttonback).buttonbacksetbounds();
        myball = new ball(450,300,3,3,20, Color.white,3);
        mypaddle = new paddle(0,200,20,100,Color.blue);
        addKeyListener(this);
        setFocusable(true);
        addMouseListener(this);
    }
    public void paintComponent(Graphics g){
        super.paintComponent(g);
        g.setColor(Color.black);
        g.fillRect(0,0,900,600);
        myball.paint(g);
        mypaddle.paint(g);
    }
    public void logic(){
        myball.ballmove();
        myball.ballbounce1p();
        if (stop) {
            add(buttonresume);
            add(buttonback);
            repaint();
            pagestart.timer1.stop();
        }
        if(mypaddle.bounce(myball)){myball.reverseX();}
        reset();
    }
    public void reset(){
        if (myball.getX()<0){
            myball.setY(300);
            myball.setX(450);
            myball.setPy(3);
            myball.setPx(3);
            myball.setSpeed(3);
            myball.setBounce(0);

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
