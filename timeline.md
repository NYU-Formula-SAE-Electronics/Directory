# 2026-2027 Season Timeline

Visual timeline for the season. Rendered with [Mermaid](https://mermaid.js.org/syntax/gantt.html) — displays automatically on GitHub and in Cursor's markdown preview.

> Dates are planning estimates. `after` links encode real dependencies, so shifting one task cascades to the ones that depend on it. See [season-plan.md](season-plan.md) for full detail on each item.

```mermaid
gantt
    title 2026-2027 Season
    dateFormat YYYY-MM-DD
    axisFormat %b %d

    section Sourcing & Sponsors
    Connector companies (sponsor/sample)   :active, conn, 2026-05-01, 45d
    Contact New Haven Display              :2026-05-01, 21d
    Confirm dash / roll hoop space         :2026-05-01, 21d
    PCBWay sponsorship                     :2026-06-01, 30d

    section LV - STM Core
    STM Core board design                  :stm, after conn, 25d
    STM Core + Dev board to prod           :milestone, stmprod, 2026-06-28, 0d
    PCBs & prints arrive                   :milestone, arrive1, 2026-07-10, 0d
    Firmware bring-up & validation         :fw, 2026-07-10, 8d
    Core design validated                  :milestone, coreval, after fw, 0d

    section LV - PCU
    Filter circuit decision                :pcufilt, 2026-06-01, 20d
    PCU Gen 2 design                       :pcu, after conn, 30d
    PCU to prod                            :pcuprod, after coreval, 5d

    section LV - CTU
    SMD component sourcing                 :ctusrc, 2026-06-01, 20d
    CTU board design                       :ctu, 2026-06-01, 30d
    CTU breadboard testing                 :2026-06-15, 25d
    CTU to prod                            :after coreval, 5d

    section LV - Dash & Steering
    Dash & Steering board design           :dash, 2026-06-10, 30d
    Dash & Steering CAD                    :dashcad, after stmprod, 45d
    Dash & Steering to prod                :after coreval, 10d
    Second batch PCBs arrive               :milestone, arrive2, 2026-08-15, 0d

    section Wiring
    Master schematic (start)               :wire, 2026-07-25, 20d
    Finish schematic sheet                 :wiresch, 2026-08-10, 15d
    Harness CAD (David & Ray)              :wirecad, after wiresch, 15d
    Export lengths + gauge table           :after wirecad, 7d

    section Harnesses (Sept)
    PCU to pedal sensors                   :2026-09-01, 10d
    PCU to brake sensor / cutoff valve     :2026-09-01, 7d
    PCU to wheel speed sensors             :2026-09-05, 10d
    PCU to dashboard (CAN2)                :2026-09-08, 10d
    Dashboard to steering wheel            :2026-09-10, 7d
    CTU harness - 12V / GND / CAN2         :2026-09-10, 7d
    Cascadia logic harness                 :2026-09-12, 12d
    Bench test firmware + harnesses        :2026-09-15, 20d

    section HV - Accumulator
    Fix fuse rig                           :fuserig, 2026-05-15, 15d
    Fuse material test + endurance         :fuse, after fuserig, 40d
    Spotweld fuses + segments              :after fuse, 15d
    Busbars (bend / assemble)              :2026-06-15, 30d
    Thermal bonding thermistors            :2026-07-01, 15d
    Module assembly complete               :milestone, 2026-07-25, 0d
    BMS temp read testing                  :2026-07-25, 15d

    section HV - Mid-Box
    Fix TSSI isolation error               :2026-06-01, 20d
    Fix precharge logic error              :2026-06-01, 20d
    TSSI lights (working)                  :2026-06-20, 20d
    Mid-box wiring + schematic doc         :2026-07-10, 25d

    section HV - Enclosure
    Nomex insulation epoxy                 :2026-06-01, 14d
    Top cover insulation                   :2026-06-15, 14d
    Top cover components - HVD / TSMP       :2026-07-01, 21d
    Enclosure CADs                         :2026-08-01, 30d
```

## Legend

- **Milestones** (diamonds): hard checkpoints like parts arriving or a design being validated.
- **`after` dependencies**: e.g. PCU/CTU/Dash go to prod only *after* the STM Core design is validated.
- **Critical path**: Connectors → STM Core → Core validation → all other boards to prod → wiring → harnesses.

## Editing tips

- Add a task: `Task name :id, START_DATE, DURATION` (e.g. `20d`) or `:id, after otherId, 20d`.
- Mark in-progress with `:active,` and done with `:done,` before the id.
- Group related work by adding a new `section`.
