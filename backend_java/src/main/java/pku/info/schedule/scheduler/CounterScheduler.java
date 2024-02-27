package pku.info.schedule.scheduler;

import jakarta.annotation.Resource;
import org.springframework.scheduling.annotation.Async;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import pku.info.schedule.service.CounterSchedulerService;

@EnableAsync
@EnableScheduling
@Component
public class CounterScheduler {

    @Resource
    private CounterSchedulerService counterSchedulerService;

    @Scheduled(cron = "* 0/10 * * * ?")
    @Async("CustomAsyncThreadPool")
    public void saveCacheData() {
        counterSchedulerService.saveViewData();
    }
}
