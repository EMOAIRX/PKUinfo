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

    public List<ActivityInfo> select(Date startDate, Date endDate){
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


    private HashMap<String, List<Float>> cachedEmbedding = new HashMap<String, List<Float>>();

    private String query_from_URL(String strURL,String text){
        JSONObject json = new JSONObject();
        try{
            json.put("text", text);
        } catch (Exception e) {
            e.printStackTrace();
        }
        URL serverUrl = null;
        try {
            serverUrl = new URL(strURL);
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
            return res;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    private List<Float> getEmbedding_from_text(String text) {
        if (cachedEmbedding.containsKey(text)) {
            return cachedEmbedding.get(text);
        }
        String res = query_from_URL("http://localhost:9001/getEmbedding", text);
        if (res == null) {
            return null;
        }
        List<Float> embedding = new ArrayList<Float>();
        embedding = extractEmbedding(res);
        cachedEmbedding.put(text, embedding);
        return embedding;
    }

    private Float cosine_similarity(List<Float> embedding1, List<Float> embedding2) {
        Float res = 0.0f;
        for (int i = 0; i < embedding1.size(); i++) {
            res += embedding1.get(i) * embedding2.get(i);
        }
        return res;
    }

    private HashMap<Integer, Float> value = new HashMap<Integer, Float>();
    private HashMap<Integer, String> tags = new HashMap<Integer, String>();
    public List<ActivityInfo> search(String text, Date startDate, Date endDate){
        List<ActivityInfo> Result = activityMapper.selectActivity(startDate, endDate);
        //text embedding
        List<Float> text_embedding = getEmbedding_from_text(text);
        List<Float> embedding;
        for (ActivityInfo activity : Result) {
            Integer id = activity.getId();
            String description = activity.getDescription();
            embedding = getEmbedding_from_text(description);
            value.put(id, cosine_similarity(embedding, text_embedding));
        }
        // sort by value from large to small
        Result.sort((a, b) -> Float.compare(value.get(b.getId()), value.get(a.getId())));
        return Result;
    }

    public String query_tag(ActivityInfo activity) {
        Integer id = activity.getId();
        String description = activity.getDescription();
        if (!tags.containsKey(id)) {
            List<Float> embedding = getEmbedding_from_text(description);
            List<String> tags_str = new ArrayList<String>();
            tags_str.add("学术");
            tags_str.add("学工");
            tags_str.add("就业");
            tags_str.add("文艺");
            tags_str.add("体育");
            List<List<Float>> embedding_tags = new ArrayList<List<Float>>();
            for (String tag : tags_str) {
                embedding_tags.add(getEmbedding_from_text(tag));
            }
            List<Float> similar = new ArrayList<Float>();
            for (List<Float> embedding_tag : embedding_tags) {
                similar.add(cosine_similarity(embedding, embedding_tag));
            }
            Float max = 0.0f;
            Integer max_index = 0;
            for (int i = 0; i < similar.size(); i++) {
                if (similar.get(i) > max) {
                    max = similar.get(i);
                    max_index = i;
                }
            }
            tags.put(id, tags_str.get(max_index));
        }
        return tags.get(id);
    }

    public String talking(String text, String appendix) {
        String ques = "现在你正在扮演一个活动信息检索工具，用户想要检索一个信息，用户的输入是：[[" + text + "]]在数据库中的内容有其中一部分和用户的输入相似，内容是：[[" + appendix + "]]现在，你需要回答对用户的输入作出反应，你的回答是[请注意简短回答，尽可能简短，但对话应当风趣幽默自然，不要简单陈列活动]：";
        String res = query_from_URL("http://localhost:9001/getResponse", ques);
        return res;
    }
    
    public List<ActivityInfo> search_tag(String text, Date startDate, Date endDate){
        List<ActivityInfo> Result = activityMapper.selectActivity(startDate, endDate);
        List<ActivityInfo> newResult = new ArrayList<ActivityInfo>();
        for (ActivityInfo activity : Result) {
            Integer id = activity.getId();
            String description = activity.getDescription();
            if (!tags.containsKey(id)) {
                List<Float> embedding = getEmbedding_from_text(description);
                List<String> tags_str = new ArrayList<String>();
                tags_str.add("学术");
                tags_str.add("学工");
                tags_str.add("就业");
                tags_str.add("文艺");
                tags_str.add("体育");
                List<List<Float>> embedding_tags = new ArrayList<List<Float>>();
                for (String tag : tags_str) {
                    embedding_tags.add(getEmbedding_from_text(tag));
                }
                List<Float> similar = new ArrayList<Float>();
                for (List<Float> embedding_tag : embedding_tags) {
                    similar.add(cosine_similarity(embedding, embedding_tag));
                }
                Float max = 0.0f;
                Integer max_index = 0;
                for (int i = 0; i < similar.size(); i++) {
                    if (similar.get(i) > max) {
                        max = similar.get(i);
                        max_index = i;
                    }
                }
                tags.put(id, tags_str.get(max_index));
            }
            System.out.println(text+tags.get(id) + ",,,,," + text);
            if (tags.get(id).equals(text)) {
                newResult.add(activity);
            }
        }
        // sort by value from large to small
        // Result.sort((a, b) -> Float.compare(value.get(b.getId()), value.get(a.getId())));
        System.out.println(newResult);
        return newResult;
    }

    
}
