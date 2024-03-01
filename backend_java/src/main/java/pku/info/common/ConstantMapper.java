package pku.info.common;

import java.util.HashMap;

public class ConstantMapper {
    private static final HashMap<Integer, String> tags = new HashMap<>(){{
        put(0, null);
        put(1, "招新");
        put(2, "招聘");
        put(3, "学工");
        put(4, "社团");
        put(5, "学术");
        put(6, "讲座");
        put(7, "志愿");
        put(8, "人物");
        put(9, "创业");
        put(10, "科技");
        put(11, "文艺");
        put(12, "体育");
    }};

    private static final HashMap<String, Integer> periods = new HashMap<>(){{
        put("week", 6);
        put("days", 2);
    }};

    public static String translateTag(Integer tagId){
        return tags.get(tagId);
    }

    public static  Integer translatePeriod(String period){
        return periods.get(period);
    }
}
