package pku.info.activity.service.impl;

import jakarta.annotation.Resource;
import org.springframework.data.redis.core.HashOperations;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Service;
import pku.info.activity.service.CounterService;
import pku.info.common.Conf;
import pku.info.common.Result;

@Service
public class CounterServiceImpl implements CounterService {

    @Resource
    private StringRedisTemplate stringRedisTemplate;

    @Override
    public Result addView(Integer id) {
        HashOperations<String, Object, Object> hashOperation = stringRedisTemplate.opsForHash();
        try{
            hashOperation.increment(Conf.ActivityView, String.valueOf(id), 1);
            return Result.success();
        }catch(Exception e){
            return Result.error(500, "CANNOT INCR VIEW COUNT");
        }
    }
}
