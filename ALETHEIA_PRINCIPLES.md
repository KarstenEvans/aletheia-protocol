---
document_id: aletheia-ecosystem-principles
version: 0.1
status: living-draft
document_class: ecosystem-guidance
date: 2026-10-14
authority: subordinate-to-aletheia-protocol
---

# Aletheia Principles: Ecosystem and Learning

> **Knowledge belongs to the project, not the assistant.**
>
> **Not just for the bright and rich, but also for the bored and poor.**
>
> **Curiosity is free. Knowledge should be within everyone's reach.**

This document records practical design commitments for Aletheia applications, knowledge libraries and learning experiences. It **does not replace or amend** [the frozen Aletheia Principles v1.0](ALETHEIA_PRINCIPLES_v1.0.md), the Protocol Specification or accepted decision records. Where there is a conflict, the normative hierarchy defined in the Protocol README applies. Some commitments below are previously agreed design directions, and others are implementation tests or proposals awaiting review.

## 1. Core stewardship (inherited from the frozen Principles)

The fifteen principles in [ALETHEIA_PRINCIPLES_v1.0.md](ALETHEIA_PRINCIPLES_v1.0.md) remain authoritative. In brief:

1. Knowledge belongs to the project, not the assistant.
2. Important conclusions trace to Truth Anchors.
3. Evidence is not interpretation.
4. Verified copies are not verified truth.
5. Preserve disagreements and competing explanations.
6. Improve the specification before repeatedly patching an output.
7. Remember contextually, not exhaustively.
8. Preserve meaning across AI dialects.
9. Archive rather than erase, except where privacy or law requires deletion.
10. Propose changes transparently; do not silently overwrite accepted knowledge.
11. Keep integrity, source identity, evidential support and applicability separate.
12. Humans retain accountable authority.
13. Minimise data exposure.
14. Invite independent challenge.
15. Leave knowledge healthier than you found it.

Refer to the frozen file for exact wording, not this summary.

## 2. Learning and inclusion: for everyone

16. **Learning is for everyone.** Design for people of all incomes, educational backgrounds, ages, abilities and confidence levels. Aletheia Smart Learn must serve curiosity, boredom and immediate practical need as well as formal study.
17. **Free-first access.** Essential lessons should not require a paid subscription, purchase, affiliate click or specific commercial AI account. Clearly label optional paid dependencies.
18. **Start with what the learner has.** Teach cooking with existing ingredients, gardening with basic household materials, repair awareness with available tools and digital skills on older equipment where feasible.
19. **Questions are valid entrances to learning.** Start with “How do I…?”, “Why…?” or “I'm bored”, not only course titles, curricula or jargon.
20. **Plain language without condescension.** Explain one concept at a time; offer adjustable depth, pacing, languages, audio and visual alternatives.
21. **Short, enjoyable and optional.** Offer bite-size sessions and “Surprise Me”, alongside long courses; avoid compulsory streaks, quizzes or needless registration.
22. **Portable and available without an AI.** Courses and progress should be usable as readable Markdown or web pages, even when an AI provider is unavailable, paid or rate-limited.
23. **Practical skills have equal dignity.** Cooking, DIY, gardening, household maintenance, money-saving, crafts and repairs matter alongside programming, science and professional education.
24. **Accessibility is a release test.** Ask: Can someone with an old phone, little money, no qualifications and twenty minutes actually use this? Support low-bandwidth, keyboard access, readable text and simple navigation.
25. **Safety before shortcuts.** Practical lessons distinguish safe beginner tasks from electrical, gas, structural, medical or other high-risk work requiring qualified help. Never use apparent simplicity to conceal risk.

## 3. AI independence and application architecture

26. **AI independent by design.** Aletheia must not depend on ChatGPT, Gemini, Claude, Copilot or any one model. Provider routing is an implementation detail, not a provider-specific fork of the application.
27. **Markdown as a durable exchange format.** Keep knowledge, course structure, task instructions, decisions and progress portable in clear, editable Markdown with provenance metadata.
28. **One shared capability before many clones.** Reuse Aletheia Improve, Site Audit, AI routing and research capabilities; avoid near-duplicate apps unless a genuinely distinct purpose is established.
29. **Simple user interface, capable internals.** Offer clear menus, Help, Restart/Resume and sensible defaults. Hide complexity until needed, especially for first-time users.
30. **Location-first when location matters.** In Aletheia Discover, make nearby, time-relevant options easy to find; permit manual location control and respect privacy.
31. **Multilingual and adaptable.** Preserve meaning through translation and support local requirements without fragmenting the underlying protocol.
32. **Own the workflow, not other people's content.** Link and cite authoritative sources; respect licences, copyrights, robots restrictions and platform terms. Do not clone a third-party site to manufacture a knowledge base.
33. **Do not make the interface the archive.** Store source facts, references, dates, decisions and reusable lesson material independently of any particular website or chat.

## 4. Evidence, freshness and honest research

34. **Separate observation, forecast and inference.** Label what is directly measured, what is projected, and what the AI infers, including uncertainty.
35. **Date information that can go stale.** Keep captured-on, published-on and checked-on dates where appropriate; distinguish current advice from historic reports.
36. **Prefer verified useful actions to viral assertions.** Demand signals, search trends, community discussions and videos suggest topics; they are not proof that instructions are correct.
37. **Research questions, not just keywords.** Aletheia Learn should compare search interest with real learner problems and use dated evidence before ranking course-demand claims.
38. **Let users keep their own records.** Support user-controlled Markdown storage and exports; don't silently centralise personal shopping lists, learning progress or research.
39. **Make correction easy.** Provide attribution, source links, revision history, clear uncertainty and a way to challenge errors.

## 5. Publishing, trust and sustainable growth

40. **Useful before monetised.** Affiliate links and commercial partnerships must not block core learning or distort rankings or recommendations.
41. **Show provenance and commercial relationships.** Distinguish independent advice, advertising, sponsorship, referrals and unverified opinion.
42. **Readable by humans and machines.** Build clear navigation and semantic content; use SEO, AEO and GEO as discoverability improvements, not as substitutes for quality.
43. **Release only what is honestly represented.** Separate prototypes, plans, verified services and deployed functionality. Do not claim a feature exists before it is tested.
44. **Iterate with evidence and human review.** Use preflight checks, accessibility review, tests, Aletheia Improve and documented handovers rather than opaque changes.

## 6. Smart Learn design checks

Before publishing a learning course, check:

- Can a complete beginner start without payment or specialist equipment?
- Is there an engaging five-minute entry point as well as deeper study?
- Can the course run on an AI chosen by the learner, and still be read without AI?
- Are source links, dates, safety limits and uncertainty present?
- Does the course teach a transferable skill rather than just output an answer?
- Can the learner save or export progress without being trapped in a provider?
- Are practical skills and curiosity treated as serious educational interests?
- Have popularity claims been measured rather than guessed?

## 7. Document governance

- **Status:** Living draft of ecosystem guidance, not a normative Protocol amendment.
- **Review:** Apply changes by visible, attributable commits and review proposed conflicts against the frozen v1.0 principles.
- **Origin:** Consolidated from previously discussed Aletheia Protocol, Knowledge, Discover, Improve, Smart Learn, shopping, site-audit and provenance design decisions (through 14 October 2026).
- **Working motto from the original Principles:** “Remember well. Reason clearly. Prosper together.”
