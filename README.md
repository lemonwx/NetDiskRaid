# NetDiskRaid


> just like disk we use usually, let net disk offer you a feature of raid.

磁盘经常通过做 raid 的方法来为应用提供容灾,性能提升等的支持.

网盘是不是也可以这样做:
* 提供备份容灾,数据冗余,比如 raid0 以外的类型
* 提升上传下载的速度,比如 raid0 
    * 一些网盘会限制上传/下载的速度,明明本地有很多空闲带宽,但上传下载文件的速度还是很慢, 这时只要本地带宽不是瓶颈,相比单独上传,肯定是会快一点
* 除 raid1 外,其他 raid 类型本身也提供了加密的功能
* 根据 raid 类型的不同,需要提供至少 2 个 pan.baidu.com 的账号


## 使用方法

手动登录 pan.baidu.com, 获取对应的 cookie, 写入到 config 文件中

## 附加说明:
### 1.针对上传:
以两个账号组成的 raid 为例

要求上行带宽不是瓶颈,比如 pan.baidu.com 限制上传最大速度为 70k/s, 则上行带宽不低于 70 * 2 = 150kb/s
raid5 raid10 raid01 类推

### 2.针对下载
以两个账号组成的 raid 为例

下行带宽不是瓶颈, 比如 pan.baidu.com 限制下载最大速度为 200k/s, 则下行带宽不低于 200 *  2 = 400 k/s

### 3.测试限流
测试机器上行带宽比较低,同时上行带宽也不稳定,为了获得比较好的测试效果,验证可行性,修改了部分源码,限制上传和下载的流量
- ssl.py:894 限制上传流量
- urllib3/response.py:351 限制下载流量

## todolist
- 大文件适配
- raid 支持适配
- 操作 api 支持