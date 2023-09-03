package pku.pkuinfo.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class RecordInfo {
    private Integer id;
    private String title;
    private String author;
    private String publish_time;
}
