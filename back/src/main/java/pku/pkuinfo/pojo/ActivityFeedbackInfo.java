package pku.pkuinfo.pojo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class ActivityFeedbackInfo {
    private Integer id;

    private Integer targetActivityId;

    private String type;

    private String description;
}
