package com.leshuibao.fragmentTax.dao.mapper;

import com.leshuibao.fragmentTax.dao.entity.SmsLogEntity;
import org.apache.ibatis.annotations.*;
import java.util.List;


@Mapper
public interface ISmsLogMapper {
@Select("SELECT `id`, `phone`, `sms_code`, `request_id`, `status_code`, `message`, `bizid`, `memo`, `create_time`, `changed_lasttime` FROM `sms_log`")
@Results({
@Result(property = "id", column = "id"), 
@Result(property = "phone", column = "phone"), 
@Result(property = "smsCode", column = "sms_code"), 
@Result(property = "requestId", column = "request_id"), 
@Result(property = "statusCode", column = "status_code"), 
@Result(property = "message", column = "message"), 
@Result(property = "bizid", column = "bizid"), 
@Result(property = "memo", column = "memo"), 
@Result(property = "createTime", column = "create_time"), 
@Result(property = "changedLasttime", column = "changed_lasttime")
})
List<SmsLogEntity> queryAll();
@Select("SELECT `id`, `phone`, `sms_code`, `request_id`, `status_code`, `message`, `bizid`, `memo`, `create_time`, `changed_lasttime` FROM `sms_log` WHERE `id` = #{id}")
@Results({
@Result(property = "id", column = "id"), 
@Result(property = "phone", column = "phone"), 
@Result(property = "smsCode", column = "sms_code"), 
@Result(property = "requestId", column = "request_id"), 
@Result(property = "statusCode", column = "status_code"), 
@Result(property = "message", column = "message"), 
@Result(property = "bizid", column = "bizid"), 
@Result(property = "memo", column = "memo"), 
@Result(property = "createTime", column = "create_time"), 
@Result(property = "changedLasttime", column = "changed_lasttime")
})
SmsLogEntity queryByKey(@Param("id") String id);

@Insert("INSERT INTO `sms_log`(`id`, `phone`, `sms_code`, `request_id`, `status_code`, `message`, `bizid`, `memo`, `create_time`, `changed_lasttime`) VALUES(#{id}, #{phone}, #{smsCode}, #{requestId}, #{statusCode}, #{message}, #{bizid}, #{memo}, #{createTime}, #{changedLasttime})")
void insert(SmsLogEntity sms_logEntity);

@Update("UPDATE `sms_log` SET id=#{id}, phone=#{phone}, sms_code=#{smsCode}, request_id=#{requestId}, status_code=#{statusCode}, message=#{message}, bizid=#{bizid}, memo=#{memo}, create_time=#{createTime}, changed_lasttime=#{changedLasttime} WHERE `id` = #{id}")
void update(SmsLogEntity sms_logEntity);

@Delete("DELETE FROM `sms_log` WHERE `id` = #{id}")
void delete(@Param("id") String id);

}