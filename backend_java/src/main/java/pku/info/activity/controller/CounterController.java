package pku.info.activity.controller;

import jakarta.annotation.Resource;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RestController;
import pku.info.activity.service.CounterService;
import pku.info.common.Result;

@RestController
@CrossOrigin(origins = "*")
public class CounterController {
    @Resource
    private CounterService counterService;

    @PutMapping("/view/{id}")
    public Result addViewCounter(@PathVariable Integer id){
        return counterService.addView(id);
    }
}
