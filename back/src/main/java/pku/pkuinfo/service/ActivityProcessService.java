package pku.pkuinfo.service;

import org.springframework.stereotype.Service;
import pku.pkuinfo.pojo.Link;

import java.io.*;
import java.net.Socket;
import java.util.Objects;

@Service
public class ActivityProcessService {

    // 后期要做其他优化
    private String transmitMessage(Link url){
        String res = null;

        String message = url.getLink();
        try {
            //创建一个Socket，跟python的8080端口链接
            Socket socket = new Socket("localhost",9001);
            // 建立IO流
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
            BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            //发送数据
            bw.write(message);
            bw.flush();

            //接收数据 IO阻塞
            System.out.println("发送完毕，准备接受");

            res = br.readLine();

            System.out.println("接收完毕");

            //关闭资源
            bw.close();
            br.close();
            socket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println("接收信息： "+res);

        return res;
    }

    public Boolean processActivityLink(Link url){
        // 后期要配合正则表达式检验
        if(url.getLink() == ""){
            return false;
        }
        // 与python端通信
        String res = transmitMessage(url);
        return Objects.equals(res, "success");
    }
}
