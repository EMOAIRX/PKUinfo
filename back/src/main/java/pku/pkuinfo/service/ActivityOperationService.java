package pku.pkuinfo.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pku.pkuinfo.mapper.ActivityMapper;
import pku.pkuinfo.pojo.ActivityInfo;
import pku.pkuinfo.pojo.WeekActivityInfo;

import java.sql.Date;
import java.util.Calendar;
import java.util.HashMap;
import java.util.ArrayList;
import org.json.JSONObject;
import pku.pkuinfo.pojo.Link;

import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Objects;


import java.util.List;

@Service
public class ActivityOperationService {

    @Autowired
    private ActivityMapper activityMapper;

    private final long ONE_DAY = 1000 * 60 * 60 * 24;

    public Boolean insert(ActivityInfo info){
        Integer res = activityMapper.insertActivity(info);
        return (res != null);
    }

    public List<ActivityInfo> select(Date startDate){
        Date endDate = new Date(startDate.getTime() + ONE_DAY * 30);
        return activityMapper.selectActivity(startDate,endDate);
    }


    public static List<Float> extractEmbedding(String jsonString) {
        List<Float> embeddingList = new ArrayList<>();

        // Find the start and end indices of the embedding array
        int startIndex = jsonString.indexOf("[");
        int endIndex = jsonString.indexOf("]");

        if (startIndex != -1 && endIndex != -1) {
            // Extract the embedding string and split into values
            String embeddingString = jsonString.substring(startIndex + 1, endIndex);
            String[] embeddingArray = embeddingString.split(",");

            for (String value : embeddingArray) {
                // Convert each value to float and add to the embedding list
                try {
                    float floatValue = Float.parseFloat(value.trim());
                    embeddingList.add(floatValue);
                } catch (NumberFormatException e) {
                    e.printStackTrace();  // Handle invalid float values
                }
            }
        }

        return embeddingList;
    }

    private List<Float> getEmbedding_from_text(String text) {
        JSONObject json = new JSONObject();
        try{
            json.put("text", text);
        } catch (Exception e) {
            e.printStackTrace();
        }
        URL serverUrl = null;
        try {
            serverUrl = new URL("http://localhost:9001/getEmbedding");
        } catch (Exception e) {
            e.printStackTrace();
        }
        HttpURLConnection connection = null;
        try {
            connection = (HttpURLConnection) serverUrl.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setDoOutput(true);
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
            String res = null;
            res = responseBuilder.toString();
            // {"embedding":value}
            // from json format contrive embedding
            // println(res);
            System.out.println(res);
            // contrive json data from res to get embedding
            List<Float> embedding = new ArrayList<Float>();
            embedding = extractEmbedding(res);
            return embedding;
            // return res;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    private Float cosine_similarity(List<Float> embedding1, List<Float> embedding2) {
        Float res = 0.0f;
        for (int i = 0; i < embedding1.size(); i++) {
            res += embedding1.get(i) * embedding2.get(i);
        }
        return res;
    }

    private HashMap<Integer, List<Float>> cachedEmbedding = new HashMap<Integer, List<Float>>();
    private HashMap<Integer, Float> value = new HashMap<Integer, Float>();
    public List<ActivityInfo> search(String text, Date startDate, Date endDate){
        List<ActivityInfo> Result = activityMapper.selectActivity(startDate, endDate);
        //text embedding
        List<Float> text_embedding = getEmbedding_from_text(text);
        List<Float> embedding;
        for (ActivityInfo activity : Result) {
            Integer id = activity.getId();
            String description = activity.getDescription();
            // System.out.println(id);
            // System.out.println(description);
            if (cachedEmbedding.containsKey(id)) {
                embedding = cachedEmbedding.get(id);
            } else {
                embedding = getEmbedding_from_text(description);
                cachedEmbedding.put(id, embedding);
            }
            value.put(id, cosine_similarity(embedding, text_embedding));
            // System.out.println(value.get(id));
        }
        // sort by value from large to small
        Result.sort((a, b) -> Float.compare(value.get(b.getId()), value.get(a.getId())));
        return Result;
    }
}
