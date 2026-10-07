# OctoSense Google Calendar 应用

[English](README.md) | 简体中文

这是一个 **macOS 开发预览版**：查看 Google 日历、保留日程草稿、审阅修改，
并通过你配置的 AI 助手讨论日程。发布者为 **ymote**；应用 ID 为
`org.octosense.samples.googlecalendar`，版本为 `0.1.0`。
这是独立示例应用，不是 Google 官方产品。

应用依赖 [OctoSense #347](https://github.com/OctoSense-org/OctoSense/pull/347)
的共享服务和 [App Hub #119](https://github.com/OctoSense-org/OctoSense-App-Hub/pull/119)
的准入及工具映射能力。提交审核不代表已进入应用目录，也不代表普通发行版已支持。
**本示例尚未验证真实 Google 登录、读取、写入及人工物理确认。**
Android Google 授权适配尚未实现；本次不宣称支持 Android、Linux 或 Windows。

## 使用方法

签名包通过审核后，在兼容的 macOS OctoSense 中经 App Hub 安装。
宿主维护者须在仓库外配置 Google OAuth 客户端；凭据只在宿主或 Google 授权界面输入。

1. 进入 **Account → Connect Google**，授权后选择日历。
2. 点击 **Refresh** 同步；同步失败时仍保留上次完整的缓存日程。
3. 使用 **+ Event** 新建，或在日程中点击 **Edit**。填写起止日期、时间和明确的
   IANA 时区；**Keep draft** 将未完成内容保存在本机。
4. **Review & Save** 打开宿主审阅界面。核对账号、日历、时间和内容后才批准。
   遇到版本冲突会保留草稿，须根据最新日程重新审阅，不能强行覆盖。
5. **Glance** 将所选日程展示 24 小时，不发送通知；卡片内的 **Open Calendar**
   返回本应用中的同一日程。
6. **Chat** 在宿主授权后，把所选日程上下文及问题发送给你配置的模型。
   助手只有四个私有只读工具，**不能预订、新建或修改日程**；建议须在编辑器中应用。

重复日程只显示原始开始时间；本版本不展开重复实例、不编辑重复规则，也不发送邀请。
尚未验证 Glance 卡片聊天与完整应用聊天是否共享历史。

## 验证和开发

可执行源码、代理指令、工具声明和原始截图来自[固定版本的 App Design Flow 示例](https://github.com/OctoSense-org/OctoScript-App-Design-Flow/tree/5b0fde7ed0e9e4131751d16f55ba3d8a3180dd95/examples/connected-apps/google-calendar)，字节保持不变。
历史 macOS 验证包括八项签名安装/模拟服务流程、六项 Glance 路由流程、真实 DeepSeek
对模拟日程的建议，以及 36 轮、620 秒的原生交互测试。这些使用**模拟日历服务**，
不能视为真实 Google 验证。原始证据在 [evidence/](evidence/)，来源与限制见
[ACCEPTANCE.md](ACCEPTANCE.md)。

验证签名发行版时，将兼容的 App Hub 工具加入 `PATH`，在本仓库运行
（Python 只读取公开的发布者公钥）：

```sh
CALENDAR_PUBLISHER_KEY="$(python3 -c 'import json; print(json.load(open("publisher.json"))["public_key"])')"
hub check bundle --publisher-key "ymote=$CALENDAR_PUBLISHER_KEY"
mkdir -p build
hub scan bundle --publisher-key "ymote=$CALENDAR_PUBLISHER_KEY" --packet build/review.json
```

验证前不要重新 stamp 或修改发行包。开发时请使用单独的可编辑副本，并按
[Hub 发布流程](https://github.com/OctoSense-org/OctoSense-App-Hub/blob/main/docs/PUBLISHING.md)
对修改后的内容重新 stamp、检查未签名副本，再用自己的发布者密钥签名及验证。
`--allow-unsigned` 仅接受确实未签名的本地包，不会信任未知签名，也不能绕过安装验证。
只提交 `bundle/`。
[审核答案](review/ANSWERS.md)涵盖扫描器全部八个问题。
依赖完整运行时的复现命令保留在[原始验收文档](https://github.com/OctoSense-org/OctoScript-App-Design-Flow/blob/5b0fde7ed0e9e4131751d16f55ba3d8a3180dd95/examples/connected-apps/google-calendar/ACCEPTANCE.md)。

连接账号或使用 AI 前请阅读[隐私说明](PRIVACY.zh-CN.md)。通过
[GitHub issues](https://github.com/ymote/octosense-google-calendar/issues)反馈问题时，
不要提交账号资料、令牌或私人日程。采用 [Apache-2.0](LICENSE)；署名见 [NOTICE](NOTICE)。
