package menu;
import javax.swing.*;
import java.awt.*;
import maingame.*;

public class pagestart extends JFrame {
    public static boolean easy,medium,hard,twoplayer,solo;
    public static Timer timer1;
    easymode em;
    mediummode mm;
    hardmode hm;
    twoplayermode tpm;
    JPanel panel = new JPanel();
    JPanel panel2 = new JPanel();
    JPanel panel3 = new JPanel();
    JPanel panel4 = new JPanel();
    JPanel panel5 = new JPanel();
    JPanel panel6 = new JPanel();
    JPanel panel7 = new JPanel();
    JPanel panelborder = new JPanel();
    JPanel panelgrid = new JPanel();
    JButton button = new JButton("Start");
    JLabel label = new JLabel("Pong Game");
    JLabel label2 = new JLabel("Pong Game");
    JLabel label3 = new JLabel("Pong Game");
    JButton button2 = new JButton("SOLO");
    JButton button3 = new JButton("TWO PLAYERS");
    JButton button4 = new JButton("Easy");
    JButton button5 = new JButton("Medium");
    JButton button6 = new JButton("Hard");
    JFrame frame = new JFrame("YOUR PONG");
    JFrame frame2 = new JFrame("YOUR PONG");
    JFrame frame3 = new JFrame("YOUR PONG");
    JFrame frame4 = new JFrame("YOUR PONG");
    JFrame frame5 = new JFrame("YOUR PONG");
    JFrame frame6 = new JFrame("YOUR PONG");
    JFrame frame7 = new JFrame("YOUR PONG");
    public pagestart(){
        em = new easymode();
        mm = new mediummode();
        hm = new hardmode();
        tpm = new twoplayermode();
        button.addActionListener(e -> {
            frame.setVisible(false);
            frame2.setVisible(true);
        });
        button2.addActionListener(e -> {
            solo=true;
            frame2.setVisible(false);
            frame3.setVisible(true);
        });
        button3.addActionListener(e -> {
            twoplayer =true;
            timer1.start();
            frame2.setVisible(false);
            frame7.setVisible(true);

        });
        button4.addActionListener(e -> {
            easy=true;
            timer1.start();
            frame3.setVisible(false);
            frame4.setVisible(true);

        });
        button5.addActionListener(e -> {
            medium=true;
            timer1.start();
            frame3.setVisible(false);
            frame5.setVisible(true);
        });
        button6.addActionListener(e -> {
            hard=true;
            timer1.start();
            frame3.setVisible(false);
            frame6.setVisible(true);

        });
        easymode.buttonresume.addActionListener(e -> {
            easymode.stop = false;
            timer1.start();
            em.remove(easymode.buttonback);
            em.remove(easymode.buttonresume);
        });
        easymode.buttonback.addActionListener(e -> {
            easy= false;
            easymode.stop = false;
            em.remove(easymode.buttonback);
            em.remove(easymode.buttonresume);
            frame4.setVisible(false);
            frame.setVisible(true);
        });
        mediummode.buttonresume.addActionListener(e -> {
            timer1.start();
            mediummode.stop = false;
            mm.remove(mediummode.buttonback);
            mm.remove(mediummode.buttonresume);
        });
        mediummode.buttonback.addActionListener(e -> {
            medium = false;
            mediummode.stop=false;
            mm.remove(mediummode.buttonback);
            mm.remove(mediummode.buttonresume);
            frame5.setVisible(false);
            frame.setVisible(true);
        });
        hardmode.buttonresume.addActionListener(e -> {
            timer1.start();
            hardmode.stop=false;
            hm.remove(hardmode.buttonback);
            hm.remove(hardmode.buttonresume);
        });
        hardmode.buttonback.addActionListener(e -> {
            hard = false;
            hardmode.stop=false;
            hm.remove(hardmode.buttonback);
            hm.remove(hardmode.buttonresume);
            frame6.setVisible(false);
            frame.setVisible(true);
        });
        twoplayermode.buttonresume.addActionListener(e -> {
            timer1.start();
            twoplayermode.stop=false;
            tpm.remove(twoplayermode.buttonback);
            tpm.remove(twoplayermode.buttonresume);
        });
        twoplayermode.buttonback.addActionListener(e -> {
            twoplayer = false;
            twoplayermode.stop = false;
            tpm.remove(twoplayermode.buttonback);
            tpm.remove(twoplayermode.buttonresume);
            frame7.setVisible(false);
            frame.setVisible(true);
        });
        button.setBounds(350,250,200,100);
        button2.setBounds(350,250,200,100);
        button3.setBounds(350,350,200,100);
        label.setBounds(380, 50, 300, 150);
        label2.setBounds(380, 50, 300, 150);
        label3.setBounds(380,50,300,150);
        label.setFont(new Font("Comic Sans MS", Font.BOLD, 30));
        label2.setFont(new Font("Comic Sans MS", Font.BOLD, 30));
        label3.setFont(new Font("Comic Sans MS", Font.BOLD, 30));
        label.setForeground(Color.pink);
        label.setBackground(Color.white);
        label2.setForeground(Color.magenta);
        label3.setForeground(Color.RED);

        panel.setLayout(new BorderLayout());
        panelborder.setLayout(null);
        panel.setBackground(Color.BLACK);
        panelborder.add(button);
        panelborder.add(label);
        panelborder.setBackground(Color.BLACK);
        panel.add(panelborder,BorderLayout.CENTER);
        panel2.setLayout(null);
        panel2.setBackground(Color.black);
        panel2.add(button2);
        panel2.add(button3);
        panel2.add(label2);
        panel3.setLayout(null);
        panelgrid.setLayout(new GridLayout(1,3));
        panelgrid.setBounds(150,250,600,100);
        panel3.setBackground(Color.black);
        panelgrid.setBackground(Color.BLACK);
        panelgrid.add(button4);
        panelgrid.add(button5);
        panelgrid.add(button6);
        panel3.add(panelgrid);
        panel3.add(label3);
        panel4.setLayout(null);
        panel4.add(em);
        panel5.setLayout(null);
        panel5.add(mm);
        panel6.setLayout(null);
        panel6.add(hm);
        panel7.setLayout(null);
        panel7.add(tpm);
        //panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.add(panel);
        frame.setSize(900, 600);
        frame.setVisible(true);
        frame.setResizable(false);
        frame.setLocationRelativeTo(null);

        frame2.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame2.add(panel2);
        frame2.setSize(900, 600);
        frame2.setVisible(false);
        frame2.setResizable(false);
        frame2.setLocationRelativeTo(null);

        frame3.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame3.add(panel3);
        frame3.setSize(900, 600);
        frame3.setVisible(false);
        frame3.setResizable(false);
        frame3.setLocationRelativeTo(null);

        frame4.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame4.add(em);
        frame4.setSize(900, 600);
        frame4.setVisible(false);
        frame4.setResizable(false);
        frame4.setLocationRelativeTo(null);

        frame5.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame5.add(mm);
        frame5.setSize(900, 600);
        frame5.setVisible(false);
        frame5.setResizable(false);
        frame5.setLocationRelativeTo(null);

        frame6.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame6.add(hm);
        frame6.setSize(900, 600);
        frame6.setVisible(false);
        frame6.setResizable(false);
        frame6.setLocationRelativeTo(null);

        frame7.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame7.add(tpm);
        frame7.setSize(900, 600);
        frame7.setVisible(false);
        frame7.setResizable(false);
        frame7.setLocationRelativeTo(null);

        timer1 = new Timer(33, e -> {
            if (easy){
                em.logic();
                em.repaint();
            }
            if (medium){
                mm.logic();
                mm.repaint();
            }
            if (hard){
                hm.logic();
                hm.repaint();
            }
            if (twoplayer){
                tpm.logic();
                tpm.repaint();
            }
        });
    }

}
