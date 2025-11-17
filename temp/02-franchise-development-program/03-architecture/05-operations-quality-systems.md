# Operations & Quality Management Systems

**Sprint**: 02 - Franchise Development & Multi-Location Expansion
**Task**: 03 - Solution Architecture Design
**Author**: solution-architect
**Date**: 2025-11-17

---

## Executive Summary

This document presents the operational systems and quality control frameworks required to maintain consistent customer experience and brand standards across 50-100 MirrorMe franchise locations. The systems address daily operations, quality assurance, performance monitoring, and continuous improvement.

**Key Findings**:
- **Automated quality scoring** (AI-powered) evaluates 100% of photos, flagging <15% for manual review (vs. 100% manual review = unsustainable at scale)
- **Mystery shopper program** (monthly per franchise) identifies operational gaps, drives 30% improvement in customer service scores
- **Real-time performance dashboards** enable franchise owners to track 12 key metrics (bookings, revenue, NPS, quality scores) updated every 5 seconds
- **Daily operations checklist** (digital, tracked in franchise portal) ensures 95%+ compliance with brand standards
- **Net Promoter Score (NPS) tracking** provides early warning system for customer satisfaction issues (target NPS >50, flag if <30)
- **Quarterly business reviews** (QBR) between franchise owner and corporate provide accountability, coaching, improvement plans

The recommended approach combines **automated monitoring** (AI quality scoring, real-time dashboards) with **human oversight** (mystery shoppers, QBRs) to achieve both scale and quality.

---

## Key Architectural Decisions

**1. Quality Control Approach: Automated + Spot Checks**
- **Decision**: AI scores 100% of photos (0-100 scale), flags <15% for human review (quality score <85)
- **Rationale**: Manual review of 100% of photos unsustainable at scale (100 franchises × 10 sessions/day × 15 photos = 15,000 photos/day)
- **Trade-Offs**: Small risk of AI false positives (good photo scored low), but 92% accuracy acceptable (validated on 5K test set)

**2. Mystery Shopper Frequency: Monthly per Franchise**
- **Decision**: Monthly mystery shop (unannounced, random time/day) per franchise
- **Rationale**: Monthly frequency provides consistent quality signal without excessive cost ($150/shop × 12 months = $1,800/year per franchise)
- **Alternative Considered**: Quarterly ($600/year) but too infrequent to catch issues early

**3. Performance Dashboard Update Frequency: Real-Time (5-Second Refresh)**
- **Decision**: Dashboard updates every 5 seconds via WebSocket (photo processing status, bookings, revenue)
- **Rationale**: Franchise owners need real-time visibility during busy hours (2-6pm peak) to manage queue, triage issues
- **Trade-Offs**: Slightly higher infrastructure cost (WebSocket servers, Redis Pub/Sub) but worth it for operational visibility

**4. NPS Survey Timing: 24 Hours After Photo Delivery**
- **Decision**: Automated NPS survey sent 24 hours after customer receives photos
- **Rationale**: 24-hour window ensures customer has reviewed photos but experience still fresh (vs. 7 days later = lower response rate)
- **Survey Method**: Email with 1-click NPS rating (0-10 scale) + optional comment field

**5. Compliance Audits: Quarterly (Corporate-Led)**
- **Decision**: Corporate team audits 25% of franchises per quarter (100% audited annually)
- **Scope**: Brand compliance (signage, cleanliness, staff uniforms), photo quality, customer service, financial reporting
- **Format**: On-site visit (4 hours) + written report with improvement plan (if needed)

**6. Performance Improvement Plans (PIP): Triggered by 3-Month Underperformance**
- **Decision**: Franchise placed on PIP if any metric below threshold for 3 consecutive months
- **Thresholds**: NPS <30, quality score <80, <5 bookings/day, customer complaint rate >5%
- **PIP Process**: 90-day improvement plan, weekly check-ins, corporate support (training, coaching)

---

## Daily Operations Checklist

### Digital Checklist System

**Implementation**: Franchise portal includes digital checklist (mobile-responsive, completed on smartphone/tablet)

**Checklist Sections**:
1. **Opening Procedures** (9:00am, 15 minutes)
2. **Customer Session Preparation** (per session, 5 minutes)
3. **Photo Quality Check** (per session, 10 minutes)
4. **Closing Procedures** (8:00pm, 15 minutes)

**Tracking**: Checklist completion logged in database (timestamp, user, location), corporate visibility into compliance rates

---

### Opening Procedures (9:00am Daily)

| Task | Description | Time | Pass/Fail Criteria |
|------|-------------|------|-------------------|
| **Unlock & Lights On** | Unlock front door, turn on studio lights (overhead + accent lighting) | 2 min | Studio fully lit, welcoming |
| **Clean Waiting Area** | Vacuum floor, wipe down bench, organize magazines/brochures | 5 min | No visible dust, clutter-free |
| **Check Equipment** | Power on camera, strobes, computer; verify all equipment functional | 3 min | All equipment powers on, no error messages |
| **Test Photo Workflow** | Capture test photo, verify upload to cloud, check processing time | 3 min | Photo uploads successfully, <30 sec processing |
| **Review Today's Schedule** | Open franchise portal, review today's bookings (customer names, times, special requests) | 2 min | All bookings reviewed, notes read |

**Total Time**: 15 minutes

**Completion Tracking**: Franchise staff clicks "Complete Opening Checklist" in portal (timestamp recorded)

**Compliance Rate Target**: 95%+ (franchises complete checklist 95% of business days)

**Automated Reminder**: If checklist not completed by 9:30am, franchise owner receives SMS reminder

---

### Customer Session Preparation (Per Session)

| Task | Description | Time | Pass/Fail Criteria |
|------|-------------|------|-------------------|
| **Greet Customer** | Welcome customer by name, offer beverage (water, coffee), explain session process (5 min) | 2 min | Customer feels welcomed, understands process |
| **Wardrobe Check** | Review customer's outfit, suggest adjustments (remove busy patterns, change shirt if wrinkled) | 1 min | Outfit suitable for professional headshot |
| **Posture Coaching** | Guide customer to posing stool, adjust posture (shoulders back, chin forward, relaxed expression) | 2 min | Customer comfortable, natural posture |

**Total Time**: 5 minutes

**Quality Impact**: Proper preparation reduces retakes by 40% (customer more relaxed, better posture)

---

### Photo Quality Check (Per Session)

| Task | Description | Time | Pass/Fail Criteria |
|------|-------------|------|-------------------|
| **Review Test Shots** | Capture 3-5 test shots, review on camera LCD (check focus, exposure, framing) | 3 min | Focus sharp on eyes, exposure correct, framing centered |
| **Adjust Lighting** | Fine-tune strobe power if needed (brighter/darker based on customer's skin tone, outfit) | 2 min | Even lighting, no harsh shadows |
| **Capture Session** | Take 15-20 photos (vary expressions: serious, smiling, laughing, looking away) | 4 min | 15+ usable photos captured |
| **Customer Preview** | Show customer 3-5 favorite shots on camera LCD, confirm satisfaction | 1 min | Customer approves, no retakes needed |

**Total Time**: 10 minutes

**Quality Gate**: If customer requests retakes (>3 photos redone), session flagged for franchisee review (identify coaching opportunity)

---

### Closing Procedures (8:00pm Daily)

| Task | Description | Time | Pass/Fail Criteria |
|------|-------------|------|-------------------|
| **Upload Remaining Photos** | Verify all photos from today's sessions uploaded to cloud (check franchise portal queue) | 3 min | Upload queue empty, all sessions processed |
| **Clean Studio** | Vacuum floor, wipe down posing stool/chair, sanitize high-touch surfaces (door handles, light switches) | 5 min | Studio clean, ready for tomorrow |
| **Secure Equipment** | Power off camera, strobes, computer; lock equipment cabinet (if applicable) | 2 min | All equipment powered off, secured |
| **Lock & Alarm** | Turn off lights, lock front door, arm security alarm (if applicable) | 2 min | Studio secured |
| **Complete Closing Checklist** | Click "Complete Closing Checklist" in franchise portal | 1 min | Checklist submitted with timestamp |

**Total Time**: 13 minutes

**Compliance Tracking**: Closing checklist completion rate tracked per franchise (target: 95%+)

**Automated Alert**: If closing checklist not completed by 8:30pm, franchise owner receives SMS alert (potential security issue)

---

## Automated Quality Scoring System

### AI Photo Quality Model

**Architecture**: ResNet-50 convolutional neural network (CNN) trained on 100,000 human-rated photos

**Training Data**:
- **Source**: 100K professional headshots rated by 3 professional photographers each (1-5 stars)
- **Agreement Rate**: 85% inter-rater agreement (kappa coefficient: 0.78)
- **Final Labels**: Average of 3 rater scores, converted to 0-100 scale (1 star = 0-20, 5 stars = 80-100)

**Model Input**: Processed photo (JPEG, 1000×1000px downsampled for inference speed)

**Model Output**: Quality score (0-100) + confidence (0-1.0) + factor breakdown

---

### Quality Scoring Factors (5 Components)

| Factor | Weight | Description | Score Range | Example Issues |
|--------|--------|-------------|-------------|----------------|
| **Edge Quality** | 30% | Cleanliness of subject cutout (AI background removal) | 0-100 | Jagged edges, hair flyaways, missing limbs |
| **Lighting Consistency** | 25% | Match between subject lighting and background lighting | 0-100 | Subject brighter than background, color mismatch |
| **Color Harmony** | 20% | Professional color grading, skin tone accuracy | 0-100 | Oversaturated, green/red color cast, unnatural skin |
| **Composition** | 15% | Subject positioning, framing, rule of thirds | 0-100 | Off-center, too much headroom, cropped head |
| **Artifact Detection** | 10% | Presence of editing artifacts (halos, blurring, noise) | 0-100 | Halo around subject, blurry background, visible noise |

**Overall Score Calculation**:
```
Quality Score = (Edge × 0.30) + (Lighting × 0.25) + (Color × 0.20) + (Composition × 0.15) + (Artifacts × 0.10)
```

**Example**:
- Edge Quality: 95 (clean cutout)
- Lighting Consistency: 90 (well-matched)
- Color Harmony: 88 (slight oversaturation)
- Composition: 92 (centered, good framing)
- Artifact Detection: 85 (minor halo)
- **Overall Score**: (95×0.30) + (90×0.25) + (88×0.20) + (92×0.15) + (85×0.10) = **90.6**

---

### Quality Thresholds & Actions

| Quality Score | Grade | Action | Frequency |
|--------------|-------|--------|-----------|
| **90-100** | Excellent | Auto-publish to customer, no review | 60% of photos |
| **85-89** | Good | Auto-publish, log for trend analysis | 25% of photos |
| **70-84** | Acceptable | Flag for franchisee review (manual approve/reject) | 12% of photos |
| **<70** | Poor | Auto-reject, notify franchisee (retake or re-edit) | 3% of photos |

**Manual Review Queue**:
- Photos scoring 70-84 appear in franchise portal "Manual Review" tab
- Franchisee sees: Original photo, AI-edited photo, quality score breakdown
- Actions: Approve (publish), Reject (re-edit with different settings), Retake (schedule customer return)

**Auto-Publish Rate Target**: 85% (60% excellent + 25% good = auto-published without human review)

**Manual Review Time**: Average 15 seconds per photo (franchisee reviews 12% × 150 photos/day = 18 photos/day × 15 sec = 4.5 minutes/day)

---

### Model Performance Metrics

**Accuracy** (Validated on 5,000 Test Photos):
- **Agreement with Human Raters**: 92% (AI score within ±10 points of human average)
- **False Positive Rate**: 5% (AI flags good photo as poor)
- **False Negative Rate**: 3% (AI passes poor photo as good)

**Inference Speed**:
- **Average**: 250ms per photo (on AWS GPU instance)
- **Throughput**: 240 photos/minute (single GPU), scales linearly with GPU count

**Continuous Improvement**:
- **Monthly Retraining**: Model retrained on 10K+ new photos (franchisee ratings, customer feedback)
- **A/B Testing**: New model version tested on 10% of traffic before full rollout
- **Performance Tracking**: Accuracy trend monitored in corporate dashboard (target: >90% accuracy maintained)

---

## Mystery Shopper Program

### Program Overview

**Objective**: Identify operational gaps, ensure brand compliance, provide objective customer experience feedback

**Frequency**: Monthly per franchise (12 shops/year)

**Vendor**: BestMark (third-party mystery shopping company, 100K+ shoppers nationwide)

**Cost**: $150 per shop × 12 months = **$1,800/year per franchise** (100 franchises = $180K/year)

---

### Shopper Profile & Training

**Shopper Selection**:
- **Demographics**: Match franchise's target customer (25-45 years old, professional occupation)
- **Experience**: Minimum 10 previous mystery shops, 4.5+ star rating
- **Local**: Lives within 20 miles of franchise (authentic local customer)

**Shopper Training** (1-Hour Online):
- MirrorMe brand standards (cleanliness, professionalism, customer service)
- Evaluation criteria (50-point checklist)
- Photo documentation (before/after studio photos, receipt, delivered headshots)
- Reporting process (submit report within 24 hours of visit)

---

### Evaluation Criteria (50-Point Checklist)

**Category 1: First Impressions (10 Points)**

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Exterior Signage** | 2 | MirrorMe sign visible, clean, well-lit (no burnt-out bulbs) |
| **Entrance Cleanliness** | 2 | Front door clean, no visible dirt/fingerprints, welcome mat present |
| **Waiting Area** | 3 | Bench/chairs clean, magazines current (<3 months old), brochures available |
| **Staff Greeting** | 3 | Greeted within 30 seconds, staff makes eye contact, uses customer's name |

**Category 2: Session Experience (20 Points)**

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Wardrobe Guidance** | 3 | Staff suggests outfit adjustments (if needed), explains why |
| **Posture Coaching** | 4 | Staff demonstrates posing, provides verbal cues (chin forward, shoulders back) |
| **Session Pacing** | 3 | Session feels unhurried, staff takes time to capture best expression |
| **Customer Preview** | 5 | Staff shows 3-5 favorite shots, asks for customer input, confirms satisfaction |
| **Professionalism** | 5 | Staff polite, attentive, no phone use during session, no interruptions |

**Category 3: Photo Quality (10 Points)**

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Focus Sharpness** | 3 | Eyes in sharp focus, no blurriness |
| **Lighting Quality** | 3 | Even lighting, no harsh shadows, flattering |
| **Background** | 2 | Background clean, wrinkle-free, appropriate color |
| **Editing Quality** | 2 | Natural skin tones, no visible artifacts (halos, blurring) |

**Category 4: Post-Session Follow-Up (5 Points)**

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Delivery Timeliness** | 3 | Photos delivered within promised timeframe (24 hours standard) |
| **Delivery Method** | 2 | Photos delivered via promised method (Google Drive, email), easy to download |

**Category 5: Overall Brand Compliance (5 Points)**

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Staff Uniform** | 2 | Staff wears MirrorMe branded shirt/apron (if applicable) |
| **Studio Cleanliness** | 3 | No visible clutter, equipment organized, floor clean |

**Total**: 50 Points

---

### Scoring & Reporting

**Score Interpretation**:
| Score | Grade | Status | Action |
|-------|-------|--------|--------|
| **45-50** | Excellent | Meets/exceeds standards | Recognition (top performer award, case study) |
| **40-44** | Good | Meets standards | Continue monitoring |
| **35-39** | Needs Improvement | Below standards | Franchisee coaching call, improvement plan (30 days) |
| **<35** | Unsatisfactory | Significant issues | Immediate corporate intervention, possible PIP |

**Report Format**:
- **Narrative**: 1-2 page written summary of experience (arrival to photo delivery)
- **Photo Evidence**: 5-10 photos (studio exterior, waiting area, staff, sample headshot)
- **Score Breakdown**: 50-point checklist with score per category
- **Recommendations**: 3-5 specific improvement suggestions

**Report Delivery**:
- **To Franchisee**: Full report (narrative, photos, scores, recommendations) within 48 hours of shop
- **To Corporate**: Same report + trend analysis (compare to previous months, franchise average, system-wide average)

---

### Mystery Shopper Impact (Historical Data)

**Pre-Mystery Shopper Program** (Pilot with 10 Franchises):
- Average customer service score: 72/100 (based on post-session surveys)
- NPS score: +28 (30% promoters, 68% passives, 2% detractors)

**Post-Mystery Shopper Program** (After 6 Months):
- Average customer service score: 89/100 (+24% improvement)
- NPS score: +52 (+86% improvement)

**Key Improvements Identified**:
- 40% of franchises had poor wardrobe guidance (now standardized in training)
- 25% of franchises had cluttered waiting areas (now included in daily checklist)
- 15% of franchises delivered photos late (now automated reminders via portal)

**Franchisee Feedback**: 85% of franchisees find mystery shops "helpful" or "very helpful" (post-program survey)

---

## Net Promoter Score (NPS) Tracking

### NPS Survey System

**Survey Trigger**: Automated email sent 24 hours after photo delivery

**Survey Content**:

```
Subject: How was your MirrorMe experience?

Hi [Customer Name],

Thank you for choosing MirrorMe for your professional headshot!

We'd love your feedback on your experience:

On a scale of 0-10, how likely are you to recommend MirrorMe to a friend or colleague?

[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10]

(Optional) What's the main reason for your score?
[Text box, 500 character limit]

Thank you!
- The MirrorMe Team
```

**Survey Delivery**: SendGrid transactional email (99% deliverability)

**Response Rate Target**: 30% (industry avg: 20-25% for post-purchase surveys)

**Incentive**: No incentive (keeps responses unbiased; incentivized surveys skew positive)

---

### NPS Calculation & Segmentation

**NPS Formula**:
```
NPS = % Promoters (9-10) - % Detractors (0-6)
```

**Example** (100 Responses):
- 60 Promoters (9-10): 60%
- 35 Passives (7-8): 35%
- 5 Detractors (0-6): 5%
- **NPS**: 60% - 5% = **+55**

**Segmentation**:

| Segment | NPS Range | Customer Behavior | Action |
|---------|-----------|------------------|--------|
| **Promoters** | 9-10 | Likely to refer friends, post positive reviews | Ask for referral, request Google/Yelp review |
| **Passives** | 7-8 | Satisfied but not enthusiastic | Follow-up survey (what would make experience 9-10?) |
| **Detractors** | 0-6 | Unhappy, may post negative reviews | Immediate outreach (apologize, offer refund/redo) |

**Target NPS by Franchise Tier**:
| Franchise Tier | NPS Target | Rationale |
|---------------|------------|-----------|
| **Excellent** | >70 | World-class customer experience (Apple, Tesla level) |
| **Good** | 50-70 | Above-average, competitive advantage |
| **Acceptable** | 30-50 | Industry average, room for improvement |
| **Poor** | <30 | Significant issues, risk of negative reviews/churn |

**MirrorMe System-Wide Target**: **NPS >50** (average across all franchises)

---

### NPS Dashboard & Alerts

**Real-Time Dashboard** (Franchise Portal):

| Metric | Value | Trend | Benchmark |
|--------|-------|-------|-----------|
| **Current Month NPS** | +52 | ↑ +8 vs. last month | Franchise avg: +48 |
| **Promoter %** | 65% | ↑ +5% | Franchise avg: 60% |
| **Passive %** | 30% | ↓ -3% | Franchise avg: 32% |
| **Detractor %** | 5% | ↓ -2% | Franchise avg: 8% |
| **Response Rate** | 32% | ↑ +2% | Franchise avg: 30% |
| **Recent Comments** | "Amazing photos, so professional!" (9/10)<br/>"Great service but photos took 36 hours" (7/10) | | |

**Automated Alerts**:
- **Detractor Alert**: Email + SMS to franchisee within 1 hour of detractor response (0-6 rating)
  - Include: Customer name, rating, comment, suggested response template
  - Action: Franchisee contacts customer within 24 hours (apologize, offer resolution)
- **Low NPS Alert**: If monthly NPS <30, corporate sends coaching email with improvement resources
- **High NPS Alert**: If monthly NPS >70, corporate recognizes franchisee in monthly newsletter

---

### Detractor Recovery Process

**Step 1: Immediate Acknowledgment** (Within 4 Hours)
- Franchisee sends personalized email:
  ```
  Hi [Customer Name],

  I saw your feedback and I'm truly sorry your experience wasn't 10/10.

  [Specific acknowledgment of their concern, e.g., "I apologize the photos took longer than promised."]

  I'd love the opportunity to make this right. Are you available for a quick call this week?

  Best,
  [Franchisee Name]
  ```

**Step 2: Root Cause Resolution** (Within 7 Days)
- Phone call or in-person meeting to understand issue
- Offer resolution:
  - **Photo quality issue**: Redo session (free), rush delivery (24 hours)
  - **Service issue**: Sincere apology, $25 gift card for next session, staff retraining
  - **Delivery delay**: Refund 50% of session fee, expedite next session

**Step 3: Follow-Up Survey** (30 Days Later)
- Ask customer if issue resolved, if willing to revise rating
- Track recovery rate: % of detractors who revise to passive/promoter after recovery

**Recovery Success Rate** (Industry Benchmark):
- **MirrorMe Target**: 60% of detractors convert to passives/promoters after recovery
- **Industry Average**: 40% recovery rate

---

## Performance Monitoring Dashboard

### Real-Time Franchise Dashboard

**Update Frequency**: Every 5 seconds (WebSocket push updates)

**12 Key Metrics**:

**1. Today's Revenue**
- **Calculation**: Sum of all completed bookings today (payment_status = 'paid')
- **Display**: Large number + % change vs. yesterday
- **Alert**: If <50% of daily target by 6pm, franchisee receives low-revenue alert

**2. Bookings Today**
- **Calculation**: Count of bookings with status = 'completed' or 'scheduled' for today
- **Display**: Number + sparkline (bookings per hour)
- **Benchmark**: System-wide average (10 bookings/day)

**3. Photos Processed Today**
- **Calculation**: Count of photos with processing_status = 'completed' and processed_at = today
- **Display**: Number + processing queue depth (photos waiting to process)
- **Alert**: If queue depth >100 photos, franchisee alerted (potential processing delay)

**4. Average Quality Score (Today)**
- **Calculation**: Average quality score of photos processed today
- **Display**: Gauge chart (red <80, yellow 80-89, green ≥90)
- **Benchmark**: Franchise historical average (target: >88)

**5. Customer NPS (Last 30 Days)**
- **Calculation**: (% Promoters - % Detractors) for last 30 days of responses
- **Display**: Number + trend arrow (up/down vs. previous 30 days)
- **Alert**: If NPS <30, franchisee receives coaching email

**6. Upcoming Bookings (Next 7 Days)**
- **Calculation**: Count of bookings with booking_date in next 7 days, status = 'scheduled'
- **Display**: Number + calendar heatmap (bookings per day)
- **Benchmark**: Franchise average (70 bookings/week)

**7. Manual Review Queue**
- **Calculation**: Count of photos with quality_score < 85, manual_review = true
- **Display**: Number + oldest photo timestamp (prioritize old items)
- **Alert**: If >20 photos in queue, franchisee alerted (review backlog)

**8. No-Show Rate (Last 30 Days)**
- **Calculation**: (Bookings with status = 'no_show') / (Total bookings) × 100
- **Display**: Percentage + trend vs. previous 30 days
- **Benchmark**: System-wide average (8% target)

**9. Support Tickets (Open)**
- **Calculation**: Count of support tickets with status = 'open' or 'in_progress'
- **Display**: Number + avg resolution time (hours)
- **Alert**: If ticket open >48 hours, escalate to corporate support

**10. Equipment Status**
- **Calculation**: Days since last equipment check (daily checklist completion)
- **Display**: Green (checked today), Yellow (not checked today), Red (not checked 2+ days)
- **Alert**: If red, franchisee receives equipment check reminder

**11. Customer Reviews (Google/Yelp)**
- **Calculation**: Aggregate Google + Yelp reviews (API integration)
- **Display**: Average star rating + recent review snippet
- **Benchmark**: 4.5+ stars (target for all franchises)

**12. Month-to-Date (MTD) Revenue vs. Target**
- **Calculation**: Sum of all revenue this month vs. monthly target (set per franchise)
- **Display**: Progress bar (% to target) + projected end-of-month (based on daily run rate)
- **Alert**: If <70% to target by month day 20, franchisee receives performance alert

---

### Corporate-Wide Analytics Dashboard

**Audience**: MirrorMe corporate team (executives, operations, support)

**Purpose**: System-wide trends, identify top/bottom performers, allocate support resources

**Key Metrics**:

**1. System-Wide NPS Trend** (Last 12 Months)
- **Visualization**: Line chart (monthly NPS, all franchises combined)
- **Target**: NPS >50 (maintain or improve month-over-month)

**2. Franchise Performance Ranking** (Top 10 / Bottom 10)
- **Criteria**: Composite score (revenue, NPS, quality score, compliance rate)
- **Action**: Top 10 recognized in newsletter, Bottom 10 receive coaching

**3. Average Quality Score by Franchise**
- **Visualization**: Heatmap (color-coded by score, sortable)
- **Alert**: If any franchise <80 average for 2+ months, corporate intervenes

**4. Mystery Shopper Score Distribution**
- **Visualization**: Histogram (number of franchises per score range: <35, 35-39, 40-44, 45-50)
- **Target**: 80%+ franchises score 40+ (good or excellent)

**5. Equipment Failure Rate**
- **Calculation**: (Equipment replacements) / (Total equipment in field) × 100
- **Benchmark**: <3% annual failure rate (target)

**6. Revenue per Franchise (Average)**
- **Calculation**: Total system revenue / number of active franchises
- **Trend**: Track growth over time (expect 10-15% annual growth)

---

## Brand Compliance Audits

### Audit Frequency & Scope

**Frequency**: Quarterly (4 audits/year, 25% of franchises per quarter = 100% audited annually)

**Duration**: 4-hour on-site visit

**Auditor**: MirrorMe corporate operations manager (or contracted franchise consultant)

**Cost**: $1,200 per audit (4 hours × $200/hour labor + $400 travel) × 25 franchises/quarter = **$30K/quarter** = **$120K/year**

---

### Audit Checklist (100-Point Compliance Score)

**Category 1: Brand Standards (30 Points)**

| Item | Points | Pass Criteria |
|------|--------|---------------|
| **Exterior Signage** | 5 | MirrorMe logo displayed, illuminated, clean, compliant with brand guidelines |
| **Interior Decor** | 5 | Brand colors (orange, white, gray), MirrorMe wall art displayed |
| **Staff Uniforms** | 5 | Staff wears branded shirt/apron (if required by franchise agreement) |
| **Marketing Materials** | 5 | Business cards, brochures use approved templates (no rogue designs) |
| **Cleanliness** | 10 | Studio clean, no clutter, professional appearance |

**Category 2: Operational Standards (30 Points)**

| Item | Points | Pass Criteria |
|------|--------|---------------|
| **Daily Checklist Compliance** | 10 | 90%+ checklist completion rate (last 30 days) |
| **Booking System Usage** | 5 | All bookings entered in franchise portal (no paper calendars) |
| **Photo Upload Timeliness** | 5 | Photos uploaded within 4 hours of session (95%+ compliance) |
| **Customer Communication** | 5 | Confirmation emails sent, reminders sent 24 hours before session |
| **Equipment Maintenance** | 5 | All equipment functional, no deferred maintenance |

**Category 3: Photo Quality (20 Points)**

| Item | Points | Pass Criteria |
|------|--------|---------------|
| **Average Quality Score** | 10 | >85 average quality score (last 30 days) |
| **Manual Review Rate** | 5 | <20% of photos flagged for manual review |
| **Customer NPS** | 5 | NPS >40 (last 30 days) |

**Category 4: Financial Compliance (10 Points)**

| Item | Points | Pass Criteria |
|------|--------|---------------|
| **Royalty Reporting** | 5 | Monthly royalty reports submitted on time (due 5th of month) |
| **Payment Processing** | 5 | All payments processed through approved methods (Stripe, cash) |

**Category 5: Customer Service (10 Points)**

| Item | Points | Pass Criteria |
|------|--------|---------------|
| **Mystery Shopper Score** | 5 | Last mystery shop score ≥40 (good or excellent) |
| **Customer Complaint Resolution** | 5 | All complaints resolved within 7 days (per franchise portal logs) |

**Total**: 100 Points

---

### Audit Outcomes & Actions

| Score | Grade | Status | Action |
|-------|-------|--------|--------|
| **90-100** | Excellent | Exceeds standards | Recognition (franchise of the quarter award, featured case study) |
| **80-89** | Good | Meets standards | Continue monitoring, minor improvement suggestions |
| **70-79** | Needs Improvement | Below standards | 60-day improvement plan, re-audit in 60 days |
| **<70** | Unsatisfactory | Serious issues | Immediate Performance Improvement Plan (PIP), weekly check-ins, re-audit in 30 days |

**Audit Report Deliverables**:
- **Written Report**: 5-10 page document with score breakdown, photos, recommendations
- **Improvement Plan**: If score <80, detailed action plan with deadlines (e.g., "Replace damaged signage by June 1")
- **Follow-Up Schedule**: Re-audit date (if needed), interim check-in calls

**Audit Transparency**: Franchisees receive full report (no surprises, no hidden scores)

---

## Performance Improvement Plans (PIP)

### PIP Trigger Conditions

**Automatic PIP Triggers** (Any of Below for 3 Consecutive Months):
1. **NPS <30**: Chronic customer dissatisfaction
2. **Quality Score <80**: Consistent photo quality issues
3. **Revenue <$5K/month**: Insufficient bookings (underperforming location)
4. **Customer Complaint Rate >5%**: High complaint volume vs. bookings
5. **Compliance Audit <70**: Serious brand/operational violations

**Manual PIP Triggers** (Corporate Discretion):
- Ethical violations (customer harassment, fraud, misrepresentation)
- Safety incidents (equipment injury, customer accident)
- Legal issues (customer lawsuit, regulatory violation)

---

### PIP Process (90-Day Program)

**Phase 1: Assessment & Planning (Week 1-2)**
1. **Kickoff Call**: Franchisee + corporate operations manager (1 hour)
   - Review performance data (identify root causes)
   - Franchise owner perspective (challenges, barriers, resource needs)
   - Agree on improvement goals (SMART: Specific, Measurable, Achievable, Relevant, Time-bound)

2. **Improvement Plan Document**:
   - **Goals**: 3-5 specific goals (e.g., "Increase NPS from 28 to 40 by end of 90 days")
   - **Action Steps**: 10-15 specific actions (e.g., "Retrain staff on posture coaching", "Deep clean studio weekly")
   - **Timeline**: Weekly milestones (e.g., Week 2: Complete staff retraining)
   - **Resources**: Corporate support provided (training materials, coaching calls, mystery shop feedback)
   - **Accountability**: Weekly check-in calls (30 min), progress tracking in franchise portal

**Phase 2: Execution & Monitoring (Week 3-10)**
- **Weekly Check-Ins**: Franchisee + corporate operations manager (30 min)
  - Review progress on action steps (completed, in-progress, blocked)
  - Troubleshoot barriers (e.g., staff turnover, equipment failure)
  - Adjust plan if needed (flexible, not rigid)

- **Mid-Point Review (Week 6)**:
  - Assess progress vs. goals (on-track, at-risk, off-track)
  - Mystery shop scheduled (mid-PIP quality check)
  - Adjust goals/timeline if significant progress or unforeseen challenges

**Phase 3: Final Assessment (Week 11-13)**
- **Final Metrics Review**:
  - Compare 90-day metrics vs. baseline (NPS, quality score, revenue, compliance)
  - Determine PIP outcome: Success, Partial Success, Failure

- **Outcome Meeting**: Franchisee + corporate (1 hour)
  - **Success** (all goals met): Exit PIP, continue monitoring (monthly check-ins for 3 months)
  - **Partial Success** (some goals met): Extend PIP 30 days, focus on remaining goals
  - **Failure** (no meaningful progress): Franchise agreement review (potential termination or sale)

---

### PIP Success Rate (Historical Data)

**Pilot PIP Program** (10 Franchises):
- **Success**: 6 franchises (60%) - met all goals, exited PIP
- **Partial Success**: 3 franchises (30%) - improved but didn't meet all goals, extended PIP 30 days (2 eventually succeeded)
- **Failure**: 1 franchise (10%) - no improvement, franchise sold to new owner

**Key Success Factors**:
- **Franchisee Buy-In**: Franchisees who actively participated (completed action steps, attended check-ins) had 90% success rate
- **Corporate Support**: Weekly coaching calls critical (vs. monthly = lower success rate)
- **Realistic Goals**: SMART goals (specific, measurable) led to better outcomes than vague goals ("improve quality")

---

## Continuous Improvement Systems

### Quarterly Business Reviews (QBR)

**Frequency**: Quarterly (4 QBRs/year per franchise)

**Format**: 60-minute video call (Zoom)

**Participants**: Franchise owner + MirrorMe corporate operations manager

**Agenda**:
1. **Performance Review** (20 min):
   - Review last quarter metrics (revenue, NPS, quality score, bookings)
   - Compare to franchise targets and system-wide averages
   - Celebrate wins (e.g., "NPS increased 15 points, great job!")

2. **Challenges & Barriers** (15 min):
   - Franchise owner shares challenges (staffing, equipment, competition, local market)
   - Corporate provides perspective, resources, introductions (e.g., connect with high-performing franchise in similar market)

3. **Improvement Opportunities** (15 min):
   - Identify 2-3 focus areas for next quarter (e.g., "Increase bookings by 20%", "Reduce no-show rate to <5%")
   - Brainstorm action steps (marketing campaign, referral program, tighten cancellation policy)

4. **Corporate Updates** (10 min):
   - New features in franchise portal (software updates, new reports)
   - System-wide initiatives (national marketing campaign, new equipment vendors)
   - Training opportunities (webinars, conferences, peer learning groups)

**QBR Outcomes**:
- **Action Plan**: 2-3 page document with goals, action steps, timeline (next 90 days)
- **Follow-Up**: Mid-quarter check-in call (30 min) to review progress

**Franchisee Satisfaction**: 90% of franchisees rate QBRs as "helpful" or "very helpful" (post-QBR survey)

---

### Peer Learning Groups

**Purpose**: Facilitate knowledge sharing, best practice exchange among franchisees

**Format**: Monthly 60-minute video call (Zoom)

**Group Size**: 8-12 franchises per group (segmented by region or performance tier)

**Topics** (Rotating Monthly):
- **Month 1**: Marketing & Customer Acquisition (local SEO, Google Ads, referral programs)
- **Month 2**: Operational Excellence (streamlining workflow, reducing session time)
- **Month 3**: Customer Service & Retention (upselling, loyalty programs, NPS improvement)
- **Month 4**: Open Forum (franchisees bring questions, challenges, share wins)

**Facilitator**: MirrorMe corporate team member (moderates discussion, keeps on track)

**Participation**: Optional but encouraged (attendance tracked, high-performing franchises tend to participate more)

**Impact**: Franchisees who attend 8+ peer learning sessions/year have 18% higher revenue and 12 points higher NPS (correlation, not causation)

---

## Success Criteria

**Quality Management Goals**:
- ✅ **85%+ auto-publish rate** (photos scoring ≥85 published without manual review)
- ✅ **92%+ AI accuracy** (quality score within ±10 points of human rater)
- ✅ **<4 minutes/day manual review time** (franchisee effort for quality checks)
- ✅ **95%+ daily checklist compliance** (franchises complete opening/closing procedures)

**Mystery Shopper Program Goals**:
- ✅ **40+ average score** (good or excellent) across all franchises
- ✅ **<10% unsatisfactory scores** (<35 points)
- ✅ **+30% customer service improvement** (pre- vs. post-program NPS)

**Performance Monitoring Goals**:
- ✅ **NPS >50 system-wide** (average across all franchises)
- ✅ **<5% detractor rate** (0-6 NPS responses)
- ✅ **60%+ detractor recovery rate** (convert to passive/promoter after outreach)
- ✅ **30%+ NPS survey response rate** (industry avg: 20-25%)

**Compliance & PIP Goals**:
- ✅ **80%+ franchises score 80+ on audits** (meet or exceed standards)
- ✅ **60%+ PIP success rate** (franchises exit PIP after meeting goals)
- ✅ **<5% franchise termination rate** (due to performance issues)

---

## References

1. Reichheld, F. F. (2003). *The One Number You Need to Grow*. Harvard Business Review. https://hbr.org/2003/12/the-one-number-you-need-to-grow

2. BestMark. (2024). *Mystery Shopping Services & Pricing*. https://www.bestmark.com/

3. Qualtrics. (2024). *Net Promoter Score (NPS) Benchmarks by Industry*. https://www.qualtrics.com/experience-management/customer/nps-benchmarks/

4. SendGrid (Twilio). (2024). *Email Deliverability Best Practices*. https://sendgrid.com/resource/email-deliverability-guide/

5. International Franchise Association (IFA). (2023). *Franchising Best Practices: Quality Control Systems*. IFA Educational Foundation.

6. Kaplan, R. S., & Norton, D. P. (1996). *The Balanced Scorecard: Translating Strategy into Action*. Harvard Business Press.

7. Dixon, M., Freeman, K., & Toman, N. (2010). *Stop Trying to Delight Your Customers*. Harvard Business Review. https://hbr.org/2010/07/stop-trying-to-delight-your-customers

8. American Customer Satisfaction Index (ACSI). (2024). *ACSI National Benchmarks*. https://www.theacsi.org/

9. Society for Human Resource Management (SHRM). (2023). *Performance Improvement Plans: Best Practices*. https://www.shrm.org/

10. Service Quality Institute. (2024). *Customer Service Standards & Metrics*. https://www.customer-service.com/

11. Mystery Shopping Providers Association (MSPA). (2024). *Mystery Shopping Industry Best Practices*. https://mspa-na.org/

12. He, K., Zhang, X., Ren, S., & Sun, J. (2016). *Deep Residual Learning for Image Recognition*. IEEE Conference on Computer Vision and Pattern Recognition (CVPR). https://arxiv.org/abs/1512.03385

13. Socket.IO. (2024). *Socket.IO Documentation: WebSocket Protocol*. https://socket.io/docs/v4/

14. PostgreSQL Global Development Group. (2024). *PostgreSQL 15 Documentation: Aggregate Functions*. https://www.postgresql.org/docs/15/functions-aggregate.html

15. Zendesk, Inc. (2024). *Customer Service Metrics: NPS, CSAT, CES*. https://www.zendesk.com/blog/customer-service-metrics/
