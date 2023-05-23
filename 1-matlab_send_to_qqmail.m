setpref('Internet','E_mail','My_Mail');
setpref('Internet','SMTP_Server','smtp.qq.com');%My_Mail是邮箱地址
props = java.lang.System.getProperties;
props.setProperty('mail.smtp.auth','true');
setpref('Internet','SMTP_Username','My_Mail');
setpref('Internet','SMTP_Password','My_Password');%My_Password是授权码
sendmail('My_Mail', '标题', '信息')