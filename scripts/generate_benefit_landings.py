#!/usr/bin/env python3
"""Generate benefit landing pages for BookMyClinics (simple English, expanded copy)."""

from pathlib import Path
import re
from datetime import date

ROOT = Path("/workspace")
OUT = ROOT / "landings" / "benefits"
OUT.mkdir(parents=True, exist_ok=True)

TODAY = date.today().isoformat()
SITE = "https://bookmyclinics.com"
WA_CLINIC = "https://wa.me/918511180957?text=Hi%2C%20I%20want%20to%20register%20my%20clinic%20on%20BookMyClinics"
WA_PATIENT = "https://wa.me/918511180957?text=Hi%2C%20I%20want%20to%20book%20a%20doctor%20on%20BookMyClinics"

IMG = {
    "reception":  "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=1600&q=70",
    "doctor":     "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=1600&q=70",
    "stetho":     "https://images.unsplash.com/photo-1631815588090-d4bfec5b1ccb?auto=format&fit=crop&w=1600&q=70",
    "equipment":  "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=1600&q=70",
    "consult":    "https://images.unsplash.com/photo-1584982751601-97dcc096659c?auto=format&fit=crop&w=1600&q=70",
    "team":       "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?auto=format&fit=crop&w=1600&q=70",
    "phonehand":  "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?auto=format&fit=crop&w=1600&q=70",
    "waiting":    "https://images.unsplash.com/photo-1538108149393-fbbd81895907?auto=format&fit=crop&w=1600&q=70",
    "corridor":   "https://images.unsplash.com/photo-1504439468489-c8920d796a29?auto=format&fit=crop&w=1600&q=70",
    "handshake":  "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&w=1600&q=70",
    "calendar":   "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?auto=format&fit=crop&w=1600&q=70",
    "nightphone": "https://images.unsplash.com/photo-1529653762956-b0a27278529c?auto=format&fit=crop&w=1600&q=70",
    "family":     "https://images.unsplash.com/photo-1609220136736-443140cffec6?auto=format&fit=crop&w=1600&q=70",
    "smile":      "https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=1600&q=70",
    "desk":       "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=1600&q=70",
}

# Ordered for the hub: money first, operations second, patient experience third.
BENEFITS = [
    # ---------------- MONEY ----------------
    {
        "slug": "increased-revenue",
        "group": "Grow your clinic",
        "audience": "clinic",
        "img": IMG["handshake"],
        "title": "Protect Clinic Revenue with Online Booking | BookMyClinics",
        "meta": "Online booking helps clinics earn more from the same open hours — fewer empty chairs, faster refills of cancelled slots, no fee increase needed.",
        "h1": "Revenue follows filled appointment time",
        "lead": "You do not need higher fees to earn more. You need fewer empty chairs on days the doctor is already sitting in the clinic.",
        "sections": [
            {
                "h2": "The empty chair problem",
                "p": (
                    "Think about last Tuesday evening. The doctor was in, the lights were on, the staff were paid — and two patients "
                    "simply did not come. Nobody called to cancel. Those two slots earned nothing, and no other patient could take them "
                    "because nobody knew they were free. Now multiply that by six days a week, fifty-two weeks a year. "
                    "That is where clinic revenue quietly leaks. Not from low fees — from paid doctor time that nobody used."
                ),
                "facts": [
                    "An empty slot costs you rent, staff salary, and doctor time — with zero income.",
                    "Most clinics lose slots to silent no-shows and cancellations that never get refilled.",
                    "The fix is not charging more. It is filling more of what you already have.",
                ],
            },
            {
                "h2": "How online booking recovers that money",
                "p": (
                    "Online booking attacks the leak from three sides at once. First, patients who choose their own time are far less likely "
                    "to disappear — clinics that moved booking online have seen missed visits fall sharply, in some cases from around 8% to under 2%. "
                    "Second, when someone cancels online, the slot goes straight back on the calendar where the next patient can grab it — "
                    "no phone round-trips needed. Third, open times become visible to everyone, so slots that used to sit unknown and unbooked "
                    "actually get taken. Clinics that measured this carefully saw unused appointments drop from roughly a quarter of the calendar "
                    "to about one in ten."
                ),
                "facts": [
                    "Fewer no-shows protect the doctor hours you already pay for.",
                    "Cancelled times return to the calendar in minutes, not days.",
                    "Slots patients could never see before now get discovered and booked.",
                ],
            },
            {
                "h2": "A simple way to think about it",
                "p": (
                    "If your clinic runs 40 appointment slots a day and 6 go empty, that is 15% of your capacity earning nothing. "
                    "Cut that waste in half and you have added three paid visits a day without extending hours, hiring anyone, "
                    "or touching your fees. Over a month, that is around 75 extra visits from the same clinic, the same team, the same electricity bill. "
                    "This is why filling slots is the fastest revenue improvement most clinics can make — it needs no new investment, only a better door for patients to walk through."
                ),
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "BookMyClinics makes your open sessions easy for patients to find, and every booking is confirmed on WhatsApp so it sticks. "
                    "Your team keeps full control of doctors, timings, and leave. We will not promise you a fixed income number — every clinic is different — "
                    "but the goal is simple and honest: fewer empty chairs on days you are already open. "
                    "And because the first 25 clinics join free forever as Founding Members, the extra revenue is not eaten by a software bill."
                ),
            },
        ],
        "related": ["fewer-no-shows", "better-slot-utilization", "lower-operating-cost"],
    },
    {
        "slug": "fewer-no-shows",
        "group": "Grow your clinic",
        "audience": "clinic",
        "img": IMG["calendar"],
        "title": "Fewer Missed Appointments | BookMyClinics",
        "meta": "Patients who book online and pick their own time show up more often. Online booking helps clinics cut no-shows without chasing anyone by phone.",
        "h1": "Fewer missed appointments",
        "lead": "When patients choose their own slot and get a written confirmation, they show up. Missed visits fall — sometimes dramatically.",
        "sections": [
            {
                "h2": "A story every clinic knows",
                "p": (
                    "A patient calls on Monday and books for Thursday evening. Reception writes it in the register. "
                    "By Thursday the patient is not sure — was it 6 o'clock or 7? Was it this Thursday or next? "
                    "Calling to check feels like a bother, so he decides to come \"sometime\" — and then does not come at all. "
                    "The doctor waited, the slot died, and the patient still needs care. Nobody did anything wrong. "
                    "The system itself made forgetting easy: a verbal time, no confirmation, and no simple way to check or change the booking."
                ),
                "facts": [
                    "Most no-shows are not careless patients — they are forgotten or unclear bookings.",
                    "A verbal phone booking has nothing the patient can look at later.",
                    "If cancelling is hard, patients skip the visit silently instead.",
                ],
            },
            {
                "h2": "What changes with online booking",
                "p": (
                    "Online booking fixes exactly the weak points in that story. The patient picks the time himself, so it is a time that "
                    "actually fits his life — not the first gap reception offered. He gets a confirmation on his phone that he can re-read "
                    "any moment. And if Thursday stops working, he can change or cancel in seconds instead of avoiding an awkward call. "
                    "Clinics and health systems that moved to online booking have watched missed visits drop — from around 8% with phone-only "
                    "booking to as low as 1–2% for online bookings in some places, with several clinics reporting missed appointments falling by "
                    "roughly 40% overall."
                ),
                "facts": [
                    "Self-chosen times fit real life, so patients keep them.",
                    "A confirmation message on the phone is hard to forget.",
                    "Easy cancel and reschedule turns silent no-shows into open slots you can refill.",
                ],
            },
            {
                "h2": "Why this matters beyond money",
                "p": (
                    "Every no-show is also a patient who did not get care and another patient who could not get that slot. "
                    "Reducing missed visits means shorter queues for everyone, less idle doctor time, and fewer awkward evening gaps "
                    "in the middle of a busy day. It makes the whole clinic run the way the calendar said it would."
                ),
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "Patients find your clinic, pick a doctor and a live slot, and confirm on WhatsApp — the app they already check every day. "
                    "Your team still controls doctors, timings, and leave from the clinic portal. "
                    "Results always depend on how each clinic runs, but the goal is the same everywhere: fewer empty chairs, more completed visits."
                ),
            },
        ],
        "related": ["appointment-reminders", "easier-reschedule-cancel", "increased-revenue"],
    },
    {
        "slug": "less-staff-labor",
        "group": "Grow your clinic",
        "audience": "clinic",
        "img": IMG["desk"],
        "title": "Less Front-Desk Phone Work | BookMyClinics",
        "meta": "Online booking takes repetitive scheduling calls off your reception team so they can focus on patients standing in front of them.",
        "h1": "Give your front desk hours back",
        "lead": "Every \"Tuesday at 5 or Thursday at 11?\" call takes staff time. Online booking lets patients answer that question themselves.",
        "sections": [
            {
                "h2": "Where reception time really goes",
                "p": (
                    "Watch a clinic reception desk for one hour. A big share of the phone calls are the same conversation on repeat: "
                    "which doctor is available, which day, which time, hold on while I check, no that slot is gone, what about Thursday. "
                    "Each call takes a few minutes — and while your staff member is on that call, the patient standing at the desk waits, "
                    "the second phone line rings unanswered, and the queue grows. None of this is bad staff work. "
                    "It is good staff trapped doing work a calendar could do by itself."
                ),
                "facts": [
                    "Routine slot-picking calls eat a large share of reception time.",
                    "Every booking call blocks the line for the next caller.",
                    "Patients at the desk wait while staff repeat availability on the phone.",
                ],
            },
            {
                "h2": "What changes when patients self-book",
                "p": (
                    "When patients can see open times and pick one online, the routine calls simply stop happening. "
                    "Clinics that added online booking consistently report less scheduling workload — it is one of the most commonly "
                    "seen benefits when bookings move online. Some hospital teams measured around 20 staff hours per week saved on "
                    "booking admin after switching to digital scheduling. That time does not disappear — it moves to work that actually needs a human: "
                    "helping elderly patients, handling payments, managing the day's queue, and answering questions that a calendar cannot."
                ),
                "facts": [
                    "Less phone scheduling is one of the most common wins clinics report.",
                    "Teams have saved on the order of 20 staff hours a week on booking admin.",
                    "Staff attention returns to patients physically in the clinic.",
                ],
            },
            {
                "h2": "Your phone still matters — for the right calls",
                "p": (
                    "This is not about switching the phone off. Some patients will always prefer to call, and complex cases need conversation. "
                    "The point is choice: simple bookings flow online by themselves, and your phone line stays free for the calls that truly need it. "
                    "The desk feels calmer, and callers who do phone in get answered faster because the line is not jammed with slot-picking."
                ),
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "BookMyClinics adds an online booking lane while your clinic portal keeps full control of doctors, schedules, and leave. "
                    "Patients confirm on WhatsApp, so reception can see clean bookings instead of scribbled phone notes. "
                    "First 25 clinics join as Founding Members — free forever."
                ),
            },
        ],
        "related": ["less-phone-bottleneck", "lower-operating-cost", "smoother-checkin"],
    },
    {
        "slug": "lower-operating-cost",
        "group": "Grow your clinic",
        "audience": "clinic",
        "img": IMG["team"],
        "title": "Lower Scheduling Costs | BookMyClinics",
        "meta": "Phone-only booking is expensive staff time. Online booking cuts the cost per appointment and wastes fewer paid clinic hours.",
        "h1": "Cut the cost of getting someone on the calendar",
        "lead": "Booking by phone only means paying staff to do what a calendar can do free. Online booking lowers that cost — and wastes fewer paid hours.",
        "sections": [
            {
                "h2": "What one appointment really costs you",
                "p": (
                    "Every phone booking has a hidden price: a few minutes of staff salary spent on the call, plus the calls that "
                    "did not end in a booking at all — the busy signals, the call-backs, the \"let me check and call you again.\" "
                    "When your only booking channel is the phone, that cost repeats for every single appointment, every single day. "
                    "Clinics rarely calculate it because it hides inside salaries — but it is real money, paid monthly, for work that "
                    "patients are happy to do themselves."
                ),
                "facts": [
                    "Each phone booking consumes paid staff minutes — including the failed calls around it.",
                    "The cost hides inside salaries, so most clinics never see it clearly.",
                    "Online self-booking handles routine slots at nearly zero marginal cost.",
                ],
            },
            {
                "h2": "The second hidden cost: empty sessions",
                "p": (
                    "There is another cost most clinics carry silently: paying the whole team through sessions that are partly empty. "
                    "When slots go unbooked or patients do not show, your rent, salaries, and electricity keep running against zero income. "
                    "Clinics that moved booking online have seen unused appointments fall from around 23% of the calendar to about 10% — "
                    "meaning the same staffing cost now serves many more actual patients. Digital scheduling programs have also reported "
                    "saving around 20 hours of admin work per week. Fewer wasted slots plus fewer wasted hours is how operating cost per patient comes down."
                ),
                "facts": [
                    "Unused slots have dropped from roughly 23% to 10% after online booking in measured clinics.",
                    "Around 20 admin hours a week saved is a realistic outcome seen in digital scheduling programs.",
                    "Lower waste means each patient visit carries less overhead cost.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "Patients self-serve the routine slots; your team keeps control of doctors and leave and handles only the exceptions. "
                    "And because the first 25 clinics stay free forever as Founding Members, you are not trading phone labor for a heavy "
                    "software subscription while you prove the workflow in your own clinic."
                ),
            },
        ],
        "related": ["less-staff-labor", "increased-revenue", "scheduling-efficiency"],
    },
    {
        "slug": "better-slot-utilization",
        "group": "Grow your clinic",
        "audience": "clinic",
        "img": IMG["corridor"],
        "title": "Better Use of Doctor Slots | BookMyClinics",
        "meta": "Online booking helps fill empty and never-booked slots so more of your clinic calendar actually serves patients.",
        "h1": "Fill the calendar you already opened",
        "lead": "Empty slots cost money even when no patient comes. Online booking helps more of your open times actually get used.",
        "sections": [
            {
                "h2": "The slots nobody ever sees",
                "p": (
                    "Here is a strange truth about phone-only clinics: some appointment slots are never booked simply because "
                    "no patient ever knew they existed. The doctor added an extra evening session; reception mentioned it to a few callers; "
                    "the rest of the city had no idea. The slot sat open, then expired. That is not a demand problem — plenty of patients "
                    "wanted a doctor that evening. It is a visibility problem. Your calendar and your patients could not see each other."
                ),
                "facts": [
                    "Slots hidden behind a phone line often expire unbooked.",
                    "The demand usually exists — patients just cannot see the opening.",
                    "Extra sessions and schedule changes are hardest to fill by phone alone.",
                ],
            },
            {
                "h2": "What measured clinics found",
                "p": (
                    "One medical practice that tracked this carefully saw unused appointments fall from about 23% to about 10% "
                    "after moving booking online, and never-booked openings fall from about 9% to under 2%. "
                    "The mechanics are simple: when open times are published where patients already look, they get taken. "
                    "And when someone cancels late, the freed slot goes straight back into view — so instead of dying quietly, "
                    "it often gets picked up by the next patient searching that evening."
                ),
                "facts": [
                    "Unused appointments: roughly 23% down to 10% after online booking.",
                    "Never-booked openings: roughly 9% down to under 2%.",
                    "Late cancellations get refilled instead of wasted.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "BookMyClinics shows your real doctor availability to patients across your city, so open sessions are discoverable "
                    "instead of hidden behind a phone tree. You manage leave and day lists in the clinic portal, which keeps the public calendar honest — "
                    "patients only see slots that truly exist. More of the calendar you already pay for ends up doing what it was made for: seeing patients."
                ),
            },
        ],
        "related": ["increased-revenue", "fewer-no-shows", "after-hours-booking"],
    },
    # ---------------- OPERATIONS ----------------
    {
        "slug": "less-phone-bottleneck",
        "group": "Run smoother",
        "audience": "clinic",
        "img": IMG["phonehand"],
        "title": "Less Phone-Line Bottleneck | BookMyClinics",
        "meta": "A busy phone line feels like a closed clinic even when doctors have free slots. Online booking opens a second door for patients.",
        "h1": "Stop making care wait on a busy signal",
        "lead": "A full phone line feels like a closed clinic — even when doctors still have free times. Online booking opens a second door.",
        "sections": [
            {
                "h2": "Phone capacity is not doctor capacity",
                "p": (
                    "Your clinic can see forty patients a day, but your phone can hold one conversation at a time. "
                    "At 9 a.m. when everyone calls at once, the real limit on your clinic is not the doctor — it is the busy signal. "
                    "Patients who cannot get through do not queue politely and retry all morning. Some try twice and give up. "
                    "Some go to whichever clinic answered first. Your calendar may have had exactly the slot they wanted. They never found out."
                ),
                "facts": [
                    "One phone line means one booking conversation at a time — regardless of how many slots are free.",
                    "Peak-hour callers often give up after a couple of busy signals.",
                    "Lost callers sometimes become another clinic's patients.",
                ],
            },
            {
                "h2": "The second door",
                "p": (
                    "Online booking is a door that is never engaged, never on hold, and never closed for lunch. "
                    "A hundred patients can look at your calendar at the same moment, and each one books against real open slots. "
                    "The clinics that add this lane see the pressure come off the phone line naturally: routine bookings drain away to the calendar, "
                    "and the phone becomes what it should be — a line for questions, follow-ups, and people who genuinely need to talk to a human. "
                    "Callers get through faster precisely because the simple traffic went elsewhere."
                ),
                "facts": [
                    "Unlimited patients can browse and book at the same time.",
                    "Routine bookings drain off the phone line automatically.",
                    "The patients who do call get answered sooner.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "Patients who can self-serve book online through BookMyClinics; your staff keep the phone for everything else. "
                    "This is not \"no phones ever\" — it is phones no longer being the only way into your clinic."
                ),
            },
        ],
        "related": ["less-staff-labor", "after-hours-booking", "scheduling-efficiency"],
    },
    {
        "slug": "scheduling-efficiency",
        "group": "Run smoother",
        "audience": "clinic",
        "img": IMG["equipment"],
        "title": "More Efficient Scheduling | BookMyClinics",
        "meta": "Online booking completes more scheduling work with less back-and-forth. More bookings finish, fewer get stuck half-way.",
        "h1": "Scheduling that scales without extra phone lines",
        "lead": "Online booking lets many patients reserve slots at once. Your team handles the exceptions — not every single booking.",
        "sections": [
            {
                "h2": "How a booking gets stuck",
                "p": (
                    "A phone booking is a chain: patient calls, line is free or not, staff finds the register, availability is read out, "
                    "a time is negotiated, a name is written. If any link breaks — busy line, lunch hour, misheard name, page not found — "
                    "the booking stalls or dies, and someone has to start over. Multiply that chain by every appointment in your week "
                    "and you can see why scheduling eats so much energy. Every step needs a human, and every human step can drop the ball."
                ),
                "facts": [
                    "Phone booking is a multi-step chain, and every step can fail.",
                    "Failed calls create repeat work: call-backs, re-checks, re-negotiation.",
                    "The register itself becomes a bottleneck at busy hours.",
                ],
            },
            {
                "h2": "What efficiency actually looks like",
                "p": (
                    "With online booking, the whole chain collapses into one step the patient completes alone: see the open slots, tap one, done. "
                    "Studies of digital self-booking in outpatient care find far higher scheduling efficiency than manual methods — "
                    "in one hospital program, completed bookings rose from about 83% to about 93% while missed visits fell at the same time. "
                    "The important word is completed. Not attempted, not half-arranged, not \"call back tomorrow\" — finished bookings sitting cleanly on the calendar."
                ),
                "facts": [
                    "Booking completion rose from about 83% to 93% in one measured digital program.",
                    "Self-booking removes the human chain from routine appointments.",
                    "Staff intervene only on exceptions, not on every booking.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "One patient entry point, clinic-controlled calendars, WhatsApp confirmation on every booking. "
                    "The reception desk stops being an assembly line for slot-picking and becomes what it should be — the welcome desk of your clinic."
                ),
            },
        ],
        "related": ["less-phone-bottleneck", "lower-operating-cost", "smoother-checkin"],
    },
    {
        "slug": "easier-reschedule-cancel",
        "group": "Run smoother",
        "audience": "clinic",
        "img": IMG["consult"],
        "title": "Easier Reschedule and Cancel | BookMyClinics",
        "meta": "When cancelling is easy, patients cancel instead of vanishing — and the freed slot can go to another patient in time.",
        "h1": "When plans change, change the booking too",
        "lead": "If cancelling by phone is a chore, patients simply do not come. Easy changes turn silent no-shows into open slots you can refill.",
        "sections": [
            {
                "h2": "Why patients vanish instead of cancelling",
                "p": (
                    "Nobody plans to waste a doctor's time. But life interferes: a child gets sick, the boss calls a meeting, the bus is late. "
                    "Now the patient has to phone your clinic, wait on the line, explain, apologize, maybe negotiate a new time — all to deliver bad news. "
                    "Many people quietly avoid that call. They just do not come, and they feel too awkward to rebook later. "
                    "The clinic loses the slot and often loses the patient. All because cancelling was harder than disappearing."
                ),
                "facts": [
                    "Cancelling by phone feels awkward, so many patients skip it entirely.",
                    "A silent no-show wastes the slot and often the patient relationship too.",
                    "The easier the change, the earlier the clinic finds out.",
                ],
            },
            {
                "h2": "What easy changes unlock",
                "p": (
                    "When changing a booking takes seconds on a phone screen, patients actually do it — and early. "
                    "An early cancellation is completely different from a no-show: the slot returns to the calendar while there is still time "
                    "to fill it with someone else. The patient stays in the system too, usually rebooking for a better day instead of dropping out of care. "
                    "Large health systems now run patient self-reschedule at massive volume — hundreds of thousands of self-managed changes a year — "
                    "because it keeps calendars accurate and patients attached."
                ),
                "facts": [
                    "Early cancels give you time to refill the slot.",
                    "Patients who can reschedule easily usually rebook instead of disappearing.",
                    "Self-managed changes keep the calendar honest hour by hour.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "Your clinic portal handles the day-of realities — cancellations, doctor leave, exports — while patients confirm and "
                    "communicate on WhatsApp, a chat thread they already use. Changing a plan starts from a message, not from an awkward phone call nobody wants to make."
                ),
            },
        ],
        "related": ["fewer-no-shows", "appointment-reminders", "better-slot-utilization"],
    },
    {
        "slug": "appointment-reminders",
        "group": "Run smoother",
        "audience": "clinic",
        "img": IMG["nightphone"],
        "title": "Appointment Reminders | BookMyClinics",
        "meta": "A clear message after booking keeps the visit on the patient's mind. Reminders cut forgetful no-shows and trigger earlier cancels.",
        "h1": "Reminders turn bookings into arrivals",
        "lead": "People forget. A clear message after booking keeps the visit on their mind until they walk through your door.",
        "sections": [
            {
                "h2": "Forgetting is the most human no-show",
                "p": (
                    "A patient books a check-up ten days in advance. Ten days is a long time: work deadlines, a wedding, school exams. "
                    "By the appointment day, the visit has simply slipped his mind — not because he did not care, but because nothing reminded him. "
                    "Phone bookings leave no trace on the patient's side. There is nothing to glance at, nothing that pops up the evening before. "
                    "The longer the gap between booking and visit, the more likely the memory fails."
                ),
                "facts": [
                    "Long gaps between booking and visit are where memory fails most.",
                    "A phone booking leaves nothing on the patient's side to check.",
                    "Forgotten visits are the most preventable kind of no-show.",
                ],
            },
            {
                "h2": "What a simple message changes",
                "p": (
                    "Message reminders are one of the simplest and best-proven tools in appointment care. They cut missed visits, "
                    "and they do a second, less obvious job: patients who realize they cannot come tend to cancel when the reminder arrives — "
                    "early enough for the clinic to offer the slot to someone else. A booking that lives in the patient's chat history works "
                    "even before any reminder is sent: he can scroll back any time and see the day, the time, and the doctor's name in writing."
                ),
                "facts": [
                    "Reminders reliably reduce forgotten appointments.",
                    "They trigger early cancels — far better than empty chairs.",
                    "A written confirmation is a reminder the patient carries in his pocket.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "BookMyClinics confirmations travel over WhatsApp — the app most patients in India check many times a day. "
                    "The booking sits in a chat thread the patient will see again, instead of disappearing into a paper note or a half-remembered call."
                ),
            },
        ],
        "related": ["fewer-no-shows", "easier-reschedule-cancel", "higher-patient-satisfaction"],
    },
    {
        "slug": "smoother-checkin",
        "group": "Run smoother",
        "audience": "clinic",
        "img": IMG["reception"],
        "title": "Smoother Clinic Check-In | BookMyClinics",
        "meta": "When the booking is clear before arrival, reception spends less time untangling confusion and more time starting the visit.",
        "h1": "Start the visit before the patient walks in",
        "lead": "A clear online booking means reception already knows who is coming, for which doctor, at what time — before the door opens.",
        "sections": [
            {
                "h2": "The desk at 9:30 in the morning",
                "p": (
                    "Peak hour at any clinic desk looks the same: one patient insists he called yesterday and someone wrote his name somewhere; "
                    "another is at the wrong doctor's queue; a third booked for his mother but came himself. Staff dig through the register, "
                    "make apologetic phone calls, and rebuild bookings from memory while the queue behind grows restless. "
                    "The first ten minutes of many visits are spent not on care, but on figuring out what the appointment even was."
                ),
                "facts": [
                    "Unclear bookings turn reception into detective work.",
                    "Peak-hour confusion delays every patient in the queue, not just one.",
                    "Verbal bookings are the hardest to verify when it matters.",
                ],
            },
            {
                "h2": "Arrival with a clean booking",
                "p": (
                    "An online booking arrives at your desk already complete: patient name, doctor, date, time — written, confirmed, findable. "
                    "Check-in becomes a ten-second lookup instead of an interrogation. Many online systems also let patients review "
                    "basic details ahead of the visit, which cuts misunderstandings before they happen. The lobby feels calmer because "
                    "the queue moves; staff feel calmer because they start each visit from facts, not fragments."
                ),
                "facts": [
                    "A complete written booking makes check-in a ten-second job.",
                    "Fewer misunderstandings at the desk means a faster-moving queue.",
                    "Staff start visits from facts instead of rebuilding them from memory.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "Every BookMyClinics booking carries clinic, doctor, slot, and a WhatsApp confirmation both sides can see. "
                    "Arrival matches what the calendar promised — and your front desk finally gets to greet patients instead of cross-examining them."
                ),
            },
        ],
        "related": ["clearer-visit-reasons", "less-staff-labor", "scheduling-efficiency"],
    },
    {
        "slug": "clearer-visit-reasons",
        "group": "Run smoother",
        "audience": "clinic",
        "img": IMG["doctor"],
        "title": "Clearer Visit Details | BookMyClinics",
        "meta": "Patients explain their problem more clearly when booking online than when rushed on a phone call — which helps your team prepare.",
        "h1": "Clearer visit details before the patient arrives",
        "lead": "Online booking gives patients space to say why they are coming — which helps your team prepare the right visit.",
        "sections": [
            {
                "h2": "What gets lost on a phone call",
                "p": (
                    "On a rushed phone call, a patient gives the shortest possible version: \"stomach problem,\" \"check-up,\" \"for my father.\" "
                    "Some details are cut short by the queue behind them. Others are held back on purpose — many people will not describe "
                    "a private or embarrassing problem out loud to a stranger at a reception desk. So the clinic finds out the real reason "
                    "only when the patient is already sitting in front of the doctor — sometimes booked into the wrong kind of slot entirely."
                ),
                "facts": [
                    "Phone bookings compress the visit reason to two or three words.",
                    "Sensitive problems often go unsaid until the consultation itself.",
                    "Wrong visit types waste doctor time and embarrass patients.",
                ],
            },
            {
                "h2": "Typing is easier than saying",
                "p": (
                    "When people book online and type for themselves, something changes: they write more, and they write more honestly. "
                    "There is no queue listening, no stranger on the line, no rush. Clinics using online booking have found that "
                    "self-written visit reasons are noticeably more detailed — and that patients are more candid about sensitive concerns "
                    "when they do not have to say them aloud. That detail flows to your team before the visit: the right doctor, the right "
                    "slot length, the right preparation."
                ),
                "facts": [
                    "Self-typed reasons are usually longer and clearer than phone notes.",
                    "Privacy at booking time invites honesty about sensitive issues.",
                    "Better information upfront means better-prepared consultations.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "Each BookMyClinics booking carries structured details — clinic, doctor, time — into a WhatsApp confirmation both sides can read. "
                    "Reception starts from a clear appointment, and the doctor starts from a clearer picture of who is walking in and why."
                ),
            },
        ],
        "related": ["smoother-checkin", "higher-patient-satisfaction", "patient-choice-control"],
    },
    # ---------------- PATIENT EXPERIENCE ----------------
    {
        "slug": "after-hours-booking",
        "group": "Happier patients",
        "audience": "patient",
        "img": IMG["nightphone"],
        "title": "24/7 After-Hours Booking | BookMyClinics",
        "meta": "Book a doctor at night or on the weekend — whenever you remember, not only when the clinic phone is open.",
        "h1": "Book when the clinic phone is asleep",
        "lead": "Health worries do not keep office hours. Online booking works at night and on weekends — whenever you decide to see a doctor.",
        "sections": [
            {
                "h2": "The 10 p.m. decision",
                "p": (
                    "It is 10 at night. The fever has not come down, or the back pain is worse, or you finally have a quiet moment to think "
                    "about that check-up you have been postponing. This is the moment you decide: I should see a doctor. "
                    "But the clinic phone closed hours ago. So the plan becomes \"I will call tomorrow\" — and tomorrow brings work, traffic, "
                    "and a phone queue at 9 a.m. sharp. For many people, the visit that felt urgent at 10 p.m. quietly dies by lunchtime the next day."
                ),
                "facts": [
                    "Most health decisions happen outside clinic phone hours.",
                    "\"I will call tomorrow\" is where many needed visits end.",
                    "Morning phone rush punishes exactly the people who decided at night.",
                ],
            },
            {
                "h2": "Booking at the moment you decide",
                "p": (
                    "Online booking captures the decision the moment you make it. The calendar is open at midnight, on Sunday, "
                    "during your lunch break — whenever the thought strikes. You see real open slots, pick one, and it is done before "
                    "the motivation fades. For working people and parents, this is the difference between getting care and postponing it for weeks. "
                    "And the clinic does not need a night receptionist for any of this — the calendar simply stays open when the building is closed."
                ),
                "facts": [
                    "Book at night, on weekends, on holidays — the calendar never closes.",
                    "Booking at the moment of decision beats hoping to remember tomorrow.",
                    "Working families benefit most from out-of-hours access.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "BookMyClinics works on any phone, day or night, showing live availability from clinics near you. "
                    "Pick a doctor, pick a time, confirm on WhatsApp — even if the clinic itself went dark hours ago. "
                    "Your booking will be waiting for them in the morning."
                ),
            },
        ],
        "related": ["shorter-wait-times", "patient-choice-control", "higher-patient-satisfaction"],
    },
    {
        "slug": "shorter-wait-times",
        "group": "Happier patients",
        "audience": "patient",
        "img": IMG["waiting"],
        "title": "Shorter Wait Times | BookMyClinics",
        "meta": "Skip the phone queue and the token line. Online booking shows open times right away, so you get a slot in minutes.",
        "h1": "Shorter waits to get an appointment",
        "lead": "Online booking removes the phone queue and the token line. You see open times right away and book in minutes.",
        "sections": [
            {
                "h2": "The two waits nobody counts",
                "p": (
                    "Before you ever sit in a waiting room, you wait twice. First, the wait to book: redialing a busy line, "
                    "standing in a token queue, or waiting for someone to call you back. Second, the wait for the visit itself. "
                    "The first wait is pure waste — it exists only because the booking system is a bottleneck. "
                    "In one hospital that measured it, patients queued an average of 98 minutes just to get an appointment; "
                    "after online booking, that fell to about 7 minutes. The medicine did not change. The queue did."
                ),
                "facts": [
                    "Getting a slot has its own hidden waiting time — hold music, redials, token lines.",
                    "One measured hospital cut booking waits from about 98 minutes to about 7.",
                    "The booking queue is waste; removing it costs patients nothing.",
                ],
            },
            {
                "h2": "Faster slots, not just faster booking",
                "p": (
                    "Online calendars can shorten the second wait too. When cancellations go back on the calendar instantly, "
                    "earlier slots open up for whoever is looking — so a visit planned for next week sometimes becomes tomorrow. "
                    "And because you can see every open time across days, you find the earliest slot that fits your life instead of "
                    "accepting whatever a hurried phone call happened to offer."
                ),
                "facts": [
                    "Freed cancellation slots become earlier appointments for others.",
                    "Seeing the full calendar helps you find the earliest workable time.",
                    "No more accepting the first slot read out on a rushed call.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "BookMyClinics shows live availability for the next two weeks at clinics near you. "
                    "Browse, tap, confirm on WhatsApp — usually faster than the hold music would have finished."
                ),
            },
        ],
        "related": ["after-hours-booking", "patient-choice-control", "fewer-no-shows"],
    },
    {
        "slug": "higher-patient-satisfaction",
        "group": "Happier patients",
        "audience": "patient",
        "img": IMG["smile"],
        "title": "Higher Patient Satisfaction | BookMyClinics",
        "meta": "Booking a doctor should feel as easy as ordering food. Online booking is the clinic experience patients actually enjoy.",
        "h1": "Patients are happier when booking is easy",
        "lead": "You can order dinner, book a cab, and buy a train ticket from your phone. Seeing a doctor should be just as easy.",
        "sections": [
            {
                "h2": "The first impression happens before the visit",
                "p": (
                    "A patient's opinion of a clinic starts forming long before meeting the doctor — it starts at the booking. "
                    "A busy line, a brusque \"call after 4,\" a scribbled token: all of it colors how the clinic feels. "
                    "Now compare that with opening an app at your convenience, seeing every available time laid out clearly, "
                    "and choosing the one that suits you. Same clinic, same doctor — a completely different feeling. "
                    "Clinics that added online booking have seen patient satisfaction scores rise, and the reason patients give is simple: ease."
                ),
                "facts": [
                    "The booking experience is the clinic's first impression.",
                    "Clinics adding online booking have measured higher patient satisfaction.",
                    "Ease of use is the single biggest driver patients mention.",
                ],
            },
            {
                "h2": "Control feels like respect",
                "p": (
                    "There is a deeper reason satisfaction rises: control. Choosing your own doctor, your own day, your own time — "
                    "on your own schedule, without asking permission from a phone queue — feels respectful of your life. "
                    "Book at night after the kids sleep. Book on Sunday for Tuesday. Change it if work interferes. "
                    "Patients who book this way overwhelmingly say they would do it again, which is the most honest satisfaction score there is."
                ),
                "facts": [
                    "Choosing your own slot feels respectful, not transactional.",
                    "Night and weekend booking fits real working lives.",
                    "Most patients who try online booking want to keep using it.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "BookMyClinics keeps the journey short and human: find a clinic near you, choose a doctor and time, confirm on WhatsApp. "
                    "No heavy app account, no OTP maze — just a booking that respects your time from the first tap."
                ),
            },
        ],
        "related": ["patient-choice-control", "after-hours-booking", "appointment-reminders"],
    },
    {
        "slug": "patient-choice-control",
        "group": "Happier patients",
        "audience": "patient",
        "img": IMG["family"],
        "title": "Choose Your Own Appointment Time | BookMyClinics",
        "meta": "See every open slot and pick what fits your life — not just the two options a busy receptionist reads out.",
        "h1": "Let patients choose a time that fits real life",
        "lead": "On the phone you hear two or three options. Online you see the whole week — and pick what actually works for you.",
        "sections": [
            {
                "h2": "\"We have 5 o'clock or 7 o'clock\"",
                "p": (
                    "That is how phone booking works: a busy receptionist reads out the first free gaps, you pick one under pressure, "
                    "and the call ends. Maybe Thursday morning would have suited you perfectly — but nobody mentioned Thursday, "
                    "so you took Tuesday 7 p.m. and hoped the office lets you leave early. Half the no-show problem starts right here: "
                    "appointments made to end a phone call, not to fit a life."
                ),
                "facts": [
                    "Phone booking offers a few options, not the real choice.",
                    "Times picked under pressure are times people struggle to keep.",
                    "The best slot for you may never be mentioned on the call.",
                ],
            },
            {
                "h2": "The whole calendar in your hand",
                "p": (
                    "Online booking flips the picture: you see every open slot across doctors and days, laid out like a timetable. "
                    "You can compare, think, check your work schedule, ask your spouse — and then choose. "
                    "Pick the lady doctor your mother prefers. Pick the evening slot after the school run. Pick Saturday because weekdays are impossible. "
                    "A time chosen this way fits, and appointments that fit are appointments people keep."
                ),
                "facts": [
                    "See all doctors, days, and times before deciding.",
                    "Compare and check your own schedule without anyone waiting on the line.",
                    "Self-chosen appointments are kept more often — better for you and the clinic.",
                ],
            },
            {
                "h2": "How BookMyClinics helps",
                "p": (
                    "BookMyClinics shows real availability at clinics near you for the next two weeks. "
                    "Choose the clinic, the doctor, and the exact time — then confirm on WhatsApp with nothing lost in translation."
                ),
            },
        ],
        "related": ["higher-patient-satisfaction", "shorter-wait-times", "after-hours-booking"],
    },
]

SLUG_MAP = {b["slug"]: b for b in BENEFITS}


def cta_block(b):
    """Hero CTA row matched to the page audience."""
    if b["audience"] == "patient":
        return (
            f'<a class="btn btn-primary" href="{SITE}/patient.html">Book a Doctor</a>\n'
            f'        <a class="btn btn-wa" href="{WA_PATIENT}">WhatsApp</a>'
        )
    return (
        f'<a class="btn btn-primary" href="{SITE}/clinic.html">Register Your Clinic</a>\n'
        f'        <a class="btn btn-wa" href="{WA_CLINIC}">WhatsApp</a>'
    )


def band_block(b):
    """Bottom CTA band matched to audience."""
    if b["audience"] == "patient":
        return f"""  <section class="cta-band">
    <h2>Ready to book without the queue?</h2>
    <p>BookMyClinics works on any phone — day or night, weekday or weekend.</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="{SITE}/patient.html">Book a Doctor</a>
      <a class="btn btn-wa" href="{WA_PATIENT}">WhatsApp</a>
    </div>
  </section>"""
    return f"""  <section class="cta-band">
    <h2>Ready to try this in your clinic?</h2>
    <p>We are onboarding our first 25 Founding Member clinics now — free forever, setup done by our team.</p>
    <div class="cta-row">
      <a class="btn btn-teal" href="{SITE}/clinic.html">Register Your Clinic</a>
      <a class="btn btn-wa" href="{WA_CLINIC}">WhatsApp</a>
    </div>
  </section>"""


def related_block(b):
    links = []
    for slug in b["related"]:
        rb = SLUG_MAP[slug]
        links.append(
            f'      <a class="related-item" href="{slug}.html">{rb["h1"]}</a>'
        )
    return f"""  <section class="section related-section">
    <h2>Related benefits</h2>
    <div class="related-list">
{chr(10).join(links)}
    </div>
  </section>"""


def render_page(b):
    sections_html = []
    for sec in b["sections"]:
        facts = ""
        if sec.get("facts"):
            items = "".join(f"<li>{f}</li>" for f in sec["facts"])
            facts = f'\n      <ul class="evidence-list">{items}</ul>'
        sections_html.append(
            f"""
  <section class="section prose-section">
    <h2>{sec['h2']}</h2>
    <div class="prose">
      <p>{sec['p']}</p>{facts}
    </div>
  </section>"""
        )
    url = f"{SITE}/landings/benefits/{b['slug']}.html"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="canonical" href="{url}">
  <title>{b['title']}</title>
  <meta name="description" content="{b['meta']}">
  <meta name="theme-color" content="#0f172a">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="BookMyClinics">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{b['h1']} | BookMyClinics">
  <meta property="og:description" content="{b['meta']}">
  <meta property="og:image" content="{b['img']}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{b['h1']} | BookMyClinics">
  <meta name="twitter:description" content="{b['meta']}">
  <meta name="twitter:image" content="{b['img']}">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{b['h1']}",
    "description": "{b['meta']}",
    "url": "{url}",
    "image": "{b['img']}",
    "publisher": {{
      "@type": "Organization",
      "name": "BookMyClinics",
      "url": "{SITE}/"
    }}
  }}
  </script>
  <link rel="icon" type="image/png" href="https://upadhyaymehul9-prog.github.io/bookmyclinic/icon-192.png">
  <link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800;900&family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../lp.css">
</head>
<body>
  <nav>
    <a class="nav-brand" href="{SITE}/">Book<span>My</span>Clinics</a>
    <div class="nav-links">
      <a class="nav-link" href="./">Benefits</a>
      <a class="nav-link" href="{SITE}/clinic.html">Register</a>
    </div>
  </nav>

  <header class="hero">
    <div class="hero-media" style="background-image:url('{b['img']}');"></div>
    <div class="hero-shade"></div>
    <div class="hero-content">
      <div class="brand-mark">Book<span>My</span>Clinics</div>
      <h1>{b['h1']}</h1>
      <p>{b['lead']}</p>
      <div class="cta-row">
        {cta_block(b)}
      </div>
    </div>
  </header>
{''.join(sections_html)}
{related_block(b)}
{band_block(b)}

  <footer>
    <div class="footer-links">
      <a href="./">Benefits</a> ·
      <a href="{SITE}/landings/lp-register.html">For Clinics</a> ·
      <a href="{SITE}/patient.html">Book a Doctor</a> ·
      <a href="{SITE}/privacy.html">Privacy</a> ·
      <a href="{SITE}/terms.html">Terms</a>
    </div>
    © 2026 BookMyClinics · Gujarat, India
  </footer>
</body>
</html>
"""


def render_hub():
    groups = {}
    for b in BENEFITS:
        groups.setdefault(b["group"], []).append(b)
    n = len(BENEFITS)
    body = []
    idx = 1
    for gname, items in groups.items():
        body.append(f'    <h2 class="hub-group">{gname}</h2>')
        body.append('    <div class="hub-list">')
        for b in items:
            body.append(
                f"""      <a class="hub-item" href="{b['slug']}.html">
        <strong>{idx:02d} · {b['h1']}</strong>
        <span>{b['meta']}</span>
      </a>"""
            )
            idx += 1
        body.append("    </div>")
    hub_url = f"{SITE}/landings/benefits/"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="canonical" href="{hub_url}">
  <title>{n} Benefits of Online Appointment Booking | BookMyClinics</title>
  <meta name="description" content="Simple explanations of {n} real benefits of online doctor appointment booking — for clinic owners and patients.">
  <meta name="theme-color" content="#0f172a">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="BookMyClinics">
  <meta property="og:url" content="{hub_url}">
  <meta property="og:title" content="{n} Benefits of Online Appointment Booking | BookMyClinics">
  <meta property="og:description" content="Simple explanations of {n} real benefits of online doctor appointment booking — for clinic owners and patients.">
  <meta property="og:image" content="{IMG['reception']}">
  <meta name="twitter:card" content="summary_large_image">
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
      max-width: 24ch;
      margin-bottom: 12px;
    }}
    .hub-lead {{
      color: rgba(255,255,255,0.55);
      margin-bottom: 8px;
      line-height: 1.65;
      max-width: 46ch;
    }}
    .hub-group {{
      font-family: var(--font-display);
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--sky);
      margin: 34px 0 14px;
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
    <a class="nav-brand" href="{SITE}/">Book<span>My</span>Clinics</a>
    <div class="nav-links">
      <a class="nav-link" href="{SITE}/clinic.html">Register</a>
      <a class="nav-link" href="{SITE}/patient.html">Book</a>
    </div>
  </nav>
  <main class="hub">
    <div class="hub-brand">Book<span>My</span>Clinics</div>
    <h1>{n} benefits of online appointment booking</h1>
    <p class="hub-lead">Each page explains one benefit in simple English — why online booking helps clinics and patients.</p>
{chr(10).join(body)}
  </main>
  <footer>
    <div class="footer-links">
      <a href="{SITE}/">Home</a> ·
      <a href="{SITE}/clinic.html">Register</a> ·
      <a href="{SITE}/patient.html">Book a Doctor</a> ·
      <a href="{SITE}/privacy.html">Privacy</a>
    </div>
    © 2026 BookMyClinics · Gujarat, India
  </footer>
</body>
</html>
"""


CSS_BLOCK = """
/* benefit landing prose */
.nav-links { display: flex; gap: 18px; align-items: center; }
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
.related-section h2 { margin-bottom: 16px; }
.related-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.related-item {
  display: inline-block;
  padding: 12px 18px;
  border-radius: 999px;
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.14);
  color: rgba(255,255,255,0.75);
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  transition: border-color 0.2s, background 0.2s, transform 0.2s;
}
.related-item:hover {
  border-color: rgba(56,189,248,0.45);
  background: rgba(56,189,248,0.1);
  transform: translateY(-1px);
}
"""


def patch_css():
    css_path = ROOT / "landings" / "lp.css"
    css = css_path.read_text()
    marker = "/* benefit landing prose */"
    if marker in css:
        css = css[: css.index(marker)].rstrip() + "\n"
    css_path.write_text(css + CSS_BLOCK)


def patch_sitemap():
    sm = ROOT / "sitemap.xml"
    text = sm.read_text()
    text = re.sub(
        r"\n<url>\n  <loc>https://bookmyclinics.com/landings/benefits/[^<]*</loc>[\s\S]*?</url>",
        "",
        text,
    )
    entries = [
        f"""
<url>
  <loc>{SITE}/landings/benefits/</loc>
  <lastmod>{TODAY}T00:00:00+00:00</lastmod>
  <priority>0.75</priority>
</url>"""
    ]
    for b in BENEFITS:
        entries.append(
            f"""
<url>
  <loc>{SITE}/landings/benefits/{b['slug']}.html</loc>
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
    html = re.sub(
        r"(?:Evidence|Benefits) library · \d+(?: benefit)? pages",
        f"Benefits library · {n} pages",
        html,
    )
    html = re.sub(
        r"a \d+-page (?:evidence |benefits )?library[^.<]*\.",
        f"a {n}-page benefits library in simple English.",
        html,
    )
    path.write_text(html)


def main():
    for b in BENEFITS:
        (OUT / f"{b['slug']}.html").write_text(render_page(b))
        print("wrote", b["slug"])
    (OUT / "index.html").write_text(render_hub())
    print("wrote index")
    patch_css()
    patch_sitemap()
    patch_landings_index()
    print("done", len(BENEFITS), "benefit pages")


if __name__ == "__main__":
    main()
