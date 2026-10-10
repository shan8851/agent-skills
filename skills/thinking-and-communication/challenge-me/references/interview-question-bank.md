# Interview Question Examples

These are example question shapes for pressure-testing proposals. They are **not** a fixed questionnaire and should not be asked mechanically.

Use them to inspire bespoke questions when you are stuck or choosing between branches. The live conversation is the source of truth: each answer should change the next follow-up where appropriate.

Rules:
- Ask one question at a time.
- Prefer a bespoke question over copying one from this file.
- Include your recommended/default answer with the question.
- Skip any question whose answer can be discovered by inspecting context, files, docs, or web sources.
- Do not force every category; follow the load-bearing uncertainty.

## Universal

- What exact problem are we solving?
- Who is the actor, and what job are they trying to get done?
- What evidence says this matters now?
- What does success look like in 2 weeks and 6 weeks?
- What assumption must be true for this to work?
- What is the smallest version that still proves the idea?
- What are we explicitly not doing?
- What is the opportunity cost of doing this now?
- What would make us kill or park this?

## Product / project

- Is this problem painful enough for repeated use?
- What existing alternative solves 80% of this?
- What is the wedge that makes this better, faster, safer, cheaper, or more delightful?
- What is the first moment where a user says “oh, I get it”?
- What single risk could kill the project early?
- What would be impressive in a demo but useless in real life?
- What would be boring in a demo but essential in real life?
- What can be mocked without weakening the thesis?

## Engineering design

- What are the core domain nouns, and are they precise?
- What is the public interface of the most important module?
- Where can we create a deep module: simple interface, meaningful hidden complexity?
- What decision is hardest to reverse?
- What state transition or edge case is most likely to break?
- What should be tested through public behaviour rather than implementation detail?
- What failure mode needs a first-class recovery path?

## Workflow / automation

- Which step is currently the bottleneck?
- What should remain manual by design?
- What metric improves if this workflow works?
- Where does automation create hidden maintenance overhead?
- What is the rollback path if it fails?
- Where does the human need visibility, approval, or override?

## Demo / hackathon / stakeholder pitch

- What is the 30-second pitch?
- What is the 3-minute demo path?
- What is the wow moment?
- What is real vs mocked vs dry-run?
- What fails if the network/API/provider dies during the demo?
- What would judges/stakeholders misunderstand?

## Writing/content

- What is the one claim worth arguing?
- What specific audience pain does this address?
- What proof/examples make this non-generic?
- What would a strong critic say is wrong?
- What action should a reader take after reading?
