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
TODO list

|TODO|Status|
|-|-|
|1.登录之后，在添加任务中，显示登录信息|✓|
|2.添加任务中，增加删除功能|✓|
|3.添加任务中,输入框改大一些|✓|
|4.添加任务中,完成后端|✓|
|5.研究一下github CI/CD||
|6.每个页面添加返回主页|✓|
|7.如何通过json格式将文件和字符传到后端||
|8.添加页面通过点击，返回主页|✓|
|9.根据不同用户角色返回列表|✓|
|10.完成前端展示所有任务|✓|
|11.完成切换不同维度展示|✓|
|12.点击展示相关details||
|13.点击ongong 显示相关信息|✓|
|14.点击finished显示相关信息|✓|
|15.点击相关表头进行排序||

tips:
1. 
FloatField vs. DecimalField
The FloatField class is sometimes mixed up with the DecimalField class. Although they both represent real numbers, they represent those numbers differently. FloatField uses Python’s float type internally, while DecimalField uses Python’s Decimal type. For information on the difference between the two, see Python’s documentation for the decimal module.
在Django中选择小数的类型时，还是建议选择使用DecimalField。
