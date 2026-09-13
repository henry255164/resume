# 蕭學鴻 Henry Hsiao

**資深後端工程師｜OAuth 整合・JWT 生命週期・雲端部署**

新北市 · [henry255164@gmail.com](mailto:henry255164@gmail.com) · [LinkedIn](https://www.linkedin.com/in/henry255164)

## 專業摘要

具備 Keycloak 服務間 OAuth 串接、client 設定及 API 驗證授權經驗。曾獨立規劃並上線跨 Session／JWT 的憑證撤銷與閒置逾時功能，處理 token refresh、多分頁競爭及跨系統一致性。另具 HMAC 驗證、可恢復工作流、PHP／Java API 開發與 Kubernetes 部署經驗。

## 工作經歷

### ZeroLogix｜資深後端工程師

2023.07－至今

- 實作 Keycloak 服務間 OAuth 串接，使用環境變數提供的 client secret 取得 token，再呼叫目標微服務；接收端透過 Keycloak 驗證並依 scope／role 判斷 API 存取權限。
- 獨立交付並上線強制登出、閒置逾時功能，以 token 版本統一 Session／JWT 撤銷判定，涵蓋帳號停用與密碼變更；處理 JWT refresh 後的失效判定及多分頁活動時間競爭。
- 為內部 reconciliation endpoint 加入 HMAC 驗證，區分 transport、domain 與狀態錯誤；建立冪等、重試、checkpoint 與逾時恢復機制，並提供只讀稽核、dry-run 及可續跑資料修復流程。
- 在 React／TypeScript 實作 iframe origin／source guard 及登出同步，以 Jest 測試訊息來源與登出行為；使用 PHPUnit 覆蓋跨服務競態與失敗情境，並以 Playwright 建立註冊與 KYC 自動化流程。
- 親自設定 Keycloak client、網域及跳轉 URL，配合既有 realm 串接不同 API；負責 Kubernetes 測試環境及白牌配置，為 3 個後端、3 個前端專案容器化，整合 Terraform 與 GitLab CI/CD。

### OwlTing Group 奧丁丁集團｜後端工程師

2023.05－2023.06

- 在一個多月內學習 C#，協助新專案上線，支援 AWS 部署與 RabbitMQ 串接。

### awoo 阿物科技｜後端工程師

2021.02－2023.02

- 開發 Laravel 高流量 API，維護 CodeIgniter 及 Go 資料處理排程，依需求設計與串接資料庫。
- 維運部分 Kubernetes 與 VM 服務，以 GitLab、Argo CD 支援部署，透過監控及日誌排除效能瓶頸。

### Gamesofa 慧邦科技｜後端工程師

2017.04－2020.05

- 使用 Perl、PHP、Vue.js 參與平均同時在線人數過萬的手機遊戲開發，負責多國金流、統計功能與 MySQL 優化。
- 運用 Socket、WebSocket 與非阻塞程式設計開發即時互動功能。

### 晴天蕃茄資訊｜PHP 程式設計師

2015.01－2016.10

- 開發會員系統、金流及外部服務串接，曾獨立負責政府單位資產管理系統後端。

## 核心技能

- **認證與後端**：OAuth、Keycloak、JWT、Session、scope／role 整合、HMAC；PHP／Laravel、Java 17／Spring Boot、Perl、MySQL；Go、C# 專案經驗。
- **品質與一致性**：PHPUnit、JUnit、Jest、Playwright、冪等設計、reconciliation、稽核與失敗恢復。
- **雲端與維運**：Kubernetes、Docker、Terraform、GCP／AWS、GitLab CI/CD、Grafana、Loki、日誌分析。

## 技術分享與開源

- **COSCUP 講者**：於開源人年會進行技術演講，分享 MySQL 底層優化概念。
- **k9s 開源貢獻**：提交 shell 執行問題修正，獲接受並於 v0.50.14 修正。

## 學歷

**國立東華大學｜資訊管理學系學士**，2009－2013。
