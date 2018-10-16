package com.leshuibao.fragmentTax.dao.entity;

import javax.persistence.*;
import java.io.Serializable;
import java.sql.Timestamp;


@Entity
public class SmsLogEntity implements Serializable {

@Column
private String id;
@Column
private String phone;
@Column
private String smsCode;
@Column
private String requestId;
@Column
private String statusCode;
@Column
private String message;
@Column
private String bizid;
@Column
private String memo;
@Column
private String createTime;
@Column
private String changedLasttime;

public SmsLogEntity(){}

public SmsLogEntity(String id,String phone,String smsCode,String requestId,String statusCode,String message,String bizid,String memo,String createTime,String changedLasttime){
this.id = id;
this.phone = phone;
this.smsCode = smsCode;
this.requestId = requestId;
this.statusCode = statusCode;
this.message = message;
this.bizid = bizid;
this.memo = memo;
this.createTime = createTime;
this.changedLasttime = changedLasttime;
}

public String getId() {return id;}

public void setId(String id){this.id = id;}

public String getPhone() {return phone;}

public void setPhone(String phone){this.phone = phone;}

public String getSmsCode() {return smsCode;}

public void setSmsCode(String smsCode){this.smsCode = smsCode;}

public String getRequestId() {return requestId;}

public void setRequestId(String requestId){this.requestId = requestId;}

public String getStatusCode() {return statusCode;}

public void setStatusCode(String statusCode){this.statusCode = statusCode;}

public String getMessage() {return message;}

public void setMessage(String message){this.message = message;}

public String getBizid() {return bizid;}

public void setBizid(String bizid){this.bizid = bizid;}

public String getMemo() {return memo;}

public void setMemo(String memo){this.memo = memo;}

public String getCreateTime() {return createTime;}

public void setCreateTime(String createTime){this.createTime = createTime;}

public String getChangedLasttime() {return changedLasttime;}

public void setChangedLasttime(String changedLasttime){this.changedLasttime = changedLasttime;}

}