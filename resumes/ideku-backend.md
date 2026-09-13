# 蕭學鴻 Henry Hsiao

**資深後端工程師｜API 開發・資料庫效能・系統整合**

新北市 · [henry255164@gmail.com](mailto:henry255164@gmail.com) · [LinkedIn](https://www.linkedin.com/in/henry255164)

## 專業摘要

具備金融科技、CRM、高流量 API 與 SaaS 系統經驗，主要使用 PHP／Laravel、Perl，亦有 Java 17／Spring Boot、Go 與 C# 專案經驗。擅長支付整合、MySQL 調校及既有系統重構，以冪等工作流與 Unit／Feature／E2E 測試處理跨服務一致性與失敗情境。

曾擔任 COSCUP 講者，分享 MySQL 底層優化概念。

## 工作經歷

### ZeroLogix｜資深後端工程師

2023.07－至今

- 開發 GateToPay API，維護 Binance 入金核對與 Worldpay 退款資料流程；於 Java 17／Spring Boot 帳戶管理服務實作交易識別碼 API，串接 controller、domain port、JPA repository 及 service test。
- 將跨服務代理推薦關係改為可恢復的非同步工作流，加入狀態管理、lease、checkpoint、冪等約束與 reconciliation；以單元測試覆蓋競態、部分成功及失敗恢復。
- 重構 CRM 查詢為先按 ID 分頁再載入資料，以批次查詢消除 N+1 query，加入 request-level cache；改善 MySQL 慢查詢造成的 I/O wait、CPU 飆升及排程卡頓。
- 獨立規劃並上線 Session／JWT 強制登出及閒置逾時功能，處理多分頁競爭與 token refresh；以 Jest 測試 iframe 訊息來源及登出行為，並使用 Playwright 建立註冊與個人／企業 KYC 自動化流程。
- 入職半年內擔任組內 SaaS 轉型主要負責人，處理 QA 回報；為 3 個後端、3 個前端專案容器化，整合 Terraform、GitLab CI/CD 與 Kubernetes，並支援 Keycloak 及白牌服務配置。

### OwlTing Group 奧丁丁集團｜後端工程師

2023.05－2023.06

- 在一個多月內學習 C#，協助新專案開發至上線，並支援 AWS 部署與 RabbitMQ 串接。

### awoo 阿物科技｜後端工程師

2021.02－2023.02

- 使用 Laravel 開發客戶串接的高流量 API，維護 CodeIgniter 舊系統與 Go 資料處理排程。
- 依需求設計與串接資料庫，透過監控、日誌分析進行效能調校；使用 Docker Compose、Kubernetes、GitLab 與 Argo CD 支援開發部署。

### Gamesofa 慧邦科技｜後端工程師

2017.04－2020.05

- 參與平均同時在線人數過萬的手機遊戲開發，使用 Perl、PHP、Vue.js；開發遊戲內容、多國金流及統計分析功能。
- 優化 MySQL 查詢與資料表設計，運用 Socket、WebSocket 與非阻塞程式設計處理即時互動。

### 晴天蕃茄資訊｜PHP 程式設計師

2015.01－2016.10

- 開發會員系統、金流及外部服務串接，曾獨立負責政府單位資產管理系統後端。

## 核心技能

- **開發與資料**：PHP、Laravel、Java 17／Spring Boot、Perl、MySQL、Redis、Elasticsearch、Service／Repository pattern、DTO；Go、C# 專案經驗。
- **品質與重構**：PHPUnit、JUnit、Jest、Playwright、Unit／Feature／E2E test、冪等設計、批次處理、既有流程重構。
- **整合與部署**：金流、RabbitMQ、OAuth／Keycloak、Docker、Kubernetes、Terraform、GCP／AWS、GitLab CI/CD。

## 技術分享與開源

- **COSCUP 講者**：於開源人年會進行技術演講，分享 MySQL 底層優化概念。
- **k9s 開源貢獻**：提交 shell 執行問題修正，獲接受並於 v0.50.14 修正。

## 學歷

**國立東華大學｜資訊管理學系學士**，2009－2013。
