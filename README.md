# Israeli AI Ecosystem

![Banner](images/banner.png)

A curated map of the Israeli AI ecosystem: AI agents, agent skills, MCP servers, Hebrew language resources, communities, meetups, government bodies, conferences, and domain-specific tools — covering finance, healthcare, government data, real estate, safety, and more.

Projects are presented as compact tables; ecosystem and community sections use grouped lists. See [SCOPE.md](SCOPE.md) for inclusion criteria and [pending.md](pending.md) for planned sections awaiting entries.

> **Note:** This repo is **not** intended to be a collection of every AI company in Israel — that would be an impossible task, and not particularly useful. Rather, it's a thoughtful organisation of links outlining useful directions for those professionally involved in AI in Israel to find community, organisations, and practical tools.

*Last updated: 2026-04-09*

## Contents

<table>
<tr>
<td valign="top" width="25%">

### 🤖 Projects

- [AI Agents](#ai-agents)
- [Agent Skills](#agent-skills)
- [Skills & Frameworks](#agent-skills--frameworks)
- [Curated Lists](#curated-lists)

</td>
<td valign="top" width="25%">

### 🌐 Ecosystem

- [Communities](#communities--organizations)
- [Government Bodies](#government-bodies)
- [Centers of Excellence](#centers-of-excellence)
- [Conferences](#conferences--events)
- [Inference Providers](#inference-providers--local-clouds)
- [Startups](#startup-ecosystem)

</td>
<td valign="top" width="25%">

### 🇮🇱 Hebrew & Language

- [Overview](#hebrew-language-resources)
- [Hebrew AI Models](https://github.com/danielrosehill/Hebrew-AI-Models)
- [Hebrew Language Projects Index](https://github.com/danielrosehill/Hebrew-Language-Projects-Index)
- [Hebrew TTS Providers](https://github.com/danielrosehill/Hebrew-TTS-Providers)
- [English ↔ Hebrew Translation](https://github.com/danielrosehill/English-Hebrew-Translation)
- [Hebrew Calendar Resources](https://github.com/danielrosehill/Hebrew-Calendar-Resources)
- [Hebrew Image Generation Eval](https://github.com/danielrosehill/Hebrew-Image-Generation-Eval)

</td>
<td valign="top" width="25%">

### 🧰 By Domain

- [Finance & Banking](#finance--banking)
- [Government Data](#government--open-data)
- [Government Services](#government-services)
- [Healthcare](#healthcare--medical)
- [Legal](#legal)
- [Insurance](#insurance)
- [Real Estate](#real-estate--land)
- [Safety & Emergency](#safety--emergency)
- [Shopping & Retail](#shopping--retail)
- [Transportation](#transportation)
- [Weather](#weather--environment)
- [Economics & Statistics](#economics--statistics)
- [Library & Archives](#library--archives)
- [Careers & Jobs](#careers--jobs)
- [Dashboards](#dashboards) · [Plugins](#plugins) · [Voice](#voice-agents)

</td>
</tr>
</table>

# AI Agents

Autonomous AI agents built for Israeli use cases.

| Project | Description | Stars |
|---|---|---|
| [Claudi](https://github.com/itaisabi-collab/claudi) | ClaudioSabi — Israeli AI agent on Moltbook | ![](https://img.shields.io/github/stars/itaisabi-collab/claudi?style=social) |
| [Nachla Agent](https://github.com/Ofir-Metis/nachla-agent) | AI agent for בדיקת התכנות נחלות — feasibility studies for Israeli agricultural settlements | ![](https://img.shields.io/github/stars/Ofir-Metis/nachla-agent?style=social) |
| [News Agent](https://github.com/eyalban/News-Agent) | Daily Hebrew security briefing agent for the Iran-Israel conflict, automated via GitHub Actions | ![](https://img.shields.io/github/stars/eyalban/News-Agent?style=social) |
| [OlehAssist Agent](https://github.com/abernatkunin/OlehAssistAgent) | Chatbot to assist new Israeli immigrants (olim) with bureaucratic issues after making Aliyah | ![](https://img.shields.io/github/stars/abernatkunin/OlehAssistAgent?style=social) |


# Agent Skills

Individual AI agent skills for Israeli services and data.

| Skill | Description | Stars |
|---|---|---|
| [Clalit Pharmacy Search](https://github.com/tomron/agent-skill-clalit-pharm-search) | Search medications and check real-time stock at Clalit (כללית) pharmacies | ![](https://img.shields.io/github/stars/tomron/agent-skill-clalit-pharm-search?style=social) |
| [Morning Skill](https://github.com/D1DX/morning-skill) | Morning (Green Invoice) expense management, S3 upload, classifications, search | ![](https://img.shields.io/github/stars/D1DX/morning-skill?style=social) |
| [Nadlan Skill](https://github.com/IsraelZablianov/nadlan-skill) | Israeli real estate market analysis | ![](https://img.shields.io/github/stars/IsraelZablianov/nadlan-skill?style=social) |
| [OnTopo Skill](https://github.com/alexpolonsky/agent-skill-ontopo) | Search Israeli restaurants, check availability, get booking links (OnTopo/Tabit) | ![](https://img.shields.io/github/stars/alexpolonsky/agent-skill-ontopo?style=social) |
| [JLM Coffee](https://github.com/alexpolonsky/agent-skill-jlm-coffee) | Discover coffee shops in Jerusalem | ![](https://img.shields.io/github/stars/alexpolonsky/agent-skill-jlm-coffee?style=social) |
| [Israeli Corporate Law](https://github.com/avivshafir/israeli-corporate-law-skill) | Agent skill for Israeli corporate law | ![](https://img.shields.io/github/stars/avivshafir/israeli-corporate-law-skill?style=social) |
| [iCount Skill](https://github.com/Tura2/icount-skill) | iCount — Israeli invoicing and accounting platform | ![](https://img.shields.io/github/stars/Tura2/icount-skill?style=social) |
| [Rail IL Skill](https://github.com/lirantal/skill-railil) | Agent skill for the Israel Railways API | ![](https://img.shields.io/github/stars/lirantal/skill-railil?style=social) |
| [Seret Skill](https://github.com/omernesh/seret-skill) | Israeli movie showtimes, ratings, cinema info from seret.co.il | ![](https://img.shields.io/github/stars/omernesh/seret-skill?style=social) |


# Agent Skills & Frameworks

Organizations and projects providing collections of Israel-focused AI agent skills and MCP servers

## [Skills IL](https://github.com/skills-il)

![Skills](https://img.shields.io/badge/skills-127-blue) ![Categories](https://img.shields.io/badge/categories-12-green) ![Website](https://img.shields.io/badge/website-agentskills.co.il-orange)

Curated AI agent skills for Israeli developers — an open-source collection of [Agent Skills](https://docs.anthropic.com/en/docs/build-with-claude/skills) built for Israeli-specific needs (tax compliance, Hebrew localization, government APIs, and more). Each skill follows the open Agent Skills standard and works across Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex, and other AI coding agents.

| Category | Skills | Description | Repo |
|----------|--------|-------------|------|
| Tax & Finance | 19 | Invoices, income tax, VAT, payments, stock analysis, startup finance | [tax-and-finance](https://github.com/skills-il/tax-and-finance) |
| Government Services | 18 | Population Authority, National Insurance, Knesset, gov APIs | [government-services](https://github.com/skills-il/government-services) |
| Localization | 17 | Hebrew RTL, i18n, accessibility, document generation, design systems | [localization](https://github.com/skills-il/localization) |
| Developer Tools | 15 | ID validation, date conversion, Israeli dev utilities | [developer-tools](https://github.com/skills-il/developer-tools) |
| Accounting | 14 | Bookkeeping, bank reconciliation, expense management, financial reporting | [accounting](https://github.com/skills-il/accounting) |
| Marketing & Growth | 9 | Hebrew SEO, product launch, LinkedIn strategy, content marketing | [marketing-growth](https://github.com/skills-il/marketing-growth) |
| Communication | 8 | SMS, email, WhatsApp automation, Monday.com workflows | [communication](https://github.com/skills-il/communication) |
| Health Services | 7 | HMO navigation, patient rights, health insurance, telemedicine | [health-services](https://github.com/skills-il/health-services) |
| Security & Compliance | 7 | Privacy law, cyber regulations, e-commerce compliance | [security-compliance](https://github.com/skills-il/security-compliance) |
| Food & Dining | 6 | Kashrut, supermarket prices, restaurant operations, food compliance | [food-and-dining](https://github.com/skills-il/food-and-dining) |
| Education | 4 | Bagrut exams, academia, online learning | [education](https://github.com/skills-il/education) |
| Legal Tech | 3 | Employment contracts, labor law, regulatory compliance | [legal-tech](https://github.com/skills-il/legal-tech) |

**Website:** [agentskills.co.il](https://agentskills.co.il) · **Built by:** [YooTech](https://yootech.io/) · **CLI:** `npx skills` via [skills-il-cli](https://github.com/skills-il/skills-il-cli)

**Author:** [skills-il](https://github.com/skills-il)

---

# Curated Lists

Community-maintained collections of Israeli AI agent resources.

**External ecosystem maps:**

- [The Israeli Agentic AI Landscape (Twine Security)](https://www.twinesecurity.com/resource/the-israeli-agentic-ai-landscape) — Market map of Israeli companies building in the agentic AI space.

| Project | Description | Stars |
|---|---|---|
| [Claude Israel](https://github.com/danielrosehill/Claude-Israel) | Index of Claude / Claude Code projects with an Israel focus. | ![](https://img.shields.io/github/stars/danielrosehill/Claude-Israel?style=social) |
| [Awesome Open Source Israel](https://github.com/lirantal/awesome-opensource-israel) | Awesome list of open source projects created by Israeli developers — broader than AI, but includes many AI-adjacent projects. | ![](https://img.shields.io/github/stars/lirantal/awesome-opensource-israel?style=social) |
| [Awesome Agent Skills Israel](https://github.com/alexpolonsky/awesome-agent-skills-israel) | A curated list of Agent Skills for navigating life in Israel | ![](https://img.shields.io/github/stars/alexpolonsky/awesome-agent-skills-israel?style=social) |
| [Useful AI Agent Skills — Israel-Specific](https://github.com/danielrosehill/Useful-AI-Agent-Skills#13-israel-specific) | A broader catalogue of useful AI agent skills with a dedicated Israel-specific section. | ![](https://img.shields.io/github/stars/danielrosehill/Useful-AI-Agent-Skills?style=social) |


# Communities & Organizations

Israeli AI communities, professional associations, and organizations supporting the local AI ecosystem.

- [AI Israel (aiisrael.org.il)](https://aiisrael.org.il/) — Israeli AI community organization.
- [The Institute AI (theinstituteai.org.il)](https://www.theinstituteai.org.il/en/) — Israeli institute for AI research and policy.
- [Agent Skills IL (agentskills.co.il)](https://agentskills.co.il/en) — Companion website to the Skills IL open-source project.
- [Machine Learning Israel (machinelearning.co.il)](https://machinelearning.co.il/) — Israeli machine learning community.
- [Israeli Association for Artificial Intelligence (iaai.org.il)](https://iaai.org.il/) — Professional association for AI practitioners and researchers in Israel.
- [Ivrit.ai](https://www.ivrit.ai/en/ivrit-ai-2/) — Open Hebrew speech and language datasets for AI research.
- [Dicta / DictaLM](https://dicta.org.il/dicta-lm) — Hebrew NLP research center and open-source Hebrew LLMs.
- [Data-IL](https://data-il.org/en/) — Israeli data science and AI community.

## Meetups

In-person and hybrid AI/ML meetup groups across Israel.

- [Artificial Intelligence Israel](https://www.meetup.com/artificial-intelligence-israel/) — General AI meetup group in Israel.
- [Generative AI Israel](https://www.meetup.com/generative-ai-israel/) — Meetup focused on generative AI.
- [Tel Aviv-Yafo Agentic AI Meetup Group](https://www.meetup.com/tel-aviv-yafo-agentic-ai-meetup-group/) — Tel Aviv meetup on agentic AI.
- [DataTalks JLM — Machine & Deep Learning in the Holy City](https://www.meetup.com/datatalks-jlm-machine-and-deep-learning-in-the-holy-city/) — Jerusalem-based ML/DL meetup. ([LinkedIn](https://il.linkedin.com/company/datatalks-jlm))
- [Prompt Practices TLV](https://www.meetup.com/prompt-practices-tlv) — Tel Aviv meetup on prompt engineering practices.
- [Computer Vision Israel Meetup](https://www.meetup.com/Computer-Vision-Israel-Meetup) — Computer vision community meetup.
- [Responsible AI TLV](https://www.meetup.com/responsible-ai-tlv) — Tel Aviv meetup on responsible and ethical AI.

## Facebook Groups

- [AI JLM](https://www.facebook.com/groups/aijlm/) — Jerusalem AI Facebook group.
- [AI Israel](https://www.facebook.com/groups/aisrael/) — General Israeli AI Facebook group.
- [MCP Israel](https://www.facebook.com/groups/mcpisrael/) — Israeli community Facebook group for Model Context Protocol. ([mcpisrael.com](https://mcpisrael.com/))

---

# Government Bodies

Israeli government agencies and national programs relevant to AI.

- [Israel Innovation Authority (innovationisrael.org.il)](https://innovationisrael.org.il/) — Government agency supporting Israeli innovation and R&D, including AI initiatives.
- [National AI Program (aiisrael.org.il)](https://aiisrael.org.il/) — Israel's national program for AI.
- [The Institute for AI (theinstituteai.org.il)](https://www.theinstituteai.org.il/en/) — National institute for AI research and policy.

---

# Centers of Excellence

Academic and research centers focused on AI and data science in Israel.

- [Israel Data Science & AI Initiative — Technion (idsai.net.technion.ac.il)](https://idsai.net.technion.ac.il/) — Technion's interdisciplinary data science and AI research center.

---

# Conferences & Events

AI, ML, and tech conferences and event aggregators in Israel.

- [AI Week](https://ai-week.com/) — Annual AI conference in Israel.
- [IMVC — Israel Machine Vision Conference](https://www.imvc.co.il/) — Annual machine vision and deep learning conference.
- [AI Dev TLV](https://aidevtlv.com/) — Tel Aviv AI developer conference.
- [Tech1](https://tech1.co.il/) — Israeli tech conference.
- [Cyber Week TAU](https://cyberweektau.com/) — Tel Aviv University's annual cybersecurity conference (AI/ML tracks).
- [Dev.Events — Israel AI](https://dev.events/AS/IL/ai) — Aggregated listing of AI events in Israel.
- [Events.co.il](https://events.co.il/) — General Israeli events directory.
- [Science.co.il — AI Conferences](https://www.science.co.il/ai/Conferences.php) — Directory of AI-related conferences in Israel.
- [Machine Learning Israel — Events](https://machinelearning.co.il/events/) — Events calendar from the Machine Learning Israel community.

---

# Inference Providers & Local Clouds

Cloud and inference providers with a presence relevant to Israeli AI workloads.

- [Nebius](https://nebius.com/) — AI-focused cloud and GPU inference provider.

---

# Startup Ecosystem

Directories and databases tracking the Israeli AI startup ecosystem.

- [Startup Nation Finder](https://finder.startupnationcentral.org/) — Searchable database of Israeli startups maintained by Start-Up Nation Central.

---

# Hebrew Language Resources

Indexes and resource lists focused on Hebrew-language AI models, tooling, and evaluations — adjacent to the Israel-specific agent and MCP ecosystem.

## External Resources

- [Dicta (dicta.org.il)](https://dicta.org.il/) — Israeli center for the analysis of Hebrew texts; open-source Hebrew NLP models, datasets, and tools (including DictaLM and OCR for Hebrew).
- [Open Hebrew LLM Leaderboard (Hugging Face)](https://huggingface.co/blog/leaderboard-hebrew) — Community leaderboard evaluating LLMs on Hebrew language tasks.
- [RubyBot (rubybot.co.il)](https://rubybot.co.il/) — Hebrew-native AI chatbot.
- [PolyLM (polylm.com)](https://www.polylm.com/) — Hebrew-native AI assistant / LLM product.

## Indexes

| Project | Description | Stars |
|---|---|---|
| [Hebrew AI Models](https://github.com/danielrosehill/Hebrew-AI-Models) | Index of AI/LLM models with Hebrew language support. | ![](https://img.shields.io/github/stars/danielrosehill/Hebrew-AI-Models?style=social) |
| [Hebrew Language Projects Index](https://github.com/danielrosehill/Hebrew-Language-Projects-Index) | A broad index of Hebrew language projects across the AI/NLP ecosystem. | ![](https://img.shields.io/github/stars/danielrosehill/Hebrew-Language-Projects-Index?style=social) |
| [English ↔ Hebrew Translation](https://github.com/danielrosehill/English-Hebrew-Translation) | Resources, tools, and notes on English ↔ Hebrew translation workflows. | ![](https://img.shields.io/github/stars/danielrosehill/English-Hebrew-Translation?style=social) |
| [Hebrew Calendar Resources](https://github.com/danielrosehill/Hebrew-Calendar-Resources) | Resources for working with the Hebrew calendar (Jewish/Israeli date systems). | ![](https://img.shields.io/github/stars/danielrosehill/Hebrew-Calendar-Resources?style=social) |
| [Hebrew TTS Providers](https://github.com/danielrosehill/Hebrew-TTS-Providers) | Index of text-to-speech providers and engines supporting Hebrew. | ![](https://img.shields.io/github/stars/danielrosehill/Hebrew-TTS-Providers?style=social) |
| [Hebrew Image Generation Eval](https://github.com/danielrosehill/Hebrew-Image-Generation-Eval) | Evaluation of image generation models on their ability to render Hebrew text. | ![](https://img.shields.io/github/stars/danielrosehill/Hebrew-Image-Generation-Eval?style=social) |

# Economics & Statistics

Economic indicators, price indices, and statistical data

| Project | Description | Stars |
|---|---|---|
| [Israel Statistics MCP Server](https://github.com/reuvenaor/israel-statistics-mcp) | Access to Israeli economic data from the Central Bureau of Statistics (CBS) | ![](https://img.shields.io/github/stars/reuvenaor/israel-statistics-mcp?style=social) |


# Finance & Banking

Banking transactions, financial analysis, and economic data

| Project | Description | Stars |
|---|---|---|
| [Invoice Extractor](https://github.com/gil-hue/invoice-extractor) | AI-powered extractor for Israeli invoices. | ![](https://img.shields.io/github/stars/gil-hue/invoice-extractor?style=social) |
| [Payroll](https://github.com/moshe084/payroll) | Israeli payroll tool with AI assistance. | ![](https://img.shields.io/github/stars/moshe084/payroll?style=social) |
| [IL Bank MCP](https://github.com/glekner/il-bank-mcp) | AI-powered financial analysis through automated Israeli bank scraping | ![](https://img.shields.io/github/stars/glekner/il-bank-mcp?style=social) |
| [Nudlers](https://github.com/enudler/nudlers) | Smart personal finance tracker for Israeli banks and credit cards with AI categorization, recurring payment detection, self-hosting via Docker, and MCP support | ![](https://img.shields.io/github/stars/enudler/nudlers?style=social) |
| [GreenInvoice MCP](https://github.com/danielrosehill/GreenInvoice-MCP) | MCP server for Israeli invoicing and accounting via the Green Invoice API | ![](https://img.shields.io/github/stars/danielrosehill/GreenInvoice-MCP?style=social) |
| [Israeli Bank MCP](https://github.com/mottibec/israeli-bank-mcp) | MCP server for managing Israeli bank accounts and transactions | ![](https://img.shields.io/github/stars/mottibec/israeli-bank-mcp?style=social) |
| [ClawSavings](https://github.com/yhyatt/ClawSavings) | Savings tracker/tool with Israeli market focus. | ![](https://img.shields.io/github/stars/yhyatt/ClawSavings?style=social) |


# Government & Open Data

Access to Israeli government datasets, budgets, and public information

| Project | Description | Stars |
|---|---|---|
| [Data.gov.il MCP Server](https://github.com/DavidOsherdiagnostica/data-gov-il-mcp) | Advanced MCP server for accessing Israeli government open data through data.gov.il CKAN API | ![](https://img.shields.io/github/stars/DavidOsherdiagnostica/data-gov-il-mcp?style=social) |
| [Data Israel](https://github.com/LiorVainer/data-israel) | AI agent network that connects to Israeli open data APIs (data.gov.il & CBS) — ask questions in Hebrew, get answers grounded in real data with charts and sources | ![](https://img.shields.io/github/stars/LiorVainer/data-israel?style=social) |
| [DataGov Israel MCP Server](https://github.com/aviveldan/datagov-mcp) | MCP server providing access to Israel's government public data platform (data.gov.il) | ![](https://img.shields.io/github/stars/aviveldan/datagov-mcp?style=social) |
| [ILBudget MCP](https://github.com/david-aftergut/ILBudget-mcp) | Access to Israeli government budget data | ![](https://img.shields.io/github/stars/david-aftergut/ILBudget-mcp?style=social) |
| [Knesset MCP](https://github.com/zohar/knesset-mcp) | Access to Israeli parliament (Knesset) data | ![](https://img.shields.io/github/stars/zohar/knesset-mcp?style=social) |
| [Israel Knesset API MCP](https://github.com/nadavshalev/israel-knesset-api-mcp) | MCP server for accessing the Israeli Knesset (parliament) API | ![](https://img.shields.io/github/stars/nadavshalev/israel-knesset-api-mcp?style=social) |


# Government Services

Public services and administrative functions

| Project | Description | Stars |
|---|---|---|
| [Disabled Parking Permit MCP](https://github.com/MaorEi/disabled-parking-permit-mcp-server) | Israeli disabled parking permit information | ![](https://img.shields.io/github/stars/MaorEi/disabled-parking-permit-mcp-server?style=social) |
| [Israel Fine Checker](https://github.com/kistik1/Israel-fine-checker) | Open-source skill and MCP server for checking Israeli parking and HOV/public-transport-route fines through doh.co.il, with Hebrew intake prompts and support for 63 municipalities | ![](https://img.shields.io/github/stars/kistik1/Israel-fine-checker?style=social) |


# Healthcare & Medical

Medical data, pharmaceuticals, and health services information

| Project | Description | Stars |
|---|---|---|
| [ILHealth MCP](https://github.com/david-aftergut/ILHealth-mcp) | Access to Israeli Ministry of Health data dashboard | ![](https://img.shields.io/github/stars/david-aftergut/ILHealth-mcp?style=social) |
| [Israel Drugs MCP Server](https://github.com/DavidOsherdiagnostica/israel-drugs-mcp-server) | Comprehensive access to Israel's pharmaceutical database from the Ministry of Health | ![](https://img.shields.io/github/stars/DavidOsherdiagnostica/israel-drugs-mcp-server?style=social) |
| [Super-Pharm Stock Checker](https://github.com/BarMalka/super-pharm-stock-checker) | Stock checker for Super-Pharm, Israel's largest pharmacy chain. | ![](https://img.shields.io/github/stars/BarMalka/super-pharm-stock-checker?style=social) |


# Insurance

Israeli insurance market data and intelligence

| Project | Description | Stars |
|---|---|---|
| [Up360 MCP](https://github.com/eliko86/up360mcp) | MCP server for Israeli insurance intelligence — 15 tools for business data, insurance market analysis, lead discovery, and enrichment | ![](https://img.shields.io/github/stars/eliko86/up360mcp?style=social) |


# Legal

Israeli law and regulatory data

| Project | Description | Stars |
|---|---|---|
| [Israel Law MCP](https://github.com/Ansvar-Systems/israel-law-mcp) | Israel law — Privacy Protection Law, Cyber Directorate regulations, Companies Law with Hebrew/English search | ![](https://img.shields.io/github/stars/Ansvar-Systems/israel-law-mcp?style=social) |


# Library & Archives

Library collections and archival data

| Project | Description | Stars |
|---|---|---|
| [NLI AI Search](https://github.com/mula2812/NLI_AI_Search) | National Library of Israel AI-powered search | ![](https://img.shields.io/github/stars/mula2812/NLI_AI_Search?style=social) |


# Real Estate & Land

Property data, land tenders, and real estate information

| Project | Description | Stars |
|---|---|---|
| [Nadlan MCP](https://github.com/nitzpo/nadlan-mcp) | Israeli real estate data (Nadlan = Real Estate in Hebrew) | ![](https://img.shields.io/github/stars/nitzpo/nadlan-mcp?style=social) |
| [Urban Guardian MCP](https://github.com/GaryShnol/urban-guardian-mcp) | An intelligent MCP server that transforms raw Israeli real-estate data into actionable financial insights using Claude | ![](https://img.shields.io/github/stars/GaryShnol/urban-guardian-mcp?style=social) |
| [Remy MCP (Israeli Land Authority)](https://github.com/barvhaim/remy-mcp) | Access to Israeli Land Authority public tender data | ![](https://img.shields.io/github/stars/barvhaim/remy-mcp?style=social) |


# Safety & Emergency

Public shelters, emergency services, and civil defense data

| Project | Description | Stars |
|---|---|---|
| [Miklat MCP](https://github.com/danielrosehill/Miklat-MCP) | MCP server enabling AI agents to guide users towards miklatim tziburim (public shelters) in Israel | ![](https://img.shields.io/github/stars/danielrosehill/Miklat-MCP?style=social) |
| [Pikud HaOref Alerts](https://github.com/yaniv-golan/pikud-haoref-alerts) | MCP server providing live Pikud HaOref alert data to AI assistants | ![](https://img.shields.io/github/stars/yaniv-golan/pikud-haoref-alerts?style=social) |
| [Red Alert MCP Server](https://github.com/ozba/redalert-mcp-server) | MCP server for Israel's Red Alert (צבע אדום) emergency alert system — real-time alerts, statistics, shelter search, and city data | ![](https://img.shields.io/github/stars/ozba/redalert-mcp-server?style=social) |
| [Miklat MCP Data](https://github.com/danielrosehill/Miklat-MCP-Data) | Community-maintained geodata repository and data pipeline for Israeli public shelters, upstream data source for Miklat MCP | ![](https://img.shields.io/github/stars/danielrosehill/Miklat-MCP-Data?style=social) |
| [Israel Preparedness Guidelines AI Assistant](https://github.com/danielrosehill/Israel-Preparedness-Guidelines-AI-Assistant) | AI assistant providing civil defense and emergency preparedness guidance based on Israeli Home Front Command material. | ![](https://img.shields.io/github/stars/danielrosehill/Israel-Preparedness-Guidelines-AI-Assistant?style=social) |


# Shopping & Retail

Israeli e-commerce and price comparison tools

| Project | Description | Stars |
|---|---|---|
| [KSP MCP](https://github.com/guymon92/ksp-mcp) | MCP server for searching and browsing products on KSP.co.il — one of Israel's largest electronics and retail stores | ![](https://img.shields.io/github/stars/guymon92/ksp-mcp?style=social) |
| [Israeli Price Comparison MCP](https://github.com/Simtob-Eran/mcp-israeli-price-comparison) | MCP server for Israeli price comparison | ![](https://img.shields.io/github/stars/Simtob-Eran/mcp-israeli-price-comparison?style=social) |
| [Israeli Tech Shopping MCP](https://github.com/danielrosehill/Israeli-Tech-Shopping-MCP) | MCP server for comparison shopping across Israeli tech retailers with browser automation | ![](https://img.shields.io/github/stars/danielrosehill/Israeli-Tech-Shopping-MCP?style=social) |


# Transportation

Routing, transit, and transportation data

| Project | Description | Stars |
|---|---|---|
| [Routes MCP Israel](https://github.com/yoni-j/routes-mcp-israel) | Israeli transportation and routing data | ![](https://img.shields.io/github/stars/yoni-j/routes-mcp-israel?style=social) |


# Weather & Environment

Meteorological data and environmental information

| Project | Description | Stars |
|---|---|---|
| [IMS MCP (Israeli Meteorological Service)](https://github.com/GuyKh/ims-mcp) | Access to Israeli Meteorological Service data | ![](https://img.shields.io/github/stars/GuyKh/ims-mcp?style=social) |


# Careers & Jobs

AI tools for job hunting and career monitoring in the Israeli market.

| Project | Description | Stars |
|---|---|---|
| [Job Hunt AI](https://github.com/ayhambd12/job-hunt-ai) | AI-powered job hunting assistant. | ![](https://img.shields.io/github/stars/ayhambd12/job-hunt-ai?style=social) |
| [Israeli Job Scanner](https://github.com/benkleinben-pixel/israeli-job-scanner) | Scanner for Israeli job listings. | ![](https://img.shields.io/github/stars/benkleinben-pixel/israeli-job-scanner?style=social) |
| [Develeap BDR Job Monitor](https://github.com/DoriKafri/develeap-bdr-job-monitor) | Job monitor for Develeap BDR roles. | ![](https://img.shields.io/github/stars/DoriKafri/develeap-bdr-job-monitor?style=social) |


# Dashboards

AI-powered dashboards with an Israeli focus.

| Project | Description | Stars |
|---|---|---|
| [News Dashboard](https://github.com/avivbaramamirim-crypto/news-dashboard) | AI-powered news dashboard. | ![](https://img.shields.io/github/stars/avivbaramamirim-crypto/news-dashboard?style=social) |


# Plugins

Claude Code and agent plugins for Israeli services.

| Project | Description | Stars |
|---|---|---|
| [Deep Value TASE Plugin](https://github.com/deepvalueinvesting/deep-value-tase-plugin) | Deep-value investing plugin for the Tel Aviv Stock Exchange (TASE). | ![](https://img.shields.io/github/stars/deepvalueinvesting/deep-value-tase-plugin?style=social) |


# Voice Agents

Voice-enabled AI agents for Israeli use cases.

| Project | Description | Stars |
|---|---|---|
| [Voxione](https://github.com/voxiproxiv1-blip/voxione) | Voice AI agent project. | ![](https://img.shields.io/github/stars/voxiproxiv1-blip/voxione?style=social) |


# Other Projects

Projects that need categorization.

| Project | Description | Stars |
|---|---|---|
| [Geopol Forecaster POC](https://github.com/danielrosehill/Geopol-Forecaster-POC) | Proof-of-concept AI geopolitical forecaster with a focus on events relevant to Israel and the wider region. | ![](https://img.shields.io/github/stars/danielrosehill/Geopol-Forecaster-POC?style=social) |
| [Quantum Pinuy Binuy Analyzer](https://github.com/hemichaeli/quantum-pinuy-binuy-analyzer) | Analyzer for Israeli pinuy-binuy (evacuation-reconstruction) urban renewal projects. | ![](https://img.shields.io/github/stars/hemichaeli/quantum-pinuy-binuy-analyzer?style=social) |
| [Asher MCP](https://github.com/shlomiuziel/asher-mcp) | Unknown purpose - requires investigation | ![](https://img.shields.io/github/stars/shlomiuziel/asher-mcp?style=social) |
| [Fingent](https://github.com/amitdan1/Fingent) | Fingent — Smart Financial Management System for Israel. AI-powered advisor (Finni), open banking, expense analytics | ![](https://img.shields.io/github/stars/amitdan1/Fingent?style=social) |
| [RPA Port Platform](https://github.com/doronrpa-hub/rpa-port-platform) | Israeli Customs Intelligence Platform — AI-powered document classification, email monitoring, and self-learning knowledge base | ![](https://img.shields.io/github/stars/doronrpa-hub/rpa-port-platform?style=social) |


# Contributing

Anyone is welcome to open a pull request to add an Israel-related AI agent, skill, or MCP server to this list.

To add a new project:
1. Fork this repository
2. Add your project to `projects.json` using the update script:
   ```bash
   ./update-projects.py --add https://github.com/username/repo --category category-name
   ```
3. Run the README generator:
   ```bash
   ./generate-readme.py
   ```
4. Submit a pull request

Alternatively, drop me a line at public@danielrosehill.com if you'd like me to add it manually.

# Disclaimer

This resource is intended for those discovering AI agents, skills, and MCP servers relevant to Israel. It is not exhaustive and is maintained on a best-effort basis.

The inclusion of a project in this list does not constitute an endorsement. Users should evaluate each project independently for their specific use cases.

---

*Last updated: 2026-04-05*

Maintained by [Daniel Rosehill](https://github.com/danielrosehill)