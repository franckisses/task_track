# task_track
task track

该项目主要用于提交任务，并且跟踪任务的状态

Task model 设计

任务表设计
```
id 任务id 
creator 创建人 
project_name 项目名称
task_name 任务名称
design_doc 设计文档
priority 优先级
created_time 创建时间
backend_handler     前端处理人
frontend_handler    后端处理人
backend_finished_rate 前端完成度
frontend_finished_rate 前端完成度
finished_rate 完成度
deadline 最后期限
```

任务详情表设计
```
task_id:  任务id onetomany
prove_pic: 完成图片
result_data: 完成数据
created_time 创建时间
```


到底是把这些表分开好呢还是合在一起呢？！！
