package pku.pkuinfo.service;

import org.json.JSONObject;
import org.springframework.stereotype.Service;
import pku.pkuinfo.pojo.Link;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Objects;

@Service
public class ActivityProcessService {

    // 后期要做其他优化
    private String transmitMessage(Link url) {
        String res = null;

        try {
            // Create a JSON object with the URL
            JSONObject json = new JSONObject();
            json.put("URL", url.getLink());

            // Create a URL object for the server
            URL serverUrl = new URL("http://localhost:9001");

            // Open a connection to the server
            HttpURLConnection connection = (HttpURLConnection) serverUrl.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setDoOutput(true);

            // Write the JSON object to the connection's output stream
            OutputStream outputStream = connection.getOutputStream();
            outputStream.write(json.toString().getBytes());
            outputStream.flush();
            outputStream.close();

            // Read the response from the server
            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder responseBuilder = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                responseBuilder.append(line);
            }
            reader.close();

            // Set the response string
            res = responseBuilder.toString();
        } catch (Exception e) {
            e.printStackTrace();
        }

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
