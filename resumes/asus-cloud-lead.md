# 蕭學鴻 Henry Hsiao

**資深後端工程師｜雲端服務・系統可靠性・跨專案交付**

新北市 · [henry255164@gmail.com](mailto:henry255164@gmail.com) · [LinkedIn](https://www.linkedin.com/in/henry255164)

## 專業摘要

具備金融科技與 CRM 跨服務開發、SaaS 轉型、Kubernetes 部署及正式環境 EC2 維運經驗。曾擔任組內 SaaS 轉型主要負責人，建立可恢復的非同步工作流，並獨立交付帳號安全功能。擅長結合應用程式、系統日誌與資料庫分析定位故障，以自動化部署、集中日誌及測試改善服務可靠性。

曾擔任 COSCUP 講者，分享 MySQL 底層優化概念。

## 工作經歷

### ZeroLogix｜資深後端工程師

2023.07－至今

- 入職半年內擔任組內 SaaS 轉型主要負責人，處理 QA 回報；為 3 個後端與 3 個前端專案容器化，整合 Terraform、GitLab CI/CD 與 Kubernetes 部署流程。
- 整合多個服務的代理推薦關係與帳戶流程，建立具狀態、冪等、checkpoint 及失敗恢復的非同步工作流；提供 reconciliation、只讀稽核及可續跑 backfill，支援資料修復與營運排查。
- 整合 Keycloak 服務間認證與權限流程，獨立上線 Session／JWT 強制登出及閒置逾時功能；設定 Cloudflare IP 白名單，透過定期 Terraform job 更新存取規則。
- 維護正式環境多台 EC2 及 NGINX／PHP-FPM／Supervisor 設定與日誌輪替；透過系統日誌定位掛載失敗導致排程無法啟用的原因，並排查 Redis OOM 與服務效能問題。
- 建立 Promtail 採集、Loki 集中儲存與 Grafana 呈現的日誌流程，分析請求耗時、次數與來源 IP，搭配 PHP-FPM／MySQL slow log 定位效能瓶頸；改善 MySQL 慢查詢造成的 I/O wait、CPU 飆升及排程卡頓。

### OwlTing Group 奧丁丁集團｜後端工程師

2023.05－2023.06

- 在一個多月內學習 C#，協助新專案交付上線，並支援 AWS 部署與 RabbitMQ 串接。

### awoo 阿物科技｜後端工程師

2021.02－2023.02

- 開發 Laravel 高流量 API，維護 CodeIgniter 與 Go 排程專案，依需求設計與串接資料庫。
- 維運部分 Kubernetes／VM，使用 GitLab 與 Argo CD 支援 CI/CD，透過監控及日誌解決資料庫效能問題。

### Gamesofa 慧邦科技｜後端工程師

2017.04－2020.05

- 參與平均同時在線人數過萬的手機遊戲開發，負責遊戲內容、多國金流與統計分析，使用 Perl、PHP、Vue.js。
- 進行 MySQL 優化與 Socket／WebSocket 非阻塞開發，兼顧效能及可維護性。

### 晴天蕃茄資訊｜PHP 程式設計師

2015.01－2016.10

- 曾獨立負責政府單位資產管理系統後端，並開發會員系統、金流及外部服務串接。

## 跨專案工程實踐（ZeroLogix）

- 建立並開源一鍵開發環境，整合 8 個 PHP 專案、3 種 PHP 版本、2 個 Java 專案及前端、WebSocket 與資料庫服務；維護白牌服務的環境參數與部署配置。
- 跨 React／TypeScript、PHP 與 Java 17／Spring Boot 完成 API 及介面開發，以 PHPUnit、JUnit、Jest 交付測試，並建立 Playwright 註冊與 KYC 自動化流程；與 AI 協作驗證跨系統登入狀態。

## 核心技能

- **交付與協作**：跨專案整合、QA／SRE 協作、環境建置、AI 輔助驗證、漸進式重構、資料修復與診斷。
- **系統開發**：PHP／Laravel、Java 17／Spring Boot、MySQL、Keycloak、冪等工作流、Queue、RabbitMQ；Go 排程專案維護經驗。
- **雲端與維運**：AWS EC2、Kubernetes、Docker、Terraform、GitLab CI/CD、Cloudflare、NGINX、PHP-FPM、Supervisor、Redis、Promtail／Loki／Grafana。
- **品質驗證**：PHPUnit、JUnit、Jest、Playwright、系統日誌與 slow log 分析。

## 技術分享與開源

- **COSCUP 講者**：於開源人年會進行技術演講，分享 MySQL 底層優化概念。
- **k9s 開源貢獻**：提交 shell 執行問題修正，獲接受並於 v0.50.14 修正。

## 學歷

**國立東華大學｜資訊管理學系學士**，2009－2013。
