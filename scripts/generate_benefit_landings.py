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
        "nav": "Benefits",
        "title": "Fewer Missed Appointments | BookMyClinics",
        "meta": "Online doctor booking helps clinics cut missed appointments. Patients pick their own time and get a clear confirmation.",
        "h1": "Fewer missed appointments",
        "lead": "When patients book online and choose their own time, they are more likely to show up — and less likely to waste a doctor slot.",
        "cta_primary": ("See how clinics go live", "https://bookmyclinics.com/landings/lp-register.html"),
        "cta_secondary": ("Read all benefits", "./"),
        "sections": [
            {
                "h2": "What this means in plain words",
                "p": (
                    "A missed appointment is an empty chair while the doctor is ready. Phone booking often leads to forgotten times, "
                    "wrong notes, or patients who never got a clear confirmation. Online booking lets the patient pick a real slot "
                    "and keep that booking on their phone. Across many clinics and health systems that moved to online booking, "
                    "missed visits went down — sometimes from around 8% on phone booking to about 1–2% on web booking."
                ),
                "facts": [
                    "Patients who book online often miss fewer visits than patients who book only by phone.",
                    "Some clinics saw missed appointments drop by around 40% after online booking.",
                    "When patients can cancel or change a slot easily, silent no-shows go down.",
                ],
            },
            {
                "h2": "Why it works",
                "p": (
                    "People remember a time they chose themselves. They also get a written confirmation instead of relying on a rushed phone call. "
                    "If plans change, they can update the booking instead of simply not arriving. That frees the slot for another patient."
                ),
                "facts": [
                    "Self-chosen times feel more real to patients.",
                    "A message confirmation is harder to forget than a verbal note.",
                    "Easy cancel and reschedule means empty slots can be filled again.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "Patients find a clinic, pick a doctor and time, and confirm on WhatsApp. Your team still controls doctors, leave, and the day list. "
                    "Results always depend on how each clinic runs — but the goal is the same: fewer empty chairs on busy days."
                ),
            },
        ],
    },
    {
        "slug": "less-staff-labor",
        "nav": "Benefits",
        "title": "Less Front-Desk Phone Work | BookMyClinics",
        "meta": "Online booking reduces repetitive phone scheduling so your reception team can focus on patients in the clinic.",
        "h1": "Give your front desk hours back",
        "lead": "Every “Tuesday at 5 or Thursday at 11?” call takes staff time. Online booking lets patients pick the slot themselves.",
        "cta_primary": ("Register your clinic", "https://bookmyclinics.com/clinic.html"),
        "cta_secondary": ("Talk on WhatsApp", "https://wa.me/918511180957?text=Hi%2C%20I%20want%20to%20reduce%20front-desk%20phone%20load%20with%20BookMyClinics"),
        "sections": [
            {
                "h2": "What this means in plain words",
                "p": (
                    "Phone booking needs a person on every call. When many patients only need a simple slot, that work piles up. "
                    "Clinics that add online booking often report less scheduling work for staff — it is one of the most common benefits seen "
                    "after moving bookings online. Some teams saved around 20 staff hours a week on routine booking work after digital scheduling."
                ),
                "facts": [
                    "Less phone scheduling work is one of the most common wins from online booking.",
                    "Staff spend less time repeating the same availability questions.",
                    "Routine bookings move online; complex questions can stay on the phone.",
                ],
            },
            {
                "h2": "Why it works",
                "p": (
                    "Patients can see open times and choose without waiting on hold. Your team stops being the only path to the calendar. "
                    "Reception can focus on walk-ins, payments, and patients who truly need human help."
                ),
                "facts": [
                    "Self-booking removes the middle step for simple appointments.",
                    "Phone lines stay freer for urgent or complex calls.",
                    "Check-in is smoother when the booking already exists.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "BookMyClinics adds an online lane for patients while your clinic portal stays in control of doctors and leave. "
                    "First 25 clinics become Founding Members and stay free forever."
                ),
            },
        ],
    },
    {
        "slug": "shorter-wait-times",
        "nav": "Benefits",
        "title": "Shorter Wait Times | BookMyClinics",
        "meta": "Online booking can cut waiting for a slot and waiting in line to book — patients see open times and reserve faster.",
        "h1": "Shorter waits to get an appointment",
        "lead": "Online booking removes the phone queue and shows open times right away, so patients spend less time waiting to book.",
        "cta_primary": ("Book a doctor", "https://bookmyclinics.com/patient.html"),
        "cta_secondary": ("For clinics", "https://bookmyclinics.com/landings/lp-register.html"),
        "sections": [
            {
                "h2": "What this means in plain words",
                "p": (
                    "Waiting happens twice with old systems: waiting on the phone, then waiting for the next free doctor day. "
                    "Online booking attacks the first wait — and sometimes the second. In one hospital program, average waiting to get an appointment "
                    "fell from about 98 minutes in a queue to about 7 minutes when patients booked online instead of standing in line. "
                    "Other programs got more patients into the right time window because booking no longer depended on a busy desk."
                ),
                "facts": [
                    "Patients stop waiting on hold just to hear available times.",
                    "Open slots are visible, so booking can happen in minutes.",
                    "Freed slots from cancellations can be offered again faster.",
                ],
            },
            {
                "h2": "Why it works",
                "p": (
                    "The calendar is open to the patient. No backlog of phone calls sits between them and a free slot. "
                    "When someone cancels, that time can show up again for the next patient instead of staying hidden."
                ),
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "Patients see live availability for the next two weeks and book without standing in a reception queue. "
                    "Clinics keep doctor schedules accurate so the times patients see are real."
                ),
            },
        ],
    },
    {
        "slug": "higher-patient-satisfaction",
        "nav": "Benefits",
        "title": "Higher Patient Satisfaction | BookMyClinics",
        "meta": "Patients like booking on their own time. Online appointments usually feel easier than waiting on a busy clinic phone.",
        "h1": "Patients are happier when booking is easy",
        "lead": "People prefer choosing a time on their phone over waiting on hold. Easy booking is a big part of how patients judge a clinic.",
        "cta_primary": ("Try patient booking", "https://bookmyclinics.com/patient.html"),
        "cta_secondary": ("Clinic registration", "https://bookmyclinics.com/clinic.html"),
        "sections": [
            {
                "h2": "What this means in plain words",
                "p": (
                    "Satisfaction starts before the doctor visit — at the moment someone tries to book. "
                    "When booking is simple, patients say they would use it again. Many clinics that added online scheduling "
                    "saw better patient satisfaction scores. The reason is simple: ease of use. Book at night, book on Sunday, "
                    "pick the slot that fits work and family — without fighting a busy phone line."
                ),
                "facts": [
                    "Easy online booking is something most patients say they want again.",
                    "Satisfaction often rises when patients control the time themselves.",
                    "Booking outside office hours matters for working families.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "BookMyClinics is built for a simple Gujarat patient journey: find a clinic, choose a doctor and time, confirm on WhatsApp — "
                    "without forcing another heavy app signup for a basic booking."
                ),
            },
        ],
    },
    {
        "slug": "after-hours-booking",
        "nav": "Benefits",
        "title": "24/7 After-Hours Booking | BookMyClinics",
        "meta": "Patients can book doctor appointments at night and on weekends — not only while your reception phone is open.",
        "h1": "Book when the clinic phone is asleep",
        "lead": "Online booking works after hours. Patients can reserve a slot at night or on weekends without calling reception.",
        "cta_primary": ("Open evening booking", "https://bookmyclinics.com/patient.html"),
        "cta_secondary": ("Clinic setup", "https://bookmyclinics.com/landings/lp-register.html"),
        "sections": [
            {
                "h2": "What this means in plain words",
                "p": (
                    "Many people decide to see a doctor after work. If your phone is closed, that intent often dies until tomorrow — "
                    "and tomorrow they may forget or choose another clinic. Real online booking stays open. "
                    "Patients claim free slots anytime the calendar shows them, without waiting for staff to return."
                ),
                "facts": [
                    "After-hours access is one of the biggest practical wins of online booking.",
                    "Night and weekend booking captures demand your phone hours miss.",
                    "You do not need night reception staff for simple slot booking.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "BookMyClinics works on any phone, day or night, against the live calendar your clinic maintains. "
                    "You set doctor shifts and leave; patients stop depending on phone hours to book care."
                ),
            },
        ],
    },
    {
        "slug": "patient-choice-control",
        "nav": "Benefits",
        "title": "Patient Choice of Appointment Time | BookMyClinics",
        "meta": "Online booking lets patients browse open times and choose what fits their life — not only the few slots a caller reads aloud.",
        "h1": "Let patients choose a time that fits real life",
        "lead": "Online booking shows open slots clearly. Patients pick what works — instead of accepting whatever the phone desk offers first.",
        "cta_primary": ("See live clinic slots", "https://bookmyclinics.com/patient.html"),
        "cta_secondary": ("Register a clinic", "https://bookmyclinics.com/clinic.html"),
        "sections": [
            {
                "h2": "What this means in plain words",
                "p": (
                    "On a phone call, patients usually hear two or three options. Online, they can scan the week and choose. "
                    "That control is a core reason online booking feels fairer and easier. Patients book the doctor and time that fit work, travel, and family — "
                    "so the appointment is more likely to stick."
                ),
                "facts": [
                    "A visible calendar gives more real choices than a short phone list.",
                    "Patients feel more in control of their care when they pick the slot.",
                    "Better-fit times mean fewer “this day never worked” no-shows.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "Patients choose clinic, doctor, and time from real availability, then send a clear WhatsApp confirmation. "
                    "Less negotiation on the phone. More clarity for both sides."
                ),
            },
        ],
    },
    {
        "slug": "easier-reschedule-cancel",
        "nav": "Benefits",
        "title": "Easier Reschedule and Cancel | BookMyClinics",
        "meta": "When plans change, online booking makes it easier to cancel or move a slot — so another patient can take the time.",
        "h1": "When plans change, change the booking too",
        "lead": "If cancelling by phone is hard, patients often just do not come. Easy online changes turn no-shows into open slots again.",
        "cta_primary": ("Clinic tools", "https://bookmyclinics.com/landings/lp-register.html"),
        "cta_secondary": ("WhatsApp", "https://wa.me/918511180957?text=Hi%2C%20I%20want%20online%20rescheduling%20for%20my%20clinic"),
        "sections": [
            {
                "h2": "What this means in plain words",
                "p": (
                    "Life changes. Kids get sick. Work runs late. If the only way to cancel is calling a busy line, many people skip the call "
                    "and simply miss the visit. Online booking and messaging make it easier to move or cancel in time. "
                    "Clinics then get the slot back while there is still a chance to fill it."
                ),
                "facts": [
                    "Hard cancellations create silent no-shows.",
                    "Easy reschedule keeps the patient and frees the old slot.",
                    "Large clinics already run self-reschedule paths at high volume.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "Your clinic portal supports day-of needs like cancellations and doctor leave. "
                    "Patients confirm on WhatsApp, so changing a plan starts from a chat they already use."
                ),
            },
        ],
    },
    {
        "slug": "better-slot-utilization",
        "nav": "Benefits",
        "title": "Better Use of Doctor Slots | BookMyClinics",
        "meta": "Online booking helps fill empty and never-booked slots so your clinic calendar works harder.",
        "h1": "Fill the calendar you already opened",
        "lead": "Empty slots cost money even when no patient comes. Online booking helps more of your open times get used.",
        "cta_primary": ("Founding Member offer", "https://bookmyclinics.com/landings/lp-founding.html"),
        "cta_secondary": ("Register online", "https://bookmyclinics.com/clinic.html"),
        "sections": [
            {
                "h2": "What this means in plain words",
                "p": (
                    "You pay for clinic hours whether chairs are full or empty. Online booking makes open times easier to find and book. "
                    "In one medical practice that tracked this carefully, unused appointments fell from about 23% to about 10%, "
                    "and never-booked openings fell from about 9% to under 2% after online scheduling. "
                    "That is more of the same calendar actually serving patients."
                ),
                "facts": [
                    "Unused slots can drop sharply when patients can book online.",
                    "Never-booked openings shrink when availability is visible.",
                    "Late cancellations can be refilled faster online than by phone alone.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "BookMyClinics shows real doctor availability to patients, so open sessions are discoverable — not hidden behind a phone tree. "
                    "You manage leave and daily lists so the calendar stays honest."
                ),
            },
        ],
    },
    {
        "slug": "scheduling-efficiency",
        "nav": "Benefits",
        "title": "More Efficient Scheduling | BookMyClinics",
        "meta": "Online booking completes more scheduling work with less phone back-and-forth — your calendar fills with fewer bottlenecks.",
        "h1": "Scheduling that scales without extra phone lines",
        "lead": "Online booking lets many patients reserve slots at once. Your team handles exceptions — not every single booking call.",
        "cta_primary": ("Start clinic setup", "https://bookmyclinics.com/clinic.html"),
        "cta_secondary": ("See demo path", "https://bookmyclinics.com/landings/lp-demo.html"),
        "sections": [
            {
                "h2": "What this means in plain words",
                "p": (
                    "Efficiency here means more bookings finish without a long phone chain. "
                    "Studies of digital self-booking in outpatient care find much higher scheduling efficiency than old manual methods. "
                    "In one hospital digital program, the share of bookings completed rose from about 83% to about 93% while missed visits fell. "
                    "More of the work gets done. Less of it gets stuck."
                ),
                "facts": [
                    "Self-booking finishes routine scheduling without serial phone handling.",
                    "Staff time shifts to exceptions and in-clinic care.",
                    "More completed bookings, fewer abandoned phone attempts.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "One patient entry point, clinic-controlled calendars, WhatsApp confirmation. "
                    "That is how scheduling gets cleaner on a real reception desk."
                ),
            },
        ],
    },
    {
        "slug": "appointment-reminders",
        "nav": "Benefits",
        "title": "Appointment Reminders | BookMyClinics",
        "meta": "Reminders help patients remember the visit. Booking plus a message confirmation cuts forgetful no-shows.",
        "h1": "Reminders turn bookings into arrivals",
        "lead": "People forget. A clear message after booking keeps the visit on their mind until they walk in.",
        "cta_primary": ("WhatsApp clinic setup", "https://wa.me/918511180957?text=Hi%2C%20I%20want%20booking%20reminders%20for%20my%20clinic"),
        "cta_secondary": ("Register online", "https://bookmyclinics.com/clinic.html"),
        "sections": [
            {
                "h2": "What this means in plain words",
                "p": (
                    "Even a perfect booking fails if the patient forgets the day. Message reminders are one of the simplest ways to cut missed visits. "
                    "They also push people who cannot come to cancel earlier — which frees the slot for someone else. "
                    "Online booking plus a confirmation message is stronger than a phone note alone."
                ),
                "facts": [
                    "Reminders reduce forgotten appointments.",
                    "Early cancels are better than empty chairs.",
                    "A chat confirmation stays visible on the patient’s phone.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "BookMyClinics confirmations go over WhatsApp — the app most patients in India already check — "
                    "so the booking does not disappear into a missed paper note."
                ),
            },
        ],
    },
    {
        "slug": "less-phone-bottleneck",
        "nav": "Benefits",
        "title": "Less Phone-Line Bottleneck | BookMyClinics",
        "meta": "When booking only works by phone, busy lines block care even if doctors still have open slots. Online booking adds another door.",
        "h1": "Stop making care wait on a busy signal",
        "lead": "A full phone line feels like a closed clinic — even when doctors still have free times. Online booking opens a second door.",
        "cta_primary": ("Move bookings online", "https://bookmyclinics.com/landings/lp-register.html"),
        "cta_secondary": ("Patient booking", "https://bookmyclinics.com/patient.html"),
        "sections": [
            {
                "h2": "What this means in plain words",
                "p": (
                    "Old booking is limited by how many calls staff can take. Patients give up when the line is busy, "
                    "even if the doctor calendar still has openings. Online booking removes that choke point for simple appointments. "
                    "Your phone stays for questions that need a human voice."
                ),
                "facts": [
                    "Phone capacity is not the same as doctor capacity.",
                    "Online booking clears demand against real open slots.",
                    "Reception phones become freer for real conversations.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "Patients who can self-serve book online. Your staff keep the line for everything else. "
                    "Not “no phones ever” — just phones no longer being the only door."
                ),
            },
        ],
    },
    {
        "slug": "smoother-checkin",
        "nav": "Benefits",
        "title": "Smoother Clinic Check-In | BookMyClinics",
        "meta": "When the booking is clear before arrival, reception spends less time fixing confusion and more time starting the visit.",
        "h1": "Start the visit before the patient walks in",
        "lead": "A clear online booking means reception already knows who is coming, for which doctor, and at what time.",
        "cta_primary": ("Clinic onboarding", "https://bookmyclinics.com/clinic.html"),
        "cta_secondary": ("Benefits index", "./"),
        "sections": [
            {
                "h2": "What this means in plain words",
                "p": (
                    "Walk-in chaos at the desk wastes the first minutes of care. Online booking creates a known appointment before arrival. "
                    "Many online systems also let patients review basic details ahead of time, so check-in is faster and misunderstandings drop. "
                    "Reception starts from a real booking — not a vague “I called someone yesterday.”"
                ),
                "facts": [
                    "Known bookings make lobby flow calmer.",
                    "Less paperwork panic at peak hours.",
                    "Staff help the visit start, not rebuild the appointment from scratch.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "BookMyClinics captures clinic, doctor, slot, and WhatsApp confirmation up front. "
                    "Arrival matches what the calendar already promised."
                ),
            },
        ],
    },
    {
        "slug": "increased-revenue",
        "nav": "Benefits",
        "title": "Protect Clinic Revenue with Online Booking | BookMyClinics",
        "meta": "Online booking helps clinics earn more from the same open hours by filling empty slots and cutting missed visits — not by raising fees.",
        "h1": "Revenue follows filled appointment time",
        "lead": "You do not need higher fees to earn more. You need fewer empty chairs when the doctor is already there.",
        "cta_primary": ("Become a Founding Member", "https://bookmyclinics.com/landings/lp-founding.html"),
        "cta_secondary": ("Register your clinic", "https://bookmyclinics.com/clinic.html"),
        "sections": [
            {
                "h2": "What this means in plain words",
                "p": (
                    "Clinic income sits in used doctor time. Missed visits and never-filled openings leave paid hours empty. "
                    "Online booking helps in three simple ways: fewer no-shows, faster refill of cancelled times, and more of your open slots actually getting booked. "
                    "In practice data, unused appointments have fallen from about 23% to about 10%, and never-booked openings from about 9% to under 2%, "
                    "after online scheduling. That is recovered capacity — the same clinic hours doing more work."
                ),
                "facts": [
                    "Fewer missed visits protect billable doctor time.",
                    "Visible open slots get filled instead of staying empty.",
                    "Cancelled times can return to the calendar quickly.",
                ],
            },
            {
                "h2": "How empty slots become lost money",
                "p": (
                    "Staff costs and clinic rent do not pause when a patient does not arrive. "
                    "Long waits also push patients to other clinics. Online booking shortens the path to a slot and keeps more of your day productive."
                ),
                "facts": [
                    "An empty chair still costs you to keep the clinic open.",
                    "Patients who cannot book easily may go elsewhere.",
                    "Better fill rate means better use of the same team.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "We make your open sessions easy for patients to find and confirm on WhatsApp. "
                    "No fake promises of a fixed income number — just a clearer path to fewer empty chairs on days you are already open."
                ),
            },
        ],
    },
    {
        "slug": "lower-operating-cost",
        "nav": "Benefits",
        "title": "Lower Scheduling Costs | BookMyClinics",
        "meta": "Online booking lowers the cost of getting patients on the calendar by cutting phone labor and wasted empty sessions.",
        "h1": "Cut the cost of getting someone on the calendar",
        "lead": "Scheduling by phone only is expensive staff time. Online booking reduces that cost and wastes fewer paid clinic hours.",
        "cta_primary": ("Register online", "https://bookmyclinics.com/clinic.html"),
        "cta_secondary": ("WhatsApp", "https://wa.me/918511180957?text=Hi%2C%20I%20want%20to%20lower%20scheduling%20costs%20with%20BookMyClinics"),
        "sections": [
            {
                "h2": "What this means in plain words",
                "p": (
                    "The cost of booking is mostly people answering phones. When online booking takes the routine slots, "
                    "clinics need fewer hours of pure scheduling labor — sometimes around 20 hours a week saved on booking admin in published digital programs. "
                    "There is a second cost too: paying staff through empty sessions. When unused slots fall, your team’s time is spent on real patients."
                ),
                "facts": [
                    "Less phone booking work means lower admin cost per appointment.",
                    "Fewer empty sessions mean better value from staff already on duty.",
                    "Online booking scales without adding more phone lines.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "Patients self-serve routine slots. Your team keeps control of doctors and leave. "
                    "First 25 clinics stay free forever as Founding Members — so you are not swapping phone labor for a heavy software bill while you prove the flow."
                ),
            },
        ],
    },
    {
        "slug": "clearer-visit-reasons",
        "nav": "Benefits",
        "title": "Clearer Visit Details | BookMyClinics",
        "meta": "Patients often explain their problem more clearly when booking online than when rushed on a phone call.",
        "h1": "Clearer visit details before the patient arrives",
        "lead": "Online booking gives patients space to say why they are coming — which helps your team prepare.",
        "cta_primary": ("See patient booking", "https://bookmyclinics.com/patient.html"),
        "cta_secondary": ("Clinic registration", "https://bookmyclinics.com/landings/lp-register.html"),
        "sections": [
            {
                "h2": "What this means in plain words",
                "p": (
                    "On a rushed phone call, many patients give short or incomplete reasons — especially for private or sensitive problems. "
                    "When people type for themselves online, they often share clearer detail. That helps reception and doctors prepare the right kind of visit "
                    "instead of discovering the real issue only after the patient sits down."
                ),
                "facts": [
                    "Written booking details are often clearer than quick phone notes.",
                    "Sensitive concerns are easier to share without saying them aloud to a stranger on the phone.",
                    "Better detail means fewer wrong visit types and less lobby confusion.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "Each booking carries clinic, doctor, and time into a WhatsApp confirmation both sides can see. "
                    "Reception starts from a clear appointment, not a half-remembered call."
                ),
            },
        ],
    },
]


def slug_to_title(slug: str) -> str:
    return BENEFITS[[b["slug"] for b in BENEFITS].index(slug)]["h1"]


def render_page(b: dict, idx: int) -> str:
    img = IMAGES[idx % len(IMAGES)]
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
  <section class="cta-band">
    <h2>Ready to try this in your clinic?</h2>
    <p>First 25 clinics become Founding Members on BookMyClinics — free forever.</p>
    <div class="cta-row">
      <a class="btn btn-teal" href="https://bookmyclinics.com/clinic.html">Register Your Clinic</a>
      <a class="btn btn-ghost" href="./">All {len(BENEFITS)} benefits</a>
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
  <title>{len(BENEFITS)} Benefits of Online Appointment Booking | BookMyClinics</title>
  <meta name="description" content="Simple explanations of {len(BENEFITS)} real benefits of online doctor appointment booking for clinics and patients.">
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
    <h1>{len(BENEFITS)} benefits of online appointment booking</h1>
    <p class="hub-lead">Each page explains one benefit in simple English — why online booking helps clinics and patients, without heavy research jargon.</p>
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
        <strong>Benefits library · {n} pages</strong>
        <span>Simple English explanations of why online appointment booking helps clinics and patients</span>
      </a>"""
        html = html.replace(
            '      <a class="hub-item" href="lp-partners.html">',
            inject + "\n      <a class=\"hub-item\" href=\"lp-partners.html\">",
        )
    html = re.sub(
        r"(?:Evidence|Benefits) library · \d+(?: benefit)? pages",
        f"Benefits library · {n} pages",
        html,
    )
    html = re.sub(
        r"a \d+-page (?:evidence )?library[^.]*\.",
        f"a {n}-page benefits library in simple English.",
        html,
    )
    html = html.replace(
        "Five purpose-built pages for patients, clinics, demo, founding partners, and team growth.",
        f"Funnel pages plus a {n}-page benefits library in simple English.",
    )
    html = html.replace(
        "Documented research on online appointment booking — one landing page per benefit",
        "Simple English explanations of why online appointment booking helps clinics and patients",
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
