# Project Charter

## General Information

| Project Name | Project Overseer |
| ------------ | ---------------- |
| Green-IT     | Ecole IT         |

| Team Members    |
| --------------- |
| Jason Grosso    |
| Alexis Lasselin |

| Start Date | End Date   |
| ---------- | ---------- |
| 13/01/2026 | 16/01/2026 |

## Project Overview

| Section               | Details                                                                                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Project Purpose       | Green-IT is a monitoring dashboard for tracking and reducing the environmental impact of IT infrastructures.                                                 |
| Problem Statement     | 1. Lack of awareness about the environmental impact of IT operations. <br> 2. Need for tools to monitor and reduce energy consumption in IT infrastructures. |
| Goals / Metrics       | 1. Develop a functional monitoring dashboard by the end of the project. <br> 2. Achieve at least 80% user satisfaction in post-deployment surveys.           |
| Expected deliverables | 1. Monitoring Dashboard <br> 2. Documentation (Project Charter, Backlog, Risk Register) <br> 3. Oral Presentation                                            |

## Project Scope

| In Scope                                                | Out of Scope                           |
| ------------------------------------------------------- | -------------------------------------- |
| Development of a monitoring dashboard                   | Hardware procurement                   |
| Data collection and analysis                            | Long-term maintenance of the dashboard |
| User training and documentation                         | Integration with non-IT systems        |
| Environmental impact reporting features                 |                                        |
| Implementation of energy-saving recommendations         |                                        |
| Regular updates and improvements based on user feedback |                                        |

## Project Milestones

| Key Milestone           | Description                                      | Due Date   |
| ----------------------- | ------------------------------------------------ | ---------- |
| Project Kickoff         | Initial project meeting and planning             | 13/01/2026 |
| Requirements Gathering  | Collecting and documenting project requirements  | 14/01/2026 |
| Prototype Development   | Creating a prototype of the monitoring dashboard | 15/01/2026 |
| Testing Phase           | Testing the dashboard for functionality and bugs | 15/01/2026 |
| Final Deployment        | Launching the dashboard for end-users            | 16/01/2026 |
| Oral Presentation       | Presenting the project outcomes                  | 16/01/2026 |
| Final Report Submission | Submitting the comprehensive project report      | 16/01/2026 |

## ROI and Business Case Analysis

### Problematic

How can organizations effectively measure, monitor, and reduce the environmental impact of their IT infrastructures while maintaining operational efficiency and controlling costs?

### Assumptions

The following ROI analysis is based on realistic but estimated data, intended to demonstrate the potential value of the Green-IT dashboard rather than provide exact financial projections.

- Average IT infrastructure size: **10 cloud-based servers**
- Average annual energy consumption: **50,000 kWh**
- Average electricity cost: **€0.10 per kWh**
- Annual energy cost: **€5,000**
- Average carbon emission factor: **50 gCO₂ per kWh**
- Annual carbon footprint: **2.5 tons of CO₂**
- Average IT staff cost: **€20/hour**

### Business Cases

#### 1. Energy Consumption Reduction

The Green-IT monitoring dashboard enables organizations to identify inefficient resource usage, such as over-provisioned virtual machines, underutilized services, or idle workloads. By providing real-time visibility and optimization recommendations, organizations can implement targeted corrective actions.

A conservative energy reduction of **10–15%** is considered achievable.

- Estimated energy savings: **7,500 kWh per year**
- Estimated cost savings: **€750 per year**

#### 2. Carbon Emission Reduction

By optimizing energy consumption, the Green-IT dashboard directly contributes to reducing greenhouse gas emissions associated with IT operations.

- Estimated CO₂ reduction: **375 kg CO₂ per year**
- Environmental impact equivalent to:

  - Approximately **2,500 km of car travel avoided**, or
  - The annual carbon absorption of **30 mature trees**

This reduction supports corporate sustainability objectives and environmental responsibility commitments.

#### 3. Operational Efficiency Gains

Without centralized monitoring, IT teams often rely on manual data collection and analysis to assess infrastructure performance and energy usage. The Green-IT dashboard automates these processes and consolidates data into a single interface.

- Estimated time saved: **2 hours per week**
- Annual time savings: **~100 hours**
- Estimated productivity gain: **€2,000 per year**

#### 4. Regulatory Compliance and Sustainability Reporting

Increasing environmental regulations and corporate social responsibility (CSR) requirements demand accurate reporting of energy consumption and carbon emissions. The Green-IT dashboard provides structured and exportable sustainability reports, reducing compliance risks and preparation effort.

Although difficult to quantify financially, this benefit contributes to:

- Reduced regulatory risk
- Improved audit readiness
- Enhanced corporate sustainability image

### ROI Summary

| Category                           | Estimated Annual Value |
| ---------------------------------- | ---------------------- |
| Energy cost savings                | €750                   |
| Operational efficiency gains       | €2,000                 |
| **Total estimated annual benefit** | **€2,750**             |

### Non-Financial ROI

In addition to measurable financial benefits, the Green-IT dashboard provides several qualitative advantages:

- Improved environmental awareness across IT teams
- Better-informed infrastructure decision-making
- Enhanced corporate sustainability reputation
- Educational value for IT and sustainability best practices
- Promotion of a culture of continuous improvement in environmental performance

## Estimated Budget

| Expense Category              | Estimated Cost (€) |
| ----------------------------- | ------------------ |
| Software Development          | 1,500              |
| Testing and Quality Assurance | 500                |
| Documentation and Training    | 300                |
| Miscellaneous Expenses        | 200                |
| **Total Estimated Budget**    | **2,500**          |

## Stakeholder Analysis

| Stakeholder | Role                                                                        | Interest Level | Influence Level | Engagement Strategy                            |
| ----------- | --------------------------------------------------------------------------- | -------------- | --------------- | ---------------------------------------------- |
| Client      | Project Sponsor                                                             | High           | High            | Regular updates, involvement in key decisions  |
| Alexis      | Service Request Manager <br> Project Manager <br> Software Engineer <br> QA | High           | High            | Active participation in planning and execution |
| Jason       | Service Delivery Manager <br> Tech Lead <br> Software Engineer <br> QA      | High           | High            | Active participation in planning and execution |

## RACI Matrix

The RACI Matrix is a management document used to define team roles across 4 categories: Responsible, Accountable, Consulted, Informed.

| Name               | Project Manager | Program Manager | Tech Lead | Software Engineer | Quality Assurance | Technical Writer | Client |
| :----------------- | :-------------: | :-------------: | :-------: | :---------------: | :---------------: | :--------------: | :----: |
| Project Brief      |        I        |        I        |     I     |         I         |         I         |        I         | R / A  |
| Project Charter    |      R / A      |      C / I      |   C / I   |       C / I       |       C / I       |      C / I       |   C    |
| Planning           |      R / A      |      C / I      |   C / I   |       C / I       |       C / I       |      C / I       |   C    |
| Code               |        -        |        -        |     C     |       R / A       |         I         |        -         |   -    |
| Code Documentation |        -        |        -        |     C     |       R / A       |       C / I       |        -         |   -    |

**Responsible**: Those who are responsible for the correct completion of the task; <br>
**Accountable**: The one that must sign off (approve) work that the Responsible provides; <br>
**Consulted**: Those whose opinions are sought, typically subject-matter experts, and with whom there is a two-way communication; <br>
**Informed**: Those who are kept up-to-date on progress, often only on completion of the task or deliverable, and with whom there is just a one-way communication; <br>

## MoSCoW Prioritization

The MoSCoW method is a prioritization technique used to reach a common understanding with stakeholders on the importance they place on the delivery of each requirement. The letters in MoSCoW stand for:

- **M**ust have
- **S**hould have
- **C**ould have
- **W**on't have this time

| Must Have                          | Should Have                        | Could Have                  | Won't Have This Time               |
| ---------------------------------- | ---------------------------------- | --------------------------- | ---------------------------------- |
| Monitoring dashboard core features | User training sessions             | Advanced analytics features | Integration with non-IT systems    |
| Real-time data collection          | Environmental impact reporting     | Mobile app version          | Long-term maintenance services     |
| Basic documentation                | Customizable dashboard views       | Social sharing features     | Hardware procurement               |
| Testing and quality assurance      | Automated alerts and notifications | Gamification elements       | Extensive third-party integrations |

