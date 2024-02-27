package pku.info.activity.vo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Page {
    private Object[] records;

    private Integer total;

    private Integer size;

    private Integer current;

    private Integer pages;
}
