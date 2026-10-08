# OctoSense Google Calendar

[English](README.md) | 简体中文

这是 **macOS 开发预览版**，用于查看有限范围的 Google 日程、保留草稿、在宿主中审阅修改，并与只读助手讨论所选日程。
发布者为 [ymote](https://github.com/ymote)，新应用 ID 为 `io.github.ymote.googlecalendar`，
可编辑源码版本为 **0.2.1**。这是独立示例，不是 Google 官方产品。

新版本通过 GitHub 发布证明确认发布者身份，无需开发者签名私钥或仓库签名机密。
它与旧应用 `org.octosense.samples.googlecalendar` 分别安装，账户授权和本地数据不会自动迁移。
旧 `v0.1.0`／`v0.1.1` 标签、签名和验收记录不变；`publisher.json` 仅描述历史身份。

## 安装与连接

新版本需要 **应用契约 1.8.0／`publisher-github-v1`** 及兼容的 OctoSense
连接服务主机。旧 desktop beta.2 无法安装 GitHub 证明发行包。创建标签不等于
App Hub 收录；先查看提交 issue 的目录／发行状态。已收录且主机兼容时，使用
**App Hub → Search → Google Calendar → Get → Install → Open**，审阅请求的权限。

Google 登录由宿主浏览器／提供方流程完成，应用不收集密码。宿主维护者配置
OAuth 客户端和对应 API，普通用户无需注册开发者客户端，也无需另建 OctoSense
账户。参见[宿主 OAuth 指南](https://github.com/OctoSense-org/OctoSense/blob/main/crates/oauth-service/README.md)。
应用仅获得绑定应用与账户的不透明句柄，不接收凭据。

**发布流程测试不验证真实 Google 登录、读取／写入或物理确认。** Android Google
授权仍不可用，本版本不宣称支持 Android、Linux 或 Windows。独立 `card-host`
只能验证本地界面和明确的服务不可用状态。

## 使用

1. **Account → Connect Google** 完成授权后选择日历。**Refresh** 读取刷新时刻
   之前 30 天／之后 366 天；失败时保留上次完整缓存。旧数据缺少范围元信息时明确
   显示不可用。范围内未显示的事件不一定已从 Google 删除。
2. **+ Event** 或 **Edit** 打开本地编辑器，填写起止日期／时间及 IANA 时区。
   **Keep draft** 保留未发送修改，不写入 Google；**Review & Save** 使用宿主的
   完整内容审阅界面。
3. **Glance** 展示所选日程 24 小时且不通知；**Open Calendar** 通过新应用 ID
   返回同一日程。
4. **Chat** 经同意后将所选日程发送到已配置模型。助手只有四个私有读取工具，
   不能预订、新建或修改日程；建议须在编辑器中应用并审阅。

本版本不展开／编辑重复实例、不发送邀请；Glance 和完整应用的聊天历史共享未验证。

## 发布和本地检查

可编辑 `bundle/` 不含发行证明。[GitHub 工作流](.github/workflows/publish-app.yml)
固定已审阅的 Hub 工具版本。完成源码测试和审阅后推送全新 `v<manifest.version>`
标签，GitHub 准备、证明、验证并上传 `app.bundle.pack.json`。不要把已封存包覆盖
回开发源码，不要移动已有标签。

```sh
python3 -m unittest discover -s tests -v
"$HUB" stamp bundle
"$HUB" check bundle --allow-unsigned
mkdir -p build
"$HUB" scan bundle --packet build/review.json
```

通过 [App Hub issue](https://github.com/OctoSense-org/OctoSense-App-Hub/issues) 请求
发布，提供 ID、源码、权限、截图和审核答案。issue 可先于标签创建；完成后补充
成功工作流、确切提交和包哈希。管理员审阅和目录发布与创建发行版是不同步骤。
下载包使用 `hub publisher-unpack`／`hub publisher-verify` 验证，不重新 stamp
或移除证明。

## 证据边界

本版本保留当前功能代码，使用新身份及发布流程。`review/`、已有 `evidence/`
和旧标签中的记录保留原始源码／二进制身份，不能当作 0.2.0 的新验收。发行前只用
新实际原生截图替换列表图，并逐张审视。

历史 Mac 测试使用模拟服务，包括 36 轮交互及 DeepSeek 对虚构事件的建议。
[ACCEPTANCE](ACCEPTANCE.md) 保留确切身份和限制；不能由此推断真实 Google、
物理确认或新包摘要已验证。

连接账户或启用 AI 前请阅读[隐私说明](PRIVACY.zh-CN.md)。
[公开支持](https://github.com/ymote/octosense-google-calendar/issues) 中不要提交私人邮件／事件、凭据
或原始日志。采用 [Apache-2.0](LICENSE)。

当前源码检查：[0.2.1 准备记录](review/releases/0.2.1/PREPARATION.json)、[准入输出](review/releases/0.2.1/GATE.txt)、[八项审核答案](review/ANSWERS.md)。界面未变；[0.2.0 离线记录](review/releases/0.2.0/NATIVE.json)和[真实发行包安装记录](review/releases/0.2.0/PUBLISHING.json)保留确切受测版本。0.2.1 修正发布工作流对目录准入的表述；真实更新验收在发行后另行记录。
