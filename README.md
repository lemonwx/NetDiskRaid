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

## todolist
- 大文件适配
- raid 支持适配
- 操作 api 支持