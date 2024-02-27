package pku.info.global;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

import java.util.concurrent.Executor;
import java.util.concurrent.ThreadPoolExecutor;

@Configuration
public class AsyncThreadPool {

    @Bean(name = "CustomAsyncThreadPool")
    public Executor newAsync() {
        ThreadPoolTaskExecutor taskExecutor = new ThreadPoolTaskExecutor();
        // 核心线程数
        taskExecutor.setCorePoolSize(10);
        // 线程池维护线程的最大数量
        taskExecutor.setMaxPoolSize(20);
        // 缓存队列
        taskExecutor.setQueueCapacity(50);
        // 空闲时间
        taskExecutor.setKeepAliveSeconds(120);
        // 异步方法内部线程名称
        taskExecutor.setThreadNamePrefix("CustomAsyncThread");
        // 拒绝策略
        taskExecutor.setRejectedExecutionHandler(new ThreadPoolExecutor.CallerRunsPolicy());
        taskExecutor.initialize();
        return taskExecutor;
    }
}
