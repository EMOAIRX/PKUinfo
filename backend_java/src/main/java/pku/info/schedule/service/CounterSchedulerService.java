package pku.info.schedule.service;

import com.baomidou.mybatisplus.core.conditions.update.UpdateWrapper;
import jakarta.annotation.Resource;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.dao.DataAccessException;
import org.springframework.data.redis.core.RedisOperations;
import org.springframework.data.redis.core.SessionCallback;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;
import pku.info.activity.entity.Activity;
import pku.info.activity.mapper.ActivityMapper;
import pku.info.common.Conf;

import java.util.List;
import java.util.Map;
import java.util.Set;

@Component
public class CounterSchedulerService {
    @Resource
    private StringRedisTemplate stringRedisTemplate;

    @Resource
    private ActivityMapper activityMapper;

    @Transactional(rollbackFor = {Exception.class})
    @CacheEvict(value = "activity", allEntries = true)
    public void saveViewData() {
        updateActivityData(Conf.ActivityView,"view = view + ");
    }

    public void updateActivityData(String field, String setSQL) {
        // 取缓存数据
        Map<Object, Object> map = stringRedisTemplate.opsForHash().entries(field);
        // 活动id
        Set<Object> keys = map.keySet();
        for (Object key : keys) {
            int id = Integer.parseInt(key.toString());
            int delta = Integer.parseInt(map.get(key).toString());

            if(delta == 0){
                continue;
            }
            // 生成浏览数据
            UpdateWrapper<Activity> activityUpdateWrapper = new UpdateWrapper<>();
            activityUpdateWrapper.eq("id", id);
            activityUpdateWrapper.setSql(setSQL + delta);
            activityMapper.update(activityUpdateWrapper);
        }

        List<Object> txResults = stringRedisTemplate.execute(new SessionCallback<List<Object>>() {
            public List<Object> execute(RedisOperations operations) throws DataAccessException {
                operations.multi();
                for (Object key : keys) {
                    // 清除Redis字段
                    System.out.println("Clear Data" + field + key);
                    stringRedisTemplate.opsForHash().delete(field, key);
                }
                return operations.exec();
            }
        });

        // 更新成功后修改redis浏览量缓存
        //HashOperations<String, Object, Object> hashOperation = stringRedisTemplate.opsForHash();
        //for (Object key : keys){
        //    int delta = Integer.parseInt(map.get(key).toString());
        //    if(delta == 0){
        //        continue;
        //    }
        //    hashOperation.increment(field, key, -1 * delta);
        //}
    }
}
