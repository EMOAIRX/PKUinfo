package pku.pkuinfo.pojo;

import com.fasterxml.jackson.annotation.JsonFormat;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.format.annotation.DateTimeFormat;

import java.sql.Date;
import java.sql.Time;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ActivityInfo {
    private Integer id;

    private String title;

    private String address;

    @DateTimeFormat(pattern="yyyy-MM-dd")
    // @DateTimeFormat(pattern="dd-MM-yyyy")
    @JsonFormat(timezone = "GMT+8",pattern = "yyyy-MM-dd")
    private Date startDate;

    @DateTimeFormat(pattern="yyyy-MM-dd")
    // @DateTimeFormat(pattern="dd-MM-yyyy")
    @JsonFormat(timezone = "GMT+8",pattern = "yyyy-MM-dd")
    private Date endDate;

    @DateTimeFormat(pattern="HH:mm:ss")
    @JsonFormat(timezone = "GMT+8",pattern = "HH:mm:ss")
    private Time endTime;

    @DateTimeFormat(pattern="HH:mm:ss")
    @JsonFormat(timezone = "GMT+8",pattern = "HH:mm:ss")
    private Time startTime;

    private String description;

    private String college;

    private String accountLink;

    private String extraInfo;
}
