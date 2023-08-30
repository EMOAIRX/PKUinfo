package pku.pkuinfo;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Calendar;
import java.util.Date;

@SpringBootTest
class PkUinfoApplicationTests {

    @Test
    void contextLoads() {
        //
        java.sql.Date sqlDate = new java.sql.Date(new java.util.Date().getTime());
        System.out.println(sqlDate);
    }

    @Test
    void testPythonWebServer(){
        String msg = "Hello,world";
        try {
            //创建一个Socket，跟服务器的8080端口链接
            Socket socket = new Socket("localhost",9001);
            //使用PrintWriter和BufferedReader进行读写数据
            PrintWriter pw = new PrintWriter(socket.getOutputStream());
            InputStreamReader is = new InputStreamReader(socket.getInputStream());
            //发送数据
            pw.println(msg);
            pw.flush();
            //接收数据
            System.out.println("发送完毕，准备接受");
            int c;
            while((c=is.read())!=-1){
                System.out.print((char)c);
            }
            System.out.println();
            System.out.println("接收完毕");
            //关闭资源
            pw.close();
            is.close();
            socket.close();
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
