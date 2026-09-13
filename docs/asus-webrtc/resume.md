# 蕭學鴻 Henry Hsiao

**資深後端工程師｜即時通訊・非阻塞開發・系統可觀測性**

新北市 · [henry255164@gmail.com](mailto:henry255164@gmail.com) · [LinkedIn](https://www.linkedin.com/in/henry255164)

## 專業摘要

具備高流量手機遊戲、Socket／WebSocket 與非阻塞程式設計經驗，擅長跨服務狀態管理、失敗恢復及系統除錯。具備 Go 專案維護、Java 17／Spring Boot API 開發、Kubernetes 維運與語音對話 POC 研究經驗，期望將既有即時互動與後端能力延伸至 WebRTC 雲端服務。

## 工作經歷

### ZeroLogix｜資深後端工程師

2023.07－至今

- 主動改善 Kubernetes Pod 日誌保存，架設 Promtail 串接 Loki／Grafana，針對多日誌檔配置採集路徑及欄位解析，支援告警設定與問題排查。
- 將跨服務長時間操作改為非同步工作流，加入 worker ownership、lease、checkpoint、重試與逾時恢復，以單元測試覆蓋競態、部分成功及過期操作。
- 整合 MT4／MT5 帳戶建立與重試流程，將交易伺服器設定改由管理 API 提供並加入 Redis cache；補強遠端回應、authentication 與錯誤邊界，支援狀態診斷及只讀稽核。
- 獨立交付跨 Session／JWT 的強制登出及閒置逾時功能，處理多分頁競爭與 iframe 同步；在 React／TypeScript 加入 origin／source guard 並以 Jest 驗證，另修正快速換頁造成的心跳中斷及誤登出。
- 為 3 個後端、3 個前端專案容器化，整合 Terraform 與 GitLab CI/CD 部署至 Kubernetes；一鍵開發環境涵蓋多版本 PHP、Java、前端及 WebSocket 服務。

### OwlTing Group 奧丁丁集團｜後端工程師

2023.05－2023.06

- 在一個多月內學習 C#，協助新專案開發至上線，並支援 AWS 部署與 RabbitMQ 串接。

### awoo 阿物科技｜後端工程師

2021.02－2023.02

- 維護 Go 資料處理排程，開發 Laravel 高流量 API，維護 CodeIgniter 舊系統。
- 透過監控與日誌調校資料庫效能，維運部分 Kubernetes／VM 環境，使用 GitLab 與 Argo CD 支援部署。

### Gamesofa 慧邦科技｜後端工程師

2017.04－2020.05

- 參與平均同時在線人數過萬的手機遊戲產品，使用 Perl Socket、PHP 與 Vue.js 開發即時互動功能。
- 運用 WebSocket 與非阻塞程式設計，進行 MySQL 查詢優化及資料表正規化，兼顧效能與可讀性。
- 開發遊戲內容、多國金流、圖表與統計分析功能。

### 晴天蕃茄資訊｜PHP 程式設計師

2015.01－2016.10

- 開發會員、金流、地圖及語音串接功能，曾獨立負責政府單位資產管理系統後端。

## 技術分享、研究與開源

- **COSCUP 講者**：於開源人年會進行技術演講，分享 MySQL 底層優化概念。
- **Shuo 語音對話 POC**：以小型概念驗證研究語音對話系統，作為延伸即時通訊領域的探索；屬研究經驗。
- **k9s**：研究並提交 shell 執行問題修正，獲接受並於 v0.50.14 修正。

## 核心技能

- **通訊與後端**：Socket、WebSocket、非阻塞程式設計、非同步工作流、PHP、Perl、Java 17／Spring Boot、MySQL；Go、C# 專案經驗。
- **系統維運**：Linux、Kubernetes、Docker、Terraform、RabbitMQ、Grafana、Loki、Promtail。
- **品質與整合**：PHPUnit、JUnit、Jest、Playwright、重試與失敗恢復、Redis、跨服務 API。

## 學歷

**國立東華大學｜資訊管理學系學士**，2009－2013。
