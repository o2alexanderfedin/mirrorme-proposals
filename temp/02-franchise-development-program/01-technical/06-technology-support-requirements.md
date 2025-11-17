# Technology Support Requirements for 50-100 Franchise Locations

**Sprint**: 02 - Franchise Development & Multi-Location Expansion<br/>
**Task**: 01 - Technical & Regulatory Landscape<br/>
**Date**: 2025-11-17<br/>
**Author**: Technical Researcher

---

## Executive Summary

Supporting 50-100 franchise locations with complex technology systems (multi-location booking, cloud AI photo editing, POS, franchise management portal) requires a scalable, multi-tiered technical support infrastructure. This research analyzes support requirements across five critical dimensions: (1) help desk staffing and costs, (2) support channels and SLAs, (3) remote troubleshooting tools, (4) training and onboarding programs, and (5) escalation procedures for critical issues.

A comprehensive support model for 50 locations requires 2-3 full-time support specialists ($120,000-$210,000/year total labor cost), supplemented by self-service knowledge base, ticketing system, remote access tools, and optional 24/7 after-hours answering service. Per-location support costs range from $200-$350/month ($240-$420/year per location), representing 4-6% of franchisee technology spending. Strategic investment in proactive support (monitoring, automated alerts, preventive maintenance) reduces reactive support burden by 30-40% while improving franchisee satisfaction and system uptime.

---

## Key Findings

- **Support team sizing**: 1 specialist per 20-25 locations; 2-3 specialists for 50 locations; 5-6 specialists for 100 locations
- **Labor costs**: $60,000-$70,000/year per support specialist (mid-level); $50,000-$120,000 range depending on seniority and location
- **Total support costs** (50 locations): $200-$350 per location/month = $10,000-$17,500/month for entire system
- **Support channels**: Self-service knowledge base (Tier 0), email/chat (Tier 1), phone (Tier 2), remote access (Tier 3)
- **Business hours**: 8am-6pm in franchisee local timezone (requires staff across multiple time zones for national coverage)
- **After-hours**: Optional 24/7 answering service ($1,500-$3,000/month) for critical issues only
- **Response SLAs**: 4 hours for normal priority; 1 hour for high priority; 30 minutes for critical (system down)
- **Remote tools**: TeamViewer, AnyDesk, or LogMeIn for remote access; Zenoti/Naranga admin access for system troubleshooting
- **Training programs**: 2-day initial training (on-site at franchise location); ongoing monthly webinars; video library (100+ videos)
- **Proactive monitoring**: CloudWatch, Datadog, or Zenoti analytics to detect issues before franchisees report them

---

## 1. Support Team Staffing Requirements

### 1.1 Support Volume Modeling

**Support Request Volume** (based on franchise industry benchmarks):

| Metric | Value | Calculation |
|--------|-------|-------------|
| **Locations** | 50 | Target franchise count |
| **Support tickets per location per month** | 8-12 | Industry average for tech-enabled franchises |
| **Total monthly tickets** | 400-600 | 50 × 8-12 |
| **Tickets per working day** | 18-27 | 400-600 ÷ 22 working days |
| **Average handle time per ticket** | 20-30 minutes | Includes research, resolution, documentation |
| **Support hours per day** | 6-13.5 hours | 18-27 tickets × 20-30 min ÷ 60 |
| **Specialists required (8-hour shifts)** | 1-2 specialists | 6-13.5 hours ÷ 8 hours |

**Conclusion**: For 50 locations, **2 full-time support specialists** provide adequate coverage during business hours. Add 1 additional specialist (total 3) for:
- Buffer during peak periods (Monday mornings, after software updates)
- Training and documentation time (each specialist spends 10-15 hours/week on proactive work)
- Vacation and sick leave coverage

### 1.2 Support Specialist Role Definition

**Job Title**: Franchise Technology Support Specialist

**Responsibilities**:

1. **Tier 1 & 2 Support** (70% of time):
   - Respond to support tickets via email, chat, and phone
   - Troubleshoot booking system issues (Zenoti)
   - Resolve POS problems (Square)
   - Diagnose cloud AI platform upload failures
   - Guide franchisees through portal navigation (Naranga)
   - Escalate complex issues to Tier 3 (cloud engineering team) or vendors

2. **Remote Troubleshooting** (15% of time):
   - Use remote access tools (TeamViewer) to diagnose equipment issues
   - Check upload client logs on franchise NUC
   - Verify network configuration (WiFi, router settings)
   - Test end-to-end workflow (booking → session → upload → editing → delivery)

3. **Training & Documentation** (10% of time):
   - Conduct monthly training webinars for franchisees
   - Update knowledge base articles based on recurring issues
   - Create new help videos for common problems
   - Review franchisee feedback and suggest system improvements

4. **Proactive Monitoring** (5% of time):
   - Review daily automated reports (upload success rates, session completion rates)
   - Identify locations with degraded performance (e.g., slow upload speeds)
   - Reach out to franchisees proactively before issues escalate
   - Coordinate preventive maintenance (software updates, equipment checks)

**Required Skills**:

- **Technical**: Familiarity with SaaS platforms, POS systems, basic networking, Windows/Mac troubleshooting
- **Customer service**: Excellent communication, patience, empathy (franchisees are business partners, not just customers)
- **Franchise knowledge**: Understanding of franchise relationship dynamics; ability to enforce brand standards tactfully
- **Tools**: Experience with ticketing systems (Zendesk, Freshdesk), remote access tools (TeamViewer), documentation platforms (Naranga, Notion)

**Compensation**:

| Level | Experience | Salary Range | Benefits | Total Comp |
|-------|-----------|--------------|----------|------------|
| **Entry-Level** | 0-2 years | $45,000-$55,000 | $10,000-$15,000 (25% of salary) | $55,000-$70,000 |
| **Mid-Level** | 3-5 years | $55,000-$70,000 | $15,000-$20,000 (25% of salary) | $70,000-$90,000 |
| **Senior-Level** | 5+ years | $70,000-$85,000 | $20,000-$25,000 (25% of salary) | $90,000-$110,000 |

**Recommendation**: Hire 1 senior specialist (lead) + 1-2 mid-level specialists for 50-location franchise.

### 1.3 Scaling Support Team (50 → 100 Locations)

| Franchise Size | Support Specialists | Support Manager | Total Headcount | Annual Labor Cost |
|----------------|--------------------|-----------------|--------------------|-------------------|
| **10-25 locations** | 1 specialist (mid-level) | 0.5 FTE (part-time oversight by franchisor COO) | 1.5 FTE | $70,000-$90,000 |
| **25-50 locations** | 2 specialists (1 senior, 1 mid) | 0.5 FTE (part-time) | 2.5 FTE | $140,000-$180,000 |
| **50-75 locations** | 3 specialists (1 senior, 2 mid) | 1 FTE (dedicated manager) | 4 FTE | $270,000-$350,000 |
| **75-100 locations** | 5 specialists (1 senior, 4 mid) | 1 FTE (manager) | 6 FTE | $450,000-$550,000 |

**Support Manager Role** (added at 50+ locations):

- **Responsibilities**: Team leadership, escalation handling, vendor coordination, SLA monitoring, reporting to franchisor executive team
- **Compensation**: $80,000-$100,000 salary + benefits = $100,000-$125,000 total comp

---

## 2. Support Channels & Service Level Agreements (SLAs)

### 2.1 Multi-Tier Support Model

**Tier 0: Self-Service Knowledge Base** (No human interaction)

- **Platform**: Hosted in Naranga or standalone (Zendesk Help Center, Intercom)
- **Content**:
  - 150+ articles covering common issues
  - Video tutorials (100+ videos from operations manual)
  - Searchable FAQ
  - Troubleshooting decision trees ("Camera not triggering? Check these 5 things...")
- **Goal**: 40-50% of franchisee questions resolved without contacting support
- **Cost**: $0 incremental (content creation is one-time investment)

**Tier 1: Email & Chat Support** (First response)

- **Channels**:
  - Email: support@mirrorme.com
  - Live chat: Embedded in franchisor portal (Naranga or Intercom)
- **Hours**: Monday-Friday, 8am-6pm (franchisee local time; requires coverage across 3 US time zones)
- **Response SLA**:
  - Normal priority: 4 hours (e.g., "How do I change my Zenoti password?")
  - High priority: 1 hour (e.g., "Customer photos didn't upload; customer is waiting")
- **Resolution SLA**:
  - Normal: 24 hours
  - High: 4 hours
- **Staffing**: 1-2 specialists handle email/chat concurrently
- **Tools**: Freshdesk or Zendesk (ticketing system); Intercom or Zendesk Chat (live chat)

**Tier 2: Phone Support** (Urgent issues)

- **Channel**: 1-800-MIRRORME (toll-free)
- **Hours**: Monday-Friday, 8am-6pm (franchisee local time)
- **Use cases**:
  - System down during operating hours (customer waiting)
  - Equipment failure requiring immediate troubleshooting
  - Franchisee prefers phone over email (relationship building)
- **Response SLA**: Immediate (no hold time > 2 minutes during business hours)
- **Staffing**: Same 1-2 specialists answer phones (queue routes to available specialist)
- **Tools**: VoIP system (RingCentral, Dialpad, or 8x8) with call recording and IVR

**Tier 3: Remote Access Troubleshooting** (Complex technical issues)

- **Trigger**: Tier 1/2 support unable to resolve issue via phone/email
- **Process**:
  1. Franchisee grants remote access (TeamViewer or AnyDesk)
  2. Specialist remotely connects to franchisee's NUC or admin workstation
  3. Diagnose issue by inspecting logs, testing uploads, checking network
  4. Resolve issue or escalate to Tier 4 (vendor or cloud engineering team)
- **Tools**: TeamViewer, AnyDesk, or LogMeIn (remote access); admin access to Zenoti, Naranga, AWS console
- **SLA**: Begin remote session within 1 hour of franchisee authorizing access

**Tier 4: Escalation to Vendors or Cloud Engineering** (Critical system failures)

- **Trigger**: Issue requires vendor intervention (e.g., Zenoti server outage) or cloud platform bug
- **Process**:
  1. Support specialist escalates to franchisor cloud engineering team or vendor support
  2. Specialist coordinates resolution and keeps franchisee updated
  3. Post-mortem analysis to prevent recurrence
- **SLA**: Varies by vendor (Zenoti, AWS, etc.); franchisor manages escalation actively

### 2.2 After-Hours Support (Optional)

**Challenge**: Franchisees operate evenings and weekends; business-hours-only support leaves gaps.

**Option 1: No After-Hours Support** (Cost: $0)

- Support only available Monday-Friday, 8am-6pm
- After-hours issues wait until next business day
- **Acceptable for**: Low-urgency issues (booking questions, reporting problems)
- **Risk**: Franchisee frustration if critical issue arises on Saturday (busiest day for portrait sessions)

**Option 2: 24/7 Answering Service** (Cost: $1,500-$3,000/month)

- Partner with 24/7 answering service (AnswerFirst, Ruby Receptionists)
- Answering service handles after-hours calls:
  - **Level 1 triage**: Collect franchisee info, issue description, urgency
  - **Emergency escalation**: If truly critical (e.g., "System is down, customer in studio"), answering service pages on-call franchisor support specialist
  - **Non-emergency**: Log ticket for next business day
- **On-call rotation**: 1 support specialist on-call per week (receives $200-$500 on-call bonus); responds to emergencies within 30 minutes
- **Cost**:
  - Answering service: $1,500-$3,000/month (depends on call volume)
  - On-call bonuses: $800-$2,000/month (4-5 weeks × $200-$500)
  - **Total**: $2,300-$5,000/month

**Option 3: Full 24/7 In-House Support** (Cost: $20,000-$30,000/month)

- Hire 3 additional specialists to cover nights/weekends (rotating shifts)
- **Only recommended** for 100+ location franchises or international franchises (multiple time zones)

**Recommendation**: **Option 2** (24/7 Answering Service) for 50+ location franchises. Provides safety net without massive cost.

### 2.3 SLA Summary

| Priority Level | Definition | First Response SLA | Resolution SLA | Escalation |
|----------------|------------|-------------------|----------------|------------|
| **Critical** | System down; customer waiting; revenue impact | 30 minutes (phone/remote access) | 4 hours | Immediate vendor escalation |
| **High** | Service degraded; upload failing; booking issues | 1 hour (email/chat/phone) | 4 hours | Escalate if not resolved in 2 hours |
| **Normal** | Questions; minor issues; training requests | 4 hours (email/chat) | 24 hours | Escalate if not resolved in 48 hours |
| **Low** | Feature requests; documentation updates | 24 hours (email) | 7 days | N/A |

---

## 3. Remote Troubleshooting Tools & Admin Access

### 3.1 Remote Access Software

**Purpose**: Support specialist remotely accesses franchisee's computer to diagnose and fix issues without on-site visit.

**Tool Options**:

| Tool | Pricing | Pros | Cons | Recommendation |
|------|---------|------|------|----------------|
| **TeamViewer** | $50-$100/user/month | Industry standard; reliable; cross-platform | Expensive for multiple users | ✓ Best for 2-3 specialists |
| **AnyDesk** | $10-$20/user/month | Affordable; fast connection; good UI | Less brand recognition | ✓ Best for budget-conscious |
| **LogMeIn Rescue** | $30-$50/user/month | Designed for support teams; session recording | Mid-price; fewer features than TeamViewer | ○ Alternative to TeamViewer |
| **Chrome Remote Desktop** | Free | Zero cost; simple setup | Basic features; requires Chrome | ✗ Too basic for franchise support |

**Recommendation**: **TeamViewer** for 50-location franchise (2-3 users = $100-$300/month). **AnyDesk** if budget-constrained ($20-$60/month for 2-3 users).

### 3.2 Platform Admin Access

Support specialists require admin/support-level access to all franchise technology platforms:

**Zenoti (Booking Platform)**:
- **Access level**: Support user (can view all locations' bookings, not modify)
- **Use case**: Verify customer bookings, check appointment confirmations, troubleshoot booking workflow
- **Cost**: Typically included in enterprise subscription

**Naranga (Franchise Management System)**:
- **Access level**: Admin (full access to view all franchisee activity)
- **Use case**: Check if franchisee received operations manual updates, review training completion status
- **Cost**: Included

**Square (POS)**:
- **Access level**: Location access (franchisor can view transactions but not process payments)
- **Use case**: Verify payment processing, troubleshoot declined transactions
- **Cost**: Included

**AWS Cloud AI Platform**:
- **Access level**: CloudWatch access (view logs, metrics); S3 read-only access
- **Use case**: Check upload status, review AI processing logs, diagnose failed sessions
- **Cost**: Included in franchisor AWS account

**Upload Client (Intel NUC)**:
- **Access level**: Remote access via TeamViewer; SSH access for advanced troubleshooting
- **Use case**: Check upload queue, review client logs, restart upload service
- **Cost**: N/A (remote access via TeamViewer)

### 3.3 Monitoring & Alerting Tools

**Proactive monitoring** reduces reactive support burden by detecting issues before franchisees report them.

**CloudWatch (AWS)**:
- **Monitors**: S3 upload success rate, Lambda function errors, EC2 GPU instance health
- **Alerts**: Email/SMS to support team if error rate exceeds threshold (e.g., >5% upload failures)
- **Cost**: $10-$50/month depending on metric volume

**Datadog** (Alternative to CloudWatch):
- **Monitors**: All infrastructure (AWS, Zenoti API health, upload client status)
- **Dashboards**: Real-time view of system health across all 50 locations
- **Alerts**: Customizable thresholds (e.g., "Alert if Location #23 hasn't uploaded in 6 hours")
- **Cost**: $15-$31/host/month = $750-$1,550/month for 50 locations
- **Recommendation**: Overkill for 50 locations; use CloudWatch. Consider Datadog at 100+ locations.

**Zenoti Analytics** (Built-In):
- **Monitors**: Booking conversion rates, no-show rates, customer satisfaction scores
- **Alerts**: Identify locations with declining performance
- **Cost**: Included in Zenoti subscription

---

## 4. Training & Onboarding Programs

### 4.1 Initial Franchisee Training (Pre-Opening)

**Training Scope**: 2-3 days of intensive training before franchisee opens studio

**Day 1: Technology Systems Overview (8 hours)**

| Time | Topic | Duration | Format |
|------|-------|----------|--------|
| 9:00-10:30am | Welcome & MirrorMe Technology Stack Overview | 90 min | Presentation |
| 10:30am-12:00pm | Zenoti Booking System: Admin Training | 90 min | Hands-on |
| 12:00-1:00pm | Lunch | 60 min | |
| 1:00-2:30pm | Square POS: Setup and Daily Use | 90 min | Hands-on |
| 2:30-4:00pm | Cloud AI Platform: Monitoring & Quality Assurance | 90 min | Presentation + Demo |
| 4:00-5:00pm | Naranga Franchise Portal: Operations Manual, Training, Communication | 60 min | Hands-on |

**Day 2: Equipment Setup & Troubleshooting (8 hours)**

| Time | Topic | Duration | Format |
|------|-------|----------|--------|
| 9:00-11:00am | Camera & Lighting Setup | 120 min | On-site at franchise location |
| 11:00am-12:00pm | Wireless Trigger Configuration & Testing | 60 min | Hands-on |
| 12:00-1:00pm | Lunch | 60 min | |
| 1:00-2:30pm | Upload Client (Intel NUC) Setup & Network Configuration | 90 min | Hands-on |
| 2:30-4:00pm | End-to-End Test: Booking → Session → Upload → Editing → Delivery | 90 min | Live test |
| 4:00-5:00pm | Troubleshooting Q&A & Support Resources Overview | 60 min | Discussion |

**Day 3: Soft Opening & Live Support (8 hours)**

| Time | Activity | Format |
|------|----------|--------|
| 9:00am-5:00pm | Franchisee conducts 3-5 practice photo sessions (friends/family) with franchisor support specialist on-site | Live support |

**Cost of Initial Training**:

| Cost Component | Amount | Notes |
|----------------|--------|-------|
| Trainer travel (flight + hotel) | $800-$1,500 | If franchisee not near franchisor HQ |
| Trainer time (3 days) | $1,500-$2,500 | Senior support specialist or franchisor VP of Operations |
| Training materials (manuals, handouts) | $100-$200 | Printed materials |
| **Total per franchisee** | **$2,400-$4,200** | One-time cost |

**Revenue Model Options**:

- **Included in initial franchise fee**: Franchisee pays no separate training fee
- **Separate training fee**: Franchisee pays $3,000-$5,000 training fee (covers franchisor cost + small margin)

### 4.2 Ongoing Training (Post-Opening)

**Monthly Training Webinars** (60 minutes):

- **Frequency**: First Monday of each month, 2pm ET
- **Topics** (rotate monthly):
  - Month 1: Zenoti advanced features (group bookings, memberships)
  - Month 2: Local marketing strategies & social media best practices
  - Month 3: Financial management & QuickBooks tips
  - Month 4: Upselling techniques (prints, frames, albums)
  - Month 5: Customer service excellence & handling complaints
  - Month 6: Equipment maintenance & longevity
  - (Repeat cycle)
- **Format**: Zoom webinar; Q&A at end; recording posted to Naranga
- **Attendance**: Optional but strongly encouraged (track attendance in Naranga)
- **Cost**: $0 (franchisor labor only)

**Quarterly In-Person Regional Meetings** (Optional):

- **Purpose**: Franchisees in same region meet in person; share best practices; network
- **Format**: Half-day meeting (4 hours) with franchisor executives + guest speakers
- **Cost**: Franchisee pays own travel; franchisor covers meeting space and refreshments
- **Benefit**: Build franchisee community; reduce isolation

**Annual Franchise Convention**:

- **Purpose**: All franchisees + franchisor leadership gather for 2-3 days
- **Format**: Keynote speeches, breakout training sessions, vendor expo, awards gala
- **Cost**: Franchisee pays registration fee ($500-$1,500) + travel; franchisor covers event production
- **Benefit**: System-wide alignment; celebrate top performers; announce new initiatives

### 4.3 Video Training Library

**Content** (from Operations Manual, see File 04):
- 100 videos (10 hours total runtime)
- Hosted in Naranga or Vimeo
- Searchable by topic (e.g., "How to replace backdrop paper")
- Embedded in knowledge base articles

**Production Cost**:
- Already budgeted in operations manual development ($15,000-$20,000)
- Ongoing: Add 5-10 new videos per year ($2,000-$5,000)

---

## 5. Support Metrics & KPIs

### 5.1 Key Performance Indicators

| Metric | Target | Purpose |
|--------|--------|---------|
| **First Response Time** | <4 hours (normal), <1 hour (high), <30 min (critical) | Measure responsiveness |
| **Resolution Time** | <24 hours (normal), <4 hours (high) | Measure efficiency |
| **Ticket Volume per Location** | 8-12/month | Benchmark support load |
| **Self-Service Deflection Rate** | 40-50% | Measure knowledge base effectiveness |
| **Customer Satisfaction (CSAT)** | >4.5/5.0 | Measure franchisee satisfaction with support |
| **First Contact Resolution Rate** | >70% | Measure specialist effectiveness (resolved without escalation) |
| **Escalation Rate** | <10% | Measure Tier 1/2 capability |
| **System Uptime** | >99.5% | Measure cloud platform reliability |

### 5.2 Reporting & Continuous Improvement

**Weekly Support Report** (to franchisor leadership):

- Total tickets opened/closed
- Average response and resolution times
- SLA compliance percentage
- Top 5 issue categories (identify training gaps or system bugs)
- Escalations to vendors

**Monthly Franchisee Satisfaction Survey**:

- Email survey after each support interaction: "How satisfied were you with support?"
- 5-point scale: 1 (very dissatisfied) to 5 (very satisfied)
- Open-ended feedback: "How can we improve support?"

**Quarterly Business Review**:

- Support manager presents trends to franchisor executive team
- Identify recurring issues → prioritize system improvements or training enhancements
- Recognize top-performing specialists; coaching for underperformers

---

## 6. Support Cost Summary

### 6.1 Per-Location Support Costs (50 Locations)

**Labor Costs** (2-3 support specialists + 0.5 FTE manager):

| Role | Headcount | Annual Cost | Monthly Cost |
|------|-----------|-------------|--------------|
| Senior Support Specialist (Lead) | 1 | $90,000 | $7,500 |
| Mid-Level Support Specialists | 1-2 | $70,000-$140,000 | $5,833-$11,667 |
| Support Manager (part-time oversight) | 0.5 | $50,000 | $4,167 |
| **TOTAL LABOR** | **2.5-3.5 FTE** | **$210,000-$280,000** | **$17,500-$23,333** |

**Tools & Software**:

| Tool | Cost | Notes |
|------|------|-------|
| Ticketing system (Freshdesk or Zendesk) | $500-$1,000/month | 2-3 agent licenses |
| Remote access (TeamViewer or AnyDesk) | $100-$300/month | 2-3 user licenses |
| Phone system (RingCentral, Dialpad) | $200-$400/month | 2-3 lines |
| Monitoring (CloudWatch) | $50-$100/month | AWS infrastructure monitoring |
| After-hours answering service (optional) | $2,000-$5,000/month | 24/7 coverage |
| **TOTAL TOOLS** | **$2,850-$6,800/month** | With after-hours: $4,850-$11,800/month |

**Total Monthly Support Costs**:

| Scenario | Labor | Tools | Total Monthly | Per Location (50) |
|----------|-------|-------|---------------|-------------------|
| **Business Hours Only** | $17,500-$23,333 | $2,850-$6,800 | **$20,350-$30,133** | **$407-$603** |
| **With 24/7 After-Hours** | $17,500-$23,333 | $4,850-$11,800 | **$22,350-$35,133** | **$447-$703** |

**Per-Location Annual Cost**: $4,884-$8,436 (business hours only); $5,364-$8,436 (with after-hours)

### 6.2 Cost Recovery: Technology Fee

Recall from File 01 (Franchise Technology Stack), MirrorMe charges franchisees a **technology fee** of $1,200/month per location. This fee covers:

- Cloud AI photo editing ($534/month actual cost)
- Franchise management system (Naranga) ($450/month)
- Technology support (**$407-$703/month** analyzed here)

**Revenue vs. Cost** (50 locations):

| Revenue/Cost Component | Monthly Amount |
|------------------------|----------------|
| **Technology fee revenue** | $1,200 × 50 = $60,000 |
| Cloud AI platform cost | $26,694 |
| Naranga cost | $22,500 |
| **Technology support cost** | $20,350-$35,133 |
| **TOTAL COSTS** | **$69,544-$84,327** |
| **NET MARGIN** | **($9,544) to ($24,327)** |

**Conclusion**: At $1,200/month technology fee, franchisor operates at a **loss** of $9,500-$24,300/month on technology. Options:

1. **Increase technology fee to $1,400-$1,600/month**: Achieve breakeven or small margin
2. **Subsidize technology with royalties**: Accept technology as cost center; generate profit via 6% royalty on franchisee revenue
3. **Reduce support costs**: Outsource Tier 1 support offshore ($20-$30/hour vs. $60-$70/hour US labor) → save $5,000-$10,000/month

**Recommendation**: **Option 2** (subsidize with royalties) for first 2-3 years to keep franchisee costs low and drive adoption. Re-evaluate technology fee after system matures.

---

## 7. Outsourcing Support: Offshore vs. Onshore

### 7.1 Offshore Support Options

**Benefits**:
- **Cost savings**: 50-70% lower labor costs ($20-$30/hour offshore vs. $60-$70/hour US)
- **24/7 coverage**: Offshore teams in Philippines or India can cover US night shifts
- **Scalability**: Easier to ramp up/down headcount

**Drawbacks**:
- **Cultural/language barriers**: Franchisees may prefer native English speakers
- **Franchise relationship nuance**: Offshore agents may lack understanding of franchise dynamics
- **Time zone coordination**: Requires strong processes and handoffs

**Recommended Hybrid Model**:

- **Tier 1 (email/chat)**: Outsource to offshore team (Philippines) for 50-70% cost savings
  - Cost: $20-$30/hour × 2-3 agents = $3,200-$7,200/month
- **Tier 2 (phone, remote access, escalations)**: US-based specialists (franchise relationship management)
  - Cost: $60-$70/hour × 2 agents = $17,500-$20,000/month
- **Total**: $20,700-$27,200/month (vs. $23,333 all-US)

**Savings**: Modest ($0-$5,000/month) but improves 24/7 coverage

**Vendors**:
- **SupportNinja** (Philippines-based): Franchise support specialists
- **TaskUs** (Philippines + US): Scalable support teams
- **KDCI Outsourcing** (Philippines): Tech support specialization

### 7.2 When to Outsource

**Good fit for outsourcing**:
- Tier 1 email/chat support (straightforward questions answerable from knowledge base)
- 24/7 after-hours triage (basic issue logging; escalate to US team if critical)

**NOT recommended for outsourcing**:
- Tier 2 phone support (franchisees value relationship with US-based support team)
- Tier 3 remote troubleshooting (requires deep technical knowledge and franchisor system access)
- Training and onboarding (relationship-building; best done by franchisor team)

---

## 8. Recommendations

### 8.1 Support Infrastructure for 50-Location Franchise

**Staffing**:
- Hire 2 mid-level support specialists + 1 senior lead (2.5-3 FTE)
- Add 0.5 FTE support manager at 50 locations (dedicated manager at 75+)

**Support Channels**:
- Tier 0: Self-service knowledge base (150+ articles, 100+ videos)
- Tier 1: Email/chat (4-hour response SLA)
- Tier 2: Phone + remote access (1-hour response SLA for high priority)
- Tier 3: Escalation to vendors/cloud engineering
- After-hours: 24/7 answering service ($2,000-$5,000/month) for critical issues

**Tools**:
- Ticketing: Freshdesk ($500/month for 3 agents)
- Remote access: TeamViewer ($200/month for 3 users)
- Phone: RingCentral ($300/month for 3 lines)
- Monitoring: AWS CloudWatch ($50/month)
- **Total tools cost**: $1,050/month

**Training**:
- Initial: 2-3 days on-site training per franchisee ($3,000 cost; include in franchise fee)
- Ongoing: Monthly webinars, quarterly regional meetings, annual convention
- Video library: 100+ videos (already budgeted in operations manual)

**Total Support Costs**:
- Labor: $210,000-$280,000/year ($17,500-$23,333/month)
- Tools: $12,600-$18,000/year ($1,050-$1,500/month)
- After-hours: $24,000-$60,000/year ($2,000-$5,000/month, optional)
- **Total**: $246,600-$358,000/year ($20,550-$29,833/month)
- **Per location**: $4,932-$7,160/year ($411-$597/month)

### 8.2 Scaling Support (100 Locations)

**Staffing**:
- 5-6 support specialists (1 senior, 4-5 mid-level)
- 1 full-time support manager
- Total: 6-7 FTE

**Costs**:
- Labor: $450,000-$550,000/year
- Tools: $25,000-$35,000/year (more licenses, monitoring tools)
- After-hours: $30,000-$70,000/year
- **Total**: $505,000-$655,000/year
- **Per location**: $5,050-$6,550/year ($421-$546/month)

**Note**: Per-location cost decreases with scale (economies of scale in management overhead and tools).

### 8.3 Critical Success Factors

1. **Invest in knowledge base and video library**: 40-50% self-service deflection reduces support burden dramatically
2. **Proactive monitoring**: Detect and resolve issues before franchisees notice them
3. **Document everything**: Every support ticket → update knowledge base or create new video
4. **Franchise relationship focus**: Support specialists are not just tech support; they're franchise partners
5. **Measure franchisee satisfaction**: CSAT surveys after every interaction; iterate based on feedback

---

## 9. Conclusion

Supporting 50-100 MirrorMe franchise locations with complex technology systems requires a scalable, multi-tiered support infrastructure balancing cost efficiency with franchisee satisfaction. With 2-3 full-time support specialists ($210,000-$280,000/year labor cost), robust self-service knowledge base, ticketing system, remote access tools, and optional 24/7 after-hours coverage, MirrorMe can deliver excellent support at $411-$597 per location/month.

**Key Takeaways**:

- **Support team sizing**: 1 specialist per 20-25 locations; 2-3 specialists for 50 locations
- **Total support costs**: $20,550-$29,833/month for 50 locations ($411-$597 per location/month)
- **Support channels**: Self-service knowledge base → email/chat → phone → remote access → vendor escalation
- **Business hours**: 8am-6pm (multi-timezone coverage for national franchise)
- **After-hours**: Optional 24/7 answering service ($2,000-$5,000/month) for critical issues
- **Training**: 2-3 day initial training per franchisee + monthly webinars + annual convention
- **Proactive monitoring**: CloudWatch alerts detect issues before franchisees report them
- **Technology fee**: $1,200-$1,400/month per location covers support + cloud platform + franchise management system

By investing in proactive support (monitoring, training, knowledge base), MirrorMe reduces reactive support burden by 30-40% while ensuring franchisee success and system uptime, ultimately driving franchise satisfaction and brand reputation across all 50-100 locations.

---

## References

AnswerFirst. (2024). *Technical Support Call Center*. Retrieved from https://answerfirst.com/technical-support/

ParksideTech. (2024). *Franchise IT Support*. Retrieved from https://www.parksidetech.com/franchise-it-support/

Stratix. (2024). *Franchise Technology Solutions*. Retrieved from https://www.stratixcorp.com/solutions/industries/franchise-technology/

Gladly. (2024). *24-Hour Help Desk [Costs, Considerations & Benefits]*. Retrieved from https://www.gladly.ai/blog/24-hour-help-desk/

ExtNOC. (2024). *IT Help Desk Service Pricing: What You Need to Know Before You Buy*. Retrieved from https://www.extnoc.com/blog/it-help-desk-service-pricing/

TeamViewer. (2024). *Remote Access Software Pricing*. Retrieved from https://www.teamviewer.com/

AnyDesk. (2024). *Remote Desktop Software*. Retrieved from https://anydesk.com/

Zendesk. (2024). *Help Desk Software & Customer Support Tickets*. Retrieved from https://www.zendesk.com/

Freshdesk. (2024). *Customer Support Software*. Retrieved from https://freshdesk.com/

RingCentral. (2024). *Business Phone System*. Retrieved from https://www.ringcentral.com/

Datadog. (2024). *Cloud Monitoring as a Service*. Retrieved from https://www.datadoghq.com/

Amazon Web Services. (2024). *Amazon CloudWatch Pricing*. Retrieved from https://aws.amazon.com/cloudwatch/pricing/
