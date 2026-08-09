#!/usr/bin/env python3
"""Generate evidence-based benefit landing pages for BookMyClinics."""

from pathlib import Path
import re
from datetime import date

ROOT = Path("/workspace")
OUT = ROOT / "landings" / "benefits"
OUT.mkdir(parents=True, exist_ok=True)

TODAY = date.today().isoformat()

# Shared source registry (short keys used in pages)
SOURCES = {
    "zhao2017": {
        "label": "Zhao et al., Journal of Medical Internet Research (2017)",
        "detail": "Systematic review of 36 articles covering 21 web-based medical appointment systems.",
        "url": "https://www.jmir.org/2017/4/e134",
    },
    "wang2024": {
        "label": "Wang & Lin, digital self-scheduling meta-analysis (Research Square preprint)",
        "detail": "Meta-analysis of 18 observational hospital outpatient studies on digital self-scheduling.",
        "url": "https://doi.org/10.21203/rs.3.rs-4243854/v1",
    },
    "frontiers2025": {
        "label": "Frontiers in Digital Health (2025)",
        "detail": "Observational analysis of online appointment scheduling in a medical practice and a university hospital (16,894 practice appointments; 81,173 hospital appointments).",
        "url": "https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1567397/full",
    },
    "gallo2024": {
        "label": "Gallo et al., JMIR (2024) — EHR Fast Pass self-rescheduling",
        "detail": "Retrospective cohort on automated self-rescheduling; median access improvement of 14 days when patients accepted earlier slots.",
        "url": "https://www.jmir.org/2024/1/e52071",
    },
    "sutter2020": {
        "label": "Martinez et al., JMIR / PMC (2020) — patient-centric Fast Pass scheduling",
        "detail": "Retrospective case-control analysis: no-shows fell 1.3 percentage points (38% relative reduction) among patients who accepted earlier-slot offers.",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7315363/",
    },
    "swiftqueue2024": {
        "label": "Imperial College Healthcare NHS Trust / Swiftqueue evaluation (Studies in Health Technology and Informatics)",
        "detail": "Retrospective analysis of 14,122 plain-film X-ray referrals (Jan–Jun 2024): DNA rate 12.1% → 3.1%; ~20 admin hours/week saved.",
        "url": "https://doi.org/10.3233/shti260505",
    },
    "jrms2023": {
        "label": "Journal of Research in Medical Sciences (2023)",
        "detail": "Orthopedic outpatient comparison of web-based self-scheduling vs traditional staff scheduling; notes greater patient autonomy and less office-staff burden.",
        "url": "https://journals.lww.com/jrms/fulltext/2023/04060/the_effect_of_outpatient_web_based_online.6.aspx",
    },
    "wood2023": {
        "label": "Healthcare Review / mammography self-scheduling study (2023)",
        "detail": "Single-institution experience: after EHR-tethered online scheduling optimization, online screening mammography self-scheduling rose 26-fold with a concurrent ~16× reduction in patient-access-specialist scheduling engagement.",
        "url": "https://doi.org/10.36502/2023/hcr.6222",
    },
    "northwestern2024": {
        "label": "Northwestern Medicine self-scheduling program description (Health Services Research & Managerial Epidemiology, 2024)",
        "detail": "Multisite, multispecialty practice reported 733,651 successfully self-scheduled completed visits in 2023 across seven self-schedule / self-reschedule processes.",
        "url": "https://doi.org/10.1177/23333928241271933",
    },
}

IMAGES = [
    "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=2000&q=80",
    "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=2000&q=80",
    "https://images.unsplash.com/photo-1631815588090-d4bfec5b1ccb?auto=format&fit=crop&w=2000&q=80",
    "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=2000&q=80",
    "https://images.unsplash.com/photo-1666213288397-ce381c62c2f0?auto=format&fit=crop&w=2000&q=80",
    "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?auto=format&fit=crop&w=2000&q=80",
]

BENEFITS = [
    {
        "slug": "fewer-no-shows",
        "nav": "Evidence",
        "title": "Fewer Missed Appointments | BookMyClinics",
        "meta": "Peer-reviewed evidence shows online medical appointment booking often reduces no-show rates versus phone scheduling.",
        "h1": "Fewer missed appointments, documented in research",
        "lead": "Across published clinic and system studies, web-based booking is repeatedly linked with lower no-show rates than traditional phone booking.",
        "cta_primary": ("See how clinics go live", "https://bookmyclinics.com/landings/lp-register.html"),
        "cta_secondary": ("Read all benefits", "./"),
        "sections": [
            {
                "h2": "What the evidence shows",
                "p": (
                    "Missed appointments waste clinic capacity and delay care for other patients. "
                    "A Journal of Medical Internet Research systematic review of web-based medical appointment systems "
                    "found that many practices report lower no-show rates after adopting online scheduling. "
                    "Concrete comparisons in that review include Tricare web scheduling at a 2% no-show rate versus 8% for phone scheduling, "
                    "and Murray Hill Medical Group reporting under 1% missed web appointments versus about 8% for phone appointments. "
                    "Other programs in the same review reported large relative reductions — for example, Patient Online (−42%) and "
                    "Dartmouth-Hitchcock’s messaging-based appointment management (−40%)."
                ),
                "facts": [
                    "Tricare: 2% no-show online vs 8% phone (cited in Zhao et al., JMIR 2017).",
                    "Murray Hill Medical Group: &lt;1% missed web appointments vs ~8% phone (JMIR 2017 review).",
                    "Patient Online: 42% reduction in no-shows (Walters et al., cited in JMIR 2017).",
                    "Meta-analysis of hospital outpatient digital self-scheduling: lower no-show odds (OR 0.70; 95% CI 0.57–0.85).",
                ],
            },
            {
                "h2": "More recent practice data",
                "p": (
                    "A 2025 Frontiers in Digital Health study compared online versus offline booking in a medical practice and a university hospital. "
                    "In the practice setting, the median no-show rate was 1.8% for online bookings versus 5.9% for offline bookings. "
                    "Separately, an NHS Trust evaluation of a digital appointment platform for plain-film X-ray referrals reported DNA "
                    "(did-not-attend) rates falling from 12.1% to 3.1% — a 74% reduction — after digital scheduling replaced manual processes. "
                    "Results can vary by setting: the same Frontiers paper found a different pattern in a referral-heavy university hospital, "
                    "which is why clinics should treat published figures as evidence of potential, not a guaranteed outcome for every specialty."
                ),
                "facts": [
                    "Practice OAS no-shows: median 1.8% online vs 5.9% offline (Frontiers 2025).",
                    "NHS Swiftqueue evaluation: DNA 12.1% → 3.1% across 14,122 referrals.",
                    "Hospital contexts can differ; reminders remained valuable even where OAS alone was less protective.",
                ],
            },
            {
                "h2": "Why online booking can reduce no-shows",
                "p": (
                    "Researchers do not claim a single magic mechanism. The JMIR review notes that lower no-shows may reflect easier verification, "
                    "cancellation, and rescheduling — plus a greater sense of ownership when patients choose their own slot. "
                    "Patient-centric systems that let people move into earlier openings have also been shown to cut missed visits: "
                    "in a Sutter Health Fast Pass analysis, accepting an earlier slot was associated with a 1.3 percentage-point drop in no-shows "
                    "(about a 38% relative reduction)."
                ),
                "facts": [
                    "Easier cancel/reschedule access is a leading proposed mechanism (JMIR 2017).",
                    "Fast Pass acceptors: −1.3 pp no-shows / ~38% relative reduction (Martinez et al., 2020).",
                ],
            },
            {
                "h2": "How BookMyClinics puts this into practice",
                "p": (
                    "BookMyClinics gives Gujarat clinics a patient-facing booking path with live doctor availability, "
                    "so patients pick a real slot instead of leaving a phone message. WhatsApp confirmation keeps the booking visible on the patient’s phone. "
                    "We do not invent BookMyClinics-specific no-show percentages here — the figures above are from independent published studies of online booking systems. "
                    "The product goal is to give your clinic the same structural advantages those studies describe: chosen times, clear confirmation, and an easy path to change plans."
                ),
            },
        ],
        "source_keys": ["zhao2017", "wang2024", "frontiers2025", "sutter2020", "swiftqueue2024"],
    },
    {
        "slug": "less-staff-labor",
        "nav": "Evidence",
        "title": "Less Front-Desk Scheduling Labor | BookMyClinics",
        "meta": "Published reviews find reduced staff labor is the most frequently reported benefit of web-based medical appointment systems.",
        "h1": "Give your front desk hours back",
        "lead": "In the peer-reviewed literature, cutting staff labor is the single most commonly reported operational win from web-based scheduling.",
        "cta_primary": ("Register your clinic", "https://bookmyclinics.com/clinic.html"),
        "cta_secondary": ("Talk on WhatsApp", "https://wa.me/918511180957?text=Hi%2C%20I%20want%20to%20reduce%20front-desk%20phone%20load%20with%20BookMyClinics"),
        "sections": [
            {
                "h2": "What the evidence shows",
                "p": (
                    "Traditional booking depends on phone lines and human schedulers. Every request competes with other calls. "
                    "Zhao and colleagues’ JMIR systematic review summarized impacts across 21 web-based systems and found "
                    "“reducing staff labor” was the most cited positive change (10 of 21 systems) — ahead of satisfaction, efficiency, "
                    "no-show reduction, and wait-time reduction. That does not mean every clinic saves the same number of hours, "
                    "but it shows labor relief is the benefit researchers see reported most often."
                ),
                "facts": [
                    "Reducing staff labor: most-cited impact (10/21 systems) in Zhao et al., JMIR 2017.",
                    "Phone/in-person booking capacity is limited by scheduler availability and phone lines (JMIR 2017).",
                ],
            },
            {
                "h2": "Measured admin-time reductions",
                "p": (
                    "Newer operational evaluations put numbers on that labor shift. An Imperial College Healthcare NHS Trust analysis of "
                    "Swiftqueue digital appointment management for plain-film X-ray referrals (14,122 referrals) reported roughly "
                    "20 fewer administrative hours per week versus manual scheduling, alongside large drops in DNA and cancellations. "
                    "In screening mammography, a 2023 single-institution study reported that optimizing an EHR-tethered online self-scheduling "
                    "platform produced a 26-fold rise in online bookings and an approximately 16-fold reduction in patient-access-specialist "
                    "hands-on scheduling engagement for those exams."
                ),
                "facts": [
                    "Swiftqueue NHS evaluation: ~20 admin hours/week saved; DNA 12.1% → 3.1%.",
                    "Mammography self-scheduling optimization: ~16× less specialist scheduling engagement (Wood et al., 2023).",
                ],
            },
            {
                "h2": "Why labor falls when patients self-schedule",
                "p": (
                    "Self-scheduling moves routine slot selection from staff to patients. Orthopedic outpatient research comparing web-based "
                    "online scheduling with traditional staff scheduling notes greater patient autonomy and less burden on office staff. "
                    "The JMIR review also observes that when patients complete registration or pre-visit steps online before arrival, "
                    "check-in workload can fall. Staff time is then available for complex cases, walk-ins, and patients who still prefer to call."
                ),
                "facts": [
                    "Online scheduling described as less burden on office staff (JRMS 2023).",
                    "Pre-arrival forms/policies online can smooth workflow (JMIR 2017).",
                ],
            },
            {
                "h2": "How BookMyClinics puts this into practice",
                "p": (
                    "With BookMyClinics, patients browse clinic and doctor availability online and reserve a slot without holding your phone line. "
                    "Your team still controls doctors, leave, and daily appointments in the clinic portal — but they spend less time repeating "
                    "“Tuesday at 5 or Thursday at 11?” on every call. First 25 clinics join as Founding Members and stay free forever."
                ),
            },
        ],
        "source_keys": ["zhao2017", "swiftqueue2024", "wood2023", "jrms2023"],
    },
    {
        "slug": "shorter-wait-times",
        "nav": "Evidence",
        "title": "Shorter Appointment Wait Times | BookMyClinics",
        "meta": "Documented cases show online appointment systems can cut queueing and improve time-to-appointment offers.",
        "h1": "Shorter waits — measured in published studies",
        "lead": "Waiting is a quality signal. Research links web-based booking with shorter queues at registration and faster offered appointments in several documented programs.",
        "cta_primary": ("Book a doctor", "https://bookmyclinics.com/patient.html"),
        "cta_secondary": ("For clinics", "https://bookmyclinics.com/landings/lp-register.html"),
        "sections": [
            {
                "h2": "What the evidence shows",
                "p": (
                    "Zhao et al.’s JMIR systematic review lists decreased waiting time among the recurring benefits after clinics adopt "
                    "web-based scheduling (reported for 6 of 21 systems reviewed). One detailed example in that review is Cao and colleagues’ "
                    "hospital Web-based Appointment System in China, where average total waiting time fell from 98 minutes to 7 minutes "
                    "because patients no longer had to queue physically to obtain an appointment. Another UK sexual-health eTriage program "
                    "raised the share of patients offered an appointment within the required 48-hour window from 48% to 100%."
                ),
                "facts": [
                    "Waiting-time improvement cited for 6/21 systems (Zhao et al., JMIR 2017).",
                    "Chinese hospital WAS: average wait 98 min → 7 min (Cao et al., cited in JMIR 2017).",
                    "UK eTriage: appointments offered within 48 h rose from 48% → 100% (cited in JMIR 2017).",
                ],
            },
            {
                "h2": "Faster access through self-rescheduling",
                "p": (
                    "Beyond the initial booking queue, digital tools can shorten the wait until the actual visit. "
                    "A 2024 JMIR retrospective cohort on an EHR-based Fast Pass self-rescheduling tool reported that patients who accepted "
                    "earlier openings improved their appointment timing by a median of 14 days. That is not “magic marketing speed” — "
                    "it is unused earlier capacity being offered back to patients who want it."
                ),
                "facts": [
                    "Fast Pass acceptors: median 14-day earlier appointment (Gallo et al., JMIR 2024).",
                    "Real-time systems make open slots transparent so patients claim them without phone backlog (JMIR 2017).",
                ],
            },
            {
                "h2": "Why waits shrink",
                "p": (
                    "Phone booking creates two waits: waiting on hold for a scheduler, then waiting for an available clinical slot. "
                    "Real-time online calendars remove the scheduler queue for simple bookings. Same-day or soon slots, when clinics enable them, "
                    "can further compress request-to-visit time. The JMIR review also notes that late cancellations can be reused more quickly "
                    "online than through slow phone turnaround — recovering capacity that would otherwise sit empty."
                ),
            },
            {
                "h2": "How BookMyClinics puts this into practice",
                "p": (
                    "Patients on BookMyClinics see live availability for the next two weeks and pick a slot without standing in a reception queue "
                    "or waiting through a busy phone hour. Clinics keep control of doctor schedules and leave so the calendar patients see is real. "
                    "Published wait-time figures above come from independent studies, not from BookMyClinics outcome claims."
                ),
            },
        ],
        "source_keys": ["zhao2017", "gallo2024"],
    },
    {
        "slug": "higher-patient-satisfaction",
        "nav": "Evidence",
        "title": "Higher Patient Satisfaction with Online Booking | BookMyClinics",
        "meta": "Systematic reviews and meta-analysis associate digital self-scheduling with improved patient satisfaction.",
        "h1": "Patients prefer being able to book themselves",
        "lead": "Satisfaction surveys and pooled analyses repeatedly find that online appointment access is valued — and often improves measured satisfaction.",
        "cta_primary": ("Try patient booking", "https://bookmyclinics.com/patient.html"),
        "cta_secondary": ("Clinic registration", "https://bookmyclinics.com/clinic.html"),
        "sections": [
            {
                "h2": "What the evidence shows",
                "p": (
                    "Patient satisfaction with booking depends on getting the right time with the right provider. "
                    "Zhao et al. note that multiple satisfaction surveys found web-based appointment scheduling to be an extremely important feature, "
                    "with most patients saying they would use the service again. In their review of 21 systems, improved satisfaction was the "
                    "second most frequently reported positive change (7 of 21). A later meta-analysis of digital self-scheduling in hospital "
                    "outpatient settings estimated substantially higher odds of improved patient satisfaction versus conventional methods "
                    "(OR 2.83; 95% CI 2.20–3.64)."
                ),
                "facts": [
                    "Improved satisfaction reported for 7/21 systems (Zhao et al., JMIR 2017).",
                    "Digital self-scheduling meta-analysis: satisfaction OR 2.83 (95% CI 2.20–3.64).",
                    "Survey literature summarized in JMIR: most patients would use online booking again.",
                ],
            },
            {
                "h2": "What patients say they want",
                "p": (
                    "Convenience and control drive acceptance. The digital self-scheduling meta-analysis reports that patient acceptance increased "
                    "as digital tools matured and was dominated by perceived ease of use. Orthopedic outpatient research likewise frames online "
                    "scheduling as increasing patient autonomy: people can book without phone conversations and outside office hours. "
                    "Satisfaction rises when the booking channel matches how patients already live — on a phone, at night, without waiting on hold."
                ),
                "facts": [
                    "Ease of use dominates acceptance of digital self-scheduling (Wang & Lin meta-analysis).",
                    "Online scheduling available 24/7 with no phone wait (JRMS 2023 description of system design).",
                ],
            },
            {
                "h2": "How BookMyClinics puts this into practice",
                "p": (
                    "BookMyClinics is built for the Gujarat patient journey: find a clinic, choose a doctor and time, confirm on WhatsApp — "
                    "without forcing another app account or OTP maze for a simple booking. Clinics that go live give patients a modern first impression "
                    "grounded in the same access advantages the literature associates with higher satisfaction."
                ),
            },
        ],
        "source_keys": ["zhao2017", "wang2024", "jrms2023"],
    },
    {
        "slug": "after-hours-booking",
        "nav": "Evidence",
        "title": "24/7 After-Hours Appointment Booking | BookMyClinics",
        "meta": "Peer-reviewed reviews identify after-hours access as a core advantage of real-time online medical scheduling.",
        "h1": "Book when the clinic phone is asleep",
        "lead": "Real-time online scheduling’s most cited convenience advantage is after-hours access — patients claim open slots anytime, not only while reception is staffed.",
        "cta_primary": ("Open evening booking", "https://bookmyclinics.com/patient.html"),
        "cta_secondary": ("Clinic setup", "https://bookmyclinics.com/landings/lp-register.html"),
        "sections": [
            {
                "h2": "What the evidence shows",
                "p": (
                    "Phone booking stops when staff leave. Asynchronous email or form requests made at night still wait until schedulers return, "
                    "and may sit in the same queue as daytime phone calls. The JMIR systematic review states that the most cited benefit of "
                    "real-time scheduling is after-hour access: available slots are transparent on a web interface, and patients can claim them "
                    "anytime and anywhere with minimal scheduler intervention. Orthopedic outpatient system descriptions make the same operational point: "
                    "online scheduling is available 24/7, including weekends, with no phone waiting time."
                ),
                "facts": [
                    "After-hour access is the most cited benefit of real-time scheduling (Zhao et al., JMIR 2017).",
                    "Asynchronous web requests outside business hours wait until staff return (JMIR 2017).",
                    "24/7 online scheduling with no phone wait described in JRMS 2023 outpatient study context.",
                ],
            },
            {
                "h2": "Why after-hours access matters clinically",
                "p": (
                    "Working patients often decide to seek care after office phone hours. If the only channel is a busy daytime line, "
                    "they delay, forget, or choose another provider. Continuous booking converts evening intent into a reserved slot while "
                    "motivation is high. For clinics, that expands the capture window for demand without paying for overnight reception staff."
                ),
            },
            {
                "h2": "How BookMyClinics puts this into practice",
                "p": (
                    "BookMyClinics patient booking works on any phone, day or night, against the live calendar your clinic maintains. "
                    "You still set doctor shifts and leave; patients simply stop depending on your phone hours to reserve care. "
                    "That is the same structural after-hours advantage documented for real-time web scheduling in the research literature."
                ),
            },
        ],
        "source_keys": ["zhao2017", "jrms2023"],
    },
    {
        "slug": "patient-choice-control",
        "nav": "Evidence",
        "title": "Patient Choice and Control in Scheduling | BookMyClinics",
        "meta": "Research describes online medical scheduling as more patient-centered, with transparent calendars and broader time choices.",
        "h1": "Let patients choose the slot that fits real life",
        "lead": "Web-based booking reframes scheduling as a patient-centered self-service: browse open times, compare options, and decide — instead of accepting the few slots a caller reads aloud.",
        "cta_primary": ("See live clinic slots", "https://bookmyclinics.com/patient.html"),
        "cta_secondary": ("Register a clinic", "https://bookmyclinics.com/clinic.html"),
        "sections": [
            {
                "h2": "What the evidence shows",
                "p": (
                    "Patient-centeredness is one of the Institute of Medicine’s quality aims, and the JMIR review frames web-based medical scheduling "
                    "as a more patient-centered channel. Most systems present a calendar-like list so patients can select a convenient time from "
                    "available slots. By contrast, traditional phone booking typically offers only a limited set of times the scheduler mentions. "
                    "Some platforms also let patients filter physicians by attributes such as background, experience, gender, and reviews. "
                    "JRMS (2023) similarly emphasizes that online scheduling increases patient autonomy by removing the need to negotiate times by phone."
                ),
                "facts": [
                    "Web scheduling described as more patient-centered self-service (Zhao et al., JMIR 2017).",
                    "Calendar UIs let patients browse available slots vs limited verbal options (JMIR 2017).",
                    "Online scheduling increases patient autonomy (JRMS 2023).",
                ],
            },
            {
                "h2": "Better information when patients write for themselves",
                "p": (
                    "The same review notes a qualitative clinical upside: in self-service booking, patients’ written reasons for visit are often "
                    "more detailed. People who feel uncomfortable stating sensitive symptoms to a phone scheduler may be more candid online. "
                    "That improves triage quality before the visit — another documented dimension of patient-centered access, not just convenience."
                ),
                "facts": [
                    "Self-entered visit reasons often more detailed/illuminating (JMIR 2017).",
                    "Patients may be more candid online about sensitive symptoms (JMIR 2017).",
                ],
            },
            {
                "h2": "How BookMyClinics puts this into practice",
                "p": (
                    "On BookMyClinics, patients choose clinic, doctor, and time from real availability — then send a clear WhatsApp confirmation. "
                    "That mirrors the patient-choice pattern described in the literature: transparent options, patient decision, less phone negotiation."
                ),
            },
        ],
        "source_keys": ["zhao2017", "jrms2023"],
    },
    {
        "slug": "easier-reschedule-cancel",
        "nav": "Evidence",
        "title": "Easier Rescheduling and Cancellation | BookMyClinics",
        "meta": "Studies link easier online cancel/reschedule paths with fewer no-shows and more timely slot recovery.",
        "h1": "When plans change, the calendar should change too",
        "lead": "Published analyses connect easy online rescheduling and cancellation with fewer silent no-shows and faster recovery of clinic capacity.",
        "cta_primary": ("Clinic tools", "https://bookmyclinics.com/landings/lp-register.html"),
        "cta_secondary": ("WhatsApp", "https://wa.me/918511180957?text=Hi%2C%20I%20want%20online%20rescheduling%20for%20my%20clinic"),
        "sections": [
            {
                "h2": "What the evidence shows",
                "p": (
                    "People miss visits because they forget, because the original date no longer works, or because cancelling by phone is hard. "
                    "The JMIR review proposes that improved ability to verify, cancel, and reschedule is a plausible reason online programs see "
                    "fewer no-shows. Dartmouth-Hitchcock’s asynchronous messaging service — which let patients request, review, reschedule, and cancel — "
                    "was associated with a 40% no-show reduction in that review. Sutter Health’s Fast Pass analysis found accepting an earlier slot "
                    "also facilitated timely cancellation of appointments no longer needed (+1.7 percentage points; about a 9% relative change)."
                ),
                "facts": [
                    "Easier cancel/reschedule proposed as a no-show reduction mechanism (JMIR 2017).",
                    "Dartmouth-Hitchcock messaging appointments: −40% no-shows (cited in JMIR 2017).",
                    "Fast Pass: timely cancellations +1.7 pp when earlier offers accepted (Martinez et al., 2020).",
                ],
            },
            {
                "h2": "Self-rescheduling at scale",
                "p": (
                    "Large multispecialty practices now run multiple self-schedule and self-reschedule pathways. A 2024 program description "
                    "from a multisite clinic reported 733,651 successfully self-scheduled completed visits in a single year across seven processes, "
                    "including patient self-reschedule and automated waitlist self-reschedule paths. The operational lesson is clear: "
                    "giving patients structured digital ways to move appointments is no longer experimental — it is production infrastructure."
                ),
                "facts": [
                    "733,651 self-scheduled completed visits in 2023 across 7 processes (Northwestern Medicine program paper, 2024).",
                    "Self-reschedule and waitlist self-reschedule were major secondary pathways in that program.",
                ],
            },
            {
                "h2": "How BookMyClinics puts this into practice",
                "p": (
                    "BookMyClinics clinic portals support day-of realities: cancellations, exports, and leave when a doctor is unavailable. "
                    "Patients confirm on WhatsApp so changing a plan starts from a message thread they already use. "
                    "The research case for easy change-management is strong; our product focus is making that change visible to both clinic and patient."
                ),
            },
        ],
        "source_keys": ["zhao2017", "sutter2020", "gallo2024", "northwestern2024"],
    },
    {
        "slug": "better-slot-utilization",
        "nav": "Evidence",
        "title": "Better Appointment Slot Utilization | BookMyClinics",
        "meta": "Practice data show online appointment scheduling can cut unused and never-booked slots and raise calendar utilization.",
        "h1": "Fill the calendar you already paid for",
        "lead": "Online booking does not only move demand online — published practice data show it can reduce unused slots and lift utilization of available appointments.",
        "cta_primary": ("Founding Member offer", "https://bookmyclinics.com/landings/lp-founding.html"),
        "cta_secondary": ("Register online", "https://bookmyclinics.com/clinic.html"),
        "sections": [
            {
                "h2": "What the evidence shows",
                "p": (
                    "A 2025 Frontiers in Digital Health study tracked online appointment scheduling in a medical practice. "
                    "After OAS implementation, unused appointments fell from a median 22.7% to 10.3%, and never-booked appointments fell "
                    "from 8.6% to 1.6%, increasing utilization of available appointments. The authors also report that as the share of "
                    "online-booked appointments rose, efficiency gains strengthened — a practical signal that digital booking density matters."
                ),
                "facts": [
                    "Unused appointments: median 22.7% → 10.3% after OAS (Frontiers 2025 practice data).",
                    "Never-booked appointments: median 8.6% → 1.6% (Frontiers 2025).",
                    "Utilization of available appointments increased (p &lt; 0.0001).",
                ],
            },
            {
                "h2": "Recovering late cancellations",
                "p": (
                    "The JMIR review explains another utilization pathway: real-time systems can reuse slots released by late cancellations "
                    "faster than phone-driven turnaround allows. Empty sessions are expensive whether they come from no-shows, "
                    "unbooked template time, or cancellations that never get refilled. Online visibility is how those holes get filled."
                ),
                "facts": [
                    "Late-cancellation slots can be reused more quickly online than via phone turnaround (JMIR 2017).",
                    "JMIR review also lists increasing revenue among reported impacts for 4/21 systems — typically via better filled capacity.",
                ],
            },
            {
                "h2": "How BookMyClinics puts this into practice",
                "p": (
                    "BookMyClinics exposes real doctor availability to patients across the city, so open sessions are discoverable instead of "
                    "hidden behind a phone tree. Clinics manage leave and daily lists so the template patients see matches the day you intend to run. "
                    "Utilization figures cited above are from independent practice research, presented so you can judge the opportunity size."
                ),
            },
        ],
        "source_keys": ["frontiers2025", "zhao2017"],
    },
    {
        "slug": "scheduling-efficiency",
        "nav": "Evidence",
        "title": "Higher Scheduling Efficiency | BookMyClinics",
        "meta": "Meta-analysis finds digital self-scheduling associated with markedly higher scheduling efficiency versus conventional methods.",
        "h1": "Scheduling that scales without adding phone lines",
        "lead": "Pooled hospital outpatient evidence associates digital self-scheduling with large gains in scheduling efficiency — more completed booking work with less manual bottleneck.",
        "cta_primary": ("Start clinic setup", "https://bookmyclinics.com/clinic.html"),
        "cta_secondary": ("See demo path", "https://bookmyclinics.com/landings/lp-demo.html"),
        "sections": [
            {
                "h2": "What the evidence shows",
                "p": (
                    "Wang and Lin’s systematic review and meta-analysis of digital self-scheduling in hospital outpatient settings "
                    "(18 observational studies) reported increased scheduling efficiency with a pooled odds ratio of 4.94 "
                    "(95% CI 4.54–5.38; p &lt; 0.001) compared with conventional methods. The same analysis found lower no-show odds "
                    "and higher satisfaction odds. Separately, Zhao et al. grouped related operational gains — optimizing referrals and "
                    "streamlining operations — under “improving efficiency,” reported for 6 of 21 web-based systems."
                ),
                "facts": [
                    "Scheduling efficiency OR 4.94 (95% CI 4.54–5.38) for digital self-scheduling (Wang & Lin).",
                    "Improving efficiency cited for 6/21 systems (Zhao et al., JMIR 2017).",
                    "NHS Swiftqueue evaluation also raised booking completion 82.8% → 93.4%.",
                ],
            },
            {
                "h2": "Efficiency is a system property",
                "p": (
                    "Efficiency here is not a slogan about “working faster.” It means more of the booking workflow completes without "
                    "serial human handling. When thousands of routine appointments are self-scheduled, staff intervene on exceptions — "
                    "exactly the pattern described in high-volume self-scheduling programs and in admin-hour reductions from digital platforms."
                ),
            },
            {
                "h2": "How BookMyClinics puts this into practice",
                "p": (
                    "BookMyClinics standardizes the booking path for multi-clinic Gujarat operations: one patient entry point, "
                    "clinic-controlled doctor calendars, and WhatsApp confirmation. That is how scheduling efficiency shows up in a real reception — "
                    "fewer repeated calls for the same slot decision."
                ),
            },
        ],
        "source_keys": ["wang2024", "zhao2017", "swiftqueue2024"],
    },
    {
        "slug": "appointment-reminders",
        "nav": "Evidence",
        "title": "Appointment Reminders Reduce No-Shows | BookMyClinics",
        "meta": "SMS and digital reminders are repeatedly associated with lower no-show rates in peer-reviewed scheduling research.",
        "h1": "Reminders turn bookings into arrivals",
        "lead": "Even the best booking channel needs memory support. Controlled and observational evidence shows digital reminders reduce missed visits.",
        "cta_primary": ("WhatsApp clinic setup", "https://wa.me/918511180957?text=Hi%2C%20I%20want%20booking%20reminders%20for%20my%20clinic"),
        "cta_secondary": ("Register online", "https://bookmyclinics.com/clinic.html"),
        "sections": [
            {
                "h2": "What the evidence shows",
                "p": (
                    "Forgetting is a classic no-show driver — especially when the gap between booking and visit is long. "
                    "The Sutter Fast Pass paper summarizes prior work showing SMS reminders reduce no-show rates and increase cancellation rates, "
                    "which frees slots for other patients. In the 2025 Frontiers study, SMS reminders were among the most effective factors "
                    "associated with lower hospital no-shows (odds ratio 0.93), alongside regular consultation types. "
                    "Digital booking platforms often bundle reminders with scheduling; the NHS Swiftqueue evaluation’s large DNA reduction "
                    "occurred in a digital scheduling and patient-engagement context, not phone-only workflows."
                ),
                "facts": [
                    "SMS reminders linked to fewer no-shows and more timely cancellations (literature summarized in Martinez et al., 2020).",
                    "Frontiers 2025 hospital analysis: SMS reminders OR 0.93 for no-show reduction.",
                    "JMIR review notes auto-generated email/message reminders as a no-show mitigation tactic providers can enforce.",
                ],
            },
            {
                "h2": "Booking + reminder is the practical pair",
                "p": (
                    "Online scheduling gets the right slot on the calendar; reminders keep that commitment salient. "
                    "Frontiers authors explicitly note that OAS provides 24/7 booking, easier rescheduling/cancellation, and enables automated reminders — "
                    "a combined design for efficiency and access. Clinics that only move booking online without any confirmation channel "
                    "leave the forgetfulness problem unsolved."
                ),
            },
            {
                "h2": "How BookMyClinics puts this into practice",
                "p": (
                    "BookMyClinics confirmations travel over WhatsApp — the messaging channel most patients in India already check — "
                    "so the booking does not disappear into a missed phone note. That aligns with the documented reminder principle: "
                    "keep the appointment visible until the visit happens."
                ),
            },
        ],
        "source_keys": ["sutter2020", "frontiers2025", "zhao2017", "swiftqueue2024"],
    },
    {
        "slug": "less-phone-bottleneck",
        "nav": "Evidence",
        "title": "Escape the Phone-Line Booking Bottleneck | BookMyClinics",
        "meta": "Research shows traditional appointment access is limited by phone lines and schedulers — online booking removes that queue for routine slots.",
        "h1": "Stop making care wait on a busy signal",
        "lead": "Documented analyses of traditional booking show access is constrained not only by clinical capacity, but by phone lines and scheduler bandwidth.",
        "cta_primary": ("Move bookings online", "https://bookmyclinics.com/landings/lp-register.html"),
        "cta_secondary": ("Patient booking", "https://bookmyclinics.com/patient.html"),
        "sections": [
            {
                "h2": "What the evidence shows",
                "p": (
                    "Zhao et al. open their JMIR review with a structural diagnosis: traditional telephone or in-person booking requires scheduler "
                    "intervention, so timely appointments are limited by available slots and by schedulers and phone lines. "
                    "Asynchronous web forms that still dump into the same queue as phone calls inherit that backlog. "
                    "Real-time online systems change the constraint: patients interact with the schedule directly. "
                    "Operational studies then show the labor shift — for example, mammography self-scheduling optimization with a ~16× drop in "
                    "specialist scheduling engagement, and NHS digital scheduling cutting about 20 admin hours per week."
                ),
                "facts": [
                    "Phone booking limited by schedulers and phone lines (Zhao et al., JMIR 2017).",
                    "Async web requests can share the same queue as phone calls (JMIR 2017).",
                    "Documented admin relief: ~20 hrs/week (Swiftqueue); ~16× less specialist engagement (mammography 2023 study).",
                ],
            },
            {
                "h2": "What patients experience on a saturated line",
                "p": (
                    "A busy line feels like a closed clinic even when doctors still have open slots. Satisfaction research ties booking success "
                    "to getting the right time with the right provider; phone congestion blocks that outcome before clinical scarcity does. "
                    "Online calendars make remaining capacity visible, so demand can clear against real openings instead of abandoning the call."
                ),
            },
            {
                "h2": "How BookMyClinics puts this into practice",
                "p": (
                    "BookMyClinics adds a parallel booking lane that does not consume your reception phone. "
                    "Patients who can self-serve do; your staff keep the line for questions that truly need a human. "
                    "That is the bottleneck redesign the literature describes — not “no phones ever,” but phones no longer being the only door."
                ),
            },
        ],
        "source_keys": ["zhao2017", "swiftqueue2024", "wood2023"],
    },
    {
        "slug": "smoother-checkin",
        "nav": "Evidence",
        "title": "Smoother Check-In with Online Pre-Registration | BookMyClinics",
        "meta": "Peer-reviewed reviews note online appointment workflows can shift registration and policy review before the visit, smoothing arrival.",
        "h1": "Start the visit before the patient walks in",
        "lead": "Published descriptions of web-based appointment programs show pre-visit forms, policy review, and clearer visit reasons — all of which smooth front-desk workflow on arrival.",
        "cta_primary": ("Clinic onboarding", "https://bookmyclinics.com/clinic.html"),
        "cta_secondary": ("Benefits index", "./"),
        "sections": [
            {
                "h2": "What the evidence shows",
                "p": (
                    "The JMIR systematic review highlights a convenience that is easy to underestimate: patients can fill out registration forms, "
                    "get pre-screened, and review practice policies online before they show up. Authors note this can smooth workflow and reduce "
                    "misunderstandings at the desk. JRMS (2023) repeats the same operational logic — patients who schedule themselves can complete "
                    "registration and pre-screening before arrival, leaving staff with less check-in workload. "
                    "Separately, self-entered reasons for visit tend to be more detailed than rushed phone statements, which helps the clinical team prepare."
                ),
                "facts": [
                    "Pre-visit registration/policy review online can smooth workflow (Zhao et al., JMIR 2017).",
                    "Self-scheduling associated with less check-in workload when forms are completed ahead (JRMS 2023, citing Zhao).",
                    "Self-described visit reasons often more detailed than phone statements (JMIR 2017).",
                ],
            },
            {
                "h2": "Arrival quality is part of access",
                "p": (
                    "Access is not only “got a slot.” It is also whether the first ten minutes of the visit are spent fixing paperwork or starting care. "
                    "Digital intake attached to online booking moves demographic and policy steps out of peak lobby time. "
                    "That is why smoother check-in appears in the literature as a companion benefit of web scheduling, not a separate product category."
                ),
            },
            {
                "h2": "How BookMyClinics puts this into practice",
                "p": (
                    "BookMyClinics captures the booking essentials up front — clinic, doctor, slot, and WhatsApp confirmation — "
                    "so reception starts from a known appointment instead of a vague walk-in story. "
                    "As you grow with Founding Member onboarding, our team helps standardize the patient path so arrival matches what the calendar already promised."
                ),
            },
        ],
        "source_keys": ["zhao2017", "jrms2023"],
    },
    {
        "slug": "increased-revenue",
        "nav": "Evidence",
        "title": "Online Booking and Clinic Revenue Capacity | BookMyClinics",
        "meta": "Peer-reviewed reviews report increased revenue among clinics adopting web-based scheduling, usually through better-filled capacity and fewer wasted slots.",
        "h1": "Revenue follows filled appointment time",
        "lead": "Published reviews list increased revenue among reported outcomes of web-based scheduling — typically because clinics waste fewer paid clinician hours on empty chairs.",
        "cta_primary": ("Become a Founding Member", "https://bookmyclinics.com/landings/lp-founding.html"),
        "cta_secondary": ("Register your clinic", "https://bookmyclinics.com/clinic.html"),
        "sections": [
            {
                "h2": "What the evidence shows",
                "p": (
                    "Zhao and colleagues’ JMIR systematic review of web-based medical appointment systems found that increasing revenue was reported "
                    "as a positive change for 4 of the 21 systems reviewed. That sits alongside related capacity findings in the same literature: "
                    "lower no-shows, shorter turnaround to refill late cancellations, and higher utilization of available appointments. "
                    "Revenue in these studies is not framed as “charge patients more” — it is framed as recovering clinical time that phone-only "
                    "workflows leave empty."
                ),
                "facts": [
                    "Increasing revenue reported for 4/21 web-based systems (Zhao et al., JMIR 2017).",
                    "Practice OAS cut unused appointments 22.7% → 10.3% and never-booked slots 8.6% → 1.6% (Frontiers 2025).",
                    "Tricare / Murray Hill comparisons in JMIR show sharply lower no-shows for web vs phone booking — preserving billable visit capacity.",
                ],
            },
            {
                "h2": "How empty slots become lost revenue",
                "p": (
                    "Every no-show and every never-refilled cancellation is clinician time you still staff for. "
                    "The Sutter Fast Pass analysis quantified avoided no-shows at system scale and discussed clinical implications of recovering those visits; "
                    "the JMIR review similarly notes that long waits can push patients to other providers and cause revenue loss. "
                    "Digital booking attacks both sides: patients are more likely to keep self-chosen times, and open or freed slots stay visible for someone else to take."
                ),
                "facts": [
                    "Long waits can drive patients to other providers and potential revenue loss (JMIR 2017 discussion).",
                    "Fast Pass acceptors had lower no-show rates than matched comparisons (Martinez et al., 2020).",
                    "NHS Swiftqueue digital scheduling raised booking completion 82.8% → 93.4% while cutting DNA 12.1% → 3.1%.",
                ],
            },
            {
                "h2": "How BookMyClinics puts this into practice",
                "p": (
                    "BookMyClinics makes your open doctor sessions discoverable to patients across Gujarat, with WhatsApp confirmation so the booking sticks. "
                    "We do not publish BookMyClinics revenue guarantees — the figures above are from independent studies. "
                    "The product intent is the same capacity logic those studies describe: fewer empty chairs on days you are already open."
                ),
            },
        ],
        "source_keys": ["zhao2017", "frontiers2025", "sutter2020", "swiftqueue2024"],
    },
    {
        "slug": "lower-operating-cost",
        "nav": "Evidence",
        "title": "Lower Scheduling Operating Costs | BookMyClinics",
        "meta": "Documented evaluations link digital appointment scheduling with lower administrative burden and reported cost reductions versus manual phone workflows.",
        "h1": "Cut the cost of getting someone on the calendar",
        "lead": "Research and operational evaluations associate online scheduling with reduced administrative cost — fewer staff hours per completed booking, and tighter use of already-paid clinic time.",
        "cta_primary": ("Register online", "https://bookmyclinics.com/clinic.html"),
        "cta_secondary": ("WhatsApp", "https://wa.me/918511180957?text=Hi%2C%20I%20want%20to%20lower%20scheduling%20costs%20with%20BookMyClinics"),
        "sections": [
            {
                "h2": "What the evidence shows",
                "p": (
                    "In Zhao et al.’s JMIR review, reducing cost was reported for 3 of 21 web-based appointment systems, while reducing staff labor "
                    "was the single most-cited benefit (10 of 21). Those two findings travel together: scheduling cost is largely people-time on phones. "
                    "A 2024 NHS Trust evaluation of Swiftqueue digital appointment management estimated about 20 fewer administrative hours per week "
                    "versus manual scheduling for plain-film X-ray referrals, alongside large drops in DNA and cancellations. "
                    "A mammography self-scheduling optimization study likewise reported an approximately 16-fold reduction in specialist scheduling engagement "
                    "after online booking scaled."
                ),
                "facts": [
                    "Reducing cost reported for 3/21 systems; reducing staff labor for 10/21 (Zhao et al., JMIR 2017).",
                    "Swiftqueue NHS evaluation: ~20 admin hours/week saved (14,122 referrals analyzed).",
                    "Mammography OSS optimization: ~16× less patient-access-specialist scheduling engagement (2023 study).",
                ],
            },
            {
                "h2": "Cost also hides in unused sessions",
                "p": (
                    "Frontiers (2025) practice data showed unused appointments falling from 22.7% to 10.3% after online appointment scheduling, "
                    "with authors noting that reduced variability in unused slots supports more precise personnel planning and can lower staffing costs. "
                    "Paying staff to sit through empty template time is an operating cost even when no patient fee is collected. "
                    "Better utilization is therefore a cost story as much as a revenue story."
                ),
                "facts": [
                    "Unused appointments median 22.7% → 10.3% after OAS (Frontiers 2025).",
                    "Authors link lower unused-slot variability to more precise personnel planning and lower staffing costs (Frontiers 2025).",
                ],
            },
            {
                "h2": "How BookMyClinics puts this into practice",
                "p": (
                    "BookMyClinics shifts routine slot selection to patients while your team keeps control of doctors, leave, and the day list. "
                    "Founding Members (first 25 clinics) stay free forever on the platform fee — so you are not trading phone labor for a heavy software bill "
                    "while you prove the workflow. Published hour-and-cost figures above remain independent study results, not BookMyClinics guarantees."
                ),
            },
        ],
        "source_keys": ["zhao2017", "swiftqueue2024", "wood2023", "frontiers2025"],
    },
    {
        "slug": "clearer-visit-reasons",
        "nav": "Evidence",
        "title": "Clearer Visit Reasons with Online Booking | BookMyClinics",
        "meta": "Peer-reviewed reviews find patients often provide more detailed and candid reasons for visit when booking online versus speaking to a phone scheduler.",
        "h1": "Better visit details before the patient arrives",
        "lead": "Documented analyses of web-based scheduling note that self-entered reasons for visit are often more detailed — and that patients may be more candid online about sensitive symptoms.",
        "cta_primary": ("See patient booking", "https://bookmyclinics.com/patient.html"),
        "cta_secondary": ("Clinic registration", "https://bookmyclinics.com/landings/lp-register.html"),
        "sections": [
            {
                "h2": "What the evidence shows",
                "p": (
                    "Zhao et al.’s JMIR systematic review describes a qualitative advantage of medical self-service booking: "
                    "patients’ own descriptions of the reason for visit are often more detailed and illuminating than statements captured over the phone. "
                    "The review also notes that some patients feel uncomfortable or unable to vocalize certain symptoms — for example sexual health concerns — "
                    "to a scheduler by phone or in person, and may give an untrue statement. When they schedule online by themselves, they tend to be more candid. "
                    "That is a documented information-quality benefit, not only a convenience benefit."
                ),
                "facts": [
                    "Self-entered visit reasons often more detailed and illuminating (Zhao et al., JMIR 2017).",
                    "Patients may withhold or misstate sensitive symptoms to phone schedulers (JMIR 2017).",
                    "Self-scheduling associated with more candid symptom reporting online (JMIR 2017).",
                ],
            },
            {
                "h2": "Why clearer reasons improve the visit",
                "p": (
                    "Front-desk and clinical teams prepare differently when they know whether a slot is a follow-up, a new complaint, or a sensitive concern. "
                    "Richer pre-visit text supports better rooming, better time allocation, and fewer wrong-appointment-type mismatches — "
                    "another impact category the JMIR review recorded for web-based systems. "
                    "Combined with pre-arrival registration and policy review (also documented in the same review), online booking becomes an information channel, not just a calendar click."
                ),
                "facts": [
                    "Reducing wrong appointment type appears among reported impacts in the JMIR 2017 synthesis.",
                    "Pre-visit forms and policy review online can reduce misunderstandings at arrival (JMIR 2017).",
                ],
            },
            {
                "h2": "How BookMyClinics puts this into practice",
                "p": (
                    "BookMyClinics bookings travel with structured clinic, doctor, and slot details into a WhatsApp confirmation the patient can see and the clinic can act on. "
                    "That gives reception a clearer starting point than a hurried phone note. "
                    "As with every evidence page here, the candid-detail findings come from published research on web-based scheduling systems generally."
                ),
            },
        ],
        "source_keys": ["zhao2017"],
    },
]


def slug_to_title(slug: str) -> str:
    return BENEFITS[[b["slug"] for b in BENEFITS].index(slug)]["h1"]


def render_page(b: dict, idx: int) -> str:
    img = IMAGES[idx % len(IMAGES)]
    src_blocks = []
    for key in b["source_keys"]:
        s = SOURCES[key]
        src_blocks.append(
            f'<li><a href="{s["url"]}" target="_blank" rel="noopener noreferrer">{s["label"]}</a>'
            f' — {s["detail"]}</li>'
        )
    sections_html = []
    for sec in b["sections"]:
        facts = ""
        if sec.get("facts"):
            items = "".join(f"<li>{f}</li>" for f in sec["facts"])
            facts = f'<ul class="evidence-list">{items}</ul>'
        sections_html.append(
            f"""
  <section class="section prose-section">
    <h2>{sec['h2']}</h2>
    <div class="prose">
      <p>{sec['p']}</p>
      {facts}
    </div>
  </section>"""
        )
    cta_p, cta_h = b["cta_primary"]
    cta_s, cta_sh = b["cta_secondary"]
    wa = "btn-wa" if "wa.me" in cta_sh else "btn-ghost"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="canonical" href="https://bookmyclinics.com/landings/benefits/{b['slug']}.html">
  <title>{b['title']}</title>
  <meta name="description" content="{b['meta']}">
  <meta name="theme-color" content="#0f172a">
  <link rel="icon" type="image/png" href="https://upadhyaymehul9-prog.github.io/bookmyclinic/icon-192.png">
  <link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800;900&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../lp.css">
</head>
<body>
  <nav>
    <a class="nav-brand" href="https://bookmyclinics.com/">Book<span>My</span>Clinics</a>
    <a class="nav-link" href="./">{b['nav']}</a>
  </nav>

  <header class="hero">
    <div class="hero-media" style="background-image:url('{img}');"></div>
    <div class="hero-shade"></div>
    <div class="hero-content">
      <div class="brand-mark">Book<span>My</span>Clinics</div>
      <h1>{b['h1']}</h1>
      <p>{b['lead']}</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="{cta_h}">{cta_p}</a>
        <a class="btn {wa}" href="{cta_sh}">{cta_s}</a>
      </div>
    </div>
  </header>
{''.join(sections_html)}
  <section class="section sources-section">
    <h2>Documented sources</h2>
    <p class="sources-note">Figures on this page come from peer-reviewed journals, systematic reviews, and published operational evaluations of online / digital appointment systems. They are not BookMyClinics proprietary outcome claims. Results vary by clinic type, specialty, and implementation.</p>
    <ol class="sources-list">
      {''.join(src_blocks)}
    </ol>
  </section>

  <section class="cta-band">
    <h2>Put evidence to work in your clinic</h2>
    <p>First 25 clinics become Founding Members on BookMyClinics — free forever.</p>
    <div class="cta-row">
      <a class="btn btn-teal" href="https://bookmyclinics.com/clinic.html">Register Your Clinic</a>
      <a class="btn btn-ghost" href="./">All {len(BENEFITS)} evidence pages</a>
    </div>
  </section>

  <footer>
    <div class="footer-links">
      <a href="./">Benefits</a> ·
      <a href="https://bookmyclinics.com/landings/lp-register.html">For Clinics</a> ·
      <a href="https://bookmyclinics.com/privacy.html">Privacy</a> ·
      <a href="https://bookmyclinics.com/terms.html">Terms</a>
    </div>
    © 2026 BookMyClinics · Gujarat, India
  </footer>
</body>
</html>
"""


def render_hub() -> str:
    items = []
    for i, b in enumerate(BENEFITS, 1):
        items.append(
            f"""      <a class="hub-item" href="{b['slug']}.html">
        <strong>{i:02d} · {b['h1']}</strong>
        <span>{b['meta']}</span>
      </a>"""
        )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="canonical" href="https://bookmyclinics.com/landings/benefits/">
  <title>{len(BENEFITS)} Evidence-Based Benefits of Online Appointment Booking | BookMyClinics</title>
  <meta name="description" content="{len(BENEFITS)} BookMyClinics landing pages on documented benefits of online medical appointment systems, each backed by published research.">
  <meta name="theme-color" content="#0f172a">
  <link rel="icon" type="image/png" href="https://upadhyaymehul9-prog.github.io/bookmyclinic/icon-192.png">
  <link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800;900&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../lp.css">
  <style>
    .hub {{
      min-height: 100vh;
      padding: 100px 24px 64px;
      max-width: 760px;
      margin: 0 auto;
      background:
        radial-gradient(ellipse at 15% 0%, rgba(37,99,235,0.22), transparent 45%),
        radial-gradient(ellipse at 90% 40%, rgba(13,148,136,0.14), transparent 42%),
        var(--navy);
    }}
    .hub-brand {{
      font-family: var(--font-display);
      font-size: clamp(32px, 7vw, 48px);
      font-weight: 900;
      letter-spacing: -1.4px;
      margin-bottom: 14px;
    }}
    .hub-brand span {{ color: var(--sky); }}
    .hub h1 {{
      font-family: var(--font-display);
      font-size: clamp(22px, 4.2vw, 30px);
      font-weight: 700;
      letter-spacing: -0.6px;
      line-height: 1.25;
      max-width: 22ch;
      margin-bottom: 12px;
    }}
    .hub-lead {{
      color: rgba(255,255,255,0.55);
      margin-bottom: 28px;
      line-height: 1.65;
      max-width: 46ch;
    }}
    .hub-list {{ display: grid; gap: 12px; }}
    .hub-item {{
      display: block;
      padding: 18px 20px;
      border-radius: 16px;
      background: rgba(255,255,255,0.04);
      border: 1px solid rgba(255,255,255,0.1);
      text-decoration: none;
      transition: transform 0.2s, border-color 0.2s, background 0.2s;
    }}
    .hub-item:hover {{
      transform: translateY(-2px);
      border-color: rgba(56,189,248,0.35);
      background: rgba(255,255,255,0.06);
    }}
    .hub-item strong {{
      display: block;
      font-family: var(--font-display);
      font-size: 16px;
      font-weight: 700;
      margin-bottom: 6px;
      letter-spacing: -0.3px;
    }}
    .hub-item span {{
      display: block;
      font-size: 13px;
      color: rgba(255,255,255,0.48);
      line-height: 1.5;
    }}
  </style>
</head>
<body>
  <nav>
    <a class="nav-brand" href="https://bookmyclinics.com/">Book<span>My</span>Clinics</a>
    <a class="nav-link" href="https://bookmyclinics.com/landings/lp-register.html">For Clinics</a>
  </nav>
  <main class="hub">
    <div class="hub-brand">Book<span>My</span>Clinics</div>
    <h1>{len(BENEFITS)} documented benefits of online appointment booking</h1>
    <p class="hub-lead">Each page explains one benefit using peer-reviewed reviews, meta-analyses, and published clinic or hospital evaluations — with source links. Figures are from independent studies of online booking systems, not BookMyClinics proprietary claims.</p>
    <div class="hub-list">
{chr(10).join(items)}
    </div>
  </main>
  <footer>
    <div class="footer-links">
      <a href="https://bookmyclinics.com/">Home</a> ·
      <a href="https://bookmyclinics.com/clinic.html">Register</a> ·
      <a href="https://bookmyclinics.com/privacy.html">Privacy</a>
    </div>
    © 2026 BookMyClinics · Gujarat, India
  </footer>
</body>
</html>
"""


def patch_css():
    css_path = ROOT / "landings" / "lp.css"
    css = css_path.read_text()
    marker = "/* benefit landing prose */"
    block = """
/* benefit landing prose */
.prose-section .prose p {
  font-size: 16px;
  color: rgba(255,255,255,0.62);
  line-height: 1.75;
  max-width: 62ch;
  margin-bottom: 18px;
}
.evidence-list {
  list-style: none;
  display: grid;
  gap: 10px;
  margin: 8px 0 0;
  max-width: 62ch;
}
.evidence-list li {
  position: relative;
  padding: 14px 16px 14px 18px;
  border-left: 3px solid rgba(56,189,248,0.55);
  background: linear-gradient(90deg, rgba(37,99,235,0.12), transparent 85%);
  color: rgba(255,255,255,0.72);
  font-size: 14px;
  line-height: 1.55;
}
.sources-section h2 { margin-bottom: 10px; }
.sources-note {
  font-size: 14px;
  color: rgba(255,255,255,0.5);
  line-height: 1.65;
  max-width: 62ch;
  margin-bottom: 20px;
}
.sources-list {
  max-width: 62ch;
  padding-left: 1.2rem;
  display: grid;
  gap: 12px;
  color: rgba(255,255,255,0.55);
  font-size: 13px;
  line-height: 1.55;
}
.sources-list a {
  color: var(--sky);
  text-decoration: underline;
  text-underline-offset: 2px;
}
"""
    if marker in css:
        # replace from marker to end or previous block end — simplest: append only if missing styles
        pass
    else:
        css_path.write_text(css.rstrip() + "\n" + block)


def patch_sitemap():
    sm = ROOT / "sitemap.xml"
    text = sm.read_text()
    # Remove prior benefit urls if regenerating
    text = re.sub(
        r"\n<url>\n  <loc>https://bookmyclinics.com/landings/benefits/[^<]+</loc>[\s\S]*?</url>",
        "",
        text,
    )
    entries = [
        f"""
<url>
  <loc>https://bookmyclinics.com/landings/benefits/</loc>
  <lastmod>{TODAY}T00:00:00+00:00</lastmod>
  <priority>0.75</priority>
</url>"""
    ]
    for b in BENEFITS:
        entries.append(
            f"""
<url>
  <loc>https://bookmyclinics.com/landings/benefits/{b['slug']}.html</loc>
  <lastmod>{TODAY}T00:00:00+00:00</lastmod>
  <priority>0.70</priority>
</url>"""
        )
    text = text.replace("</urlset>", "".join(entries) + "\n\n</urlset>")
    sm.write_text(text)


def patch_landings_index():
    path = ROOT / "landings" / "index.html"
    html = path.read_text()
    n = len(BENEFITS)
    if "benefits/" not in html:
        inject = f"""
      <a class="hub-item" href="benefits/">
        <strong>Evidence library · {n} benefit pages</strong>
        <span>Documented research on online appointment booking — one landing page per benefit</span>
      </a>"""
        html = html.replace(
            '      <a class="hub-item" href="lp-partners.html">',
            inject + "\n      <a class=\"hub-item\" href=\"lp-partners.html\">",
        )
    html = re.sub(
        r"Evidence library · \d+ benefit pages",
        f"Evidence library · {n} benefit pages",
        html,
    )
    html = re.sub(
        r"a \d+-page evidence library",
        f"a {n}-page evidence library",
        html,
    )
    html = html.replace(
        "Five purpose-built pages for patients, clinics, demo, founding partners, and team growth.",
        f"Funnel pages plus a {n}-page evidence library on documented benefits of online appointment booking.",
    )
    path.write_text(html)


def main():
    for i, b in enumerate(BENEFITS):
        (OUT / f"{b['slug']}.html").write_text(render_page(b, i))
        print("wrote", b["slug"])
    (OUT / "index.html").write_text(render_hub())
    print("wrote index")
    patch_css()
    patch_sitemap()
    patch_landings_index()
    print("done", len(BENEFITS), "benefit pages")


if __name__ == "__main__":
    main()
