# SOA-C03 Compact Skill Model

Short language. Full exam context. One skill at a time.

## Domain 1 - Monitoring, Logging, Analysis, Remediation, and Performance Optimization

### Task 1.1 - Implement metrics, alarms, and filters

## Skill 1.1.1 - Configure monitoring and logging for workloads

**Official goal:** Use AWS monitoring and logging services for serverless, compute, container, and AI workloads.

### What exam tests

- Primary: `CFG EVD BEH`
  - Configure telemetry.
  - Find the right evidence.
  - Know what each service does.
- Supporting: `SEL GOV`
  - Pick the right service.
  - Give it correct access.
- Precision: `L2 - Object`
  - Know exact object names and links.
  - No need for full CLI/API syntax.

### Core model

```text
Workload
  -> emits metric, log, trace, event, or API call
  -> AWS service collects it
  -> operator queries, graphs, alarms, or audits it
```

### Pick the service

| Need | Use |
|---|---|
| Resource/application metrics | CloudWatch Metrics |
| Application/system logs | CloudWatch Logs |
| Who changed AWS resource | CloudTrail |
| Request path across services | X-Ray / CloudWatch tracing views |
| ECS/EKS resource visibility | Container Insights |
| Prometheus metrics and PromQL | Amazon Managed Service for Prometheus |
| Dashboards for many data sources | Amazon Managed Grafana |
| Stream telemetry to destination | Data Firehose |
| SQL over logs in S3 | Athena |

Fast clue:

```text
CPU high? CloudWatch.
Who deleted resource? CloudTrail.
PromQL needed? Managed Prometheus.
Request slow across services? Trace.
Historical S3 logs need SQL? Athena.
```

### Exact objects to know

**CloudWatch Metrics**

- Namespace: metric family.
- Metric: measured value.
- Dimension: metric identity/filter.
- Period: time bucket.
- Statistic: average, sum, minimum, maximum, percentile.

**CloudWatch Logs**

- Log group: shared settings and retention.
- Log stream: events from one source.
- Log event: timestamp plus message.
- Metric filter: log pattern -> metric.
- Subscription filter: log events -> destination.
- Logs Insights: query logs.

**CloudTrail**

- Event history: recent management activity.
- Trail: ongoing delivery.
- Management event: control-plane operation.
- Data event: resource-level activity, often high volume.
- Multi-Region trail: records supported activity across Regions.
- Organization trail: central trail for organization accounts.

**Managed Prometheus**

- Workspace: stores Prometheus metrics.
- Ingestion: metrics enter workspace.
- PromQL: query language.
- Grafana: optional visualization layer.

### Workload clues

- EC2 native metrics: CPU, network, status checks.
- EC2 guest memory/disk: agent needed. Not native.
- Lambda: invocations, errors, throttles, duration, concurrency.
- ECS/EKS: cluster, service, task/pod, node, container metrics.
- Bedrock/AI workload: use available service metrics and logs. Same monitoring model.

CloudWatch agent configuration belongs mainly to **Skill 1.1.2**.

### Configuration path

```text
Choose telemetry
  -> enable source/service integration
  -> grant write/read permissions
  -> choose Region and destination
  -> set log retention
  -> verify data arrives
  -> query or graph it
```

For CloudTrail:

```text
Create trail
  -> choose Regions/accounts
  -> choose management/data events
  -> deliver to S3
  -> optional CloudWatch Logs delivery
  -> protect and retain logs
```

### Evidence to inspect

- Metric graph has datapoints and correct dimensions.
- Log group has recent log streams/events.
- CloudTrail event shows time, principal, event source/name, source IP, request, and error.
- PromQL returns expected series and labels.
- Container Insights shows expected cluster/node/pod/task scope.

### Failure clues

| Symptom | First checks |
|---|---|
| No metric | Region, namespace, dimensions, source enabled |
| No log | Log group/stream, source config, IAM, network path |
| No CloudTrail event | Event type, trail scope, Region, data events enabled |
| Prometheus query empty | Ingestion, labels, time range, PromQL selector |
| Container data missing | Insights enabled, collector/add-on, permissions |

### Exam traps

- CloudTrail is not application logging.
- CloudWatch Logs does not replace API audit history.
- EC2 memory and filesystem space are not default EC2 metrics.
- Metric dimension mismatch looks like missing data.
- Data events are not the same as management events.
- Managed Prometheus stores/queries metrics; Grafana visualizes them.
- Central viewing is not the same as moving all telemetry into one account.

### Do not memorize

- Every CloudWatch metric.
- Full query syntax.
- Full agent configuration JSON.
- Every CloudTrail data-event type.
- Console click paths.

### Ready when

Given a scenario, you can answer:

1. Which telemetry type is missing?
2. Which service should collect it?
3. Which exact object/settings matter?
4. Where do you verify data arrival?
5. Why is a plausible alternative wrong?

---

## Skill 1.1.2 - Configure and manage the CloudWatch agent

**Official goal:** Collect metrics and logs from EC2, ECS, and EKS.

### What exam tests

- Primary: `CFG EVD DIA`
  - Install and configure agent.
  - Prove data arrives.
  - Find why data is missing.
- Supporting: `REM GOV PRC`
  - Repair agent/configuration.
  - Give correct permissions.
- Precision: `L2 - Object`
  - Know agent parts and links.
  - No need for full JSON.

### Core model

```text
Host/container data
  -> CloudWatch agent
  -> CloudWatch Metrics / Logs
  -> dashboard, query, alarm
```

No agent or custom collection:

```text
EC2 has CPU/network/status metrics.
EC2 has no guest memory/filesystem metric.
```

### Where agent runs

| Target | Operational form |
|---|---|
| EC2 | Agent installed on instance |
| ECS | Agent/collector in container environment |
| EKS | Observability add-on or collector deployment |
| On premises | Agent on supported server |
| Lambda | No agent installation needed |

### Exact objects to know

- Agent package/process: collector itself.
- Agent configuration: metrics and log sources.
- IAM instance/task/pod role: permission to send data.
- Parameter Store parameter: central agent configuration.
- CloudWatch namespace: destination for metrics.
- Log group: destination for logs.
- Log stream: source-specific log flow.
- Agent log: agent's own errors and state.
- Container Insights: container telemetry view.

### What agent can collect

**Metrics**

- Guest CPU details.
- Memory.
- Disk/filesystem.
- Swap.
- Network.
- Process metrics.
- GPU metrics where supported.
- Custom application metrics.

**Logs**

- File paths.
- Timestamp format.
- Multiline records.
- Log group and stream.
- Retention setting.

**Traces**

- Agent can participate in supported trace collection.
- Trace design is not the main focus here.

### Configuration path

```text
Install/deploy agent
  -> attach IAM role
  -> create configuration
  -> choose metric/log sources
  -> choose Region and destinations
  -> start/fetch configuration
  -> verify agent state
  -> verify CloudWatch data
```

Fleet pattern:

```text
Store config in Parameter Store
  -> deploy/fetch through Systems Manager
  -> same config on many nodes
```

### Evidence to inspect

1. Agent process/container is running.
2. Agent configuration loaded successfully.
3. Agent log has no permission/config/network error.
4. Expected metric namespace and dimensions exist.
5. Expected log group/stream has recent events.
6. Container Insights shows correct cluster/node/pod/task scope.

### Failure clues

| Symptom | First checks |
|---|---|
| Agent not running | Installation, service/container state, configuration load |
| Metrics missing | Metric section, namespace, dimensions, IAM, Region |
| Logs missing | File path, read access, timestamp parsing, group/stream |
| All data missing | IAM role, network/DNS/endpoints, Region, agent state |
| Wrong node shown | Dimensions, hostname/instance identity, reused config |
| Container data missing | Add-on/collector, service account/task role, deployment state |
| Duplicate/high-cost data | Duplicate collectors, excessive dimensions, collection interval |

### Repair pattern

```text
Check agent
  -> read agent log
  -> validate configuration
  -> check IAM
  -> check network and Region
  -> restart/reload
  -> verify new datapoint/log event
```

### Exam traps

- EC2 native metrics do not include guest memory or free disk.
- Running agent does not prove data delivery.
- Correct IAM with wrong Region still looks like missing data.
- Correct log group with wrong file path stays empty.
- CloudWatch agent and ECS container agent are not the same job.
- More dimensions can increase custom-metric cost.
- Agent collects data; alarm configuration is mainly Skill 1.1.3.

### Do not memorize

- Full configuration JSON.
- Every agent metric name.
- Package-install commands for every OS.
- Every container deployment manifest.
- Console click paths.

### Ready when

Given missing EC2/ECS/EKS telemetry, you can identify:

1. Is agent needed?
2. Where should it run?
3. Which config section matters?
4. Which IAM/network path is required?
5. Which evidence proves the fix?

---

## Skill 1.1.3 - Configure and troubleshoot CloudWatch alarms

**Official goal:** Create alarms, connect actions, reduce noise, fix failures.

### What exam tests

- Primary: `CFG BEH DIA REM`
- Supporting: `EVD GOV`
- Precision: `L3 - Property`
  - Exact states and evaluation settings matter.

### Core model

```text
Metric
  -> alarm evaluates data
  -> alarm changes state
  -> action runs / EventBridge receives event
```

### Exact alarm types

| Type | Watches |
|---|---|
| Metric alarm | One metric or metric-math expression |
| Anomaly alarm | Metric against expected band |
| Composite alarm | States of other alarms |

Composite alarm:

```text
CPU alarm AND latency alarm
  -> service alarm
  -> less noise
```

It does not read raw metrics directly.

### Exact states

- `OK`: threshold condition not met.
- `ALARM`: threshold condition met.
- `INSUFFICIENT_DATA`: not enough usable data.

State is not the same as action delivery.

```text
Alarm can be ALARM
but notification can still fail.
```

### Exact evaluation properties

- Metric namespace.
- Metric name.
- Dimensions.
- Statistic: average, sum, min, max, percentile.
- Period: size of one time bucket.
- Threshold and comparison.
- Evaluation periods: `N` recent periods checked.
- Datapoints to alarm: `M` breaching points required.
- Missing-data treatment.

Example:

```text
3 of 5
  -> inspect 5 periods
  -> ALARM when at least 3 breach
```

Missing data can be treated as:

- Missing.
- Breaching.
- Not breaching.
- Ignore current state change.

Choice depends on meaning:

```text
No requests may be normal.
No heartbeat may be failure.
```

### Actions to know

- SNS notification.
- Lambda invocation.
- EC2 action.
- Auto Scaling action.
- Systems Manager operational action where supported.
- EventBridge receives alarm state-change events and routes them.

Direct alarm action:

```text
Alarm -> SNS
```

Filtered/multi-target reaction:

```text
Alarm state event -> EventBridge rule -> target(s)
```

### Configuration path

```text
Choose metric
  -> verify namespace/dimensions
  -> choose statistic and period
  -> set threshold
  -> set M of N
  -> choose missing-data behavior
  -> add action
  -> verify state and delivery
```

### Evidence chain

```text
Metric graph
  -> alarm state reason
  -> alarm history
  -> action configuration
  -> target permissions/policy
  -> target delivery status
```

For SNS:

```text
Alarm history
  -> topic ARN and policy
  -> subscription confirmed
  -> filter/delivery result
```

### Failure clues

| Symptom | First checks |
|---|---|
| Always `INSUFFICIENT_DATA` | Region, namespace, dimensions, period, source data |
| Never alarms | Wrong statistic, threshold, comparison, M/N, missing-data choice |
| Too noisy | Period/threshold too sensitive; use M/N or composite alarm |
| Alarm state correct, no message | Actions enabled, SNS topic policy, subscription confirmation, KMS |
| Wrong resource alarms | Dimension mismatch |
| Composite stays wrong | Child alarm states and Boolean rule |
| Automation fails | Target role, permissions, supported action, execution history |

### Selection rules

| Need | Choose |
|---|---|
| Alert from one metric | Metric alarm |
| Detect unusual baseline | Anomaly alarm |
| Alert only when several conditions agree | Composite alarm |
| Turn log pattern into alarm | Metric filter -> metric alarm |
| Send simple notification | Alarm -> SNS |
| Route/enrich state change | Alarm -> EventBridge -> target |

### Exam traps

- Dashboard shows data. Dashboard does not evaluate alarm state.
- Log filter alone does not alarm. It creates a metric.
- Composite alarm watches alarms, not raw metrics.
- Wrong dimension often creates no data, not an obvious error.
- `INSUFFICIENT_DATA` does not automatically mean workload failure.
- Alarm success does not prove SNS/email delivery.
- EventBridge routes the state event. CloudWatch still evaluates the alarm.
- High-resolution data and short periods can increase cost/noise.

### Do not memorize

- Every comparison operator.
- Full alarm API/CloudFormation syntax.
- Every supported action by resource type.
- Console click paths.

### Ready when

Given an alarm scenario, you can identify:

1. Correct metric and dimensions.
2. Correct statistic, period, and M-of-N rule.
3. Correct missing-data behavior.
4. Direct action or EventBridge routing.
5. Exact evidence showing where failure occurred.

---

## Skill 1.1.4 - Create and manage CloudWatch dashboards

**Official goal:** Build useful, shareable dashboards across accounts and Regions.

### What exam tests

- Primary: `CFG BEH`
- Supporting: `SEL EVD GOV`
- Precision: `L2 - Object`
  - Know widgets, data scope, sharing, and cross-account objects.

### Core model

```text
Existing telemetry
  -> dashboard widgets
  -> one operational view
```

Dashboard displays data.

```text
It does not collect data.
It does not evaluate alarms.
```

### Exact objects to know

- Dashboard: group of widgets.
- Metric widget: graph or number from metrics.
- Alarm widget: alarm state/view.
- Log-query widget: Logs Insights result.
- Text widget: runbook links and operator notes.
- Explorer-style widget: resource/tag-based view.
- Variable: reusable account/Region/resource input.
- Time range: dashboard-wide or widget context.

Cross-account observability:

- Monitoring account: central view.
- Source account: owns telemetry.
- Sink: monitoring destination relationship.
- Link: source-to-sink connection and permissions.

### Build path

```text
Define operator question
  -> choose telemetry
  -> choose account and Region
  -> choose namespace/dimensions
  -> choose statistic and period
  -> select widget
  -> set time range/variables
  -> configure access/sharing
  -> verify every widget
```

Good dashboard order:

```text
Service health
  -> traffic
  -> errors
  -> latency
  -> saturation/capacity
  -> logs and runbook link
```

### Cross-account and Region model

```text
Source accounts
  -> cross-account observability links
  -> monitoring account
  -> central dashboard
```

- Cross-account observability gives central access to linked telemetry.
- Cross-account/cross-Region dashboards can show data from several scopes.
- Always verify account and Region of each widget.

Important:

```text
Central view != central data copy.
```

### Sharing

| Need | Approach |
|---|---|
| Operations team access | Authenticated dashboard access |
| Central multi-account view | Monitoring account and source links |
| External/public view | Shared dashboard with strict data review |

Public sharing risk:

- Resource names.
- Metric labels.
- Operational patterns.
- Text-widget links or sensitive notes.

### Evidence to inspect

- Widget source account and Region.
- Namespace, metric, and dimensions.
- Statistic, period, and time range.
- Logs Insights query result.
- Alarm state and underlying alarm.
- Cross-account sink/link state and permissions.
- Dashboard access or sharing configuration.

### Failure clues

| Symptom | First checks |
|---|---|
| Empty metric widget | Account, Region, namespace, dimensions, time range |
| Wrong values | Statistic, period, aggregation, metric math |
| Log widget empty | Query, log group, Region, time range, permissions |
| Source account missing | Sink/link, source permissions, correct monitoring account |
| User cannot open dashboard | IAM or sharing configuration |
| Alarm widget unexpected | Underlying alarm state/configuration, not dashboard |
| Slow/noisy dashboard | Too many widgets, broad queries, bad default time range |

### Selection rules

| Need | Choose |
|---|---|
| Native AWS operational view | CloudWatch dashboard |
| Alert when condition breaches | CloudWatch alarm |
| Query logs | Logs Insights |
| Prometheus/many data sources | Managed Grafana may fit better |
| Move telemetry centrally | Logging/metric centralization, not dashboard alone |

### Exam traps

- Dashboard does not create telemetry.
- Dashboard does not replace alarms.
- Cross-account viewing does not move data.
- Empty widget often means wrong dimension/account/Region.
- A shared dashboard can expose operational details.
- Correct metric with wrong statistic can mislead.
- Text widgets can carry runbook context but execute nothing.

### Do not memorize

- Dashboard JSON body.
- Every widget property.
- Console layout.
- Exact visual styling options.

### Ready when

Given a dashboard scenario, you can identify:

1. Correct widget and telemetry.
2. Correct account/Region/dimensions.
3. Correct cross-account setup.
4. Safe sharing model.
5. Why a widget is empty or misleading.

---

## Skill 1.1.5 - Configure SNS notifications and alarm integration

**Official goal:** Send AWS notifications through SNS and connect alarms to SNS.

### What exam tests

- Primary: `CFG BEH DIA`
- Supporting: `SEL GOV`
- Precision: `L2 - Object`
  - Know topic, subscription, policy, encryption, and delivery path.

### Core model

```text
Publisher
  -> SNS topic
  -> subscription(s)
  -> endpoint(s)
```

Alarm path:

```text
CloudWatch alarm state change
  -> SNS topic
  -> email/SQS/Lambda/HTTP(S)/other endpoint
```

### Exact objects to know

- Topic: message destination and fan-out point.
- Publisher: service or principal sending message.
- Subscription: topic-to-endpoint connection.
- Protocol: endpoint type.
- Endpoint: message receiver.
- Topic policy: who can publish or subscribe.
- Filter policy: which messages a subscription receives.
- Delivery policy: retry behavior for supported endpoints.
- KMS key: encrypts topic messages at rest when configured.
- Dead-letter queue: stores failed deliveries for supported subscriptions.

### Topic types

| Type | Main use |
|---|---|
| Standard | General pub/sub and fan-out; common alarm target |
| FIFO | Ordered, deduplicated messaging for supported endpoints |

For exam alarm scenarios:

```text
CloudWatch alarm -> standard SNS topic
```

### Configuration path

```text
Create topic
  -> configure encryption/policy
  -> create subscription
  -> confirm subscription if required
  -> attach topic to alarm/service
  -> trigger test event
  -> verify endpoint delivery
```

Direct alarm notification:

```text
Alarm -> SNS
```

Filtered or transformed event:

```text
AWS event/alarm state
  -> EventBridge rule
  -> SNS
```

### Permissions model

Three checks:

```text
Can publisher send to topic?
Can SNS use the KMS key?
Can SNS deliver to endpoint?
```

Possible controls:

- Publisher IAM permission.
- SNS topic resource policy.
- KMS key policy/grant.
- Target resource policy, such as SQS queue policy.
- Cross-account permissions when accounts differ.

### Subscription behavior

- Email/HTTP-style subscriptions may require confirmation.
- Pending confirmation means no normal delivery.
- Filter policy can intentionally drop nonmatching messages.
- One topic can fan out to several subscriptions.
- Each subscription can use a different protocol/filter.

### Evidence chain

```text
Source event/alarm history
  -> topic ARN
  -> topic policy and KMS key
  -> subscription status/filter
  -> delivery attempt/failure evidence
  -> endpoint health
```

### Failure clues

| Symptom | First checks |
|---|---|
| Alarm changed, no email | Alarm action, topic ARN, confirmed subscription, spam/endpoint |
| No message reaches topic | Publisher permission, topic policy, Region/account |
| Encrypted topic fails | KMS key policy and service permissions |
| Only some subscribers receive | Subscription status, filter policy, protocol-specific failure |
| SQS receives nothing | Queue policy allows SNS, subscription correct |
| EventBridge route fails | Rule match, target role/policy, retry/DLQ |
| Duplicate/unordered message concern | Standard-topic behavior; check whether FIFO is required/supported |

### Selection rules

| Need | Choose |
|---|---|
| Fan out one message | SNS |
| Human alarm email | Alarm -> SNS email subscription |
| Durable worker queue | SQS |
| Filter/transform AWS events | EventBridge |
| Application-formatted email | SES, often invoked by application/Lambda |
| Multi-step notification workflow | Step Functions or automation around SNS |

Fast clues:

```text
Broadcast? SNS.
Buffer work? SQS.
Route events? EventBridge.
Send application email? SES.
```

### Exam traps

- Creating an email subscription is not enough; it may need confirmation.
- Alarm state can be correct while SNS delivery fails.
- IAM allow can still fail because topic or KMS policy denies.
- SNS filter policy can make a healthy subscription look broken.
- EventBridge routes/filters; SNS fans out.
- SNS sends messages; it does not prove a human read them.
- SES is not a direct CloudWatch alarm action.
- Wrong account or Region can point to the wrong topic.

### Do not memorize

- Full SNS policy JSON.
- Every supported protocol.
- Exact retry timings.
- Console click paths.

### Ready when

Given a notification failure, you can identify:

1. Did the source publish?
2. Is the topic correct and allowed?
3. Is KMS blocking access?
4. Is the subscription confirmed and matched?
5. Did the endpoint accept delivery?

---

### Task 1.2 - Identify and remediate issues by using monitoring and availability metrics

## Skill 1.2.1 - Analyze performance metrics and automate remediation

**Official goal:** Use AWS evidence to find issues and automate safe correction.

### What exam tests

- Primary: `EVD DIA REM`
- Supporting: `SEL OPT GOV`
- Precision: `L2 - Object`
  - Know evidence sources, metric meanings, and remediation tools.

### Core model

```text
Symptom
  -> evidence
  -> correlation
  -> likely cause
  -> safe action
  -> verify recovery
```

Do not start with the fix.

```text
First prove scope, time, and cause.
```

### First five questions

1. What failed?
2. When did it start?
3. Which resources/users are affected?
4. What changed before it started?
5. Which dependency is saturated or unavailable?

### Evidence sources

| Need | Evidence |
|---|---|
| Resource/application performance | CloudWatch metrics |
| Error details | CloudWatch/application logs |
| Who changed AWS configuration | CloudTrail |
| AWS-side event or planned maintenance | AWS Health Dashboard |
| Request path and dependency latency | Traces/X-Ray views |
| Deployment/resource change | CloudFormation events, CloudTrail, deployment history |
| Automation result | Systems Manager/Lambda execution history and logs |

### Metric clues

**EC2**

- High CPU: compute pressure or busy process.
- CPU credit low: burstable instance throttling risk.
- System status failure: AWS host/infrastructure problem.
- Instance status failure: guest OS/network/configuration problem.
- Memory/disk pressure: agent metric required.
- EBS queue/latency high: storage bottleneck possible.

**Lambda**

- `Errors`: invocation failed.
- `Throttles`: concurrency/capacity blocked invocation.
- `Duration`: execution time.
- `ConcurrentExecutions`: concurrency use.
- Iterator age/backlog metric: consumer falling behind.

**ECS/EKS**

- Desired > running: placement/startup/health problem.
- CPU/memory high: workload pressure.
- Repeated restarts: application, probe, resource, or dependency problem.
- Node pressure: cluster capacity problem.

**RDS/Aurora**

- High connections: connection exhaustion risk.
- High CPU/DB load: compute/query pressure.
- Low free memory/storage: capacity pressure.
- High read/write latency or queue: storage bottleneck.
- Replica lag: replica cannot keep up.

**DynamoDB**

- Throttled requests: capacity or hot-partition problem.
- Consumed near provisioned: capacity pressure.
- High latency with no throttling: inspect application/dependency path too.

These are clues, not automatic proof.

### Correlation path

```text
Metric spike
  -> matching logs
  -> CloudTrail recent change
  -> AWS Health event
  -> affected dependencies
  -> baseline comparison
```

Useful comparisons:

- Before versus after change.
- Healthy resource versus affected resource.
- Average versus percentile latency.
- Traffic versus errors.
- Utilization versus configured limit.
- One AZ/account/Region versus all.

### Pick remediation tool

| Need | Tool |
|---|---|
| Add/remove capacity | Auto Scaling |
| Small custom stateless action | Lambda |
| Governed infrastructure workflow | Systems Manager Automation |
| Route detected event | EventBridge |
| Notify operator | SNS |
| Multi-step stateful workflow | Step Functions |
| AI-assisted operational RCA/remediation | AWS DevOps Agent |
| Interactive investigation/script help | Kiro |

### Automation chain

```text
Detect
  -> CloudWatch alarm / EventBridge event / Config finding / Health event
Route
  -> EventBridge
Act
  -> Lambda / Systems Manager / Auto Scaling
Verify
  -> metric, log, state, execution history
Notify
  -> SNS
```

### Safe automation controls

- Least-privilege execution role.
- Narrow resource/tag scope.
- Idempotent action.
- Retry limit and backoff.
- Concurrency/rate limit.
- Approval for risky action.
- Timeout and failure path.
- Execution logs.
- Rollback or stop condition.
- Verification after change.

### AWS DevOps Agent and Kiro

**AWS DevOps Agent**

- Monitors AWS infrastructure.
- Performs automated root-cause analysis.
- Runs remediation procedures.
- Suggests/configures preventive measures.

**Kiro**

- Helps inspect context and generate scripts/actions.
- Useful for assisted investigation.
- Human validates output and blast radius.

Rule:

```text
AI suggestion != proven cause.
AI action still needs permission and guardrails.
```

### Failure clues

| Symptom | First checks |
|---|---|
| Alarm fired, action did not run | Action config, EventBridge rule, role, target, DLQ |
| Automation ran, issue remains | Wrong cause, wrong target, verification metric |
| Remediation loops | Trigger matches change created by remediation |
| Lambda times out | Timeout, dependency latency, network, scope |
| Automation denied | Execution role, trust, `PassRole`, resource/KMS policy |
| Scaling happens, latency remains | Downstream/database/storage bottleneck |
| Only one AZ affected | AZ resources, routes, capacity, AWS Health |

### Exam traps

- Correlation is not always causation.
- CloudTrail shows change/API activity, not CPU or latency.
- More compute does not fix every bottleneck.
- Auto Scaling can overload an already-limited database.
- A restart may hide the cause and lose evidence.
- Event-driven remediation can create loops.
- Broad Lambda permissions make a small error dangerous.
- AI output needs verification.
- Successful execution does not prove service recovery.

### Do not memorize

- Every service metric.
- Every DevOps Agent/Kiro command.
- Full remediation code.
- Fixed thresholds without workload context.

### Ready when

Given a performance incident, you can:

1. Find the best evidence.
2. Correlate symptom with change/dependency.
3. Select likely cause, not only symptom.
4. Choose the smallest safe remediation tool.
5. Prove the workload recovered.

---

## Skill 1.2.2 - Route, enrich, and deliver events with EventBridge

**Official goal:** Match AWS events, route them to targets, and fix failed rules.

### What exam tests

- Primary: `CFG BEH DIA REM`
- Supporting: `SEL GOV`
- Precision: `L3 - Property`
  - Exact bus, pattern, event fields, target, retry, and DLQ matter.

### Core model

```text
Event source
  -> event bus
  -> rule pattern
  -> optional transform
  -> target
```

Rule matches?

```text
Yes -> target delivery attempted.
No  -> nothing happens.
```

### Exact bus types

| Bus | Use |
|---|---|
| Default bus | Events from AWS services and account applications |
| Custom bus | Application/custom events |
| Partner bus | Supported SaaS partner events |

Cross-account path:

```text
Source account rule
  -> destination event bus
  -> destination bus policy allows event
  -> destination rule
  -> destination target
```

### Event structure to know

- `source`: event producer.
- `detail-type`: event category.
- `detail`: service-specific payload.
- `resources`: affected resource ARNs when supplied.
- `account`: source account.
- `region`: source Region.
- `time`: event time.
- `id`: event identifier.

Important:

```text
Pattern must match real nesting and values.
```

### Exact rule objects

- Event pattern: content to match.
- Schedule: time-based trigger.
- Rule state: enabled or disabled.
- Target: destination service/resource.
- Input path: select event fields.
- Input transformer: build new target payload.
- Target role/resource policy: allows delivery.
- Retry policy: retry failed delivery.
- Maximum event age: stop retrying stale event.
- Dead-letter queue: keep failed target deliveries.
- Archive: retain selected bus events.
- Replay: send archived events back for processing.

### Configuration path

```text
Choose bus
  -> capture real sample event
  -> build/test pattern
  -> create rule
  -> add target
  -> transform input if needed
  -> configure role/policy
  -> set retry and DLQ
  -> enable rule
  -> send test event
  -> verify target
```

### Enrichment and transformation

Basic transformation:

```text
Large source event
  -> input path selects fields
  -> transformer creates target message
```

Use when target needs:

- Different field names.
- Smaller payload.
- Static text plus event values.
- Only selected details.

Need external lookup or complex logic?

```text
EventBridge -> Lambda/Step Functions -> enriched action
```

### Permissions model

Check two directions:

```text
Can source put event on bus?
Can EventBridge invoke target?
```

Possible controls:

- Event-bus resource policy.
- EventBridge target execution role.
- Target resource policy.
- Cross-account trust/permissions.
- KMS/resource permissions used by target.

### Evidence chain

```text
Source emitted event
  -> correct account/Region/bus
  -> rule enabled
  -> pattern matches
  -> target invoked
  -> retry/DLQ state
  -> target logs/history
```

Best test input:

```text
Actual captured event shape.
Not guessed event shape.
```

### Failure clues

| Symptom | First checks |
|---|---|
| Rule never triggers | Bus, account, Region, rule enabled, event pattern |
| Some events match | Pattern values, arrays, nested `detail`, event variants |
| Rule matches, target fails | Target ARN, role/resource policy, target availability |
| Wrong target payload | Input path/transformer and field paths |
| Cross-account event missing | Destination bus policy and source rule/role |
| Repeated failures | Retry settings, target error, DLQ |
| Automation loop | Remediation creates another matching event |
| Replay causes duplicate action | Target idempotency and replay scope |

### Selection rules

| Need | Choose |
|---|---|
| Match and route events | EventBridge |
| Fan out same message | SNS |
| Buffer work for consumer | SQS |
| Small custom reaction | Lambda target |
| Multi-step stateful process | Step Functions target |
| Governed infrastructure remediation | Systems Manager Automation target/workflow |
| Notify people | SNS target |

Fast clues:

```text
Route by event content? EventBridge.
Broadcast? SNS.
Queue work? SQS.
Remember workflow state? Step Functions.
```

### Exam traps

- EventBridge is not a durable worker queue.
- DLQ stores failed target deliveries, not unmatched events.
- Rule on wrong bus or Region sees nothing.
- Correct field value at wrong nesting level does not match.
- EventBridge routes event; target still needs permission.
- Input transformer reshapes data; it does not perform external lookup.
- Archive/replay can repeat business action; target must be idempotent.
- Remediation event can trigger itself again.

### Do not memorize

- Full event-pattern syntax.
- Every possible target.
- Every service event schema.
- Exact retry timing defaults.
- Console click paths.

### Ready when

Given a failed event workflow, you can identify:

1. Did source emit the event?
2. Did it reach the correct bus?
3. Does the pattern match the real event?
4. Can EventBridge invoke the target?
5. Is failure visible in retry, DLQ, or target evidence?

---

## Skill 1.2.3 - Create and run Systems Manager Automation runbooks

**Official goal:** Use AWS-managed or custom runbooks to automate operational work.

### What exam tests

- Primary: `CFG REM PRC GOV`
- Supporting: `DIA EVD`
- Precision: `L2 - Object`
  - Know runbook parts, execution controls, roles, and evidence.

### Core model

```text
Trigger/operator
  -> Automation runbook
  -> ordered steps
  -> AWS resources/actions
  -> outputs and execution status
```

Runbook is definition.

```text
Automation execution is one run of that definition.
```

### Exact objects to know

- Automation document/runbook: workflow definition.
- AWS-managed runbook: maintained predefined document.
- Custom runbook: customer-defined document.
- Document version: immutable version.
- Default version: version used when none specified.
- Parameter: runtime input.
- Step: one workflow action.
- Action: operation performed by step.
- Input: data given to action.
- Output: value returned/reused by later step.
- Automation execution: running workflow instance.
- Execution role: permissions used by Automation.
- Target: resource(s) receiving action.
- Rate control: concurrency and error limit.

### Important actions

| Need | Automation action |
|---|---|
| Call AWS API | `aws:executeAwsApi` |
| Run command on managed node | `aws:runCommand` |
| Run Python/PowerShell script | `aws:executeScript` |
| Invoke Lambda | `aws:invokeLambdaFunction` |
| Choose path | `aws:branch` |
| Wait for resource state | `aws:waitForAwsResourceProperty` |
| Verify resource state | `aws:assertAwsResourceProperty` |
| Call another runbook | `aws:executeAutomation` |

Exact full syntax is not needed.

### Execution paths

- Manual operator start.
- EventBridge rule.
- CloudWatch operational action where supported.
- AWS Config remediation.
- Maintenance Window.
- CLI/SDK call.
- Multi-account/multi-Region execution.

### Configuration path

```text
Choose managed/custom runbook
  -> review exact version
  -> set parameters
  -> choose targets
  -> set execution role
  -> set concurrency/error controls
  -> add approval if risky
  -> execute
  -> inspect each step
  -> verify resource outcome
```

Custom runbook flow:

```text
Define parameters
  -> define ordered steps/actions
  -> connect outputs to later inputs
  -> define retry/timeout/failure path
  -> test on small scope
  -> publish version
```

### Permissions model

Three actors may matter:

```text
Caller
  -> allowed to start Automation
Caller/service
  -> allowed to pass execution role
Execution role
  -> allowed to perform runbook actions
```

Also check:

- Role trust policy.
- `iam:PassRole`.
- Resource policy.
- KMS key policy.
- Cross-account trust.
- Managed-node IAM role for `aws:runCommand`.

### Safety controls

- Narrow targets using tags/resource IDs.
- Limit concurrency.
- Stop after error threshold.
- Require approval for destructive action.
- Set timeout and retry limit.
- Use idempotent steps.
- Log outputs.
- Verify state before and after change.
- Test new version on one resource first.

### Evidence chain

```text
Automation execution
  -> execution status
  -> failed/waiting step
  -> step inputs and outputs
  -> role/API error
  -> target resource state
```

Best evidence:

- Execution ID and selected document version.
- Step-level status.
- Step output/error message.
- Approval state.
- Target and parameter values.
- CloudTrail API activity.
- Managed-node command output when used.

### Failure clues

| Symptom | First checks |
|---|---|
| Automation cannot start | Caller permission, parameters, document/version, `PassRole` |
| First AWS action denied | Execution role trust and permissions |
| Run Command step fails | Managed-node state, agent, node role, network, command output |
| Later step gets empty value | Earlier output selector/reference |
| Execution waits | Approval, wait condition, resource never reaches state |
| Only some targets run | Target tags, concurrency, error threshold |
| Cross-account run fails | Trust, delegated roles, account/Region configuration |
| Runbook succeeds, resource wrong | Weak assertion or wrong target/parameter |

### Selection rules

| Need | Choose |
|---|---|
| Governed multi-step AWS operation | Systems Manager Automation |
| One command across managed nodes | Run Command |
| Keep node configuration compliant | State Manager |
| Small custom stateless code | Lambda |
| Application workflow with long-lived state | Step Functions |
| Scheduled maintenance task | Maintenance Window + suitable task/runbook |

### Exam traps

- Runbook definition is not execution evidence.
- Latest document version may not be default version.
- Caller permission does not give execution role permission.
- Execution role permission does not give caller `PassRole`.
- `aws:runCommand` needs a managed node; AWS API actions may not.
- Approval can make a healthy execution appear stuck.
- Successful steps do not prove final workload recovery.
- High concurrency can widen damage.
- Retrying a non-idempotent destructive step can repeat damage.
- AWS-managed runbook still needs correct scope and permissions.

### Do not memorize

- Full runbook YAML/JSON.
- Every Automation action.
- Complete SDK code.
- Every execution status.
- Console click paths.

### Ready when

Given an Automation scenario, you can identify:

1. Correct runbook and version.
2. Correct parameters and targets.
3. Caller, `PassRole`, and execution-role permissions.
4. Failed step and its evidence.
5. Safe retry, repair, or rollback action.

---

### Task 1.3 - Optimize compute, storage, and database resources

## Skill 1.3.1 - Optimize compute resources and remediate performance problems

**Official goal:** Use metrics, tags, and AWS tools to fix compute performance and waste.

### What exam tests

- Primary: `EVD DIA OPT`
- Supporting: `SEL REM`
- Precision: `L2 - Object`
  - Know bottleneck signals, compute choices, tags, and optimization tools.

### Core model

```text
Measure
  -> find limiting resource
  -> choose smallest useful change
  -> apply safely
  -> verify performance and cost
```

Rule:

```text
Do not resize from CPU alone.
```

### Bottleneck types

| Limit | Main evidence |
|---|---|
| Compute | CPU utilization, load, processing time |
| Memory | Agent/container memory, swapping, OOM/restarts |
| Network | Throughput, packets, errors, instance network ceiling |
| Storage | EBS latency, queue, IOPS, throughput, filesystem pressure |
| Concurrency | Lambda throttles/concurrency, worker/task backlog |
| Dependency | Database/service latency and errors while compute is healthy |

### EC2 evidence

- `CPUUtilization`: CPU use.
- CPU credit metrics: burst capacity on burstable instances.
- Status checks: instance or AWS host problem.
- Network in/out and packets: traffic and possible ceiling.
- EBS metrics: storage pressure.
- Guest memory/disk/process: CloudWatch agent needed.
- Application latency/error rate: user impact.

Read together:

```text
High CPU + high latency
  -> compute bottleneck possible.

Low CPU + high latency
  -> check memory, storage, network, database, dependency.
```

### Instance choice model

| Workload shape | Instance category |
|---|---|
| Balanced | General purpose |
| CPU-heavy | Compute optimized |
| Large memory/cache/database | Memory optimized |
| Local high I/O | Storage optimized |
| GPU/ML/special hardware | Accelerated computing |
| Small variable CPU | Burstable, if credits fit pattern |

Need exact family category.
No need full instance catalog.

### Remediation choices

| Finding | Likely action |
|---|---|
| Sustained CPU/memory saturation | Resize instance/task or scale out |
| Short predictable peak | Scheduled scaling or suitable burst capacity |
| Variable demand | Auto Scaling/managed scaling |
| CPU credits exhausted | Change size/type or move from burst model |
| Low sustained utilization | Downsize after peak/headroom review |
| Network/EBS ceiling | Choose instance with higher relevant capability |
| Wrong architecture/family | Move only after compatibility check |
| Downstream bottleneck | Fix dependency; more compute may hurt it |

Vertical versus horizontal:

```text
Resize one resource = vertical.
Add/remove resources = horizontal.
```

### Containers

**ECS/EKS signals**

- CPU/memory utilization.
- CPU/memory reservation or requests.
- Limits and throttling.
- OOM/restarts.
- Desired versus running tasks/pods.
- Node utilization and placement capacity.

Patterns:

```text
Task/pod limit too low -> throttling/OOM.
Request too high -> poor placement/waste.
Nodes full -> workload cannot schedule.
Nodes empty -> possible waste.
```

### Lambda

- Memory setting also changes available CPU.
- Compare memory, duration, errors, throttles, and concurrency.
- More memory can reduce duration.
- Higher memory is not always higher total cost if runtime drops enough.
- Check downstream limits before increasing concurrency.

### Tags

Tags help:

- Group workload/environment.
- Assign owner.
- Filter metrics/cost.
- Target automation.
- Apply different schedules or policies.

Useful examples:

```text
Application, Environment, Owner, CostCenter, Schedule
```

Wrong/missing tag can target wrong resource or miss it entirely.

### AWS optimization tools

**Compute Optimizer**

- Uses observed utilization.
- Recommends suitable resource configuration.
- Shows performance risk and savings context.
- Recommendation needs validation before change.

**Cost Explorer**

- Interactive cost trends, grouping, and forecast.

**Cost and Usage Report**

- Detailed line-item usage/cost data.
- Often queried from S3 with Athena.

**Savings Plans**

- Commitment-based discount for eligible compute use.
- Reduces price; does not resize resource or fix performance.

### Optimization path

```text
Choose observation window
  -> include peak and normal load
  -> group by tags/workload
  -> inspect all limiting metrics
  -> review Compute Optimizer/cost evidence
  -> choose change
  -> test/deploy safely
  -> compare before/after
```

Verify:

- Latency/errors improved.
- Resource no longer saturated.
- Required headroom remains.
- Cost moved as expected.
- No downstream service became bottleneck.

### Failure clues

| Symptom after change | First checks |
|---|---|
| Smaller instance now slow | Peak CPU/memory/network/EBS limit |
| Larger instance still slow | Dependency, storage, query/application path |
| Scale-out fails | Launch config, subnet IPs, quotas, health checks |
| Containers still restart | Limits, memory leak/pressure, probe/dependency |
| Lambda cost rises | Memory-duration balance and invocation volume |
| Recommendation unsafe | Observation window, architecture, headroom, licensing |
| Automation changed wrong fleet | Tag selection |

### Exam traps

- Low average utilization can hide short critical peaks.
- CPU is not the only instance limit.
- More EC2 instances can overload database/downstream service.
- Compute Optimizer recommends; it does not prove safe migration.
- Savings Plans optimize price, not performance.
- Tags organize and target; tags do not improve performance themselves.
- Graviton/architecture change needs software/image compatibility.
- Downsizing without memory metrics is guesswork.
- Stop/start or replacement may be required for some changes.

### Do not memorize

- Every EC2 family and size.
- Exact prices or Savings Plans discount.
- Every Compute Optimizer field.
- Fixed utilization threshold for all workloads.
- Console click paths.

### Ready when

Given a compute problem, you can:

1. Identify the limiting resource.
2. Choose resize, scale, or dependency fix.
3. Use tags and tools without unsafe scope.
4. Explain cost/performance trade-off.
5. Prove improvement with before/after evidence.

---

## Skill 1.3.2 - Analyze and optimize EBS performance

**Official goal:** Read EBS metrics, find storage bottlenecks, choose better volume settings/type.

### What exam tests

- Primary: `SEL EVD DIA OPT REM`
- Supporting: `CFG`
- Precision: `L3 - Property`
  - Exact volume type, IOPS, throughput, burst, queue, and limits matter.

### Core model

```text
Application I/O
  -> filesystem
  -> EBS volume limit
  -> EC2 EBS limit
```

Actual performance:

```text
Lower of volume capability and EC2 capability.
```

### Volume types

| Type | Best fit | Key behavior |
|---|---|---|
| `gp3` | Most general SSD workloads | Size, IOPS, throughput adjusted independently |
| `gp2` | Existing general SSD workloads | IOPS tied to size; burst-credit behavior |
| `io2` | Critical, high-IOPS transactional workload | Provisioned IOPS, high durability, consistent performance |
| `io1` | Older provisioned-IOPS workload | Provisioned IOPS; know as existing option |
| `st1` | Large sequential throughput | Throughput-optimized HDD |
| `sc1` | Cold, infrequent sequential data | Lowest-cost HDD |

Fast choice:

```text
Small random I/O? SSD.
Large sequential I/O? HDD may fit.
General workload? gp3.
Critical consistent high IOPS? io2.
```

`st1` and `sc1` are not boot-volume choices.

### Exact performance properties

- Capacity: GiB/TiB stored.
- IOPS: operations per second.
- Throughput: MiB/s transferred.
- Latency: time per I/O.
- Queue length: waiting I/O requests.
- Burst credits: temporary performance above baseline on supported types.
- EC2 EBS bandwidth/IOPS ceiling: instance-side limit.

Do not mix:

```text
IOPS = operation rate.
Throughput = data rate.
```

### Metrics to know

| Metric | Meaning |
|---|---|
| `VolumeReadOps` / `VolumeWriteOps` | Number of read/write operations |
| `VolumeReadBytes` / `VolumeWriteBytes` | Data transferred |
| `VolumeTotalReadTime` / `VolumeTotalWriteTime` | Time spent on I/O; helps derive latency |
| `VolumeQueueLength` | Waiting operations |
| `VolumeIdleTime` | Time with no I/O |
| `VolumeThroughputPercentage` | Used throughput versus provisioned capability where available |
| `VolumeConsumedReadWriteOps` | Consumed operations for supported provisioned volumes |
| `BurstBalance` | Remaining burst credits where applicable |

Filesystem free space is not native EBS telemetry.

```text
Need free disk space? CloudWatch agent/OS metric.
```

### Bottleneck patterns

```text
High queue + high latency + max IOPS
  -> IOPS saturation likely.

Large sequential workload + throughput ceiling
  -> throughput saturation likely.

BurstBalance near zero + slower I/O
  -> burst credits exhausted.

Volume metrics below limit + poor performance
  -> check EC2 limit, filesystem, application, network/dependency.
```

Queue alone is not proof. Expected queue depends on workload and volume type.

### Optimization choices

| Finding | Action |
|---|---|
| General SSD needs independent tuning | Move to/tune `gp3` |
| Sustained critical high IOPS | Use/tune `io2` |
| Large sequential throughput | Consider `st1` |
| Cold sequential workload | Consider `sc1` |
| Volume IOPS/throughput too low | Increase provisioned values |
| EC2 is limiting EBS | Change EC2 type/size |
| Burst model exhausted often | Provision sustained performance/change type |
| Restored volume first reads slow | Initialize data or use supported fast-restore feature |
| One volume insufficient | Stripe only when justified; accept added risk/management |

### Elastic Volumes

Can modify supported volume settings:

- Type.
- Size.
- IOPS.
- Throughput.

Operational flow:

```text
Modify EBS volume
  -> monitor modification state
  -> extend partition/filesystem if size increased
  -> verify metrics and application
```

Important:

```text
Increasing EBS size does not automatically grow filesystem.
EBS volume cannot simply be shrunk in place.
```

### Snapshot restore behavior

- Snapshot is durable backup source.
- Restored volume can load blocks on first access.
- First-read latency can be higher before initialization.
- Initialize/read blocks when predictable performance is required.
- Fast Snapshot Restore can provide initialized performance where configured/supported.

### Evidence path

```text
Application latency
  -> OS/filesystem metrics
  -> EBS CloudWatch metrics
  -> volume configuration
  -> EC2 EBS capability
  -> recent modification/snapshot restore
```

### Failure clues

| Symptom | First checks |
|---|---|
| High I/O latency | Queue, IOPS/throughput usage, burst, EC2 ceiling |
| Disk full | Filesystem metric, partition/filesystem size, not EBS queue |
| Larger gp3 did not get faster | gp3 IOPS/throughput configured separately |
| Increased volume IOPS did not help | EC2 EBS ceiling or application pattern |
| Restored volume initially slow | Lazy block loading/initialization |
| Modification complete, OS sees old size | Partition/filesystem not extended |
| HDD performs poorly | Check small/random I/O pattern |
| Volume unavailable to another AZ | EBS volume is AZ-scoped |

### Cost model

- Pay for provisioned capacity.
- Some types charge separately for provisioned performance.
- `gp3` can avoid buying extra capacity only to gain performance.
- Remove unattached unused volumes only after ownership/data checks.
- Snapshot retention also creates cost.

### Exam traps

- Volume limit and EC2 EBS limit are separate.
- Bigger `gp3` does not automatically mean more IOPS/throughput.
- `BurstBalance` does not apply to every volume/type.
- High queue can be normal for large sequential HDD work.
- EBS metric does not show filesystem free space.
- Snapshot restore can have first-read penalty.
- Increasing volume size and growing filesystem are separate actions.
- HDD is poor for small random transactional I/O.
- EBS volume belongs to one AZ, even though snapshots can support recreation elsewhere.

### Do not memorize

- Every numeric volume limit.
- Exact price per GiB/IOPS.
- Every metric available on every platform.
- Filesystem-specific resize commands.
- Console click paths.

### Ready when

Given an EBS problem, you can:

1. Identify IOPS, throughput, latency, queue, or capacity issue.
2. Separate volume limit from EC2 limit.
3. Select correct volume type.
4. Apply safe modification and filesystem follow-up.
5. Verify performance and cost improved.

---

## Skill 1.3.3 - Implement and optimize S3 performance strategies

**Official goal:** Improve S3 transfer speed, access pattern, and storage efficiency.

### What exam tests

- Primary: `SEL CFG OPT`
- Supporting: `BEH PRC`
- Precision: `L2 - Object`
  - Know transfer tools, multipart flow, storage classes, and Lifecycle actions.

### Core model

```text
Slow transfer?
  -> optimize network and parallelism.

High storage cost?
  -> optimize storage class and lifecycle.
```

These are different problems.

### Pick the feature

| Need | Use |
|---|---|
| Upload large object reliably | Multipart upload |
| Faster far-away client upload/download | S3 Transfer Acceleration |
| Bulk/recurring managed data movement | DataSync |
| Frequently read web content near users | CloudFront |
| Move old objects to cheaper class | S3 Lifecycle transition |
| Delete expired objects/versions | S3 Lifecycle expiration |
| Remove abandoned multipart parts | Abort incomplete multipart upload rule |
| Read only part of large object | Byte-range GET |

Fast clues:

```text
One huge upload? Multipart.
Remote users worldwide? Transfer Acceleration.
Move file estate? DataSync.
Cache downloads? CloudFront.
Old objects cost too much? Lifecycle.
```

### Multipart upload

Flow:

```text
Initiate upload
  -> upload parts, often in parallel
  -> retry failed parts only
  -> complete upload
```

If abandoned:

```text
Abort upload
or Lifecycle removes incomplete parts.
```

Benefits:

- Parallel upload.
- Retry one failed part.
- Resume workflow more easily.
- Better use of available bandwidth.

Trap:

```text
Uncompleted parts consume storage and cost money.
```

### Transfer Acceleration

```text
Remote client
  -> nearest AWS edge
  -> optimized AWS path
  -> S3 bucket
```

Use when:

- Client is far from bucket Region.
- Internet path is limiting transfer.
- Speed test shows benefit.

Do not assume benefit:

- Same-Region compute may already have good path.
- Acceleration adds cost.
- Test before choosing.

### DataSync

Core objects:

- Source location.
- Destination location.
- Task.
- Schedule.
- Agent when required for on-premises access.
- Task execution and verification status.

Use for:

- Large file/object migration.
- Recurring synchronization.
- Managed parallel transfer.
- Verification and reporting.
- On-premises-to-AWS or AWS-storage movement.

DataSync moves data.

```text
It does not cache application reads.
```

### Request-performance model

- Parallelize independent requests.
- Use multipart upload for large objects.
- Use byte-range GET for parallel/partial reads.
- Keep compute near bucket when practical.
- Reuse connections through SDK/client behavior.
- Retry temporary errors with exponential backoff.
- Monitor `4xx`, `5xx`, latency, and throughput.
- Scale request rate gradually when workload jumps sharply.

`503 Slow Down` clue:

```text
Retry with backoff.
Avoid synchronized retry storm.
```

### Storage classes

| Access pattern | Likely class |
|---|---|
| Frequent, low-latency access | S3 Standard |
| Unknown/changing access | S3 Intelligent-Tiering |
| Infrequent, multi-AZ access | S3 Standard-IA |
| Infrequent, recreatable, one-AZ data | S3 One Zone-IA |
| Archive with instant access | S3 Glacier Instant Retrieval |
| Archive with slower restore | S3 Glacier Flexible Retrieval |
| Long-term lowest-cost archive | S3 Glacier Deep Archive |

Selection factors:

- Access frequency.
- Retrieval speed.
- Availability/resilience.
- Retrieval charge.
- Minimum storage duration.
- Object size.

### Lifecycle

Lifecycle actions:

- Transition current objects.
- Transition noncurrent versions.
- Expire current objects.
- Expire noncurrent versions.
- Remove expired delete markers where configured.
- Abort incomplete multipart uploads.

Flow:

```text
Filter by prefix/tag/size
  -> wait defined age
  -> transition or expire
```

Lifecycle runs asynchronously.

```text
It reduces storage cost.
It does not speed up upload.
```

### Evidence path

```text
Client transfer time
  -> object size/request pattern
  -> client-to-Region network path
  -> S3 request errors/latency
  -> acceleration/parallel settings
  -> storage class and Lifecycle status
```

For DataSync:

```text
Task execution
  -> bytes/files transferred
  -> verification
  -> skipped/failed item
  -> agent/network/storage error
```

### Failure clues

| Symptom | First checks |
|---|---|
| Large upload slow | Multipart/parallel use, client bandwidth, Region, acceleration test |
| Upload restarts from zero | Multipart not used or state not retained |
| Incomplete-upload cost grows | Abort/Lifecycle rule |
| DataSync task fails | Agent, locations, IAM, network, task log/status |
| Lifecycle did not transition | Rule filter, object age/size/class eligibility |
| Archive retrieval too slow | Wrong class for required retrieval time |
| High read latency for global users | CloudFront/cache pattern, Region/path |
| Many temporary failures | Retry/backoff and request burst pattern |

### Exam traps

- Lifecycle optimizes storage placement, not network speed.
- Transfer Acceleration is not content caching.
- CloudFront caches; DataSync copies.
- Multipart upload must be completed or aborted.
- Cheapest storage class may have retrieval/minimum-duration cost.
- One Zone-IA is not multi-AZ.
- Archive class can violate required retrieval time.
- Retry without backoff can worsen throttling.
- S3 object storage is not a shared POSIX filesystem.

### Do not memorize

- Exact storage prices.
- Every minimum-duration number.
- Multipart API syntax.
- Exact request-rate numbers.
- Every DataSync option.
- Console click paths.

### Ready when

Given an S3 scenario, you can:

1. Separate transfer, request, cache, and storage-cost problems.
2. Choose multipart, acceleration, DataSync, CloudFront, or Lifecycle.
3. Select storage class from access/retrieval needs.
4. Find failed transfer or Lifecycle evidence.
5. Explain performance and cost trade-off.

---

## Skill 1.3.4 - Evaluate and optimize shared storage solutions

**Official goal:** Select and tune EFS, FSx, S3 Files, or other shared storage for the workload.

### What exam tests

- Primary: `SEL BEH OPT`
- Supporting: `CFG`
- Precision: `L2 - Object`
  - Know protocol, filesystem type, mount objects, performance modes, and lifecycle.

### Core model

```text
Protocol/semantics
  -> operating system/workload
  -> performance pattern
  -> availability
  -> cost/lifecycle
```

First question:

```text
Does application need object API or mounted filesystem?
```

### Pick the storage

| Need | Choose |
|---|---|
| Shared Linux NFS filesystem | EFS |
| Windows SMB and Active Directory integration | FSx for Windows File Server |
| Very high parallel/HPC/ML throughput | FSx for Lustre |
| Enterprise NAS, NFS/SMB/iSCSI features | FSx for NetApp ONTAP |
| Existing S3 data exposed with file semantics | S3 Files |
| Object API, massive object storage | S3 |
| Hybrid local file/block/tape access | Storage Gateway |

Fast clues:

```text
Linux shared files? EFS.
Windows SMB? FSx Windows.
HPC parallel files? FSx Lustre.
Enterprise NAS? FSx ONTAP.
S3 data but app needs files? S3 Files.
Only objects needed? S3.
On-premises gateway/cache? Storage Gateway.
```

FSx for OpenZFS is explicitly out of SOA-C03 scope.

### EFS model

```text
Clients in VPC
  -> mount target in AZ
  -> EFS filesystem
```

Exact objects:

- EFS filesystem.
- Mount target.
- Mount-target network interface.
- Security group.
- Access point.
- File-system policy/IAM authorization where used.
- Lifecycle policy.

Main behavior:

- Shared NFS filesystem.
- Multiple clients can mount it.
- Regional option spans AZs.
- One Zone option trades resilience for lower cost.
- Encryption at rest and in transit supported.

### EFS performance modes

| Mode | Fit |
|---|---|
| General Purpose | Most latency-sensitive applications |
| Max I/O | Very high parallelism; higher per-operation latency trade-off |

Choose mode when creating filesystem.

### EFS throughput modes

| Mode | Behavior |
|---|---|
| Elastic | Throughput scales automatically with activity |
| Provisioned | Set throughput independent of stored size |
| Bursting | Baseline grows with stored data; credits support bursts |

Fast choice:

```text
Unknown/spiky load? Elastic.
Known sustained need independent of size? Provisioned.
Size-linked use with bursts? Bursting.
```

### EFS metrics

- `PercentIOLimit`: proximity to I/O limit.
- `PermittedThroughput`: throughput currently allowed.
- `MeteredIOBytes`: metered read/write data.
- `BurstCreditBalance`: burst credits where relevant.
- Client connections: mounted-client activity.

Pattern:

```text
Low burst credits + throughput capped
  -> Bursting mode/size may be limiting.
```

### EFS lifecycle

Lifecycle can move cold files from Standard to lower-cost classes.

```text
No access for defined time
  -> transition to IA/Archive where supported
  -> optional move back on access
```

Trade-offs:

- Lower storage cost.
- Access/retrieval charge.
- First access can be slower.
- Lifecycle changes storage class, not protocol.

### FSx families

**FSx for Windows File Server**

- SMB.
- Windows ACLs.
- Active Directory integration.
- Windows application/home-share use.

**FSx for Lustre**

- Parallel filesystem.
- High throughput and IOPS.
- HPC, analytics, ML, media processing.
- Can integrate with S3 datasets.

**FSx for NetApp ONTAP**

- NFS, SMB, iSCSI use cases.
- Enterprise NAS features.
- Snapshots, cloning, and tiering concepts.

FSx deployment, throughput, storage, backup, and availability settings vary by family.

### S3 Files

Purpose:

```text
Keep data in S3
but let compute use normal file operations.
```

Exact objects:

- S3 bucket containing data.
- S3 file system.
- Mount target.
- Client/mount helper.
- IAM role/policy.
- VPC subnet/security path.
- CloudWatch mount/health metrics.

Use when:

- Data already belongs in S3.
- File-based application/agent needs mounted access.
- Same data should remain available through S3 object access.

Do not choose only because application says “file.” Compare EFS/FSx protocol, OS, latency, throughput, and filesystem-feature needs.

### Storage Gateway

| Gateway pattern | Presents locally |
|---|---|
| File Gateway | File protocol backed by AWS object storage |
| Volume Gateway | iSCSI block volumes with AWS-backed protection |
| Tape Gateway | Virtual tape library backed by AWS storage |

Use when on-premises application needs familiar storage protocol plus AWS-backed storage/cache.

### Configuration path

```text
Choose storage/protocol
  -> choose Region/AZ deployment
  -> create filesystem/gateway
  -> create mount targets/endpoints
  -> configure security/IAM/DNS
  -> mount/connect clients
  -> choose performance/throughput mode
  -> enable lifecycle/backup
  -> verify metrics and access
```

### Failure clues

| Symptom | First checks |
|---|---|
| EFS mount fails | Mount target, AZ/DNS, SG/NACL, NFS client, IAM/access point |
| EFS slow | Throughput mode, I/O limit, burst credits, workload parallelism |
| Windows client cannot access | SMB/AD/DNS/security/permissions; correct FSx family |
| Lustre workload slow | Throughput/storage settings, client concurrency, data loading |
| S3 Files mount fails | File system/mount target, client, IAM, subnet/SG/DNS |
| S3 Files wrong semantics/performance | Compare application need with EFS/FSx |
| Gateway offline | Appliance/agent, network, endpoint, cache/storage, credentials |
| Cost high | Throughput mode, storage tier, lifecycle, unused data/snapshots |

### Exam traps

- EFS is NFS-focused; it is not native Windows SMB storage.
- S3 object API is not a mounted shared filesystem.
- S3 Files exposes S3 data as files; data remains in S3.
- FSx is a family; choose the correct filesystem.
- EFS performance mode and throughput mode are different settings.
- Bursting throughput depends on stored size/credits.
- Lifecycle lowers storage cost; it does not fix active-data throughput.
- One Zone trades resilience for cost.
- Mount target/security/DNS problems can look like filesystem failure.
- Storage Gateway is for hybrid access, not a general replacement for every AWS filesystem.

### Do not memorize

- Every FSx configuration property.
- Exact throughput limits.
- Exact lifecycle prices.
- Mount commands.
- FSx for OpenZFS details.
- Console click paths.

### Ready when

Given a shared-storage scenario, you can:

1. Identify required protocol and semantics.
2. Choose EFS, correct FSx family, S3 Files, S3, or Gateway.
3. Choose performance/throughput/lifecycle settings.
4. Diagnose mount, permission, or performance failure.
5. Explain availability and cost trade-off.

---

## Skill 1.3.5 - Monitor and optimize Amazon RDS

**Official goal:** Use RDS metrics and database insights to find bottlenecks and improve efficiency.

### What exam tests

- Primary: `EVD DIA REM OPT`
- Supporting: `SEL CFG`
- Precision: `L3 - Property`
  - Exact monitoring layer, metric, DB-load view, and remediation choice matter.

### Core model

```text
Application symptom
  -> RDS service metrics
  -> OS metrics
  -> DB load/waits/SQL
  -> limiting layer
  -> targeted change
```

Rule:

```text
High database latency does not always mean high CPU.
```

### Monitoring layers

| Layer | Tool | Shows |
|---|---|---|
| RDS resource | CloudWatch metrics | CPU, memory, connections, storage, I/O, network, replica lag |
| Operating system | Enhanced Monitoring | OS processes, CPU, memory, disk, load at finer detail |
| Database engine | Performance Insights / CloudWatch Database Insights | DB load, waits, SQL, users, hosts, bottlenecks |
| Database logs | RDS logs / CloudWatch Logs export | Engine error, slow-query, audit/general logs where supported |
| Configuration change | CloudTrail / RDS events | Who changed resource and service events |

Fast clues:

```text
Instance CPU/storage? CloudWatch.
OS process/memory detail? Enhanced Monitoring.
Which SQL/wait drives load? Database Insights/Performance Insights.
Who changed DB config? CloudTrail.
```

### Metrics to know

| Metric | Meaning |
|---|---|
| `CPUUtilization` | Instance CPU use |
| `DatabaseConnections` | Open DB connections |
| `FreeableMemory` | Memory available for reuse |
| `FreeStorageSpace` | Remaining allocated storage |
| `ReadLatency` / `WriteLatency` | Time per storage operation |
| `ReadIOPS` / `WriteIOPS` | Storage operation rate |
| `ReadThroughput` / `WriteThroughput` | Storage data rate |
| `DiskQueueDepth` | Waiting storage operations |
| `ReplicaLag` | Delay behind source |
| Network metrics | Data sent/received and possible path pressure |

One metric is rarely enough.

### Database-load model

Performance Insights/Database Insights organizes load by:

- Average active sessions/DB load.
- Wait event.
- SQL statement.
- User.
- Host/application source.

Pattern:

```text
DB load above available vCPU
  -> database work queues somewhere.

CPU wait dominant
  -> compute pressure likely.

I/O wait dominant
  -> storage/query access problem likely.

Lock wait dominant
  -> transaction/contention problem likely.
```

Proactive recommendation:

- Detects problematic metric pattern.
- Suggests action.
- Operator validates before change.

### Diagnosis patterns

| Evidence | Likely direction |
|---|---|
| High CPU + CPU waits + high DB load | Larger instance/read scaling/query optimization |
| High connections + low useful work | Connection pooling/RDS Proxy/application connection control |
| Low free memory + swapping/pressure | Larger memory class or workload/query review |
| Low free storage | Increase storage/enable suitable autoscaling; clean data only with owner approval |
| High latency + queue + IOPS ceiling | Tune storage IOPS/throughput/type |
| High replica lag | Replica capacity, source write rate, long queries/network/engine limits |
| Normal RDS metrics + application slow | Network, application, DNS, proxy, downstream path |
| One SQL dominates DB load | Query/index remediation by responsible team |

### Remediation choices

**Compute**

- Change DB instance class.
- Choose memory/compute profile fitting workload.
- Add read replica/Aurora reader for read scaling.

**Storage**

- Increase allocated storage.
- Adjust storage type, IOPS, or throughput.
- Configure storage autoscaling with safe maximum.
- Storage autoscaling grows; it does not automatically shrink.

**Connections**

- Use RDS Proxy for supported workloads.
- Pool and reuse connections.
- Absorb connection surges.
- Improve connection behavior during failover.

**Database configuration**

- Modify parameter group where justified.
- Know dynamic versus reboot-required parameter behavior.
- Apply immediately or during maintenance window based on risk.

**Queries**

- Use top SQL/waits to prove problem.
- Query/index development is not the CloudOps exam's main coding task.
- CloudOps identifies evidence and coordinates/applies approved change.

### RDS Proxy

```text
Application connections
  -> RDS Proxy pool
  -> fewer/reused database connections
  -> RDS/Aurora
```

Good for:

- Many short-lived connections.
- Lambda/serverless connection bursts.
- Connection pooling.
- Better connection resilience during failover.

Not for:

- Caching query results.
- Adding database CPU.
- Fixing slow SQL.
- Providing read replicas.
- Increasing storage performance.

### Change path

```text
Capture baseline
  -> find limiting layer
  -> choose one targeted change
  -> review outage/reboot/failover effect
  -> apply now or maintenance window
  -> monitor event/change state
  -> compare DB load, latency, errors, cost
```

### Alarm set

Typical alarms:

- CPU sustained high.
- Connections near safe maximum.
- Free storage low.
- Freeable memory low.
- Read/write latency high.
- Replica lag high.
- Database load/wait anomaly.

Use workload baseline. Avoid one universal threshold.

### 2026 console transition

- Exam guide still names RDS Performance Insights.
- Performance Insights console experience ends July 31, 2026.
- Console redirects to CloudWatch Database Insights.
- Performance Insights API continues.

Study the concepts:

```text
DB load + waits + top SQL
```

Do not focus on old console layout.

### Failure clues

| Symptom | First checks |
|---|---|
| CPU alarm but no DB load | Non-database OS process, monitoring mismatch, short spike |
| Connections fail | Connection count, security/network, credentials, Proxy health |
| Storage change did not help | Instance storage ceiling, query pattern, lock/CPU wait |
| Replica lag remains | Replica size, long query, source write volume, engine limits |
| Parameter change absent | Wrong parameter group, pending reboot, apply timing |
| Proxy adds no benefit | Workload not connection-bound or unsupported behavior |
| Modification causes impact | Apply-immediately/maintenance/failover expectations |

### Availability and scaling traps

- Multi-AZ improves availability; it is not primary read scaling.
- Read replica scales reads; replication is asynchronous and can lag.
- RDS Proxy pools connections; it is not a read replica.
- Storage autoscaling does not reduce storage later.
- Larger DB instance does not fix lock contention automatically.
- High average CPU is not required for a serious wait bottleneck.
- Enhanced Monitoring and Database Insights show different layers.
- Recommendation is evidence, not automatic approval.

### Do not memorize

- Every RDS metric.
- Engine-specific SQL tuning syntax.
- Every DB parameter.
- Exact instance/storage prices.
- Old Performance Insights console layout.
- Console click paths.

### Ready when

Given an RDS problem, you can:

1. Choose CloudWatch, Enhanced Monitoring, logs, or DB Insights.
2. Identify compute, memory, connection, storage, lock, or query bottleneck.
3. Select instance, storage, replica, Proxy, or parameter remediation.
4. Predict reboot/failover/maintenance impact.
5. Prove improvement with DB load, latency, errors, and cost.

---

## Skill 1.3.6 - Implement, monitor, and optimize EC2 instances, storage, and networking

**Official goal:** Operate EC2 with the right compute, storage, network, and placement capabilities.

### What exam tests

- Primary: `CFG EVD DIA OPT`
- Supporting: `SEL REM`
- Precision: `L3 - Property`
  - Exact health-check meaning, storage persistence, ceilings, and placement type matter.

### Core model

```text
Instance type defines
  CPU + memory + network + EBS capability.

Workload performance
  = lowest limiting layer.
```

Reuse:

- General compute right-sizing: Skill 1.3.1.
- EBS volume tuning: Skill 1.3.2.

This skill joins those layers at EC2 level.

### Instance health

| Signal | Meaning | First direction |
|---|---|---|
| System status check fails | AWS host/infrastructure path problem | Recover, stop/start, or replace as appropriate |
| Instance status check fails | Guest OS/network/startup problem | Reboot, inspect console/OS, repair or replace |
| Both fail | Host problem can also affect guest | Start with infrastructure recovery |
| Scheduled event | AWS plans maintenance/retirement/change | Act before deadline |

Exact metrics:

- `StatusCheckFailed_System`.
- `StatusCheckFailed_Instance`.
- `StatusCheckFailed`.
- `CPUUtilization`.
- `NetworkIn` / `NetworkOut`.
- `NetworkPacketsIn` / `NetworkPacketsOut`.

Memory/filesystem/process metrics need agent.

### Recovery action

| Need | Action |
|---|---|
| Restart guest OS | Reboot |
| Move EBS-backed instance to new host | Stop/start |
| Restore service through fleet | Auto Scaling replacement |
| Preserve stable public IPv4 | Elastic IP, not auto-assigned public IP |
| Rebuild repeatably | Launch template + AMI |

Stop/start effects:

- Instance store data is lost.
- Auto-assigned public IPv4 can change.
- Private IPv4 normally remains on primary ENI.
- EBS volumes persist.

### Storage model

**EBS**

- Persistent block storage.
- Volume belongs to one AZ.
- Performance limited by volume and EC2 instance capability.
- EBS-optimized path provides dedicated/defined EBS capability.

**Instance store**

- Physically attached ephemeral storage.
- Very low-latency/high-throughput use cases.
- Data lost on stop, terminate, or host loss.
- Use only for cache, buffer, scratch, or replicated data.

Rule:

```text
Need durable data? EBS.
Can rebuild data? Instance store may fit.
```

### Network model

Instance network capability includes:

- Bandwidth.
- Packet rate.
- Number/behavior of flows.
- ENI capability.
- Enhanced networking support.

Exact objects:

- ENI: virtual network interface.
- Primary/secondary private IP.
- Public IPv4 or Elastic IP.
- Security groups attached to ENI.
- ENA: enhanced networking adapter for high performance.
- EFA: specialized low-latency HPC/ML communication where supported.

Pattern:

```text
Network metric near workload ceiling
  -> check instance network capability
  -> choose larger/different instance or scale out
```

Low `NetworkIn/Out` does not prove network healthy. Also inspect packet loss, latency, routing, and application behavior when relevant.

### Placement groups

| Type | Placement | Best fit | Main trade-off |
|---|---|---|---|
| Cluster | Instances close together in one AZ | Low latency/high throughput, tightly coupled workload | Correlated AZ/hardware-capacity risk |
| Spread | Instances on distinct hardware | Small number of critical instances | Limited scale |
| Partition | Groups separated into hardware partitions | Large distributed systems | Application must understand partitions |

Fast clues:

```text
Fast node-to-node traffic? Cluster.
Few critical instances isolated? Spread.
Large distributed fleet with rack-like partitions? Partition.
```

Cluster placement:

- One AZ.
- Best launched together with compatible types/capacity.
- Capacity error can occur later when adding instances.
- Not a multi-AZ availability solution.

Spread placement:

- Reduces shared-hardware failure risk.
- Does not replace multi-AZ design.

Partition placement:

- Instances in one partition do not share underlying hardware with another partition.
- Useful when software can place replicas across partitions.

### Configuration path

```text
Choose AMI architecture
  -> choose instance family/size
  -> choose subnet/AZ
  -> attach storage and ENIs
  -> choose placement group if needed
  -> launch through template/fleet
  -> verify health and limits
  -> alarm and optimize
```

Compatibility checks:

- AMI CPU architecture.
- Instance family/virtualization support.
- ENA/EFA driver support.
- EBS and network requirements.
- AZ capacity.
- Licensing/software constraints.

### Evidence path

```text
Application latency/error
  -> EC2 status checks
  -> CPU/agent metrics
  -> network metrics/path
  -> EBS volume + instance ceiling
  -> placement/AZ/capacity
  -> recent event/change
```

### Failure clues

| Symptom | First checks |
|---|---|
| Instance unreachable | Status checks, SG/routes, OS, scheduled event |
| High EBS latency after tuning volume | EC2 EBS ceiling, filesystem/application pattern |
| Network throughput capped | Instance bandwidth/PPS/flow limits, ENA, path |
| Data vanished after stop | Data was on instance store |
| Cluster placement launch fails | AZ capacity, compatible types, placement request |
| New architecture does not boot/run | AMI/application architecture compatibility |
| Public endpoint changed after stop/start | Auto public IP used instead of Elastic IP/DNS abstraction |
| Fleet returns old configuration | Launch template/AMI version not updated |

### Optimization choices

- Resize instance for sustained compute/memory/network/EBS need.
- Scale horizontally for variable/stateless load.
- Select family matching bottleneck.
- Select EBS settings plus EC2 capability together.
- Use instance store only for disposable/recoverable data.
- Use placement group only when workload requirement justifies constraint.
- Update launch template and replace/refresh fleet for repeatability.

### Exam traps

- Larger EBS volume cannot exceed EC2 EBS ceiling.
- Instance store is not durable across stop/host loss.
- Cluster placement group is not multi-AZ.
- Spread placement reduces hardware sharing; it does not guarantee application HA alone.
- Auto-assigned public IPv4 can change after stop/start.
- Reboot and stop/start have different effects.
- Wrong AMI architecture blocks instance-family migration.
- EC2 default metrics still do not show guest memory/filesystem.
- Low bandwidth use does not exclude latency, packet, DNS, or security-path failure.

### Do not memorize

- Every instance-family limit.
- Exact network bandwidth for every size.
- Every ENI quota.
- Placement-group numeric limits.
- OS repair commands.
- Console click paths.

### Ready when

Given an EC2 issue, you can:

1. Separate system failure from guest failure.
2. Separate EBS volume limit from instance limit.
3. Explain EBS versus instance-store persistence.
4. Select cluster, spread, or partition placement.
5. Choose reboot, stop/start, resize, or replace safely.

---

# Domain 2 - Reliability and Business Continuity

### Task 2.1 - Implement scalability and elasticity

## Skill 2.1.1 - Configure and manage scaling mechanisms in compute environments

**Official goal:** Configure compute to add/remove capacity as demand changes.

### What exam tests

- Primary: `CFG BEH OPT`
- Supporting: `EVD DIA PRC`
- Precision: `L3 - Property`
  - Exact scaling policy, capacity values, health, warmup, and concurrency type matter.

### Core model

```text
Demand signal
  -> scaling policy
  -> desired capacity changes
  -> resources launch/terminate
  -> health check validates capacity
```

Two directions:

```text
Scale out/in = add/remove resources.
Scale up/down = larger/smaller resource.
```

### EC2 Auto Scaling objects

- Launch template: AMI, instance type, network, storage, IAM, user data.
- Auto Scaling group: fleet definition.
- Minimum capacity: lower bound.
- Desired capacity: requested running count.
- Maximum capacity: upper bound.
- Subnets/AZs: placement and resilience.
- Scaling policy: when/how desired changes.
- Health check: EC2 and optional ELB health.
- Health-check grace period: startup time before health replacement.
- Instance warmup: time before new capacity fully affects scaling metrics.
- Cooldown: pause/reduce repeated scaling response where applicable.
- Termination policy: which instance leaves first.
- Lifecycle hook: pause launch/terminate for custom action.
- Instance refresh: replace fleet with new launch-template configuration.

Capacity rule:

```text
minimum <= desired <= maximum
```

### Scaling policies

| Policy | Best fit |
|---|---|
| Target tracking | Keep metric near target |
| Step scaling | Different capacity changes for different breach sizes |
| Simple scaling | One adjustment plus cooldown; older/basic pattern |
| Scheduled scaling | Known time-based demand |
| Predictive scaling | Recurring demand forecast |

Fast clues:

```text
Keep CPU near 50%? Target tracking.
Add 1/3/5 based on severity? Step scaling.
Every weekday at 08:00? Scheduled.
Recurring pattern forecast? Predictive.
```

### Target tracking

Examples:

- Average CPU utilization.
- ALB requests per target.
- Suitable custom utilization metric.

Behavior:

- Adds capacity when metric above target.
- Removes capacity when safely below target.
- AWS manages related alarm behavior.
- Do not manually edit managed alarms.

Good metric:

```text
Load rises -> metric rises.
Capacity rises -> metric falls.
```

### Step scaling

Example:

```text
CPU 60-70% -> add 1
CPU 70-85% -> add 2
CPU >85%   -> add 4
```

Needs:

- CloudWatch alarm.
- Breach ranges/steps.
- Adjustment type/value.
- Warmup considered.

### Health and replacement

```text
Instance launches
  -> startup/user data
  -> grace period
  -> EC2/ELB health check
  -> healthy capacity or replacement
```

If application needs long startup:

```text
Too-short grace period
  -> instance marked unhealthy
  -> replacement loop
```

ELB health is stronger application evidence than EC2 running state alone.

### Instance refresh

Use for:

- New AMI.
- New launch-template version.
- New instance configuration.

Flow:

```text
Set desired launch-template version
  -> start refresh
  -> replace batch
  -> wait for healthy/warm
  -> continue or rollback/stop
```

Know minimum healthy capacity and warmup/bake impact.

### ECS scaling

Two separate layers:

```text
ECS service scaling
  -> desired task count.

Capacity provider/EC2 scaling
  -> cluster instance capacity.
```

Trap:

```text
More desired tasks do not help
if cluster has nowhere to place them.
```

For Fargate, AWS supplies underlying hosts; service/task scaling still matters.

### EKS scaling

Two layers:

```text
Workload scaling
  -> more/fewer pods.

Node scaling
  -> more/fewer worker nodes.
```

More pods need schedulable node capacity.

Check:

- Pod resource requests/limits.
- Pending pods.
- Node capacity.
- Scaling controller/node-group state.
- Subnet IP and quotas.

### Lambda scaling

Exact concepts:

- Account concurrency: regional shared capacity limit.
- Reserved concurrency: reserves and caps concurrency for one function.
- Provisioned concurrency: pre-initialized environments to reduce cold starts.
- Throttles: invocation blocked by concurrency limit.
- Event-source batch/backlog: work waits for processing.

Fast clues:

```text
Protect capacity for function? Reserved concurrency.
Limit function from overwhelming DB? Reserved concurrency cap.
Reduce cold starts? Provisioned concurrency.
Function throttled? Check concurrency limits and downstream capacity.
```

### Evidence path

```text
Demand metric
  -> alarm/policy activity
  -> desired capacity
  -> launch/termination activity
  -> instance/task/pod/function health
  -> application latency/errors
```

For EC2 Auto Scaling inspect:

- Group activity history.
- Desired/min/max values.
- Policy/alarm state.
- Launch-template version.
- Instance lifecycle/health state.
- ELB target health.
- CloudTrail changes.

### Failure clues

| Symptom | First checks |
|---|---|
| No scale-out | Metric/alarm, policy, maximum reached, warmup/cooldown |
| Desired rises, no instance | AMI/type, IAM, quota/capacity, subnet IP, launch-template error |
| Instances replace repeatedly | Health check, grace period, startup/user data, application port |
| Scale-in never happens | Minimum/desired, scale-in protection, policy metric, warmup |
| Scaling oscillates | Sensitive threshold, poor metric, missing warmup/cooldown |
| ECS tasks pending | Cluster capacity, placement, resources, subnet IP |
| EKS pods pending | Requests, node capacity, node scaling, quotas/IPs |
| Lambda throttles | Reserved/account concurrency, event source, downstream limit |

### Reliability and cost

- Use multiple AZs for EC2 fleet resilience.
- Keep minimum capacity required for availability.
- Scale in slowly enough to avoid oscillation.
- Do not add capacity faster than downstream can handle.
- Predictive/scheduled capacity can reduce delayed scale-out.
- Provisioned concurrency reduces latency but adds standing cost.
- Excess minimum/desired capacity creates waste.

### Exam traps

- Desired capacity cannot exceed max or go below min.
- Scaling policy changes desired capacity; launch template defines new instances.
- Updating launch template does not replace running fleet without refresh/replacement.
- EC2 health can pass while application/ELB health fails.
- Too-short grace/warmup creates replacement or scaling loops.
- Scheduled scaling is time-based, not reactive.
- Predictive scaling needs recurring pattern; it is not instant response to surprise spike.
- ECS task scaling and EC2 capacity scaling are different.
- EKS pod scaling and node scaling are different.
- Provisioned concurrency reduces cold start; reserved concurrency controls capacity allocation/limit.
- More compute can overload database or queue consumer dependency.

### Do not memorize

- Every scaling API property.
- Exact service quotas.
- Every termination-policy option.
- Full Kubernetes autoscaler manifests.
- Console click paths.

### Ready when

Given a scaling problem, you can:

1. Choose target, step, scheduled, or predictive scaling.
2. Explain min/desired/max and warmup/health behavior.
3. Find why capacity did not launch or stay healthy.
4. Separate service/task/pod scaling from host/node scaling.
5. Separate reserved from provisioned Lambda concurrency.

---

## Skill 2.1.2 - Implement caching for dynamic scalability

**Official goal:** Use caching to reduce latency and remove load from backend resources.

### What exam tests

- Primary: `SEL CFG BEH OPT`
- Supporting: `DIA`
- Precision: `L2 - Object`
  - Know cache layer, key, TTL, engine, replicas/shards, and failure behavior.

### Core model

```text
Request
  -> cache hit: return fast
  -> cache miss: call backend, store result, return
```

Main benefit:

```text
Less backend work + lower latency.
```

Main risk:

```text
Stale or missing cache data.
```

### Pick the cache

| Need | Choose |
|---|---|
| Cache HTTP content near global users | CloudFront |
| Cache application data/sessions | ElastiCache |
| Cache DynamoDB reads | DAX |

Fast clues:

```text
Viewer near edge? CloudFront.
App needs shared in-memory cache? ElastiCache.
DynamoDB microsecond reads? DAX.
```

### CloudFront cache

```text
Viewer
  -> edge cache
  -> origin only on miss/expiry
```

Exact objects:

- Distribution.
- Origin.
- Cache behavior/path pattern.
- Cache policy.
- Cache key.
- TTL.
- Invalidation.
- Origin request policy.

Cache key can include:

- URL path.
- Query strings.
- Headers.
- Cookies.

Rule:

```text
More cache-key variants
  -> fewer hits
  -> more origin load.
```

Use only required headers/cookies/query strings in cache key.

### CloudFront behavior

- Cache static or cacheable dynamic HTTP responses.
- TTL controls freshness duration.
- Origin cache headers can influence TTL within policy limits.
- Invalidation removes selected cached objects early.
- Versioned object names avoid repeated invalidation for immutable files.
- Cache hit reduces origin requests and scaling need.

### ElastiCache engine choice

| Engine | Best fit |
|---|---|
| Valkey/Redis OSS | Replication, failover, persistence options, rich data structures, sessions, counters, pub/sub |
| Memcached | Simple distributed volatile key/value cache; easy horizontal distribution |

Fast choice:

```text
Need replication/failover/rich features? Valkey/Redis OSS.
Need simple disposable cache? Memcached.
```

### ElastiCache objects

- Cluster/replication group.
- Cache node.
- Node type.
- Shard/node group.
- Primary node.
- Read replica.
- Endpoint.
- Subnet group.
- Security group.
- Parameter group.
- Snapshot/backup where supported.

### Replicas versus shards

```text
Read replicas
  -> more read capacity + availability.

More shards
  -> more write/data capacity.
```

Valkey/Redis-style Multi-AZ automatic failover needs suitable replica topology.

Memcached nodes do not provide the same replication/failover model. Lost node means lost cached items.

### Cache patterns

**Cache-aside/lazy loading**

```text
Read cache
  -> miss
  -> read database
  -> write cache
  -> return
```

- Only requested data cached.
- First request is slower.
- Application manages miss and invalidation.

**Write-through**

```text
Write database
  -> update cache
```

- Cache stays warm/current.
- More write work.
- Failure ordering must be handled.

### TTL and eviction

- TTL: item expires after time.
- Eviction: cache removes item because of policy/memory pressure.
- Cache miss: item absent/expired/evicted.
- Hot key: one key receives heavy traffic.
- Cache stampede: many clients rebuild same expired item together.

Trade-off:

```text
Long TTL -> more hits, more stale risk.
Short TTL -> fresher, more backend load.
```

### DAX

```text
Application with DAX client
  -> DAX cluster
  -> DynamoDB
```

Use for:

- DynamoDB read-heavy workload.
- Microsecond cached reads.
- Repeated reads of same items.

Exact needs:

- DAX-aware client.
- DAX cluster and nodes.
- Subnet/security path.
- IAM permission.
- Application points to DAX endpoint.

Behavior:

- Eventually consistent reads can use cache.
- Strongly consistent reads pass through to DynamoDB and are not served from cache.
- Writes still reach DynamoDB; DAX does not remove DynamoDB write-capacity needs.

Not for:

- RDS queries.
- Generic HTTP caching.
- Fixing bad DynamoDB partition key.
- Eliminating write throttling.

### Metrics/evidence

**CloudFront**

- Cache hit ratio.
- Origin requests/latency.
- Viewer/origin status codes.
- Cache result type.

**ElastiCache**

- Cache hits/misses.
- Evictions.
- CPU/engine CPU.
- Free memory/memory use.
- Connections.
- Replication lag.
- Network throughput.

**DAX**

- Cache hits/misses.
- Request latency/errors.
- CPU/memory/network.
- DynamoDB consumed capacity/throttling behind DAX.

### Failure clues

| Symptom | First checks |
|---|---|
| CloudFront hit ratio low | Cache key, TTL, behavior, headers/cookies/query strings |
| Origin still overloaded | Uncacheable requests, low hit rate, short TTL, bypass behavior |
| ElastiCache misses high | TTL, key construction, workload reuse, eviction |
| Evictions high | Memory pressure, node size, TTL, item volume |
| One cache node hot | Hot key, shard distribution, client routing |
| Stale data | TTL/invalidation/write pattern |
| Cache outage breaks app | No cache-miss/fallback behavior or weak HA |
| DAX gives no benefit | App not using DAX client/endpoint, low reuse, strong reads |
| DynamoDB writes throttle | DAX is read cache; inspect write capacity/partitioning |

### Optimization choices

- Improve cache key reuse.
- Adjust TTL from freshness need.
- Remove unnecessary key dimensions.
- Increase ElastiCache node size for memory/CPU.
- Add replicas for reads/availability.
- Add shards for write/data scale.
- Protect backend from stampede with controlled refresh/locking pattern.
- Keep application fallback when cache unavailable where required.

### Exam traps

- Cache is normally not source of truth.
- CloudFront cache key and origin request policy are different.
- Invalidation fixes stale object now; versioning is better for repeated immutable releases.
- Read replicas and shards solve different ElastiCache limits.
- Memcached does not provide Redis-style replication/failover.
- DAX requires DAX-aware application client.
- DAX helps repeated DynamoDB reads, not writes or RDS.
- Strongly consistent DynamoDB reads bypass DAX cache.
- Longer TTL improves hits but increases stale-data risk.
- Cache failure can create sudden database load.

### Do not memorize

- Every engine command/data type.
- Every cache-node family.
- Exact eviction-policy catalog.
- Exact TTL values for generic workloads.
- Console click paths.

### Ready when

Given a caching scenario, you can:

1. Choose CloudFront, ElastiCache, or DAX.
2. Choose Valkey/Redis OSS or Memcached.
3. Explain TTL, hit rate, eviction, replica, and shard behavior.
4. Diagnose low hit rate, hot key, stale data, or failover issue.
5. Explain how cache changes backend scaling and failure risk.

---

## Skill 2.1.3 - Configure and manage scaling in AWS managed databases

**Official goal:** Configure databases to grow with read, write, storage, or connection demand.

### What exam tests

- Primary: `CFG BEH OPT`
- Supporting: `EVD DIA SEL`
- Precision: `L2 - Object`
  - Know the capacity mode, replica, endpoint, scaling limit, and bottleneck.

### Core model

First ask:

```text
What is full?
  Read capacity?
  Write capacity?
  Compute/memory?
  Storage/IOPS?
  Connections?
  One hot partition?
```

Then scale that layer.

### Fast selection

| Need | Main choice |
|---|---|
| More RDS/Aurora reads | Read replicas/Aurora readers |
| More RDS compute or memory | Larger DB instance class |
| More RDS storage space | Storage autoscaling/increase storage |
| Absorb connection bursts | RDS Proxy/pooling |
| Variable Aurora capacity | Aurora Serverless v2 |
| Unpredictable DynamoDB traffic | On-demand mode |
| Predictable DynamoDB traffic | Provisioned + auto scaling |
| DynamoDB repeated reads | DAX |
| DynamoDB hot partition | Better partition-key distribution |

### RDS scaling

```text
Writer workload
  -> primary DB instance

Read workload
  -> read replicas
```

Main choices:

- Change DB instance class: vertical compute/memory scaling.
- Add read replicas: horizontal read scaling.
- Increase allocated storage/IOPS/throughput: storage scaling.
- Enable storage autoscaling: automatic storage growth.
- Use RDS Proxy: connection pooling, not database compute scaling.

Read replica behavior:

- Replication is asynchronous.
- Replica can lag.
- Application must send reads to replica endpoint.
- Promotion creates an independent primary.
- Read replica is not the same as Multi-AZ standby.

### RDS storage autoscaling

Exact properties:

- Allocated storage.
- Maximum storage threshold.
- Free storage.
- Storage type.
- Provisioned IOPS/throughput where supported.

Behavior:

```text
Free storage stays low
  -> RDS grows storage
  -> never automatically shrinks it.
```

Rules:

- Set maximum above expected growth.
- Scaling is not instant.
- Engine/storage modification limits still apply.
- Storage space, IOPS, and throughput are different limits.
- Autoscaling space does not fix slow SQL or a saturated DB instance.

### Aurora scaling

```text
Writes -> cluster/writer endpoint -> writer
Reads  -> reader endpoint -> Aurora replicas
```

Objects:

- DB cluster.
- Writer instance.
- Aurora Replica/reader.
- Cluster/writer endpoint.
- Reader endpoint.
- Instance endpoint.
- Serverless v2 minimum/maximum ACUs.

Behavior:

- Reader endpoint distributes new read connections across readers.
- It does not split queries already using one connection.
- Add readers for read scale and failover candidates.
- Writer scaling is usually instance/serverless capacity, not more writers.
- Replica lag still matters for read-after-write needs.

### Aurora Serverless v2

```text
Demand changes
  -> capacity moves within min/max ACUs.
```

- ACU = Aurora Capacity Unit.
- Minimum controls lowest running capacity.
- Maximum limits scale-up.
- Too-low maximum can cause saturation.
- Higher minimum gives more ready capacity but costs more.
- Auto-pause is available only with supported engine/configuration and minimum settings.
- Applications still need sensible connection and retry behavior.

### DynamoDB capacity modes

| Mode | Best fit | Operator controls |
|---|---|---|
| On-demand | New, spiky, unpredictable traffic | Pay per request; optional throughput limits |
| Provisioned | Predictable traffic/capacity control | Read/write capacity; auto-scaling min, max, target |

Fast choice:

```text
Traffic hard to predict? On-demand.
Traffic predictable and controlled? Provisioned + auto scaling.
```

Changing mode does not repair a poor partition key.

### DynamoDB provisioned auto scaling

```text
Utilization above target
  -> increase capacity within max.

Utilization below target
  -> decrease capacity within min.
```

Exact objects/properties:

- Table read capacity.
- Table write capacity.
- GSI read/write capacity.
- Minimum capacity.
- Maximum capacity.
- Target utilization.
- Application Auto Scaling scalable target/policy.
- CloudWatch alarms created for target tracking.

Important:

- Read and write scale separately.
- Each GSI can need separate scaling.
- Auto scaling reacts; a sudden spike can throttle before scale-out.
- Maximum capacity can block needed scale-out.
- Minimum capacity controls ready baseline.

### DynamoDB hot partitions

```text
Good total table capacity
  + one overloaded partition key
  -> throttling still happens.
```

Clues:

- A few keys dominate traffic.
- Throttling occurs while table-wide utilization looks acceptable.
- One GSI has the problem, not the base table.

Fix direction:

- Spread traffic across high-cardinality partition keys.
- Remove monotonic or single-key concentration where design allows.
- Inspect the affected table/index and read/write path.
- Do not assume more total capacity alone fixes uneven distribution.

### DAX and ElastiCache boundary

- DAX caches DynamoDB reads.
- DAX does not increase DynamoDB write capacity.
- ElastiCache replicas add cache read capacity/availability.
- ElastiCache shards add cache write/data capacity.
- Neither cache fixes the source database's write partitioning.

### Metrics/evidence

**RDS/Aurora**

- CPU utilization.
- Freeable memory.
- Database connections.
- Read/write latency and IOPS.
- Disk queue depth.
- Free storage space.
- Replica lag.
- Aurora Serverless capacity.

**DynamoDB**

- Consumed versus provisioned read capacity.
- Consumed versus provisioned write capacity.
- Read/write throttled requests/events.
- Successful request latency and errors.
- Table versus GSI evidence.
- Contributor Insights for frequently accessed/throttled keys when enabled.

### Failure clues

| Symptom | First checks |
|---|---|
| RDS CPU high | Instance class, DB load, SQL/waits, read offload |
| RDS reads slow | Read replicas, replica routing, storage/SQL evidence |
| Replica added but primary unchanged | Application still reads primary or workload is write-heavy |
| Replica returns old data | Replica lag/eventual replication |
| Storage still fills | Autoscaling enabled, maximum threshold, modification state |
| Aurora readers unused | Application using writer endpoint |
| Serverless does not grow enough | Maximum ACUs or another bottleneck |
| DynamoDB provisioned table throttles | Capacity, max setting, scaling delay, hot key, GSI |
| DynamoDB utilization low but throttles | Uneven partition/key or index traffic |
| DAX added but writes throttle | DAX is a read cache |

### Change path

```text
Identify limiting layer
  -> choose scaling object
  -> set safe min/max/target
  -> route application correctly
  -> watch scale event and metrics
  -> verify latency, throttling, lag, and cost.
```

### Exam traps

- Multi-AZ is availability, not normal read scaling.
- Read replica scales reads, not writes.
- Creating a replica does nothing unless the application uses it.
- RDS Proxy manages connections; it is not a cache or read replica.
- Storage autoscaling grows only; it does not shrink.
- Aurora reader endpoint handles readers, not writes.
- Aurora Serverless v2 stays inside configured ACU bounds.
- DynamoDB auto scaling is reactive, not instant.
- Table capacity and GSI capacity can fail separately.
- More table capacity may not solve a hot partition.
- DAX improves repeated reads, not write throughput.

### Do not memorize

- Every DB instance class.
- Exact storage-autoscaling trigger timing.
- Exact ACU-to-resource conversion.
- Every DynamoDB quota.
- Engine-specific replication commands.
- Console click paths.

### Ready when

Given a database scaling scenario, you can:

1. Name the limiting layer.
2. Choose vertical scale, replica, storage autoscaling, Serverless, or capacity mode.
3. Route RDS/Aurora reads to the correct endpoint.
4. Configure DynamoDB table/GSI min, max, and target.
5. Separate insufficient capacity from hot-key throttling.

---

## Skill 2.2.1 - Configure and troubleshoot ELB and Route 53 health checks

**Official goal:** Configure traffic distribution and find why an endpoint or target is unhealthy.

### What exam tests

- Primary: `SEL CFG BEH DIA REM`
- Supporting: `EVD`
- Precision: `L3 - Property`
  - Exact load balancer, listener, rule, target group, check, state, and DNS setting matter.

### Core model

```text
Client
  -> Route 53 chooses endpoint
  -> load balancer listener/rule
  -> target group
  -> healthy target
```

Three different health views:

| Check | Controls |
|---|---|
| Route 53 health | Which DNS answer is returned |
| ELB target health | Which target receives load-balancer traffic |
| EC2 status check | Instance/platform health |

Do not mix them.

### Pick the load balancer

| Need | Choose |
|---|---|
| HTTP/HTTPS content routing | ALB |
| TCP/UDP/TLS, extreme performance, static IP | NLB |
| Insert virtual network appliances | GWLB |
| Existing legacy load balancer | CLB; recognize, rarely choose new |

### ALB

Layer 7:

- HTTP/HTTPS.
- Host-based routing.
- Path-based routing.
- Header/query/method/source-IP conditions.
- Redirect or fixed response.
- WebSockets.
- Instance, IP, or Lambda targets where supported.

Flow:

```text
Listener
  -> ordered listener rules
  -> action
  -> target group
```

Use when the question understands the HTTP request.

### NLB

Layer 4:

- TCP, UDP, TCP_UDP, or TLS listeners.
- Very high throughput/low latency.
- Static IP per enabled AZ.
- Elastic IP option for internet-facing use where supported.
- Source-IP preservation in relevant target modes.

Use when the question needs connection/protocol handling, not HTTP content rules.

### GWLB

```text
Traffic
  -> GWLB
  -> firewall/inspection appliance fleet
  -> destination
```

- Transparently inserts network appliances.
- Uses GWLB endpoints in routed designs.
- Balances appliance targets.
- Not an application web load balancer.

### ELB objects

- Load balancer.
- Enabled subnet/AZ.
- Security group where applicable.
- Listener: protocol + port.
- Listener rule: priority + condition + action.
- Target group: target type + protocol + port.
- Registered target.
- Health check.
- Deregistration delay/draining.
- Cross-zone load balancing setting/behavior.

### Target-health properties

- Health-check protocol.
- Health-check port.
- Path for HTTP/HTTPS.
- Success matcher/status code.
- Interval.
- Timeout.
- Healthy threshold.
- Unhealthy threshold.

Core rule:

```text
Target becomes healthy/unhealthy
only after threshold results.
```

The target must answer the health check from the load balancer path.

### Target states

| State | Meaning |
|---|---|
| `initial` | Registration/checks starting |
| `healthy` | Passing checks; can receive traffic |
| `unhealthy` | Failed checks |
| `unused` | Not usable by this load balancer/AZ/configuration |
| `draining` | Deregistering; existing work allowed during delay |
| `unavailable` | Health checks unavailable/disabled in relevant case |

Reason code/message gives the next clue.

### Diagnose an unhealthy target

Check in this order:

```text
1. Registered in correct target group?
2. Target/AZ enabled?
3. Correct health protocol, port, path, matcher?
4. Application listening and returning success?
5. Security group/NACL/routing allows health path?
6. Target overloaded or timing out?
```

Common causes:

- Wrong health-check path.
- Expected `200`, application returns redirect/auth/error.
- App listens on another port/interface.
- Target security group blocks load balancer.
- NACL blocks request or return ephemeral traffic.
- Target in disabled AZ/subnet.
- Listener and target-group protocol/port mismatch.
- Timeout too short for slow endpoint.
- Target is still starting.

Use a cheap health endpoint. Do not require user authentication.

### Traffic and health are separate

A healthy target can still fail user requests because:

- Health path tests too little.
- Listener rule sends users to another target group.
- Host/path condition does not match.
- TLS certificate/SNI issue occurs before forwarding.
- Application fails only on real requests.

Trace both:

```text
Listener/rule path + target health path.
```

### Deregistration and cross-zone

**Deregistration delay**

- Target enters `draining`.
- New traffic stops.
- Existing requests/connections get time to finish.

**Cross-zone load balancing**

- Determines whether a load-balancer node can send traffic to targets in other enabled AZs.
- Behavior/defaults differ by load-balancer type.
- It does not create targets in an empty AZ.

### Route 53 health-check types

| Type | Use |
|---|---|
| Endpoint | Public IP/domain endpoint check |
| Calculated | Combine child health checks |
| CloudWatch alarm | Convert monitored metric/alarm into DNS health |

Endpoint properties can include:

- IP address or domain name.
- Protocol.
- Port.
- Path.
- Request interval.
- Failure threshold.
- Optional string matching/inversion settings.

### Route 53 DNS failover

```text
Route 53 sees endpoint unhealthy
  -> stops returning unhealthy record when policy allows
  -> recursive resolver keeps old answer until TTL expires.
```

Required pieces:

- Suitable routing policy.
- Primary/secondary or other policy records.
- Health check attached to the correct record, or alias target health evaluation.
- Healthy alternate endpoint.
- Sensible TTL.

Route 53 changes DNS answers. It does not move existing connections.

### Alias target health

For an alias to an AWS resource such as an ELB:

- `Evaluate Target Health` can inherit target-resource health.
- This is different from attaching a separate Route 53 endpoint check.
- The alias target and record configuration must be correct.

### Private endpoint problem

Public Route 53 health checkers cannot directly reach private VPC/on-premises endpoints.

Pattern:

```text
Internal monitoring
  -> CloudWatch metric/alarm
  -> Route 53 alarm-based health check
  -> DNS decision
```

Do not make a private service public only to health-check it.

### Evidence

**ELB**

- Target health state and reason.
- Healthy/unhealthy host count.
- Target response time.
- HTTP/TCP error/reset metrics.
- Load-balancer access logs where supported/enabled.
- Application logs.
- VPC Flow Logs/network reachability evidence.

**Route 53**

- Health-check status and failure reasons/regions.
- CloudWatch health-check/alarm metrics.
- Record, policy, health-check association.
- `Evaluate Target Health` setting.
- DNS answer and TTL from a resolver query.

### Failure clues

| Symptom | First checks |
|---|---|
| All ELB targets unhealthy | Shared path/port/matcher, SG/NACL, application state |
| One target unhealthy | Target app, registration, local network, overload |
| Target healthy but gets no traffic | Listener rule, priority, target-group action, AZ/cross-zone |
| Target stays `initial` | Registration, checks, startup time, enabled AZ |
| Target stays `draining` | Deregistration delay/open connections |
| Route 53 still returns failed endpoint | Record association, policy, health state, TTL/cache |
| Private endpoint check fails | Public checkers cannot reach it; use alarm pattern |
| DNS changed but users still fail | Resolver cache, existing connection, alternate endpoint health |
| Failover record never used | Secondary misconfigured/unhealthy or primary not associated correctly |

### Remediation pattern

```text
Read health reason
  -> test exact protocol/port/path
  -> verify network path
  -> verify application response
  -> correct setting or application
  -> wait for thresholds/TTL
  -> verify traffic.
```

### Exam traps

- ALB understands HTTP content; NLB normally does not.
- NLB static IP is not a reason to choose ALB.
- GWLB is for appliances, not ordinary web targets.
- Listener health and target health are different questions.
- Correct user URL does not prove health-check path is correct.
- Security groups are stateful; NACLs are stateless.
- Healthy target does not prove every application dependency works.
- Route 53 health affects DNS answers, not ELB target membership.
- DNS failover is delayed by TTL and resolver caching.
- Route 53 public health checkers cannot directly test private endpoints.
- A backup endpoint must itself be healthy and configured.

### Do not memorize

- Every target-health reason code.
- Exact default interval/threshold for every load-balancer type.
- Every routing-policy edge case.
- Health-checker IP ranges.
- Console click paths.

### Ready when

Given a traffic-health scenario, you can:

1. Choose ALB, NLB, or GWLB.
2. Trace listener -> rule -> target group -> target.
3. Configure exact health-check properties.
4. Diagnose unhealthy targets from reason and network/application evidence.
5. Configure Route 53 failover and explain TTL delay.
6. Separate public endpoint checks from private alarm-based health.

---

## Skill 2.2.2 - Configure fault-tolerant systems

**Official goal:** Keep a workload working when a resource or Availability Zone fails.

### What exam tests

- Primary: `SEL CFG BEH`
- Supporting: `REM OPT`
- Precision: `L2 - Object`
  - Know the failure boundary, redundant object, failover method, and hidden dependency.

### Core model

```text
Duplicate every critical path
  -> detect failure
  -> stop using failed part
  -> keep enough healthy capacity
  -> recover redundancy.
```

One Multi-AZ component does not make the whole application Multi-AZ.

### Failure boundaries

| Failure | Design response |
|---|---|
| One process/instance | Multiple targets + health replacement |
| One AZ | Resources and dependencies in multiple AZs |
| One Region | Prepared second Region + replicated/restorable data + traffic control |

First question:

```text
What can fail together?
```

### Multi-AZ application pattern

```text
Route 53
  -> load balancer in multiple AZs
  -> Auto Scaling targets in multiple AZs
  -> Multi-AZ data/service layer
```

Needs:

- At least two enabled AZs.
- Healthy targets in more than one AZ.
- Enough remaining capacity after one AZ fails.
- Application state outside replaceable instances.
- Each AZ has working network and dependency paths.
- Health checks remove failed targets.

### Compute exact objects

- Auto Scaling group.
- Multiple subnet/AZ selections.
- Minimum, desired, and maximum capacity.
- Load balancer target groups.
- Health-check grace/warmup.
- Replacement policy/process.

Trap:

```text
ASG uses three AZs but desired capacity = 1
  -> still only one running instance.
```

Multi-AZ placement is not enough; capacity must survive failure.

### Hidden network dependencies

Check:

- Public/private subnets in each AZ.
- Route table for each subnet.
- NAT gateway path for private outbound traffic.
- Load-balancer subnet/AZ enablement.
- VPC endpoint or other private service path.
- Security group and NACL path.
- DNS and health-check behavior.

Common resilient pattern:

```text
Private subnet in AZ-A -> NAT gateway in AZ-A
Private subnet in AZ-B -> NAT gateway in AZ-B
```

One NAT gateway can become the application’s single-AZ dependency.

### Database availability choices

| Need | Choice | Behavior |
|---|---|---|
| RDS automatic AZ failover | Multi-AZ deployment | Synchronous standby/failover |
| RDS read scale | Read replica | Asynchronous; can lag |
| Aurora compute failover | Writer + Aurora Replica in another AZ | Replica promoted on failover |
| DynamoDB Regional HA | DynamoDB table | Service distributes data across AZs |
| DynamoDB multi-Region | Global table | Multi-Region replicas |

RDS rule:

```text
Multi-AZ standby = availability.
Read replica = read scaling.
```

Failover can change the underlying database host. Applications should use the service endpoint, reconnect, and retry safely.

### Aurora availability

- Cluster storage spans multiple AZs.
- Compute still needs more than one DB instance for fast instance/AZ failover.
- Cluster/writer endpoint follows the writer.
- Reader endpoint serves readers.
- Replica promotion tiers influence failover preference.

Storage resilience alone does not create a second healthy database process.

### Storage failure boundaries

| Service/object | Availability fact |
|---|---|
| EBS volume | Lives in one AZ; attach within that AZ |
| EBS snapshot | Durable recovery copy; not a live attached standby |
| EFS Standard | Regional, multi-AZ storage; use reachable mount targets |
| EFS One Zone | Lower cost; single-AZ storage trade-off |
| S3 | Regional service designed across multiple AZs |

Backup improves recovery. It does not keep a live request path running.

### Decouple with SQS

```text
Producer -> SQS queue -> consumer fleet
```

Benefit:

- Producer and consumer fail independently.
- Queue absorbs traffic bursts.
- Consumers can scale/recover later.

Exact reliability properties:

- Visibility timeout.
- Message retention.
- Receive count.
- Dead-letter queue.
- Redrive policy and `maxReceiveCount`.
- Long polling.

Processing rule:

```text
Receive
  -> process successfully
  -> delete message.
```

If visibility expires first, message can appear again. Consumer must be idempotent.

### Choose the integration service

| Need | Choose |
|---|---|
| Buffer work for consumers | SQS |
| Fan one message to subscribers | SNS |
| Route matching events | EventBridge |
| Run stateful steps with retry/catch | Step Functions |

These services reduce direct dependency between components. They do not fix non-idempotent processing automatically.

### Failure controls

- Timeout: stop waiting forever.
- Retry: try a transient failure again.
- Exponential backoff: increase wait between attempts.
- Jitter: spread retry timing.
- Idempotency: repeated request has one intended effect.
- DLQ: isolate repeatedly failing work.
- Circuit-breaker pattern: stop hammering a failing dependency.

Bad pattern:

```text
Many clients retry immediately
  -> dependency receives more load
  -> outage grows.
```

### Amazon Application Recovery Controller

| ARC capability | Use |
|---|---|
| Zonal shift | Temporarily move supported resource traffic away from one impaired AZ |
| Zonal autoshift | AWS automatically shifts supported traffic during an AZ impairment |
| Routing control | Operator switches traffic between prepared replicas/endpoints |
| Safety rule | Blocks unsafe routing-control combinations |
| Region switch | Orchestrates planned/unplanned multi-Region traffic recovery |

Routing-control objects:

- Cluster.
- Control panel.
- Routing control.
- Safety rule.
- Route 53 health-check integration.

Legacy readiness checks recognize resource readiness, but are not the recovery mechanism to emphasize for new designs.

ARC rule:

```text
ARC controls prepared traffic paths.
It does not create infrastructure or replicate data.
```

### Zonal shift boundary

Use zonal shift when:

- A supported resource spans AZs.
- Healthy capacity exists elsewhere.
- You need to stop sending traffic to one AZ.

It cannot help if:

- All capacity is in the impaired AZ.
- A database/data dependency has no alternate.
- The resource does not support zonal shift.
- Remaining capacity is too small.

### Evidence and validation

Check:

- Healthy capacity by AZ.
- Auto Scaling activity/replacement events.
- ELB healthy/unhealthy host counts.
- Database failover events and replica health.
- Queue age, depth, receive count, and DLQ growth.
- Route 53/ARC traffic state.
- Application errors, latency, and dependency timeouts.

Test:

```text
Remove one failure domain
  -> observe detection
  -> confirm traffic moves
  -> confirm capacity/data remain valid
  -> restore redundancy.
```

### Failure clues

| Symptom | Likely gap |
|---|---|
| Multi-AZ app fails with one AZ | Hidden single-AZ dependency or too little remaining capacity |
| ELB has no healthy targets in one AZ | No targets, failed health path, or disabled AZ |
| Private instances lose outbound access | Single NAT path/AZ dependency |
| RDS failover works but app stays down | Cached connection/DNS, no retry, wrong endpoint |
| Aurora storage healthy but DB unavailable | No healthy/promotable DB instance |
| Queue backlog grows | Consumers failed, too slow, or cannot scale |
| Same message changes data twice | Visibility/retry plus non-idempotent consumer |
| Poison message loops forever | Missing DLQ/redrive limit |
| ARC traffic shift fails | Alternate not prepared, routing control/health record wrong |

### Design check

For every tier ask:

```text
1. Is there another healthy copy?
2. Is it in another failure domain?
3. Can traffic find it?
4. Is state/data available there?
5. Is remaining capacity enough?
6. Has failover been tested?
```

### Exam traps

- Multi-AZ is not multi-Region disaster recovery.
- Multi-AZ is not a backup.
- A read replica is not the same as an RDS Multi-AZ standby.
- Aurora multi-AZ storage does not replace multiple DB instances.
- Multiple AZ subnets do not guarantee multiple running instances.
- Cross-zone balancing does not create missing capacity.
- One NAT gateway can remain a single-AZ dependency.
- EBS volume is AZ-scoped.
- SQS standard delivery can repeat; consumers need idempotency.
- Retry without backoff can amplify failure.
- ARC shifts traffic only to infrastructure that already exists.

### Do not memorize

- Exact failover times.
- Every ARC API/console screen.
- Every service availability SLA.
- Engine-specific replication internals.
- One fixed timeout/retry count for all workloads.

### Ready when

Given a resilience scenario, you can:

1. Name the failure boundary and single point.
2. Build enough compute/network/data capacity across AZs.
3. Separate Multi-AZ availability from read scaling and backup.
4. Choose SQS, SNS, EventBridge, or Step Functions for decoupling.
5. Configure safe timeout, retry, idempotency, and DLQ behavior.
6. Explain when ARC zonal shift or routing control helps.

---

## Skill 2.3.1 - Automate snapshots and backups

**Official goal:** Automatically protect EC2, EBS, RDS, S3, DynamoDB, and other supported resources.

### What exam tests

- Primary: `CFG PRC GOV`
- Supporting: `SEL EVD`
- Precision: `L2 - Object`
  - Know plan, rule, assignment, vault, recovery point, copy, lifecycle, job, and restore test.

### Core model

```text
Resource assignment
  -> backup plan/rule
  -> backup job
  -> recovery point in vault
  -> copy/lifecycle
  -> restore test.
```

Rule:

```text
Successful backup job != proven recovery.
```

### AWS Backup object tree

```text
Backup plan
  -> backup rule
       -> schedule/window
       -> destination vault
       -> lifecycle
       -> copy action
  -> resource assignment

Backup job
  -> recovery point
```

### Backup plan

A plan contains one or more rules.

Rule properties:

- Schedule.
- Start window.
- Completion window.
- Destination backup vault.
- Lifecycle: move to cold storage/delete where supported.
- Copy action: another Region/account/vault.
- Recovery-point tags.
- Continuous backup/PITR option where supported.

Do not mix:

```text
Schedule = when job starts.
Window   = allowed start/finish time.
Lifecycle = how long recovery point lives.
```

### Resource assignment

Select resources by:

- ARN.
- Resource type.
- Tags/conditions.

Also needs:

- Backup service role.
- Correct Region/account.
- Service/resource enabled and supported.
- Resource and KMS permissions.

Tag selection is dynamic:

```text
New resource gets matching tag
  -> plan can protect it automatically.
```

Wrong/missing tag means no backup.

### Backup vault

Vault holds recovery points.

Objects/settings:

- Vault name.
- Encryption key.
- Vault access policy.
- Recovery points.
- Notifications.
- Vault Lock.

Vault is storage/control boundary. It is not the schedule.

### Vault Lock

Use for retention protection and write-once-read-many controls.

- Governance mode: controlled administrative flexibility.
- Compliance mode: lock becomes immutable after its grace period.
- Minimum/maximum retention can be enforced.
- Prevents early recovery-point deletion according to policy.

Plan retention must agree with Vault Lock limits.

Trap:

```text
Vault Lock blocks deletion
  -> “Access denied” may be correct protection, not broken IAM.
```

### Recovery point and jobs

**Recovery point**

- Restorable backup object.
- Has resource type, creation time, status, vault, encryption, and lifecycle.

**Job types**

- Backup job.
- Copy job.
- Restore job.
- Restore-testing job.

Key states:

- Created/pending/running.
- Completed.
- Failed/aborted/expired.
- Partial where applicable.

Read the status message before changing policy.

### Periodic versus continuous

| Need | Choice |
|---|---|
| Recovery only at scheduled points | Periodic snapshot backup |
| Fine-grained point-in-time recovery | Continuous backup/PITR where supported |

Periodic example:

```text
Daily backup -> up to about one schedule interval of data loss.
```

Continuous backup records changes for a recovery window. Service support differs.

### Copy protection

Copy actions can provide:

- Cross-Region recovery.
- Cross-account isolation.
- Different vault/KMS/retention controls.

Copy needs:

- Destination vault.
- Destination vault policy.
- Source and destination KMS access.
- Backup role/service permission.
- Organization/account permission where used.
- Supported resource/copy path.

Copy is separate from creating the source recovery point.

### Native backup choices

| Resource | Native protection |
|---|---|
| EC2 | AMI + underlying EBS snapshots |
| EBS | EBS snapshots/lifecycle policies |
| RDS/Aurora | Automated backups, PITR, manual snapshots |
| DynamoDB | On-demand backup and PITR |
| S3 | Versioning, replication, Object Lock; AWS Backup support |

Use AWS Backup when central policy, assignment, vault, reporting, or cross-account control is the clue.

Use a native mechanism when the question asks for that service’s specific backup feature.

### EBS and EC2 consistency

**EBS snapshot**

- Incremental after the first snapshot.
- Captures block-volume state.
- Restores by creating a volume.

**EC2 AMI backup**

- Captures launch image metadata.
- Includes snapshots for mapped EBS volumes.

Consistency:

```text
Crash-consistent
  -> storage captured like sudden power loss.

Application-consistent
  -> application flush/freeze/quiesce before capture.
```

Multiple related volumes may need coordinated capture.

### RDS/Aurora protection

- Automated backups support PITR within retention.
- Manual snapshots remain until explicitly deleted, subject to policy.
- Snapshot copy can support Region/account recovery.
- Encryption/KMS permissions follow copy and restore needs.
- Snapshot/backup does not preserve every surrounding application dependency.

Multi-AZ is availability. Backup is recovery from deletion, corruption, or wider failure.

### DynamoDB protection

- On-demand backup: full backup at a chosen point.
- PITR: continuous recovery within its supported window.
- Restore creates a new table.
- Table data backup does not automatically recreate every surrounding application dependency.

DAX is cache, not backup.

### S3 protection boundary

- Versioning protects object versions.
- Replication copies objects to another bucket.
- Object Lock protects versions from deletion/change under retention.
- AWS Backup can apply centralized supported backup policy.

These are related but not identical controls.

### IAM and KMS path

```text
Backup permission
  + source-resource permission
  + source KMS permission
  + vault policy
  + destination KMS/policy for copy
  = job can succeed.
```

Check:

- AWS Backup service role/trust.
- Resource policy where relevant.
- Vault access policy.
- KMS key policy and grants.
- Key state and Region/account.
- Cross-account destination permission.

Resource access and KMS access are separate.

### Evidence

- Backup job status/message.
- Copy job status/message.
- Recovery point exists in expected vault.
- Correct creation time, resource ARN, retention, and encryption.
- EventBridge/SNS notification where configured.
- AWS Backup Audit Manager control/report.
- Restore-test result.
- CloudTrail for configuration/deletion changes.

### Restore testing

```text
Restore testing plan
  -> select recovery point
  -> create temporary restored resource
  -> run validation
  -> record result
  -> clean up.
```

Verify:

- Resource restores.
- Data is readable/correct.
- Encryption and permissions work.
- Network and application can connect.
- Restore completes within RTO.
- Cleanup does not delete the protected source.

Backup job success proves capture, not usable application recovery.

### Failure clues

| Symptom | First checks |
|---|---|
| Resource never backed up | Assignment ARN/tag/type, Region, service opt-in/support |
| Job never starts | Schedule, start window, plan assignment, role |
| Job expires | Start window/capacity/service issue |
| Backup fails | Job message, role, resource state, KMS access |
| Copy fails | Destination vault policy, KMS keys, account/Region support |
| Recovery point deleted too soon | Rule lifecycle/retention and correct plan |
| Recovery point cannot be deleted | Vault Lock/retention/legal protection |
| Restore cannot decrypt | Destination role/key policy/grant/key state |
| Restore works but app fails | Missing network, secrets, DNS, parameters, dependencies |
| Compliance report shows gaps | Resource assignment, plan coverage, retention, job failures |

### Operational path

```text
Define RPO/retention
  -> choose periodic or continuous
  -> create vault/policy/key
  -> create rule and assignment
  -> verify first backup/copy
  -> alarm/report on failures
  -> test restore
  -> measure RTO.
```

### Exam traps

- A backup plan without resource assignment protects nothing.
- A vault stores recovery points; it does not schedule jobs.
- Lifecycle transition is not a cross-Region/account copy.
- Multi-AZ is not backup.
- S3 versioning is not the same as an AWS Backup recovery point.
- Snapshot availability does not prove application consistency.
- Successful source backup does not prove copy succeeded.
- Cross-account copy needs destination policy and KMS access.
- Vault Lock can intentionally block deletion.
- Backup success does not prove restore time or application function.

### Do not memorize

- Every supported resource type.
- Exact cold-storage minimum for every service.
- Exact default backup windows.
- Every job-state enum.
- Console click paths.

### Ready when

Given a backup scenario, you can:

1. Build plan -> rule -> assignment -> vault.
2. Choose periodic, PITR, native, or centralized protection.
3. Configure retention, lifecycle, copy, KMS, and Vault Lock.
4. Diagnose missing, failed, expired, or undeletable backups.
5. Prove recovery with restore testing, not job success alone.

---

## Skill 2.3.2 - Restore databases to meet RTO, RPO, and cost requirements

**Official goal:** Choose and run the database restore method that meets allowed data loss, downtime, and cost.

### What exam tests

- Primary: `PRC BEH SEL OPT`
- Supporting: `CFG GOV`
- Precision: `L3 - Property`
  - Know restore point/time, recovery window, new resource, endpoint, KMS key, network, and cutover.

### Core terms

```text
RPO = how much data can be lost.
RTO = how long service can be unavailable.
```

Example:

```text
RPO 15 minutes -> lose no more than 15 minutes of data.
RTO 1 hour     -> service working again within 1 hour.
```

Lower RPO/RTO usually means more automation, replication, ready capacity, and cost.

### Restore-choice model

| Requirement | Likely choice |
|---|---|
| Return to exact saved snapshot | Snapshot restore |
| Return to time just before corruption/deletion | PITR |
| Prove backup is usable | Restore test |
| Near-zero outage | HA/replication design, not ordinary restore alone |

Rule:

```text
Restore usually creates a new database/table.
Then application must cut over.
```

### RDS/Aurora restore choices

| Method | Recovery point | Needs |
|---|---|---|
| Snapshot restore | Snapshot creation time | Available manual/automated snapshot |
| Point-in-time restore | Chosen time or latest restorable time | Automated backups/logs within retention |
| AWS Backup restore | Selected recovery point | Vault recovery point + restore permission/metadata |

All normally create a new DB instance or cluster. They do not rewind the source in place.

### RDS point-in-time restore

```text
Full backup
  + transaction logs
  -> new DB at selected time.
```

Exact time choices:

- Latest restorable time.
- Specific date/time inside retention window.

For corruption:

```text
Choose time just before bad change.
```

Important:

- Latest restorable time can be behind current time.
- PITR requires automated backup retention.
- Time must be inside the available recovery window.
- Restore time depends on database size, logs, provisioning, and warm-up.

### RDS snapshot restore

```text
Selected snapshot
  -> new DB instance/cluster
  -> new endpoint.
```

Use when:

- Required restore point matches snapshot.
- PITR is unavailable.
- Restoring a copied cross-Region/account snapshot.
- Creating a test/clone environment from a known backup.

Snapshot age limits achievable RPO.

### Restored RDS/Aurora properties

Choose or verify:

- New DB identifier.
- DB instance class/capacity.
- Storage type, size, IOPS, and throughput.
- VPC and DB subnet group.
- Security groups.
- Availability/Multi-AZ settings.
- Parameter group.
- Option group where applicable.
- Port/public accessibility.
- KMS key/encryption access.
- Backup/maintenance settings.
- Tags and monitoring.
- New endpoint.

Do not assume every surrounding setting is restored exactly as needed.

### Aurora-specific restore

- Restore creates a new cluster.
- Ensure the cluster has healthy DB instance capacity.
- Writer/reader endpoints differ from the old cluster.
- Verify parameter groups, security, readers, scaling, and failover setup.
- Application must use the restored cluster endpoint.

A restored cluster with no usable compute path does not meet RTO.

### DynamoDB restore choices

| Method | Recovery point |
|---|---|
| On-demand backup restore | Time backup was created |
| PITR | Any second in the supported recovery window, up to 35 days |
| AWS Backup restore | Selected vault recovery point |

Core behavior:

```text
Backup/PITR
  -> new DynamoDB table.
```

The destination table needs a new name.

### Restored DynamoDB checks

Verify/reconfigure as required:

- Table name and Region/account.
- Partition/sort key schema.
- Local/global secondary indexes.
- Capacity mode and auto scaling.
- Encryption/KMS key.
- Tags.
- TTL.
- Streams and event-source mappings.
- Alarms, Contributor Insights, and monitoring.
- IAM policies referencing the old table ARN.
- Global table/replication configuration.
- Application endpoint/configuration.

Do not assume dependent settings follow the data automatically.

### RPO selection

```text
Incident time
  -> choose latest clean restorable point before incident
  -> actual data loss = incident time - chosen point.
```

Examples:

- Daily snapshot: potential loss approaches one day.
- Frequent snapshots: smaller gap, more backup activity/storage.
- PITR: fine-grained point selection inside window.

PITR protects only while enabled and within retention.

### Full RTO clock

RTO includes:

```text
Detect
  + decide clean restore point
  + create restored resource
  + replay/recover data
  + configure dependencies
  + validate
  + switch traffic
  + wait for DNS/cache/connection effects.
```

AWS job completion is only one part.

### Safe restore runbook

```text
1. Detect and contain incident.
2. Preserve evidence and current database.
3. Choose clean snapshot/time.
4. Restore to new resource.
5. Apply network, security, KMS, parameters, scaling.
6. Validate data and application.
7. Stop or reconcile writes during cutover.
8. Update endpoint/DNS/secret/configuration.
9. Monitor errors, latency, and data correctness.
10. Retire old resource only after approval.
```

Do not delete or overwrite the source during investigation.

### Cutover objects

Application may depend on:

- Database endpoint/hostname.
- Route 53 record.
- Secrets Manager secret or Parameter Store value.
- Security group rules.
- IAM policy/resource ARN.
- Lambda environment variable.
- ECS task/EKS/application configuration.
- RDS Proxy target registration.
- Event source/stream configuration.

Changing the database alone may not redirect the application.

### Encryption and cross-Region/account restore

Need:

- Access to source recovery point/snapshot.
- Destination copy where required.
- Source and destination KMS permissions.
- Key enabled in correct Region/account.
- Vault/snapshot sharing policy.
- Restore role permission.

Pattern when a different KMS key is required:

```text
Copy snapshot with destination KMS key
  -> restore copied snapshot.
```

Database permission and KMS permission are separate checks.

### Validation

Before traffic:

- Correct recovery time/data version.
- Key tables/records present.
- Referential/application checks pass.
- Authentication works.
- Network path works.
- Read and write test works safely.
- Performance/capacity is sufficient.
- Backups, alarms, logs, and HA are re-enabled.

After traffic:

- Error rate.
- Query/request latency.
- Connections/throttling.
- Replication/HA status.
- Data consistency.
- Actual RTO and data loss.

### Cost trade-offs

| Choice | Cost tendency | Recovery tendency |
|---|---|---|
| Infrequent snapshots | Lowest | Larger RPO; restore work remains |
| Frequent snapshots | More storage/activity | Smaller snapshot gap |
| PITR | Continuous protection cost | Fine-grained RPO; restore still takes time |
| Warm/live replica | Higher standing cost | Faster traffic recovery |

Do not buy a faster RPO when the requirement is only RTO—or vice versa.

### Failure clues

| Symptom | First checks |
|---|---|
| PITR option unavailable | Automated backups/PITR enabled, retention, supported source |
| Desired time unavailable | Recovery window and latest restorable time |
| Snapshot not visible | Region, account, sharing, copy status |
| Restore cannot decrypt | KMS key state/policy/grant and restore role |
| RDS restore fails networking | DB subnet group, VPC, AZ capacity, security configuration |
| Restored DB exists but app uses old DB | Endpoint/DNS/secret/proxy/configuration not changed |
| Aurora cluster has no service | DB instance/endpoint/parameter/network path |
| DynamoDB restore name conflict | Restore needs a new table name |
| DynamoDB data works but automation fails | Streams, mappings, IAM ARN, TTL, alarms, scaling not rebuilt |
| RTO missed after job completed | Validation/cutover/DNS/warm-up was not included |

### Exam traps

- RPO is allowable data loss; RTO is allowable downtime.
- Snapshot restore and PITR normally create a new resource.
- Latest restorable time is not guaranteed to equal now.
- Choose a time before corruption, not after it.
- A restored database gets a new endpoint/name/ARN.
- Multi-AZ failover is not a restore method.
- Read replica is not a backup replacement.
- Restore-job completion does not mean application recovery.
- DynamoDB restore creates a new table.
- Dependencies and monitoring may need rebuilding.
- Lower RPO and lower RTO are different requirements.

### Do not memorize

- Exact restore duration by database size.
- Every engine-specific restore option.
- Console click paths.
- One universal RTO/RPO target.
- Exact prices.

### Ready when

Given a database-loss scenario, you can:

1. Calculate which objective is RPO and which is RTO.
2. Choose snapshot restore, PITR, AWS Backup, or ready replica.
3. Select a clean valid recovery point/time.
4. Restore and rebuild network, KMS, scaling, and application links.
5. Cut over safely and measure full RTO/data loss.

---

## Skill 2.3.3 - Implement versioning for storage services

**Official goal:** Preserve older storage states so overwritten or deleted data can be recovered.

### What exam tests

- Primary: `CFG BEH PRC`
- Supporting: `GOV OPT`
- Precision: `L2 - Object`
  - Know versioning state, version ID, delete marker, noncurrent lifecycle, retention protection, and restore action.

### Core model

```text
Same object/file name
  -> multiple historical states
  -> choose an older state
  -> make it current again.
```

Versioning is fast logical recovery. It is not automatically an independent backup.

### Fast selection

| Need | Main choice |
|---|---|
| Recover overwritten/deleted S3 object | S3 Versioning |
| Stop permanent S3 version deletion | Object Lock/permissions; MFA Delete recognition |
| Move/delete old S3 versions | Lifecycle for noncurrent versions |
| Keep another Region/account copy | Replication or backup |
| User restores old Windows file | FSx for Windows shadow copies |
| Restore whole FSx filesystem/volume | FSx/AWS Backup mechanism supported by that family |

### S3 versioning states

| State | New write behavior | Old versions |
|---|---|---|
| Unversioned | Overwrite replaces object | No protected history |
| Enabled | New unique version ID | Preserved |
| Suspended | New writes use `null` version behavior | Existing non-null versions remain |

Important:

```text
After enabling versioning,
you can suspend it,
but cannot return bucket to never-versioned state.
```

Suspending does not delete existing versions.

### S3 object model

```text
Bucket
  -> object key
       -> current version
       -> noncurrent versions
       -> possible delete marker
```

Exact objects/properties:

- Bucket versioning status.
- Object key.
- Version ID.
- Current/noncurrent status.
- Delete marker and its version ID.
- Last modified time.
- Storage class/size.
- Replication status where configured.
- Object Lock retention/legal hold where configured.

### Write behavior

With versioning enabled:

```text
PUT same key
  -> new current version
  -> old current becomes noncurrent.
```

The old data still consumes storage.

GET behavior:

- Request key without version ID: return current version.
- Request key with version ID: return that exact version if allowed.

### Delete behavior

**Delete without version ID**

```text
DELETE key
  -> create delete marker as current
  -> older object versions remain.
```

Normal GET now looks deleted.

**Delete with exact version ID**

```text
DELETE key + version ID
  -> permanently delete that version
```

Object Lock or policy can block permanent deletion.

### Restore an S3 object

**Deleted by delete marker**

```text
List versions
  -> find current delete marker
  -> delete that marker by version ID
  -> prior version becomes current.
```

**Overwritten**

```text
List versions
  -> choose good old version
  -> copy it to the same key
  -> copied data becomes a new current version.
```

Copying preserves history and creates a new recovery event.

### Required S3 permissions

Common actions:

- `s3:GetBucketVersioning`
- `s3:PutBucketVersioning`
- `s3:ListBucketVersions`
- `s3:GetObjectVersion`
- `s3:DeleteObjectVersion`

Also check:

- Bucket policy.
- IAM policy/SCP.
- Object Lock retention/legal hold.
- KMS decrypt permission for encrypted older versions.

Object access and KMS access are separate.

### Lifecycle for versions

Current-object lifecycle and noncurrent-version lifecycle are different.

Useful actions:

- Transition current version.
- Expire current version.
- Transition noncurrent versions.
- Permanently expire noncurrent versions.
- Remove expired delete markers where configured.

Core cost rule:

```text
Versioning enabled
  + no noncurrent lifecycle
  -> old versions accumulate cost.
```

Be careful: expiring noncurrent versions removes recovery history permanently.

### Versioned lifecycle behavior

For a versioned bucket:

- Expiring a current object normally adds a delete marker.
- Noncurrent expiration removes old versions permanently.
- Object Lock can prevent lifecycle deletion until protection ends.
- Lifecycle timing is policy-driven, not an immediate restore tool.

Retention must meet recovery/compliance need before cost cleanup.

### S3 Object Lock boundary

```text
Versioning = keep versions.
Object Lock = prevent protected version deletion/change.
```

Object Lock controls:

- Retention period/date.
- Governance mode.
- Compliance mode.
- Legal hold.

Object Lock works on individual versions. It does not choose which version is current.

### S3 replication boundary

Replication can copy versions to another bucket.

Needs:

- Versioning enabled on source and destination.
- Replication rule/scope.
- IAM replication role.
- Destination bucket policy for cross-account use.
- KMS permissions for encrypted objects.
- Destination Region/account where required.

Know:

- New eligible versions can replicate.
- Existing objects may require S3 Batch Replication or another migration action.
- Delete-marker replication follows rule configuration.
- Replication status/errors show whether copy completed.

Replication improves separation. It is not automatically safe from every bad write/delete policy.

### Versioning versus backup

| Control | Best at | Main weakness |
|---|---|---|
| S3 Versioning | Fast recovery of an object key | Same bucket/account control plane |
| Object Lock | Preventing version deletion | Not another copy |
| Replication | Another bucket/Region/account copy | Can copy unwanted changes depending on design |
| AWS Backup | Central recovery points/policy | Restore process required |

Strong design may combine them.

### FSx has no universal versioning switch

Each FSx family differs.

| FSx family | Version-related control to recognize |
|---|---|
| FSx for Windows File Server | Shadow copies/Previous Versions; backups |
| FSx for NetApp ONTAP | Volume snapshots; backup/replication features |
| FSx for OpenZFS | Snapshots/clones and supported backups |
| FSx for Lustre | Supported filesystem backups/data repository protection; not Windows shadow copies |

Choose by filesystem family and recovery scope.

### FSx for Windows shadow copies

```text
User changes/deletes file
  -> open Previous Versions
  -> restore/copy older shadow copy.
```

Needs:

- Shadow-copy storage allocation.
- Schedule.
- Available shadow copy.
- User/admin permissions.

Boundary:

- Fast file-level recovery.
- Stored with the filesystem.
- Consumes filesystem capacity.
- Not an independent full-filesystem backup.

### FSx snapshot/backup boundary

- Snapshot: fast historical state at volume/filesystem layer where supported.
- Backup: separate recovery object used to create/restore supported resources.
- Replication: maintains another data copy/location where supported.
- Shadow copy: end-user file version on Windows filesystem.

Do not assume one FSx family’s objects or commands apply to another.

### Evidence

**S3**

- Bucket versioning status.
- List of versions and delete markers.
- Current version ID.
- Lifecycle configuration.
- Object Lock retention/legal hold.
- Replication rule and status.
- CloudTrail data event for overwrite/delete when enabled.

**FSx**

- Filesystem/volume family.
- Snapshot/shadow-copy list.
- Backup job/recovery point.
- Schedule, capacity, retention, and status.
- File/user permissions.

### Failure clues

| Symptom | First checks |
|---|---|
| Old S3 object missing | Versioning state when write occurred; list versions/delete markers |
| Object looks deleted but versions exist | Current delete marker |
| Delete marker removed but object still absent | Wrong marker/version or previous version permanently deleted |
| Old version access denied | `GetObjectVersion`, bucket/SCP, KMS key |
| Cannot delete old version | `DeleteObjectVersion`, Object Lock, legal hold, policy |
| Storage cost grows | Noncurrent versions and lifecycle policy |
| Replica missing | Rule scope, versioning, role/policy, KMS, replication status |
| Old objects never replicated | Rule covers new writes; existing data needs batch action |
| Windows Previous Versions empty | Shadow copies disabled, no schedule/capacity, no snapshot |
| FSx restore choice invalid | Wrong filesystem family/control |

### Recovery path

```text
Identify service/family
  -> list versions/snapshots
  -> choose clean state
  -> check retention, permissions, KMS
  -> restore/copy without destroying evidence
  -> validate
  -> fix lifecycle/protection gap.
```

### Exam traps

- S3 delete without version ID usually creates a delete marker.
- Delete marker is not the object data.
- Delete with a version ID can be permanent.
- Suspending versioning preserves existing versions.
- Versioning costs storage for every retained version.
- Current expiration and noncurrent expiration behave differently.
- Object Lock protects versions; it is not replication.
- Replication needs versioning on both buckets.
- Replication does not automatically include old objects.
- FSx families do not share one universal versioning feature.
- Windows shadow copies are not independent backups.

### Do not memorize

- Every lifecycle XML/JSON field.
- Exact replication-status enum.
- Every FSx command.
- Exact shadow-copy capacity formula.
- Console click paths.

### Ready when

Given a storage-recovery scenario, you can:

1. Explain enabled, suspended, current, noncurrent, and delete-marker behavior.
2. Restore an overwritten or deleted S3 object safely.
3. Configure noncurrent lifecycle without accidental data loss.
4. Separate Versioning, Object Lock, replication, and backup.
5. Choose the correct FSx-family snapshot/shadow-copy/backup control.

---

## Skill 2.3.4 - Follow disaster-recovery procedures and best practices

**Official goal:** Recover a workload from a major failure by using a tested strategy and runbook.

### What exam tests

- Primary: `PRC SEL OPT BEH`
- Supporting: `CFG GOV`
- Precision: `L2 - Object`
  - Know the strategy, standing recovery resources, data method, activation steps, traffic control, and failback.

### Core distinction

```text
High availability
  -> keep serving through local/resource/AZ failure.

Disaster recovery
  -> restore or shift workload after major/Regional failure.
```

Multi-AZ is not automatically multi-Region DR.

### Four DR strategies

| Strategy | Recovery environment before disaster | Cost | Typical RTO/RPO tendency |
|---|---|---|---|
| Backup and restore | Backups; little/no runtime | Lowest | Longest |
| Pilot light | Core/data running; app mostly off | Low-medium | Faster |
| Warm standby | Full workload running at reduced capacity | Medium-high | Short |
| Multi-site active/active | Full workload serving in multiple Regions | Highest | Shortest |

Order:

```text
More ready infrastructure
  -> faster recovery
  -> higher cost and complexity.
```

Exact RTO/RPO still depends on data replication, automation, testing, and scale-up time.

### Fast exam clues

| Wording | Choose |
|---|---|
| “Lowest cost; hours to restore” | Backup and restore |
| “Database/core services always running; compute started later” | Pilot light |
| “Complete smaller environment already working” | Warm standby |
| “Both Regions serve production traffic” | Multi-site active/active |
| “Automatic AZ failover in one Region” | High availability, not multi-Region DR strategy |

### Backup and restore

Before disaster:

- Protected backups/snapshots.
- Cross-Region/account copy where required.
- Infrastructure as code.
- Images/artifacts/configuration available.
- Restore runbook tested.

During recovery:

```text
Deploy infrastructure
  -> restore data
  -> start application
  -> validate
  -> redirect traffic.
```

Best when cost matters more than fast recovery.

Main risk: hidden dependencies and long manual restore/cutover time.

### Pilot light

Before disaster:

- Critical data continuously replicated.
- Core services running.
- Most application compute stopped, absent, or minimal.
- Deployment and scale automation ready.

During recovery:

```text
Promote/activate data
  -> deploy/start compute
  -> scale
  -> validate
  -> redirect traffic.
```

Faster than backup/restore because the data/core already exists.

Pilot light is not a fully functioning production environment before activation.

### Warm standby

Before disaster:

- Complete application stack running.
- Data replicated.
- Environment functional but smaller than production.
- Health and monitoring active.

During recovery:

```text
Scale up warm environment
  -> verify capacity/data
  -> redirect traffic.
```

Main difference:

```text
Pilot light = core only.
Warm standby = whole workload works at reduced scale.
```

### Multi-site active/active

Before disaster:

- Multiple Regions serve users.
- Data replication/conflict design active.
- Traffic distribution and health controls active.
- Each site has defined failure capacity.

During failure:

```text
Remove failed Region from traffic
  -> remaining Region(s) absorb load.
```

Needs the most work:

- Data consistency/conflict handling.
- Global traffic routing.
- Enough spare capacity.
- Regional dependency isolation.
- Continuous testing and operations.

Active/active reduces recovery time but increases failure modes.

### Strategy is not the data method

Every strategy still needs data protection.

| Data need | Example mechanism |
|---|---|
| Restore from recovery point | AWS Backup/snapshot copy |
| S3 object copy | Cross-Region Replication/versioning |
| DynamoDB multi-Region writes | Global tables |
| Aurora cross-Region recovery | Aurora Global Database/replica or backup restore |
| RDS cross-Region recovery | Cross-Region replica or copied snapshot/backup |
| EFS second-Region data | EFS replication or backup copy |

Traffic tools do not replicate data.

### Recovery dependency order

Common order:

```text
Account/IAM/KMS/quotas
  -> network/DNS/security
  -> data stores
  -> shared services/queues/secrets
  -> application compute
  -> load balancers/health
  -> traffic shift
  -> validation/monitoring.
```

Exact application dependencies can change the order.

Start traffic only after the data and application are ready.

### Infrastructure and artifact readiness

Recovery Region may need:

- CloudFormation/CDK templates.
- StackSets for multi-account/Region deployment.
- AMIs and launch templates.
- ECR images/application packages.
- S3 artifacts.
- Secrets/parameters.
- KMS keys and policies.
- ACM certificates.
- Service-linked roles/IAM roles.
- Quotas and IP capacity.
- VPC, subnets, routes, endpoints, and security groups.

IaC recreates declared infrastructure. It does not copy database state or undeclared dependencies.

### Detection and declaration

```text
Alarm/event
  -> confirm scope
  -> incident authority declares disaster
  -> freeze unsafe changes
  -> invoke correct runbook.
```

Define beforehand:

- Who declares DR.
- Which evidence is required.
- Which runbook/version to use.
- Communication/escalation path.
- Manual approval points.
- Abort/rollback criteria.

Do not trigger destructive failover from one noisy alarm without safeguards.

### Traffic shift choices

| Need | Tool |
|---|---|
| DNS record failover | Route 53 |
| Static anycast entry and endpoint traffic control | Global Accelerator |
| Guarded operator-controlled recovery | ARC routing controls/Region switch |
| Move supported traffic away from one AZ | ARC zonal shift |

Route 53 considerations:

- Health check/routing policy.
- Record association.
- TTL and resolver caching.
- Healthy secondary endpoint.

Global Accelerator considerations:

- Endpoint group/endpoint health.
- Traffic dial/endpoint weight where used.
- Recovery endpoints must already be configured and reachable.

### Failover runbook

```text
1. Detect and declare.
2. Contain writes/damage.
3. Confirm recovery Region and quotas.
4. Restore/promote and verify data.
5. Deploy/start infrastructure in dependency order.
6. Scale to required capacity.
7. Apply secrets, IAM, KMS, network, and configuration.
8. Run technical and business validation.
9. Shift traffic gradually where possible.
10. Monitor, communicate, and stabilize.
```

Record times to measure real RTO and RPO.

### Validation before traffic

- Correct data point and replication state.
- No split-brain/dual-writer risk unless design supports it.
- Authentication and secrets work.
- Network paths and DNS work.
- Queues/events have correct consumers.
- Application read/write tests pass.
- Capacity can take expected traffic.
- Alarms, logs, dashboards, backups, and security controls work.

Health check alone is not full business validation.

### Failback

Failback is a new controlled migration, not simply “turn primary back on.”

```text
Repair original Region
  -> rebuild/validate it
  -> synchronize changed data
  -> choose write authority
  -> shift traffic back gradually
  -> validate
  -> restore normal replication/protection.
```

Prevent:

- Stale data overwriting newer recovery data.
- Two unintended writers.
- Traffic before capacity is ready.
- Deleting the only good recovery copy.

### Testing

Test regularly:

- Backup restore.
- Infrastructure deployment.
- Data promotion/replication.
- Scaling time.
- Traffic shift and rollback.
- Permissions/KMS/certificates/secrets.
- Monitoring and communications.
- Failback.

Useful test types:

- Tabletop: people walk through decisions.
- Technical drill: execute parts safely.
- Full recovery exercise: run end-to-end in isolated/controlled scope.

Update the runbook from observed evidence.

### Evidence

- Recovery-point age/copy status.
- Replication lag/health.
- CloudFormation stack status.
- Quota/capacity availability.
- Database promotion/restore events.
- ELB/Route 53/Global Accelerator/ARC health and traffic state.
- Application errors, latency, and business checks.
- Timeline versus RTO.
- Recovered data point versus RPO.

### Failure clues

| Symptom | First checks |
|---|---|
| Recovery stack will not deploy | IAM, quota, Region-specific parameter, dependency/artifact |
| Restored data is too old | Backup/copy schedule and actual recovery point versus RPO |
| Replica cannot promote safely | Lag, state, write authority, engine procedure |
| Recovery app cannot decrypt | KMS key/policy/grant in recovery Region/account |
| Environment works internally but users fail | Traffic record/endpoint, health, certificate, TTL/cache |
| Warm standby overloads | Scale-up incomplete or capacity/quota too low |
| Both Regions accept unsafe writes | Split-brain/traffic-control failure |
| Failback loses new data | Reverse synchronization not complete |
| Test meets service restore but misses RTO | Deployment, validation, traffic shift omitted from timing |

### Exam traps

- Backup/restore normally has lowest cost and longest recovery.
- Pilot light has core/data running, not the full application.
- Warm standby is fully functional at reduced capacity.
- Active/active serves traffic from multiple sites before disaster.
- Multi-AZ is high availability, not multi-Region DR.
- Route 53/Global Accelerator/ARC move traffic; they do not copy data.
- CloudFormation recreates infrastructure, not application data.
- A recovery Region needs quotas, keys, secrets, certificates, and artifacts.
- Failover without validation can expose corrupt or stale data.
- Failback requires data reconciliation and its own runbook.
- Recovery tests must measure the complete RTO/RPO.

### Do not memorize

- Universal recovery times for each strategy.
- Exact prices.
- Every Global Accelerator/ARC field.
- One dependency order for every application.
- Console click paths.

### Ready when

Given a DR scenario, you can:

1. Choose backup/restore, pilot light, warm standby, or active/active.
2. Explain the cost and RTO/RPO trade-off.
3. Identify required data, infrastructure, security, and traffic controls.
4. Execute failover in dependency order and validate before traffic.
5. Explain safe failback and prove recovery through testing.

---

## Skill 3.1.1 - Create and manage AMIs and container images

**Official goal:** Build, test, distribute, secure, and retire reusable EC2 and container images.

### What exam tests

- Primary: `CFG PRC DIA`
- Supporting: `GOV EVD`
- Precision: `L2 - Object`
  - Know AMI/snapshot relationships, ECR repository/tag/digest, and Image Builder pipeline objects.

### Core distinction

| Image | Contains | Starts as |
|---|---|---|
| AMI | OS, packages, configuration, block-device mapping | EC2 instance |
| Container image | Application/runtime filesystem layers and metadata | Container |

Both should be:

```text
Build -> patch -> test -> scan -> distribute -> launch -> retire.
```

### AMI object model

```text
AMI
  -> AMI metadata
  -> root-volume snapshot
  -> optional data-volume snapshots
  -> block-device mappings.
```

AMI metadata includes:

- Architecture.
- Root device type/name.
- Virtualization type.
- Boot mode where relevant.
- Block-device mappings.
- Launch permissions.
- Owner/account.
- Region-specific AMI ID.
- Tags/name/description.

### Create an AMI from EC2

```text
Configured instance
  -> create image
  -> EBS snapshots
  -> AMI becomes available
  -> launch test instance.
```

Default reboot helps filesystem consistency.

No-reboot choice:

- Avoids the reboot interruption.
- Pending writes can produce crash-consistent, not application-consistent, data.
- Application quiesce/flush may still be needed.

For multiple volumes, coordinate writes before capture.

### What an AMI does not carry automatically

- Running instance identity.
- Elastic IP attachment.
- IAM role/profile attachment.
- Security group selection.
- Subnet placement.
- Current instance user data.
- External database/data state.
- Secrets that should be supplied at launch.

Launch templates/user data/configuration management complete the instance.

### AMI launch compatibility

Check:

- CPU architecture: x86_64 versus Arm64.
- Chosen instance type supports that architecture.
- Virtualization/root-device/boot-mode support.
- Required ENA/NVMe/storage/network drivers.
- OS license/product-code rules.
- AMI owner and launch permission.
- AMI and launch Region.
- Snapshot and KMS-key access.

Architecture mismatch means the instance cannot boot correctly.

### AMI share versus copy

| Action | Result |
|---|---|
| Share | Another account can use source AMI; source owner retains it |
| Copy | New AMI/snapshots with new ID in destination account/Region |

Sharing needs:

- AMI launch permission.
- Snapshot access where required.
- Customer-managed KMS-key policy/grant for encrypted images.

Encrypted cross-account sharing normally needs a customer-managed KMS key. AWS-managed-key encryption is not a general cross-account sharing solution.

Copying can provide independent ownership and destination encryption.

### AMI Region behavior

- AMI IDs are Region-specific.
- Copy to each required Region.
- Copied AMI receives a new ID.
- Tags/permissions/configuration should be verified after copy.
- Automation should resolve the correct Region’s AMI ID.

One hard-coded AMI ID does not work globally.

### AMI retirement

```text
Stop new use
  -> update launch templates/catalogs
  -> verify no required dependency
  -> deregister AMI
  -> delete unneeded snapshots separately.
```

Important:

- Deregistering blocks new launches.
- Existing instances keep running.
- Deregistration does not automatically delete every backing snapshot.
- Snapshot deletion saves cost but removes image recovery material.

### EC2 Image Builder object tree

```text
Image pipeline
  -> image recipe/container recipe
       -> base image
       -> build components
       -> test components
  -> infrastructure configuration
  -> distribution configuration.
```

### Image Builder objects

**Recipe**

- Versioned definition.
- Base image.
- Components.
- Block-device/container settings.

**Component**

- Build or test steps.
- Install patches/software.
- Apply hardening/configuration.
- Validate result.

**Infrastructure configuration**

- Build/test instance type.
- Instance profile/role.
- VPC subnet/security group.
- Logging/output settings.
- SNS notification where configured.

**Distribution configuration**

- Destination Regions.
- Target accounts/organizations.
- AMI/container naming and permissions.
- Encryption/key settings where used.

### Image Builder flow

```text
Resolve base image
  -> launch temporary builder
  -> run build components
  -> create image
  -> launch temporary test resource
  -> run test components
  -> distribute only after success.
```

Pipeline can run:

- Manually.
- On a schedule.
- When dependency/update conditions require, where configured.

Failed build/test should stop bad image distribution.

### Image Builder evidence

- Pipeline execution status.
- Build/test phase and failed component step.
- CloudWatch Logs/S3 logs where configured.
- Build EC2 instance/network state.
- IAM instance-profile/service-role events.
- Output AMI/image ARN and lineage.
- Distribution/copy status by Region/account.
- Inspector/ECR scan findings where integrated.

Read the first failed component, not only the final pipeline status.

### ECR object model

```text
Account/Region registry
  -> repository
       -> image manifest
       -> layers
       -> tag(s)
       -> immutable digest.
```

Exact objects/properties:

- Registry URI.
- Repository name/URI.
- Repository policy.
- Image tag.
- Image digest.
- Tag-mutability setting.
- Scan configuration/findings.
- Encryption configuration.
- Lifecycle policy.
- Replication configuration.

### Tag versus digest

```text
Tag = movable human label, such as prod or v2.
Digest = immutable content identity, sha256:...
```

If tags are mutable, pushing the same tag can point it to different content.

Use:

- Tag for readable release labels.
- Tag immutability to block accidental reuse.
- Digest when exact content must be pinned.

“Latest” is convenient, not reproducible.

### Push/pull permission path

```text
Authenticate to registry
  -> authorize repository action
  -> find tag/digest
  -> download manifest/layers
  -> run compatible image.
```

Common IAM actions/controls:

- ECR authorization token.
- Repository push/pull actions.
- Repository policy for cross-account access.
- ECS task execution role or compute/node role that performs pull.
- KMS access where customer-managed encryption requires it.

Application task role is not always the role that pulls the image.

### ECR network path

Private workload needs a path to:

- ECR API.
- ECR Docker registry endpoint.
- S3 layer storage path.
- DNS.

Provide:

- NAT/internet path, or
- Correct VPC endpoints and policies.

PrivateLink design commonly needs ECR API and ECR DKR interface endpoints plus an S3 gateway endpoint.

### ECR scanning

- Scan image for package vulnerabilities.
- Basic/enhanced scanning depends on configured mode.
- Enhanced findings integrate with Amazon Inspector.
- Findings have severity and remediation data.
- New findings can appear after image push as vulnerability data changes.

Important:

```text
Scan finding does not automatically block deployment
unless policy/pipeline enforcement does so.
```

Patch the recipe/base/package, rebuild, retest, and publish a new image.

### ECR lifecycle policy

Rules can expire images by:

- Tag status/prefix/pattern.
- Image count.
- Age.
- Rule priority.

Use lifecycle-policy preview before applying.

Trap:

```text
Lifecycle deletes old image
  -> running container may continue
  -> replacement task later cannot pull it.
```

Retain every image digest still needed for rollback or scaling.

### ECR replication

Use for required Regions/accounts.

Needs:

- Registry replication rule.
- Destination Region/account.
- Destination registry permission for cross-account use.
- Repository/prefix filter where configured.
- KMS and pull permission at destination.

Verify eligible images and tags exist in destination. Do not assume old images or every repository appeared without checking rule scope.

### Multi-architecture containers

- Image architecture must match runtime architecture.
- A manifest list/image index can reference platform-specific images.
- ECS task or EKS node architecture must have a matching image.

Typical failure:

```text
Arm image
  -> x86 runtime
  -> exec-format/start failure.
```

### Failure clues

| Symptom | First checks |
|---|---|
| AMI not found | Region, owner, AMI ID, deregistration |
| AMI launch denied | Launch permission, snapshot permission, KMS policy/grant |
| Instance will not boot | Architecture, boot/root mapping, driver, corrupted/inconsistent image |
| Copied AMI unusable | Copy state, destination KMS, permissions, architecture |
| Image Builder build fails | First failed component, instance profile, network, package source, disk |
| Image Builder test fails | Test step/logs, service startup, expected file/port/configuration |
| Distribution fails | Destination role/account policy, KMS, Region quota/permission |
| ECR authentication error | Token, principal, Region, registry URI |
| ECR access denied | Identity policy, repository policy, pull-role identity, KMS |
| Image/tag not found | Repository URI, Region/account, tag/digest, lifecycle deletion |
| Container pull timeout | DNS, NAT/endpoints, SG/NACL, endpoint policy, S3 path |
| Container starts then crashes | Entrypoint/config/secret/runtime issue, not necessarily ECR |
| Exec-format error | Image/runtime architecture mismatch |
| Vulnerable image still deploys | Scan has no blocking policy/pipeline gate |

### Operational path

```text
Use trusted base
  -> apply patch/hardening components
  -> build
  -> test and scan
  -> distribute
  -> update launch/task reference
  -> canary/validate
  -> retain rollback image
  -> retire old image safely.
```

### Exam traps

- AMI ID is Region-specific.
- AMI shares and AMI copies are different.
- Encrypted cross-account image use needs KMS permission too.
- No-reboot AMI creation can reduce consistency.
- Deregistering an AMI does not terminate existing instances.
- Deregistering does not automatically clean every snapshot.
- Image Builder recipe, pipeline, infrastructure, and distribution are separate objects.
- Failed tests should stop distribution.
- ECR tag can move; digest identifies exact content.
- Repository permission and registry authentication are separate.
- ECS task role and task execution role serve different purposes.
- Private ECR pull also needs network access to image layers.
- Scan findings do not block deployment by themselves.
- Lifecycle deletion can break rollback or future scale-out.

### Do not memorize

- Every Image Builder component-document field.
- Every ECR IAM action.
- Exact vulnerability database timing.
- Every AMI boot-mode combination.
- Dockerfile syntax.
- Console click paths.

### Ready when

Given an image scenario, you can:

1. Explain AMI -> snapshots and ECR tag -> digest relationships.
2. Build/test/distribute an image with Image Builder.
3. Share/copy encrypted AMIs with correct Region/account/KMS controls.
4. Configure ECR scanning, immutability, lifecycle, and replication.
5. Diagnose AMI launch or container pull/start failures.

---

## Skill 3.1.2 - Create and manage resources with CloudFormation and AWS CDK

**Official goal:** Declare AWS resources as code, preview changes, deploy safely, and manage their lifecycle.

### What exam tests

- Primary: `CFG BEH PRC`
- Supporting: `DIA GOV`
- Precision: `L3 - Property`
  - Exact template section, intrinsic function, update behavior, retention control, CDK command, and permission matter.

### Core model

```text
Template
  -> stack
  -> physical AWS resources.

Template change
  -> change set
  -> stack update
  -> in-place change or replacement.
```

CloudFormation owns resource lifecycle. Avoid manual changes.

### Template structure

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Example
Parameters: {}
Mappings: {}
Conditions: {}
Transform: ...
Resources: {}
Outputs: {}
```

`Resources` is the main required section.

### Template sections

| Section | Use |
|---|---|
| Parameters | Values supplied at deployment |
| Mappings | Static lookup table in template |
| Conditions | Decide whether/value to create or use |
| Transform | Macro/template transformation, such as SAM |
| Resources | AWS objects to create/manage |
| Outputs | Return or export useful values |
| Metadata | Extra information for tools/resources |
| Rules | Validate parameter combinations |

Do not use mappings for dynamic live service data.

### Resource anatomy

```yaml
Resources:
  WebBucket:                    # logical ID
    Type: AWS::S3::Bucket
    DeletionPolicy: Retain
    UpdateReplacePolicy: Retain
    Properties:
      BucketEncryption: ...
```

Know:

- Logical ID: name inside template.
- Resource type: `AWS::Service::Resource`.
- Properties: desired configuration.
- Physical ID: real resource name/ID after creation.

Logical and physical IDs are not the same.

### Parameters

Useful properties:

- Type.
- Default.
- Allowed values/pattern/range.
- Description.
- `NoEcho`.

Use parameters for environment-specific input.

`NoEcho: true` masks normal display. It is not encryption and does not safely hide values placed in Metadata or Outputs.

Prefer Secrets Manager/Parameter Store dynamic references for secrets.

### Core intrinsic functions

| Function | Meaning |
|---|---|
| `Ref` | Parameter value or resource’s main physical identifier |
| `Fn::GetAtt` | Resource attribute |
| `Fn::Sub` | Substitute variables in string |
| `Fn::Join` | Join strings |
| `Fn::FindInMap` | Read mapping value |
| `Fn::If` | Choose value from condition |
| `Fn::ImportValue` | Read another stack’s export |
| `Fn::Select` | Choose list item |
| `Fn::Split` | Split string into list |
| `Fn::GetAZs` | Get AZ names for Region |
| `Fn::Base64` | Encode user data/string |

Condition functions:

- `Equals`
- `And`
- `Or`
- `Not`

Read the data flow; do not memorize YAML punctuation only.

### References and dependencies

```text
Ref/GetAtt/Sub references another resource
  -> CloudFormation creates implicit dependency.
```

Use `DependsOn` when ordering is required but no reference creates it.

Do not add `DependsOn` everywhere. It slows parallel creation and can hide poor design.

### Conditions

```yaml
Conditions:
  IsProd: !Equals [!Ref Environment, prod]
```

Apply to:

- Whole resources.
- Outputs.
- Property values through `Fn::If`.

Condition is evaluated during stack operation from parameters/mappings/pseudo parameters.

### Pseudo parameters

Recognition examples:

- `AWS::AccountId`
- `AWS::Region`
- `AWS::StackName`
- `AWS::Partition`
- `AWS::NoValue`

`AWS::NoValue` removes a conditional property value.

### Outputs and exports

```text
Stack A output/export
  -> Stack B Fn::ImportValue.
```

Rules:

- Export name must be unique in account/Region.
- Import/export is same account/Region.
- Export cannot be removed or changed while another stack imports it.
- Outputs are not a safe place for secrets.

Use for deliberate cross-stack dependency.

### Nested stacks

```text
Parent stack
  -> AWS::CloudFormation::Stack resource
  -> child/nested stack.
```

Use to split/reuse large templates.

- Parent passes parameters.
- Child returns outputs.
- Parent controls nested lifecycle.
- Troubleshooting follows parent event into child events.

Nested stack is not the same as StackSets.

### Change sets

```text
Proposed template/parameters
  -> change set
  -> Add / Modify / Remove / Replace preview
  -> review
  -> execute or delete.
```

Use before risky updates.

Change set shows planned infrastructure actions. It cannot guarantee application success or reveal every service-runtime effect.

### Update behavior

A property change can cause:

| Behavior | Effect |
|---|---|
| No interruption | Modify resource in place |
| Some interruption | In-place change with disruption |
| Replacement | Create new physical resource; switch reference; remove/retain old |

Replacement risk:

- New physical ID/name/endpoint.
- Data loss if old resource deleted.
- Temporary extra quota/capacity needed.
- Downstream references may change.

Always inspect replacement for stateful resources.

### Deletion controls

**DeletionPolicy**

Controls resource when removed from template or stack is deleted:

- `Delete`
- `Retain`
- `Snapshot` for supported resources

**UpdateReplacePolicy**

Controls old physical resource when an update replaces it:

- `Delete`
- `Retain`
- `Snapshot` where supported

Core trap:

```text
DeletionPolicy protects deletion.
UpdateReplacePolicy protects old resource during replacement.
```

For important state, often consider both.

### Other stack protections

| Control | Protects against |
|---|---|
| Termination protection | Deleting the stack |
| Stack policy | Updates to selected stack resources |
| DeletionPolicy | Resource deletion with stack/template removal |
| UpdateReplacePolicy | Old resource loss during replacement |

Termination protection does not block normal stack updates.

Stack policy does not replace IAM permission.

### Rollback

```text
Deployment resource fails
  -> stack rolls back successful changes
  -> stack returns toward prior stable state.
```

Common statuses to recognize:

- `CREATE_IN_PROGRESS` / `CREATE_COMPLETE`
- `CREATE_FAILED`
- `ROLLBACK_IN_PROGRESS` / `ROLLBACK_COMPLETE`
- `UPDATE_IN_PROGRESS` / `UPDATE_COMPLETE`
- `UPDATE_ROLLBACK_IN_PROGRESS`
- `UPDATE_ROLLBACK_FAILED`

Start diagnosis from the first failed resource event, not the final rollback event.

Detailed rollback repair belongs in Skill 3.1.3.

### Drift

```text
Template expected state
  versus
actual supported resource state
  -> drift status/differences.
```

- Detects supported out-of-band changes.
- Does not support every resource/property.
- Does not automatically fix drift.
- Stack can be drifted because one resource is drifted.

Fix by bringing code and reality back into controlled agreement.

### Resource import

Supported existing resources can be imported into stack management.

Needs:

- Template resource definition.
- Stable identifier for physical resource.
- Compatible resource/configuration.
- Retention/safety review.

Import adopts; it does not recreate the resource.

### IAM and security

Deployment path:

```text
Caller
  -> CloudFormation service/execution role
  -> AWS service APIs/resources.
```

Check:

- Caller can create/update stack and pass execution role.
- `iam:PassRole` for the exact role.
- Execution role can create/update resources.
- KMS/resource policies allow service actions.
- IAM capabilities acknowledged.

Capabilities:

- `CAPABILITY_IAM`
- `CAPABILITY_NAMED_IAM`
- `CAPABILITY_AUTO_EXPAND` for macros where required

Capabilities acknowledge powerful template behavior. They do not grant missing IAM permission.

### Secrets

Avoid plaintext secrets in:

- Template source.
- Parameters without protected handling.
- Outputs.
- Metadata.
- Logs.

Use dynamic references, for example:

```text
CloudFormation reference
  -> Secrets Manager or SSM Parameter Store
  -> value resolved during deployment.
```

Also grant the execution/service role access to the secret and KMS key.

### AWS CDK object model

```text
CDK app
  -> stack(s)
       -> constructs
            -> synthesized CloudFormation resources.
```

Objects:

- App.
- Stack.
- Construct.
- Environment: account + Region.
- Context/lookups.
- Tokens/lazy values.
- Assets: files, Lambda packages, container images.

CDK is a higher-level way to produce CloudFormation.

### Construct levels

| Level | Meaning |
|---|---|
| L1 | Direct CloudFormation resource; low-level properties |
| L2 | AWS service construct with helpful defaults/methods |
| L3 | Opinionated multi-resource pattern |

Higher level means convenience, not a different deployment engine.

### CDK command chain

```text
cdk bootstrap
  -> prepare account/Region toolkit resources.

cdk synth
  -> produce CloudFormation template.

cdk diff
  -> compare deployed stack with proposed template.

cdk deploy
  -> stage assets and deploy CloudFormation stack.
```

`cdk destroy` deletes stack through CloudFormation, subject to protections/retention.

### CDK bootstrap

Bootstrap creates environment support such as:

- Asset bucket.
- ECR repository where needed.
- Deployment/file/image publishing roles.
- CloudFormation execution role.

Bootstrap is per target environment/account/Region as required.

Cross-account deployment needs correct bootstrap trust and role permissions.

### CDK assets and context

**Assets**

- Local file/image built or staged before deployment.
- Uploaded to bootstrap S3/ECR.
- Missing publish permission/network can fail deploy before resource creation.

**Context/lookups**

- Resolve environment information during synth.
- Cached context can become stale.
- Account/Region-specific lookup requires correct environment and credentials.

**Token**

- Value unresolved until synth/deploy/CloudFormation runtime.
- Seeing `${Token[...]}` too early means code tried to use an unresolved value as a normal string.

### CDK behavior

- `synth` success does not prove deployment permission/capacity.
- `diff` is a preview, not execution.
- `deploy` inherits CloudFormation update/replacement/rollback behavior.
- CDK failure often requires reading CloudFormation stack events.
- Manual resource edits create the same drift problem.

### AWS Service Catalog

Use when central teams provide approved products while users avoid broad infrastructure permissions.

Object tree:

```text
Portfolio
  -> product
       -> provisioning artifact/version
       -> constraints
  -> principal access

Launch product
  -> provisioned product
  -> underlying CloudFormation stack/resources.
```

Key objects:

- Portfolio.
- Product.
- Provisioning artifact/version.
- Principal association.
- Launch constraint/role.
- Template constraint.
- Provisioned product.

Launch role allows approved deployment without giving the user every underlying service permission.

### Evidence

- Template validation/synth output.
- Change set and replacement flags.
- Stack events and first failure.
- Resource logical/physical IDs.
- Drift results.
- CloudTrail caller and API denial.
- CDK diff/synth/deploy output.
- Asset publication logs.
- Service Catalog product/version/constraint and provisioned-product event.

### Failure clues

| Symptom | First checks |
|---|---|
| Unexpected resource replacement | Changed property, change set, physical-name constraint |
| Resource deleted with stack | DeletionPolicy/UpdateReplacePolicy absent or wrong |
| Export update blocked | Another stack imports it |
| Stack update denied | Caller, execution role, `PassRole`, stack policy, IAM capability |
| Secret access denied | Execution role, secret policy, KMS key |
| Drift exists | Manual/out-of-band change on supported property |
| `cdk synth` fails | Code/context/dependency/lookup error |
| `cdk deploy` fails before stack | Bootstrap or asset publication/credentials |
| `cdk deploy` rolls back | Read CloudFormation first failed resource event |
| Service Catalog product unavailable | Portfolio/principal share or product version |
| Product launch denied | Launch role, `PassRole`, constraint, underlying template permission |

### Safe lifecycle

```text
Validate/synth
  -> diff/change set
  -> inspect replacements and data policy
  -> deploy
  -> read events
  -> validate application
  -> detect drift
  -> update only through code.
```

### Exam traps

- `Ref` and `GetAtt` return different values.
- Reference normally creates dependency; `DependsOn` is for missing implicit order.
- `NoEcho` is masking, not encryption.
- Outputs/Metadata can expose secrets.
- Change set previews infrastructure action, not application success.
- Stateful-property change can replace the resource.
- `DeletionPolicy` and `UpdateReplacePolicy` solve different deletion paths.
- Termination protection blocks stack delete, not stack update.
- Drift detection reports; it does not remediate.
- Nested stacks are not StackSets.
- CDK synthesizes and deploys CloudFormation.
- `synth`, `diff`, and `deploy` are different stages.
- IAM capability acknowledgement does not grant permission.
- Service Catalog launch role is different from the end user’s role.

### Do not memorize

- Every CloudFormation resource property.
- Every intrinsic-function syntax variant.
- Complex CDK application code.
- Every stack status.
- Console click paths.

### Ready when

Given an IaC scenario, you can:

1. Read template sections, references, conditions, and outputs.
2. Predict in-place update versus replacement risk.
3. Choose DeletionPolicy, UpdateReplacePolicy, stack policy, and termination protection.
4. Run bootstrap -> synth -> diff -> deploy and follow failures into stack events.
5. Detect drift and protect secrets/stateful resources.
6. Explain Service Catalog portfolio -> product -> provisioned product.

---

## Skill 3.1.3 - Identify and remediate deployment issues

**Official goal:** Find the first real deployment failure, fix its cause, preserve state, and return the deployment to a stable state.

### What exam tests

- Primary: `EVD DIA REM PRC`
- Supporting: `GOV BEH`
- Precision: `L3 - Property`
  - Exact event, status, reason, principal, quota, subnet capacity, and rollback action matter.

### Core troubleshooting model

```text
Tool/template stage
  -> CloudFormation orchestration
  -> AWS service control plane
  -> resource startup/network
  -> application health.
```

Find which layer failed first.

### First rule

```text
Open stack events
  -> ignore later rollback noise
  -> find earliest FAILED resource
  -> read exact StatusReason.
```

Events often display newest first. Work backward to the first failure.

### CloudFormation event fields

- Timestamp.
- Logical resource ID.
- Physical resource ID.
- Resource type.
- Resource status.
- Resource status reason.
- Client request token where relevant.

The logical ID tells where in the template. The physical ID tells which real resource to inspect.

### Failure path

```text
Parent stack fails
  -> inspect failed nested-stack resource
  -> open child stack events
  -> find child’s first failed resource
  -> inspect that AWS service.
```

Final parent error is often only a summary.

### Status meanings

| Status | Meaning/action |
|---|---|
| `CREATE_FAILED` | Resource creation failed; read reason |
| `ROLLBACK_IN_PROGRESS` | Stack undoing create changes |
| `ROLLBACK_COMPLETE` | Failed create rolled back; stack normally must be deleted before recreation |
| `UPDATE_ROLLBACK_IN_PROGRESS` | Failed update returning to old state |
| `UPDATE_ROLLBACK_COMPLETE` | Prior state restored |
| `UPDATE_ROLLBACK_FAILED` | Rollback itself is blocked; fix blocker then continue rollback |
| `DELETE_FAILED` | One or more resources could not be deleted |

Do not start a new update while the stack is still moving through rollback.

### `UPDATE_ROLLBACK_FAILED`

Safe path:

```text
Read rollback failure
  -> fix permission/dependency/resource condition
  -> ContinueUpdateRollback
  -> reach UPDATE_ROLLBACK_COMPLETE
  -> create reviewed corrective change set.
```

`resources-to-skip` is last resort.

- Skipped resources may not match the template.
- Stack becomes operationally inconsistent.
- Reconcile them before the next normal update.

### Evidence order

```text
1. Deployment command/output.
2. Change set/template diff.
3. Stack events and first failure.
4. CloudTrail for caller/API denial.
5. Service-specific event/state.
6. Resource logs/network evidence.
7. Application health/logs.
```

Do not begin with random resource changes.

### Failure categories

| Error clue | Category |
|---|---|
| `AccessDenied`, unauthorized | IAM/resource policy/KMS/SCP |
| `PassRole` denied | Caller cannot pass named role |
| Capability required | IAM/macro acknowledgement missing |
| Already exists/name unavailable | Name collision or unmanaged existing resource |
| Limit/quota exceeded | Service quota/resource count |
| Insufficient capacity | AZ/instance/service capacity |
| Insufficient free addresses | Subnet IP exhaustion |
| Invalid property/parameter | Template, parameter, Region/engine support |
| Timeout/unhealthy | Runtime, network, startup, dependency, health check |
| Delete/replace blocked | Stateful dependency, protection, nonempty resource |

Classify first. Then inspect the right evidence.

### Permission chain

```text
Human/pipeline caller
  -> CloudFormation API
  -> CloudFormation execution role
  -> target AWS service
  -> resource policy/KMS key.
```

Possible blockers:

- Caller lacks stack action.
- Caller lacks `iam:PassRole` for execution/launch role.
- Role trust policy rejects CloudFormation/service.
- Execution role lacks target service action.
- Permission boundary/session policy restricts role.
- SCP explicit deny.
- Resource policy rejects principal/service.
- KMS key policy/grant missing.

The error’s principal ARN tells which identity failed.

### IAM capabilities

If template creates/modifies IAM or expands macros, deployment may require:

- `CAPABILITY_IAM`
- `CAPABILITY_NAMED_IAM`
- `CAPABILITY_AUTO_EXPAND`

Acknowledging capability does not grant permission.

### `iam:PassRole`

Need when a caller tells a service to use an IAM role.

Check:

- Caller can pass that exact role ARN.
- `iam:PassedToService` condition permits target service where used.
- Role trust policy trusts target service.
- Role itself has needed permissions.

PassRole and role permissions are different gates.

### KMS deployment denial

Check:

- Correct key ARN/alias.
- Same expected Region/account.
- Key enabled and not pending deletion.
- Key policy permits principal/service.
- IAM permission/grant exists.
- Encryption context/conditions match.
- Cross-account copy/share policy exists.

Permission to create a resource does not imply permission to use its KMS key.

### Template and parameter failures

Common causes:

- YAML/JSON syntax.
- Unknown resource type/property.
- Wrong property data type.
- Missing required property.
- Invalid parameter value.
- Unsupported value in target Region/AZ/engine version.
- Bad `Ref`/`GetAtt` attribute.
- Circular dependency.
- Condition returns invalid property combination.
- Transform/macro or S3 template access failure.

`ValidateTemplate` checks template structure. It does not prove every service property can deploy.

Use change sets and linting/validation before execution.

### Resource already exists

CloudFormation cannot silently adopt a matching physical resource.

Choices:

- Use a different physical name.
- Import the supported existing resource into the stack.
- Reference it as an input instead of creating it.
- Remove it only if confirmed safe and authorized.

Never delete an unknown production resource only to clear the name.

### Immutable replacement problem

Some property changes require replacement.

Failure can occur because:

- Fixed physical name cannot coexist with replacement.
- New resource needs extra quota/IP/capacity.
- Deletion protection blocks old resource cleanup.
- Nonempty bucket/security/dependency blocks deletion.
- Data resource cannot be safely replaced.

Safe response:

```text
Review change set
  -> protect/snapshot state
  -> choose migration/new name/in-place supported change
  -> update references
  -> remove old only after validation.
```

### Subnet sizing

AWS reserves five IPv4 addresses in every subnet.

```text
Usable IPv4 addresses = total addresses - 5.
```

Example:

```text
/28 = 16 total -> 11 usable.
```

Subnet consumers can include:

- EC2 instances.
- Load-balancer nodes.
- RDS network interfaces.
- NAT gateways.
- VPC interface endpoints.
- Lambda VPC networking.
- ECS tasks using `awsvpc`.
- EKS nodes/pods with VPC CNI.
- EFS mount targets and other ENIs.

Count peak deployment and replacement capacity, not only steady state.

### Subnet failure clues

| Symptom | Check |
|---|---|
| `InsufficientFreeAddressesInSubnet` | Available IP count and ENIs |
| New ALB/RDS/ECS cannot launch | Free IPs in each required AZ subnet |
| Rolling deploy stalls | Old and new resources coexist; subnet lacks surge IPs |
| CIDR conflict | VPC/subnet/peering/TGW ranges overlap |
| Resource launches but no dependency access | Routes, NAT/endpoints, DNS, SG/NACL |

Fix choices:

- Use/add a larger non-overlapping subnet where service permits.
- Add subnets/AZs and update placement configuration.
- Remove only confirmed orphaned ENIs/resources.
- Reduce surge/concurrency if safe.
- Redesign IP allocation before exhaustion.

Subnet CIDR generally cannot simply be enlarged in place.

### Quota versus capacity

**Quota failure**

- Account/Region limit reached.
- Check Service Quotas/current usage.
- Request increase or reduce authorized use.

**Capacity failure**

- Requested resource/type unavailable in an AZ.
- Try another supported AZ/type/family or wait/retry if design allows.
- A quota increase does not create AZ capacity.

**Throttling**

- API rate temporarily exceeded.
- Use bounded retry with backoff/jitter.
- Do not treat permanent validation error as throttling.

### Region/AZ compatibility

Check:

- AMI exists in target Region.
- Instance type offered in target AZ.
- Service/feature/engine version supported in Region.
- KMS key and certificate are in correct Region.
- Parameter Store/Secrets Manager value exists in Region/account.
- Availability Zone names/IDs map correctly across accounts.

Hard-coded Region-specific IDs are a common failure.

### Private deployment network

Resource may create successfully but fail bootstrap/pull/register.

Needs a path to required services:

- S3 artifacts.
- ECR API/registry and S3 layers.
- Systems Manager endpoints.
- CloudWatch Logs/monitoring.
- Package repositories/licensing endpoints.
- Secrets Manager/Parameter Store/KMS.

Provide NAT/internet or correct VPC endpoints, DNS, routes, SGs, NACLs, and endpoint policies.

Control-plane success does not prove data-plane connectivity.

### EC2/Auto Scaling deployment issues

Evidence:

- Auto Scaling activity history.
- EC2 state transition/status checks.
- Launch-template version.
- AMI and architecture.
- User-data/cloud-init logs.
- Instance system log/console output.
- ELB target-health reason.

Common causes:

- Invalid AMI/instance type.
- Missing instance profile/PassRole.
- No subnet IP/AZ capacity.
- User data/package install failed.
- Target health path blocked or slow.

### ECS/EKS container deployment issues

Evidence:

- ECS service events/task stopped reason.
- EKS pod events/status/node state.
- ECR image/tag/digest.
- Pull/exec/health logs.
- Task execution role/node role.
- Cluster/subnet capacity.

Common causes:

- Image missing or access denied.
- ECR/NAT/VPC endpoint path missing.
- CPU architecture mismatch.
- Insufficient CPU/memory/IP capacity.
- Secret/KMS access denied.
- Load-balancer health check fails.

### Lambda deployment issues

Check:

- Package/image exists and format is supported.
- Execution role trust/permissions.
- Handler/runtime/architecture.
- Environment/KMS/secret access.
- VPC subnet IP and dependency path.
- Layer/version compatibility.
- Code/configuration quota.

Creation success does not prove invocation success; inspect function logs/errors.

### CDK/Service Catalog boundary

**CDK**

- `synth` failure: code/context/lookup.
- Asset publish failure: bootstrap S3/ECR/role/network.
- Stack deploy failure: inspect CloudFormation events.

**Service Catalog**

- Product unavailable: portfolio/share/principal/version.
- Launch denied: launch constraint role/PassRole.
- Provisioned-product failure: inspect underlying CloudFormation stack.

Always follow the tool into the underlying failing layer.

### Delete failure

Common causes:

- Termination/deletion protection.
- Nonempty S3 bucket/ECR repository.
- Resource still referenced/attached.
- Security group/network interface dependency.
- Snapshot/backup/retention/Vault Lock.
- Missing delete permission/KMS permission.

Do not force-delete state without retention and ownership review.

### Safe remediation path

```text
1. Stop blind retries/parallel changes.
2. Capture template, parameters, change set, events.
3. Find first failed logical resource.
4. Read exact service reason/principal.
5. Classify: config, IAM, KMS, quota, capacity, IP, network, runtime.
6. Preserve data/state.
7. Fix smallest root cause in code/configuration.
8. Preview replacement with change set/diff.
9. Resume rollback or redeploy.
10. Validate resources and application.
11. Check drift and update runbook.
```

### Retry decision

Retry can help:

- Throttling.
- Temporary service/AZ capacity issue.
- Dependency not ready yet.

Retry will not fix:

- Access denied.
- Invalid property.
- Missing capability.
- CIDR overlap.
- Exhausted fixed subnet.
- Duplicate name.
- Unsupported Region feature.

### Exam traps

- Final rollback event is usually not the root cause.
- Parent nested-stack failure may hide the child resource failure.
- `ROLLBACK_COMPLETE` after failed creation is not a normal updatable success state.
- `UPDATE_ROLLBACK_FAILED` needs blocker repair, then continue rollback.
- Skipping rollback resources can leave template/resource inconsistency.
- Caller permission, execution-role permission, and `PassRole` are separate.
- IAM capability acknowledgement does not grant IAM rights.
- KMS policy is separate from resource permission.
- `/28` gives 11 usable IPv4 addresses, not 16.
- Rolling replacement needs old + new capacity/IPs.
- Quota and AZ capacity are different failures.
- A created resource can still fail runtime bootstrap/network/health.
- Blind retry does not repair permanent configuration errors.
- Do not manually delete stateful resources merely to make rollback succeed.

### Do not memorize

- Every status enum.
- Every AWS error-string spelling.
- Exact default quota values.
- Every service log path.
- Console click paths.

### Ready when

Given a failed deployment, you can:

1. Find the first failed resource and underlying service evidence.
2. Separate caller, PassRole, execution role, resource policy, and KMS gates.
3. Diagnose subnet IP, quota, capacity, Region, and runtime-network failures.
4. Recover safely from rollback/delete/replacement problems.
5. Fix the smallest root cause, preview changes, redeploy, and verify.

---

## Skill 3.1.4 - Provision and share resources across Regions and accounts

**Official goal:** Centrally share supported resources or deploy consistent resources into many accounts and Regions.

### What exam tests

- Primary: `SEL CFG PRC GOV`
- Supporting: `DIA`
- Precision: `L2 - Object`
  - Know RAM share/resource/principal/permission and StackSet/stack instance/target/operation preference.

### Core selection

```text
One existing supported resource used by many accounts?
  -> AWS RAM.

Same infrastructure created separately in many accounts/Regions?
  -> CloudFormation StackSets.
```

RAM shares. StackSets deploys.

### Fast selection table

| Need | Choose |
|---|---|
| Workload accounts use central VPC subnets | AWS RAM |
| Share supported license/network/resource object | AWS RAM |
| Create IAM roles/config resources in every account | StackSets |
| Deploy standard baseline to every OU/Region | StackSets |
| Give another account API access to an S3 bucket | Resource/bucket policy |
| Give another account an independent AMI/image | Copy/Image Builder distribution |

Do not use StackSets just to share one live subnet. Do not use RAM to clone infrastructure.

### AWS RAM object model

```text
Resource owner
  -> resource share
       -> supported resource(s)
       -> principal(s)
       -> managed permission
  -> participant uses shared resource.
```

Exact objects:

- Resource share.
- Shared resource ARN.
- Principal.
- AWS RAM managed permission/version.
- Invitation where required.
- Owner account.
- Participant account.

### RAM principals

Depending on resource type and organization setup:

- AWS account.
- Organization.
- Organizational unit.
- IAM role/user where supported.
- Service principal where supported.

The target principal must be supported for that resource type.

### Organization sharing

With AWS Organizations integration:

```text
Enable sharing with Organizations
  -> RAM creates/uses service-linked integration
  -> shares to organization/OUs/accounts
  -> organization members normally avoid invitations.
```

Outside the organization:

- External sharing must be allowed.
- Invitation is sent where required.
- Recipient must accept before expiry.

Trusted access/organization membership is separate from ordinary IAM permission.

### RAM managed permissions

Managed permission defines what participant can do with the shared resource.

- AWS managed or customer managed where supported.
- Permission versions can change assigned behavior.
- Resource type decides available actions.
- Participant still needs identity/service-specific permission where required.

RAM permission is not a blanket administrator grant.

### RAM sharing behavior

- Owner keeps ownership and lifecycle control.
- Participant gets permitted use, not a copied resource.
- Resource remains in owner account/Region.
- Billing and modification rules depend on service.
- Unsharing does not mean “delete everything” universally; service-specific behavior applies.
- RAM does not replicate a resource across Regions.

### Shared VPC subnet model

```text
Networking account owns VPC/subnets
  -> shares subnets through RAM
  -> workload account launches supported resources there.
```

Owner controls:

- VPC/subnet/CIDR.
- Route tables.
- Internet/NAT gateways.
- Network ACLs.
- Shared network architecture.

Participant controls:

- Resources it creates in shared subnet.
- Its own supported security groups/resources.
- Workload configuration and IAM.

Participant cannot assume owner network paths are correct. Route/NAT/endpoint/DNS design remains owner-side.

### RAM sharing steps

```text
1. Confirm resource type supports RAM.
2. Confirm owner and Region.
3. Create resource share.
4. Add resource ARN(s).
5. Choose managed permission.
6. Add account/OU/organization principal.
7. Accept invitation if required.
8. Verify participant visibility and allowed action.
```

### RAM failure clues

| Symptom | First checks |
|---|---|
| Share not visible | Region, principal, invitation, organization membership |
| Cannot add resource | Unsupported type, not owner, wrong Region/state |
| OU share does not work | Organizations sharing/trusted integration and OU target |
| External account cannot accept | External sharing setting, invitation state/expiry |
| Resource visible but use denied | RAM managed permission, participant IAM/SCP, service policy |
| Shared subnet workload has no network | Owner route/NAT/endpoint/NACL/DNS configuration |
| Participant cannot modify owner object | Ownership/managed permission/service behavior; may be expected |

### StackSets object model

```text
StackSet
  -> template + parameters
  -> deployment targets: accounts/OUs
  -> Regions
  -> stack instances
       -> CloudFormation stack in each account/Region.
```

Exact objects:

- StackSet.
- Stack instance.
- Target account/OU.
- Target Region.
- Parameter override.
- Operation.
- Operation preferences.
- Permission model.
- Auto-deployment setting.
- Delegated administrator.

### StackSet versus stack instance

- StackSet: central definition and deployment policy.
- Stack instance: reference to one actual stack in one account and one Region.
- Underlying stack follows normal CloudFormation events/rollback.

Example:

```text
10 accounts x 3 Regions = up to 30 stack instances.
```

### Permission models

| Model | Best fit | Permission mechanism |
|---|---|---|
| Service-managed | AWS Organizations accounts/OUs | Trusted access/service-linked roles |
| Self-managed | Explicit accounts or no Organizations integration | Admin role + execution role |

### Service-managed StackSets

Needs:

- AWS Organizations.
- Trusted access enabled.
- Management account or registered delegated administrator.
- Target accounts/OUs.

Benefits:

- Deploy by OU.
- Auto-deploy to new accounts joining target OU.
- Remove/retain behavior when account leaves OU.
- AWS manages execution-role integration.

An SCP can still block deployed resource actions.

### Self-managed StackSets

```text
Administrator account role
  -> assumes execution role in target account
  -> creates/updates target stack.
```

Needs:

- Administration role and trust.
- Execution role in each target account.
- Execution role permission for template resources.
- `PassRole` and KMS/resource-policy access where required.
- Explicit target account IDs/Regions.

Wrong role name/trust is a common failure.

### Delegated administrator

- Registered member account manages service-managed StackSets.
- Management account still owns Organizations authority.
- Operations run in delegated-admin context.
- StackSets created in management and delegated-admin contexts have ownership/visibility boundaries.

Use the correct administrator context when a StackSet appears missing.

### Deployment targets

For service-managed permissions, select:

- Organization.
- OU(s).
- Account filter/inclusion/exclusion where supported.

For self-managed permissions, select explicit accounts.

Then choose Regions.

Each target account/Region must have:

- Service availability.
- Quota/capacity.
- Valid Region-specific parameters.
- Required permissions, keys, artifacts, and networking.

### Operation preferences

Control blast radius:

- Region order.
- Sequential or parallel Region behavior.
- Maximum concurrent accounts: count or percentage.
- Failure tolerance: count or percentage.
- Concurrency mode where configured.

Rule:

```text
Max concurrency = how many targets change together.
Failure tolerance = how many failures allowed before operation stops.
```

Failure tolerance is not automatic success or global rollback.

Each failed stack instance has its own CloudFormation evidence.

### Safe rollout pattern

```text
Canary OU/account + one Region
  -> validate
  -> low concurrency batch
  -> watch failures
  -> expand to more Regions/accounts.
```

Use small failure tolerance for sensitive baselines.

### Auto-deployment

Service-managed StackSet can automatically:

- Create stack instances for accounts added to targeted OUs.
- Delete stack instances when accounts leave, or retain stacks based on setting.

Auto-deployment affects OU membership changes. It does not mean every StackSet template update executes without an operation.

### Parameters and Region-specific values

- StackSet has default parameters.
- Stack instances can have parameter overrides.
- Overrides can differ by account/Region.
- New template parameters need compatible defaults/overrides.

Common Region-specific values:

- AMI ID.
- KMS key ARN.
- ACM certificate.
- Subnet/VPC ID.
- S3 artifact bucket.
- Service endpoint/feature.

Use mappings, SSM parameters, or explicit overrides. Do not hard-code one Region’s IDs everywhere.

### StackSet updates

```text
Update StackSet template/parameters
  -> choose target stack instances
  -> set operation preferences
  -> operation updates underlying stacks.
```

Review:

- Replacement/data risk.
- Permission model.
- Target scope.
- Parameter overrides.
- Region order/concurrency/tolerance.

A central mistake can fan out widely.

### Retain versus delete

When removing stack instances:

- Delete stacks/resources according to CloudFormation policies, or
- Retain stacks/resources in target accounts.

Retained stacks stop being managed by that StackSet.

Delete stack instances before deleting the StackSet definition.

Stateful resources still need DeletionPolicy/UpdateReplacePolicy review.

### StackSet drift

- Drift detection compares target stacks/resources with expected StackSet configuration where supported.
- One account may drift while others remain correct.
- Drift detection reports; it does not automatically repair.
- Retained stacks are outside future StackSet control.

Fix through a reviewed StackSet operation or controlled reconciliation.

### StackSet failure clues

| Symptom | First checks |
|---|---|
| Operation stops early | Failure tolerance and first failed stack instance |
| All self-managed targets fail | Admin/execution role name, trust, permissions |
| One account fails | SCP, quota, parameter, existing resource, local policy |
| One Region fails | Service support, AMI/KMS/certificate/artifact, capacity |
| New OU account has no stack | Auto-deployment, OU target, trusted access |
| Stack exists but StackSet says OUTDATED | Update operation/target/override failed or not run |
| StackSet missing | Wrong administrator account/delegated-admin context or Region |
| Retained stack no longer updates | Expected: no longer a managed stack instance |

### Cross-account/Region security

Check all layers:

```text
Organizations/SCP
  + administrator permission
  + execution role/trust
  + service IAM
  + resource policy
  + KMS key policy
  + target Region/account artifact access.
```

No single sharing mechanism overrides an explicit deny.

### Evidence

**RAM**

- Resource-share status.
- Associated resource/principal/permission.
- Invitation status.
- Organizations-sharing setting.
- Participant service error and CloudTrail.

**StackSets**

- StackSet permission model/status.
- Operation status and preferences.
- Stack-instance status/reason.
- Underlying target stack events.
- Administrator/execution-role CloudTrail events.
- Drift results.

### Safe operating path

```text
Choose share versus deploy
  -> define ownership and principals/targets
  -> test one account/Region
  -> validate permissions and service behavior
  -> expand with controlled concurrency
  -> monitor failures/drift
  -> remove or retain deliberately.
```

### Exam traps

- RAM shares an existing resource; it does not copy it.
- StackSets creates/manages separate stacks in target accounts/Regions.
- RAM share permission does not bypass participant IAM/SCP/service rules.
- Organization members often avoid invitations; external principals may need acceptance.
- VPC owner controls shared-subnet routing/NAT/NACL architecture.
- Service-managed and self-managed StackSets use different role models.
- Stack instance means one account + one Region.
- Maximum concurrency and failure tolerance are different.
- Failure tolerance does not roll back every successful target.
- Hard-coded AMI/KMS/certificate IDs can fail across Regions.
- Retained stack is no longer managed by the StackSet.
- StackSets do not replicate application data or image artifacts automatically.

### Do not memorize

- Every RAM-supported resource type.
- Exact default operation-preference values.
- Every StackSet status enum.
- Exact service-linked role names.
- Console click paths.

### Ready when

Given a multi-account/Region scenario, you can:

1. Choose RAM sharing, StackSets deployment, resource policy, or artifact copy.
2. Configure RAM resources, principals, permissions, and invitations.
3. Choose service-managed versus self-managed StackSets.
4. Set targets, Regions, parameters, concurrency, and failure tolerance.
5. Diagnose one-account, one-Region, role, OU, and drift failures.

---

## Skill 3.1.5 - Implement deployment strategies and services

**Official goal:** Release a new application/infrastructure version with acceptable downtime, risk, capacity, and rollback speed.

### What exam tests

- Primary: `SEL CFG BEH PRC OPT`
- Supporting: `EVD REM`
- Precision: `L2 - Object`
  - Know old/new capacity, batch/traffic size, health signal, bake time, version reference, and rollback object.

### Core model

Every deployment answers:

```text
How much changes at once?
Do old and new run together?
How is traffic moved?
What proves health?
How do we roll back?
```

### Strategy comparison

| Strategy | Old/new behavior | Cost | Risk/downtime |
|---|---|---|---|
| In-place/all-at-once | Change existing whole fleet | Lowest extra | Highest blast/downtime risk |
| Rolling | Replace small batches | Low-medium | Mixed versions; capacity can dip |
| Immutable | Build new fleet; remove old after validation | Higher temporary | Strong isolation; slower/costlier |
| Blue/green | Two full environments; switch traffic | High temporary | Fast switch/rollback |
| Canary | Small traffic percent to new version first | Medium | Small initial blast radius |
| Linear | Increase new-version traffic in fixed steps | Medium | Gradual exposure |

### Fast exam clues

| Wording | Choose |
|---|---|
| Fastest, no spare capacity, downtime accepted | All-at-once/in-place |
| Replace a few instances/tasks at a time | Rolling |
| Never modify old instances; create new ones | Immutable |
| Complete green environment, then traffic switch | Blue/green |
| Send 5% first, watch, then continue | Canary |
| Add 10% every 10 minutes | Linear |

### In-place/all-at-once

```text
Existing fleet
  -> change every resource
  -> same fleet runs new version.
```

Benefits:

- Fast.
- Little duplicate capacity.
- Simple for noncritical environments.

Risks:

- Whole fleet can fail together.
- Downtime likely if service stops/restarts.
- Old state may be overwritten.
- Rollback can require another full deployment.

Use only when interruption and blast radius are acceptable.

### Rolling

```text
Old fleet
  -> replace batch 1
  -> validate
  -> replace batch 2
  -> continue until new fleet.
```

Properties:

- Batch size/percentage.
- Minimum healthy capacity.
- Maximum/surge capacity.
- Warmup/readiness time.
- Pause/checkpoint/bake time.
- Health failure threshold/rollback.

Trade-offs:

- Smaller batch: safer, slower.
- Larger batch: faster, larger blast.
- No surge: capacity may drop.
- Surge capacity: old + new coexist, needs quota/IP/cost.

Old and new versions must work together during rollout.

### Immutable

```text
Create entirely new resources from versioned artifact
  -> test new fleet
  -> move traffic/attach
  -> terminate old fleet later.
```

Benefits:

- Old fleet remains unchanged.
- Consistent clean instances/tasks.
- Easy infrastructure rollback while old fleet exists.

Costs:

- Temporary duplicate capacity.
- More IP/quota/startup time.
- Data/schema compatibility still required.

Immutable compute does not make the database immutable.

### Blue/green

```text
Blue = current production
Green = complete new environment

Validate green
  -> switch traffic blue to green
  -> keep blue for rollback window.
```

Best when:

- Fast traffic rollback required.
- Full pre-production validation needed.
- Duplicate environment cost accepted.

Need:

- Two target groups/environments where applicable.
- Traffic switch control.
- Health/readiness checks.
- Session/connection draining.
- Compatible shared data/schema.
- Clear cleanup time.

Rollback is fast only while blue remains valid and data-compatible.

### Canary

```text
Most traffic -> old version
Small percent -> new version
  -> observe
  -> increase or roll back.
```

Use to limit initial blast radius.

Needs:

- Representative traffic.
- Enough requests during observation.
- Version-specific metrics/logs.
- Alarm and stop/rollback criteria.
- Bake time long enough to expose slow failures.

A canary that receives no meaningful traffic proves little.

### Linear

```text
10% new
  -> wait
  -> 20%
  -> wait
  -> ...
  -> 100%.
```

Difference:

- Canary emphasizes a small initial test, then may jump.
- Linear shifts fixed increments on a schedule.

Both need health gates and rollback.

### Strategy versus traffic pattern

These can combine:

- Green environment can receive canary traffic before full blue/green switch.
- Immutable fleet can be introduced through rolling batches.
- ECS/Lambda can use progressive traffic against immutable versions.

Question asks for the dominant operational behavior.

### EC2 Auto Scaling instance refresh

```text
New launch-template version/desired configuration
  -> instance refresh
  -> replace nonmatching instances
  -> warm/health check
  -> continue or roll back.
```

Exact objects/settings:

- Launch template and version.
- Auto Scaling group desired configuration.
- Minimum healthy percentage.
- Maximum healthy percentage/surge.
- Instance warmup.
- Checkpoints and checkpoint delay where used.
- Skip matching.
- Auto rollback.
- Bake time/CloudWatch alarm preferences where configured.

### Instance refresh behavior

- Uses new instances; does not patch old ones in place.
- Replacement rate follows min/max healthy settings.
- Skip matching avoids replacing instances already on desired configuration.
- Scale-in protection/standby/unhealthy behavior can block or alter replacement.
- New instances must pass EC2/ELB health after warmup.

Rollback needs a known good previous launch-template/configuration.

### Instance refresh failure clues

| Symptom | First checks |
|---|---|
| Refresh will not start | Another refresh/update, invalid desired config |
| Progress stops | Health failures, protected/standby instance, min healthy constraint |
| New instances fail | AMI, user data, instance profile, subnet IP, capacity, target health |
| Refresh too slow | Warmup, checkpoints, batch size, capacity launch time |
| Rollback unavailable/fails | Previous config missing/invalid or new launches still fail |
| Too many instances replaced | Skip matching/configuration comparison |

### CloudFormation Auto Scaling updates

CloudFormation can control ASG update behavior through update policies.

Recognize:

- Rolling update settings.
- Replacing update/immutable-style behavior.
- Minimum instances in service.
- Maximum batch size.
- Pause time/resource signals.

Change set shows resource action. Update policy controls replacement rollout behavior.

### ECS rolling deployment

```text
New task-definition revision
  -> service starts new tasks
  -> new tasks become healthy
  -> old tasks drain/stop.
```

Exact objects/settings:

- ECS service.
- Task-definition revision/image digest.
- Desired count.
- `minimumHealthyPercent`.
- `maximumPercent`.
- Deployment circuit breaker/rollback.
- Deployment alarms where configured.
- Target-group health check.
- Capacity provider/cluster capacity.
- Health-check grace period.

`minimumHealthyPercent` controls how low healthy running tasks may go.

`maximumPercent` controls temporary old + new task count.

### ECS rolling clues

```text
Desired count 10
minimum healthy 50%
maximum 200%
  -> scheduler has room to stop/start in batches
  -> may run up to 20 tasks temporarily.
```

Actual ordering depends on capacity and scheduler decisions.

Need enough:

- CPU/memory.
- ENI/subnet IPs.
- Container-instance/Fargate capacity.
- Target-group registration capacity.

### ECS deployment failure clues

| Symptom | First checks |
|---|---|
| New tasks never start | Capacity, IPs, task definition, image, role, secrets |
| Tasks start then stop | Container exit reason/logs, architecture, health |
| Tasks run but stay unhealthy | Port mapping, health path, SG, startup time |
| Deployment stalls | Min/max percentages leave no room, no cluster capacity |
| Circuit breaker rolls back | Service could not reach steady state |
| Old tasks never drain | Connections, deregistration delay, deployment state |

### ECS blue/green

```text
Blue task set/target group
Green task set/target group
  -> test green
  -> shift production listener traffic
  -> retain blue briefly for rollback.
```

Know at operational level:

- Separate task sets/target groups.
- Test and production traffic paths where configured.
- Traffic-shift configuration.
- Termination wait/rollback window.
- Alarms and health gates.

Do not need to design a full CI/CD pipeline.

### Lambda versions and aliases

```text
$LATEST
  -> publish immutable version 12
  -> alias prod points to version 12.
```

Objects:

- `$LATEST`: mutable working version.
- Published numbered version: immutable code/config snapshot.
- Alias: stable name pointing to a version.
- Alias routing configuration: optional weight to a second version.

Applications invoke alias ARN. Deployment moves alias traffic, not client configuration.

### Lambda canary/linear

```text
Alias prod
  -> 90% version 11
  -> 10% version 12
```

Watch per-version/alias:

- Errors.
- Duration/latency.
- Throttles.
- Concurrency.
- Logs/traces.
- Business result.

Rollback:

```text
Set alias weight back to known good version.
```

Alias rollback does not undo database writes or schema changes.

### CloudFormation and image-pipeline boundary

- Image Builder creates tested AMI/container artifacts.
- Launch template/task definition/Lambda version references artifact.
- CloudFormation change set previews infrastructure update.
- Stack rollback restores supported prior infrastructure state.

Neither automatically proves application health unless health/alarm controls are connected.

### Deployment health signals

Use more than “resource exists.”

| Layer | Evidence |
|---|---|
| Infrastructure | Create/start success, capacity, status checks |
| Traffic | Healthy targets, 4xx/5xx, resets, response time |
| Application | Error rate, latency, logs, traces |
| Dependency | DB connections/throttling, queue age, downstream failures |
| Business | Successful checkout/job/result, not only HTTP 200 |

Compare old and new versions during progressive rollout.

### Alarm and rollback controls

Define before deployment:

- Metric and dimension/version.
- Threshold and evaluation period.
- Missing-data behavior.
- Bake/observation time.
- Stop versus automatic rollback.
- Rollback artifact/configuration.

Bad alarm:

```text
Measures whole service
  -> small canary failures hidden by healthy old version.
```

Prefer version/target-specific evidence where possible.

### Readiness versus liveness

- Liveness: process is alive.
- Readiness: process is ready to receive real traffic.

New deployment should not receive production traffic before readiness.

Health endpoint should test enough critical dependencies without becoming slow/fragile.

### Connection and session behavior

During replacement:

- Deregister/drain old target.
- Allow in-flight requests to finish.
- Externalize session state if users can move between versions.
- Keep old/new APIs compatible during overlap.
- Expect long-lived connections to delay complete cutover.

Traffic weight changes do not instantly move existing connections.

### Database/schema compatibility

Safest pattern:

```text
1. Add backward-compatible schema.
2. Deploy code that works with old + new schema.
3. Shift traffic and validate.
4. Remove old code.
5. Remove obsolete schema later.
```

Avoid destructive schema change before old version is gone.

Infrastructure rollback cannot automatically reverse data changes.

### Rollback readiness

Keep:

- Previous AMI ID.
- Previous launch-template version.
- Previous task-definition revision and ECR digest.
- Previous Lambda version.
- Previous configuration/secret schema compatibility.
- Blue environment until rollback window ends.

Test rollback path before deleting old artifacts.

### Safe deployment path

```text
Choose strategy from risk/downtime/capacity
  -> pin immutable artifact
  -> define health and rollback
  -> verify surge IP/quota/capacity
  -> deploy smallest exposure
  -> bake and compare evidence
  -> continue or roll back
  -> drain old version
  -> validate full service
  -> retire old artifact later.
```

### Failure clues

| Symptom | First checks |
|---|---|
| Deployment causes outage | Strategy blast radius, min healthy, readiness, capacity |
| Rolling deploy freezes | No surge capacity/IPs, health failure, percentage constraints |
| Canary looks healthy but users fail later | Too little traffic/bake time or wrong metric |
| Blue/green switch fails | Listener/target group/health/config/data compatibility |
| Rollback restores compute but not service | Schema/data/config changed incompatibly |
| New fleet healthy but old still serves | Traffic weight/listener/alias and long connections |
| Cost remains high | Old/blue resources not retired after rollback window |
| Scale-out pulls missing image | Lifecycle deleted rollback/deployed digest |

### Exam traps

- Rolling deployment can run mixed versions.
- Rolling is not automatically zero downtime.
- Immutable means new compute; shared data can still change.
- Blue/green describes environments; canary/linear describes progressive exposure.
- Smaller batches reduce blast but increase deployment time.
- Min healthy and max capacity solve different constraints.
- Health check pass does not prove business correctness.
- Bake time must be long enough and receive representative traffic.
- Lambda alias points to published versions; `$LATEST` is mutable.
- Traffic rollback does not undo database/data mutations.
- Existing connections may not follow a traffic-weight change immediately.
- Deleting old images/versions too early removes rollback and scale-out ability.

### Do not memorize

- One universal batch percentage.
- Exact deployment times.
- Full CI/CD pipeline design; it is out of exam scope.
- Every ECS deployment-controller field.
- Console click paths.

### Ready when

Given a deployment scenario, you can:

1. Choose all-at-once, rolling, immutable, blue/green, canary, or linear.
2. Predict old/new capacity, mixed-version, downtime, and cost behavior.
3. Configure ASG refresh, ECS deployment, or Lambda alias traffic controls.
4. Select version-specific health, alarm, bake, and rollback evidence.
5. Preserve data compatibility and a tested rollback artifact.

---

## Skill 3.1.6 - Use and manage third-party deployment tools

**Official goal:** Safely operate Terraform and Git-based infrastructure deployment workflows.

### What exam tests

- Primary: `CFG BEH DIA PRC`
- Supporting: `GOV`
- Precision: `L2 - Object`
  - Know Terraform configuration/state/backend/lock/plan and Git commit/branch/tag/merge/secret boundaries.

### Core Terraform model

```text
Configuration = desired resources.
State         = Terraform's mapping/known attributes.
AWS           = real resources.

plan compares all three.
```

If they disagree, diagnose before apply.

### Terraform workflow

```text
terraform init
  -> terraform fmt/validate
  -> terraform plan
  -> review actions
  -> terraform apply
  -> verify AWS/application
  -> store state safely.
```

`destroy` is a deliberate destructive operation, not routine cleanup.

### Terraform configuration objects

| Object | Use |
|---|---|
| `terraform` block | Required versions/backends/settings |
| Provider | Connects Terraform to AWS/service API |
| Resource | Object Terraform creates/manages |
| Data source | Reads existing information; does not own it |
| Variable | Input value |
| Local | Computed reusable expression |
| Output | Exposed result |
| Module | Reusable group of configuration |
| Lifecycle | Resource update/destroy behavior controls |

### Resource address

```text
aws_instance.web
module.network.aws_subnet.private[0]
```

State maps resource address to physical AWS resource ID.

Changing an address without a move/import can make Terraform think:

```text
old object removed + new object required.
```

### Provider

Provider configuration can include:

- Region.
- Credentials/assume-role path.
- Aliases for multiple accounts/Regions.
- Default tags/settings.
- Version constraint.

Provider lock file records selected provider builds.

Common failure:

```text
Correct code + wrong provider account/Region
  -> plan targets wrong environment.
```

Always verify caller identity, account, Region, and workspace/backend.

### `terraform init`

Init prepares:

- Backend.
- Providers/plugins.
- Modules.
- Dependency lock information.

Run after cloning or changing backend/provider/module requirements.

Init failure directions:

- Backend credentials/network.
- Provider registry/network.
- Invalid version constraint.
- Missing module source/access.
- Backend configuration mismatch/migration prompt.

Init does not create normal declared infrastructure.

### Validate versus plan

**`terraform fmt`**

- Normalizes source formatting.

**`terraform validate`**

- Checks configuration syntax/internal consistency.
- Does not prove AWS permission, quota, or capacity.

**`terraform plan`**

- Refreshes/reads relevant real state by default.
- Calculates proposed actions.
- Does not normally execute those infrastructure changes.

Plan is the deployment preview.

### Plan action symbols

| Symbol | Meaning |
|---|---|
| `+` | Create |
| `~` | Update in place |
| `-` | Destroy |
| `-/+` | Destroy then create replacement |
| `+/-` | Create replacement then destroy old where lifecycle allows |
| `<=` | Read data source |

Exact display can vary, but replacement/destruction must be recognized.

### Review a plan

Check:

- Correct account/Region/workspace.
- Unexpected creates/deletes.
- Replacement of stateful resource.
- Physical-name/endpoint change.
- Security/IAM/network exposure.
- Capacity/quota/IP surge.
- Sensitive values.
- Output/dependency change.

Use a saved plan when the workflow requires applying exactly the reviewed actions.

Plan can become stale if AWS, state, variables, or configuration changes before apply.

### Apply behavior

```text
terraform apply reviewed plan
  -> acquires state lock where backend supports it
  -> calls provider APIs in dependency order
  -> records successful results in state
  -> releases lock.
```

An apply can partially succeed.

- Successful AWS resources may remain.
- State may contain completed operations.
- Read error and run a new plan before retry.
- Do not assume automatic global rollback.

### State

State contains:

- Resource addresses and physical IDs.
- Attributes and dependencies.
- Provider/schema data.
- Output values.
- Potentially sensitive values.

State is operationally sensitive even when source code contains no secret.

Protect it with:

- Remote durable backend.
- Encryption.
- Least-privilege access.
- Versioning/backups.
- Locking.
- Audit logging.

Do not commit state to Git.

### Backend

Backend controls where state lives and how operations coordinate.

```text
Local backend
  -> state on operator machine.

Remote backend
  -> shared protected state for team/automation.
```

Remote backend is preferred for shared production workflows.

Backend authentication can differ from AWS provider authentication.

Example failure:

```text
Can read state backend
but cannot create AWS resource,
or reverse.
```

### State locking

Lock prevents two writers from changing the same state together.

```text
Pipeline A holds lock
  -> Pipeline B must wait/fail.
```

If lock remains:

1. Confirm no operation is running.
2. Identify lock owner/operation.
3. Recover the failed process if possible.
4. Force-unlock only with verified stale lock and correct lock ID.

Removing a live lock can corrupt state or create duplicate changes.

### Dependencies

```text
resource references another resource attribute
  -> implicit dependency.
```

Use `depends_on` only for dependency not visible through data references.

Terraform can create independent resources in parallel.

Dependency order does not guarantee application readiness unless provider/resource checks model it.

### Variables and outputs

Variables can come from:

- Defaults.
- Variable files.
- Environment variables.
- CLI/automation inputs.

Check which value reaches the plan.

Marking variable/output `sensitive` hides normal display. It does not remove value from state or encrypt it.

Never put credentials in committed `.tfvars` files.

### Modules

Module call passes inputs and reads outputs.

Need:

- Trusted source.
- Pinned/reviewed version.
- Compatible provider requirements.
- Clear ownership and output interface.

Updating module version can change many resources. Review full plan.

### Lifecycle controls

Recognition:

- `create_before_destroy`: create replacement first where possible.
- `prevent_destroy`: reject planned destruction while configured.
- `ignore_changes`: ignore selected drift for update planning.

Traps:

- `create_before_destroy` needs duplicate name/quota/IP capacity.
- `prevent_destroy` is configuration safety, not IAM protection.
- `ignore_changes` can hide meaningful drift.

### Drift

```text
Someone changes AWS outside Terraform
  -> configuration/state/reality differ
  -> next plan shows drift-driven action.
```

Choices:

- Revert AWS to code through reviewed apply.
- Update code to accept intentional change.
- Import/move ownership correctly.

Do not edit state merely to hide the difference.

### Import

```text
Existing AWS resource
  -> map to Terraform resource address/state
  -> create/review matching configuration
  -> plan until no unintended change.
```

Import does not automatically guarantee configuration matches reality.

After import, next plan may propose changes or replacement.

### State commands

Recognition:

- `state list/show`: inspect managed objects.
- `state mv`: move address/ownership inside state.
- `state rm`: stop tracking without deleting AWS object.
- `import`: begin managing existing AWS object.

These are powerful state surgery. Back up state and review exact address first.

`state rm` does not delete the cloud resource; later configuration can try to create a duplicate.

### Workspaces

Workspace selects a separate state for the same configuration.

```text
same code
  -> dev workspace state
  -> prod workspace state.
```

Workspace is not:

- A Git branch.
- An AWS account security boundary.
- Automatic variable isolation.

Always confirm workspace before plan/apply.

### Terraform failure clues

| Symptom | First checks |
|---|---|
| No changes but wrong environment | Backend/workspace/provider account/Region |
| Provider cannot authenticate | Credential chain, assume role, trust, expiry, clock |
| Init cannot download provider | Network/proxy/registry/version constraint |
| State access denied | Backend identity/policy/KMS, not only provider role |
| State lock error | Active run versus verified stale lock |
| Plan wants duplicate resource | Lost/wrong state, address change, import needed |
| Plan wants unexpected destroy/replace | Config/address/module/provider change and lifecycle |
| Apply AccessDenied | Failing provider principal, IAM/SCP/resource/KMS policy |
| Apply partly fails | Read exact resource error, preserve successes, re-plan |
| Imported resource changes immediately | Configuration does not match actual resource |
| Quota/subnet/capacity error | Same AWS service evidence as any deployment |

### Git object model

```text
Working tree
  -> stage/index
  -> commit
  -> branch points to commit
  -> tag names a release commit
  -> remote stores shared references.
```

Exact objects:

- Repository.
- Commit/hash.
- Branch.
- Tag.
- Remote.
- Pull/merge request.
- Merge conflict.
- `.gitignore`.

### Git operations

| Operation | Meaning |
|---|---|
| Clone | Create local repository from remote |
| Fetch | Download remote objects/references; no working merge |
| Pull | Fetch then integrate into current branch |
| Commit | Record staged snapshot locally |
| Push | Publish local commits/references |
| Merge | Combine branch histories |
| Tag | Name a specific commit/release |

Commit is immutable history. Branch name moves as new commits arrive.

Pin deployments to reviewed commit/tag/artifact digest, not an uncontrolled moving branch alone.

### Branch and review workflow

```text
Create branch
  -> edit IaC
  -> fmt/validate/plan
  -> commit
  -> pull request/review
  -> merge
  -> deploy reviewed commit/plan
  -> tag release where used.
```

Review should include generated Terraform plan and ownership/security impact.

### Merge conflicts

Conflict means Git cannot automatically combine changes.

Safe path:

```text
Read both versions
  -> understand intended infrastructure
  -> resolve file deliberately
  -> validate/plan again
  -> commit resolution.
```

Never choose “ours” or “theirs” blindly for IaC or state references.

A text-clean merge can still produce an unsafe Terraform plan.

### Git and secrets

Never commit:

- AWS access keys/session tokens.
- Private keys.
- Passwords/API tokens.
- Terraform state/backup state.
- Saved plan files if they contain sensitive data.
- Secret-bearing variable files.

`.gitignore` prevents new untracked files from being added by normal commands.

It does not:

- Remove a secret already committed.
- Erase Git history.
- Rotate exposed credential.

If secret was committed:

```text
Revoke/rotate immediately
  -> assess use/exposure
  -> remove from current code
  -> clean history under controlled process if required.
```

Rotation is first; history cleanup alone is not enough.

### Common Terraform Git hygiene

Usually commit:

- `.tf` source.
- Module source.
- Provider dependency lock file.
- Documentation/tests.

Usually exclude:

- `.terraform/` working directory.
- `*.tfstate` and backups.
- Crash logs.
- Sensitive variable files.
- Saved plans with sensitive content.

Follow repository policy; never treat ignore rules as secret protection.

### Ownership boundary

Bad pattern:

```text
Terraform manages resource
  + CloudFormation manages same resource
  + human edits it manually
  -> tools fight and drift repeats.
```

Define one owner per resource/property.

Valid boundaries can be:

- Terraform manages VPC; CloudFormation consumes subnet IDs.
- CloudFormation manages application stack; Terraform does not declare those resources.
- Shared resource accessed through data source/output, not managed twice.

Data source/reference is not ownership.

### Safe operating path

```text
Verify repository commit
  -> verify backend/workspace/account/Region
  -> init/validate
  -> acquire clean state/lock
  -> plan
  -> review destroy/replace/security
  -> apply reviewed change
  -> verify AWS/application
  -> commit/tag evidence and protect state.
```

### Exam traps

- Configuration, state, and real AWS resources are three different things.
- Plan is a preview; apply changes infrastructure.
- Apply can partially succeed; Terraform has no universal rollback.
- State can contain secrets even when marked sensitive.
- Backend credentials and AWS provider credentials can differ.
- Never force-unlock until the lock is proven stale.
- `prevent_destroy` is not an IAM control.
- `ignore_changes` can hide drift.
- Import attaches an existing resource; next plan may still change it.
- Workspace is separate state, not a Git branch or security boundary.
- Git branch moves; commit hash/tag identifies a release.
- `.gitignore` does not remove committed secrets.
- Terraform and CloudFormation should not both own the same resource.

### Do not memorize

- Every Terraform CLI flag.
- HCL syntax for every resource.
- Git internals/rebase algorithms.
- One mandatory branching model.
- Specific third-party vendor pipeline design.
- Console click paths.

### Ready when

Given a third-party deployment scenario, you can:

1. Explain configuration -> state -> AWS comparison.
2. Safely run init -> validate -> plan -> apply.
3. Protect/lock remote state and diagnose auth, drift, import, and partial apply.
4. Read Git branch/commit/tag/merge behavior and handle conflicts.
5. Keep secrets/state out of Git and enforce one tool owner per resource.

---

## Skill 3.2.1 - Automate operational processes with AWS services

**Official goal:** Use Systems Manager and related AWS controls to operate existing resources safely at fleet scale.

### What exam tests

- Primary: `SEL CFG PRC DIA REM`
- Supporting: `EVD GOV`
- Precision: `L2 - Object`
  - Know managed-node prerequisites, document/association/baseline/window/session objects, targeting, rate limits, status, and output.

### Core selection

| Need | Choose |
|---|---|
| Run command now on many nodes | Run Command |
| Keep/schedule node configuration | State Manager |
| Multi-step AWS/resource workflow | Automation runbook |
| Scan/install operating-system patches | Patch Manager |
| Schedule controlled operational task | Maintenance Windows |
| Interactive node access without inbound SSH/RDP | Session Manager |
| GUI-based node administration | Fleet Manager |
| Collect software/config metadata | Inventory |
| Store hierarchical configuration/value | Parameter Store |

### Managed-node foundation

```text
Supported machine
  + running SSM Agent
  + IAM/activation identity
  + network/DNS path to Systems Manager
  + correct Region/time
  = managed node online.
```

If this foundation fails, most Systems Manager features fail together.

### Managed-node types

- EC2 instance.
- On-premises server/VM through hybrid activation.
- Other supported machine types registered through Systems Manager.

The node receives a managed-node ID and reports to one Region/account context.

### SSM Agent

Agent:

- Registers/reports node information.
- Polls/receives Systems Manager work.
- Runs documents locally.
- Sends status/output.

Check:

- Installed and supported.
- Service/process running.
- Version compatible/current enough.
- Correct Region/proxy configuration.
- Local clock and certificate/TLS path.
- Agent logs.

Agent running alone does not prove IAM or network works.

### EC2 IAM path

EC2 commonly needs an instance profile role with permissions equivalent to the Systems Manager managed-node core actions.

```text
EC2 instance
  -> instance profile role
  -> Systems Manager messaging/API.
```

Check:

- Instance profile attached.
- Role trust permits EC2.
- Role policy has required SSM/message actions.
- SCP/permissions boundary does not deny.
- Instance can obtain role credentials from metadata.

Human operator permission is separate from node permission.

### Hybrid activation

For on-premises/other hybrid nodes:

```text
Create activation
  -> activation code + ID
  -> register SSM Agent
  -> node uses configured service role
  -> appears as managed node.
```

Check activation expiry/registration limit, role, Region, network, and duplicate/old registration.

Do not embed reusable activation credentials in public images/scripts.

### Systems Manager network path

Node needs outbound HTTPS/DNS to required endpoints.

Private VPC choices:

- NAT/internet egress, or
- VPC interface endpoints for Systems Manager messaging services.

Common endpoints to recognize:

- `ssm`
- `ssmmessages`
- `ec2messages` where relevant

Tasks can also need:

- S3 for scripts/packages/output.
- CloudWatch Logs.
- KMS.
- Package repositories.
- Secrets Manager/Parameter Store.

Endpoint security groups, private DNS, endpoint policies, routes, NACLs, and local proxy/firewall still matter.

### Managed node offline checklist

```text
1. Agent installed/running?
2. Correct Region/account/registration?
3. Instance profile or activation role valid?
4. Credentials/metadata/time valid?
5. DNS and HTTPS path to SSM endpoints?
6. Endpoint policy/SG/NACL/proxy/firewall?
7. Read agent logs.
```

“Instance is running” does not mean “managed node is online.”

### Systems Manager documents

Document defines work.

Common document types:

- Command document.
- Automation runbook.
- Session document.
- Package/policy-related documents where used.

Exact properties:

- Document name/version.
- Document type.
- Parameters.
- Platform type.
- Steps/plugins/actions.
- Owner/sharing permissions.

Use trusted/pinned document version for controlled operations.

### Run Command

```text
Command document + parameters
  -> targets
  -> rate controls
  -> node command invocations
  -> status/output.
```

Use for noninteractive commands/scripts across nodes.

Exact controls:

- Document and version.
- Targets: IDs, tags, resource groups.
- Parameters.
- Command timeout.
- `MaxConcurrency`.
- `MaxErrors`.
- S3/CloudWatch output where configured.
- SNS/EventBridge notification where configured.
- Service role where required.

### Run Command rate controls

```text
MaxConcurrency = how many targets run together.
MaxErrors      = error threshold before sending stops to more targets.
```

Can be count or percentage.

Important:

- Already running invocations may continue after error threshold.
- Rate control limits blast radius; it is not rollback.
- Small concurrency is safer but slower.

### Run Command statuses

Recognize:

- Pending/delayed.
- In progress.
- Success.
- Failed.
- Timed out.
- Cancelled.
- Undeliverable/terminated where applicable.

Overall command status and each node invocation can differ. Inspect failed plugin/output on the specific node.

### Run Command failure clues

| Symptom | First checks |
|---|---|
| Target not listed | Managed-node status, Region/account, tag/resource-group match |
| Pending/undeliverable | Agent/message path/node offline |
| Delivery timeout | Node did not receive before delivery window |
| Execution timeout | Script/plugin exceeded runtime timeout |
| Command failed on one OS | Document platform/plugin/command syntax |
| Access denied inside script | Local OS user/permissions or AWS role permission |
| No central output | S3/Logs config, node role, bucket/log/KMS policy |
| Too many nodes changed | Target/rate control was too broad |

Success means command process succeeded as defined. It does not automatically prove application result.

### State Manager

```text
Association
  -> document + parameters
  -> targets
  -> schedule/change trigger
  -> apply desired state
  -> association compliance.
```

Use for recurring or continuously enforced node configuration.

Exact objects:

- Association.
- Document/version.
- Targets.
- Parameters.
- Schedule.
- Compliance severity.
- Output location.
- Concurrency/error controls where configured.

Run Command is operator execution. State Manager is desired configuration/association.

### State Manager failure clues

- Association targets wrong/missing tag.
- Node offline during schedule.
- Document version/platform mismatch.
- Local command/package fails.
- Association succeeds but configuration later drifts.
- Compliance data is stale because node no longer reports.

Read association execution history and per-node output.

### Automation runbooks

Use for multi-step AWS API/resource workflows.

```text
Runbook
  -> steps/actions
  -> assume role
  -> branches/waits/approvals
  -> outputs/rollback path.
```

Key distinction:

- Run Command runs commands on managed nodes.
- Automation orchestrates AWS actions and can call Run Command.

Runbook detail was covered in Skill 1.2.3.

### Patch Manager object model

```text
Patch baseline
  -> approval/rejection rules
  -> patch group/targets
  -> scan or install operation
  -> patch compliance.
```

Exact objects/settings:

- Patch baseline.
- Operating system/product/classification/severity.
- Approval rules/delay.
- Approved/rejected patches.
- Patch group mapping.
- `AWS-RunPatchBaseline` document.
- `Scan` versus `Install`.
- Reboot option.
- Compliance state.

### Scan versus install

```text
Scan
  -> evaluate missing/installed/rejected state
  -> no patch installation.

Install
  -> apply approved patches
  -> reboot according to option/need
  -> report compliance.
```

Scanning does not remediate.

No-reboot choice can leave a patch installed but not fully effective until reboot.

### Patch baseline

Baseline answers:

- Which patches are approved?
- When do they become approved?
- Which are rejected?
- What compliance severity applies?

Default baseline may not match organization policy.

Patch groups map different node groups to different baselines.

Baseline selection does not guarantee repository/network availability.

### Patch failure clues

| Symptom | First checks |
|---|---|
| Node shows noncompliant | Missing/failed/rejected patch and last scan time |
| Correct patch not approved | Baseline product/classification/severity/approval delay |
| Wrong baseline used | Patch-group tag/mapping/OS |
| Install fails | Package manager/repository network, disk, dependency, local lock |
| Patch installed but app broken | Reboot/service compatibility and maintenance validation |
| Node still needs reboot | Reboot option and patch requirement |
| Compliance absent | Node managed/online and inventory/scan execution |

### Maintenance Windows

```text
Maintenance window
  -> schedule + duration + cutoff
  -> registered targets
  -> registered tasks by priority
  -> task executions.
```

Use to schedule Run Command, Automation, Lambda, or Step Functions tasks where supported.

Exact objects/settings:

- Schedule/time zone.
- Duration.
- Cutoff.
- Registered targets.
- Registered tasks.
- Task priority.
- Task role.
- `MaxConcurrency` and `MaxErrors`.
- Input parameters.

### Duration versus cutoff

- Duration: total time window remains open.
- Cutoff: stop starting new tasks when little time remains.
- Running tasks are not necessarily cancelled at cutoff.

A maintenance window with no registered targets/tasks does nothing.

### Maintenance-window failure clues

- Schedule/time zone wrong.
- Window disabled.
- Target tag changed/no targets resolved.
- Task priority/dependency incorrect.
- Cutoff reached before task started.
- Task role/PassRole denied.
- Underlying Run Command/Automation/Lambda task failed.

Inspect task execution, then follow into the called service.

### Session Manager

```text
Authorized operator
  -> Systems Manager session
  -> managed node
```

Benefits:

- No inbound SSH/RDP port required.
- No bastion/public IP required.
- IAM-controlled access.
- Session logging/audit where configured and supported.
- Port forwarding/tunneling use cases where allowed.

Needs:

- Managed node online.
- Session-capable SSM Agent.
- Operator `StartSession` permission.
- Session document permission.
- Node/message endpoint path.
- Local Session Manager plugin for CLI use.

### Session governance

Configure:

- Session timeout/preferences.
- Shell profile where used.
- S3/CloudWatch session logging.
- KMS encryption.
- IAM conditions by tags/user/session document.
- CloudTrail session start/stop audit.

Know: some encrypted tunnel/port-forwarding content is not command-logged like an interactive shell. Network access control still matters.

### Fleet Manager

Use for browser-based managed-node administration:

- Files/processes/logs.
- Users/groups.
- Registry/Windows operations where supported.
- Performance/filesystem information.

Fleet Manager still depends on managed-node foundation and operator IAM.

It does not require opening general inbound administration ports.

### Inventory

Collects metadata such as:

- Applications/packages.
- AWS components/agent.
- Network configuration.
- Services/processes/files/registry where configured and supported.
- Instance details.

Inventory comes from associations/collection schedule. It is not guaranteed real-time.

Use for search, compliance, patch targeting, and fleet understanding—not live performance metrics.

### Parameter Store

Object model:

```text
Hierarchy/name
  -> parameter type
  -> value versions/labels
  -> access/KMS policy.
```

Types:

- `String`
- `StringList`
- `SecureString`

Use for configuration and secured values.

`SecureString` uses KMS. Caller needs parameter access and KMS decrypt access.

### Parameter Store versus Secrets Manager

| Need | Choose |
|---|---|
| Hierarchical configuration, simple secured parameter | Parameter Store |
| Managed secret rotation/lifecycle and secret-specific integration | Secrets Manager |

Parameter Store does not automatically become a rotation system merely because value is `SecureString`.

### Targeting

Prefer dynamic fleet targeting:

- Tags.
- Resource groups.
- Patch groups.
- Explicit IDs for small controlled scope.

Before large action:

```text
Preview target count
  -> test small canary
  -> set MaxConcurrency/MaxErrors
  -> run
  -> validate.
```

Tags can change. Re-evaluate targets at execution time.

### Governance and evidence

Use:

- Least-privilege operator and node roles.
- `PassRole` control for Automation/window tasks.
- Document sharing/version control.
- KMS/bucket/log policies.
- CloudTrail API history.
- Command/association/automation execution history.
- Patch/inventory compliance.
- Session logs and start/stop audit.
- EventBridge/SNS notifications.

Systems Manager output destinations need their own IAM/KMS permissions.

### Safe fleet operation

```text
Confirm managed-node foundation
  -> choose correct SSM capability
  -> pin document/version
  -> preview targets
  -> canary
  -> set concurrency/error limit
  -> schedule/approve
  -> run
  -> inspect per-node output
  -> validate business result
  -> record compliance.
```

### Failure clues

| Symptom | First checks |
|---|---|
| Many SSM features fail on same node | Agent, IAM, Region, network/DNS foundation |
| Only one document fails | Document platform/version/parameters/local command |
| Command success but desired state drifts later | Use State Manager association, not one-time command |
| Patch task never runs | Window schedule/targets/task/cutoff |
| Session denied but commands work | Operator StartSession/session-document permission |
| Session opens but no logs | Preferences, log destination/KMS, session type limitation |
| Inventory stale | Collection association/schedule/node reporting |
| SecureString access denied | Parameter permission plus KMS decrypt |
| Fleet change affects too many nodes | Broad tags and missing canary/rate control |

### Exam traps

- EC2 running does not mean SSM managed node online.
- Operator permission and node instance-profile permission are separate.
- Private node needs SSM endpoint/NAT path and DNS.
- Run Command is one-time execution; State Manager maintains configuration.
- Automation orchestrates steps; it can invoke Run Command.
- `MaxConcurrency` and `MaxErrors` are different.
- Rate control is not rollback.
- Patch `Scan` does not install.
- No-reboot patch can remain pending activation.
- Maintenance-window cutoff does not necessarily kill running tasks.
- Session Manager removes inbound SSH need, not IAM/network requirements.
- Inventory is metadata, not CloudWatch performance monitoring.
- `SecureString` needs KMS and does not provide automatic secret rotation.
- Command success does not prove application success.

### Do not memorize

- Every SSM document plugin.
- Exact default timeouts.
- Every agent log path.
- Every Patch Manager classification.
- Console click paths.

### Ready when

Given an operations scenario, you can:

1. Bring an EC2/hybrid machine online as a managed node.
2. Choose Run Command, State Manager, Automation, Patch Manager, or Maintenance Windows.
3. Configure targets, documents, schedules, concurrency, errors, and output.
4. Diagnose offline nodes, failed commands, patch noncompliance, and session denial.
5. Use Session/Fleet Manager, Inventory, and Parameter Store with correct governance.

---

## Skill 3.2.2 - Implement event-driven automation

**Official goal:** Detect events, route them to the right automation, handle failure safely, and avoid duplicate or recursive effects.

### What exam tests

- Primary: `SEL CFG BEH REM`
- Supporting: `DIA GOV PRC`
- Precision: `L2 - Object`
  - Know event source, filter/rule, target, invocation permission, retry, concurrency, DLQ/destination, state, and loop guard.

### Core model

```text
Event source
  -> filter/router
  -> target permission
  -> automation
  -> retry/failure destination
  -> evidence.
```

Every event workflow needs:

```text
Correct event + correct route + correct permission + idempotent target.
```

### Fast service selection

| Need | Choose |
|---|---|
| Simple reaction to S3 object event | S3 Event Notification |
| Rich event filtering/routing/many targets | EventBridge |
| Fan one message to subscribers | SNS |
| Buffer work and let consumers pull | SQS |
| Run short stateless code | Lambda |
| Run explicit multi-step stateful workflow | Step Functions |
| Governed infrastructure remediation/runbook | Systems Manager Automation |
| Investigate/correlate operational issues with an agent | AWS DevOps Agent |

These services can combine.

### S3 Event Notification flow

```text
S3 object event
  -> event type + prefix/suffix filter
  -> Lambda, SNS, SQS, or EventBridge
  -> consumer.
```

Exact settings:

- Event type.
- Destination ARN/configuration.
- Object-key prefix filter.
- Object-key suffix filter.
- Destination permission/resource policy.

### S3 event types

Recognition examples:

- Object created.
- Object removed.
- Object restore.
- Replication/lifecycle-related events where supported.

Choose only events needed. Broad `ObjectCreated:*` catches several creation methods.

### S3 filter behavior

Filters use object key, not arbitrary object metadata.

Example:

```text
prefix = incoming/
suffix = .csv
  -> only matching object keys.
```

Be careful with URL-encoded/special key characters and overlapping filter rules.

Prefix/suffix narrows events. It does not inspect file content.

### S3 destination permission

**Lambda**

- Function resource-based policy allows `s3.amazonaws.com` to invoke.
- Restrict by source bucket ARN/account where possible.

**SNS/SQS**

- Topic/queue resource policy allows source S3 bucket/service.

Also check:

- Bucket and destination are in compatible Regions for direct notification.
- Destination exists when notification configuration is saved.
- KMS key policy allows encrypted SNS/SQS destination use where required.

S3 bucket permission alone does not authorize the target invocation.

### S3 delivery behavior

- Delivery is at least once.
- Duplicate events can occur.
- Event order is not guaranteed.
- One event can arrive after a later event.

Therefore:

```text
Consumer must be idempotent.
```

For same-key ordering decisions, store/check event identity, object version, or sequencer logic as appropriate.

### S3 recursive-loop trap

Bad flow:

```text
Upload to bucket
  -> Lambda runs
  -> Lambda writes to same matching bucket/prefix
  -> Lambda runs again forever.
```

Fix:

- Write output to another bucket.
- Use separate input/output prefixes and filter input only.
- Add processed marker/idempotency guard.
- Restrict target permissions and monitor invocation growth.

### S3 notification failure clues

| Symptom | First checks |
|---|---|
| Cannot save notification | Destination exists/Region/policy/KMS/filter overlap |
| No event arrives | Event type, prefix/suffix, bucket config, destination policy |
| Lambda never invokes | Function resource policy and Region |
| Some objects never match | Actual encoded key and filter case/prefix/suffix |
| Same object processed twice | Expected at-least-once; idempotency missing |
| Invocation storm | Recursive write path/filter too broad |

### EventBridge object model

```text
Event producer
  -> event bus
  -> rule/event pattern
  -> target(s)
       -> retry policy/DLQ.
```

Exact objects:

- Default/custom/partner event bus.
- Event.
- Rule.
- Event pattern or schedule.
- Target.
- Target input/transformer.
- Retry policy.
- Dead-letter queue.
- Archive/replay where configured.
- Bus/resource policy for cross-account routing.

### Event envelope

Common fields:

- `source`
- `detail-type`
- `detail`
- `account`
- `region`
- `resources`
- `id`
- `time`

Event pattern matches the actual envelope and nested detail fields.

Wrong field/case/value means no match.

### Event pattern

```json
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {"state": ["stopped"]}
}
```

Pattern is filter, not procedural code.

Recognition operators can include exact match, prefix, anything-but, numeric, and existence rules.

Test with a real sample event shape.

### Rule versus schedule

- Event pattern: runs when matching event arrives.
- Scheduled rule/EventBridge Scheduler: runs by rate/cron/time schedule.

Schedule is time-driven, not evidence that a resource changed.

Use schedule for polling/periodic maintenance only when event source cannot provide the required trigger.

### EventBridge target input

Target can receive:

- Whole event.
- Selected input path.
- Constant input.
- Input transformer output.

Malformed transformed input can make target fail even when rule matched.

Preserve required identifiers such as account, Region, resource ARN, event ID, and desired state.

### EventBridge permissions

Depending on target:

- EventBridge uses an IAM target role, or
- Target resource policy allows `events.amazonaws.com`.

Cross-account event routing also needs:

- Destination event-bus resource policy.
- Source principal/organization permission.
- Target-side rule/role permission.

Rule enabled and matching does not prove target authorization.

### EventBridge retry and DLQ

Target settings:

- Maximum event age.
- Retry attempts/policy.
- SQS dead-letter queue.

Flow:

```text
Target delivery fails
  -> retry within age/attempt limits
  -> send undelivered event to DLQ if configured.
```

DLQ needs queue policy allowing EventBridge.

DLQ is evidence and recovery buffer. It does not replay itself automatically.

### Archive and replay

- Archive stores matching events from an event bus.
- Replay sends archived events back through the bus/rules.
- Consumers can receive old events again.

Use idempotency and controlled replay scope/time.

Replay is not a rollback of prior side effects.

### EventBridge delivery behavior

- Delivery is at least once.
- Duplicates are possible.
- Global ordering is not guaranteed.
- Rule can have multiple targets.
- One target can fail while another succeeds.

Each target needs its own permission, retry, and evidence review.

### EventBridge evidence

- Rule enabled state.
- Event pattern and sample event.
- Matched-events metric.
- Target invocation/failure/throttle metrics.
- DLQ messages.
- CloudTrail configuration changes.
- Target service logs/execution history.
- Archive/replay status where used.

If matched-events is zero, fix producer/pattern. If matches exist but target fails, inspect permission/target.

### SNS and SQS boundary

**SNS**

```text
Publisher -> topic -> many push subscribers.
```

Use for fan-out. Each subscription has its own delivery/filter behavior.

**SQS**

```text
Producer -> durable queue -> consumer polls/processes/deletes.
```

Use to buffer rate differences and survive consumer outage.

Common pattern:

```text
EventBridge/SNS -> SQS -> Lambda/worker
```

Queue absorbs bursts; Lambda direct invocation does not provide the same consumer-controlled buffer.

### Lambda invocation models

| Model | Examples | Failure owner |
|---|---|---|
| Synchronous | Direct request/API-style caller | Caller receives response/retries |
| Asynchronous | S3/EventBridge/SNS invocation | Lambda queues and applies async retry/failure handling |
| Event source mapping | SQS/stream polling | Lambda poller manages batches/checkpoints/retries |

Do not apply one retry model to every source.

### Lambda permission model

```text
Source invokes function
  -> Lambda resource-based policy.

Function code calls AWS
  -> Lambda execution role.
```

These are separate.

Also check:

- Source ARN/account conditions.
- Event source mapping role permissions.
- KMS, secret, VPC, and destination permissions.
- Organization/SCP boundaries.

### Lambda execution controls

- Function timeout.
- Memory/CPU allocation.
- Environment variables/layers.
- VPC configuration.
- Reserved concurrency.
- Account concurrency availability.
- Event-source batch size/window.
- Async retry/maximum event age.
- DLQ or destinations.

Reserved concurrency can protect downstream services, reserve capacity, or throttle function if set too low/zero.

### Lambda async failure handling

```text
Async event
  -> internal Lambda queue
  -> invoke
  -> retry on function/system failure
  -> on-failure destination or DLQ after policy exhausted.
```

Destinations can provide richer invocation records and success/failure routing.

DLQ captures failed event payload for supported async behavior.

Do not configure failure destination without permission to publish/send.

### Lambda with SQS

```text
Lambda polls SQS batch
  -> invokes function
  -> successful messages deleted
  -> failures become visible again after visibility timeout.
```

Need:

- Event source mapping enabled.
- Execution role can receive/delete/get queue attributes.
- Queue and function Region compatibility.
- Visibility timeout longer than function processing needs.
- Batch/partial-batch failure behavior.
- Queue DLQ/redrive policy.
- Idempotent message handling.

One poison message can repeat; partial batch response can avoid retrying successful records where supported/configured.

### Lambda failure clues

| Symptom | First checks |
|---|---|
| Function never invokes | Source rule/config, resource policy, event source mapping state |
| Invocation throttled | Reserved/account concurrency and source retry/backlog |
| Function times out | Timeout, dependency/network, code path, memory/CPU |
| Access denied in code | Execution role/resource/KMS policy, not invoke policy |
| Async event disappears | Retry age/attempts, DLQ/destination permission/config |
| SQS backlog grows | Mapping, concurrency, errors, visibility, downstream capacity |
| Same side effect repeats | Duplicate delivery/retry and no idempotency |
| VPC function cannot reach AWS service | Route/NAT/VPC endpoint/DNS/SG |

### Idempotency

```text
Same event arrives multiple times
  -> intended business result happens once.
```

Possible key:

- Event ID.
- S3 bucket + key + version/sequencer.
- SQS message/business ID.
- Resource ARN + desired state + event time/version.

Possible control:

- DynamoDB conditional write.
- Existing-state check.
- Unique transaction key.
- Processed-event record with expiry.

Store idempotency state before/atomically with irreversible side effect when design allows.

“Check then act” without atomicity can race.

### Retry safety

Use:

- Bounded attempts.
- Exponential backoff.
- Jitter.
- Maximum event age.
- DLQ/failure destination.
- Idempotency.
- Downstream rate/concurrency control.

Bad pattern:

```text
Many failing events
  -> immediate retries
  -> downstream overload
  -> larger failure.
```

### Step Functions selection

Use when process needs explicit state:

- Multiple steps.
- Branching.
- Parallel work.
- Wait/timer.
- Retry/catch by error.
- Human/external callback.
- Per-step execution history.

Do not pack a long stateful workflow into one Lambda when Step Functions fits.

### Step Functions object model

```text
State machine definition
  -> execution
       -> states
       -> input/output/history
  -> execution role calls services.
```

State types to recognize:

- Task.
- Choice.
- Wait.
- Parallel.
- Map.
- Pass.
- Succeed.
- Fail.

### Standard versus Express

| Workflow | Best fit |
|---|---|
| Standard | Durable, auditable, long-running workflows |
| Express | High-rate, short-duration workflows |

Choose from duration, event rate, execution-history, and pricing/semantics needs.

### Step Functions retry/catch

Retry properties to recognize:

- `ErrorEquals`
- `IntervalSeconds`
- `MaxAttempts`
- `BackoffRate`
- Jitter setting where used

Catch properties:

- `ErrorEquals`
- `ResultPath`
- `Next`

```text
Task fails
  -> matching Retry
  -> if exhausted, matching Catch
  -> recovery/cleanup state.
```

Catch is controlled branch, not automatic undo.

### Step Functions permissions/evidence

- State-machine execution role needs each service action.
- Human caller needs permission to start/read execution.
- Resource/KMS policies still apply.
- Execution history shows input/output/error per state for Standard workflows and configured logging varies by type.
- CloudWatch Logs/metrics and target service logs complete evidence.

Failure clue:

```text
State entered + AccessDenied
  -> execution role or target resource/KMS policy.
```

### Systems Manager Automation boundary

| Need | Choose |
|---|---|
| General application/business workflow | Step Functions |
| AWS operational runbook/remediation with managed actions | Systems Manager Automation |
| One short event reaction | Lambda |
| Only route/filter event | EventBridge |

Automation can include approvals, branches, waits, API actions, and Run Command. It is optimized for operational runbooks.

### AWS DevOps Agent

Recognition-level model:

```text
Operational telemetry/events
  -> agent investigates/correlates
  -> proposes likely root cause
  -> recommends or runs authorized remediation
  -> suggests preventive action.
```

Use when broad operational investigation across signals is the clue.

Verify:

- Connected data sources/telemetry scope.
- IAM role and least-privilege actions.
- Account/Region/resource coverage.
- Investigation evidence and recommendation.
- Human approval/guardrails for impactful actions.
- Remediation execution and rollback evidence.

DevOps Agent does not replace deterministic alarms, permissions, runbooks, or operator accountability.

### Safe remediation design

```text
Narrow event match
  -> confirm resource/account/Region
  -> check current state
  -> acquire idempotency/lock guard
  -> run least-privilege action
  -> verify desired result
  -> emit audit/result event
  -> retry or DLQ safely.
```

For destructive/high-impact actions, add approval or stronger conditions.

### Loop prevention

Automation action may emit another event matching the same rule.

Guard with:

- Event source/detail that distinguishes remediated state.
- Tag/state marker.
- Idempotency record.
- Maximum attempts/event age.
- Rule filter excluding automation actor/result.
- Concurrency/rate limits.

Always ask:

```text
Will my fix create the trigger again?
```

### Evidence ladder

```text
1. Did source emit event?
2. Did filter/rule match?
3. Did target invocation get authorized?
4. Did target start?
5. Did code/workflow succeed?
6. Did desired resource state change?
7. Did retry/DLQ capture failure?
```

Use layer-specific evidence; “nothing happened” is not a diagnosis.

### Failure clues

| Symptom | First checks |
|---|---|
| No automation at all | Source event/config, rule enabled, pattern/filter |
| Rule matches but target absent | Target ARN, role/resource policy, target metrics/DLQ |
| Target starts but resource unchanged | Execution role, parameters, condition/current state, downstream error |
| Duplicate side effects | At-least-once delivery/retry and no atomic idempotency |
| Old event changes newer state | Ordering/version/current-state check missing |
| DLQ grows | Target permission, throttling, malformed input, persistent code failure |
| Archive replay causes repeats | Expected old events; idempotency/replay scope missing |
| Step Functions stops at task | Retry/catch mismatch or execution-role/target error |
| DevOps Agent cannot remediate | Role/guardrail/scope/action permission or approval |
| Costs/invocations explode | Recursive loop, broad match, uncontrolled retry/concurrency |

### Exam traps

- S3 event delivery can duplicate and arrive out of order.
- Prefix/suffix filters inspect object key, not contents.
- S3/Lambda source permission and Lambda execution role are different.
- EventBridge pattern match and target authorization are different stages.
- EventBridge DLQ needs a queue policy and does not replay itself.
- Archive replay repeats events; it does not undo old side effects.
- SNS pushes/fans out; SQS buffers for polling consumers.
- Lambda retry behavior depends on invocation model/source.
- Reserved concurrency can protect or throttle.
- Step Functions Catch handles flow; it does not automatically compensate prior actions.
- Success of function/workflow does not prove desired business result.
- Every automatic remediation needs idempotency and loop analysis.
- DevOps Agent recommendations/actions still need permissions and governance.

### Do not memorize

- Every EventBridge pattern operator.
- Every Lambda retry count/default.
- Full Step Functions definition syntax.
- Every DevOps Agent interface/detail.
- Console click paths.

### Ready when

Given an event-driven scenario, you can:

1. Choose S3 notification, EventBridge, SNS, SQS, Lambda, Step Functions, or Automation.
2. Configure source filter/rule, target, permissions, retries, DLQ, and concurrency.
3. Explain async versus event-source-mapping failure behavior.
4. Build idempotent, bounded, loop-safe remediation.
5. Trace failure from event emission through desired-state verification.

---

## Skill 4.1.1 - Implement IAM features

**Official goal:** Give the correct identity the minimum required access under the correct conditions.

### What exam tests

- Primary: `CFG BEH GOV`
- Supporting: `SEL DIA`
- Precision: `L3 - Property`
  - Exact principal, action, resource, effect, condition, trust, boundary, session, MFA, and `PassRole` setting matter.

### Core authorization question

```text
Who
  can do what
  to which resource
  under which conditions?
```

Map to:

```text
Principal + Action + Resource + Context.
```

### Authentication versus authorization

- Authentication: prove who you are.
- Authorization: decide what that identity can do.

MFA strengthens authentication. It does not grant permissions.

### Identity selection

| Need | Choose |
|---|---|
| Account ownership/root-only task | Root user; protect heavily, avoid daily use |
| Human workforce access | Federation/IAM Identity Center |
| Legacy/specific long-lived IAM identity | IAM user, only when necessary |
| AWS workload access | IAM role |
| Cross-account temporary access | AssumeRole |
| AWS service-managed role lifecycle | Service-linked role |

Prefer temporary role credentials over long-lived access keys.

### Root user

Protect with:

- Strong unique password.
- MFA/passkey.
- No routine access keys.
- Secure recovery email/phone.
- Alerts/monitoring for use.
- Use only for root-required tasks.

Root credentials are not an operations account.

### IAM users and groups

**IAM user**

- Long-lived account identity.
- Can have console password and access keys.
- Can receive identity policies directly or through groups.

**IAM group**

- Collection of IAM users.
- Policies apply to member users.
- Cannot be assumed like a role.
- Is not a principal used in a resource policy.

Use groups to manage common IAM-user permissions, not workloads.

### IAM roles

Role contains:

```text
Trust policy
  -> who may assume/use role.

Permissions policies
  -> what role session may do after assumption.
```

Role has no long-lived access key.

Assuming role returns STS temporary credentials:

- Access key ID.
- Secret access key.
- Session token.
- Expiration.
- Assumed-role session ARN/name.

### Trust policy versus permissions policy

**Trust policy**

- Resource-based policy on role.
- `Principal` names who/service can assume.
- `Action` commonly `sts:AssumeRole` or service-specific STS action.
- Conditions can require MFA, external ID, organization, source identity, tags.

**Permissions policy**

- Allows/denies AWS actions after role is assumed.
- Does not decide who can assume role.

Trap:

```text
Role has powerful permissions
but trust rejects caller
  -> caller cannot assume it.
```

### AssumeRole gates

Cross-account/common model:

```text
Caller identity policy allows sts:AssumeRole
  + target role trust allows caller
  + trust conditions match
  -> temporary role session.

Role permissions then govern AWS actions.
```

Check both accounts.

### External ID

Use for third-party cross-account role access to reduce confused-deputy risk.

```text
Customer trusts vendor role
  + trust condition requires customer-specific ExternalId
  -> vendor must present correct value.
```

External ID is a trust condition, not a password or permission grant.

### Service role and service-linked role

**Service role**

- Customer creates/configures role used by an AWS service.
- Trust policy allows that service principal.
- Permissions define service actions.

**Service-linked role**

- Predefined for one AWS service.
- Service creates/uses it with defined trust/permissions.
- Deletion/modification may be restricted while service resources depend on it.

Do not replace a required service-linked role with an ordinary user.

### EC2 instance profile

```text
EC2 instance
  -> instance profile
  -> IAM role
  -> temporary credentials from instance metadata.
```

Instance profile is the attachment container. Role holds permissions.

Never bake access keys into AMI/user data when an instance role fits.

### Identity Center/federation

```text
Workforce identity source
  -> user/group
  -> permission set
  -> account assignment
  -> generated account role/session.
```

Benefits:

- Central authentication/MFA.
- Temporary credentials.
- Group-based account access.
- No duplicate IAM users in every account.

Permission set defines access. Account assignment gives that permission set to a user/group in an account.

### Policy types

| Policy | Attached to | Main purpose |
|---|---|---|
| Identity-based | User, group, role | Allow/deny identity actions |
| Resource-based | Resource | Name allowed/denied principals |
| Trust policy | IAM role | Who may assume role |
| Permissions boundary | User/role | Maximum identity permissions |
| SCP | Organization root/OU/account | Maximum permissions in member accounts |
| Session policy | STS session | Further limit temporary session |

Boundary, SCP, and session policy do not grant access.

### Managed versus inline policy

**AWS managed policy**

- AWS maintains it.
- Reusable.
- Can be broader/change over time.

**Customer managed policy**

- Customer controls versions/content.
- Reusable across identities.
- Easier central update than inline policy.

**Inline policy**

- Embedded in one identity/resource relationship.
- Deleted with that identity.
- Useful for tightly coupled one-off permission; harder to reuse/audit at scale.

### Policy document anatomy

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "ReadReports",
    "Effect": "Allow",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::reports/*",
    "Condition": {
      "Bool": {"aws:SecureTransport": "true"}
    }
  }]
}
```

Exact elements:

- `Version`
- `Statement`
- `Sid`
- `Effect`
- `Principal`/`NotPrincipal`
- `Action`/`NotAction`
- `Resource`/`NotResource`
- `Condition`

### Element behavior

**Effect**

- `Allow`
- `Deny`

**Action**

- API operation(s), such as `s3:GetObject`.
- Wildcards broaden scope.

**Resource**

- ARN(s) affected.
- Some actions require `*` because they lack resource-level permissions.

**Principal**

- Used in resource-based/trust policies.
- Names account, role, user, service, federated principal, etc.
- Not normally used in identity-based policy.

**Condition**

- Tests request context.

### `NotAction` and `NotResource`

These mean “everything except” within the statement’s scope.

They can be useful but dangerous.

```text
Allow + NotAction
  -> potentially broad access to all other applicable actions.
```

Always read Effect, Resource, and Condition together.

### Effective permission rule

Simplified:

```text
Explicit deny anywhere applicable
  -> DENY.

No applicable allow
  -> implicit DENY.

Applicable allow
  + no applicable explicit deny
  + inside boundary/SCP/session limits
  -> ALLOW.
```

Explicit deny wins.

### Permission intersection

For the common identity-policy permission path:

```text
Effective permission
  = identity-policy allow
  INTERSECT boundary
  INTERSECT SCP
  INTERSECT session policy
  minus explicit denies.
```

A broad administrator identity policy cannot escape a restrictive SCP or boundary.

Resource-based policies can provide another allow path. Exact behavior depends on whether `Principal` names a user, role, or role/session ARN. Applicable explicit denies still win. Identify the exact principal before evaluating that path.

### Permissions boundary

- Attached to IAM user or role.
- Sets maximum identity-based permission.
- Does not grant anything itself.
- Identity policy must still allow action.
- Explicit denies and other policies still apply.

Example:

```text
Identity policy allows S3 + EC2.
Boundary allows only S3.
  -> effective maximum is S3.
```

### SCP

- Attached through Organizations root/OU/account.
- Inherited down hierarchy.
- Limits member-account principals.
- Does not grant permission.
- Explicit deny wins.

Detailed organization behavior belongs in Skill 4.1.3.

### Session policy

- Passed when creating/assuming a temporary session where supported.
- Narrows role/user session permissions.
- Cannot grant more than identity/role permission.
- Session duration and policy affect only that temporary session.

### Same-account versus cross-account

**Same account**

- Identity policy or resource policy can form an allow path, depending on service/principal type.
- Boundaries/SCPs/session/explicit denies still matter.

**Cross-account**

Usually requires:

```text
Caller-side identity allow
  + target-side resource/trust allow
  + no deny/limit blocking either side.
```

One account cannot unilaterally grant permissions the other side forbids.

### Resource policies

Common on:

- S3 bucket/access point.
- KMS key.
- SNS topic.
- SQS queue.
- Secrets Manager secret.
- Lambda function.
- EventBridge event bus.

Resource policy states which principals can access that resource and under what conditions.

Service/resource policies do not replace caller-side permissions in every cross-account pattern.

### Condition model

```text
Condition operator
  -> context key
  -> expected value(s).
```

Examples:

- String/ARN comparison.
- Boolean.
- Numeric/date.
- IP address.
- `Null`/`IfExists` variants.

Multiple different condition blocks/keys generally narrow the statement together. Read operator semantics carefully.

If a required context key is absent, the condition may not match; negated/`IfExists` behavior needs special care.

### High-value global condition keys

| Goal | Key/example |
|---|---|
| Require MFA context | `aws:MultiFactorAuthPresent` |
| Require TLS | `aws:SecureTransport` |
| Limit source IP | `aws:SourceIp` |
| Limit source VPC endpoint | `aws:SourceVpce` |
| Limit source VPC | `aws:SourceVpc` where supported |
| Limit requested Region | `aws:RequestedRegion` |
| Limit organization | `aws:PrincipalOrgID` / resource-org keys |
| Bind service call to source resource | `aws:SourceArn` |
| Bind service call to source account | `aws:SourceAccount` |
| Match principal/resource tags | `aws:PrincipalTag` / service resource-tag keys |
| Control requested tags | `aws:RequestTag` / `aws:TagKeys` |

Context key availability depends on request/service.

### Confused-deputy protection

When AWS service calls another resource for you:

```text
Allow service principal
  + require expected aws:SourceAccount
  + require expected aws:SourceArn where supported.
```

This stops another customer’s resource from abusing your service permission.

Example use: S3 invoking Lambda or publishing to SNS/SQS.

### Network-based conditions

- Source IP checks public request source.
- Source VPC endpoint checks endpoint ID where context exists.
- Source VPC checks VPC context where supported.
- `SecureTransport` enforces TLS.

These IAM conditions are authorization filters. They do not create routes, endpoints, or network reachability.

### Region condition trap

`aws:RequestedRegion` limits endpoint Region used for request.

Some global-service actions/side effects need exceptions. Test policy before broad Region deny.

Region condition does not move a resource to another Region.

### MFA

Use for:

- Root.
- Workforce/privileged users.
- Sensitive role assumption or API operations where policy supports MFA context.

Policy can require MFA condition.

Important:

- Device registration alone is not enough; session/request needs MFA context.
- Long-lived access-key requests may not carry MFA context unless temporary session obtained appropriately.
- MFA does not fix overbroad authorization.

### Password policy

IAM account password policy can control IAM-user passwords:

- Minimum length.
- Character requirements.
- Password expiration.
- Reuse prevention.
- User self-change behavior.

It applies to IAM users, not federated Identity Center/IdP passwords.

Prefer federation over building large IAM-user password fleets.

### Access-key lifecycle

IAM user can have up to two access keys, enabling safe rotation.

```text
Create second key
  -> update application
  -> verify new key use
  -> deactivate old key
  -> monitor
  -> delete old key.
```

Never delete old key before confirming all users of it changed.

Prefer workload roles so rotation is automatic through temporary credentials.

### Credential report and last-used data

Credential report helps audit IAM users:

- Password enabled/last used/changed.
- MFA active.
- Access-key active/age/last rotated.
- Signing certificate status where relevant.

Service last-accessed data helps reduce permissions but can have reporting delay/coverage limits.

Evidence is not itself remediation.

### `iam:PassRole`

PassRole means:

```text
Human/pipeline tells AWS service:
“Use this IAM role.”
```

Caller needs:

- `iam:PassRole` on exact role ARN.
- Permission for service API action creating/updating resource.

Role needs:

- Trust policy for target service.
- Permissions needed by workload/service.

Caller does not receive role credentials through PassRole.

### PassRole restriction

Use:

- Exact role ARN/path.
- `iam:PassedToService` condition.
- Least privilege around create/update APIs.

Broad `iam:PassRole` can allow privilege escalation by attaching a powerful role to a service.

### Tag-based access control/ABAC

Pattern:

```text
Principal tag project=A
  matches
Resource tag project=A
  -> allow project-A resource action.
```

Controls:

- Principal/session tags.
- Resource tags.
- Request tags during create/tag.
- Allowed tag keys.

Need permissions to create resource and apply required tags.

Protect tag mutation; otherwise user can change tag to gain access.

### Least-privilege build process

```text
Start from required job/API actions
  -> scope resources
  -> add required conditions
  -> test
  -> review CloudTrail/last-access evidence
  -> remove unused permission
  -> monitor changes.
```

Avoid `Action: *`, `Resource: *` unless action/service requires it and risk is controlled.

### Failure clues

| Symptom | First checks |
|---|---|
| Cannot assume role | Caller `sts:AssumeRole`, trust principal/action/conditions, MFA/external ID |
| Can assume but AWS action denied | Role permissions, boundary, SCP, session, resource/KMS policy |
| Service cannot use role | Service trust policy and role permissions |
| User cannot attach role to service | `iam:PassRole` plus service create/update action |
| Policy allow seems ignored | Explicit deny, boundary/SCP/session, wrong ARN/context |
| Tag-based access fails | Principal/resource/request tags and tag-key spelling |
| MFA policy still denies | Session lacks MFA-authenticated context |
| Cross-account resource denied | Caller allow plus target resource/trust allow |
| Secure resource policy breaks service | Missing SourceArn/SourceAccount/KMS/service exception |

### Safe IAM change path

```text
Identify principal/action/resource/context
  -> choose identity/role/policy type
  -> write narrow allow or explicit guardrail deny
  -> validate syntax/conditions
  -> test with noncritical scope
  -> verify CloudTrail/access
  -> remove temporary broad permission
  -> monitor credential/policy drift.
```

### Exam traps

- Authentication and authorization are different.
- MFA adds authentication assurance; it grants no API action.
- Trust policy controls assumption; permissions policy controls post-assumption actions.
- Role has temporary credentials only after assumption/use.
- Permissions boundary, SCP, and session policy limit; they do not grant.
- Explicit deny overrides an allow.
- Missing allow is implicit deny.
- `Principal` belongs in resource/trust policies, not normal identity policies.
- Cross-account access usually needs permission on both sides.
- Resource policy does not bypass every boundary/SCP/session restriction.
- `SourceArn`/`SourceAccount` reduce service confused-deputy risk.
- Password policy applies to IAM users, not federated IdP passwords.
- PassRole does not let caller assume the role.
- Broad PassRole can become privilege escalation.
- `SecureTransport`/VPC conditions do not create network connectivity.
- Sensitive ABAC tag keys must be protected from unauthorized changes.

### Do not memorize

- Every IAM global condition key.
- Every root-only account task.
- Full policy-evaluation edge-case matrix.
- Exact credential-report column order.
- Console click paths.

### Ready when

Given an IAM scenario, you can:

1. Choose user, group, role, federation, Identity Center, or service-linked role.
2. Read policy Effect/Action/Resource/Principal/Condition precisely.
3. Separate trust, permissions, boundary, SCP, session, and resource policies.
4. Configure MFA, password/access-key controls, conditions, and ABAC.
5. Explain AssumeRole and PassRole without mixing them.

---

## Skill 4.1.2 - Troubleshoot and audit access issues

**Official goal:** Prove why an AWS request was allowed or denied, then make the smallest safe permission correction.

### What exam tests

- Primary: `EVD DIA REM GOV`
- Supporting: `BEH`
- Precision: `L3 - Property`
  - Exact principal/session, action, resource ARN, account, Region, request context, error, and policy layer matter.

### Core investigation tuple

Capture:

```text
Principal
+ Action
+ Resource
+ Context
+ Decision/error
```

Without all five, access troubleshooting is guesswork.

### First questions

```text
Who actually made the request?
Which API action was denied?
Which exact resource ARN?
Which account and Region?
Which request conditions were present?
Was denial explicit or was allow missing?
```

Do not begin by attaching a broad policy.

### Identity/session reality

The human’s expected role may not be the actual caller.

Possible principals:

- IAM user.
- IAM role session/assumed-role ARN.
- Identity Center-created role session.
- EC2 instance role session.
- Lambda/ECS execution role session.
- AWS service principal/service-linked role.
- Federated user/session.
- Root.

Use caller identity and CloudTrail session context.

### `sts:GetCallerIdentity`

Useful to confirm:

- Account ID.
- Principal/user ID.
- ARN of current credentials/session.

It does not show permissions. It proves which credentials are being used.

Wrong profile, stale environment credentials, or wrong assumed role is common.

### Access-decision layers

Check applicable layers:

```text
Identity policy
  + resource policy
  + role trust policy for assumption
  + permissions boundary
  + SCP
  + session policy
  + VPC endpoint policy
  + KMS key policy/grant
  + service-specific control
  + request context.
```

Not every request uses every layer. Identify which apply.

### Deny-first rule

```text
Applicable explicit deny
  -> deny, even when another policy allows.

No applicable allow
  -> implicit deny.
```

Find explicit denies before adding an allow.

Enhanced error messages may name the blocking layer, but coverage varies by service/cross-account context. Read the exact message; verify with evidence.

### Troubleshooting order

```text
1. Reproduce/capture exact error safely.
2. Confirm caller ARN/account/Region.
3. Identify API action and resource ARN.
4. Find CloudTrail event.
5. Search explicit denies/limits.
6. Confirm required allow path.
7. Evaluate conditions/context.
8. Check resource/KMS/endpoint/service controls.
9. Simulate/analyze as supporting evidence.
10. Apply narrow fix and retest.
```

### CloudTrail role

CloudTrail answers:

```text
Who called what,
when,
from where,
in which Region/account,
with which parameters,
and what AWS returned.
```

It is primary audit evidence for control-plane/API access.

### High-value CloudTrail fields

- `eventTime`
- `eventSource`
- `eventName`
- `awsRegion`
- `userIdentity.type`
- `userIdentity.arn`
- `userIdentity.principalId`
- `userIdentity.accountId`
- `sessionContext`/session issuer/MFA data
- `sourceIPAddress`
- `userAgent`
- `requestParameters`
- `resources`
- `errorCode`
- `errorMessage`
- `recipientAccountId`
- request/event ID

For assumed roles, inspect both session ARN and session issuer/base role.

### Management versus data events

**Management events**

- Control-plane operations: create, modify, delete, list/configure.
- Commonly available in Event History/trails according to configuration.

**Data events**

- High-volume resource activity, such as S3 object or Lambda invocation events.
- Must be enabled/selectively configured for audit use.

If object-level request is absent, confirm data-event logging was configured at that time.

CloudTrail cannot reconstruct an event that was never logged.

### Event History versus trail/log store

- Event History is convenient recent Regional management-event lookup.
- Trail delivers configured events to durable destination.
- Organization trail centralizes member-account events where configured.
- CloudTrail Lake/Athena-style queries help broader investigation when logs are available.

Check correct Region, time range, account, event source/name, and data-event selector.

### CloudTrail limitations

- A service may make downstream calls under another service role.
- Some denied requests have limited fields.
- Sensitive fields can be redacted.
- CloudTrail shows request/decision, not every policy statement evaluated.
- Network timeout before API reach may produce no event.

Use exact event plus policies and service evidence.

### AssumeRole denial

Required path:

```text
Caller identity allows sts:AssumeRole
  + role trust allows caller
  + trust conditions match
  + no SCP/boundary/session deny
  -> role session.
```

Check:

- Caller ARN versus trust `Principal`.
- Role ARN/account.
- `sts:AssumeRole` action.
- External ID.
- MFA context.
- Source identity/session-tag conditions.
- Organization/account conditions.
- Maximum/session duration request.
- Caller SCP/boundary/session policy.

Role permissions do not help if assumption itself fails.

### PassRole denial

Request commonly needs:

```text
Service create/update action
  + iam:PassRole on role ARN
  + PassedToService condition match
  + role trust for target service.
```

CloudTrail may show the outer service API failing because PassRole was denied.

Do not grant `iam:PassRole` on `*` as a quick fix.

### Permission after assumption

If role assumption succeeds but later API fails, inspect:

- Role identity policies.
- Permissions boundary.
- Session policy.
- SCP.
- Target resource policy.
- KMS key/grant.
- Endpoint/service-specific controls.
- Session tags/MFA/source conditions.

Trust policy is no longer the main gate for the later resource API.

### ARN/resource mismatch

Read policy and API documentation resource shape.

Common S3 split:

```text
s3:ListBucket
  -> arn:aws:s3:::bucket-name

s3:GetObject
  -> arn:aws:s3:::bucket-name/*
```

Other mistakes:

- Wrong account ID.
- Wrong Region/partition.
- Role ARN versus assumed-role session ARN.
- KMS key ARN versus alias ARN.
- Missing path/prefix/wildcard.
- Action supports only `Resource: *`.
- Case-sensitive tag/condition value mismatch.

An allow on the wrong ARN is no allow.

### Condition failure

Compare policy expectation with actual request context:

- `aws:SourceIp`
- `aws:SourceVpc`/`aws:SourceVpce`
- `aws:SecureTransport`
- `aws:RequestedRegion`
- `aws:MultiFactorAuthPresent`
- `aws:PrincipalOrgID`
- `aws:SourceArn`/`aws:SourceAccount`
- Principal/resource/request tags.
- Time/session/external ID.

Check:

- Key exists for this request.
- Operator is correct.
- String/ARN/case value matches.
- Multiple conditions all match as intended.
- Negated and `IfExists` logic does not broaden/deny unexpectedly.

### MFA-context failure

Device may be configured, but current session may lack MFA context.

Check:

- How credentials were obtained.
- CloudTrail session MFA data.
- Role trust/identity condition.
- Long-lived access key versus MFA-backed temporary session.

Registering MFA is not the same as using MFA for the session.

### Tag/ABAC failure

Check all tag sides:

- Principal/session tag.
- Resource tag.
- Request tag on create.
- `TagKeys` restriction.
- Exact key/value case.
- Whether action exposes that tag context.
- Permission to tag at create time.

Also check who can mutate the authorization tags.

### VPC endpoint policy

Endpoint policy can restrict API traffic passing through a VPC endpoint.

```text
Network reaches endpoint
  + IAM/resource policy allows
  but endpoint policy rejects
  -> AccessDenied.
```

Endpoint policy does not grant principal permission and does not affect requests that do not use that endpoint.

Confirm DNS/path actually used the endpoint.

### KMS access denial

Encrypted-resource action often has two gates:

```text
Permission to use resource
  + permission to use KMS key.
```

Check:

- Key ARN/account/Region.
- Key state.
- Key policy.
- IAM permission where key policy enables it.
- KMS grant.
- Encryption context/conditions.
- Service principal and `ViaService`/source conditions where used.
- Cross-account permission on both sides.

Outer service can return an access error caused by downstream KMS denial.

### Resource-policy denial

Check:

- Exact principal or account.
- Principal is role versus role session/service.
- Action and resource ARN.
- SourceArn/SourceAccount conditions.
- Organization/VPC/IP/TLS conditions.
- Explicit deny/public-access controls.
- Cross-account caller identity allow.

Common resources:

- S3 bucket.
- KMS key.
- SQS queue/SNS topic.
- Lambda function.
- Secrets Manager secret.
- EventBridge bus.

### Service-specific blockers

IAM allow can still be insufficient because of:

- S3 Block Public Access/Object Ownership/ACL where relevant.
- KMS key policy/grant/state.
- Secrets Manager resource policy/KMS.
- VPC endpoint policy.
- Organizations SCP.
- Permissions boundary/session policy.
- Service deletion protection/retention lock.
- Network/resource configuration unrelated to IAM.

Not every failed operation is an IAM policy problem.

### IAM Policy Simulator

Use to test a policy hypothesis:

```text
Principal/policies
  + action
  + resource
  + supplied context
  -> simulated allow/deny and matched statements.
```

Useful for:

- Identity-policy changes.
- Resource/action scoping.
- Boundary/context effects supported by simulator.
- Finding missing allow or explicit deny in included policies.

### Policy Simulator limitations

- Does not make the real API call.
- Only evaluates policies/context included and supported.
- Live resource state, network path, quotas, and service behavior are outside simulation.
- Cross-account/resource-policy and Organizations effects can require separate real evaluation.
- Missing context values can make result misleading.
- Results do not replace CloudTrail evidence.

Treat simulator as test bench, not final proof.

### IAM Access Analyzer capabilities

| Capability | Use |
|---|---|
| External access analysis | Find resource policies allowing outside account/organization/zone of trust |
| Internal access analysis | Analyze access paths within defined organization/account scope where supported |
| Unused access analysis | Find unused roles, credentials, services/actions |
| Policy validation | Find errors, warnings, security/general suggestions |
| Policy generation | Build policy from observed CloudTrail activity |
| Access preview | Preview external/public access before supported policy change |

Access Analyzer uses policy reasoning. Finding does not automatically mean malicious use.

### External access finding

Finding identifies:

- Resource.
- External principal/access path.
- Policy condition/context.
- Status.
- Analyzer zone of trust.

Response:

```text
Validate intended access
  -> remove/narrow policy if unintended
  -> archive with reason only if accepted
  -> verify finding resolves/new preview.
```

Archived is workflow status, not permission removal.

### Unused access

Can identify:

- Unused role.
- Unused access key/password.
- Unused service/action permission.

Use as least-privilege evidence.

Before removal:

- Confirm reporting period/coverage.
- Check rare/seasonal/emergency workloads.
- Identify owner and rollback.
- Remove in controlled stage.

“Not recently used” is not proof “never needed.”

### Policy validation

Finding categories can include:

- Error.
- Security warning.
- Warning.
- Suggestion.

Examples:

- Invalid element/action/ARN.
- Overly broad principal/action/resource.
- Risky condition or public/cross-account path.

Validation improves policy quality. It does not prove the workload can perform every required request.

### Policy generation

```text
Selected principal
  + selected CloudTrail activity period
  -> generated policy candidate.
```

Limits:

- Only observed activity/covered services/events.
- Rare actions may be missing.
- Resource-level detail may need refinement.
- Generated policy needs human review/testing.

Do not deploy generated policy blindly.

### Audit evidence selection

| Question | Best first evidence |
|---|---|
| Who made denied API request? | CloudTrail |
| Which statement would allow/deny a test request? | Policy Simulator |
| Which resource policy exposes outside trust boundary? | Access Analyzer external access |
| Which permissions/credentials appear unused? | Access Analyzer unused access/credential data |
| Is policy syntactically/risk-wise problematic? | Access Analyzer validation |
| What did a role use during period? | CloudTrail + policy generation/last-access evidence |

### Safe remediation patterns

**Missing allow**

- Add exact action/resource/condition to correct principal.
- Prefer managed reusable policy when appropriate.

**Wrong trust**

- Correct principal/action/ExternalId/MFA/org/source conditions.

**Explicit deny**

- Identify guardrail owner and intent.
- Narrow exception only if policy allows and risk approved.
- Do not add competing allow; it cannot win.

**Wrong KMS/resource policy**

- Add exact principal/service conditions and least-required actions.

**Wrong credentials/session**

- Use correct profile/role/Region and renew expired session.

### Verification after fix

```text
Retry exact request safely
  -> confirm CloudTrail success/principal/context
  -> verify intended resource effect
  -> confirm unrelated principals remain denied
  -> remove temporary test access
  -> record policy/change evidence.
```

An `Allow` result in simulator is not enough.

### Failure clues

| Symptom | First checks |
|---|---|
| Policy looks correct but request denied | Actual caller/session, explicit deny, boundary/SCP/session, context |
| Cross-account role cannot be assumed | Caller STS allow + target trust + conditions |
| Role assumed but service action denied | Role permission plus target resource/KMS/endpoint policy |
| Service can create resource but cannot write logs/S3 | Service/workload role and destination resource/KMS policy |
| Works from internet, fails through endpoint | Endpoint policy/source-VPCE condition/DNS path |
| Works for one resource, fails another | Resource ARN/tag/KMS key difference |
| Simulator allows, API denies | Missing real policy layer/context/service control/live state |
| Access Analyzer finding archived but exposure exists | Archive does not change policy |
| Generated least-privilege policy breaks rare job | Activity window missed rare action |
| No CloudTrail event | Wrong account/Region/time/data-event config or request never reached API |

### Exam traps

- Troubleshoot actual assumed-role session, not only human username.
- First identify exact action and resource ARN.
- Explicit deny cannot be repaired with another allow.
- Caller permission and role trust are both needed for cross-account AssumeRole.
- Trust policy is not the post-assumption permissions policy.
- PassRole and AssumeRole are different.
- S3 bucket ARN and object ARN serve different actions.
- Resource permission and KMS permission are separate.
- Endpoint policy can deny even when network path works.
- Device registered does not mean session has MFA context.
- CloudTrail data events must be configured for relevant object-level audit.
- Policy Simulator does not call the service or model every live control.
- Access Analyzer finding archive does not remove access.
- Policy generated from activity may omit rare/unobserved actions.
- Never attach administrator access merely to “see if IAM is the problem.”

### Do not memorize

- Every CloudTrail JSON field.
- Every Access Analyzer finding type/status.
- Exact enhanced-denial message wording.
- Full IAM evaluation edge cases.
- Console click paths.

### Ready when

Given an access problem, you can:

1. Capture principal/session, action, resource, context, and decision.
2. Trace CloudTrail and all applicable policy layers.
3. Separate AssumeRole, PassRole, resource policy, endpoint policy, and KMS failures.
4. Use Policy Simulator and Access Analyzer within their limits.
5. Apply a narrow fix and prove both intended access and retained guardrails.

---

## Skill 4.1.3 - Implement secure multi-account strategies

**Official goal:** Use accounts, organizational structure, central identities, and guardrails to reduce blast radius and govern access.

### What exam tests

- Primary: `SEL CFG BEH GOV`
- Supporting: `DIA PRC`
- Precision: `L3 - Property`
  - Exact organization/root/OU/account, SCP attachment/inheritance, permission set/assignment, delegated admin, and Control Tower control matter.

### Core model

```text
Accounts = isolation boundaries.
OUs      = policy/management grouping.
SCPs     = maximum permission guardrails.
Identity Center = workforce access.
Control Tower   = governed landing zone/account lifecycle.
```

Do not put every workload in one account and call IAM alone a multi-account strategy.

### Why multiple accounts

- Reduce failure/security blast radius.
- Separate production and nonproduction.
- Separate logging/security administration.
- Separate billing/ownership/quotas.
- Apply different guardrails by OU.
- Delegate service administration safely.
- Isolate shared network/services from workloads.

Account boundary does not remove need for least privilege inside each account.

### Common account layout

```text
Organization
  -> Security OU
       -> Log archive account
       -> Audit/security tooling account
  -> Infrastructure OU
       -> Network/shared services accounts
  -> Workloads OU
       -> Production accounts
       -> Nonproduction accounts
  -> Sandbox/Exceptions OU as governed.
```

Exact names vary. Separation of duties is the point.

### AWS Organizations object tree

```text
Organization
  -> management account
  -> root
       -> OU(s)
            -> child OU(s)
            -> member accounts.
```

Exact objects:

- Organization.
- Management account.
- Organization root.
- Organizational unit.
- Member account.
- Policy attachment.
- Delegated administrator.
- Trusted access/service integration.

An account belongs to one parent root/OU at a time.

### Management account

- Creates/manages organization and policies.
- Controls delegated administration/trusted access.
- Has consolidated billing authority.
- Should run minimal workloads.
- Protect root and privileged access heavily.

SCPs do not restrict principals in the management account.

This makes management-account compromise especially dangerous.

### Member accounts

- Hold workloads/resources.
- Receive inherited organization policies.
- Have their own root user/IAM resources/quotas.
- Can be moved between OUs.

Moving an account changes inherited policies and can immediately change access.

Test destination-OU guardrails before moving production accounts.

### Organizational units

OU groups accounts for policy and administration.

```text
Root policy
  -> parent OU policy
  -> child OU policy
  -> account policy.
```

Policies inherit down the path.

OU is not a network boundary and does not contain AWS resources directly like an account.

### Trusted access

Trusted access lets an AWS service operate across organization accounts with Organizations integration.

Can enable:

- Service-linked roles.
- Organization-wide configuration/data collection.
- Delegated administrator.

Enable only for required services and understand created roles/access.

Trusted access does not give human users automatic service access.

### Delegated administrator

```text
Management account
  -> registers member account as delegated admin
  -> member account manages supported service across organization.
```

Benefits:

- Keep daily security/service operations out of management account.
- Centralize findings/configuration.
- Separate organization ownership from service operations.

Delegation scope and supported capabilities differ by service.

Delegated admin does not bypass SCPs or resource/KMS requirements automatically.

### SCP purpose

```text
SCP = maximum available permissions
for principals in member accounts.
```

SCP:

- Can allow or deny actions.
- Inherits through root/OUs/account.
- Does not grant permission.
- Does not create IAM roles/users.
- Does not replace resource policies.
- Affects member-account IAM principals, including member-account root.

Identity/resource policy still must allow the action.

### SCP evaluation

Simplified common path:

```text
Action must be allowed by applicable SCP path
  + allowed by IAM/resource policy path
  + not explicitly denied
  -> potentially allowed.
```

Explicit SCP deny wins over IAM allow.

If using an allow-list SCP model, required action must remain allowed at every inherited level.

### Deny-list SCP model

```text
FullAWSAccess remains
  + add explicit guardrail denies.
```

Examples:

- Deny leaving organization.
- Deny disabling central CloudTrail/Config/security services.
- Deny use outside approved Regions with exceptions.
- Deny unencrypted/publicly exposed resource actions where policy supports it.

Simpler to start, but anything not denied can still be allowed by account IAM.

### Allow-list SCP model

```text
Only approved services/actions are allowed through SCP hierarchy.
```

Stronger restriction, more operational maintenance.

Need exceptions for:

- Global services.
- Required support/security/billing operations.
- Service-linked/integration behavior.
- Deployment and recovery roles.

Missing allow at any inherited level can block action.

### SCP attachment points

Attach to:

- Organization root.
- OU.
- Individual member account.

Effective account guardrails come from all policies on its path.

Do not inspect only the account attachment; parent/root policies matter.

### SCP exceptions/limits

Know:

- Management-account principals are not restricted by SCPs.
- Service-linked roles have documented SCP exceptions.
- SCPs restrict permissions; they do not affect service availability or create configuration.
- SCPs do not directly grant cross-account access.
- External principals accessing member resources have different evaluation ownership; resource-policy design still matters.

Do not use SCP as a substitute for IAM least privilege.

### Region restriction SCP

Often uses `aws:RequestedRegion` with `NotAction` exceptions.

Need care for:

- Global services/endpoints.
- Central security/logging.
- STS/IAM/Route 53/CloudFront-style global behavior.
- Cross-Region DR, backups, replication.

Bad Region deny can break authentication, logging, or recovery.

Test from a sandbox OU/account first.

### Protect central controls

Guardrail denies can protect:

- Organization trail.
- Config recorder/delivery.
- Security Hub/GuardDuty delegated setup.
- Log buckets/KMS keys.
- Required IAM/security roles.
- Backup vault/recovery points.
- Network/security baselines.

Use conditions/exceptions for authorized central service roles.

Otherwise the SCP can block its own administrators/automation.

### SCP change path

```text
Write policy
  -> validate syntax/action scope
  -> simulate/review affected services
  -> attach to test OU
  -> run positive + negative tests
  -> monitor CloudTrail/access failures
  -> expand gradually
  -> maintain emergency recovery path.
```

An SCP change can affect every account beneath an OU immediately.

### SCP failure clues

| Symptom | First checks |
|---|---|
| IAM admin policy still denied | Inherited SCP explicit deny/missing allow |
| Account worked before OU move | New parent/root SCP path |
| Only management account works | SCP does not restrict management account |
| Service integration fails everywhere | SCP blocks service action/role or trusted access absent |
| One Region fails | RequestedRegion condition/exception/global-service behavior |
| Emergency role also denied | SCP applies above IAM role; missing guarded exception |
| SCP edit has no effect in management account | Expected management-account exception |

### IAM Identity Center object model

```text
Identity source
  -> users/groups
  -> permission set
  + AWS account
  -> account assignment
  -> provisioned IAM role
  -> temporary workforce session.
```

Exact objects:

- Identity Center instance.
- Identity source.
- User/group.
- Permission set.
- Account assignment.
- Provisioned account role.
- Access portal/application.
- Session/MFA settings.

### Identity sources

Can use supported:

- Identity Center directory.
- Active Directory integration.
- External identity provider through federation/provisioning.

External identity flow commonly separates:

- Authentication/federation.
- User/group provisioning/synchronization.

User existing in IdP does not guarantee it exists/is assigned in Identity Center.

### Permission set

Defines account access through:

- AWS managed policies.
- Customer managed policy references.
- Inline policy.
- Permissions boundary where configured.
- Session duration.

Permission set is a template. Account assignment and provisioning create/update the role in target account.

### Account assignment

```text
User/group
  + permission set
  + account
  -> access shown in portal.
```

No assignment means no account/role access, even if permission set exists.

Prefer group assignments over many direct user assignments.

### Permission-set provisioning

Changing permission set requires updated provisioning to assigned accounts.

Possible problem:

```text
Permission set updated centrally
  but target account role not reprovisioned/current
  -> old permissions remain/fail.
```

Also check customer-managed policy with expected name/path exists in target accounts where referenced.

### Identity Center session behavior

- User authenticates through access portal/CLI flow.
- Chooses assigned account and permission set.
- Receives temporary role credentials.
- Session duration limits access lifetime.
- SCP/boundary/resource/KMS policies still apply.

Identity Center is not a bypass around account guardrails.

### Identity Center failure clues

| Symptom | First checks |
|---|---|
| User cannot sign in | Identity source, user state, MFA/federation, portal URL |
| User sees no account | Account assignment/group membership/sync |
| Account visible but permission set absent | Assignment and provisioning status |
| Role session gets AccessDenied | Permission set policy, boundary, SCP, resource/KMS policy |
| Recent permission update absent | Reprovisioning/status and target policy reference |
| Group user missing access | SCIM/directory sync and nested/group membership support |
| CLI session expired | Refresh Identity Center login/session |

### Control Tower purpose

Control Tower builds/governs a multi-account landing zone using Organizations and other AWS services.

```text
Landing zone
  -> governed OUs/accounts
  -> controls
  -> account factory
  -> centralized logging/audit.
```

It orchestrates governance. It does not replace Organizations/IAM/Config.

### Control Tower objects

- Landing zone.
- Home Region/governed Regions.
- Registered OU.
- Enrolled account.
- Account Factory.
- Control.
- Drift/compliance status.
- Log archive/audit accounts.

### Control types

| Control type | Behavior |
|---|---|
| Preventive | Stops prohibited actions, commonly through SCP-style guardrail |
| Detective | Detects noncompliant resources, commonly through Config |
| Proactive | Evaluates resources before provisioning, commonly through CloudFormation hooks |

Preventive blocks. Detective reports after state exists. Proactive checks before deployment.

Exact implementation can vary by control.

### Account Factory

Use to provision standardized new accounts with:

- Approved OU placement.
- Baseline identity/governance.
- Required account metadata.
- Landing-zone controls.

Account creation success does not prove every workload baseline/StackSet completed. Verify enrollment and provisioned baselines.

### Control Tower drift

Drift means governed setup differs from expected landing-zone configuration.

Causes:

- Manual Organizations/IAM/Config changes.
- Deleted/changed required roles/resources.
- OU/account changes outside supported workflow.
- Failed baseline update.

Do not “fix” drift by deleting central resources. Use Control Tower repair/update workflow and underlying evidence.

### Central security/logging services

Common design:

- Organization CloudTrail -> protected log archive account.
- Config aggregation/conformance -> central compliance account.
- Security Hub/GuardDuty -> delegated security administrator.
- Central KMS/log bucket policies.
- AWS Backup policies/vaults in protected accounts.
- RAM for shared network/resources.
- StackSets for account baselines.

Central collection still needs member-account enablement, trusted access, roles, Region coverage, and destination policies.

### Organization trail

- Created from management/delegated configuration as supported.
- Applies to member accounts.
- New member accounts join coverage according to trail configuration.
- Deliver to centralized S3/CloudWatch destination where configured.

Protect:

- Trail configuration.
- Log bucket policy.
- KMS key.
- Log-file validation/retention.
- Access to log archive account.

Logging in same workload account weakens isolation.

### Break-glass access

Design emergency access before incident:

- Separate tightly controlled role/account path.
- Strong MFA and approval.
- Short sessions.
- Minimal required exceptions.
- Alert on every use.
- Test regularly.
- Review and revoke temporary changes afterward.

Break-glass must still work under intended SCPs—or have a controlled organizational recovery procedure.

Do not create a permanent unmonitored administrator exception.

### Evidence

**Organizations/SCP**

- Account parent/OU path.
- Policies attached at root/OU/account.
- Trusted-access/delegated-admin state.
- CloudTrail organization-policy/account-move changes.
- Exact access-denied policy context.

**Identity Center**

- Identity source/sync.
- User/group membership.
- Account assignment.
- Permission-set content/provisioning status.
- Generated role and session ARN.

**Control Tower**

- Landing-zone version/status.
- OU/account enrollment.
- Control enablement/compliance.
- Drift and underlying Config/CloudFormation/Organizations evidence.

### Safe multi-account operating path

```text
Define account boundaries
  -> create OU hierarchy
  -> centralize identity/log/security
  -> design/test SCP guardrails
  -> delegate daily service administration
  -> enroll/vend accounts through governed workflow
  -> deploy baselines with StackSets
  -> monitor drift/compliance
  -> test break-glass and recovery.
```

### Failure clues

| Symptom | First checks |
|---|---|
| Admin role denied in member account | SCP path, boundary, permission set/session, resource/KMS policy |
| New account lacks baseline | OU target, auto-deployment/StackSet, enrollment/trusted access |
| Security service misses accounts | Delegated admin, trusted access, member enablement, Region coverage |
| Central logs absent | Organization trail, bucket/KMS policy, member coverage |
| Control reports noncompliant | Control type, resource/evaluation, Config status, exception |
| Control Tower account drifted | Manual changes, landing-zone version, repair workflow |
| Account move causes outage | Destination OU inherited SCP/control/baseline |
| Identity Center role too broad/narrow | Permission set + boundary + SCP + provisioning |

### Exam traps

- Account is security/blast-radius boundary; OU is management/policy grouping.
- SCP limits maximum permission; it never grants.
- IAM administrator policy cannot override an SCP deny.
- SCP inheritance includes root, every parent OU, and account attachment.
- SCP does not restrict the management account.
- Service-linked roles have SCP exceptions.
- Moving account to another OU changes inherited guardrails.
- Trusted access is service integration, not human access.
- Delegated administrator is service-specific, not organization owner.
- Permission set alone gives no access; account assignment is required.
- Identity Center sessions still obey SCP/resource/KMS controls.
- Preventive blocks; detective reports; proactive checks before provision.
- Control Tower builds on Organizations/Config/CloudFormation; it does not replace them.
- Central service configuration still needs Region/account coverage and destination policies.

### Do not memorize

- Every Organizations policy type.
- Every Control Tower control name.
- Exact Identity Center generated-role naming suffix.
- Every service’s delegated-admin limit.
- Console click paths.

### Ready when

Given a multi-account security scenario, you can:

1. Design account/OU boundaries and delegated administration.
2. Predict SCP inheritance, allow/deny behavior, and management-account exception.
3. Configure Identity Center identity -> permission set -> account assignment.
4. Explain Control Tower landing zone, account factory, control types, and drift.
5. Centralize logs/security services and troubleshoot missing coverage/access.

---

## Skill 4.1.4 - Remediate Trusted Advisor security checks

**Official goal:** Validate a Trusted Advisor security recommendation, remediate it safely, and prove the risk is reduced without breaking the workload.

### What exam tests

- Primary: `EVD DIA REM PRC`
- Supporting: `GOV`
- Precision: `L2 - Object`
  - Know check, status, affected resource, recommendation, refresh/evaluation, exclusion, owner, and verification evidence.

### Core model

```text
Trusted Advisor check
  -> affected resource
  -> recommended security change
  -> validate context/blast radius
  -> remediate
  -> verify workload + refreshed check.
```

Trusted Advisor advises. It does not normally enforce the configuration by itself.

### Trusted Advisor check object

Read:

- Check name/ID.
- Category.
- Description/criteria.
- Overall status.
- Affected resource(s).
- Account and Region.
- Resource status/metadata.
- Recommended action.
- Last refresh/evaluation time.
- Excluded/suppressed status.
- Feature/support-plan availability.

One check can list many resources. Fixing one does not clear the others.

### Status model

Recognition:

- Error/action recommended.
- Warning/investigation recommended.
- OK/no current issue detected.
- Excluded/suppressed.
- Not available/unknown where applicable.

Color/label details can vary by experience/API. Read the status meaning and resource metadata.

### Security check examples

Possible themes:

- Security group exposes risky ports.
- S3 resource is publicly accessible.
- Root/IAM MFA or credential weakness.
- Old/unused access keys.
- CloudTrail/logging not protected or enabled.
- Public database/snapshot/resource sharing.
- Certificate expiration/renewal risk.
- Encryption or service-specific security setting.

The exam tests the remediation reasoning, not a fixed catalog of every current check.

### First response

Do not click “fix” blindly.

```text
1. Confirm check definition.
2. Confirm exact resource/account/Region.
3. Inspect current live configuration.
4. Identify resource owner/business purpose.
5. Decide if exposure is required.
6. Find least-permissive valid replacement.
7. Capture rollback/current state.
8. Change through approved path.
9. Test workload and security.
10. Refresh/wait for reevaluation.
```

### Check freshness

Trusted Advisor result can lag the live resource.

```text
Live state changed
  -> check still shows old result
  -> refresh or wait for next evaluation
  -> verify timestamp.
```

Refresh behavior/frequency and available checks depend on check type, integration, and support/feature level.

Do not revert a correct fix just because an advisory view is stale.

### Support/feature availability

- Check catalog/API/refresh/organization features can depend on support plan or service integration.
- Some checks are available broadly; others have different access/refresh behavior.
- Do not memorize one permanent support-plan matrix.
- If result is unavailable, verify entitlement, Region/account, service state, and permissions.

Exam answer should meet the security requirement, not merely choose a higher support plan unless availability is the actual blocker.

### Evidence hierarchy

```text
Trusted Advisor recommendation
  -> live service configuration
  -> CloudTrail/Config history
  -> workload/network/access evidence
  -> refreshed Trusted Advisor result.
```

Trusted Advisor is the signal. Live resource state is the change target.

### Security-group remediation

Finding example:

```text
Inbound TCP 22/3389
from 0.0.0.0/0 or ::/0.
```

Validate:

- Which SG/rule/resource.
- IPv4 and IPv6 exposure.
- Is port actually required?
- Current administration path/users.
- Referencing SG, CIDR, prefix list, VPN/private path alternatives.

Safer fixes:

- Remove unused rule.
- Narrow to approved source CIDR/prefix list/security group.
- Use VPN/private connectivity.
- Use Session Manager and remove inbound admin port.

Verify administrators still have approved access.

### Public web-service boundary

Public access can be intentional.

```text
Internet-facing ALB on 443
  -> public ingress may be required.

EC2 target on app port
  -> allow from ALB security group, not whole internet.
```

Do not make a public application private without replacement traffic path.

Narrow each tier to its real caller.

### S3 public-access remediation

Check:

- Account/bucket Block Public Access.
- Bucket/access-point policy.
- ACL/Object Ownership.
- Website hosting requirement.
- CloudFront origin access design.
- Cross-account partners versus true public principal.

Fix direction:

- Enable appropriate Block Public Access.
- Remove/narrow public policy/ACL.
- Use CloudFront origin access control or authenticated access where required.
- Keep approved cross-account access explicit and conditional.

Test application delivery before/after.

“Public” and “cross-account” are not always the same risk path.

### Root/MFA remediation

- Enable strong MFA/passkey for root.
- Remove root access keys where they exist and are not required.
- Secure recovery channels.
- Alert on root use.
- Move daily operations to federated/role access.

MFA enrollment needs secure custody/recovery process.

Do not use root as a permanent automation identity.

### Access-key remediation

For old/unused key:

```text
Identify owner/workload
  -> inspect last-used evidence
  -> create/shift to role or rotate key
  -> verify new credential
  -> deactivate old key
  -> monitor
  -> delete after rollback window.
```

Immediate deletion without ownership check can cause outage.

If compromised, containment/rotation urgency overrides normal grace period.

### CloudTrail/logging remediation

Possible fix:

- Enable multi-Region/organization trail where required.
- Include required management/data events.
- Deliver to protected central bucket/log group.
- Encrypt with correct KMS policy.
- Enable validation/retention controls.
- Restrict trail/log deletion and modification.

Verify:

- Events arrive from expected accounts/Regions.
- Bucket and KMS policies allow delivery.
- Operators/security tools can read logs.
- Workload roles cannot alter central evidence.

Trail “created” does not prove logs are delivered.

### Public snapshot/resource-share remediation

- Confirm snapshot/resource and owner.
- Remove public restore/share permission.
- Keep only approved account/organization principals.
- Review copies created while public.
- Check KMS encryption/key policy.
- Monitor CloudTrail for access/config changes.

Making future access private cannot recall copies already made.

### Certificate remediation

Check:

- Certificate ARN/Region.
- Expiration/status.
- ACM-managed versus imported.
- DNS/email validation state.
- Certificate in use by listener/distribution.
- DNS validation record and renewal reachability.

Fix:

- Restore ACM renewal prerequisites, or
- Import/request replacement and attach it safely.

Validate TLS hostname, chain, policy, and client traffic before removing old certificate.

### Encryption-setting remediation

Before changing encryption:

- Identify service/resource and supported in-place behavior.
- Confirm KMS key policy/grants.
- Determine whether copy/replacement/migration is required.
- Preserve rollback/data.
- Update application/service roles.

Enabling a customer-managed key without permissions can cause outage.

### AWS Config-powered checks

Some Trusted Advisor checks use AWS Config managed-rule evaluations.

Path:

```text
Config recorder/resource coverage
  -> Config rule evaluation
  -> Trusted Advisor result.
```

If result is missing/stale:

- Config recorder enabled/running?
- Correct resource types/Region recorded?
- Delivery/evaluation working?
- Rule/check scope correct?
- Resource recently changed and awaiting evaluation?

Do not create duplicate remediation that fights an existing Config automation.

### Automation options

Possible controlled flow:

```text
Trusted Advisor/Config event
  -> EventBridge
  -> SNS approval/notification
  -> Systems Manager Automation/Lambda
  -> validate
  -> audit result.
```

Automation needs:

- Exact resource targeting.
- Least-privilege execution role.
- Idempotency/current-state check.
- Concurrency/error control.
- Approval for high-impact changes.
- Rollback/exception path.

Avoid automatic deletion or access closure from a broad check alone.

### Exclusion/suppression

Exclude only when risk is intentionally accepted or check does not fit approved design.

Record:

- Business justification.
- Owner/approver.
- Scope/resource.
- Compensating controls.
- Expiry/review date.
- Evidence.

```text
Exclude finding
  != remediate resource.
```

Exclusion hides/suppresses workflow noise; underlying configuration remains.

### IaC ownership

If resource is managed by CloudFormation/Terraform:

```text
Fix IaC source
  -> preview
  -> deploy
  -> verify drift resolved/check refreshed.
```

Direct console fix alone can create drift and be reverted by the next deployment.

Emergency console fix may be justified, but reconcile code immediately afterward.

### Verification model

Security verification:

- Exposure/weak setting removed.
- Intended principals/path still allowed.
- Unintended path denied.
- CloudTrail/Config records change.
- Trusted Advisor refresh clears/reduces affected resource.

Workload verification:

- Availability/health checks.
- Authentication/administration path.
- Application errors/latency.
- Partner/customer access.
- Logging/monitoring still works.

Need both.

### Failure clues

| Symptom | First checks |
|---|---|
| Check remains red after change | Refresh timestamp, wrong resource/Region, incomplete IPv4/IPv6/policy fix |
| Check disappeared but risk remains | Resource excluded/suppressed or scope/Config recording changed |
| Fix causes outage | Required public/admin/service path removed; rollback and narrow correctly |
| S3 still public | BPA, bucket/access-point policy, ACL, website/CloudFront design |
| SG check persists | Another rule/SG, IPv6 `::/0`, wrong port/resource |
| Trail check persists | Trail not multi-Region/org, delivery/KMS/bucket failure |
| Certificate still warns | Renewal validation/Region/attachment/imported certificate issue |
| Automation denied | Execution role, PassRole, resource/KMS policy, SCP |
| Automation repeats | Config/TA reevaluation loop and non-idempotent remediation |
| Check unavailable | Support/feature entitlement, permissions, account/Region/integration |

### Safe remediation path

```text
Read check + affected resource
  -> verify live state/evidence
  -> identify owner and required access
  -> choose least-permissive valid design
  -> capture rollback/current state
  -> change via IaC/approved automation
  -> test security + workload
  -> refresh/reevaluate
  -> close or document time-bound exception.
```

### Exam traps

- Trusted Advisor recommendation is advisory, not automatic enforcement.
- Check result can be stale; inspect refresh/evaluation time.
- One check can have multiple affected resources.
- Excluding a resource does not fix it.
- Green check does not prove every security requirement.
- Closing public access blindly can break a required application path.
- Check both `0.0.0.0/0` and `::/0`.
- CloudTrail created does not prove log delivery.
- MFA/key remediation needs ownership and recovery planning.
- Config-powered result depends on recorder/rule coverage.
- Direct fix to IaC-owned resource can drift/revert.
- Automation needs least privilege, idempotency, approval, and rollback.
- Support-plan/check availability can vary; do not memorize a static catalog.

### Do not memorize

- Every Trusted Advisor check name/ID.
- Exact refresh interval for every check.
- Permanent support-plan entitlement matrix.
- Console color/icon details.
- Console click paths.

### Ready when

Given a Trusted Advisor security result, you can:

1. Read check/status/resource/recommendation/freshness precisely.
2. Validate live exposure, owner, business purpose, and blast radius.
3. Choose least-permissive remediation without breaking valid traffic.
4. Handle Config integration, automation, exclusions, and IaC ownership.
5. Prove both security improvement and workload health after refresh.

---

## Skill 4.1.5 - Enforce compliance requirements and continuous monitoring

**Official goal:** Record resource configuration, evaluate it against policy, remediate noncompliance, and enforce approved Region/service boundaries.

### What exam tests

- Primary: `CFG EVD REM GOV`
- Supporting: `DIA PRC SEL`
- Precision: `L2 - Object`
  - Know recorder, delivery channel, configuration item, rule, trigger, compliance state, conformance pack, aggregator, remediation, and guardrail.

### Core AWS Config model

```text
Resource configuration/change
  -> configuration recorder
  -> configuration item/history
  -> Config rule evaluation
  -> compliant/noncompliant
  -> manual or automatic remediation.
```

AWS Config records and evaluates. It does not block ordinary resource creation by itself.

### Prevent, detect, remediate

| Need | Control type/example |
|---|---|
| Stop prohibited API action | SCP/preventive Control Tower control |
| Reject noncompliant CloudFormation before creation | Proactive control/hook where supported |
| Detect existing bad configuration | AWS Config rule/detective control |
| Fix detected resource | SSM Automation remediation |

Choose from timing requirement.

```text
Must never happen -> preventive/proactive.
Can detect and repair -> Config + remediation.
```

### AWS Config object tree

```text
Configuration recorder
  -> recording scope/resource types
  -> configuration items/history

Delivery channel
  -> S3 snapshot/history delivery
  -> optional SNS notification

Config rule
  -> evaluation
  -> compliance result
  -> remediation configuration.
```

### Configuration recorder

Recorder controls what Config records.

Exact settings:

- Recorder name/type.
- Recording enabled/stopped state.
- IAM/service-linked role.
- All supported resource types versus selected types.
- Inclusion/exclusion strategy where supported.
- Global-resource recording choice.
- Recording frequency/strategy where supported.

No recording means rules can lack current configuration evidence.

### Recording scope

Choose deliberately:

- All supported resources.
- Selected resource types.
- Excluded resource types where supported.
- Global IAM/resource types where required.

Trade-off:

```text
Broad recording -> better coverage + more configuration items/cost.
Narrow recording -> lower volume + blind spots.
```

Config is Regional. Configure every governed Region and handle global resource recording deliberately to avoid gaps/duplication.

### Delivery channel

Delivery channel can define:

- S3 bucket/prefix.
- SNS topic.
- Snapshot delivery frequency.
- KMS/bucket/topic permissions where used.

Recorder collects configuration. Delivery channel delivers snapshots/history/notifications.

Do not confuse recorder with delivery channel.

### Configuration item/history

Configuration item describes a resource at a point/change:

- Resource type and ID/ARN.
- Account and Region.
- Configuration/state.
- Tags.
- Relationships to other resources.
- Capture/change time.
- Status.

Configuration history/timeline helps answer:

```text
What changed, when, and what was related?
```

CloudTrail answers who made the API call. Config answers how recorded configuration changed.

### Config rule types

| Rule | Logic owner |
|---|---|
| AWS managed rule | AWS supplies evaluation logic; operator sets parameters/scope |
| Custom Lambda rule | Customer Lambda evaluates configuration/periodic state |
| Custom policy rule | Customer policy logic, such as Guard, where supported |

Prefer managed rule when it exactly matches requirement.

Custom rule needs code/policy lifecycle, permissions, logging, and tests.

### Rule scope

Can narrow by supported:

- Resource type.
- Resource ID.
- Tag key/value.
- Account/Region deployment.
- Rule parameters.

Wrong scope can create false compliance or no evaluation.

Rule attached in one Region does not automatically evaluate every Region/account.

### Trigger types

**Configuration change**

```text
Relevant recorded resource changes
  -> evaluate rule.
```

Good for supported configuration drift.

**Periodic**

```text
Schedule interval
  -> evaluate current state.
```

Good for conditions not tied to one supported configuration-item change.

Some rules support one or both. Choose from check logic.

### Compliance states

Recognize:

- `COMPLIANT`
- `NON_COMPLIANT`
- `NOT_APPLICABLE`
- `INSUFFICIENT_DATA`

Meaning:

- Compliant: rule says requirement met for evaluated item.
- Noncompliant: requirement failed.
- Not applicable: rule does not apply.
- Insufficient data: Config/rule lacks enough valid evidence/evaluation.

Compliant with one rule does not mean resource is globally compliant.

### Rule parameters

Managed rule behavior often depends on parameters:

- Allowed values/ranges.
- Required tag keys.
- Approved ports/instance types.
- KMS key/reference.
- Retention/age.

Wrong parameter can mark valid resources noncompliant—or weak resources compliant.

Treat parameters as policy, version and review them.

### Evaluation evidence

Read:

- Rule name/ARN.
- Resource type/ID.
- Compliance state.
- Evaluation timestamp.
- Ordering timestamp.
- Annotation/reason.
- Rule parameters/scope.
- Trigger/evaluation mode.
- Related configuration item.

Start with the exact noncompliant resource and annotation.

### Managed-rule failure clues

| Symptom | First checks |
|---|---|
| Rule evaluates nothing | Recorder scope, resource type/Region, rule scope/trigger |
| `INSUFFICIENT_DATA` | Recorder stopped/missing type, recent resource, permission/evaluation problem |
| Unexpected noncompliance | Rule parameters, current config, evaluation freshness |
| Unexpected compliance | Wrong resource/scope/tag/Region or weak parameter |
| Compliance stale | Resource not recorded, trigger/period not reached, evaluation backlog |

### Custom Lambda rule

Needs:

- Lambda invocation permission for Config.
- Function execution role.
- Correct event parsing/resource scope.
- `PutEvaluations`/required Config interaction.
- Timeout/concurrency/logging.
- Idempotent evaluation.

Failure evidence:

- Rule error/status.
- Lambda logs/errors/throttles.
- Resource/KMS/network dependencies.

Function success does not prove correct compliance logic.

### Conformance packs

```text
Conformance pack template
  -> Config rules
  -> parameters
  -> optional remediation configurations
  -> pack compliance.
```

Use to deploy a repeatable compliance framework.

Exact objects:

- Pack name/template.
- Input parameters.
- Included rules.
- Remediation definitions.
- Account/organization deployment.
- Region.
- Delivery/configuration prerequisites.
- Pack/rule compliance result.

### Conformance-pack behavior

- Packages rules/remediations consistently.
- Can deploy by account/organization/Region with supported mechanism.
- Each underlying rule still evaluates resources.
- Requires Config foundation/permissions in target scope.
- Updating pack can add/change/remove rules.

Conformance pack is not:

- A legal certification.
- A preventive firewall by itself.
- Automatic proof every account/Region is covered.
- Automatic business approval for every remediation.

### Organization conformance packs

Need:

- Organizations trusted/service access where required.
- Management/delegated administrator permissions.
- Target accounts/Regions.
- Config recorder/delivery prerequisites.
- Execution/remediation roles.
- S3/KMS access for templates/delivery where used.

One failed member account can have different quota/IAM/Region cause than others.

### Aggregator

```text
Source accounts/Regions
  -> configuration aggregator
  -> centralized inventory/compliance view.
```

Use for:

- Multi-account/Region resource inventory.
- Rule/conformance compliance summary.
- Central queries/reporting.

Aggregator:

- Collects views/data references.
- Does not record source resources itself.
- Does not deploy rules.
- Does not automatically remediate.

Source accounts/Regions still need Config and authorization/organization integration.

### Aggregator failure clues

| Symptom | First checks |
|---|---|
| One account absent | Aggregation authorization/org source/account status |
| One Region absent | Region source selection and recorder/rules there |
| Resources visible but no compliance | Rules not deployed/evaluating in source |
| Stale central view | Source recording/evaluation and aggregation lag |
| Query shows nothing | Resource type/Region/account scope and Config coverage |

### Remediation types

**Manual remediation**

- Operator selects/executes approved action.
- Good for high-risk/context-heavy fixes.

**Automatic remediation**

- Config triggers Systems Manager Automation for noncompliant resource.
- Good for deterministic, reversible, well-tested fixes.

Choose by blast radius and context.

### Remediation object model

```text
NON_COMPLIANT evaluation
  -> remediation configuration
  -> SSM Automation document
  -> parameters/resource ID
  -> assume role
  -> execution controls/retries
  -> resource changed
  -> Config reevaluates.
```

Exact settings:

- Target Automation document/version.
- Automatic versus manual.
- Static/dynamic resource parameters.
- Automation assume role.
- Maximum attempts/retry interval.
- Concurrency/error controls where supported.
- Remediation exception.

### Automatic-remediation safety

Need:

- Current-state check.
- Exact resource targeting.
- Idempotent action.
- Least-privilege role.
- Bound concurrency/error rate.
- Rollback/backup for stateful change.
- Verification and reevaluation.
- Loop prevention.

Config evaluation can be stale when remediation starts. Runbook must inspect live state.

### Remediation exceptions

Use for approved temporary/permanent exception according to governance.

Record:

- Resource/rule.
- Reason.
- Owner/approver.
- Expiration/review date.
- Compensating controls.

Exception changes remediation/compliance workflow. It does not technically make insecure configuration safe.

### Remediation failure clues

| Symptom | First checks |
|---|---|
| Automatic remediation never starts | Automatic config, target mapping, exception, evaluation state |
| Automation AccessDenied | Config/PassRole, assume role, resource/KMS policy, SCP |
| Wrong resource changed | Dynamic parameter/resource ID mapping |
| Automation succeeds but remains noncompliant | Fix incomplete, rule parameter, reevaluation delay |
| Remediation repeats | Non-idempotent fix, evaluation loop, resource owner reverting |
| Too many resources change | Broad rule scope/concurrency and no staged deployment |

### Region restriction choices

| Requirement | Main control |
|---|---|
| Prevent member-account API use in disallowed Regions | SCP with Region conditions/exceptions |
| Detect resources in disallowed Region | Config rule/aggregator |
| Govern Control Tower accounts/Regions | Control Tower controls |
| Prevent unapproved service actions | SCP/service-specific preventive control |
| Detect unapproved service/resource use | Config/inventory/CloudTrail/Security Hub reporting |

Preventive and detective controls should complement each other.

### Region SCP pattern

Concept:

```text
Deny actions when aws:RequestedRegion is not approved
  except required global/security/billing/support actions.
```

Need exceptions for:

- Global services/endpoints.
- Identity and organization operations.
- Central logs/security monitoring.
- Backup/replication/DR.
- Automation/support operations.

Test actual API behavior. Requested Region condition does not mean resource physical location in every global-service case.

### Service restriction

SCP can deny unapproved service actions, but:

- It does not delete existing resources.
- It does not grant approved-service permissions.
- It can break CloudFormation/automation dependencies.
- Service-linked-role behavior has exceptions.
- Required read/audit actions may need allowance.

Pair with Config/CloudTrail inventory to find existing use.

### Continuous monitoring evidence

Combine:

- Config resource timeline/history.
- Rule/conformance evaluations.
- Aggregator queries.
- CloudTrail actor/API history.
- Security Hub findings.
- EventBridge notifications.
- SSM Automation execution.
- Control Tower control/drift status.
- Compliance reports/exceptions.

No one signal proves full compliance.

### Notifications and workflow

```text
NON_COMPLIANT event
  -> EventBridge/SNS
  -> ticket/owner/automation
  -> remediation
  -> Config reevaluation
  -> evidence/closure.
```

Notification without owner/action is monitoring noise.

### Safe implementation path

```text
Define requirement and scope
  -> choose preventive/detective/proactive/remedial control
  -> enable Config recording/delivery in all target Regions
  -> deploy/test rule parameters
  -> aggregate/report
  -> canary remediation
  -> control concurrency/role
  -> reevaluate and document exceptions
  -> monitor coverage/drift continuously.
```

### Failure clues

| Symptom | First checks |
|---|---|
| No Config data | Recorder state/role/scope/Region |
| Snapshots not delivered | Delivery channel, S3/SNS/KMS policy |
| Rule misses resource | Recording type, rule scope/tag, Region, trigger |
| Pack deployment fails | Template/parameters, Config prerequisite, IAM/S3/KMS, target Region |
| Aggregator missing members | Authorization/trusted access/source selection |
| SCP blocks required automation | RequestedRegion/service deny and exception role/actions |
| Config detects but violation continues | No remediation/owner, automation failed, resource reverted |
| Compliance suddenly improves suspiciously | Recorder/rule disabled or scope narrowed |

### Exam traps

- Config recorder records; Config rule evaluates.
- Delivery channel delivers; it does not evaluate.
- Config is Regional; one Region does not cover all Regions.
- CloudTrail shows API activity; Config shows resource configuration history.
- `COMPLIANT` means one rule passed, not total compliance.
- `INSUFFICIENT_DATA` is not compliant.
- Conformance pack groups rules; it is not legal certification.
- Aggregator centralizes visibility; it does not record/deploy/remediate.
- Automatic remediation must inspect live state because evaluations can be stale.
- Exception suppresses/changes workflow; it does not remove technical risk.
- SCP prevents actions; Config normally detects after configuration exists.
- SCP does not delete existing disallowed resources.
- Region restrictions need global/security/backup/DR exceptions.
- Restricting services can break IaC and operational dependencies.

### Do not memorize

- Every Config managed rule.
- Exact delivery/evaluation timing.
- Full conformance-pack YAML syntax.
- Every global-service Region exception.
- Console click paths.

### Ready when

Given a compliance scenario, you can:

1. Configure recorder, delivery channel, resource coverage, and Regions.
2. Choose managed/custom rule, change/periodic trigger, scope, and parameters.
3. Deploy conformance packs and aggregate multi-account/Region evidence.
4. Configure safe SSM remediation and governed exceptions.
5. Choose SCP/Control Tower prevention versus Config detection/remediation.

---

## Skill 4.2.1 - Implement and enforce a data classification scheme

**Official goal:** Identify data sensitivity, label it, and apply access, encryption, retention, monitoring, backup, and deletion controls that match the class.

### What exam tests

- Primary: `SEL CFG EVD GOV`
- Supporting: `REM`
- Precision: `L2 - Object`
  - Know classification level, owner, storage scope, Macie discovery/job/identifier/allow list/finding, and mapped control.

### Core model

```text
Discover/inventory data
  -> classify sensitivity
  -> assign owner and tags/metadata
  -> apply controls
  -> monitor findings/drift
  -> retain/archive/delete by policy.
```

Classification without enforcement is only a label.

### Classification dimensions

Classify from:

- Data type: public, personal, financial, health, credential, intellectual property, logs.
- Sensitivity/impact if exposed.
- Regulatory/contractual requirement.
- Data owner/business purpose.
- Account/Region/residency.
- Required retention/deletion.
- Required availability/recovery.
- Sharing/consumer population.

Do not classify only from filename or bucket name.

### Example classification levels

| Class | Meaning | Typical control direction |
|---|---|---|
| Public | Approved for public release | Integrity, availability, approved publication path |
| Internal | Organization use | Authenticated access, encryption, standard logging |
| Confidential | Material harm if exposed | Least privilege, stronger audit, restricted sharing/KMS controls |
| Restricted | Highest legal/security impact | Tight account/Region/principal controls, strong monitoring/retention/deletion governance |

Names differ by organization. The control mapping matters.

### Control matrix

For each class define:

- Allowed storage services/accounts/Regions.
- Public/cross-account access.
- Encryption at rest and key ownership.
- Encryption in transit.
- IAM/ABAC requirements.
- CloudTrail/data-access logging.
- Retention/lifecycle/Object Lock.
- Backup/replication/DR.
- Masking/tokenization where required.
- Incident response/notification.
- Approved destruction.

One class may need several controls.

### Ownership metadata

Useful metadata/tags:

- Classification.
- Data owner.
- Application/business unit.
- Environment.
- Retention class/date.
- Residency/Region restriction.
- Compliance scope.

Protect tag mutation. If tags drive authorization/lifecycle, unauthorized retagging can bypass policy or delete data.

### Data lifecycle

```text
Create/ingest
  -> classify/tag
  -> store/use/share
  -> monitor/access review
  -> archive/retain
  -> delete and record evidence.
```

Classification can change. Reclassify when content, purpose, owner, or regulation changes.

### Amazon Macie purpose

```text
S3 objects/bucket posture
  -> Macie analyzes
  -> sensitive-data/policy findings and discovery results
  -> security workflow.
```

Macie focuses on sensitive-data discovery and S3 security posture.

Macie does not scan EBS/RDS/EFS files directly as a general data classifier.

### Macie object model

```text
Macie account/administrator
  -> S3 bucket inventory
  -> automated sensitive-data discovery
     or sensitive-data discovery job
  -> identifiers/allow lists
  -> findings/results/coverage.
```

Exact objects:

- Macie administrator/member account.
- S3 bucket inventory.
- Automated sensitive-data discovery settings.
- Sensitive-data discovery job.
- Managed data identifier.
- Custom data identifier.
- Allow list.
- Finding.
- Discovery result/repository where configured.
- Suppression/archival workflow.

### Multi-account Macie

Common model:

```text
Delegated Macie administrator
  -> member accounts
  -> centralized findings/inventory.
```

Need:

- Organizations/delegated-admin integration or invitations as applicable.
- Macie enabled in required accounts/Regions.
- Member association/status.
- S3/KMS/service-role permissions.

Macie is Regional. Enable and review every governed Region.

### Automated sensitive-data discovery

Use for ongoing broad visibility with less job-by-job setup.

Behavior:

- Continuously selects/analyzes eligible S3 objects.
- Builds bucket/data sensitivity profiles and coverage information.
- Uses configured managed/custom identifiers and allow lists.
- Updates as analysis continues.

Use when continuous estate-wide discovery is the clue.

It samples/analyzes according to service behavior; it is not proof every byte was inspected immediately.

### Sensitive-data discovery job

Use for explicit scoped analysis.

Job settings can include:

- Job name/description.
- One-time or scheduled execution.
- Selected buckets or bucket criteria.
- Account/Region scope.
- Include/exclude criteria.
- Sampling depth/percentage where configured.
- Managed data identifiers.
- Custom data identifiers.
- Allow lists.
- Tags.

Use for audit, incident, migration, known dataset, or targeted validation.

### Automated discovery versus job

| Need | Choose |
|---|---|
| Ongoing broad S3 sensitivity visibility | Automated discovery |
| Exact buckets/schedule/identifier set for an investigation | Discovery job |
| Verify one remediation/data set | Targeted job |

They can coexist.

### Managed data identifiers

AWS-maintained detection logic for common sensitive-data types, such as:

- Credentials/secrets.
- Personal identifiers.
- Financial information.
- Health-related identifiers.
- Location/contact identifiers.

Select identifiers matching policy/jurisdiction/use case.

More identifiers increase discovery breadth and possible noise/cost.

### Custom data identifier

Use for organization-specific patterns:

- Employee/customer IDs.
- Internal account/reference numbers.
- Proprietary labels/secrets.

Can use pattern/regular expression plus contextual keywords/proximity rules where supported.

Test against:

- True positive examples.
- Near-miss false positives.
- Formatting variations.
- Large/realistic sample data.

Weak regex can create noise or miss data.

### Allow list

Allow list tells Macie certain matching text/patterns are expected and should not count as sensitive occurrence for that identifier context.

Use for:

- Known public sample/test values.
- Safe identifiers that resemble sensitive data.

Risk:

```text
Broad allow list
  -> real sensitive data hidden.
```

Version/review allow lists like security policy.

### Macie analysis coverage

An object can be skipped/limited because of:

- Unsupported file/storage format/class/state.
- Object too large or service analysis limits.
- S3/KMS permission denial.
- Cross-account key/policy issue.
- Corrupt/compressed/encrypted content handling limitation.
- Job scope/filter/sampling.
- Object added outside analysis window.

Read coverage/classification status before concluding “no sensitive data.”

### KMS and S3 access path

Macie needs authorized access to eligible S3 object data.

Check:

- Macie service-linked role/service permissions.
- Bucket/access-point policy.
- Object ownership.
- KMS key policy/grant for SSE-KMS objects.
- SCP/Region restriction.
- Member/admin account relationship.

Bucket visibility does not prove encrypted object content can be analyzed.

### Finding types at high level

**Sensitive-data finding**

- Sensitive data detected in S3 object(s).
- Includes resource/location, type/count/severity/context.

**Policy finding**

- S3 bucket policy/posture creates public or cross-account/access risk.

Do not treat every finding as confirmed breach. It is detected data or risk condition requiring validation.

### Finding fields

Read:

- Finding type/title.
- Severity.
- Account/Region.
- Bucket/object resource.
- Sensitive-data category/type/count.
- Discovery method/job.
- Created/updated/count.
- Access/public/shared posture.
- Encryption/storage information.
- Evidence/sample location/details available without exposing data unnecessarily.

Severity helps priority. It does not replace business classification.

### Findings versus discovery results

- Finding: security workflow signal, deliberately limited/summarized.
- Discovery result: detailed analysis record stored/configured for audit where enabled.

Protect the result repository and its KMS key. Discovery evidence can itself be sensitive.

Do not copy raw sensitive values into tickets/chat unnecessarily.

### Finding routing

```text
Macie finding
  -> Security Hub and/or EventBridge
  -> notification/ticket/automation
  -> owner validates/remediates
  -> rescan/recheck
  -> close/archive with evidence.
```

Use event pattern by finding type/severity/account/resource.

Automation should not delete data solely from one finding.

### Enforcement controls for S3

Use classification metadata with:

- IAM identity policies.
- S3 bucket/access-point policies.
- Block Public Access.
- Object Ownership/ACL controls.
- KMS keys/key policies.
- TLS-only `aws:SecureTransport` deny.
- VPC endpoint/source conditions.
- S3 Object Lock/versioning.
- Lifecycle/retention.
- Replication/backup.
- CloudTrail S3 data events.
- Config rules/Control Tower/SCP guardrails.

Macie discovers. These controls enforce.

### Tag-based enforcement

Example:

```text
Resource/Object classification=restricted
  -> deny public access
  -> require approved principal/KMS key/endpoint
  -> apply retention/logging controls.
```

Need:

- Reliable tag at creation/ingest.
- Restricted tag mutation.
- Handling for missing tag.
- Services/actions that support relevant tag condition.
- Config rule to detect missing/wrong tag.

Default-deny or quarantine unclassified data where policy requires.

### Sensitive public-object response

```text
Validate finding
  -> preserve evidence
  -> contain public/cross-account path
  -> identify owner/data subjects
  -> assess access history
  -> rotate exposed credentials if found
  -> encrypt/relocate/delete under policy
  -> update guardrail
  -> rescan and document.
```

Do not destroy evidence before incident/security review.

### Remediation choices

Depending on class/policy:

- Remove/narrow bucket/access-point policy or ACL.
- Enable Block Public Access.
- Move/copy to approved account/Region/bucket.
- Encrypt using approved KMS key through supported copy/migration.
- Restrict principals/network path.
- Apply Object Lock/retention/lifecycle.
- Enable versioning/backup/replication.
- Add classification/owner tags.
- Rotate secret/credential found in object.
- Delete data after authorized retention/incident review.

The finding type determines action; there is no universal “encrypt everything and close.”

### Classification versus other security tools

| Question | Tool |
|---|---|
| Does S3 contain sensitive data? | Macie |
| Does software/image have vulnerability? | Inspector |
| Is suspicious/threat behavior occurring? | GuardDuty |
| Is resource configuration compliant? | Config |
| Aggregate security findings/control posture? | Security Hub |

Choose the tool from the evidence asked.

### Validation after remediation

Verify:

- Public/cross-account path removed or approved.
- Intended application access still works.
- KMS/IAM/network/retention controls match class.
- Finding no longer updates/reappears after rescan/evaluation.
- CloudTrail/Config records change.
- Related copies/backups/replicas also follow classification.
- Classification metadata/owner is correct.

Fixing one object does not fix an ingestion pipeline producing more copies.

### False-positive/exception workflow

```text
Review evidence with data owner
  -> test identifier/pattern
  -> confirm false positive
  -> narrowly tune custom identifier/allow list/scope
  -> document reason and expiry
  -> verify true-positive coverage remains.
```

Archive/suppress finding only after validation.

Suppression changes workflow visibility, not the object content or access.

### Cost/scope optimization

- Use automated discovery for prioritized broad visibility.
- Use jobs for targeted/deep or scheduled requirements.
- Scope buckets/accounts/objects from risk and ownership.
- Avoid repeatedly scanning irrelevant known-safe data without reason.
- Monitor coverage, skipped objects, and analysis volume.

Cost optimization must not create compliance blind spots.

### Evidence

- Macie enabled/admin/member/Region status.
- Bucket inventory and posture.
- Automated-discovery profile/coverage.
- Job definition/status/statistics.
- Identifier/allow-list configuration.
- Finding/resource/severity/count.
- Discovery-result repository/KMS status.
- S3 policy/tags/encryption/lifecycle.
- CloudTrail object/config access history.
- Config/Security Hub/EventBridge workflow.

### Failure clues

| Symptom | First checks |
|---|---|
| Bucket absent from inventory | Account/member/Region, Macie enabled, S3 inventory timing |
| Job finds nothing unexpectedly | Bucket/object scope, sampling, identifiers, format, KMS/access |
| Many false positives | Managed/custom identifier choice, regex/context, allow list |
| Real data is missed | Broad allow list, weak pattern, unsupported/skipped objects, wrong Region |
| Findings not in Security Hub/EventBridge | Integration/Region/rule pattern/permissions |
| Finding closed but object still exposed | Archive/suppression is not remediation |
| KMS object cannot be analyzed | Key policy/grant/service/account conditions |
| Remediation breaks application | Required access/owner not validated; rollback and narrow policy |
| Same finding returns | New copies/ingestion, incomplete access fix, identifier still matches |

### Safe classification path

```text
Define classes and owners
  -> map required controls
  -> inventory/tag data
  -> enable Macie in target accounts/Regions
  -> configure automated discovery/jobs/identifiers
  -> route findings
  -> validate and contain
  -> remediate through policy/IaC
  -> rescan and monitor lifecycle.
```

### Exam traps

- Classification level must map to controls; a tag alone protects nothing.
- Macie discovers sensitive data primarily in S3, not general RDS/EBS files.
- Macie finding is not automatic proof of data exfiltration.
- Automated discovery does not prove every byte was scanned immediately.
- No finding does not mean no sensitive data; check coverage/skips/scope.
- Managed identifier, custom identifier, and allow list solve different needs.
- Broad allow list can hide true positives.
- Macie service access and KMS access are separate.
- Macie detects; S3/IAM/KMS/lifecycle policies enforce.
- Archiving/suppressing a finding does not remediate data.
- Sensitive discovery results must themselves be protected.
- Classification differs from vulnerability and threat detection.

### Do not memorize

- Every Macie managed data identifier.
- Every supported file/archive format and size limit.
- Exact Macie pricing/sample algorithm.
- Every finding-type string.
- Console click paths.

### Ready when

Given a data-classification scenario, you can:

1. Define classification levels and map them to concrete controls.
2. Choose Macie automated discovery versus a scoped discovery job.
3. Configure managed/custom identifiers, allow lists, accounts, Regions, and KMS access.
4. Route and validate findings without exposing sensitive evidence.
5. Enforce S3 access/encryption/retention and prove remediation through rescan.

---

## Skill 4.2.2 - Implement, configure, and troubleshoot encryption at rest

**Official goal:** Encrypt stored data with the right key ownership and permissions, and keep it decryptable through operations, copies, restores, and disaster recovery.

### What exam tests

- Primary: `SEL CFG BEH DIA GOV`
- Supporting: `REM PRC`
- Precision: `L3 - Property`
  - Exact key type/owner/ARN/state/policy/grant/context, service encryption setting, and copy/restore role matter.

### Core model

```text
Permission to use encrypted resource
  + permission to use its KMS key
  + key available in correct Region/account/state/context
  = data can be decrypted.
```

Resource access and key access are separate gates.

### Encryption goals

- Confidentiality of stored bytes.
- Controlled key usage.
- Audit of cryptographic operations.
- Separation of data and key administrators.
- Protected backups/copies.
- Recoverable keys during DR.

Encryption does not prevent an authorized application from reading plaintext after decryption.

### Key terminology

| Term | Meaning |
|---|---|
| KMS key | Logical key resource in AWS KMS |
| Key material | Cryptographic secret material used by key |
| Data key | Symmetric key used to encrypt application/data bytes |
| Ciphertext | Encrypted data |
| Key policy | Resource policy controlling KMS key access |
| Grant | Delegated key permission, often used by AWS services |
| Alias | Friendly pointer to a KMS key |
| Encryption context | Nonsecret authenticated key-value context |

### Envelope encryption

```text
KMS key
  -> generates/protects data key
  -> data key encrypts bulk data
  -> encrypted data key stored with ciphertext.
```

Decrypt:

```text
Encrypted data key
  -> KMS Decrypt
  -> plaintext data key in memory
  -> decrypt data locally
  -> discard plaintext data key.
```

KMS normally protects data keys; it does not receive every large data object for direct encryption.

### Why envelope encryption

- Efficient for large data.
- Central key-control/audit point.
- Data keys can be unique per object/resource.
- KMS key can rotate while old protected data keys remain decryptable.
- Service can reduce KMS calls through caching/bucket-key mechanisms where supported.

Protect both ciphertext and encrypted data key.

### KMS key ownership choices

| Key | Customer control | Audit/policy | Cross-account flexibility |
|---|---|---|---|
| AWS owned key | Lowest | Service-managed visibility/control | Lowest |
| AWS managed key | AWS manages lifecycle; customer sees key | Some audit, no customer key-policy management | Limited |
| Customer managed key | Customer policy, aliases, grants, rotation/deletion controls | Highest | Best where service supports it |

Fast choice:

```text
Need custom key policy, separation, audit, cross-account, controlled rotation/deletion?
  -> customer managed KMS key.
```

### AWS owned key

- Owned/managed by AWS service.
- Not visible as customer KMS resource.
- No customer key policy/alias/rotation control.
- Lowest operational work.

Use when service-managed encryption meets requirement.

### AWS managed key

- Exists in customer account for integrated service.
- AWS manages policy/lifecycle/rotation.
- Alias commonly service-shaped, such as `aws/service`.
- Customer cannot freely edit policy or schedule deletion.
- Cross-account/share scenarios are limited.

Use when KMS integration/audit is wanted but custom policy/control is not required.

### Customer managed key

Customer controls:

- Key policy.
- IAM delegation.
- Grants.
- Aliases/tags.
- Enable/disable.
- Rotation settings where supported.
- Deletion scheduling.
- Multi-Region/imported/custom-store options where selected.

More control means more outage responsibility.

### Key types

**Symmetric encryption KMS key**

- Same key material encrypts/decrypts.
- Most AWS service integrations use this type.
- Key material does not leave KMS boundary in plaintext.

**Asymmetric KMS key**

- Public/private key pair.
- Encrypt/decrypt or sign/verify according to key usage/spec.
- Public key can be downloaded.
- Not supported by most ordinary service at-rest integrations.

**HMAC key**

- Generate/verify message authentication codes.
- Not general storage encryption key.

Do not choose asymmetric key merely because it sounds stronger.

### Key usage/spec

Exact properties:

- Key spec.
- Key usage: encrypt/decrypt, sign/verify, or generate/verify MAC.
- Origin.
- Multi-Region setting.
- Key state.
- Enabled/rotation/deletion settings.

Key usage cannot be repurposed after creation.

### Key material origin

Recognition:

- AWS KMS-generated material.
- Imported external key material.
- Custom key store/CloudHSM-backed material.
- External key store where used.

Operational impact:

- Imported material can expire/be deleted and may require reimport.
- Custom/external stores add availability/connectivity responsibility.
- Rotation behavior differs by origin/type.

Choose only when compliance/control justifies added operations.

### Key identifiers

- Key ID.
- Key ARN.
- Alias name/ARN.
- Multi-Region key ID/related primary-replica identity where used.

Cross-account KMS references generally need full key ARN.

Aliases are Regional friendly pointers. They do not carry a key policy.

### Alias behavior

```text
alias/app-data -> key A
later alias/app-data -> key B.
```

Changing alias target:

- Does not re-encrypt old ciphertext.
- Does not delete key A.
- Old data still needs key A unless migrated/re-encrypted.
- Applications resolving alias use new target for later operations.

Alias change is not cryptographic key rotation of existing data.

### Key states

Recognize:

- `Enabled`
- `Disabled`
- `PendingDeletion`
- `PendingImport`
- `Unavailable`/custom-key-store-related states where applicable

Behavior:

```text
Disabled/pending deletion/unavailable key
  -> encrypt/decrypt operations fail.
```

Key policy can be correct while state blocks use.

### Key deletion

Customer managed key deletion is scheduled with waiting period, commonly 7-30 days.

During pending deletion:

- Key cannot be used normally.
- Alarm/event review can reveal accidental scheduling.
- Cancellation can restore key before final deletion.

After deletion:

```text
Ciphertext depending on that key can become permanently unrecoverable.
```

Inventory resources/backups/copies before scheduling deletion.

### Rotation

Rotation behavior depends on key type/origin.

For supported customer-managed symmetric keys:

- Automatic/on-demand rotation changes backing key material while logical key ID/ARN remains.
- Old key material remains available for old ciphertext.
- New encrypt operations use current material.

Rotation does not:

- Change alias/key ARN.
- Re-encrypt all stored data automatically.
- Repair a bad key policy.

Imported/asymmetric/custom-store keys may require different/manual rotation strategy.

### Key policy

Key policy is primary KMS resource policy.

Can define:

- Key administrators.
- Key users.
- AWS service principals.
- Cross-account principals.
- Conditions for service/context/source.
- Delegation to IAM policies in account.

Important:

```text
IAM Allow for kms:Decrypt
may still fail
if key policy does not permit/delegate that use.
```

### Administrator versus key user

**Key administrator**

- Manages key policy/state/rotation/aliases/deletion.
- Should not automatically receive data decrypt permission.

**Key user**

- Uses cryptographic operations such as Encrypt/Decrypt/GenerateDataKey.
- Should not automatically administer/delete key.

Separate duties where required.

### High-value KMS actions

- `kms:Encrypt`
- `kms:Decrypt`
- `kms:GenerateDataKey`
- `kms:ReEncryptFrom`
- `kms:ReEncryptTo`
- `kms:DescribeKey`
- `kms:CreateGrant`
- `kms:RetireGrant`/`RevokeGrant`
- Administrative actions for policy/state/rotation/deletion

Grant only operations required by service/workload.

### Grants

Grant delegates selected KMS operations to a principal, often for AWS service resource lifecycle.

Grant includes:

- Grantee principal.
- Allowed operations.
- Constraints/encryption context where used.
- Retiring principal.

Services may need `CreateGrant` with condition limiting grant to AWS resources.

Grant does not replace resource access permission.

### Encryption context

Nonsecret key-value pairs authenticated with ciphertext.

```text
Encrypt with context A
  -> Decrypt must provide matching context A.
```

Uses:

- Bind ciphertext to resource/purpose.
- Key-policy/grant conditions.
- Audit context in CloudTrail.

Do not put secrets in encryption context; it can appear in logs.

`InvalidCiphertext` can mean wrong key/ciphertext/context, not only corruption.

### Service conditions

Useful KMS conditions can limit:

- Calling service through `kms:ViaService`.
- Caller account.
- Encryption context keys/values.
- Grant creation for AWS resource.
- Source ARN/account in service integrations where applicable.

Conditions reduce blast radius but must match actual service request context.

### Cross-account KMS

Common requirement:

```text
Key-owner account key policy allows external principal/account
  + external caller IAM policy allows KMS action on key ARN
  + service/resource supports cross-account flow
  + no SCP/condition deny
  -> key use.
```

Need both sides.

Use customer managed key for cross-account control. AWS managed keys are not general-purpose cross-account sharing keys.

### Cross-Region KMS

KMS keys are Regional.

For copy/restore:

- Source data/key must be readable.
- Destination needs a KMS key in destination Region.
- Copy service/principal needs source decrypt and destination encrypt/grant permissions.
- Destination resource references destination key ARN.

Multi-Region KMS keys have related key material but separate Regional key resources/policies/states.

Multi-Region key does not copy application data.

### Service-role path

Integrated service can use:

- Caller credentials directly.
- Service-linked/service role.
- Grant created for resource.

Troubleshoot the principal in CloudTrail and key policy.

Human having KMS access does not guarantee RDS/Backup/Lambda service role has it.

### S3 encryption choices

| Choice | Key control |
|---|---|
| SSE-S3 | S3-managed keys |
| SSE-KMS | KMS key; policy/audit/control |
| DSSE-KMS | Dual-layer server-side KMS encryption where required/supported |
| SSE-C | Customer supplies encryption key with each request; AWS does not store key |
| Client-side encryption | Client encrypts before upload and owns crypto lifecycle |

Use SSE-KMS/customer managed key when key-policy/audit/separation/cross-account control is required.

### S3 default encryption

- Applies to new object writes.
- Existing objects do not become newly re-encrypted merely because bucket default changes.
- Re-encrypt existing objects through supported copy/batch/migration process.
- Bucket policy can require approved encryption headers/key ARN.
- S3 Bucket Key can reduce KMS request volume/cost for SSE-KMS where supported.

Changing default and migrating old objects are separate tasks.

### S3 KMS permissions

Depending on operation:

- Writer needs `GenerateDataKey`/encrypt path.
- Reader needs decrypt path.
- Multipart/copy operations can need additional permissions.
- Cross-account bucket and key policies both apply.
- Replication role needs source decrypt and destination encrypt/key access.

S3 `GetObject` allow alone is insufficient for SSE-KMS object if decrypt is denied.

### EBS encryption

EBS encryption covers:

- Data at rest on volume.
- Snapshots made from encrypted volume.
- Data movement between instance and storage infrastructure.

Controls:

- Encryption by default per Region/account.
- KMS key selection.
- Snapshot copy encryption/key.
- AMI launch/copy KMS permission.

Existing unencrypted volume usually needs migration:

```text
Snapshot
  -> copy snapshot as encrypted
  -> create encrypted volume
  -> attach/cut over.
```

Encryption-by-default affects new resources, not old volumes retroactively.

### EBS/AMI sharing

Encrypted snapshot/AMI cross-account use needs:

- Customer managed KMS key.
- Key policy/grant for target principal.
- Snapshot/AMI share permission.
- Target account IAM permission.
- Often copy into target account with target key for independence.

AWS managed key is not suitable for general encrypted snapshot sharing.

### RDS/Aurora encryption

At-rest encryption covers database storage, logs, automated backups, snapshots, and replicas according to service behavior.

Enable/select key at creation/restore.

Existing unencrypted database commonly migrates by:

```text
Create snapshot
  -> copy snapshot with encryption/KMS key
  -> restore new encrypted DB/cluster
  -> validate and cut over.
```

Cannot assume encryption can be toggled in place.

### RDS/Aurora KMS checks

- DB/cluster key ARN and Region.
- Key enabled/policy/grants.
- RDS service/caller permissions.
- Snapshot-copy source/destination key access.
- Cross-account snapshot sharing/copy rules.
- Restore creates new endpoint/resource.

Losing key access can make database/backups unusable.

### DynamoDB encryption

- DynamoDB encrypts data at rest.
- Key choice can include AWS owned, AWS managed, or customer managed options according to table configuration/support.
- Customer key provides policy/audit/control.
- Table/application permissions and KMS permissions remain separate.
- DAX/cache encryption settings are separate from table encryption.

Check table encryption status/key ARN and key state/policy.

### EFS and FSx encryption

**EFS**

- Encryption at rest selected at file-system creation.
- Existing unencrypted filesystem normally requires new encrypted filesystem and data migration.
- In-transit mount encryption is a separate setting.

**FSx**

- Encryption behavior/key selection is family/resource-creation specific.
- Backups/restores/copies can involve destination key permissions.
- Do not assume all FSx families support identical key changes.

### AWS Backup encryption

Check:

- Source resource key.
- Backup vault key.
- Recovery-point encryption behavior for that resource.
- Copy job source decrypt/destination encrypt.
- Destination account/Region vault and key policy.
- Restore role can use recovery-point key.

Backup job success does not prove another account/Region can decrypt/restore it.

### CloudWatch Logs encryption

- Log groups are encrypted at rest by service default.
- Customer managed KMS key can provide policy/control where supported.
- Associate correct Regional key with log group.
- Key policy must permit CloudWatch Logs service with correct conditions/context.

If key is disabled/deleted, log delivery/read can fail.

### SNS/SQS encryption

For customer-managed KMS encryption:

- Topic/queue service needs key use.
- Publisher/producer service principal may need key policy permission.
- Consumer still needs queue/topic/resource permission and decrypt path as applicable.
- EventBridge/S3/Lambda integrations need correct service key conditions.

Encryption can break event delivery when key policy omits source service.

### Encryption migration pattern

When in-place change unsupported:

```text
Inventory dependencies
  -> backup/snapshot
  -> copy/restore/create encrypted target
  -> grant roles/key access
  -> synchronize/freeze writes
  -> validate data/application
  -> cut over endpoint/mount/reference
  -> retain rollback
  -> retire old resource safely.
```

Encryption migration is also a resource migration.

### Troubleshooting ladder

```text
1. Which resource/ciphertext?
2. Which exact KMS key ARN and Region/account?
3. What key state/origin?
4. Which principal/session/service calls KMS?
5. Which KMS action is required?
6. Does key policy allow/delegate?
7. Does IAM policy allow?
8. Does grant exist/constraint match?
9. Does encryption context/ViaService/source condition match?
10. Do resource/SCP/endpoint policies allow?
```

Use CloudTrail KMS events and outer service error together.

### Common KMS errors

| Symptom | First checks |
|---|---|
| `AccessDenied` | Actual principal, key policy, IAM, grant, SCP, conditions |
| `NotFound` | Wrong key ID/alias/Region/account or deleted key |
| `Disabled`/unavailable | Key state/custom key store/import material |
| `InvalidCiphertext` | Wrong key, ciphertext, algorithm, encryption context |
| Throttling | KMS quota/request rate, retry/backoff, data-key/Bucket Key optimization |
| Grant-related failure | `CreateGrant`, grantee, operations, constraints |
| Copy/restore fails | Source decrypt + destination encrypt + service role/key policy |
| Service worked then stopped | Key disabled, scheduled deletion, policy/grant changed, material expired |

### CloudTrail evidence

Inspect KMS events:

- Caller/session/service.
- Key ARN.
- API action.
- Region/account.
- Encryption context.
- Error code/message.
- Source service/request context.

Also inspect outer service API event because failure may be surfaced there.

Do not log plaintext key material/secrets during troubleshooting.

### Key availability and DR

DR plan must include:

- Destination-Region key exists/enabled.
- Key policy/grants for recovery roles/services.
- Cross-account key ownership.
- Backups/copies encrypted with accessible destination key.
- Imported/custom/external key store availability.
- Key deletion/disable alarms and approvals.
- Restore test.

Data replicated without usable key is not recoverable.

### Safe key-policy change

```text
Identify exact principal/action/service/context
  -> preserve administrative access
  -> preview/review policy
  -> add narrow permission/condition
  -> test encrypt/decrypt/copy/restore
  -> verify CloudTrail
  -> remove temporary access.
```

Avoid key-policy lockout. Separate key administrators and key users.

### Exam traps

- Resource permission and KMS permission are separate.
- Key policy is central; IAM allow alone may not enable key use.
- Alias is a pointer; changing it does not re-encrypt old data.
- Rotation preserves ability to decrypt old ciphertext; it does not re-encrypt all data.
- Encryption context is nonsecret and must match.
- Disabled/pending-deletion key can cause application outage.
- Customer managed key gives control and operational responsibility.
- AWS managed key is not a general cross-account sharing key.
- KMS keys are Regional; destination copy/restore needs destination key.
- Multi-Region KMS key does not replicate data.
- Default encryption normally affects new data, not old resources retroactively.
- Some resources require snapshot/copy/restore or migration to add/change encryption.
- Successful backup/copy does not prove restore role can decrypt.
- Encryption at rest and TLS/in-transit encryption are separate controls.

### Do not memorize

- Every KMS API action.
- Every service’s exact encryption implementation.
- Cryptographic algorithm internals.
- Exact KMS quota values/prices.
- Console click paths.

### Ready when

Given an at-rest encryption scenario, you can:

1. Choose AWS owned, AWS managed, or customer managed key.
2. Explain envelope encryption, aliases, rotation, state, grants, and context.
3. Build correct key-policy + IAM + service/cross-account permission path.
4. Migrate EBS/RDS/EFS/S3 data when encryption cannot change in place.
5. Diagnose key state, policy, Region, context, copy, backup, and restore failures.

---

## Skill 4.2.3 — Implement, configure, and troubleshoot encryption in transit

### Official goal

Protect data while it moves. Use and troubleshoot TLS certificates, listeners, endpoints, and secure-transport controls.

### What the exam tests

- Select the right TLS endpoint and certificate.
- Configure validation, listeners, and TLS policies.
- Know where encryption starts and stops.
- Find whether failure is DNS, network, handshake, certificate, or backend TLS.
- Enforce encrypted connections.

### Dimensions

**Primary:** selection, configuration, behavior, diagnosis  
**Support:** remediation, governance  
**Precision:** L3 — know exact certificate, listener, validation, and policy properties.

### Core model

```text
Client
  -> DNS
  -> TCP connection
  -> TLS handshake
  -> certificate + hostname + trust + TLS policy
  -> encrypted application traffic
```

TLS can provide:

- Confidentiality.
- Integrity.
- Server identity.
- Optional client identity with mutual TLS.

No TCP connection means no TLS handshake yet.

### Certificate objects to know

- Domain name.
- Subject Alternative Names (SANs).
- Issuer.
- Leaf certificate.
- Intermediate certificate chain.
- Trusted root CA.
- Public key.
- Private key.
- Valid-from and expiry time.
- Certificate ARN.
- Status.
- Region.
- Resources using it.

Never share or log a private key.

### ACM certificate choices

**ACM public certificate**

- Publicly trusted.
- Best for supported AWS-integrated endpoints.
- ACM handles renewal when eligibility and validation remain correct.
- Its private key is not generally exportable; use an integrated AWS service unless the workflow explicitly supports export.

**Imported certificate**

- Bring certificate, private key, and chain.
- You own renewal and replacement.
- Bad or incomplete chain causes trust failure.

**Private certificate**

- Issued from private CA.
- Good for internal systems.
- Clients must trust that private CA.
- Public internet clients do not automatically trust it.

### ACM status names

Recognize:

- `PENDING_VALIDATION` — prove domain control.
- `ISSUED` — ready.
- `EXPIRED` — validity ended.
- `FAILED` — issuance failed.
- `REVOKED` — certificate revoked.
- `INACTIVE` — not active for use.

Also inspect expiry, renewal status, `In use`, SANs, and validation records.

### Domain validation

**DNS validation**

- ACM gives a CNAME name and value.
- Publish it in authoritative DNS.
- Keep it for managed renewal.
- Usually best for automation.

**Email validation**

- Approval goes to domain contact addresses.
- More manual.
- Renewal can need new approval.

Validation proves domain control. It does not prove the application is healthy.

### DNS validation failures

Check:

- Exact CNAME name and value.
- Correct authoritative hosted zone/provider.
- Record not duplicated with the zone name.
- Public DNS visibility for a public certificate.
- CNAME chain/record limits.
- Certificate still waiting or already failed.

Do not place the validation record only in a Route 53 private hosted zone for a public ACM certificate.

### Renewal model

**ACM-managed public certificate**

- Must remain eligible.
- Domain validation must remain possible.
- Certificate normally must remain associated with a supported service.
- Monitor renewal status and expiry.

**Imported certificate**

- No ACM-managed renewal.
- Obtain new certificate.
- Reimport or attach replacement.
- Test before old certificate expires.

### Hostname matching

Client hostname must match a SAN.

Examples:

```text
SAN: api.example.com
Matches: api.example.com
Does not match: www.example.com
```

```text
SAN: *.example.com
Matches: api.example.com
Does not match: example.com
Does not match: a.b.example.com
```

Changing DNS to an endpoint does not change the certificate names.

### Trust chain

```text
Leaf certificate
  -> intermediate CA(s)
  -> client-trusted root CA
```

Common failure:

- Server sends leaf only.
- Imported chain is wrong or incomplete.
- Client lacks the private/root CA.
- Old client trust store lacks the new root.

The server normally sends leaf plus intermediate certificates, not the root.

### SNI

Server Name Indication lets one TLS listener serve multiple certificates.

- Client sends requested hostname in the handshake.
- Listener selects matching certificate.
- Default certificate is used when no match or no SNI.
- Old clients without SNI can receive the wrong/default certificate.

Check certificate list and default certificate on the listener.

### Certificate Region placement

- Regional load balancer: certificate in the same Region.
- Other Regional integrations: use the required service Region.
- CloudFront viewer certificate in ACM: `us-east-1`.

Wrong Region means the certificate may not appear for selection even when it is issued.

### Load balancer TLS patterns

**ALB HTTPS listener**

```text
Client --HTTPS--> ALB --HTTP--> target
```

- TLS ends at ALB.
- Backend is plaintext.

```text
Client --HTTPS--> ALB --HTTPS--> target
```

- TLS ends at ALB.
- ALB starts a new TLS connection to target.
- Encryption exists on both legs.

**NLB TLS listener**

- NLB terminates TLS.
- Can forward to another target protocol/port.

**NLB TCP listener**

- Can pass encrypted TLS traffic through.
- Target terminates TLS.

TLS termination at the load balancer does not prove backend encryption.

### Listener objects to inspect

- Protocol: HTTPS, TLS, or TCP.
- Port.
- Default certificate.
- Additional SNI certificates.
- Security policy.
- Default action/target group.
- Target group protocol and port.
- Health-check protocol and port.

Security groups, NACLs, routes, and target reachability still apply.

### TLS security policy

Controls supported protocol versions and cipher suites.

- Stronger policy removes weak TLS/ciphers.
- Old clients may stop connecting.
- A certificate can be valid while handshake still fails.
- Compare client capability with endpoint policy.

Do not memorize every policy name. Know the compatibility tradeoff.

### CloudFront: two separate TLS legs

```text
Viewer --TLS leg 1--> CloudFront --TLS leg 2--> origin
```

**Viewer side**

- Viewer protocol policy: allow, redirect HTTP to HTTPS, or HTTPS only.
- Viewer certificate.
- Alternate domain names.
- Minimum TLS/security policy.
- ACM viewer certificate must be in `us-east-1`.

**Origin side**

- Origin protocol policy: HTTP only, HTTPS only, or match viewer.
- Origin hostname must match origin certificate.
- Origin certificate chain must be trusted by CloudFront.
- Origin TLS policy and port must work.

Viewer TLS can work while origin TLS fails.

### S3 secure transport

Use HTTPS endpoints.

To enforce HTTPS, a bucket policy can explicitly deny requests when:

```text
Condition: aws:SecureTransport = false
Effect: Deny
```

Important:

- Explicit deny overrides allows.
- Add service-principal exceptions only where the integration requires them.
- HTTP-to-HTTPS redirect is not the same as rejecting HTTP.
- A redirect receives the first request over plaintext HTTP.

### RDS TLS

- Client connects to the DB endpoint with TLS enabled.
- Client validates hostname and RDS CA chain.
- Client trust bundle must support current RDS certificate.
- Engine parameters can force encrypted connections.
- Exact enforcement setting is engine-specific.

Common failure after certificate rotation:

- Old CA bundle.
- Wrong endpoint/hostname.
- Client does not support the new chain.
- Application did not reload trust material.

RDS storage encryption and RDS connection TLS are separate.

### EFS TLS

- EFS mount helper can create encrypted-in-transit mounts.
- Recognize mount option `tls`.
- IAM authorization is a separate choice.
- Mount target, DNS, route, security group, and NFS port `2049` must still work.

An EFS TLS error can sit above a basic NFS/network failure.

### VPN and AWS API traffic

- Site-to-Site VPN uses IPsec for network-path encryption.
- Application TLS protects the application connection.
- They solve different layers and can be used together.
- AWS API endpoints use HTTPS.
- An interface VPC endpoint gives a private path; IAM and TLS still apply.

### Troubleshooting ladder

```text
1. DNS resolves correct endpoint?
2. TCP port reachable?
3. TLS handshake begins?
4. Certificate valid and complete?
5. Hostname matches SAN?
6. Client trusts issuer/root?
7. Time inside validity window?
8. TLS version/cipher compatible?
9. Correct listener/certificate/security policy?
10. If proxy/CDN/LB: does backend TLS work?
```

Do not debug certificates before proving network reachability.

### Failure map

| Symptom | First checks |
|---|---|
| Timeout | DNS, route, SG, NACL, port, listener |
| Connection refused | No listener/service on port, wrong target port |
| Hostname mismatch | Requested name versus SAN/wildcard |
| Unknown CA/untrusted issuer | Client trust store, private CA, chain |
| Incomplete chain | Imported intermediate bundle/server chain |
| Expired/not yet valid | Certificate dates and client clock |
| No shared protocol/cipher | Client capability versus security policy |
| ACM stays pending | DNS/email validation evidence |
| Certificate absent in CloudFront | ACM Region must be `us-east-1` |
| HTTPS listener cannot use cert | Certificate Region/status/private key/chain |
| Viewer works; origin fails | CloudFront origin DNS, hostname, chain, policy, port |
| ALB frontend encrypted; backend plaintext | Target group protocol is HTTP |
| RDS verify failure | Endpoint hostname, CA bundle, certificate rotation |
| EFS TLS mount failure | Mount helper, `tls`, DNS/network/2049, certificate time |

### Evidence to collect

- ACM certificate status, SANs, expiry, renewal, Region, and `In use`.
- DNS validation CNAME from authoritative DNS.
- Load-balancer listener, certificates, security policy, and target protocol.
- CloudFront viewer and origin protocol policies.
- Client handshake output and exact hostname used.
- Access/error logs and load-balancer metrics.
- CloudTrail configuration changes.
- RDS client/engine logs and CA bundle version.
- EFS mount helper and system logs.

Test from the same network and client class as the failed application.

### Safe certificate rotation

```text
Request/import new certificate
  -> validate domain and chain
  -> attach alongside old certificate where supported
  -> test hostname, SNI, TLS policy, and clients
  -> switch default/distribution configuration
  -> monitor handshake/application errors
  -> keep rollback window
  -> remove old certificate.
```

Avoid a one-step replace when SNI can support overlap.

### Exam traps

- Encryption at rest is not encryption in transit.
- TLS at the load balancer does not mean TLS to targets.
- CloudFront has viewer TLS and origin TLS separately.
- CloudFront ACM viewer certificate belongs in `us-east-1`.
- Regional endpoint certificate usually belongs in that Region.
- DNS validation record must remain for managed renewal.
- Imported certificates need manual renewal.
- Valid certificate can still fail because of hostname, chain, policy, or clock.
- Wildcard matches one label only.
- SNI selects certificates by hostname; default certificate still matters.
- Private CA certificates need client trust distribution.
- Redirect to HTTPS is weaker than denying HTTP.
- Blocked port is a network failure, not a certificate failure.
- Certificate validation proves domain control, not endpoint health.

### Do not memorize

- Every cipher suite.
- Every TLS security-policy name.
- Certificate cryptographic math.
- Every database engine’s force-TLS parameter name.
- Console click paths.

### Ready when

Given an encryption-in-transit scenario, you can:

1. Pick ACM public, imported, or private certificate.
2. Place the certificate in the correct Region.
3. Explain DNS validation, renewal, SANs, chains, SNI, and TLS policies.
4. Identify where TLS terminates and whether the backend is encrypted.
5. Enforce HTTPS for S3 and encrypted connections for supported services.
6. Separate DNS/network, handshake, certificate, policy, and backend failures.

---

## Skill 4.2.4 — Securely store secrets by using AWS services

### Official goal

Store credentials and sensitive values safely. Give workloads controlled runtime access. Rotate and audit them.

### What the exam tests

- Choose Secrets Manager or Parameter Store.
- Keep secrets out of code and deployment artifacts.
- Build IAM + KMS + resource-policy access.
- Retrieve secrets at runtime with workload roles.
- Configure and troubleshoot rotation.
- Find wrong Region, version, cache, network, or permission.

### Dimensions

**Primary:** selection, configuration, behavior, governance  
**Support:** diagnosis, remediation  
**Precision:** L3 — know service choice, versions, staging labels, rotation, policies, roles, and endpoint path.

### Core model

```text
Workload role
  -> Secrets Manager or Parameter Store API
  -> IAM/resource-policy check
  -> KMS authorization for encrypted value
  -> selected version
  -> secret returned over TLS
  -> short-lived application cache
```

Storage is only one layer. Secure use also needs:

- Least-privilege retrieval.
- Encryption.
- Network path.
- Rotation.
- Cache refresh.
- Audit.
- No accidental exposure.

### Main service choice

| Need | Best fit |
|---|---|
| Database credential with managed rotation | Secrets Manager |
| API key that needs lifecycle/rotation | Secrets Manager |
| Cross-account secret with resource policy | Secrets Manager |
| Hierarchical application configuration | Parameter Store |
| Simple encrypted value without managed rotation | Parameter Store `SecureString` |
| Plain nonsecret configuration | Parameter Store `String`/`StringList` |
| Encrypt/decrypt data or data keys | KMS; KMS is not a secret store |

Operational-efficiency clue: if rotation is required, prefer Secrets Manager.

### Secrets Manager object model

```text
Secret
  -> metadata and policy
  -> KMS key
  -> version 1 [AWSPREVIOUS]
  -> version 2 [AWSCURRENT]
  -> version 3 [AWSPENDING during rotation]
```

Know:

- Secret name and ARN.
- Secret value: string or binary.
- Version ID.
- Staging label.
- KMS key.
- Resource policy.
- Rotation configuration.
- Tags and Region.
- Primary/replica relationship where replication is used.

Do not place sensitive data in secret names, descriptions, or tags.

### Version and staging labels

- Updating a secret creates a new version.
- `AWSCURRENT` = version applications normally retrieve.
- `AWSPREVIOUS` = prior current version.
- `AWSPENDING` = version being rotated/tested.
- A label moves between versions.
- A version can carry labels.
- Retrieve a specific version only when the workflow needs it.

Applications normally request the secret without a version so they receive `AWSCURRENT`.

### Secrets Manager encryption

- Secret value is encrypted with KMS.
- Default service key is simple for same-account use.
- Customer managed KMS key gives policy and cross-account control.
- Caller needs secret retrieval permission.
- KMS authorization must also allow decryption where required.
- Key state, policy, Region, and encryption context can block access.

Secret permission and KMS permission are separate checks.

### Secrets Manager permission path

Typical retrieval needs:

```text
Identity policy:
  secretsmanager:GetSecretValue on exact secret

If customer managed KMS key:
  kms:Decrypt on exact key

Secret resource policy:
  required for resource-based/cross-account access

KMS key policy:
  must permit/delegate the decrypt path
```

Also inspect:

- SCP.
- Permission boundary.
- Session policy.
- VPC endpoint policy.
- Explicit deny.

Use the secret ARN carefully; generated ARN suffixes often require an intentional ARN pattern.

### Cross-account secret access

Need all relevant layers:

```text
Consumer account role identity policy
  + secret resource policy in owner account
  + customer managed KMS key policy
  + kms:Decrypt permission
```

Use a customer managed KMS key for cross-account control. The default AWS managed Secrets Manager key is not the general cross-account solution.

Prefer a role and exact principals/resources. Avoid public or broad wildcard resource policies.

### Secrets Manager rotation model

Rotation must change both:

1. Stored secret value.
2. Credential/value in the target system.

Changing only the stored JSON does not rotate the database credential.

Depending on the target, use:

- Managed rotation integration.
- Lambda rotation function.

Know the Lambda rotation steps:

```text
createSecret
  -> setSecret
  -> testSecret
  -> finishSecret
```

Typical label flow:

```text
new version = AWSPENDING
  -> update target
  -> test new credential
  -> move AWSCURRENT to new version
  -> old current becomes AWSPREVIOUS
```

### Rotation properties

- Rotation enabled or disabled.
- Rotation schedule.
- Rotation window.
- Rotation Lambda/integration.
- Last rotation and next rotation.
- Failed rotation evidence.
- Version labels.

Do not memorize exact schedule syntax. Know when rotation runs and whether the window is sufficient.

### Rotation Lambda requirements

The function needs:

- Permission to read/write required secret versions and labels.
- KMS access when customer managed keys are used.
- Network path to target database/service.
- DNS and correct port.
- Security groups allowing the connection.
- A path to Secrets Manager API, through NAT/public path or interface endpoint.
- Correct rotation code for the target.

If database is private, place/configure the function so it can reach the database.

### Rotation strategies

**Single user**

- Change the same credential.
- Simpler.
- Bad rotation can briefly break active clients.

**Alternating users**

- Switch between two users where supported.
- Can reduce interruption.
- Needs permission to manage both users and a privileged/master secret.

Exam clue: choose the supported managed pattern with least custom operation.

### Application caching

Fetching every request adds latency, API calls, and cost.

Use a secrets cache with:

- Short, controlled TTL.
- Refresh after rotation.
- Retry on authentication failure.
- No plaintext logging.
- No indefinite process-level storage.

Rotation may succeed while the application still uses cached `AWSPREVIOUS` credentials.

### Parameter Store object model

Parameter types:

- `String` — one plaintext configuration string.
- `StringList` — comma-separated plaintext values.
- `SecureString` — KMS-encrypted value.

Other properties:

- Hierarchical name such as `/prod/payments/db/host`.
- Version.
- Label.
- Tier.
- Data type.
- Tags.
- Parameter policies where supported.
- Region.

Use `SecureString` for sensitive values. A normal `String` is not encrypted as a secret value by KMS.

### Parameter versions and labels

- Updating a parameter creates a new version.
- Labels can point to selected versions.
- Applications can request current or a chosen version/label.
- Old versions support controlled rollback within service retention behavior.

Do not confuse Parameter Store labels with Secrets Manager staging labels.

### Parameter Store encryption and access

Typical secure retrieval:

```text
ssm:GetParameter or ssm:GetParameters
  + WithDecryption = true
  + kms:Decrypt for the SecureString key
```

For hierarchy retrieval:

```text
ssm:GetParametersByPath
```

Scope path permissions carefully. Broad parent-path access can expose many child parameters.

### Parameter policies

For supported advanced parameters, recognize:

- Expiration.
- Expiration notification.
- No-change notification.

These help lifecycle monitoring. They do not provide full credential rotation.

### What Parameter Store does not do

- It is not mainly a managed rotation service.
- A parameter update does not update the password in a database.
- `SecureString` does not remove the need for IAM/KMS permissions.
- Hierarchy is naming/organization, not automatic tenant isolation.

If the question requires automatic secret rotation, Secrets Manager is normally better.

### Workload identity

Use roles, not embedded access keys.

| Workload | Runtime identity |
|---|---|
| EC2 | Instance profile role |
| Lambda | Execution role |
| ECS application SDK | Task role |
| ECS agent injecting secret into task | Task execution role |
| EKS pod | Pod identity/IRSA role |

Give only the exact read action, secret/parameter ARN/path, and KMS key needed.

### Runtime retrieval patterns

**Best general pattern**

```text
Application starts
  -> assumes workload role automatically
  -> calls secret service over TLS
  -> caches briefly in memory
  -> refreshes after TTL/rotation.
```

Avoid long-lived credentials for retrieving another credential.

### Injection versus SDK retrieval

**Injected environment value**

- Easy for applications.
- Value is usually resolved when process/task starts.
- Rotation may require task/container restart or new deployment.
- Process/debug output can expose environment variables.

**Application SDK retrieval**

- Application can refresh without restart.
- Needs caching/retry logic.
- Uses runtime workload role.

Know when the platform snapshots the value and when the application fetches it live.

### CloudFormation and IaC

Use secure references instead of plaintext parameters or templates.

Recognize dynamic references:

```text
{{resolve:secretsmanager:...}}
{{resolve:ssm-secure:...}}
```

Important:

- Keep secret value out of template and outputs.
- Do not expose through stack outputs, logs, or resource metadata.
- Secret rotation does not always make CloudFormation update a resource automatically.
- The consuming service/application must retrieve or redeploy as required.

Do not commit secrets to Terraform state, CloudFormation templates, or source repositories.

### Unsafe locations

Do not hardcode secrets in:

- Application source.
- Git repository.
- AMI or container image.
- EC2 user data.
- Launch template plaintext.
- Lambda code/config output.
- CloudFormation outputs.
- CI/CD logs.
- Shell history.
- Tags or names.
- CloudWatch logs.

Encryption of the disk/image does not make an embedded shared secret safe.

### Private network access

A private workload needs an API path:

```text
Private subnet
  -> NAT/internet service endpoint path
or
  -> interface VPC endpoint with private DNS
```

For an interface endpoint, check:

- Endpoint exists in correct VPC/subnets/AZs.
- Private DNS enabled where expected.
- Endpoint security group allows TCP `443` from workload.
- Workload DNS resolves private endpoint addresses.
- Endpoint policy permits the API/action/resource.
- Route/NACL/SG return path works.

Direct application calls to KMS also need a KMS API path. KMS authorization is needed even when service-side integration performs decryption.

### Multi-Region behavior

- Secrets and parameters are Regional objects.
- Use the correct Region and ARN.
- Secrets Manager can replicate supported secrets to other Regions.
- Replica uses destination-Region configuration/key.
- Application failover must request the secret in the failover Region.
- Replication does not fix application cache or target-system credential design.

Do not assume a secret name is global.

### Auditing and governance

Use:

- CloudTrail for secret/parameter API activity.
- CloudWatch/EventBridge for rotation and lifecycle alarms/events.
- Config/security checks where supported.
- Tags for owner, application, environment, and rotation class.
- Access Analyzer/resource-policy validation for external access risk.

Audit:

- Who retrieved or changed the secret.
- Who changed resource/KMS policy.
- Rotation enablement and failures.
- Old/unrotated secrets.
- Broad wildcard access.
- Disabled/deleting KMS key.

Never place secret values in CloudTrail request fields, names, or custom logs.

### Troubleshooting ladder

```text
1. Correct service: Secrets Manager or Parameter Store?
2. Correct account, Region, name, and ARN/path?
3. Correct workload role/session?
4. IAM action and resource allowed?
5. Resource policy/cross-account principal allowed?
6. KMS key enabled and decrypt allowed?
7. SCP, boundary, session, endpoint policy deny?
8. DNS and HTTPS endpoint reachable?
9. Correct version/staging label returned?
10. Application cache/restart behavior?
11. For rotation: can function reach and update target?
```

Use the outer service error and CloudTrail KMS event together.

### Failure map

| Symptom | First checks |
|---|---|
| `AccessDenied` on secret | Actual role, `GetSecretValue`, secret policy, SCP/boundary |
| KMS access denied | Key ARN/state/policy, `kms:Decrypt`, encryption context |
| Secret not found | Wrong account, Region, ARN suffix, name, or deletion state |
| Parameter not found | Wrong Region/path/case/version/label |
| SecureString returned encrypted/fails | `WithDecryption`, KMS permission/key state |
| Timeout from private subnet | DNS, NAT/interface endpoint, SG `443`, endpoint policy |
| Rotation Lambda timeout | VPC path to target/API, SG, DNS, port, function timeout |
| Rotation stuck at `AWSPENDING` | Lambda step failure, permissions, target update/test, labels |
| Rotation succeeds; app login fails | Stale cache, injected old value, no restart, wrong version |
| Stored value works nowhere | Target credential was never updated or was changed elsewhere |
| Cross-account access denied | Identity + secret resource + KMS key policies |
| New task cannot start | ECS execution-role secret/KMS permission or endpoint path |
| App SDK inside ECS denied | Task role, not task execution role |

### Rotation investigation

Check in order:

1. Rotation schedule invoked.
2. Lambda invocation and logs.
3. Exact failed rotation step.
4. Secret version IDs and labels.
5. Function IAM and KMS access.
6. Function network path to target and Secrets Manager.
7. Target accepts credential update.
8. Test uses the pending credential.
9. `AWSCURRENT` moved only after success.
10. Applications refresh the new current version.

Do not force labels forward before the target credential is tested.

### Safe secret rotation/remediation

```text
Identify consumers
  -> create pending/new value
  -> update target system
  -> test new value
  -> make new version current
  -> refresh/restart consumers where needed
  -> monitor authentication errors
  -> keep short rollback path
  -> retire old value.
```

If a secret leaked:

```text
Contain access
  -> rotate/revoke immediately
  -> update consumers
  -> search CloudTrail and workload logs
  -> remove exposed copies/history
  -> fix storage/deployment path
  -> verify no unauthorized use.
```

Deleting the exposed file is not enough; rotate the credential.

### Exam traps

- KMS encrypts secrets but is not the main secret storage service.
- Secrets Manager is preferred when managed rotation is required.
- Parameter Store `SecureString` is encrypted configuration, not managed rotation.
- Updating stored value does not update the target database credential.
- `AWSCURRENT`, `AWSPREVIOUS`, and `AWSPENDING` identify secret lifecycle state.
- Runtime role is better than embedded AWS access keys.
- ECS task role and task execution role solve different retrieval paths.
- Secret access and KMS access are separate.
- Cross-account access needs both accounts’ policy path plus customer managed key control.
- A private subnet needs NAT or an interface endpoint to call the API.
- Interface endpoint policy can deny an otherwise valid IAM request.
- Rotation can succeed while application cache stays stale.
- Injected environment secrets may require workload restart after rotation.
- A secret is Regional; same name in another Region is another object.
- Never expose secret values in templates, outputs, user data, logs, or images.

### Do not memorize

- Secret or parameter size limits.
- Exact prices and quotas.
- Every rotation template.
- Complete API/CLI syntax.
- Every supported rotation integration.
- Console click paths.

### Ready when

Given a secret-storage scenario, you can:

1. Choose Secrets Manager or Parameter Store.
2. Explain secret versions, staging labels, and rotation steps.
3. Build workload IAM + secret resource + KMS authorization.
4. Use the correct EC2, Lambda, ECS, or EKS runtime role.
5. Design private endpoint access and short-lived caching.
6. Diagnose Region, version, KMS, endpoint, rotation, and stale-cache failures.
7. Keep secrets out of code, artifacts, IaC outputs, and logs.

---

## Skill 4.2.5 — Configure reports and remediate findings from AWS services

### Official goal

Collect security findings, understand what produced them, prioritize risk, remediate safely, and prove closure.

Named examples:

- Security Hub.
- GuardDuty.
- Config.
- Inspector.
- Security Agent.

Macie is also relevant for S3 sensitive-data findings.

### What the exam tests

- Choose the service that detects the problem.
- Read finding evidence and severity.
- Aggregate findings across accounts/Regions.
- Route findings to response automation.
- Select containment and remediation.
- Verify with a new evaluation or scan.
- Suppress only justified noise.

### Dimensions

**Primary:** selection, evidence, diagnosis, remediation, process  
**Support:** governance  
**Precision:** L2 — know service boundaries, finding fields, workflow states, and response flow.

### Core model

```text
Security service detects
  -> finding created
  -> Security Hub aggregates/normalizes
  -> EventBridge routes
  -> human or automation validates
  -> contain
  -> remediate
  -> rescan/reevaluate
  -> close or suppress with evidence
```

A finding is evidence to investigate. It is not always proof that the proposed remediation is safe.

### Fast service selector

| Question asks about | Service |
|---|---|
| Central security posture and finding aggregation | Security Hub CSPM |
| Suspicious or malicious activity | GuardDuty |
| Software/package vulnerability | Inspector |
| Resource configuration compliance/history | Config |
| Sensitive data in S3 | Macie |
| Application design/code threat review and scoped testing | Security Agent |

### One-line boundaries

- **Security Hub:** central view and posture controls.
- **GuardDuty:** threat detection.
- **Inspector:** vulnerability/exposure detection.
- **Config:** configuration state and compliance.
- **Macie:** sensitive-data discovery in S3.
- **Security Agent:** application security review from design/code context.

These services can report the same resource for different reasons.

### Security Hub CSPM model

Security Hub can:

- Run security standards and controls.
- Collect findings from integrated AWS and partner products.
- Normalize findings.
- Aggregate accounts and Regions.
- Filter, prioritize, and report.
- Send findings through EventBridge.
- Apply automation rules to matching findings.

Security Hub is the control plane for triage. The source service usually owns detection details.

### Security Hub objects

Know:

- Standard.
- Control.
- Finding.
- Finding provider/source product.
- Severity.
- Resource.
- Compliance status.
- Workflow status.
- Record state.
- Automation rule.
- Delegated administrator.
- Aggregation/central configuration.

Do not confuse a failed control with a GuardDuty threat finding.

### Common finding fields

Inspect:

- Finding ID.
- Product/source.
- Account and Region.
- Resource type and resource ID/ARN.
- Title and finding type.
- Description.
- Severity label/score.
- First observed, last observed, created, and updated time.
- Compliance status.
- Workflow status.
- Record state.
- Remediation recommendation.
- Network, identity, package, or data evidence.

The title alone is not enough.

### Finding state names

Recognize workflow status:

- `NEW` — not reviewed.
- `NOTIFIED` — owner notified/in progress.
- `RESOLVED` — remediation verified.
- `SUPPRESSED` — intentionally excluded from normal workflow.

Recognize record state:

- `ACTIVE` — current finding record.
- `ARCHIVED` — no longer active from provider perspective.

Recognize severity labels:

- `INFORMATIONAL`.
- `LOW`.
- `MEDIUM`.
- `HIGH`.
- `CRITICAL`.

Workflow status is analyst progress. Record state comes from finding lifecycle. Severity is risk—not completion.

### Security standards and controls

```text
Standard
  -> controls
  -> control evaluations
  -> passed/failed findings and score/reporting
```

Check:

- Standard enabled in correct accounts/Regions.
- Control enabled or disabled.
- Resource evaluation status.
- Reason for failure.
- Control parameters where supported.
- Suppression/exception justification.

A disabled control is not the same as a passing control.

### Multi-account design

Use:

- AWS Organizations integration.
- Delegated administrator.
- Central configuration where supported.
- Finding aggregation across Regions.
- Member-account enrollment.

Central team views findings; remediation still needs permission in each target account/Region.

Check whether:

- Account is enrolled.
- Region is enabled/linked.
- Source security service is enabled.
- Delegated admin is configured.
- Required service-linked roles exist.
- Cross-account execution role is assumable.

### EventBridge response pattern

```text
Finding created/updated
  -> EventBridge rule matches product/type/severity/resource
  -> SNS / ticket / Lambda / Step Functions / SSM Automation
  -> response result recorded
```

Use event-driven handling instead of periodic polling when findings already emit events.

Filter tightly. A broad rule can create duplicate tickets or unsafe repeated remediation.

### Automation rules versus EventBridge

**Security Hub automation rule**

- Matches findings.
- Updates selected finding fields/workflow.
- Helps prioritize or suppress.

**EventBridge rule**

- Routes finding events to another service.
- Starts notification or remediation workflow.

Changing a workflow label does not remediate the underlying resource.

### GuardDuty

GuardDuty detects suspicious behavior from supported AWS telemetry.

Examples:

- Compromised credentials.
- Unusual API calls.
- Crypto-mining or command-and-control traffic.
- Malicious IP/domain activity.
- Suspicious S3 activity.
- Runtime/workload threats where a protection plan supports them.
- Malware evidence where protection is enabled.

GuardDuty does not primarily test configuration against a compliance rule.

### GuardDuty objects and evidence

Know:

- Detector.
- Protection plan/feature.
- Finding type.
- Severity.
- Affected resource.
- Actor/network/API details.
- Access key/principal details.
- Count and first/last seen time.
- Suppression rule.
- Trusted IP and threat lists where applicable.
- Delegated administrator/member account.

Investigate the exact principal, resource, source IP, API, port, and time window.

### GuardDuty response

For suspected credential compromise:

```text
Identify principal/session
  -> contain or revoke access
  -> inspect CloudTrail actions
  -> rotate exposed credentials
  -> repair changed resources/policies
  -> verify no continued activity.
```

For suspected EC2 compromise:

```text
Preserve evidence
  -> isolate network carefully
  -> inspect process/network/storage evidence
  -> remove persistence
  -> rebuild from trusted image when appropriate
  -> verify finding stops.
```

Do not simply archive the finding before containment and verification.

### GuardDuty suppression

Use a suppression rule only when:

- Pattern is understood.
- Activity is expected and authorized.
- Scope is narrow.
- Owner and reason are documented.
- Review/expiry process exists.

Do not add a broad trusted IP or suppress a whole finding type merely to remove noise.

### Inspector

Inspector finds vulnerabilities and exposure in supported:

- EC2 instances.
- ECR container images.
- Lambda functions/packages/code where supported.

It continuously reassesses when software, images, or vulnerability intelligence changes.

### Inspector finding evidence

Inspect:

- Resource/account/Region.
- Finding type.
- Vulnerability/CVE.
- Affected package and installed version.
- Fixed version/remediation availability.
- Severity/CVSS and exploitability context.
- Network reachability/exposure context where available.
- First/last observed.
- Image digest/tag or Lambda version/package.

A vulnerable package in an internet-facing production workload normally outranks the same package in an unused isolated asset.

### Inspector remediation

**EC2**

- Patch supported package/OS.
- Reboot if required.
- Replace instance from patched image where immutable deployment is used.
- Reduce network exposure as temporary containment.
- Rescan/confirm finding closes.

**ECR image**

- Fix base image/dependency.
- Rebuild and push a new image.
- Redeploy workloads.
- Remove/quarantine vulnerable images according to policy.
- Verify by image digest, not only mutable tag.

**Lambda**

- Update dependency/runtime/code.
- Publish/deploy corrected version.
- Verify the active alias/version uses the fix.

Marking a finding resolved without patching the deployed artifact is not remediation.

### Config

Config answers:

- What configuration exists now?
- What changed?
- Is it compliant with a rule?
- Can an Automation document remediate it?

Config does not detect runtime malware or stolen credentials.

Typical flow:

```text
Config rule = NON_COMPLIANT
  -> inspect configuration timeline
  -> confirm scope/exception
  -> SSM Automation remediation
  -> rule reevaluates
  -> COMPLIANT
```

Prefer managed rule + managed Automation where they meet the requirement.

### Config evidence

- Resource identifier and type.
- Rule name.
- Compliance status.
- Evaluation time.
- Annotation/reason.
- Configuration item and relationship history.
- Recorder coverage.
- Remediation execution result.

If no evaluation exists, first check recorder, resource type, Region, scope, and rule trigger.

### Macie

Macie discovers and reports sensitive data in S3.

Use it for:

- Personally identifiable information.
- Financial or credential-like data.
- Sensitive-data discovery jobs.
- Automated sensitive-data discovery.
- S3 bucket security and data findings.

Macie does not scan EC2 packages and is not the main runtime threat detector.

### Macie remediation

```text
Validate object/bucket and sample evidence safely
  -> identify data owner/classification
  -> remove unintended public/cross-account access
  -> apply encryption/retention/lifecycle controls
  -> relocate or delete data only with owner approval
  -> rerun discovery/verify policy.
```

Do not copy sensitive sample data into tickets or logs.

### Security Agent

Security Agent uses application context to help:

- Build threat models.
- Review application designs.
- Review source/repository context.
- Perform scoped security/penetration testing.
- Produce findings and remediation guidance.
- Suggest code changes or pull requests where supported.

Know the **Agent Space** as the controlled application/repository context and access boundary.

### Security Agent operating model

```text
Authorized application/repository scope
  -> Agent Space receives design/code context
  -> threat model/design review/scoped test
  -> finding with evidence and recommendation
  -> human validates
  -> code/design fix
  -> review and retest.
```

Check:

- Correct repository/application scope.
- Least-privilege access.
- Approved test target and boundaries.
- Quality/currentness of context.
- Human review before merging or production change.
- Retest after fix.

Security Agent is not a replacement for GuardDuty runtime detection, Inspector package scanning, or Config compliance.

### Finding prioritization

Severity alone is not priority.

Combine:

- Severity.
- Exploitability/active exploitation.
- Internet or cross-account exposure.
- Production/business criticality.
- Data sensitivity.
- Privilege of affected identity.
- Scope/blast radius.
- Finding age and recurrence.
- Available fix and compensating controls.

Example:

```text
Medium + internet exposed + production credential
may outrank
High + isolated unused test resource.
```

### Response lifecycle

```text
1. Validate finding and affected resource.
2. Add owner/business context.
3. Set priority and workflow status.
4. Preserve evidence.
5. Contain active risk.
6. Remediate root cause through IaC/Automation where possible.
7. Rescan or reevaluate.
8. Confirm deployed resource is fixed.
9. Resolve/archive; document exception if suppressed.
10. Improve preventive control.
```

Closing a ticket is not verification.

### Containment versus remediation

**Containment** reduces immediate harm:

- Isolate instance.
- Disable or restrict compromised principal.
- Block malicious network indicator.
- Remove public access.
- Stop deployment of vulnerable image.

**Remediation** removes root cause:

- Patch/rebuild.
- Rotate credential.
- Correct policy/IaC.
- Remove malicious persistence.
- Change architecture/control.

Contain first when attack is active. Then remediate and verify.

### Safe automation

Before automatic destructive action, validate:

- Finding confidence/type.
- Exact resource/account/Region.
- Current state still matches finding.
- Business owner/exemption tags.
- Idempotency.
- Execution role and change scope.
- Rollback or quarantine path.
- Duplicate event handling.
- Result logging and reevaluation.

Quarantine is often safer than immediate deletion.

### SSM Automation response pattern

```text
EventBridge or Config finding
  -> SSM Automation document
  -> assume remediation role
  -> verify precondition
  -> change/quarantine resource
  -> record output
  -> trigger/await reevaluation
```

Cross-account remediation needs correct trust, permissions, and `iam:PassRole` where applicable.

### Reporting

Useful report views:

- Findings by severity.
- Findings by product/service.
- Failed controls by standard.
- Accounts/Regions without coverage.
- Findings by resource owner/application.
- Open critical/high findings by age.
- Mean time to contain/remediate.
- Reopened or recurring findings.
- Suppressed findings due for review.
- Vulnerabilities with known fixes/exposure.

A good report shows coverage and trend, not only a total count.

### Missing-finding troubleshooting

```text
1. Is source service enabled in account/Region?
2. Is resource type/protection plan supported and enabled?
3. Does recorder/scanner/integration cover the resource?
4. Is member account enrolled?
5. Is Region linked to aggregation Region?
6. Is Security Hub integration enabled?
7. Is finding filtered, suppressed, or archived?
8. Did EventBridge pattern match exact event fields?
9. Does target allow invocation?
```

No finding can mean no coverage—not no risk.

### Remediation-failure map

| Symptom | First checks |
|---|---|
| Finding never reaches Security Hub | Source enabled, integration, account, Region, aggregation |
| Control shows no data | Config recorder/resource coverage, control availability, Region |
| EventBridge target not invoked | Event pattern, rule state, target policy/role, DLQ |
| Automation starts then fails | Execution role, document parameters, current resource state |
| Finding returns after fix | Root cause/IaC unchanged, wrong resource/version, no redeploy |
| Inspector finding remains | Package still installed, image digest unchanged, scan pending |
| GuardDuty activity continues | Credential/session not revoked, persistence or network path remains |
| Config stays noncompliant | Remediation failed, evaluation not rerun, wrong scope/parameter |
| Too many duplicate tickets | Match on updates, finding ID/state, idempotency/deduplication |
| Central account cannot remediate | Member-account role trust/permission/Region |
| Security Agent result irrelevant | Wrong Agent Space scope or stale/missing design/code context |

### Evidence before closure

Require the proof appropriate to the source:

- Security Hub control passes or exception is documented.
- GuardDuty activity stops and compromise scope is investigated.
- Inspector rescans corrected deployed artifact.
- Config reevaluates resource as compliant.
- Macie confirms data/access treatment.
- Security Agent retest/review confirms design or code fix.
- CloudTrail proves remediation action and actor.
- Automation output shows successful exact-resource change.

Do not resolve solely because an API call returned success.

### Suppression and exceptions

Suppression needs:

- Business/security justification.
- Exact finding/control/resource scope.
- Compensating control.
- Owner.
- Expiry/review date.
- Approval trail.

Suppression hides workflow noise. It does not remove risk.

### Exam traps

- GuardDuty detects threats; Config checks configuration compliance.
- Inspector finds vulnerabilities; GuardDuty finds suspicious behavior.
- Macie finds sensitive S3 data; it is not malware scanning.
- Security Hub aggregates and controls posture; it does not replace source services.
- Security Agent reviews application design/code context; it is not GuardDuty.
- Workflow `RESOLVED` does not itself repair the resource.
- `SUPPRESSED` is not the same as remediated.
- Severity is not full business priority.
- A disabled control is not a passed control.
- A successful automation call is not proof of compliance until reevaluation.
- Patch an ECR image, rebuild, and redeploy; fixing only the repository is incomplete.
- Rotating a compromised access key without checking CloudTrail misses blast radius.
- Use event-driven routing instead of polling findings.
- Avoid duplicate remediation from Security Hub, Config, and custom automation.
- Central visibility does not automatically grant member-account remediation access.

### Do not memorize

- Every finding type name.
- Every security standard control ID.
- Full ASFF schema.
- Exact CVSS formulas.
- All GuardDuty data-source internals.
- Exact score calculations.
- Console click paths.

### Ready when

Given a security-finding scenario, you can:

1. Choose Security Hub, GuardDuty, Inspector, Config, Macie, or Security Agent.
2. Read source, resource, severity, time, workflow, and evidence fields.
3. Build multi-account aggregation and event-driven routing.
4. Separate containment, remediation, and verification.
5. Choose a safe Automation/IaC response.
6. Diagnose missing findings, failed routing, failed remediation, and recurrence.
7. Suppress only narrow, documented, reviewable exceptions.

---

# Domain 5 — Networking and Content Delivery (18%)

## Skill 5.1.1 — Configure a VPC

### Official goal

Configure VPC addressing, subnets, routes, network ACLs, security groups, NAT gateways, internet gateways, and egress-only internet gateways.

### What the exam tests

- Design CIDRs and subnets.
- Classify public, private, and isolated subnets.
- Choose the correct route destination and target.
- Configure IPv4 and IPv6 internet paths.
- Apply security groups and network ACLs correctly.
- Find the failed network layer.
- Avoid IP exhaustion, single-AZ dependencies, and avoidable transfer cost.

### Dimensions

**Primary:** configuration, behavior, diagnosis  
**Support:** remediation, optimization, governance  
**Precision:** L3 — exact CIDR, route, SG, NACL, IGW, NAT, and egress-only IGW behavior matters.

### Core VPC model

```text
Region
  -> VPC: address boundary
      -> Availability Zone A
          -> subnet A
      -> Availability Zone B
          -> subnet B
```

- VPC is Regional.
- Subnet belongs to one Availability Zone.
- Resources receive private addresses from a subnet.
- Route table chooses the next hop.
- Security group filters at resource/ENI level.
- Network ACL filters at subnet boundary.

### Packet model

```text
Source address
  -> source subnet route table
  -> route target/gateway/appliance
  -> destination route
  -> destination NACL
  -> destination security group
  -> listening application
  -> valid return path
```

Most connectivity failures are one broken object in this chain.

### Address objects

Know:

- VPC primary IPv4 CIDR.
- VPC secondary IPv4 CIDR.
- VPC IPv6 CIDR.
- Subnet IPv4 CIDR.
- Subnet IPv6 CIDR.
- Primary and secondary private IPs on an ENI.
- Public IPv4 address.
- Elastic IP address.
- Prefix list.

CIDRs that must route directly to each other cannot overlap.

### CIDR basics

```text
Smaller prefix number = larger network
/16 is larger than /24
/24 has 256 IPv4 addresses
```

AWS reserves five IPv4 addresses in each subnet:

- First address: network address.
- VPC router address.
- DNS-related reserved address.
- Future-use reserved address.
- Last address: network broadcast address, although VPC does not support broadcast.

Example:

```text
/24 = 256 total - 5 reserved = 251 usable IPv4 addresses
```

### CIDR sizing

Allow space for:

- Current workloads.
- Auto Scaling peaks.
- Load balancer nodes.
- VPC endpoint ENIs.
- NAT/firewall/appliance ENIs.
- Managed service ENIs.
- Blue/green deployments.
- Growth and failure replacement.

Tiny subnets often fail later through IP exhaustion.

### IPv4 CIDR properties

- A VPC can have primary and supported secondary CIDR blocks.
- Each subnet CIDR must fit inside a VPC CIDR.
- Subnets in one VPC cannot overlap.
- Adding a secondary CIDR adds address space; it does not enlarge an existing subnet.
- Existing resources do not automatically move into a new CIDR.

Do not memorize every CIDR association restriction. Know overlap and capacity effects.

### IPv6 properties

- A VPC can receive/associate an IPv6 CIDR.
- IPv6 subnets normally use a `/64` block.
- IPv6 addresses are globally unique; there is no IPv6 NAT requirement for ordinary internet routing.
- Public reachability still requires a route, gateway, security rules, and a listening service.
- Use egress-only internet gateway when inbound initiation must be blocked.

Global address does not mean automatically internet reachable.

### Subnet classification

**Public subnet**

```text
Route table has:
0.0.0.0/0 -> internet gateway
and/or
::/0 -> internet gateway
```

For IPv4, an instance also needs a public IPv4/EIP plus security and application allowance.

**Private subnet with internet egress**

```text
0.0.0.0/0 -> NAT gateway
```

No direct route to internet gateway for the private workload.

**Isolated subnet**

- No default route to internet gateway or NAT internet path.
- May have local, endpoint, peering, transit, or hybrid routes.

A subnet is not public merely because its resources have public IP addresses.

### Route table object model

```text
Route table
  -> routes: destination + target
  -> subnet association(s)
```

Examples:

| Destination | Target | Meaning |
|---|---|---|
| VPC CIDR | `local` | Within VPC |
| `0.0.0.0/0` | `igw-...` | Default IPv4 internet path |
| `0.0.0.0/0` | `nat-...` | Default private IPv4 egress |
| `::/0` | `igw-...` | IPv6 internet path, inbound possible if allowed |
| `::/0` | `eigw-...` | Outbound-initiated IPv6 internet path |
| Remote CIDR | `pcx-...` | VPC peering |
| Remote CIDR | `tgw-...` | Transit Gateway |
| On-premises CIDR | `vgw-...`/`tgw-...` | VPN/private hybrid path |
| Service prefix list | endpoint | Gateway endpoint path |

Route targets are resources, not arbitrary next-hop IPs in normal VPC routing.

### Route selection

First rule: **longest prefix wins**.

Example:

```text
10.0.0.0/8    -> target A
10.20.0.0/16  -> target B
10.20.5.0/24  -> target C

Destination 10.20.5.9 uses target C.
```

More specific route wins even if the default route points elsewhere.

For equal prefixes, static routes generally take priority over propagated routes. Do not memorize every propagated-route tie breaker.

### Local route

- Created for each VPC CIDR.
- Enables routing among subnets in the VPC.
- Security controls still filter traffic.
- A route does not mean the application accepts the connection.

### Main and custom route tables

- Every VPC has a main route table.
- A subnet without explicit association uses the main route table.
- A subnet can be explicitly associated with one route table at a time.
- One route table can serve multiple subnets.
- Use custom route tables to make subnet intent clear.

Changing the main table can affect every implicitly associated subnet.

### Route states

- `active` — target is usable from route-table perspective.
- `blackhole` — target is unavailable/deleted or route cannot forward.

A route can be active while SG, NACL, appliance, or application still blocks traffic.

### Internet gateway

An internet gateway:

- Attaches to a VPC.
- Provides a route target for public IPv4/IPv6 internet traffic.
- Performs public/private IPv4 address mapping for resources with public IPv4 addresses.
- Is horizontally scaled and VPC-level, not placed in one subnet.

Public IPv4 instance needs:

```text
IGW attached
  + subnet route 0.0.0.0/0 -> IGW
  + public IPv4 or EIP
  + SG/NACL allowance
  + application listening
```

Missing any one can break access.

### Public IPv4 and Elastic IP

**Auto-assigned public IPv4**

- Controlled by subnet launch setting or interface/launch configuration.
- Maps to the primary private IPv4.
- Normally changes after stop/start.

**Elastic IP**

- Static public IPv4 allocation.
- Can be remapped within supported scope.
- Has allocation/usage cost implications.

Public IPv4 is mapped at the edge. The ENI still primarily sees its private address.

### Public NAT gateway

Purpose: outbound IPv4 internet access for private subnets.

Required path:

```text
Private instance
  -> private subnet route: 0.0.0.0/0 -> NAT gateway
  -> NAT gateway in public subnet
  -> NAT has Elastic IP
  -> NAT public subnet route: 0.0.0.0/0 -> IGW
  -> internet
```

Return traffic follows the established translation state.

### NAT gateway behavior

- Managed network address translation.
- NAT gateway belongs to one subnet/AZ.
- Public NAT gateway uses an Elastic IP for internet egress.
- Private resources do not need public IPv4 addresses.
- Does not accept unsolicited inbound internet connections.
- Security groups cannot be attached to a NAT gateway.
- Subnet NACLs and routes still affect it.

NAT gateway is not a bastion host and does not make a subnet public.

### NAT gateway resilience

Common resilient pattern:

```text
Private subnet AZ-A -> NAT gateway AZ-A
Private subnet AZ-B -> NAT gateway AZ-B
```

Benefits:

- Avoid one-AZ NAT dependency.
- Avoid cross-AZ traffic for normal egress.

Tradeoff:

- More NAT gateways cost more.

Exam chooses based on availability, cost, and operational requirements.

### NAT gateway port capacity symptoms

Many connections to the same destination can exhaust translation ports.

Evidence can include:

- Connection failures under load.
- NAT gateway port-allocation errors.
- High concurrent connections to one destination.

Possible remediation:

- Add additional private IP/EIP capacity where supported.
- Spread destination endpoints.
- Reuse connections.
- Scale architecture appropriately.

Do not diagnose port exhaustion before checking routes and NAT state.

### Egress-only internet gateway

Purpose: outbound-initiated IPv6 internet access without unsolicited inbound initiation.

```text
IPv6 workload
  -> route ::/0 -> egress-only internet gateway
  -> internet
```

- VPC-level route target.
- Stateful for connection initiation direction.
- No Elastic IP.
- Does not provide IPv4 NAT.

Use normal internet gateway if inbound IPv6 internet connections are required and security rules allow them.

### IPv4 versus IPv6 egress

| Need | Route target |
|---|---|
| Public IPv4 inbound/outbound | Internet gateway + public IPv4/EIP |
| Private IPv4 outbound only | Public NAT gateway |
| IPv6 inbound/outbound | Internet gateway |
| IPv6 outbound-initiated only | Egress-only internet gateway |

Do not send `::/0` to an IPv4 NAT gateway for normal IPv6 internet access.

### Security group model

```text
Security group
  -> inbound allow rules
  -> outbound allow rules
  -> attached to ENI/resource
```

Properties:

- Stateful.
- Allow rules only.
- No explicit deny.
- All matching rules are evaluated as a set.
- Return traffic for an allowed connection is automatically allowed.

### Security group rule fields

- Direction: inbound or outbound.
- Protocol.
- Port or port range.
- Source for inbound.
- Destination for outbound.
- Source/destination can be IPv4 CIDR, IPv6 CIDR, prefix list, or supported security-group reference.
- Description.

Security group names do not create connectivity. Rules do.

### Stateful example

Web server SG:

```text
Inbound: TCP 443 from 0.0.0.0/0
Outbound: restricted as application requires
```

A valid response to the inbound HTTPS connection is allowed back even without a separate inbound-style return rule.

For a connection initiated by the server, an outbound rule must allow the initial packet.

### Security group references

Example:

```text
Database SG inbound TCP 5432 from Application SG
```

Meaning:

- ENIs associated with Application SG can be sources for that rule.
- It does not copy Application SG rules.
- It does not allow every resource in the VPC.
- Destination still needs the database SG rule and listening service.

Prefer SG references over changing application-subnet CIDRs when the resource relationship is stable.

### Default security group behavior

The default VPC security group commonly starts with:

- Inbound from the same default SG.
- Outbound to all destinations.

A new custom security group commonly starts with:

- No inbound rules.
- Outbound allow-all rule.

Always inspect actual rules; they can be changed.

### Network ACL model

```text
Network ACL
  -> numbered inbound rules
  -> numbered outbound rules
  -> associated subnet(s)
```

Properties:

- Stateless.
- Allow and deny rules.
- Lowest rule number evaluated first.
- First match wins.
- Final `*` rule denies unmatched traffic.
- Separate inbound and outbound rules required.

### NACL association

- Every subnet uses one network ACL.
- One network ACL can associate with multiple subnets.
- Default NACL commonly allows all traffic.
- New custom NACL commonly denies all until allow rules are added.

Associating a new custom NACL before adding both-direction rules can cause an outage.

### NACL rule fields

- Rule number.
- Traffic type/protocol.
- Port range.
- Source CIDR for inbound.
- Destination CIDR for outbound.
- Allow or deny.

NACLs use CIDRs, not security-group references.

### NACL ordered evaluation

Example:

```text
100 DENY 203.0.113.10/32 TCP 443
200 ALLOW 0.0.0.0/0 TCP 443
*   DENY all
```

The specific deny at 100 wins for that source.

If the allow were rule 50, the later deny would never be reached for matching traffic.

### Stateless return traffic

For a client reaching a server:

```text
Inbound NACL:
  allow destination service port

Outbound NACL:
  allow destination client ephemeral port
```

For a server initiating outbound traffic:

```text
Outbound NACL:
  allow destination service port

Inbound NACL:
  allow return traffic to source ephemeral port
```

Ephemeral port range depends on client/OS/service. Allow the required range for the real path.

### SG versus NACL

| Property | Security group | Network ACL |
|---|---|---|
| Applied to | ENI/resource | Subnet boundary |
| State | Stateful | Stateless |
| Rules | Allow only | Allow and deny |
| Evaluation | Combined rule set | Lowest number, first match |
| Return traffic | Automatically allowed for tracked connection | Must be explicitly allowed |
| Peer type | CIDR/prefix list/SG reference | CIDR only |

Use SG for primary resource-level least privilege. Use NACL for subnet-level coarse guardrails or explicit CIDR deny.

### Source/destination check

EC2 ENIs normally perform source/destination checking.

- Keep enabled for ordinary workloads.
- Disable on an instance acting as a router, NAT instance, or supported network appliance.

Disabling it does not create routes or security rules; those are still required.

### ENI facts

An elastic network interface can have:

- Primary private IPv4.
- Secondary private IPv4 addresses.
- IPv6 addresses.
- One or more security groups.
- Elastic IP mappings to private IPv4 addresses.
- MAC address and DNS properties.

ENIs belong to an Availability Zone. A network interface cannot simply move to another AZ.

### VPC DNS settings

Know VPC attributes:

- `enableDnsSupport` — Amazon-provided DNS resolution support.
- `enableDnsHostnames` — DNS hostname assignment behavior.

DHCP option sets can provide:

- Domain name servers.
- Domain name.
- Time/NTP and related supported options.

DNS success does not prove a route or security path. DNS failure can look like total network failure.

### IPAM

VPC IP Address Manager helps:

- Plan CIDR pools.
- Allocate non-overlapping space.
- Track utilization.
- Find overlapping or unused allocations.
- Monitor compliance across accounts/Regions.

IPAM does not route traffic. It manages address planning and evidence.

### Highly available VPC pattern

```text
AZ-A: public subnet + NAT-A + load-balancer node
      private app subnet -> NAT-A

AZ-B: public subnet + NAT-B + load-balancer node
      private app subnet -> NAT-B
```

- Spread application subnets across AZs.
- Route each private subnet to same-AZ NAT when resilience justifies cost.
- Keep databases/private services in private or isolated subnets.
- Use load balancer instead of public IPs on every application instance.

A subnet cannot span AZs; HA requires multiple subnets.

### Public web path

```text
Client
  -> public DNS/public IPv4
  -> IGW
  -> public subnet
  -> NACL inbound
  -> web ENI security group
  -> listener
  -> response through stateful SG + outbound NACL
```

Route table classifies the subnet. Public address identifies the instance at the internet edge.

### Private outbound path

```text
Private instance
  -> SG outbound
  -> private-subnet NACL outbound
  -> 0.0.0.0/0 route to NAT
  -> NAT-subnet NACL
  -> NAT subnet 0.0.0.0/0 route to IGW
  -> internet
  -> reverse translated return path
```

Do not add a public IP to the private instance to fix a NAT path.

### Troubleshooting order

```text
1. Correct source/destination IP and protocol/port?
2. Source resource and ENI healthy?
3. Source subnet route: longest-prefix target?
4. Route target attached/available, not blackhole?
5. Every middlebox has forward and return route?
6. Security groups allow initial direction?
7. NACLs allow both directions and ephemeral ports?
8. Destination route/ENI/address correct?
9. OS firewall and application listening?
10. DNS resolving the intended address family?
```

Test both forward and return paths.

### Public-instance failure map

| Symptom | First checks |
|---|---|
| No inbound IPv4 | Public IPv4/EIP, IGW attached, public route, SG inbound, NACL, listener |
| Outbound only fails | SG outbound, NACL both ways, route, DNS |
| Works by IP, not name | VPC DNS settings, resolver/record |
| Works inside VPC, not internet | Public address, IGW/default route, internet-facing listener |
| Connection timeout | Route, SG, NACL, firewall, no listener response |
| Connection refused | Host reachable but service not listening/wrong port |

### Private-egress failure map

| Symptom | First checks |
|---|---|
| Private instance no internet | Private route to NAT, NAT state, NAT subnet public route, EIP, IGW |
| One AZ only fails | That AZ subnet association/NAT/NACL/route |
| NAT receives no traffic | Private subnet route/association, SG/NACL, more-specific route |
| NAT sends no traffic | NAT public subnet route, IGW, NACL, NAT state |
| Intermittent under high load | NAT port allocation/connections, NACL ephemeral range |
| Internet cannot initiate to private host | Expected NAT behavior; use LB/public design if required |

### IPv6 failure map

| Need/symptom | First checks |
|---|---|
| Outbound-only IPv6 fails | IPv6 address, `::/0 -> eigw`, SG/NACL, DNS AAAA |
| Public IPv6 inbound fails | `::/0 -> igw`, SG inbound IPv6 CIDR, NACL, listener |
| IPv4 works, IPv6 fails | Separate IPv6 routes/rules; IPv4 rules do not include IPv6 |
| Unexpected inbound blocked with eigw | Expected: egress-only gateway blocks new inbound initiation |

### NACL failure patterns

- Allow rule placed after a broader lower-number deny.
- Inbound service port allowed but outbound ephemeral range denied.
- Outbound service port allowed but return ephemeral traffic denied.
- IPv4 rules exist but IPv6 rules do not.
- New custom NACL associated before allow rules.
- Client ephemeral range assumed incorrectly.

NACL problems often cause timeout, partial response, or intermittent connection failure.

### Route failure patterns

- Subnet associated with unexpected/main route table.
- More-specific route sends traffic to wrong target.
- Route target deleted: `blackhole`.
- Return route missing from appliance, peering, transit, or hybrid side.
- NAT route placed on wrong subnet table.
- Public subnet lacks IGW default route.
- IPv6 default route points to wrong gateway.
- Overlapping CIDRs make destination ambiguous/unroutable across networks.

### IP exhaustion evidence

Symptoms:

- Instance/task/pod cannot launch.
- Load balancer or endpoint cannot add ENI.
- Managed service reports insufficient free addresses.
- One AZ fails while another works.

Check:

- Available IP count per subnet.
- Hidden/managed ENIs.
- Auto Scaling and deployment surge.
- Stale ENIs.
- Subnet size and AZ placement.

Fix by adding appropriately sized new subnets/CIDRs and moving or redeploying workloads—not by expecting an existing subnet CIDR to grow in place.

### Evidence tools

- VPC route tables and associations.
- Security-group rules attached to exact ENIs.
- Network ACL rules and associations.
- ENI addresses and source/destination check.
- NAT gateway state and metrics.
- VPC Flow Logs.
- Reachability Analyzer.
- CloudTrail for network configuration changes.
- Resolver tests and application socket tests.
- IPAM/subnet available-address evidence.

Reachability Analyzer tests modeled configuration. It does not prove the application is running or the packet crossed an external network.

### Flow Log clues

Use Flow Logs to inspect:

- Source/destination address.
- Source/destination port.
- Protocol.
- Interface.
- `ACCEPT` or `REJECT`.
- Time window.

An `ACCEPT` record means captured network controls accepted the traffic. It does not prove the application responded.

### Cost and efficiency clues

- Public IPv4/EIPs have cost implications.
- NAT gateways have hourly and data-processing cost.
- Cross-AZ NAT use can add cross-AZ transfer and dependency.
- One NAT per AZ improves resilience but adds fixed cost.
- S3/DynamoDB gateway endpoints can avoid NAT for supported traffic; detailed in 5.1.2.
- Interface endpoints have their own hourly/data cost.
- Flow Log destination and volume affect logging cost.

Do not memorize prices. Identify the charged architecture component and traffic path.

### Safe network change

```text
Record current routes/rules/associations
  -> identify exact traffic flows
  -> add narrow new path/rule
  -> test forward and return traffic
  -> monitor Flow Logs/application
  -> remove obsolete rule/path
  -> retain rollback.
```

For NACL changes, add new allow before removing old access. For route changes, verify the exact associated subnets.

### Exam traps

- A public subnet is defined by route to an IGW, not by its name.
- Public subnet route alone does not give an EC2 instance a public IPv4.
- Public IPv4 alone does not work without IGW route and security allowance.
- Private subnet route to NAT does not make it public.
- NAT gateway allows outbound return traffic, not unsolicited inbound access.
- Public NAT needs public subnet, EIP, IGW, and IGW route.
- Egress-only internet gateway is for outbound-initiated IPv6, not IPv4.
- IPv4 SG/NACL rules do not match IPv6 traffic.
- Longest-prefix route wins over a less-specific default route.
- A subnet uses one route table and one NACL at a time.
- Security groups are stateful and allow-only.
- NACLs are stateless, ordered, and allow/deny.
- NACL return/ephemeral traffic must be explicitly allowed.
- Security-group reference does not copy another group’s rules.
- Security groups cannot attach to a NAT gateway.
- A subnet exists in one AZ; HA needs multiple subnets.
- An active route does not prove the application is listening.
- An `ACCEPT` Flow Log does not prove application success.
- Adding a secondary VPC CIDR does not resize an existing subnet.

### Do not memorize

- Every VPC quota.
- Every ephemeral-port range for every OS.
- Every propagated-route tie breaker.
- Exact public IPv4 or NAT prices.
- Full Flow Log schema.
- Console click paths.

### Ready when

Given a VPC configuration scenario, you can:

1. Size non-overlapping VPC/subnet CIDRs and explain reserved addresses.
2. Classify public, private-egress, and isolated subnets from routes.
3. Select routes using destination, target, and longest prefix.
4. Build public IPv4, private IPv4 egress, public IPv6, and egress-only IPv6 paths.
5. Apply stateful SG and stateless ordered NACL rules.
6. Diagnose forward route, return route, security, NAT, DNS, application, and IP exhaustion failures.
7. Balance multi-AZ resilience against NAT/public-address cost.

---

## Skill 5.1.2 — Configure private networking connectivity

### Official goal

Connect workloads privately by using VPC endpoints, PrivateLink, VPC peering, and related private-connectivity services.

### What the exam tests

- Choose the smallest correct private-connectivity service.
- Configure routes, DNS, policies, and security controls.
- Distinguish service access from full network routing.
- Understand peering non-transitivity.
- Build Transit Gateway association and propagation correctly.
- Configure private hybrid and remote-user access.
- Diagnose forward path, return path, DNS, policy, and attachment failures.

### Dimensions

**Primary:** selection, configuration, behavior, diagnosis  
**Support:** governance, optimization  
**Precision:** L3 — endpoint type, private DNS, endpoint policy, peering routes, and Transit Gateway routing objects matter.

### Fast selector

| Need | Best fit |
|---|---|
| Private S3 or DynamoDB access from VPC | Gateway endpoint |
| Private AWS service/API access through ENIs | Interface endpoint |
| Privately expose one service to consumers | PrivateLink endpoint service |
| Connect a small number of VPC pairs | VPC peering |
| Connect many VPCs and hybrid networks | Transit Gateway |
| Connect an on-premises network | Site-to-Site VPN or Direct Connect pattern |
| Connect individual remote users | Client VPN |
| Insert virtual network appliances transparently | Gateway Load Balancer endpoint |

### Core distinction

```text
Endpoint/PrivateLink = private access to a service
Peering/TGW/VPN      = private routing between networks
```

Do not create full network connectivity when only one service must be exposed.

### VPC endpoint families

Core exam types:

- Gateway endpoint.
- Interface endpoint.
- Gateway Load Balancer endpoint recognition.

Endpoint policy and workload IAM are separate authorization layers.

### Gateway endpoint

Used for supported services, chiefly:

- Amazon S3.
- DynamoDB.

Model:

```text
Workload subnet
  -> route table
  -> service prefix list -> gateway endpoint
  -> S3/DynamoDB regional service
```

Properties:

- Route-table target.
- No endpoint ENIs in subnets.
- No endpoint security group.
- Endpoint policy controls allowed use.
- No hourly endpoint charge.
- Designed for access from associated VPC route tables.

### Gateway endpoint configuration

Need:

- Endpoint in the correct VPC and Region.
- Correct service name.
- Route tables associated.
- Automatically managed service prefix-list route present.
- Endpoint policy permits action/resource/principal conditions.
- Workload IAM/resource policy permits request.
- SG/NACL outbound path permits service traffic.

No NAT or internet gateway is required for this service path.

### Gateway endpoint route behavior

Example:

```text
Destination: S3 managed prefix list
Target: S3 gateway endpoint
```

Longest-prefix routing normally makes the service route more specific than `0.0.0.0/0 -> NAT`.

Traffic to unrelated services still follows their own route.

### Gateway endpoint boundaries

- It is not a general internet gateway.
- It does not expose your own application.
- It is not represented by private endpoint ENIs.
- It does not use an endpoint SG.
- It does not create network connectivity to another VPC.
- Access through peering, TGW, VPN, or Direct Connect is not the normal gateway-endpoint sharing model.

For centrally reachable service endpoints, interface endpoints are often the relevant design.

### Interface endpoint

Powered by AWS PrivateLink.

Model:

```text
Workload
  -> private DNS name
  -> endpoint ENI private IP
  -> PrivateLink
  -> AWS/partner/your endpoint service
```

Properties:

- One endpoint ENI in each selected subnet/AZ.
- Private IP addresses.
- Security groups attach to endpoint ENIs.
- Endpoint-specific DNS names.
- Optional private DNS for supported services.
- Endpoint policy where supported.
- Hourly per-AZ and data-processing cost.
- No NAT/IGW required.

### Interface endpoint security path

Typical HTTPS access needs:

```text
Client SG outbound TCP 443
  -> endpoint ENI SG inbound TCP 443 from client CIDR/SG
  -> endpoint policy allows API
  -> workload IAM allows API
  -> service resource policy allows API
```

The endpoint SG protects the endpoint ENI, not the service resource itself.

### Interface endpoint DNS

Without private DNS:

- Use endpoint-specific DNS name.

With private DNS enabled:

- Normal Regional service hostname resolves to endpoint private IPs inside associated VPC DNS context.
- Application can often keep using the normal service name.

Need:

- VPC DNS support/hostnames configured as required.
- Private DNS enabled on endpoint.
- Correct private hosted-zone behavior.
- No conflicting DNS namespace.
- Clients actually using the VPC/hybrid resolver path.

An endpoint can be healthy while DNS still resolves the public service address.

### Endpoint policy

Endpoint policy:

- Limits requests through that endpoint.
- Can restrict actions, resources, principals, or conditions.
- Does not grant permissions by itself.
- Can explicitly deny an IAM-allowed request.

Full authorization can require:

```text
IAM identity policy
  + endpoint policy
  + service resource policy
  + KMS key policy when encrypted data is used
```

### Interface endpoint availability

For multi-AZ workloads:

- Select endpoint subnets in required AZs.
- Allow endpoint ENI IP capacity.
- Use Regional endpoint DNS unless a zonal dependency is intentional.
- Ensure clients can reach endpoint ENIs across designed paths.

One endpoint subnet/AZ can become an availability and cross-AZ dependency.

### Interface endpoint from on premises or another VPC

Possible when design provides:

- Routing to endpoint ENI private IPs.
- DNS that returns reachable endpoint addresses.
- Endpoint SG allows source.
- Endpoint and IAM policies allow request.

Common DNS pattern:

```text
On-premises DNS
  -> Route 53 Resolver inbound endpoint
  -> VPC private DNS
  -> interface endpoint ENI IPs
```

Do not expect private DNS to cross networks automatically.

### PrivateLink endpoint service

Provider model:

```text
Provider targets
  -> Network Load Balancer
  -> endpoint service
  -> PrivateLink
  -> consumer interface endpoint ENIs
  -> consumer workloads
```

Use when consumers need one private service, not provider-network access.

### Endpoint service properties

Provider configures:

- Network Load Balancer and healthy targets.
- Endpoint service.
- Allowed principals.
- Acceptance required or automatic acceptance.
- Supported Availability Zones.
- Private DNS name/verification where used.

Consumer configures:

- Interface endpoint.
- Selected subnets/AZs.
- Endpoint security groups.
- Private DNS/application DNS.
- Endpoint policy and workload permissions.

### PrivateLink behavior

- Consumer initiates connections to service.
- Provider does not receive full routing access to consumer VPC.
- No VPC route-table relationship is required between consumer and provider CIDRs.
- Overlapping consumer/provider CIDRs can work because this is service access, not routed adjacency.
- It is not transitive network connectivity.
- It scales to many consumer VPCs/accounts with controlled exposure.

PrivateLink does not make every provider port/resource reachable.

### PrivateLink failure map

| Symptom | First checks |
|---|---|
| Endpoint `pendingAcceptance` | Provider acceptance setting/action |
| Endpoint service unavailable | Allowed principals, service name, Region |
| DNS resolves but timeout | Endpoint SG, client SG/NACL, NLB listener/targets |
| Connection reaches NLB, target fails | Target group health, port, SG, application |
| Private name does not resolve | Name verification, endpoint private DNS, VPC DNS |
| Only one AZ fails | Endpoint subnet/AZ support, ENI, NLB target/AZ health |

### Gateway Load Balancer endpoint

Use for transparent insertion of supported virtual appliances such as firewalls.

```text
Route table
  -> GWLB endpoint
  -> Gateway Load Balancer
  -> appliance fleet
  -> return through symmetric path
```

Important:

- It is a route target.
- It is not the normal HTTPS API interface endpoint.
- Appliance health and symmetric routing matter.
- Forward and return traffic must follow the designed inspection path.

### VPC peering

One-to-one private routed connection between two VPCs.

```text
VPC A subnet route: VPC-B CIDR -> pcx
VPC B subnet route: VPC-A CIDR -> pcx
```

Need:

- Peering request and acceptance.
- `active` connection.
- Non-overlapping CIDRs.
- Routes on both sides.
- SG and NACL allowance.
- DNS resolution options if private DNS names must resolve across peer.

### VPC peering behavior

- Same account or cross-account.
- Same Region or supported cross-Region.
- No transitive routing.
- No central route table.
- No automatic route creation for workload subnets.
- No broad resource authorization; SG/IAM/resource policies still apply.

Peering is network adjacency, not service-level PrivateLink isolation.

### Peering non-transitivity

```text
VPC A <-> VPC B <-> VPC C
```

This does **not** allow:

```text
VPC A -> VPC B -> VPC C
```

Create direct A-C peering or use Transit Gateway when many networks need connectivity.

### Peering edge-to-edge trap

A VPC generally cannot use a peer VPC merely as transit to its:

- Internet gateway.
- NAT gateway.
- VPN/Direct Connect path.
- Another peering connection.

Peering connects the two VPC CIDRs directly; it is not a transit hub.

### Peering DNS

Private hostname resolution across a peering connection needs:

- VPC DNS attributes.
- Peering DNS-resolution options.
- Correct private hosted-zone associations/Resolver design for custom zones.

Route success does not automatically associate a private hosted zone with the peer VPC.

### Peering failure map

| Symptom | First checks |
|---|---|
| Peering cannot be created | Overlapping CIDRs, account/Region/request details |
| Connection not usable | Request not accepted or status not `active` |
| A reaches B; B cannot initiate/return | Reverse route, SG initiation rule, NACL both directions |
| A reaches B but not C | Expected non-transitive behavior |
| IP works, hostname fails | Peering DNS option, PHZ association, Resolver path |
| Some subnets fail | Wrong route-table association or missing route |

### Transit Gateway

Hub-and-spoke routing for many networks.

```text
VPC/VPN attachments
  -> Transit Gateway
  -> TGW route table
  -> destination attachment
```

Useful for:

- Many VPCs.
- Central hybrid connectivity.
- Network segmentation.
- Shared services.
- Central inspection architecture.

### Transit Gateway objects

Know:

- Transit Gateway.
- Attachment.
- VPC attachment subnets.
- Transit Gateway route table.
- Association.
- Propagation.
- Static route.
- Blackhole route.
- Appliance mode recognition.

VPC route tables and TGW route tables are different objects. Both may need routes.

### Association versus propagation

**Association**

```text
Which TGW route table is used when traffic enters from this attachment?
```

An attachment associates with one TGW route table at a time.

**Propagation**

```text
Which attachment routes are learned into this TGW route table?
```

One attachment can propagate into multiple TGW route tables where configured.

Short memory:

```text
Association = lookup table on ingress
Propagation = advertise destination into table
```

### Transit Gateway packet path

```text
Source subnet route: destination CIDR -> TGW
  -> source attachment
  -> associated TGW route table lookup
  -> route points to destination attachment
  -> destination VPC subnet route/local path
  -> SG/NACL/application
  -> reverse route through TGW
```

Missing any VPC-side or TGW-side route breaks the flow.

### TGW segmentation

Example:

- Production attachment associates with production TGW table.
- Development attachment associates with development table.
- Shared-services routes propagate into both.
- Production and development routes are not mutually propagated.

This creates routing isolation. Security groups, NACLs, firewalls, and IAM still apply.

### TGW attachment subnets

- Select VPC attachment subnets in required AZs.
- TGW creates attachment ENIs there.
- Workload subnet route points to TGW.
- Plan IP capacity and AZ coverage.
- An AZ without appropriate attachment reachability can fail or take an unintended cross-AZ path.

Do not place TGW routes only in the attachment subnet route table and forget workload subnet tables.

### TGW failure map

| Symptom | First checks |
|---|---|
| VPC sends nothing to TGW | Workload subnet route and association |
| TGW drops route | Source attachment association, TGW table route/propagation |
| One-way traffic | Destination/return VPC route, reverse TGW table, SG/NACL |
| Unexpected VPC connectivity | Wrong association or overbroad propagation |
| Intended VPC isolated | Missing propagation/static route |
| Route exists but shows blackhole | Deleted/unavailable attachment or explicit blackhole |
| Appliance path asymmetric | Appliance mode, AZ routing, forward/return inspection routes |

### Site-to-Site VPN

Connects an on-premises network to AWS through IPsec tunnels.

Core objects:

- Customer gateway representation.
- Customer gateway device.
- Virtual private gateway or Transit Gateway attachment.
- VPN connection.
- Two tunnels.
- Static routes or BGP.

Need routes on both AWS and on-premises sides plus SG/NACL allowance.

### VPN routing patterns

**Virtual private gateway**

```text
VPC route table -> on-prem CIDR -> VGW
```

Routes can be static or propagated according to VPN design.

**Transit Gateway VPN attachment**

```text
VPC route -> TGW
TGW route -> VPN attachment
on-premises route -> VPN tunnels
```

Use both tunnels for resilience. One tunnel up is degraded, not fully resilient.

### Direct Connect recognition

Direct Connect provides a dedicated network connection, not internet-encrypted IPsec by itself.

Private connectivity can use:

- Private virtual interface.
- Virtual private gateway.
- Direct Connect gateway.
- Transit Gateway integration where supported.

Use VPN over/alongside the design when encryption is required. Detailed hybrid troubleshooting appears in 5.3.4.

### Client VPN

Managed remote-user VPN into AWS.

Objects:

- Client VPN endpoint.
- Client CIDR.
- Authentication method.
- Target-network association.
- Authorization rule.
- Client VPN route.
- Security group.
- Split-tunnel/full-tunnel setting.
- Connection logging.

### Client VPN access path

```text
User authenticates
  -> Client VPN endpoint
  -> authorization rule allows destination network
  -> Client VPN route selects target association
  -> target VPC route/security path
  -> application
```

Authentication, authorization, and routing are three separate checks.

### Client VPN failure map

| Symptom | First checks |
|---|---|
| User cannot connect | Endpoint state, authentication, certificate/identity provider, client log |
| Connected but no resource access | Authorization rule, route, target association, SG/NACL |
| One subnet/AZ path fails | Target-network association and routes |
| DNS names fail | Client DNS servers, Route 53 Resolver path, split tunnel |
| Internet behavior wrong | Split/full tunnel routes and authorization |
| Client CIDR conflicts | Overlap with destination/local client networks |

### Route 53 Resolver role

Private connectivity often needs hybrid DNS:

- Inbound endpoint: on premises asks VPC Resolver.
- Outbound endpoint: VPC forwards selected domains to on-premises DNS.
- Resolver rules select domains and targets.
- Private hosted-zone associations control visibility.

The network can be connected while names still fail.

Detailed DNS configuration appears in 5.2.1.

### High-availability rules

- Interface endpoints: deploy in required AZs.
- Endpoint service: healthy NLB targets across required AZs.
- TGW VPC attachments: cover workload AZs.
- Site-to-Site VPN: configure both tunnels.
- Client VPN: use multiple target-network associations as designed.
- Resolver endpoints: use multiple IPs/AZs.
- PrivateLink consumers: use Regional DNS unless zonal pinning is required.

Route redundancy is useless if DNS returns only an unavailable endpoint.

### Connectivity troubleshooting ladder

```text
1. What is the required model: service access or network routing?
2. Correct account, Region, VPC, and object state?
3. Source resolves intended private IP/name?
4. Source subnet route uses longest-prefix target?
5. Attachment/endpoint/peering accepted and available?
6. Intermediate route table association/propagation correct?
7. Destination and return routes exist?
8. SG/NACL/firewall allow both required directions?
9. Endpoint/resource/IAM/KMS policies allow request?
10. Target listener/application healthy?
```

For API endpoints, network success and authorization success are different.

### Endpoint failure map

| Symptom | First checks |
|---|---|
| Gateway endpoint unused | Associated route table, prefix-list route, service Region/DNS |
| Interface endpoint timeout | DNS, endpoint ENI SG `443`, NACL, endpoint state |
| Interface endpoint returns access denied | Endpoint policy, IAM, resource policy, KMS |
| Private DNS resolves public IP | Private DNS/VPC DNS/conflicting zone/client resolver |
| Some AZs fail | Endpoint subnet/ENI coverage, IP exhaustion, zonal DNS |
| Service works through NAT only | Endpoint DNS/route/policy not selected |

### General private-connectivity failure map

| Symptom | Likely layer |
|---|---|
| Timeout | Route, return route, SG, NACL, tunnel/attachment, listener |
| Immediate access denied | IAM, endpoint policy, resource policy, KMS |
| IP works; DNS fails | Private DNS, Resolver, hosted-zone association |
| One direction works | Return route, stateful initiation rule, stateless NACL |
| One account/Region missing | Enrollment/share/acceptance/Regional object |
| One AZ fails | Attachment/endpoint subnet, target health, IP capacity |
| A-B and B-C work; A-C fails | Expected peering non-transitivity |

### Evidence

- Endpoint type, state, service name, subnets, ENIs, SGs, private DNS, and policy.
- Gateway endpoint route-table associations and prefix-list route.
- Endpoint-service allowed principals, acceptance, NLB, and target health.
- Peering status, CIDRs, routes, and DNS options.
- TGW attachments, subnet selections, route-table associations, propagations, and routes.
- VPN tunnel/BGP/static-route status.
- Client VPN connection/auth/route/authorization logs.
- VPC Flow Logs and Reachability Analyzer.
- CloudTrail configuration changes.
- DNS answers from the failing source network.

Inspect the exact source subnet route table, not merely a similarly named table.

### Cost selector

- Gateway endpoint: no hourly endpoint charge; best for supported S3/DynamoDB paths.
- Interface endpoint: hourly per selected AZ plus data processing.
- NAT gateway: hourly and data processing; endpoints can avoid NAT for supported service traffic.
- VPC peering: simple for few pairs; mesh route/operations grow quickly.
- Transit Gateway: attachment/data charges but simpler many-network hub.
- Cross-AZ and cross-Region traffic can add transfer cost.
- PrivateLink limits exposure but each endpoint has cost.

Do not memorize prices. Compare topology scale and traffic path.

### Safe connectivity change

```text
Map source, destination, DNS, port, and return path
  -> create endpoint/attachment/peering
  -> add narrow routes and policies
  -> test one path/AZ
  -> expand to required AZs/accounts
  -> verify Flow Logs and application
  -> remove NAT/public/legacy path only after proof
  -> retain rollback.
```

Avoid removing the old path before private DNS and endpoint policy are verified.

### Exam traps

- Gateway endpoint is for supported S3/DynamoDB service routes; interface endpoint uses ENIs.
- Gateway endpoint has no endpoint SG.
- Interface endpoint SG must allow client traffic, commonly TCP `443`.
- Private DNS can preserve the normal AWS service hostname.
- Endpoint policy limits use; it does not grant IAM permission.
- Interface endpoint does not require a route-table entry to its ENI; the VPC local route applies.
- Gateway endpoint requires route-table association/prefix-list route.
- PrivateLink exposes a service, not a whole provider VPC.
- PrivateLink can handle overlapping provider/consumer CIDRs because there is no routed adjacency.
- VPC peering requires non-overlapping CIDRs and routes in both VPCs.
- VPC peering is non-transitive and not an internet/NAT/VPN transit path.
- Peering connectivity does not automatically share private hosted zones.
- TGW association selects ingress lookup table; propagation installs attachment routes.
- TGW needs both VPC route-table and TGW route-table paths.
- VPN has two tunnels; configure both for resilience.
- Client VPN needs authentication + authorization + route.
- Network connectivity does not bypass IAM, resource, endpoint, or KMS policies.
- Private IP connectivity does not guarantee private DNS resolution.

### Do not memorize

- Every endpoint service name.
- Exact endpoint/TGW/PrivateLink prices.
- Every TGW propagated-route priority.
- VPN cryptographic parameters here.
- Full Client VPN configuration syntax.
- Console click paths.

### Ready when

Given a private-connectivity scenario, you can:

1. Choose gateway endpoint, interface endpoint, PrivateLink, peering, TGW, VPN, or Client VPN.
2. Explain endpoint ENIs, SGs, private DNS, route-table associations, and endpoint policies.
3. Build two-sided peering routes and explain non-transitivity.
4. Build a TGW path using VPC routes, attachment association, propagation, and return routes.
5. Separate authentication, authorization, routing, and DNS for Client VPN/hybrid access.
6. Diagnose state, DNS, forward/return route, SG/NACL, policy, and target-health failures.
7. Select resilient private access without unnecessary NAT or full-network exposure.

---

## Skill 5.1.3 — Audit AWS network protection services in one account

### Official goal

Audit Route 53 Resolver DNS Firewall, AWS WAF, AWS Shield, and AWS Network Firewall in one account.

### What the exam tests

- Choose the correct protection layer.
- Confirm resource/VPC association and traffic coverage.
- Read rule priority and action.
- Use logs, sampled traffic, and metrics.
- Find bypass paths and false positives.
- Move safely from monitoring to blocking.
- Remediate weak, stale, or missing protection.

### Dimensions

**Primary:** selection, configuration, evidence, diagnosis  
**Support:** remediation, governance  
**Precision:** L2 — know service boundary, rule objects/actions/priorities, association, traffic path, and logs.

### Fast selector

| Threat/control need | Service |
|---|---|
| Block or alert on DNS domain queries | Route 53 Resolver DNS Firewall |
| Filter HTTP/HTTPS requests | AWS WAF |
| DDoS protection | AWS Shield |
| Inspect routed VPC network traffic | AWS Network Firewall |
| Allow workload ports at ENI level | Security group |
| Subnet-level CIDR allow/deny | Network ACL |

### Layer model

```text
DNS query       -> DNS Firewall
HTTP request    -> WAF
DDoS event      -> Shield
VPC packet/flow -> Network Firewall
```

One service does not replace the others.

### Audit questions for every protection

```text
1. Is it enabled?
2. Is it associated with the exact VPC/resource?
3. Is traffic actually in its path?
4. Which rule/action wins?
5. Are logs and metrics enabled?
6. What is allowed, blocked, alerted, or bypassed?
7. Are exceptions narrow and current?
8. Did recent changes weaken protection?
```

Creating a policy without association or routing provides no enforcement.

## Route 53 Resolver DNS Firewall

### Purpose

Controls DNS queries made through Route 53 VPC Resolver.

Use for:

- Known malicious domains.
- Disallowed categories/domains.
- Approved-domain allowlists.
- Monitoring suspicious DNS queries.
- Managed threat domain lists.

It does not block direct IP traffic after resolution or traffic using an ungoverned external resolver path.

### DNS Firewall object model

```text
Domain list
  -> firewall rule
  -> rule group
  -> rule-group association
  -> VPC Resolver queries
```

Know:

- Customer-managed domain list.
- AWS-managed domain list.
- Firewall rule.
- Rule action.
- Rule priority.
- Rule group.
- VPC association.
- Association priority.
- Query logs and metrics.

### DNS Firewall actions

**`ALLOW`**

- Permit matching query.
- Use for approved exceptions/allowlist behavior.

**`BLOCK`**

- Stop matching DNS answer.
- Block response can use behavior such as `NODATA`, `NXDOMAIN`, or configured override.

**`ALERT`**

- Permit query.
- Record/measure match.
- Good before enforcing a new list.

`ALERT` is monitoring, not blocking.

### DNS Firewall priority

- Lower numeric priority is evaluated before higher priority.
- First matching terminating behavior controls the query.
- Put narrow approved exceptions before broad block rules where intended.
- Inspect association priority when multiple rule groups apply.

Names and list order do not determine evaluation order; priority does.

### DNS Firewall audit

Check:

- Correct VPC association.
- Association status.
- Rule-group and rule priorities.
- Domain-list content/source/update state.
- Managed list selection.
- `ALERT` versus `BLOCK` action.
- Block response behavior.
- Resolver query logging.
- Query/match/block metrics.
- VPCs or DNS paths without coverage.
- Broad allow rules before block rules.

### DNS Firewall safe rollout

```text
Add domain list
  -> action ALERT
  -> review query logs and owners
  -> add narrow exceptions
  -> change to BLOCK
  -> monitor failures/block volume
  -> rollback action if business outage occurs.
```

Test managed lists in alert mode before broad blocking.

### DNS Firewall evidence

Use:

- Route 53 Resolver query logs.
- Firewall rule/action in query-log context.
- Domain queried.
- Source VPC/resource address where available.
- Matching rule group/list.
- CloudWatch metrics.
- CloudTrail for rule/list/association changes.

Do not log or distribute sensitive internal domain names more broadly than needed.

### DNS Firewall failure map

| Symptom | First checks |
|---|---|
| Malicious domain still resolves | VPC association, rule priority/action, domain pattern, client resolver path |
| New block causes outage | Query logs, false-positive domain, exception priority, managed-list change |
| No firewall log evidence | Resolver query logging, association, client bypass/custom resolver |
| Exception does not work | Allow rule priority before block, exact domain pattern |
| Only one VPC affected | Rule-group associations and status |

## AWS WAF

### Purpose

Filters web requests at supported HTTP/HTTPS resources.

Common protected resources:

- CloudFront distributions.
- Application Load Balancers.
- API Gateway supported APIs.
- Other supported Regional web endpoints.

WAF understands web-request fields. It is not a general TCP/UDP firewall.

### WAF object model

```text
Web ACL
  -> ordered rules/rule groups
  -> default action
  -> associated web resource
```

Know:

- Web ACL.
- Scope: Regional or CloudFront.
- Rule.
- Rule group.
- AWS Managed Rules.
- Priority.
- Statement/match condition.
- Action.
- Default action.
- Visibility configuration.
- Logging and sampled requests.

### WAF scope

**Regional web ACL**

- Protects supported Regional resources in that Region.

**CloudFront web ACL**

- Uses CloudFront scope.
- Protects the distribution at edge locations.
- Managed through the CloudFront/global scope context.

A Regional web ACL cannot simply be attached to CloudFront.

### WAF rule evaluation

- Rules use numeric priority.
- Lower number evaluates first.
- Terminating match stops later evaluation.
- If no terminating rule matches, web ACL default action applies.

Rule names and visual order are not enough; inspect numeric priority.

### WAF actions

Recognize:

- `ALLOW` — terminating allow.
- `BLOCK` — terminating deny.
- `COUNT` — record match and continue evaluation.
- `CAPTCHA` — require CAPTCHA when token is not valid.
- `CHALLENGE` — client challenge/token behavior.

`COUNT` is safe for testing a rule but does not protect by itself.

CAPTCHA/challenge behavior depends on token state; understand their purpose, not every token detail.

### WAF default action

Typical models:

**Default allow**

- Block known bad patterns.
- Common public application model.

**Default block**

- Allow only known valid patterns.
- Strong allowlist model.

Audit whether rule logic matches the default action. A default block with missing allow path can cause total outage.

### WAF statements and rule types

Recognize:

- IP set.
- Geo match.
- Rate-based rule.
- Size constraint.
- String/regex match.
- SQL injection match.
- Cross-site scripting match.
- Managed rule group.
- Logical `AND`, `OR`, and `NOT`.
- Scope-down statement.

Do not memorize JSON syntax.

### Rate-based rules

- Count matching requests by an aggregation key over a rolling evaluation window.
- Apply action when rate limit is exceeded.
- Can use scope-down conditions.
- Good for abusive request rates, not volumetric network DDoS replacement.

Audit threshold against legitimate peak traffic and source distribution.

### Managed rule groups

Benefits:

- Lower operational work.
- Maintained rule intelligence.
- Broad common-threat coverage.

Audit:

- Managed group/version/update behavior.
- Excluded or overridden rules.
- Rules forced to `COUNT`.
- Capacity limits.
- False positives after updates.
- Scope-down conditions.

Using a managed group does not remove the need to inspect matches and application behavior.

### WAF labels

Rules/managed groups can add labels to matching requests.

Later rules can match labels to:

- Block selected subcategories.
- Count first, then enforce.
- Create application-specific exceptions.

Labels support composed logic. They do not directly block unless a rule action does so.

### WAF audit

Check:

- Exact resource association.
- Regional versus CloudFront scope.
- Rule priority.
- Terminating action.
- Default action.
- Managed-rule overrides/exclusions.
- `COUNT` rules mistaken for blocking.
- Rate limits and legitimate peaks.
- Logging enabled and destination healthy.
- Visibility metrics and sampled requests.
- Sensitive-field redaction/filtering.
- Recent web ACL/rule changes in CloudTrail.

### WAF logging and evidence

Use:

- Full WAF logs where configured.
- Sampled requests.
- Per-rule/web-ACL CloudWatch metrics.
- Terminating rule ID.
- Action.
- HTTP method, URI, headers, source, and labels as available.
- CloudTrail configuration history.
- ALB/CloudFront/API access logs for application result.

Sampled requests are samples, not a complete audit trail.

Protect credentials, cookies, authorization headers, and request bodies in logs through redaction/filtering and access controls.

### WAF safe rollout

```text
Add rule in COUNT
  -> inspect matches and false positives
  -> tune scope/exceptions
  -> change to BLOCK/CAPTCHA/CHALLENGE
  -> watch block rate and application errors
  -> retain fast rollback to COUNT.
```

Prefer rule override to `COUNT` while validating a new managed rule group.

### WAF failure map

| Symptom | First checks |
|---|---|
| Bad request allowed | Web ACL association, rule scope/priority, action still `COUNT`, default action |
| Good request blocked | Terminating rule ID, labels, managed-rule match, exception order |
| No WAF logs | Logging config/destination/policy, traffic hits associated resource |
| Rule never matches | Wrong field/transformation/scope-down/path/priority |
| CloudFront unprotected | CloudFront-scope web ACL association |
| Rate rule blocks shared users | Aggregation key, NAT/shared IP behavior, threshold/scope-down |

## AWS Shield

### Purpose

Protects against distributed denial-of-service attacks.

Shield is not a replacement for:

- WAF application rules.
- Security groups.
- Network Firewall policy.
- Application scaling and caching.

### Shield Standard

- Automatic baseline DDoS protection for AWS customers.
- No separate subscription.
- Protects supported AWS edge/network services against common infrastructure-layer attacks.
- Limited advanced visibility and response features compared with Shield Advanced.

Audit architecture exposure and service metrics even though Standard is automatic.

### Shield Advanced

Adds capabilities such as:

- Explicit protection of supported resources.
- Enhanced detection and event visibility.
- Advanced diagnostics/metrics.
- DDoS Response Team support and response workflows.
- Health-based detection/proactive engagement where configured.
- DDoS cost-protection capabilities under service conditions.
- Central protection management features.

It has subscription and operational setup requirements.

### Shield Advanced objects

Recognize:

- Subscription.
- Protected resource/protection.
- Protection group.
- DDoS event.
- Health check association.
- Emergency/response contacts.
- DRT access role/permissions where configured.

Paying for Shield Advanced is not enough; required resources and response setup must be configured.

### Shield audit

Check:

- Which internet-facing resources are protected.
- Any eligible resource missing explicit Advanced protection.
- CloudFront/Route 53/ELB/Elastic IP architecture coverage.
- Health checks used for detection where appropriate.
- DDoS events, vectors, start/end time, and mitigations.
- Emergency contacts and escalation process.
- DRT access permissions.
- WAF/web-layer controls for application attacks.
- Scaling/caching/origin-protection architecture.

### Shield failure/trap map

| Situation | Meaning |
|---|---|
| SQL injection attack | WAF problem, not Shield-only solution |
| Large volumetric DDoS | Shield/network-edge protection relevant |
| Advanced subscribed but resource absent | Add explicit resource protection |
| Attack mitigation works but origin overloads | Review caching, scaling, origin exposure, app bottleneck |
| No proactive engagement | Health checks/contact/response setup may be incomplete |

## AWS Network Firewall

### Purpose

Managed VPC firewall for routed network traffic.

Use for:

- Central or distributed traffic inspection.
- Domain/IP/port/protocol controls.
- Stateful threat-signature inspection.
- Internet ingress/egress inspection.
- East-west or hybrid inspection where routed through it.

It protects only traffic that traverses its firewall endpoints.

### Network Firewall object model

```text
Rule groups
  -> firewall policy
  -> firewall
  -> endpoint in selected AZ/subnet
  -> VPC route tables steer traffic
```

Know:

- Firewall.
- Firewall subnet mapping.
- Firewall endpoint per AZ.
- Firewall policy.
- Stateless rule group.
- Stateful rule group.
- Default actions.
- Policy variables/reference sets recognition.
- Logging configuration.

### Stateless versus stateful inspection

**Stateless**

- Evaluates individual packets.
- Ordered by rule priority.
- Can pass, drop, or forward traffic to stateful inspection.
- Default stateless actions handle unmatched packets/fragments.

**Stateful**

- Tracks connections/flows.
- Evaluates protocol/session context.
- Supports pass, drop, alert, and supported reject/signature behavior.
- Needs symmetric forward and return flow through compatible firewall state.

Do not treat stateless and stateful rule priorities as one combined list.

### Network Firewall traffic path

Simple egress inspection pattern:

```text
Workload subnet route
  -> Network Firewall endpoint in same AZ
  -> firewall subnet route
  -> NAT/IGW or next hop
  -> return route through same firewall endpoint
  -> workload
```

Route tables insert the firewall. Creating the firewall alone does not move traffic through it.

### Firewall subnet design

- Use dedicated firewall subnets.
- Deploy endpoint mappings in required AZs.
- Route each workload AZ through the intended endpoint.
- Keep return traffic symmetric.
- Plan separate NAT, TGW, IGW, and inspection routes carefully.
- NACLs still must permit the path.

Network Firewall endpoints do not use ordinary security groups as their primary control; firewall policy and routes perform inspection.

### Symmetric routing

Stateful firewall needs both directions of a flow.

Bad:

```text
Forward -> firewall endpoint AZ-A
Return  -> bypass or firewall endpoint AZ-B
```

Possible result:

- State not found.
- Intermittent drops.
- Different behavior by AZ.

Use same-AZ/symmetric paths and appliance-mode design where relevant.

### Network Firewall rule audit

Check:

- Rule group attached to the active policy.
- Policy attached to the firewall.
- Stateless default actions.
- Stateful rule-order mode and actions.
- Rule priority/order.
- Broad `PASS` before intended `DROP`/inspection.
- Domain/IP lists current.
- Managed rule-group update behavior.
- Capacity and failed policy updates.
- TLS inspection configuration where used.
- Exceptions and change ownership.

### Network Firewall routing audit

For every protected path, map:

```text
source subnet
  -> source route table
  -> firewall endpoint ID/AZ
  -> firewall subnet route table
  -> NAT/IGW/TGW/destination
  -> exact return route
```

Look for:

- Default route bypassing firewall.
- More-specific route bypassing firewall.
- One AZ without endpoint route.
- Return route skipping inspection.
- TGW attachment propagation creating alternate path.
- Wrong ordering between firewall and NAT.
- Blackhole firewall endpoint route.

### Network Firewall logging

Recognize:

- Alert logs.
- Flow logs.
- Supported TLS-related logs where configured.
- Destinations such as CloudWatch Logs, S3, or Firehose according to configuration.

Logs can show:

- Source/destination IP and port.
- Protocol.
- Flow/session details.
- Matching rule/signature.
- Alert/drop action.
- TLS/server-name context where available.

Firewall logs can contain sensitive network metadata. Encrypt, restrict, and retain appropriately.

### Network Firewall failure map

| Symptom | First checks |
|---|---|
| Traffic never inspected | Workload route, endpoint ID/AZ, bypass/more-specific route |
| All traffic stops after insertion | Firewall subnet routes, stateless defaults, return path, policy attachment |
| One AZ fails | Endpoint mapping, route target, firewall/NAT subnet path in that AZ |
| Intermittent stateful drops | Asymmetric routing, cross-AZ path, appliance mode |
| Rule logs but does not block | Rule action is alert/pass or earlier pass wins |
| Expected rule never logs | Traffic bypasses firewall, rule group absent, encryption/field mismatch |
| Policy update fails | Rule-group capacity/syntax/reference/dependency |

## Cross-service audit model

### Coverage inventory

Build a table of:

- Internet-facing resources.
- VPCs and DNS Firewall associations.
- Web resources and WAF web ACLs.
- Shield Advanced eligible/protected resources.
- Network Firewall endpoint coverage by AZ/path.
- Owner and environment.
- Logging destination and retention.
- Exception/suppression owner and expiry.

Missing association is a failed control even if the policy object exists.

### Rule quality

Review:

- Action: monitor/count/alert versus enforce/block/drop.
- Numeric priority.
- Default action.
- Broad allow/pass rules.
- Duplicate/shadowed/unreachable rules.
- Stale IP/domain lists.
- Managed-rule updates and exclusions.
- Exception scope and age.
- IPv4/IPv6 coverage.
- Production versus test policy differences.

A rule below an earlier terminating allow may never run.

### Logging quality

Check:

- Logging enabled.
- Destination exists and accepts writes.
- Encryption and access controls.
- Retention meets policy.
- Fields sufficient for incident response.
- Metrics/alarms on block, drop, and alert trends.
- Sensitive headers/domains/network metadata protected.
- Log volume/filtering does not hide critical events.

No logs means weak proof, even if enforcement exists.

### Change evidence

Use CloudTrail to find:

- Who changed rule/action/priority.
- Who associated or disassociated policy.
- Who disabled logging.
- When managed-rule version or policy changed.
- Whether automation role made the change.

Compare change time with traffic/error spike.

### False-positive workflow

```text
Identify exact rule and request/query/flow
  -> confirm business legitimacy
  -> create narrow exception or tune scope
  -> test in COUNT/ALERT where possible
  -> re-enable enforcement
  -> monitor
  -> document owner and expiry.
```

Do not disable the entire web ACL/firewall/rule group for one false positive.

### Bypass investigation

Ask:

- Can workload use another DNS resolver?
- Can client reach origin directly and avoid CloudFront/WAF?
- Does alternate load balancer/domain lack WAF association?
- Is there a route around Network Firewall?
- Is IPv6 path protected while only IPv4 was audited?
- Does another Region/VPC contain an uncovered resource?
- Is a public IP exposing a backend directly?

Protection must cover alternate paths, not only the documented path.

### Safe enforcement pattern

```text
Inventory and associate
  -> enable logging/metrics
  -> ALERT or COUNT
  -> establish baseline
  -> tune narrow exceptions
  -> BLOCK or DROP
  -> monitor errors and attack trend
  -> verify no bypass
  -> preserve rollback.
```

Shield mitigation is different: enable/configure protection and response readiness rather than placing attacks in count mode.

### Evidence-to-service clues

| Evidence | Most relevant service |
|---|---|
| Queried domain and firewall action | DNS Firewall |
| HTTP URI/header/terminating rule | WAF |
| DDoS vector/event/mitigation | Shield |
| IP/port/protocol/signature/flow | Network Firewall |
| ENI five-tuple `ACCEPT`/`REJECT` | VPC Flow Logs |

Use application/access logs with protection logs to prove end result.

### Exam traps

- DNS Firewall filters DNS queries, not direct IP connections.
- DNS `ALERT` allows the query; `BLOCK` stops it.
- Lower numeric priority runs first for DNS Firewall and WAF rules.
- WAF protects HTTP/HTTPS, not arbitrary TCP/UDP.
- WAF `COUNT` observes; it does not block.
- WAF terminating action can prevent later rules from running.
- WAF default action matters when no rule terminates.
- CloudFront and Regional WAF scopes are different.
- Shield Standard is automatic baseline; Advanced needs subscription/configured protections.
- Shield does not replace WAF for SQL injection or application rules.
- Network Firewall protects only routed-through traffic.
- Network Firewall creation alone does not change VPC routes.
- Stateful Network Firewall requires symmetric forward/return paths.
- An alert rule is not a drop rule.
- A policy object without association protects nothing.
- Sampled WAF requests are not complete logs.
- IPv4 control may not cover IPv6 bypass.
- Fix one false positive with a narrow exception, not full-control disablement.

### Do not memorize

- Every AWS Managed Rules group name.
- Every GuardDuty-style threat signature in Network Firewall.
- Full Suricata syntax.
- Exact Shield Advanced pricing or credit terms.
- Exact WAF capacity-unit calculations.
- Full log schemas.
- Console click paths.

### Ready when

Given a network-protection audit scenario, you can:

1. Choose DNS Firewall, WAF, Shield, or Network Firewall by traffic layer.
2. Verify exact VPC/resource association and real traffic-path coverage.
3. Read rule priority, action, default action, and managed-rule overrides.
4. Use query, web, DDoS, firewall, and change evidence.
5. Detect bypass routes, scopes, AZs, protocols, and direct origins.
6. Roll out safely from `ALERT`/`COUNT` to `BLOCK`/`DROP`.
7. Tune narrow exceptions and prove enforcement after remediation.

---

## Skill 5.1.4 — Optimize the cost of network architectures

### Official goal

Find expensive network paths and choose a lower-cost architecture without breaking availability, security, or performance requirements.

### What the exam tests

- Identify the charged hop.
- Read cost and traffic evidence.
- Reduce NAT and cross-AZ processing.
- Compare endpoints, NAT, peering, and Transit Gateway.
- Use CloudFront caching and compression.
- Reduce unnecessary public IPv4 use.
- Preserve required resilience.

### Dimensions

**Primary:** evidence, optimization, selection  
**Support:** behavior, configuration  
**Precision:** L2 — know cost drivers and evidence fields; do not memorize exact prices.

### Core model

```text
Network cost
  = fixed resources
  + bytes processed by middleboxes/services
  + bytes crossing AZ/Region/internet boundaries
  + requests/connections where priced
```

Optimization question:

```text
Which hop can be removed, shortened, cached, or replaced?
```

### Main cost drivers

- Cross-AZ data transfer.
- Cross-Region data transfer.
- Internet data transfer out.
- NAT gateway hourly and per-GB processing.
- Interface endpoint hourly and per-GB processing.
- Transit Gateway attachment and data processing.
- PrivateLink endpoint and data processing.
- Public IPv4/Elastic IP allocation.
- Load balancer hourly/capacity processing.
- Network Firewall processing.
- VPN/Direct Connect connection and transfer components.
- CloudFront requests/data transfer/features.
- High-volume network logs.

Do not assume the largest compute bill caused the largest network bill.

### Cost boundaries

Typical order of concern:

```text
same AZ
  -> cross AZ
  -> cross Region
  -> internet/edge path
```

Exact pricing varies by service and direction. Use billing evidence.

### Evidence sources

**Cost Explorer**

- Find trends and spikes.
- Group/filter by service, account, Region, usage type, operation, and tags.
- Good first view.

**Cost and Usage Report (CUR)**

- Detailed line items.
- Exact usage types, resources where available, accounts, Regions, and cost allocation.
- Query with tools such as Athena.

**VPC Flow Logs**

- Identify source, destination, interface, ports, bytes, and traffic direction.
- Map traffic to AZ/Region/middlebox path.

**CloudWatch metrics**

- NAT bytes/connections/errors.
- TGW/endpoint/load-balancer/firewall traffic.
- CloudFront requests/cache behavior/origin traffic.

**Tags and cost categories**

- Attribute shared network resources to teams/apps/environments.

Cost evidence tells **what charged**. Flow evidence tells **why**.

### Cost investigation order

```text
1. Find service/usage-type cost spike.
2. Find account, Region, AZ, and time window.
3. Map source and destination traffic.
4. Draw every charged hop.
5. Quantify fixed versus per-GB cost.
6. Compare safe alternative paths.
7. Implement small change.
8. Verify cost and service health.
```

Do not optimize from architecture diagrams alone; verify actual traffic.

## NAT gateway optimization

### NAT cost model

Public NAT gateway commonly adds:

- Hourly gateway cost.
- Per-GB processing.
- Possible cross-AZ transfer.
- Internet/service transfer depending destination.

Path example:

```text
Private workload AZ-A
  -> NAT gateway AZ-B
  -> AWS service/internet
```

This can add NAT processing plus cross-AZ traffic.

### Best-known NAT reduction

For S3 or DynamoDB traffic:

```text
Private subnet
  -> gateway endpoint
  -> S3/DynamoDB
```

Benefits:

- Avoid NAT gateway processing for that traffic.
- No gateway-endpoint hourly charge.
- Keep traffic on AWS private service path.

Need route-table association and endpoint/IAM/resource policies.

### Interface endpoint versus NAT

**Interface endpoint costs**

- Fixed endpoint-hour cost per selected AZ.
- Data-processing cost.

**NAT gateway costs**

- Fixed gateway-hour cost.
- Data-processing cost.
- Possible cross-AZ cost.

Selection depends on:

- Number of AWS services.
- Number of AZ endpoint ENIs.
- Traffic volume per service.
- Existing NAT requirement for general internet.
- Availability requirement.
- Security/private-path requirement.

No universal answer: calculate the specific topology.

### Endpoint cost clue

Likely good interface-endpoint case:

- High traffic to a small set of AWS services.
- Private access required.
- NAT traffic can be removed.

Likely weak cost case:

- Many low-volume service endpoints across many AZs.
- NAT already needed for other traffic.
- Endpoint fixed cost exceeds saved NAT processing.

Security requirements can still justify an endpoint even if it is not cheapest.

### NAT per AZ versus centralized NAT

**NAT per AZ**

- Better AZ independence.
- Avoids normal cross-AZ NAT path.
- More hourly NAT gateways.

**One centralized NAT**

- Lower fixed gateway count.
- Creates one-AZ dependency.
- Can add cross-AZ data charges.

Exam answer follows stated priorities:

- High availability/high traffic → often one NAT per AZ.
- Low traffic/cost-first and accepted dependency → centralized may be considered.

Never remove required resilience merely to reduce fixed cost.

### Reduce NAT traffic before removing NAT

Move suitable traffic to:

- S3/DynamoDB gateway endpoints.
- Interface endpoints for selected AWS APIs.
- PrivateLink for private partner/internal services.
- Local package/artifact mirrors where operationally justified.
- IPv6 egress where application/destination support it.

Then reassess whether NAT is still required.

## Cross-AZ optimization

### Common cross-AZ causes

- Workload in AZ-A uses NAT in AZ-B.
- Client hits load-balancer node in one AZ and target in another.
- Application talks repeatedly to database/cache in another AZ.
- Central firewall inspection hairpins traffic.
- TGW or endpoint path uses another AZ.
- One-zone service endpoint serves multi-AZ clients.
- Kubernetes/container traffic ignores topology.

Cross-AZ traffic may be required for resilience. Remove accidental paths, not necessary redundancy.

### Same-AZ alignment

Where service behavior and resilience permit:

- Private subnet uses same-AZ NAT.
- Workload uses local endpoint ENI.
- Load balancer routes efficiently to healthy local targets.
- Distributed firewall endpoint exists per AZ.
- High-volume producer/consumer placement is topology aware.

Do not pin all critical resources to one AZ solely to save transfer cost.

### Load-balancer cross-zone tradeoff

Cross-zone load balancing can:

- Improve distribution and absorb uneven target capacity.
- Send traffic to targets in another AZ.
- Affect transfer/processing depending load-balancer/service pricing behavior.

Before changing it, check:

- Target count and health per AZ.
- Client/source AZ distribution.
- Zonal failure behavior.
- Load-balancer type behavior.
- Actual cross-AZ usage/cost.

Cost optimization must not create overloaded or empty zones.

### Central inspection tradeoff

Centralized TGW/Network Firewall architecture can reduce appliance count but add:

- TGW processing.
- Firewall processing.
- Cross-AZ traffic.
- Extra routing hops.

Distributed inspection can reduce hairpin traffic but adds fixed endpoints/policies.

Compare total bytes and operating complexity, not only resource count.

## Transit and private connectivity cost

### VPC peering versus Transit Gateway

**VPC peering**

- No hub attachment architecture.
- Direct pairwise paths.
- Good for few VPCs.
- Mesh routes/connections become operationally expensive at scale.

**Transit Gateway**

- Attachment and data-processing costs.
- Central routing and segmentation.
- Better operational scaling for many VPCs/hybrid networks.

For two VPCs, peering may cost less. For many networks, TGW can reduce operational complexity despite service charges.

### PrivateLink cost tradeoff

PrivateLink:

- Charges endpoint hours/data processing.
- Exposes one service instead of full routing.
- Supports many consumers and overlapping CIDRs.
- Can reduce security and routing complexity.

Do not replace PrivateLink with peering solely on per-GB cost if isolation is a requirement.

### Centralized interface endpoints

Sharing access through a central networking VPC may reduce endpoint count, but can add:

- TGW/peering processing or transfer.
- Cross-AZ paths.
- Hybrid DNS complexity.
- Larger blast radius.

Distributed endpoints cost more fixed hours but simplify local routing and AZ resilience.

Calculate:

```text
endpoint count × fixed cost
versus
central transit hops + data processing + operations
```

## Cross-Region and hybrid optimization

### Cross-Region traffic

High-cost patterns:

- Chatty application calls across Regions.
- Cross-Region database reads/writes.
- Repeated backup/object copies.
- Centralized log ingestion from every Region.
- Cross-Region peering/TGW traffic.

Optimize by:

- Place compute near data/users.
- Cache/read locally.
- Compress and batch transfers.
- Replicate intentionally, then serve locally.
- Reduce unnecessary bidirectional chatter.
- Apply lifecycle/retention to replicated logs/data.

Do not disable required DR replication to save ordinary transfer cost.

### VPN versus Direct Connect

**Site-to-Site VPN**

- Fast to provision.
- Connection-hour and internet-path characteristics.
- Good for backup/lower-volume or rapid connectivity.

**Direct Connect**

- Dedicated capacity/port and transfer pricing.
- Can be cost/performance efficient for large steady hybrid traffic.
- Has fixed commitment and redundancy requirements.

Compare volume, predictability, latency, setup time, encryption, and HA—not price alone.

## Public IPv4 optimization

Public IPv4 addresses have cost implications.

Inventory:

- EC2 public IPv4 addresses.
- Elastic IPs.
- NAT gateway EIPs.
- Public load balancers.
- Unassociated/idle allocations.

Reduce by:

- Put application instances in private subnets behind a load balancer.
- Use SSM Session Manager instead of public-IP bastions where suitable.
- Use VPC endpoints for AWS APIs.
- Release unused EIPs.
- Use IPv6 where end-to-end support and controls exist.

Do not remove a public address until the replacement management/application path is verified.

## CloudFront optimization

### Why CloudFront can reduce total cost

```text
Viewer
  -> edge cache hit
  -> origin not contacted
```

Possible savings:

- Less origin data transfer.
- Fewer origin requests.
- Less origin compute/load-balancer work.
- Lower latency.

CloudFront itself has request/data/features costs. Optimize total architecture, not one bill line.

### Improve cache hit ratio

- Set appropriate `Cache-Control`/TTL.
- Keep cache key small.
- Forward only required headers, cookies, and query strings.
- Version static object names.
- Avoid unnecessary invalidations.
- Use Origin Shield where extra cache layer and origin protection justify cost.

A highly variable cache key turns CloudFront into an expensive proxy with few hits.

### Compression

- Compress text-like objects.
- Enable supported edge compression.
- Cache compressed variants correctly.
- Avoid recompressing already compressed formats.

Compression trades small CPU/feature work for fewer transferred bytes.

### CloudFront Price Class recognition

Price Class can limit which edge-location groups serve content.

- Lower-cost class can reduce delivery cost.
- May increase latency for users outside included geography.

Choose only when geographic performance tradeoff is acceptable.

### CloudFront evidence

- Requests by distribution/behavior.
- Cache hit/miss ratio.
- Bytes downloaded/uploaded.
- Origin request volume.
- HTTP status/errors.
- Log cache-result fields.
- Cost by usage type/geography.

Low hit ratio + high origin bytes = optimization target.

## Global Accelerator distinction

Global Accelerator:

- Uses AWS global network and static anycast IPs.
- Improves routing/availability for TCP/UDP applications.
- Does not cache content.
- Adds accelerator/data-transfer premium charges.

Use CloudFront for caching HTTP content. Use Global Accelerator when network-path acceleration/static IP/failover is required.

## Load-balancer cost

Load balancers commonly charge:

- Time running.
- Capacity/processed traffic dimensions.
- Additional feature/data paths depending service.

Audit:

- Idle load balancers.
- Duplicate test resources.
- Processed bytes and connections/requests.
- Rule complexity where relevant.
- Cross-zone path.
- TLS and target response behavior.
- Whether consolidation would preserve isolation and scaling.

Do not consolidate unrelated critical applications into one blast radius only to remove an hourly charge.

## Logging cost

High-volume sources:

- VPC Flow Logs.
- WAF logs.
- Network Firewall logs.
- Load-balancer access logs.
- CloudFront logs.

Optimize safely:

- Log the fields/traffic needed.
- Filter where supported.
- Use efficient format/destination.
- Compress and lifecycle S3 logs.
- Set intentional CloudWatch Logs retention.
- Separate security retention from debugging retention.

Do not disable required audit logs merely to reduce ingestion cost.

## Cost allocation and governance

Use:

- Cost allocation tags.
- Cost categories.
- Linked-account/OU grouping.
- Budgets.
- Cost Anomaly Detection.
- Ownership tags on NAT, endpoints, TGW attachments, firewalls, and load balancers.

Shared network cost needs an allocation rule; otherwise optimization ownership is unclear.

### Usage-type clues

Recognize billing terms containing concepts such as:

- NAT gateway hours/bytes.
- Regional data transfer.
- VPC endpoint hours/bytes.
- Transit Gateway attachment/bytes.
- Public IPv4 address hours.
- CloudFront requests/data transfer.

Exact usage-type prefixes vary by Region/report. Search/group; do not memorize the full string.

### Scenario selector

| Scenario | Likely optimization |
|---|---|
| Large S3 traffic through NAT | S3 gateway endpoint |
| High API traffic to few AWS services through NAT | Evaluate interface endpoints |
| Cross-AZ NAT bytes | Same-AZ NAT per private subnet or redesign path |
| Many low-volume endpoints | Compare endpoint fixed cost with shared NAT |
| Two VPCs only | Evaluate peering versus TGW |
| Many VPC mesh | Evaluate TGW operational/cost tradeoff |
| Global static content hits origin repeatedly | CloudFront caching and TTL/cache-key tuning |
| High public IPv4 count | Private subnets, LB/endpoints, release idle EIPs, IPv6 where valid |
| Chatty cross-Region application | Co-locate, cache, batch, or serve from replica |
| High log ingestion/storage | Filter, compress, lifecycle, retention—preserve required evidence |

### Savings Plans trap

Savings Plans apply to eligible compute usage.

They do not generally remove:

- Network data-transfer charges.
- NAT processing.
- Endpoint hourly/data charges.
- TGW processing.
- Public IPv4 charges.

Choose an architecture change for network cost, not a compute discount plan.

### Optimization scorecard

For each option, compare:

| Dimension | Question |
|---|---|
| Cost | Fixed resources + per-GB + transfer boundaries? |
| Availability | New AZ/Region dependency? |
| Security | Public path or broader network access introduced? |
| Performance | More latency/hops or better caching/locality? |
| Operations | More endpoints/routes/policies to manage? |
| Scale | Does design remain manageable as VPCs/services grow? |

The cheapest single component can create a more expensive total system.

### Safe optimization process

```text
Baseline cost and traffic
  -> map charged path
  -> model alternatives
  -> preserve HA/security requirements
  -> test one workload/AZ
  -> monitor latency/errors/bytes
  -> expand
  -> verify next billing period/usage data
  -> remove old resource only after proof.
```

Billing data can lag. Use traffic metrics for early verification and cost data for final proof.

### Common failed optimizations

| Change | Hidden failure |
|---|---|
| Remove per-AZ NATs | Single-AZ dependency and cross-AZ bytes |
| Add every interface endpoint | Fixed endpoint cost exceeds NAT savings |
| Centralize all endpoints | TGW/cross-AZ processing and DNS complexity |
| Disable cross-zone balancing | Uneven capacity or zonal overload |
| Co-locate everything in one AZ | Lost availability |
| Increase CloudFront TTL blindly | Stale content/security-sensitive caching |
| Disable network logs | Lost audit/incident evidence |
| Remove public IP before endpoint setup | Management/application outage |

### Exam traps

- S3/DynamoDB gateway endpoints avoid NAT processing and have no endpoint-hour charge.
- Interface endpoints have fixed per-AZ cost; more endpoints are not always cheaper.
- One NAT per AZ improves resilience and can avoid cross-AZ traffic, but adds hourly cost.
- Central NAT reduces count but may add cross-AZ cost and one-AZ dependency.
- Peering may fit few VPCs; TGW fits scale/segmentation but adds processing cost.
- PrivateLink cost can be justified by service isolation and overlapping CIDRs.
- Cross-AZ traffic can hide inside NAT, endpoint, firewall, TGW, and load-balancer paths.
- CloudFront saves origin work only when requests cache effectively.
- Global Accelerator accelerates network paths but does not cache.
- Public IPv4 cost is an architecture driver, not only an idle-EIP issue.
- Savings Plans do not solve network-transfer charges.
- Cost Explorer finds trends; CUR gives line-item detail; Flow Logs explain traffic path.
- Never remove required HA, security controls, or audit logging solely for cost.

### Do not memorize

- Exact per-GB or hourly prices.
- Every CUR usage-type prefix.
- Exact load-balancer capacity-unit formulas.
- Every CloudFront price by geography.
- Every free-transfer exception.
- Console click paths.

### Ready when

Given a network-cost scenario, you can:

1. Find the charged service/hop using Cost Explorer, CUR, metrics, and Flow Logs.
2. Reduce S3/DynamoDB NAT traffic with gateway endpoints.
3. Compare interface endpoints with NAT by AZ count and traffic volume.
4. Identify and remove accidental cross-AZ/cross-Region hairpins.
5. Compare peering, TGW, PrivateLink, VPN, and Direct Connect tradeoffs.
6. Improve CloudFront cache efficiency and reduce origin transfer.
7. Reduce public IPv4 and logging cost without breaking access or evidence.
8. Verify savings while preserving availability, security, and performance.

---

## Skill 5.2.1 — Configure DNS and Route 53 Resolver

### Official goal

Configure DNS resolution, hosted zones, records, and hybrid Route 53 Resolver paths.

### What the exam tests

- Distinguish recursive and authoritative DNS.
- Choose public or private hosted zone.
- Select the correct record type.
- Know alias versus CNAME.
- Configure VPC DNS attributes.
- Choose Resolver inbound or outbound endpoint.
- Associate and share forwarding rules.
- Diagnose cache, zone, DNS path, SG, route, and upstream failures.

### Dimensions

**Primary:** configuration, behavior, diagnosis  
**Support:** remediation, governance  
**Precision:** L3 — exact zone visibility, record behavior, endpoint direction, rule match, association, and DNS/network path matter.

### Core DNS model

```text
Application
  -> recursive resolver
      -> cache
      -> private hosted zone
      -> forwarding rule/upstream DNS
      -> public DNS hierarchy
  -> authoritative answer
```

DNS answer and network connectivity are separate layers.

### Recursive versus authoritative

**Recursive resolver**

- Receives client query.
- Finds the answer.
- Follows delegations or forwards query.
- Caches result for TTL.
- Route 53 VPC Resolver is recursive.

**Authoritative server**

- Owns a DNS zone.
- Returns records for that zone.
- Does not normally recurse for the client.
- Route 53 hosted-zone name servers are authoritative.

Exam trap: an on-premises DNS server and a Route 53 hosted zone solve different roles.

### Public DNS hierarchy

```text
Root
  -> top-level domain: .com
  -> authoritative zone: example.com
  -> record: app.example.com
```

Delegation uses `NS` records from parent to child zone.

For a registered domain, registrar name-server values must point to the intended public hosted-zone name servers.

### Domain, hosted zone, and record

- Domain registration gives control of a domain name.
- Hosted zone stores authoritative DNS records.
- Record maps a name/type to a value or routing target.

Creating a hosted zone does not automatically change registrar delegation when the domain is registered elsewhere.

### DNS names

```text
api.prod.example.com.
```

- `com` = top-level domain.
- `example.com` = domain/zone example.
- `api.prod` = labels below the zone.
- Final dot means fully qualified absolute name.

DNS names are generally case-insensitive. Record values may have their own syntax/case behavior.

### TTL and cache

TTL tells resolvers how long an answer can be cached.

```text
Authoritative record changes
  -> old cached answer remains until TTL expires
  -> new query receives new answer
```

Low TTL:

- Faster planned change/failover.
- More DNS queries.

High TTL:

- More caching/fewer queries.
- Slower change visibility.

Changing a record does not purge every client/resolver cache immediately.

### Negative caching

Resolvers can cache negative answers such as `NXDOMAIN` according to zone/SOA behavior.

After creating a previously missing record, some clients can still see the cached negative result temporarily.

### Record types

| Record | Meaning |
|---|---|
| `A` | Name to IPv4 address |
| `AAAA` | Name to IPv6 address |
| `CNAME` | One name to another canonical name |
| Alias | Route 53 name to supported AWS/DNS target |
| `MX` | Mail server with priority |
| `TXT` | Text, often validation or email/security data |
| `NS` | Authoritative name servers/delegation |
| `SOA` | Zone authority and negative-cache metadata |
| `PTR` | Reverse DNS: address to name |

Know behavior, not every record format.

### A and AAAA

```text
app.example.com A     192.0.2.10
app.example.com AAAA  2001:db8::10
```

Dual-stack clients can query both.

Having an `AAAA` answer requires a working IPv6 route/security/application path. DNS can advertise a path that is not reachable.

### CNAME

```text
www.example.com CNAME app.vendor.example
```

Properties:

- Points one DNS name to another.
- Resolver then resolves target name.
- Cannot be used at the zone apex in standard DNS.
- Cannot normally coexist with other record data at the same owner name.
- Adds another name-resolution step/cache relationship.

Zone apex example: `example.com`.

### Route 53 alias

Alias record:

- Can target supported AWS resources and another Route 53 record.
- Can be used at zone apex.
- Appears as the chosen record type, commonly `A`/`AAAA`, not as a CNAME answer.
- Can use target-health evaluation where supported.
- Uses target-related TTL behavior instead of a normal CNAME chain.

Common alias targets include supported load balancers, CloudFront distributions, API endpoints, and S3 website endpoints.

### Alias versus CNAME

| Need | Choose |
|---|---|
| Zone-apex AWS target | Alias |
| Supported AWS target without exposing CNAME chain | Alias |
| Ordinary subdomain to arbitrary DNS name | CNAME |
| Apex to arbitrary non-AWS target | Cannot use standard CNAME; redesign/use supported record approach |

An alias is a Route 53 feature, not a universal DNS record type.

### MX and TXT traps

**MX**

- Contains priority and mail-server hostname.
- Must point to a hostname, not directly to a CNAME-like URL.

**TXT**

- Used for domain validation and policies such as email authentication.
- Exact quoting/segmentation matters to the consuming service.

Do not replace an ACM validation CNAME with TXT unless ACM explicitly asks for TXT.

### NS and delegation

Parent zone delegates a child:

```text
Parent: example.com
NS record for dev.example.com -> child-zone name servers
```

Child zone then answers names beneath `dev.example.com`.

Common failure:

- Child hosted zone exists.
- Parent has no/wrong `NS` delegation.
- Public resolvers never reach child zone.

### Wildcard record

```text
*.example.com
```

- Matches names when no more-specific record exists.
- Does not represent the zone apex itself.
- An explicit record overrides wildcard matching for that name.

Do not confuse DNS wildcard behavior with TLS wildcard certificate matching.

## Hosted zones

### Public hosted zone

- Authoritative on the public internet after correct delegation.
- Stores public DNS records.
- Answers any internet resolver.
- Does not make a private target reachable from the internet.

Public DNS can legally return a private IP, but that does not create private routing and can expose internal naming information.

### Private hosted zone

- Authoritative only through Route 53 Resolver for associated VPCs/hybrid Resolver paths.
- Must be associated with one or more VPCs.
- Useful for internal names and split-horizon DNS.
- Not delegated through public internet name servers.

Association, not account ownership alone, gives a VPC visibility.

### Private hosted-zone association

Check:

- Correct VPC ID.
- Correct Region/account context.
- VPC DNS support enabled.
- Cross-account association authorization when required.
- Association completed, not only authorized.
- Resolver query originates through an associated VPC context.

Cross-account flow commonly needs:

```text
Zone owner authorizes VPC association
  -> VPC owner associates VPC
  -> authorization can be cleaned up after success.
```

### Split-horizon DNS

Same name can have different public and private answers.

```text
Public zone:  app.example.com -> public load balancer
Private zone: app.example.com -> internal load balancer
```

Associated VPC clients use the private namespace. Internet clients use public DNS.

### Private-zone shadowing

If an associated private hosted zone covers `example.com`, Route 53 Resolver uses that private namespace for matching names.

If `missing.example.com` is absent there, Resolver does not simply fall back to the public `example.com` zone. It can return `NXDOMAIN`.

This is a common reason a public record works outside the VPC but fails inside it.

### Overlapping private zones

Example:

```text
example.com
dev.example.com
```

Resolver uses the most-specific matching namespace for `app.dev.example.com`.

If the record is missing in that selected private zone, do not assume fallback to the broader zone.

### Hosted-zone failure map

| Symptom | First checks |
|---|---|
| Public name returns `NXDOMAIN` everywhere | Delegation, exact zone/record/name/type |
| Works publicly, fails in VPC | Private-zone shadowing, Resolver rule, VPC DNS |
| Works in one VPC only | Private-zone association and DNS attributes |
| Child zone unreachable | Parent `NS` delegation |
| Old answer persists | TTL/negative cache/resolver cache |
| Alias target absent/wrong | Target name/type/Region/support and health setting |

## Route 53 VPC Resolver

### Default Resolver

Each VPC has Amazon-provided recursive DNS behavior.

Recognize resolver addresses:

- VPC network base plus two address.
- Link-local address `169.254.169.253`.

Applications normally receive the Resolver through DHCP configuration.

It resolves:

- Public DNS names.
- Private hosted-zone names associated with the VPC.
- VPC-specific names.
- Forwarded namespaces through Resolver rules.

### VPC DNS attributes

- `enableDnsSupport` — use Amazon-provided DNS resolution.
- `enableDnsHostnames` — assign/use supported DNS hostnames for VPC resources.

Private hosted zones require DNS support.

Changing DHCP to custom DNS can bypass direct use of VPC Resolver unless that custom DNS forwards appropriately.

### Resolver endpoint direction

Memory rule:

```text
Inbound endpoint  = queries enter AWS/VPC Resolver
Outbound endpoint = queries leave AWS/VPC Resolver toward external DNS
```

Direction describes DNS-query direction, not who created the endpoint.

## Resolver inbound endpoint

### Purpose

Allows on-premises or connected networks to query Route 53 Resolver.

```text
On-premises client
  -> on-premises DNS server
  -> conditional forward for aws.internal
  -> Resolver inbound endpoint private IPs
  -> private hosted zone/VPC Resolver answer
```

Use for on-premises resolution of AWS private names.

### Inbound endpoint objects

- Endpoint in a VPC.
- Endpoint ENI IPs in selected subnets/AZs.
- Security group.
- On-premises conditional-forwarding rule.
- VPN/Direct Connect/TGW routing path.
- Private hosted-zone associations.

Deploy endpoint IPs across at least two AZs for resilient design.

### Inbound endpoint network path

Need:

- On-premises route to endpoint private IPs.
- AWS return route to on-premises networks.
- Endpoint SG inbound TCP and UDP port `53` from approved DNS servers.
- NACLs allowing query and return traffic.
- On-premises firewall allowing both directions.
- On-premises DNS forwards the correct domain to both endpoint IPs.

Allow both UDP and TCP DNS. Large/truncated answers can retry over TCP.

### Inbound endpoint traps

- Inbound endpoint does not forward VPC queries to on premises.
- Creating endpoint does not configure on-premises conditional forwarding.
- Endpoint IPs are private; hybrid routing must exist.
- Security group source should be approved DNS resolvers, not broad internet CIDRs.
- Private hosted zone still needs correct VPC association.

## Resolver outbound endpoint

### Purpose

Allows Route 53 Resolver to forward selected VPC DNS queries to external/on-premises DNS servers.

```text
VPC application
  -> VPC Resolver
  -> matching Resolver forwarding rule
  -> outbound endpoint ENI
  -> on-premises DNS target IP
  -> internal-domain answer
```

Use when AWS workloads need on-premises/internal names.

### Outbound endpoint objects

- Outbound endpoint in selected subnets/AZs.
- Endpoint security group.
- Forwarding rule with domain and target DNS IPs/ports.
- Rule association with querying VPCs.
- Route/VPN/DX/TGW path to target DNS servers.
- Optional RAM sharing of rule.

Endpoint alone does nothing until a matching rule is associated.

### Outbound endpoint network path

Need:

- Endpoint SG outbound TCP and UDP `53` to target DNS servers.
- Route from endpoint subnets to on premises/external DNS.
- Return route to endpoint IPs.
- NACL/firewall allowance.
- Target DNS server listening and permitting endpoint source IPs.
- Multiple endpoint/target IPs for resilience.

Do not send queries to a DNS server that cannot answer or recurse for the forwarded namespace.

### Outbound endpoint traps

- Outbound endpoint does not receive on-premises queries for AWS zones.
- Rule must be associated with the source VPC.
- Domain match must include intended suffix.
- DNS target must be reachable from endpoint subnets.
- SG outbound `53` alone is insufficient without return route/firewall.

## Resolver rules

### Forwarding rule

Defines:

- Domain suffix to match.
- Outbound endpoint.
- Target DNS server IPs and ports.
- Rule owner/share.
- VPC associations.

Example:

```text
Rule: corp.example.com
Target: 10.50.0.10, 10.50.0.11
```

Query `db.corp.example.com` matches.

### Most-specific rule match

Example:

```text
example.com      -> DNS server A
dev.example.com  -> DNS server B
```

Query `api.dev.example.com` uses the `dev.example.com` rule.

Resolver forwarding selection is based on the most-specific matching domain, not a WAF/DNS-Firewall-style numeric rule priority.

### System-rule recognition

A system rule can make a more-specific namespace use normal Route 53 Resolver behavior instead of a broader forwarding rule.

Example intent:

```text
Forward example.com on premises
but resolve aws.example.com through normal Resolver behavior.
```

Know the exception pattern; do not memorize rule API syntax.

### Rule association

- A rule applies only to associated VPCs.
- One outbound endpoint can support multiple rules.
- A shared rule still needs recipient VPC association.
- Rule owner and VPC owner can be different through RAM sharing.
- Removing association stops forwarding for that VPC.

### RAM sharing

Resource Access Manager can share Resolver rules across accounts.

Central model:

```text
Networking account owns outbound endpoint/rules
  -> shares rules through RAM
  -> application account accepts/receives share
  -> associates VPCs
```

Sharing a rule does not automatically associate every VPC or create network reachability to target DNS servers.

### Overlapping rule and zone investigation

When several namespaces can answer, inventory:

- Associated private hosted zones.
- Forwarding/system rules.
- Exact query name.
- Most-specific matching suffix.
- Rule/zone associations to source VPC.
- Interface endpoint private DNS zones.
- Client’s actual resolver.

Do not guess from the domain name alone; test from the failing VPC.

## Hybrid DNS patterns

### Bidirectional hybrid DNS

```text
On premises asks AWS names
  -> inbound endpoint

AWS asks on-premises names
  -> outbound endpoint + forwarding rule
```

Most hybrid environments needing both directions require both endpoint types.

### Centralized outbound DNS

```text
Shared-services VPC
  -> outbound endpoint
  -> on-premises DNS

Resolver rules shared to spoke VPCs
  -> spoke VPC associations
```

Benefits:

- Fewer endpoints.
- Central policy/logging.

Need:

- RAM sharing and associations.
- Endpoint route to on premises.
- Resilience/capacity.
- Clear ownership and change control.

### PrivateLink/interface-endpoint DNS from on premises

```text
On-premises DNS conditional forward for AWS service/private name
  -> Resolver inbound endpoint
  -> VPC private DNS
  -> interface endpoint private IPs
```

On-premises DNS will not automatically see interface-endpoint private DNS without the Resolver path.

### Custom DNS server pattern

If EC2-based/custom DNS servers are used:

- Make them highly available.
- Configure forwarding to VPC Resolver for AWS/private-zone names.
- Configure outbound forwarding carefully to avoid loops.
- Allow UDP/TCP `53` and return path.
- Monitor cache and server health.

Managed Resolver endpoints usually reduce custom server operations for hybrid forwarding.

## Troubleshooting

### DNS troubleshooting ladder

```text
1. What exact FQDN and record type?
2. Which resolver did the client query?
3. What answer/code and TTL came back?
4. Is answer cached/stale/negative-cached?
5. Which public/private zone or Resolver rule is most specific?
6. Is zone/rule associated with source VPC?
7. Correct inbound/outbound endpoint direction and status?
8. Endpoint SG allows UDP and TCP 53?
9. Forward and return route/NACL/firewall work?
10. Target authoritative/upstream DNS can answer?
11. Does resolved IP have network/application reachability?
```

Always record the resolver server used in the test.

### DNS response clues

| Result | Likely meaning/first checks |
|---|---|
| `NOERROR` + answer | Resolution succeeded; test target connectivity |
| `NOERROR` + no data | Name exists but requested type may not |
| `NXDOMAIN` | Name absent in selected namespace; shadowing/delegation/typo |
| `SERVFAIL` | Resolver/upstream/DNSSEC/server failure or loop |
| `REFUSED` | DNS server policy/authorization refuses query |
| Timeout | Route, SG, NACL, firewall, endpoint, server unavailable |
| Old/wrong answer | TTL/cache, wrong zone, split-horizon, wrong resolver |

Response code narrows the layer faster than “DNS does not work.”

### Query tools and evidence

Use client tools such as `dig` or `nslookup` to capture:

- Queried name and type.
- Resolver server address.
- Answer/authority section.
- Response code.
- TTL.
- CNAME chain.
- Query time.
- UDP versus TCP behavior.

For public delegation, trace from root/parent authority where appropriate.

### Resolver query logs

Can show:

- Query name/type.
- Source VPC and source IP/resource context where available.
- Response code/answer behavior.
- Resolver rule/firewall action context where available.
- Query time.

Need query-log configuration and VPC association. Logs are detailed further in 5.2.2.

### Network evidence

Check:

- Endpoint ENIs and IPs.
- Endpoint status.
- Endpoint SG rules.
- Route tables from endpoint subnets to DNS targets.
- VPN/TGW/DX state and routes.
- NACL/firewall rules.
- VPC Flow Logs for endpoint/target IP port `53`.
- On-premises DNS logs.
- CloudTrail for zone/rule/endpoint changes.

Flow Log acceptance proves packet control, not correct DNS answer.

### Hybrid DNS failure map

| Symptom | First checks |
|---|---|
| AWS cannot resolve on-premises domain | Outbound endpoint, matching rule, VPC association, target reachability |
| On premises cannot resolve private AWS domain | Inbound endpoint, on-prem forwarder, PHZ association, route/SG |
| Works from one VPC only | Rule/PHZ/query-log association and VPC DNS settings |
| UDP queries work; large answers fail | TCP `53` SG/NACL/firewall path |
| Query loops/`SERVFAIL` | Forwarders pointing back at each other, overlapping rules |
| Public name fails only inside VPC | Private-zone/interface-endpoint shadowing |
| Endpoint IP reachable but query refused | Target/Resolver policy, wrong endpoint direction, source not allowed |
| IP connection works but hostname fails | DNS layer only; do not change application SG first |

### Safe DNS change

```text
Record current zone/rule/delegation and TTL
  -> lower TTL before planned public-record change if needed
  -> create new record/rule/endpoint
  -> test from every relevant resolver/VPC/on-prem path
  -> verify UDP and TCP where hybrid
  -> monitor query logs/application
  -> remove old path after cache window
  -> retain rollback.
```

DNS rollback also waits on caches. Plan before change.

### Governance

- Centralize ownership of public delegations.
- Tag hosted zones, endpoints, and rules.
- Share Resolver rules through controlled RAM shares.
- Limit endpoint SGs to approved DNS servers/networks.
- Log DNS queries according to privacy and retention policy.
- Track changes with CloudTrail/Config where supported.
- Avoid duplicate/conflicting zones across accounts.
- Document authoritative owner for each internal domain suffix.

### Exam traps

- Recursive resolver finds answers; authoritative server owns a zone.
- Public hosted zone controls public DNS, not network reachability.
- Private hosted zone works only through associated VPC/Resolver context.
- Private zone can shadow public names and return `NXDOMAIN` without fallback.
- CNAME cannot be used at zone apex; Route 53 alias can.
- Alias is a Route 53 feature, not a standard CNAME record.
- `A` is IPv4; `AAAA` is IPv6.
- TTL means old answers can persist after change.
- Inbound Resolver endpoint lets queries enter AWS Resolver.
- Outbound Resolver endpoint sends matching VPC queries to external DNS.
- Outbound endpoint requires a forwarding rule and VPC association.
- Inbound endpoint requires on-premises conditional forwarding.
- Resolver forwarding uses most-specific domain match, not numeric priority.
- Share does not equal VPC association.
- Endpoint SG and network path need both UDP and TCP port `53`.
- Connected networks do not automatically share private DNS visibility.
- DNS resolution success does not prove the returned target is reachable.

### Do not memorize

- Every DNS RFC detail.
- Every Route 53 record type.
- Full SOA field format.
- Exact Resolver endpoint quotas.
- Every DNSSEC failure code.
- Complete `dig` output format.
- Console click paths.

### Ready when

Given a DNS scenario, you can:

1. Separate client, recursive resolver, forwarding rule, and authoritative zone.
2. Choose public/private hosted zone and correct record type.
3. Explain alias versus CNAME, delegation, TTL, and private-zone shadowing.
4. Configure VPC DNS attributes and private-zone associations.
5. Choose inbound for on-premises-to-AWS queries and outbound for AWS-to-on-premises queries.
6. Build Resolver endpoint, forwarding-rule, RAM-share, and VPC-association paths.
7. Diagnose cache, namespace, endpoint, SG, route, upstream server, and target-connectivity failures.

---

## Skill 5.2.2 — Implement Route 53 routing policies, configurations, and query logging

### Official goal

Choose and configure Route 53 routing policies, health behavior, and DNS query logging.

### What the exam tests

- Select a routing policy from the business requirement.
- Configure record-set policy properties.
- Combine health checks with routing.
- Understand TTL and recursive caching.
- Distinguish public authoritative query logs from Resolver query logs.
- Use logs to prove which DNS layer received the query.

### Dimensions

**Primary:** selection, configuration, behavior, evidence  
**Support:** diagnosis  
**Precision:** L3 — exact policy purpose, record properties, health association, TTL, and query-log type/destination matter.

### Core routing model

```text
DNS query arrives
  -> matching hosted zone/name/type
  -> routing policy selects eligible record(s)
  -> health removes unhealthy choices where configured
  -> answer cached for TTL
```

Route 53 returns DNS answers. It does not proxy the application connection.

### Fast policy selector

| Requirement | Policy |
|---|---|
| One ordinary answer/no special logic | Simple |
| Percentage split or gradual rollout | Weighted |
| Lowest measured AWS-network latency | Latency |
| Active-passive primary/secondary | Failover |
| Route by user country/continent/state | Geolocation |
| Route by geography with movable bias boundary | Geoproximity |
| Return several healthy IPs | Multivalue answer |
| Route by client/resolver CIDR | IP-based |

### Record-set properties

Depending on policy, know:

- Record name.
- Record type.
- Values or alias target.
- TTL for non-alias records.
- Set identifier.
- Weight.
- Region.
- Failover role: primary/secondary.
- Geolocation.
- Geoproximity location and bias.
- Multivalue-answer flag.
- IP-based CIDR location.
- Health check ID.
- Alias `EvaluateTargetHealth`.

Records in one policy set normally share the same name and type and use unique set identifiers.

## Simple routing

### Purpose

Use when no special routing logic is required.

```text
app.example.com -> one value
```

or multiple values in one record set:

```text
app.example.com -> IP-A, IP-B, IP-C
```

Resolver receives the values without policy-driven health/weight selection.

### Simple behavior

- One record set for a name/type.
- Can contain multiple values.
- Multiple returned values can be reordered.
- Does not provide weighted, latency, geography, or active-passive logic.
- Multiple values are not a managed load balancer.

Use an alias to a load balancer when application-aware balancing and target health are required.

### Simple traps

- Multiple IPs do not guarantee equal traffic.
- Client/resolver may use only one returned address.
- Failed endpoints can remain in the answer without a health-aware policy.
- DNS has no connection/session awareness.

## Weighted routing

### Purpose

Split DNS responses according to relative weights.

```text
Blue  weight 90
Green weight 10
```

Approximate long-run answer ratio:

```text
Blue 90%
Green 10%
```

### Weighted uses

- Canary deployment.
- A/B testing.
- Gradual migration.
- Active-active distribution.
- Drain one endpoint by reducing weight.

### Weighted properties

- Same record name and type.
- Unique set identifier per record.
- Weight is relative to sum of eligible weights.
- Health check can remove an unhealthy weighted record.
- Weight `0` normally suppresses a record while other eligible records have positive weight.

DNS caching means individual users and short samples will not match the exact percentage.

### Weighted traps

- Weight is DNS-answer probability, not per-request load balancing.
- Recursive resolvers cache and serve many clients.
- Existing connections do not move after weight changes.
- Setting low TTL improves change speed but increases queries.
- If all weights are zero, Route 53 does not mean “return nothing”; understand the set’s fallback behavior.

## Latency routing

### Purpose

Return the healthy endpoint in the AWS Region with lowest measured network latency for the query source.

```text
Europe resolver -> eu-west endpoint
Asia resolver   -> ap-southeast endpoint
```

Actual selection uses AWS latency measurements, not a static distance map.

### Latency properties

- One record per serving Region/location.
- Unique set identifier.
- Region property.
- Optional health check/evaluate target health.
- Route 53 can change choice as latency measurements change.

### Latency traps

- “Nearest geography” is not the same as lowest measured latency.
- It does not obey data-residency borders by itself.
- Source is normally the recursive resolver location, improved where EDNS client-subnet data is used.
- DNS TTL delays visible failover/selection changes.
- Endpoint still needs enough capacity.

Use geolocation for location policy; use latency for performance routing.

## Failover routing

### Purpose

Active-passive DNS.

```text
PRIMARY healthy   -> return primary
PRIMARY unhealthy -> return secondary
```

### Failover properties

- Two logical roles: `PRIMARY` and `SECONDARY`.
- Same name/type.
- Unique set identifiers.
- Primary health must be known through health check or supported alias target health.
- Secondary can also have health evaluation.

### Failover timing

Failover time includes:

```text
health detection time
  + Route 53 evaluation
  + recursive/client cached TTL
  + application retry/reconnect
```

Low TTL alone does not make a slow health check fast.

### Failover traps

- Secondary record without a ready application is not DR.
- Health checker must test the real dependency/path.
- Private endpoint cannot be tested directly by public Route 53 health checkers.
- Cached primary answers can remain until TTL expires.
- When all eligible records are unhealthy, Route 53 can return records to avoid a complete DNS black hole; do not treat DNS health as a traffic firewall.

## Geolocation routing

### Purpose

Route according to the location of the DNS query source.

Locations can include:

- Continent.
- Country.
- US state where supported.
- Default catch-all.

### Geolocation behavior

- Most-specific matching location wins.
- Useful for localization, licensing, content policy, and broad data-routing requirements.
- Default record handles unmatched or unmapped locations.
- Health evaluation can remove an unhealthy location record.

### Geolocation traps

- It is not lowest-latency routing.
- DNS source is usually resolver location, not guaranteed exact end-user GPS location.
- Without a default record, some users can receive no answer.
- Geographic routing alone does not prove legal compliance or prevent users from reaching another endpoint directly.

## Geoproximity routing

### Purpose

Route by geographic proximity between users and resources, with **bias** to move the boundary.

```text
Positive bias -> expand resource's geographic catchment
Negative bias -> shrink it
```

Resources can be identified by supported AWS Region or latitude/longitude location.

### Geoproximity uses

- Shift more traffic toward one Region without fixed country rules.
- Gradually rebalance geographic traffic.
- Route near resources while adjusting for capacity.

### Geoproximity traps

- Bias changes boundary; it is not a percentage weight.
- It is not exact latency measurement.
- It is not strict country-based geolocation.
- Large bias can move more traffic than expected; test traffic-flow result.

## Multivalue answer routing

### Purpose

Return multiple healthy records for one name.

- Each record can have its own health check.
- Route 53 returns up to eight healthy values in an answer.
- Can improve client-side distribution/resilience for simple endpoints.

### Multivalue traps

- It is not a substitute for ELB.
- No connection awareness.
- Client may use only the first address.
- TTL caching still applies.
- Health check sees endpoint from checker perspective, not every client path.

Use ELB when managed connection/request distribution is required.

## IP-based routing

### Purpose

Return an answer based on the query source’s IP CIDR mapping.

Objects:

- CIDR collection.
- CIDR locations/blocks.
- IP-based record tied to a CIDR location.
- Default/fallback location as designed.

### IP-based uses

- Route known ISP/network ranges.
- Customize answers for corporate/client networks.
- Optimize routing where IP ownership is known more precisely than geography.

### IP-based traps

- Selection is based on DNS query source information, often recursive resolver IP or available EDNS client-subnet information.
- NAT/resolver architecture can hide the end client.
- CIDR collection must be maintained as networks change.
- Most-specific CIDR mapping should represent the intended network.
- It is not security authorization; clients can still attempt another reachable endpoint.

## Health checks

### Health-check choices

Recognize:

- Endpoint health check: HTTP, HTTPS, or TCP.
- Calculated health check combining other checks.
- CloudWatch alarm health check.
- Alias `EvaluateTargetHealth` for supported AWS targets.

Choose the health signal that represents the application, not merely an open port.

### Endpoint health check

Can test:

- Public IP or domain.
- Port and protocol.
- HTTP path.
- Response status.
- Optional content string where supported.
- Request interval and failure threshold.

Route 53 health checkers must be allowed through firewall/WAF/SG and must reach the endpoint.

### Private endpoint health

Public Route 53 health checkers cannot directly reach a private-only address.

Common pattern:

```text
Private application metrics
  -> CloudWatch alarm
  -> Route 53 health check based on alarm
  -> routing decision
```

Or use supported alias target health.

Do not expose a private service publicly merely so a health checker can reach it.

### Calculated health check

Combines child health checks with a threshold.

Useful for:

- Multi-component application health.
- Maintenance overrides.
- Quorum-style condition.

Avoid a circular dependency where DNS health depends on the same DNS name being routed.

### Alias EvaluateTargetHealth

When supported:

- `true` makes Route 53 use health information of the alias target.
- Useful for ELB and supported AWS targets.
- Does not create a separate external health-check request.

Target resource must have meaningful underlying health. An empty/unhealthy target group can affect alias health.

### Health-checker reachability

For public endpoint checks, inspect:

- Public DNS/IP.
- Route and listener.
- SG/NACL/firewall/WAF allowance for health checker sources.
- Correct host header/path/port.
- TLS certificate/hostname.
- Application response and timeout.

A blocked health checker can cause healthy application traffic to be removed from DNS.

### Health behavior when all records fail

Route 53 generally avoids returning no DNS answer solely because every record is unhealthy; policy fallback can treat records as eligible.

Meaning:

- Health checks improve selection.
- They do not guarantee no traffic reaches an unhealthy endpoint.
- Application/load-balancer resilience is still required.

### Health-check failure map

| Symptom | First checks |
|---|---|
| Endpoint healthy to users, unhealthy to Route 53 | Checker reachability, SG/WAF, path, host header, TLS |
| Health check green but app broken | Check too shallow/wrong dependency/path |
| Private endpoint never healthy | Use CloudWatch alarm or supported target health |
| Failover delayed | Health interval/threshold + TTL/cache + client retry |
| Alias not failing over | `EvaluateTargetHealth`, target-group health, record policy |
| All records still returned | All-unhealthy fallback behavior |

## Policy combinations and nested logic

Route 53 can build more complex routing by using supported alias/Traffic Flow patterns, but exam answers usually ask for the simplest direct policy.

Examples:

- Latency across Regions, weighted deployment inside each Region.
- Geolocation first, failover inside each geography.
- Weighted primary migration with health checks.

Do not choose complex nested policy when one named policy satisfies the requirement.

## TTL and traffic behavior

### What TTL controls

- Recursive/client cache lifetime.
- How quickly a record change can be observed.
- DNS query volume.

TTL does not control:

- Existing TCP sessions.
- Application connection pools.
- Health-check interval.
- Load-balancer target selection.
- Browser/application DNS caching beyond standards-compliant behavior.

### Planned migration

```text
Lower TTL before change
  -> wait old TTL window
  -> change weight/record/target
  -> observe
  -> restore normal TTL after stability.
```

Lowering TTL at the moment of change is too late for resolvers holding the old high TTL.

### DNS distribution is approximate

Reasons:

- Recursive resolver caches one answer for many users.
- Client selects among returned IPs.
- Application keeps connections open.
- EDNS client-subnet support varies.
- Health removes records dynamically.

Do not expect a 90/10 weighted record to equal exactly 90/10 application requests.

## Query logging

### Two different log types

| Log | Sees |
|---|---|
| Route 53 public DNS query log | Queries reaching authoritative servers for a public hosted zone |
| Route 53 Resolver query log | DNS queries handled in associated VPC Resolver context |

They answer different questions.

### Public DNS query logging

Purpose:

- Record queries Route 53 authoritative servers receive for a public hosted zone.

Destination:

- CloudWatch Logs.

Important configuration:

- Correct public hosted-zone ID.
- CloudWatch Logs log group in the required `us-east-1` configuration context.
- CloudWatch Logs resource policy permits Route 53 log delivery.
- Query-logging configuration exists.

### Public query-log meaning

Can include:

- Query name.
- Query type.
- Response code.
- Edge location.
- Resolver source IP and protocol.
- Timestamp.

It logs queries that reach Route 53 authoritative infrastructure.

If a recursive resolver answers from cache, Route 53 authoritative servers receive no new query and create no new public-zone query-log event.

### Public query-log uses

- Find queried names/types.
- Investigate `NXDOMAIN` volume.
- Detect unexpected subdomain scans.
- Verify migration/deprecation traffic.
- Compare query geography/volume.

It does not identify every final end user behind a recursive resolver.

### Resolver query logging

Purpose:

- Record DNS queries made through Route 53 Resolver for associated VPCs.

Supported destination patterns include:

- CloudWatch Logs.
- S3.
- Firehose.

Objects:

- Resolver query logging configuration.
- Destination.
- VPC association.
- Optional RAM sharing for central management.

### Resolver query-log fields

Can provide:

- VPC/account/Region.
- Source IP and resource/instance context where available.
- Query name and type.
- Response code and response data.
- Resolver endpoint/rule context where available.
- DNS Firewall rule/action context where available.
- Timestamp.

Use it to see what workloads asked, not merely what a public zone received.

### Resolver query-log scope

Can capture supported queries such as:

- Public names resolved from VPC workloads.
- Private hosted-zone names.
- VPC-specific names.
- Queries forwarded through outbound rules.
- Queries entering through inbound endpoint where supported by association context.

Actual record contents depend on query path and service behavior.

### Central query logging

```text
Central account owns query-log configuration
  -> shares through RAM where supported
  -> member VPCs associate
  -> logs delivered to central destination
```

Check each VPC association. Creating or sharing the configuration does not attach it automatically.

### Query-log destination security

Check:

- Destination resource policy.
- Delivery-service principal.
- KMS key policy when customer managed encryption is used.
- Log-group/bucket/stream Region and naming requirements.
- Retention and lifecycle.
- Sensitive DNS metadata access.

DNS logs can reveal internal systems, users, and security tooling.

### Public logs versus Resolver logs example

VPC workload queries `api.example.com` five times.

```text
Resolver query log: can show workload queries
Public query log: only shows queries forwarded to authoritative Route 53;
                  resolver cache may reduce this count
```

Do not compare the two log counts as if they measure the same layer.

### CloudTrail distinction

CloudTrail records configuration/API changes such as:

- Record change.
- Hosted-zone/query-log configuration.
- Health-check change.
- Resolver query-log association change.

CloudTrail is not the log of every DNS query.

## Routing-policy troubleshooting

### Decision ladder

```text
1. Exact hosted zone, record name, and type?
2. Correct policy and policy-specific property?
3. Duplicate records have unique set identifiers?
4. Record eligible by weight/location/CIDR/role?
5. Health check or target health correct?
6. Alias target and EvaluateTargetHealth correct?
7. TTL/cache serving an old answer?
8. Query source resolver/location/CIDR as expected?
9. Public/private namespace selected as expected?
10. Log at correct layer: authoritative or Resolver?
```

### Failure map

| Symptom | First checks |
|---|---|
| Weighted traffic ratio looks wrong | TTL, resolver aggregation, sample size, connection reuse, weights |
| Latency sends user to unexpected Region | Resolver location/EDNS, Route 53 latency data, endpoint health |
| Geolocation user gets no answer | Missing default record or unmatched location |
| Failover does not happen | Health association, checker path, TTL/cache, primary still healthy |
| Failover happens incorrectly | Health check blocked/shallow/wrong host/path |
| Multivalue includes bad address | Health check absent/wrong or cache still holds answer |
| IP-based chooses wrong endpoint | Resolver/client source CIDR, collection mapping, EDNS behavior |
| Alias target stays eligible | `EvaluateTargetHealth` disabled/unsupported or target health differs |
| Record changed but old answer remains | Recursive/client TTL cache |

## Query-log troubleshooting

### Missing public query logs

Check:

- Public hosted-zone logging is configured.
- Correct hosted-zone ID.
- CloudWatch Logs group is in required Region/context.
- Logs resource policy allows Route 53.
- Query reached authoritative Route 53 rather than resolver cache/other DNS provider.
- Record/domain delegation points to that hosted zone.

### Missing Resolver query logs

Check:

- Query-log configuration status.
- Source VPC association.
- Correct destination.
- Destination policy and KMS permissions.
- Query actually used Route 53 Resolver.
- Custom DNS server or direct external DNS bypassed Resolver.
- Central RAM share accepted/associated.

### Log-evidence map

| Need to prove | Log |
|---|---|
| Internet resolver asked public zone | Public DNS query log |
| EC2 workload queried a name | Resolver query log |
| DNS Firewall allowed/blocked a VPC query | Resolver query log/firewall fields |
| Administrator changed a record | CloudTrail |
| Client used old cached answer | Client/resolver test plus TTL; may be absent from authoritative log |

### Safe routing change

```text
Create/verify new endpoint
  -> add health check
  -> lower TTL early
  -> introduce record with low weight or inactive failover role
  -> observe query and application evidence
  -> shift weight/role gradually
  -> restore normal TTL
  -> retain old endpoint for rollback window.
```

DNS success must be paired with application metrics and logs.

### Safe query-logging rollout

```text
Create secured destination
  -> add delivery resource policy/KMS permission
  -> create query-log configuration
  -> associate one test zone/VPC
  -> generate known query
  -> validate fields and access
  -> expand coverage
  -> set retention/lifecycle/alarms.
```

### Governance

- Standardize record ownership and change approval.
- Use health checks that reflect business availability.
- Track record and health-check changes with CloudTrail.
- Centralize query logs where appropriate.
- Encrypt/restrict logs and set retention.
- Monitor `NXDOMAIN`, failure, and unusual query trends.
- Document policy intent: weight, geography, failover, or CIDR.
- Review stale records, unused health checks, and zero-weight endpoints.

### Exam traps

- Simple multiple values are not ELB.
- Weighted policy controls DNS-answer probability, not exact request percentage.
- Weight `0` is not a universal “return no records,” especially if every eligible weight is zero.
- Latency routing uses measured latency, not fixed geography.
- Geolocation needs a default record for unmatched users.
- Geoproximity bias moves geographic boundaries; it is not a weight.
- Multivalue returns up to eight healthy values and is not a load balancer.
- IP-based routing depends on DNS query source/CIDR information, not authenticated user identity.
- Failover speed includes health detection plus TTL/cache.
- Public health checkers cannot directly reach private-only endpoints.
- `EvaluateTargetHealth` and a separate health check are different mechanisms.
- When all endpoints are unhealthy, Route 53 can fail open rather than return nothing.
- Public query logs record authoritative queries, not every client lookup.
- Resolver query logs record VPC Resolver activity, not public authoritative traffic only.
- CloudTrail records DNS configuration changes, not every DNS query.
- Query-log configuration/share without zone/VPC association provides no coverage.

### Do not memorize

- Exact health-check interval prices.
- Every routing-policy API field syntax.
- Every CloudWatch Logs resource-policy statement.
- Complete query-log schemas.
- Exact EDNS client-subnet implementation details.
- Every policy fallback edge case.
- Console click paths.

### Ready when

Given a Route 53 routing/logging scenario, you can:

1. Choose simple, weighted, latency, failover, geolocation, geoproximity, multivalue, or IP-based routing.
2. Configure set identifier, weight, Region, role, geography, CIDR, and health properties.
3. Explain TTL, resolver caching, approximate traffic distribution, and fail-open health behavior.
4. Choose endpoint, calculated, alarm-based, or alias-target health.
5. Distinguish public authoritative query logging from Resolver query logging.
6. Diagnose policy eligibility, health, source location/CIDR, TTL, association, and log-delivery failures.
7. Shift traffic safely and prove application—not only DNS—health.

---

## Skill 5.2.3 — Configure content and service distribution

### Official goal

Configure CloudFront and Global Accelerator to distribute content and services globally.

### What the exam tests

- Choose CloudFront, Global Accelerator, or Route 53.
- Configure CloudFront distributions, origins, and behaviors.
- Separate cache-key data from origin-only forwarded data.
- Secure S3 and custom origins.
- Configure viewer and origin TLS independently.
- Configure Global Accelerator listeners, endpoint groups, weights, dials, and health.
- Diagnose DNS, certificate, behavior, origin, endpoint, and health failures.

### Dimensions

**Primary:** selection, configuration, behavior, optimization  
**Support:** diagnosis, governance  
**Precision:** L3 — CloudFront origin/behavior/policies/OAC/certificate and Global Accelerator listener/group/dial/weight/health objects matter.

### Fast selector

| Requirement | Service |
|---|---|
| Cache HTTP/HTTPS content at edge | CloudFront |
| Edge web security, signed content, header manipulation | CloudFront |
| Accelerate non-cacheable TCP/UDP | Global Accelerator |
| Stable global anycast IPs | Global Accelerator |
| Rapid connection routing around unhealthy Regions | Global Accelerator |
| Policy-based DNS answer | Route 53 |
| Regional request/connection balancing | ALB/NLB |

### Core distinction

```text
CloudFront         = HTTP edge proxy + cache
Global Accelerator = TCP/UDP global network router/proxy
Route 53           = DNS answer selection
```

Global Accelerator does not cache. Route 53 does not proxy the connection.

## CloudFront

### Request path

```text
Viewer
  -> nearest CloudFront edge
  -> matching cache behavior
  -> cache hit: return object
  -> cache miss: request origin
  -> cache/store according to policy
  -> return response
```

CloudFront can reduce latency, origin load, and origin data transfer when caching works.

### CloudFront object model

```text
Distribution
  -> domain names/certificate/security/WAF/logging
  -> origins and origin groups
  -> ordered cache behaviors
      -> cache policy
      -> origin request policy
      -> response headers policy
      -> viewer/origin controls
```

### Distribution properties

Know:

- Distribution domain name.
- Alternate domain names/CNAMEs.
- Viewer certificate.
- Default root object.
- Price Class recognition.
- IPv6 enablement.
- Web ACL association.
- Geo restriction.
- Logging.
- Enabled/deployed state.
- Origins and behaviors.

Configuration changes propagate to edge locations; they are not always instantaneous.

### Origin types

Common origins:

- S3 bucket REST endpoint.
- S3 static website endpoint.
- Application Load Balancer.
- API Gateway/API endpoint.
- EC2 or other HTTP server.
- Custom HTTP/HTTPS origin.
- Another supported AWS origin.

Origin type changes security and TLS behavior.

### S3 REST origin versus website origin

**S3 REST origin**

- Can use Origin Access Control.
- Can keep bucket private.
- Supports signed CloudFront-to-S3 requests.
- Best general private-content pattern.

**S3 website endpoint**

- Treated as custom origin.
- Provides S3 website behaviors such as index/error redirects.
- Cannot use OAC like a normal S3 REST origin.
- Website endpoint does not provide HTTPS from CloudFront to S3.
- Usually requires publicly readable website content unless another design is used.

Exam clue: private S3 content → REST origin + OAC, not website endpoint.

### Origin Access Control

OAC lets CloudFront sign requests to an S3 REST origin.

Need:

```text
CloudFront distribution with OAC
  + S3 bucket policy permits CloudFront service principal
  + condition limits distribution ARN
  + Block Public Access can remain enabled
  + KMS key policy if objects use customer managed SSE-KMS
```

OAI is the older pattern. Prefer OAC for supported new designs.

### OAC failure map

| Symptom | First checks |
|---|---|
| CloudFront `403` from S3 | OAC attached, bucket policy, object key, distribution ARN |
| SSE-KMS object denied | KMS key policy for CloudFront/S3 path |
| Direct S3 URL still works publicly | Bucket policy/public access, origin not actually private |
| OAC option unavailable | Origin configured as website/custom instead of S3 REST |
| Some objects fail | Object ownership, key path/case, KMS key, bucket policy scope |

### Custom origin access

To prevent direct origin bypass:

- Restrict origin security group to CloudFront origin-facing ranges/prefix list where supported.
- Use secret custom origin header checked by origin/application where appropriate.
- Use private-origin connectivity features where supported.
- Keep WAF at CloudFront and close alternate public domains/IP paths.

A CloudFront distribution plus a publicly open origin can be bypassed.

### Origin object properties

- Origin domain name.
- Origin ID.
- Origin path.
- Origin protocol policy.
- HTTP/HTTPS port.
- Origin SSL protocols.
- Custom headers.
- Connection attempts/timeouts.
- OAC for supported S3 origin.
- Origin Shield setting.

Origin domain name must resolve and its certificate must match when HTTPS is used.

### Origin groups

Origin group contains:

- Primary origin.
- Secondary origin.
- Failover status-code criteria.

```text
Primary origin returns configured failure
  -> CloudFront tries secondary origin
```

Use for origin failover, not weighted load distribution.

Both origins must contain compatible content/application behavior.

### Cache behavior model

```text
Path pattern
  -> origin
  -> viewer protocol policy
  -> allowed/cached methods
  -> cache policy
  -> origin request policy
  -> response headers policy
  -> edge function associations
```

Every request matches one behavior.

### Behavior matching

- Ordered behaviors are checked by path-pattern order.
- First matching ordered behavior wins.
- Default behavior `*` catches everything else.
- Path matching is case-sensitive.
- More-specific intent must appear before broader matching behavior.

Wrong order can bypass intended authentication, signed URL, cache, or origin configuration.

### Behavior example

```text
/api/*     -> API origin, no/minimal cache, all required methods
/static/*  -> S3 origin, long cache
default *  -> web origin
```

Request `/api/orders` must match `/api/*` before a broader path behavior.

### Viewer protocol policy

Choices:

- Allow HTTP and HTTPS.
- Redirect HTTP to HTTPS.
- HTTPS only.

Redirect sends an HTTP response to the initial plaintext request. HTTPS only rejects HTTP.

Do not confuse viewer protocol policy with origin protocol policy.

### Allowed and cached methods

Common cached methods:

- `GET`.
- `HEAD`.
- Optional `OPTIONS`.

CloudFront can forward additional methods such as:

- `POST`.
- `PUT`.
- `PATCH`.
- `DELETE`.

Only cache methods safe/supported for the application. An API behavior needs its required allowed methods.

### Cache key

Cache key can include:

- Path.
- Selected query strings.
- Selected headers.
- Selected cookies.
- Compression variant behavior.

Same cache key means viewers can receive the same cached response.

Do not exclude a value that changes the response, such as language, tenant, or authorization-dependent content.

### Cache policy

Controls:

- What enters the cache key.
- Minimum/default/maximum TTL behavior.
- Which selected cache-key values are also forwarded.
- Compression cache variants.

Smaller cache key usually gives more hits—but can return incorrect shared content if a response-varying value is omitted.

### Origin request policy

Controls extra request values forwarded to origin **without adding them to the cache key**.

Examples:

- Header needed for origin logging.
- Header/query/cookie needed by origin but not by response variation.

Key distinction:

```text
Cache policy         = affects cache identity
Origin request policy = extra data sent only to origin
```

Forwarding a response-varying value only in origin request policy can cause cache pollution/wrong viewer response.

### Response headers policy

Can add/manage viewer response headers such as:

- CORS headers.
- Security headers.
- Custom headers.
- Header removal behavior.

It changes viewer response headers. It does not change the cached object identity unless another policy does.

### TTL sources

Caching can depend on:

- Origin `Cache-Control`.
- Origin `Expires`.
- Cache-policy minimum/default/maximum TTL.
- Error-caching settings.

CloudFront policy can constrain or override origin TTL behavior.

Detailed cache troubleshooting appears in 5.3.3.

### Compression

- Enable supported automatic compression.
- Viewer must advertise support.
- Cache compressed variants correctly.
- Best for text-like content.

Compression reduces bytes, not request count.

### Origin Shield

Adds a selected Regional cache layer between edge caches and origin.

Can:

- Reduce duplicate origin requests.
- Improve cache efficiency for globally requested objects.
- Protect a sensitive/limited origin.

It adds feature/request cost and another cache layer. Use when origin reduction justifies it.

### Viewer certificate

For an alternate domain such as `cdn.example.com`:

- Add alternate domain name to distribution.
- Certificate SAN must cover the name.
- ACM viewer certificate must be in `us-east-1`.
- DNS alias/CNAME must point to distribution.
- Viewer TLS security policy must support clients.

Certificate, alternate domain, and DNS must agree.

### Origin TLS

Origin protocol policy controls CloudFront-to-origin connection:

- HTTP only.
- HTTPS only.
- Match viewer where supported.

For HTTPS origin:

- Origin DNS name must match certificate SAN.
- Chain must be trusted/complete.
- Origin listener/port/security policy must support CloudFront.
- SG/firewall must allow CloudFront origin traffic.

Viewer HTTPS can work while origin HTTPS fails.

### WAF, Shield, and geo restriction

- Associate WAF web ACL for HTTP request filtering.
- Shield provides DDoS protection; Advanced adds configured capabilities.
- CloudFront geo restriction can allow or block countries.

Geo restriction is broad country access control. It is not application authorization and can be affected by VPN/proxy locations.

### Private content

Recognize:

- Signed URL: access to selected object/resource URL.
- Signed cookie: access to multiple protected objects without changing every URL.
- Trusted key group/public keys.
- Policy expiration and optional IP/time restrictions.

Viewer private-content authorization is separate from CloudFront access to the origin through OAC.

### Edge compute recognition

**CloudFront Functions**

- Lightweight, high-scale viewer-request/response manipulation.
- Good for URL/header redirects and simple logic.

**Lambda@Edge**

- More capable edge logic at viewer and origin event points.
- Heavier runtime/deployment model.

Choose the smallest feature that meets the logic requirement. Do not memorize every runtime limit.

### Logging

Recognize:

- Standard access logs.
- Real-time logs where required.
- CloudWatch metrics.
- WAF logs separately.
- CloudTrail for distribution configuration changes.

Useful fields:

- Viewer IP/method/URI/status.
- Edge location.
- Cache/result type.
- Bytes and timing.
- Host and user agent.

Logs can contain sensitive URLs/cookies. Restrict and lifecycle them.

### CloudFront invalidation

Invalidation removes selected cached paths before normal expiry.

- Useful for urgent corrections.
- Has request/cost/propagation considerations.
- Wildcards can invalidate many objects.
- Versioned object names are usually cleaner for normal releases.

Invalidation does not fix an incorrect origin object or cache policy.

### CloudFront failure map

| Symptom | First checks |
|---|---|
| Alternate domain TLS error | DNS, alternate name, ACM `us-east-1`, SAN, deployment |
| S3 origin `403` | OAC/OAI, bucket/KMS policy, key, object path |
| `502` from custom origin | Origin DNS, TLS name/chain/policy, listener/port |
| `504` | Origin reachability, SG/firewall, timeout, slow/unhealthy origin |
| Wrong origin used | Behavior path pattern/order |
| API method rejected | Behavior allowed methods |
| Wrong content shared | Cache key missing header/cookie/query/tenant value |
| Almost no cache hits | Cache key too broad, low TTL, no-cache origin headers |
| Direct origin bypasses WAF | Origin still publicly reachable/alternate path |
| Failover never occurs | Origin group/status criteria/request behavior |
| Config correct but old edge behavior | Distribution deployment/propagation time |

## Global Accelerator

### Request path

```text
Client
  -> static anycast IP
  -> nearest healthy AWS edge
  -> AWS global network
  -> selected Regional endpoint group
  -> selected healthy endpoint
```

It accelerates the network path. It does not store/cache application content.

### Global Accelerator object model

```text
Accelerator
  -> static anycast IPs
  -> listener(s)
      -> endpoint group per Region
          -> traffic dial
          -> health-check settings
          -> endpoint(s) + weights
```

### Accelerator properties

- Enabled/disabled state.
- Static anycast IP addresses.
- IP address type.
- Listener ports and protocols.
- Client affinity recognition.
- Endpoint groups.
- Flow logs where configured.

Static IPs remain the stable client entry while Regional endpoints change behind them.

### Listener

Defines:

- Protocol: TCP or UDP.
- Port or port range.
- Client-affinity behavior where used.

Listener protocol/port must match the application path.

CloudFront is HTTP-oriented; Global Accelerator supports general TCP/UDP workloads.

### Endpoint group

Defines a serving Region and contains:

- Regional endpoints.
- Traffic dial percentage.
- Health-check port/protocol/path/interval/threshold settings.
- Endpoint weights.

Typical endpoints include supported:

- Application Load Balancers.
- Network Load Balancers.
- EC2 instances.
- Elastic IP addresses.

### Traffic dial versus endpoint weight

**Traffic dial**

- Controls how much traffic the **Regional endpoint group** receives relative to normal routing.
- `0%` can drain new traffic from that Region.
- Useful for Regional maintenance or gradual migration.

**Endpoint weight**

- Controls distribution among endpoints **inside one endpoint group**.
- Higher weight receives more of that group’s traffic when healthy.

Memory:

```text
Dial = Region/group share
Weight = endpoint share inside Region
```

### Global Accelerator health

- Health checks run per endpoint-group settings.
- Unhealthy endpoints stop receiving new traffic.
- Accelerator routes toward healthy endpoints/Regions.
- For load balancer endpoints, underlying target health matters.
- Security controls must allow application and health-check traffic.

Health check should test the actual service port/path.

### Global Accelerator versus DNS failover

**Route 53**

- Returns a DNS answer.
- Change/failover affected by TTL and resolver caches.
- Many policy types.

**Global Accelerator**

- Clients keep using static anycast IPs.
- Connection routing can shift without DNS record/TTL change.
- Uses AWS global network.
- Good for rapid endpoint/Regional failover and fixed allowlist IPs.

Existing connections may still need application retry; accelerator does not preserve every failed backend session.

### Client IP behavior

Client source-IP preservation depends on endpoint type/protocol path.

Audit:

- Whether application sees original client IP.
- SG/firewall rules expected source ranges.
- Proxy protocol/header expectations where relevant.
- Logging fields.

Do not assume every accelerated endpoint sees an edge proxy IP or always sees the original IP.

### Global Accelerator logging/evidence

Use:

- Accelerator/listener/group/endpoint configuration.
- Endpoint health status and reason.
- Traffic dial and endpoint weights.
- CloudWatch metrics for new/active flows, bytes, and health.
- Flow logs where enabled.
- Load-balancer/application logs.
- CloudTrail configuration changes.
- Client tests to static IP and listener port.

### Global Accelerator failure map

| Symptom | First checks |
|---|---|
| Static IP unreachable | Accelerator enabled, listener port/protocol, client firewall/routing |
| Region gets no traffic | Endpoint-group traffic dial, health, listener mapping |
| One endpoint gets no traffic | Endpoint health and weight |
| All endpoints unhealthy | Health-check port/path, SG/NACL, target/listener health |
| TCP works, UDP fails | Listener protocol/port and network security |
| Failover slower than expected | Health settings, application retry, existing sessions |
| Client allowlist breaks | Correct static accelerator IPs/IP type |
| Application logs wrong source | Endpoint-type client-IP behavior/proxy handling |

## Cross-service selection

### CloudFront versus Global Accelerator

| Property | CloudFront | Global Accelerator |
|---|---|---|
| Main protocol | HTTP/HTTPS | TCP/UDP |
| Cache | Yes | No |
| Entry | Distribution DNS name | Static anycast IPs + DNS name |
| Main benefit | Cache, web delivery, edge HTTP controls | Network-path acceleration and rapid endpoint routing |
| Security | WAF, signed content, edge headers/functions | Stable ingress and DDoS-protected global path |
| Origin/endpoint | HTTP origin | Supported Regional network endpoints |

### CloudFront versus Route 53

**CloudFront**

- Proxies web request at edge.
- Can cache and apply WAF/functions.
- Hides/protects origin when configured.

**Route 53**

- Returns target DNS record.
- Supports weight, latency, geography, health, and CIDR policies.
- Client connects directly to returned target.

Use both when Route 53 alias maps a custom domain to CloudFront.

### Global Accelerator versus ALB/NLB

- Global Accelerator supplies global entry/routing.
- ALB/NLB supplies Regional balancing.
- Accelerator endpoint can be a load balancer.

Common stack:

```text
Client -> Global Accelerator -> Regional ALB/NLB -> targets
```

One does not replace the other’s layer.

## Troubleshooting workflow

### CloudFront ladder

```text
1. Viewer DNS points to correct distribution?
2. Alternate domain and certificate deployed?
3. Viewer protocol/TLS/WAF permits request?
4. Which behavior matches path first?
5. Correct origin, methods, and policies?
6. Cache hit/miss/stale/error behavior?
7. Origin DNS/route/SG/listener reachable?
8. Origin TLS hostname/chain/policy correct?
9. Origin authorization: OAC/bucket/KMS/custom header?
10. Origin application returned expected object/status?
```

### Global Accelerator ladder

```text
1. Client uses correct static IP/DNS and protocol/port?
2. Accelerator/listener enabled?
3. Endpoint group exists in intended Region?
4. Traffic dial above zero?
5. Endpoint weight above zero?
6. Endpoint healthy?
7. Health-check path/port/security correct?
8. Endpoint LB/instance listener and targets healthy?
9. SG/NACL/firewall permits client/accelerator path?
10. Application logs/metrics show connection?
```

### Evidence selector

| Question | Evidence |
|---|---|
| Which CloudFront behavior matched? | Path/order/config plus access-log behavior fields |
| Cache or origin response? | Cache/result fields, `Age`, origin logs |
| Why S3 denied? | OAC/bucket/KMS policy and CloudTrail/S3 evidence |
| Why custom origin failed? | CloudFront status, origin logs, SG/TLS test |
| Why GA skipped Region? | Traffic dial and endpoint-group health |
| Why GA skipped endpoint? | Endpoint weight and health |
| Who changed distribution/accelerator? | CloudTrail |

### Safe CloudFront rollout

```text
Create origin and narrow access
  -> create/test distribution domain
  -> add behavior/policies
  -> validate cache and private content
  -> attach certificate/alternate domain
  -> switch Route 53 alias with planned TTL
  -> monitor edge and origin errors
  -> close direct origin path
  -> retain rollback distribution/origin.
```

### Safe Global Accelerator rollout

```text
Create accelerator/listener
  -> add endpoint groups with low/controlled dial
  -> verify health
  -> test static IPs and protocols
  -> increase traffic dial/weights
  -> monitor flows/application
  -> drain old Region/endpoint
  -> keep rollback through dial/weight.
```

### Governance

- Tag distributions, accelerators, origins, and endpoint groups.
- Restrict CloudFront origin access.
- Use certificates and HTTPS policies deliberately.
- Associate WAF and logging where required.
- Protect signed-content keys.
- Encrypt/restrict/lifecycle access logs.
- Document behavior path ownership and cache-key data sensitivity.
- Monitor direct-origin exposure.
- Record accelerator dial/weight changes.

### Exam traps

- CloudFront caches HTTP/HTTPS; Global Accelerator does not cache.
- Route 53 returns DNS; it does not proxy content.
- First matching CloudFront ordered behavior wins; default catches the rest.
- Cache policy defines cache key; origin request policy forwards extra data without changing cache key.
- Missing response-varying value from cache key can leak/wrongly share content.
- Viewer TLS and origin TLS are separate.
- CloudFront viewer ACM certificate belongs in `us-east-1`.
- Alternate domain, certificate SAN, and DNS must all match.
- Private S3 origin uses REST endpoint + OAC; website endpoint cannot use OAC.
- OAC bucket permission and SSE-KMS key permission are separate.
- Origin group is failover, not weighted balancing.
- WAF association does not protect a directly reachable origin.
- Signed viewer URL/cookie is different from OAC origin authorization.
- Global Accelerator traffic dial controls Region/group; endpoint weight controls endpoint inside group.
- Global Accelerator static IPs avoid DNS TTL changes during endpoint shift.
- Global Accelerator accelerates TCP/UDP but does not reduce origin requests through caching.
- CloudFront/GA health does not fix an unhealthy application.

### Do not memorize

- Every CloudFront edge location.
- Exact CloudFront cache limits/prices.
- Every origin timeout limit.
- Every managed cache-policy ID.
- Every Global Accelerator metric.
- Exact health-check interval values.
- Edge runtime quotas.
- Console click paths.

### Ready when

Given a distribution scenario, you can:

1. Choose CloudFront, Global Accelerator, Route 53, or a Regional load balancer.
2. Configure CloudFront origins, ordered behaviors, methods, and three policy types.
3. Secure S3 with REST origin + OAC + bucket/KMS policy.
4. Configure alternate domains, `us-east-1` certificate, viewer TLS, and origin TLS.
5. Configure Global Accelerator listener, endpoint groups, traffic dials, weights, and health checks.
6. Diagnose CloudFront behavior/cache/origin/TLS/access and accelerator dial/weight/health failures.
7. Prove the correct edge, origin, Region, and endpoint path from logs and metrics.

---

## Skill 5.3.1 — Troubleshoot VPC configurations

### Official goal

Troubleshoot subnets, route tables, NACLs, security groups, Transit Gateways, NAT gateways, and related VPC paths.

### What the exam tests

- Build the real packet path from evidence.
- Prove forward and return routing.
- Apply longest-prefix routing.
- Distinguish SG and NACL failures.
- Diagnose NAT, peering, TGW, VPN, endpoint, IPv6, and appliance paths.
- Recognize IP exhaustion.
- Interpret Reachability Analyzer correctly.
- Make the smallest safe remediation.

### Dimensions

**Primary:** evidence, diagnosis, remediation, behavior  
**Support:** configuration  
**Precision:** L3 — exact source/destination, route association/target, SG/NACL semantics, attachment state, and analyzer explanation matter.

### Core rule

```text
Never ask only: “Is there a route?”
Ask: “Which route wins in each direction for this exact packet?”
```

### End-to-end model

```text
DNS answer
  -> source process/ENI/IP
  -> source security group
  -> source subnet NACL
  -> source subnet route table
  -> NAT/TGW/peering/VPN/endpoint/firewall/IGW
  -> destination route/NACL
  -> destination ENI security group
  -> OS firewall
  -> listening application
  -> complete return path
```

Every layer can succeed while the next layer fails.

### Start with the exact flow

Write five values:

```text
Source IP
Destination IP
Protocol
Source port
Destination port
```

Also record:

- Source/destination VPC, subnet, AZ, account, and Region.
- DNS name and resolved address family.
- Direction of connection initiation.
- Time of failure.
- Whether a NAT/proxy/load balancer changes addresses.

Wrong assumed source IP causes wrong SG, NACL, firewall, and route diagnosis.

### Symptom first

| Symptom | First meaning |
|---|---|
| DNS error | Resolve DNS layer before packet routing |
| Timeout | Drop, missing route/return path, firewall, or silent application |
| Connection refused | Destination reached; no listener or active reject |
| TLS error | TCP path works; inspect certificate/protocol/hostname |
| HTTP `403` | Application/WAF/IAM/resource policy, not basic route failure |
| Works from one subnet/AZ | Compare route-table/NACL/attachment/AZ objects |
| Intermittent under load | Capacity, ephemeral ports, NAT ports, target health, asymmetric path |

Do not change a route for a proven TLS hostname error.

## Route diagnosis

### Route-table facts

- Subnet uses one associated route table.
- Implicitly associated subnet uses the main route table.
- Route = destination + target.
- Longest prefix wins.
- `active` means route target is available to route-table control plane.
- `blackhole` means unusable target/path.

Always inspect the exact subnet association.

### Longest-prefix example

```text
0.0.0.0/0      -> NAT gateway
10.20.0.0/16   -> Transit Gateway
10.20.5.0/24   -> peering connection
```

Destination `10.20.5.10` uses peering, not NAT or TGW.

A newly added more-specific route can silently redirect only part of traffic.

### Forward and return route

Forward success:

```text
A subnet -> B CIDR -> target
```

Return also needs:

```text
B subnet/network -> A CIDR -> correct reverse target
```

Stateful SG does not create a missing network return route.

### Route evidence checklist

- Source subnet association.
- Destination prefix that wins.
- Route state.
- Target ID and state.
- Target attachment/acceptance.
- Destination-side route.
- Return-side longest-prefix route.
- Propagated versus static route where relevant.
- IPv4 and IPv6 tables/rules separately.
- Appliance routing and source/destination check.

### Route failure map

| Evidence | Likely cause |
|---|---|
| `blackhole` route | Deleted/unavailable peering, NAT, TGW, endpoint, or attachment |
| No matching remote route | Missing route/propagation/association |
| Wrong target used | More-specific route or wrong subnet table |
| Only return packets missing | Reverse route or asymmetric middlebox path |
| One subnet fails | Different route-table association |
| New CIDR unreachable | Route/security only covers old CIDR |
| Peering create fails | Overlapping CIDRs |

## Security group diagnosis

### Security group facts

- Attached to ENI/resource.
- Stateful.
- Allow-only.
- No numeric order.
- Return traffic for allowed connection is automatically allowed.
- Initial packet must match correct inbound/outbound rule.

Inspect every SG attached to the exact ENI; rules are combined.

### SG flow questions

For client initiating to server:

```text
Client SG outbound allows destination port/IP/SG?
Server SG inbound allows actual source IP/SG and service port?
```

No separate SG rule is needed for tracked return packets.

### Actual source trap

Destination may see:

- Original client private IP.
- NAT translated IP/EIP.
- Load balancer node/source behavior.
- Proxy/appliance IP.
- Interface endpoint ENI path.

Use Flow Logs/access logs/service behavior to determine the source the SG must match.

### SG-reference trap

```text
DB SG inbound from App SG
```

Works only when supported SG-reference semantics apply to ENIs in the path.

It does not:

- Copy rules.
- Match by SG name text.
- Automatically cross every peering/Region/transit scenario.
- Permit NACL traffic.

### SG failure map

| Symptom | First checks |
|---|---|
| Client timeout to one port | Server inbound protocol/port/source |
| Server cannot initiate outbound | Server outbound rule for initial packet |
| Response blocked despite no outbound rule | SG is stateful; inspect NACL/route/OS instead |
| Rule allows subnet but source differs | NAT/LB/proxy translation |
| SG reference fails | Wrong SG attached, unsupported path/Region, destination rule |
| IPv6 fails | IPv6 CIDR rule missing; IPv4 rule does not match |

## Network ACL diagnosis

### NACL facts

- Associated with subnet.
- Stateless.
- Separate inbound/outbound rules.
- Allow and deny.
- Lowest rule number first.
- First match wins.
- Final `*` denies unmatched traffic.

Check NACL on every subnet boundary traversed.

### NACL packet model

Client to server:

```text
Server-subnet inbound: allow destination service port
Server-subnet outbound: allow return to client ephemeral port
```

Client-subnet outbound/inbound rules must also allow its side when restrictive.

### Ephemeral-port symptom

If service port is allowed but return ephemeral range is incomplete:

- TCP handshake may fail.
- Small tests may work while other clients fail.
- Large/parallel traffic can look intermittent.
- One operating system can work while another fails.

Use actual client ephemeral range; do not assume one universal narrow range.

### NACL priority example

```text
50  ALLOW 0.0.0.0/0 TCP 443
100 DENY  203.0.113.10/32 TCP 443
```

The deny never runs for TCP 443 because rule 50 matches first.

### NACL failure map

| Symptom | First checks |
|---|---|
| SG looks correct but timeout | NACL both directions and ephemeral ports |
| Specific deny ineffective | Lower-number broad allow shadows it |
| New custom NACL causes outage | Default final deny; missing inbound/outbound allows |
| Only IPv6 fails | Separate IPv6 NACL rules |
| Return path fails | Outbound/inbound ephemeral rule and CIDR |

## Public internet path

### Public IPv4 inbound requirements

```text
IGW attached
  + subnet 0.0.0.0/0 -> IGW
  + instance public IPv4/EIP
  + SG inbound
  + NACL both directions
  + listener/OS firewall
```

Subnet name “public” proves nothing.

### Public IPv4 troubleshooting

| Evidence | Meaning |
|---|---|
| Private IP only | No direct IPv4 internet identity |
| Public IP exists, no IGW route | Address cannot create route |
| IGW route exists, no public IP | Subnet public; instance still private-only |
| Flow Log `REJECT` on ENI | SG/NACL candidate |
| Flow Log `ACCEPT`, timeout | OS/listener/return/external path candidate |
| Works locally on host only | Bind address, OS firewall, SG/NACL |

### IPv6 internet path

Public bidirectional:

```text
IPv6 address + ::/0 -> IGW + IPv6 SG/NACL rules
```

Outbound-initiated only:

```text
IPv6 address + ::/0 -> egress-only IGW + IPv6 SG/NACL rules
```

Do not troubleshoot an `AAAA` result with only IPv4 routes/rules.

## NAT gateway diagnosis

### Complete public NAT path

```text
Private subnet route 0.0.0.0/0 -> NAT
  -> NAT state available
  -> NAT in public subnet
  -> NAT has EIP
  -> NAT subnet route 0.0.0.0/0 -> IGW
  -> IGW attached
  -> return through same translation
```

NAT gateway does not accept unsolicited inbound connections.

### NAT checks

- NAT gateway type/state.
- Subnet and AZ.
- EIP for public NAT.
- Private subnet route target.
- NAT subnet route to IGW.
- IGW attachment.
- NACL on private and NAT subnets.
- DNS resolution.
- Same-AZ versus cross-AZ path.
- Port-allocation/error metrics.
- Destination reachable from internet.

Security groups do not attach to NAT gateways.

### NAT symptom map

| Symptom | First checks |
|---|---|
| Every private host lacks internet | NAT state/EIP/public route/IGW |
| One private subnet fails | Its route-table association/NACL |
| One AZ fails | AZ NAT/path/route/NACL |
| Only one destination fails under load | NAT port allocation, destination limit, connection reuse |
| Inbound connection fails | Expected NAT behavior; use LB/public endpoint |
| S3 works but internet fails | S3 gateway endpoint may work while NAT path is broken |
| Internet works but AWS API times out | DNS, endpoint policy/private DNS, service-specific path |

### NAT port exhaustion

Evidence:

- High connections to same destination tuple.
- Port-allocation error metrics.
- Failures increase with concurrency.
- Routes and NAT status remain valid.

Remediation can include connection reuse, destination spread, or supported NAT address/capacity scaling.

## VPC peering diagnosis

### Required path

```text
Peering status active
  + non-overlapping CIDRs
  + A subnet route to B CIDR -> pcx
  + B subnet route to A CIDR -> pcx
  + SG/NACL allowance
  + DNS options/zone association if using names
```

### Peering traps

- Request not accepted.
- Route added only on one side.
- Wrong route tables/subnets.
- Overlapping secondary CIDR.
- A-B and B-C do not allow A-C.
- Peer cannot be used as transit to its NAT/IGW/VPN.
- Private DNS visibility not automatic.

### Peering symptom map

| Symptom | First checks |
|---|---|
| A to B timeout | Status, A route, B return route, SG/NACL |
| A to B works by IP only | Peering DNS option/PHZ/Resolver |
| A to C through B fails | Expected non-transitivity |
| Only new VPC CIDR fails | Peering route/security missing secondary CIDR |

## Transit Gateway diagnosis

### Required route chain

```text
Source VPC subnet route -> TGW
  -> source attachment
  -> associated TGW route table
  -> destination route/propagation -> destination attachment
  -> destination VPC route/security
  -> symmetric return chain
```

### TGW object checks

- Attachment state.
- VPC attachment subnet/AZ coverage.
- Source attachment route-table association.
- Destination attachment propagation.
- Static/propagated/blackhole TGW route.
- Source and destination VPC routes.
- Return TGW table based on reverse ingress attachment.
- Appliance mode/symmetry where firewalls exist.

Association chooses the lookup table on ingress. Propagation places attachment destinations into a table.

### TGW symptom map

| Symptom | First checks |
|---|---|
| Source packet never enters TGW | Source subnet route/attachment subnet AZ |
| TGW has no destination | Association, propagation, static route |
| One-way flow | Reverse VPC/TGW route-table chain |
| Unexpected VPC reachable | Overbroad propagation/wrong table association |
| One AZ fails | Attachment subnet/AZ route or appliance symmetry |
| TGW route `blackhole` | Deleted attachment or intentional blackhole route |

## VPC endpoint diagnosis

### Gateway endpoint

Check:

- S3/DynamoDB service and Region.
- Endpoint state.
- Source subnet route table associated.
- Managed prefix-list route to endpoint.
- Endpoint policy.
- IAM/resource/KMS policy.

No endpoint SG exists.

### Interface endpoint

Check:

- Endpoint state and service name.
- ENI/subnet/AZ/IP availability.
- Endpoint SG inbound, commonly TCP `443`.
- Client SG/NACL.
- Private DNS and VPC DNS settings.
- Endpoint-specific versus public DNS result.
- Endpoint policy plus IAM/resource/KMS policy.

Local VPC route reaches endpoint ENI; do not expect a gateway-endpoint-style route-table entry.

### Endpoint symptom map

| Symptom | First checks |
|---|---|
| Timeout | DNS to endpoint IP, endpoint SG, NACL, endpoint state |
| Immediate access denied | Endpoint/IAM/resource/KMS policy, not basic route |
| Works through NAT, not endpoint | Private DNS, endpoint policy, SG, service name |
| One AZ fails | Endpoint ENI/subnet/IP exhaustion |
| Gateway endpoint unused | Route-table association and prefix-list route |

## VPN and hybrid edge diagnosis

At VPC level, check:

- VGW/TGW attachment.
- VPC route to on-premises CIDR.
- Propagated/static route presence.
- Return on-premises route.
- Non-overlapping CIDRs.
- SG/NACL source ranges.
- Tunnel/BGP state evidence.

Detailed IKE/BGP/MTU diagnosis appears in 5.3.4.

## Stateful appliance/asymmetric routing

Stateful firewall/NAT expects both directions.

Bad path:

```text
Forward -> appliance AZ-A
Return  -> appliance AZ-B or bypass
```

Symptoms:

- SYN seen, response disappears.
- One AZ works.
- Intermittent connections after scaling/route change.
- Flow Logs show different interfaces/paths.

Check:

- Source and return longest-prefix routes.
- TGW appliance mode where relevant.
- NAT ordering.
- Appliance source/destination check disabled where required.
- Endpoint/AZ symmetry.

## IP exhaustion

### What consumes subnet IPs

- EC2 ENIs.
- ECS/EKS tasks/pods using VPC addresses.
- Load balancer nodes.
- Interface endpoints.
- RDS/managed-service ENIs.
- NAT/firewall/TGW attachment interfaces.
- Blue/green or rolling deployment surge.

### Symptoms

- New instance/task/pod does not launch.
- Load balancer cannot scale/add node.
- Endpoint or managed service creation fails.
- One AZ fails while others launch.
- Existing traffic works; new capacity fails.

### Evidence

- Subnet available IPv4 count.
- ENI inventory and owners/descriptions.
- Auto Scaling/deployment desired versus running.
- Service event message.
- One-AZ comparison.
- IPAM utilization.

### Remediation

- Remove genuinely stale ENIs through owning service/process.
- Add larger/new subnets from available VPC CIDR.
- Add secondary VPC CIDR and new subnets.
- Spread workloads across AZ/subnets.
- Adjust deployment surge only if availability permits.

Existing subnet CIDR cannot simply expand in place.

## VPC Reachability Analyzer

### Purpose

Analyzes AWS network configuration between a selected source and destination.

Input can include:

- Source resource/interface.
- Destination resource/interface/IP where supported.
- Protocol.
- Destination port.

Output:

- Reachable path with components.
- Not reachable with blocking/explanation component.

### What it analyzes

Can reason about supported:

- Routes.
- Security groups.
- Network ACLs.
- Gateways/attachments/endpoints.
- Load balancer/network components where supported.

It helps identify a configuration blocker without manually opening every object.

### What it does not prove

- It does not send real packets.
- It does not prove application is listening.
- It does not prove OS firewall permits traffic.
- It does not measure latency or packet loss.
- It cannot fully validate unsupported/external on-premises network behavior.
- A reachable result is a configuration model, not an end-to-end application success test.

### Reachability Analyzer interpretation

**Not reachable**

- Read the exact blocking component and direction.
- Confirm analysis source/destination/protocol/port are correct.
- Fix narrow control, then rerun.

**Reachable**

- AWS modeled path exists.
- Next inspect DNS choice, OS firewall, listener, TLS, application, and real traffic evidence.

Do not widen all SG/NACL rules merely because analysis reports one blocker.

## Evidence tools

### VPC Flow Logs

Useful fields:

- Interface ID.
- Source/destination address.
- Source/destination port.
- Protocol.
- Packets/bytes.
- `ACCEPT`/`REJECT`.
- Start/end time.
- Log status.

`REJECT` points to captured network-control denial. `ACCEPT` does not prove a response or application success.

Detailed log interpretation appears in 5.3.2.

### CloudWatch metrics

Use for:

- NAT connections/bytes/errors/port allocation.
- VPN tunnel state/data.
- TGW/attachment traffic/drop signals.
- Load-balancer target health/errors.
- Endpoint/appliance metrics where exposed.

Correlate metric time with failed flow and configuration change.

### CloudTrail and Config

Use to find:

- Route creation/replacement/deletion.
- SG/NACL rule change.
- Endpoint/peering/TGW attachment change.
- NAT deletion.
- ENI/network setting change.
- Actor, time, request parameters, and error.

Config/resource timelines help compare before and after.

### Real packet/application tests

From the failing source:

- Resolve DNS.
- Test TCP/UDP port appropriately.
- Test TLS hostname/chain.
- Send application request.
- Check destination listener and logs.

Use the same address family and path as production.

## Scenario playbooks

### Same-VPC timeout

```text
DNS/IP
  -> local route
  -> source SG outbound
  -> destination SG inbound
  -> both subnet NACL directions
  -> OS listener/firewall
  -> return path
```

No IGW or NAT is required for private addresses in the same VPC.

### Public EC2 unreachable

```text
Public IPv4/EIP?
  -> subnet route to attached IGW?
  -> SG inbound actual source/port?
  -> NACL inbound service + outbound ephemeral?
  -> process bound to correct interface/port?
```

### Private EC2 cannot update packages

```text
DNS works?
  -> private route to NAT?
  -> NAT available/public subnet/EIP?
  -> NAT subnet route to IGW?
  -> SG/NACL return path?
  -> destination/repository reachable?
```

If only S3/DynamoDB is needed, a gateway endpoint may be better than fixing a general NAT path.

### Load balancer target unhealthy

```text
LB listener/target group
  -> target registered in enabled AZ?
  -> health-check protocol/port/path?
  -> target SG allows LB source?
  -> NACL return ephemeral path?
  -> application listens and returns success?
```

Do not open target SG to the internet when only the load balancer should connect.

### One-AZ failure

Compare AZs:

- Subnet free IPs.
- Route-table association.
- NACL association.
- NAT/endpoints/firewall/TGW attachment.
- Load-balancer targets.
- DNS/zonal endpoint answer.

One-AZ symptoms strongly suggest a zonal object difference.

## Minimal-remediation model

```text
Prove failed object
  -> capture current config
  -> change narrow route/rule/association
  -> rerun analyzer/flow test
  -> test application
  -> monitor both directions
  -> remove temporary broad rule
  -> document root cause.
```

Temporary `0.0.0.0/0 all traffic` is weak evidence and creates risk.

### Troubleshooting order

```text
1. DNS and selected IP family.
2. Exact five-tuple and source identity.
3. Source ENI/subnet/AZ.
4. Source route using longest prefix.
5. Intermediate state/attachment/association.
6. Destination and return routes.
7. SG initial direction.
8. NACL both directions/ephemeral ports.
9. Reachability Analyzer and Flow Logs.
10. OS firewall/listener/TLS/application.
11. Capacity/IP/port exhaustion under load.
```

### Exam traps

- Forward route without return route is incomplete.
- Longest-prefix route wins, not the default route or newest route.
- Subnet can use the main route table without explicit association.
- `active` route does not prove destination/application health.
- `blackhole` identifies an unusable target path.
- SG is stateful and allow-only; return traffic is automatic.
- NACL is stateless, ordered, and needs explicit return/ephemeral rules.
- Lowest-number NACL rule wins; later deny/allow may never run.
- SG source must match the address actually seen after NAT/LB/proxy behavior.
- Public subnet route and public instance address are both required for direct IPv4 internet.
- NAT gateway needs private route + public subnet + EIP + IGW route; it accepts no unsolicited inbound.
- Security groups cannot attach to NAT gateway.
- Peering is non-transitive and requires two-sided routes.
- TGW association and propagation are different; VPC and TGW route tables both matter.
- Interface endpoint timeout is network; `AccessDenied` is policy/KMS.
- Existing traffic can work while subnet IP exhaustion blocks only new resources.
- Reachability Analyzer does not send packets or test application listener.
- Flow Log `ACCEPT` does not prove application response.
- Asymmetric path can break stateful firewall even when both routes exist.

### Do not memorize

- Every Reachability Analyzer supported resource.
- Every VPC Flow Log field here.
- Every OS ephemeral-port range.
- Every TGW route priority.
- Exact NAT quota values.
- Packet-capture command syntax.
- Console click paths.

### Ready when

Given a VPC failure, you can:

1. Write the exact five-tuple and actual transformed source/destination.
2. Prove forward and return longest-prefix routes.
3. Separate stateful SG from stateless ordered NACL behavior.
4. Diagnose IGW, NAT, peering, TGW, VPN, endpoint, IPv6, and appliance paths.
5. Recognize subnet IP and NAT port exhaustion.
6. Interpret Reachability Analyzer as configuration analysis, not packet/application proof.
7. Combine Flow Logs, metrics, CloudTrail, and real application tests.
8. Apply the smallest change and verify both network and application recovery.

---

## Skill 5.3.2 — Collect and interpret networking logs

### Official goal

Use VPC Flow Logs, ELB logs, WAF logs, CloudFront logs, and container logs to find the failed network/application layer.

### What the exam tests

- Choose the log that contains the needed evidence.
- Read exact source, destination, port, protocol, status, action, and timing fields.
- Separate packet acceptance from application response.
- Separate load-balancer errors from target errors.
- Identify the WAF terminating rule.
- Identify CloudFront edge/cache/origin behavior.
- Correlate container and infrastructure logs.
- Know payload and coverage limitations.

### Dimensions

**Primary:** evidence, diagnosis  
**Support:** remediation  
**Precision:** L3 — field meaning and log limitations matter.

### Request breadcrumb model

```text
Viewer
  -> CloudFront log
  -> WAF log
  -> ELB log
  -> VPC Flow Log
  -> container/proxy/application log
```

Each log proves one layer. No single log proves the full request.

### Fast log selector

| Need | Best evidence |
|---|---|
| Was IP/port traffic accepted at an ENI? | VPC Flow Logs |
| Did load balancer receive request and contact target? | ELB access log |
| Which web rule blocked/allowed request? | WAF log |
| Was response edge cache hit/miss/error? | CloudFront log |
| What did the workload/proxy actually do? | Container/application log |
| Who changed logging/network configuration? | CloudTrail |

### Evidence rule

```text
Log present = this layer observed something
Log absent  = traffic may not have reached layer, logging may be off,
              query may be cached, or delivery may have failed
```

Absence is a clue, not automatic proof.

## VPC Flow Logs

### Purpose

Capture IP traffic metadata for supported network interfaces.

Create at:

- VPC scope.
- Subnet scope.
- ENI scope.

Deliver to supported destinations such as:

- CloudWatch Logs.
- S3.
- Firehose.

Choose traffic filter:

- Accepted.
- Rejected.
- All.

### Inheritance of scope

- VPC-level flow log covers ENIs in that VPC according to support/filter.
- Subnet-level covers ENIs in that subnet.
- ENI-level covers one interface.
- New ENIs under VPC/subnet scope can be included automatically.

Inspect exact scope and filter before concluding that missing records mean no traffic.

### Default core fields

Recognize:

```text
version
account-id
interface-id
srcaddr
dstaddr
srcport
dstport
protocol
packets
bytes
start
end
action
log-status
```

Custom formats can add VPC, subnet, instance, AZ, packet addresses, flow direction, TCP flags, and other context.

### Five-tuple fields

```text
srcaddr + dstaddr + srcport + dstport + protocol
```

Example client request:

```text
srcaddr 10.0.1.25
srcport 51514
dstaddr 10.0.2.40
dstport 443
protocol 6
```

Meaning: client ephemeral port `51514` initiates TCP to server HTTPS port `443`.

Return flow reverses address and port roles.

### Protocol numbers

Recognize common values:

- `6` = TCP.
- `17` = UDP.
- `1` = ICMP for IPv4.
- `58` = ICMPv6.

Port fields may be absent/not meaningful for protocols without ports.

### Action field

**`ACCEPT`**

- Captured network controls allowed the flow at the logging interface.
- Does not prove destination process listened.
- Does not prove return traffic.
- Does not prove TLS/HTTP/application success.

**`REJECT`**

- Captured traffic was rejected by a network control such as SG/NACL context.
- Flow Log alone may not identify the exact rule.
- Compare SG/NACL configuration or use Reachability Analyzer.

### Log-status field

Recognize:

- `OK` — data logged normally.
- `NODATA` — no eligible traffic during interval.
- `SKIPDATA` — records skipped due to internal capacity/error condition.

`SKIPDATA` does not mean the packet was accepted or rejected. It means evidence is incomplete.

### Packets, bytes, and time

- `packets` and `bytes` are aggregated for the flow record.
- `start` and `end` define observed aggregation interval.
- Records can arrive after traffic occurs.
- Flow Logs are not packet-by-packet real-time capture.

Use the correct time window and allow delivery delay.

### TCP flags

Custom field `tcp-flags` can help identify handshake/reset behavior.

Common bit values:

- `1` = FIN.
- `2` = SYN.
- `4` = RST.
- `8` = PSH.
- `16` = ACK.

Values can be combined.

Examples:

- SYN seen, no reverse SYN-ACK evidence → path/listener/return issue.
- RST evidence → active rejection/no listener/application reset.

Flow aggregation can combine flags; it is not a packet trace.

### Packet address fields

Custom fields such as `pkt-srcaddr` and `pkt-dstaddr` can preserve packet-level address context when interface/resource translation or intermediate services make `srcaddr`/`dstaddr` less intuitive.

Useful for:

- NAT paths.
- Transit/inspection paths.
- Identifying original source behind an intermediate interface.

Always interpret fields using the ENI where the flow log was captured.

### Flow direction

Custom `flow-direction` can identify ingress or egress relative to the interface.

Direction is relative to that ENI—not the overall application architecture.

### Flow Log limitations

Flow Logs do not capture:

- Packet payload.
- HTTP URL/body/header meaning.
- TLS certificate or decrypted content.
- Exact SG/NACL rule ID that rejected traffic.
- Application process/listener status.
- Every documented AWS-reserved/control-plane traffic type.

Some traffic such as Amazon-provided DNS, DHCP, metadata/time/licensing paths can have documented exclusions.

Use DNS, ELB, WAF, or application logs for higher-layer meaning.

### Flow Log example diagnosis

```text
Request:  client:51514 -> server:443  ACCEPT
Response: no reverse flow found
```

Check:

- Server listener/OS firewall.
- Server-subnet outbound NACL ephemeral path.
- Return route.
- Stateful appliance symmetry.

Do not change client SG inbound merely because response is absent; SG return traffic is stateful.

### Flow Log failure map

| Evidence | Likely next check |
|---|---|
| Request `REJECT` at server ENI | Server SG inbound, server-subnet NACL |
| Request `ACCEPT`, no app log | OS firewall, listener, target address/process |
| Request and response `ACCEPT`, client times out | Other path segment, client OS/app, asymmetric capture |
| No record | Scope/filter/time/delivery, wrong ENI/IP/path, documented exclusion |
| `NODATA` | No eligible traffic in interval |
| `SKIPDATA` | Evidence gap; use another source/retry window |
| High bytes across AZ/interface | Cost/hairpin candidate |
| Repeated SYN/RST | Listener or active rejection candidate |

## ELB access and connection logs

### Purpose

Show load-balancer-side client, listener, target, TLS, status, and timing evidence.

Log capabilities and fields vary by ALB, NLB, and Classic Load Balancer.

Core question:

```text
Did the load balancer create the error,
or did the target return the error?
```

### ALB access-log fields

Recognize:

- Request time/type.
- Load balancer ID.
- Client IP and port.
- Target IP and port.
- Request line: method, URL, protocol.
- Request processing time.
- Target processing time.
- Response processing time.
- Load-balancer status code.
- Target status code.
- Received/sent bytes.
- User agent.
- TLS protocol/cipher.
- Target group ARN.
- Trace/request ID.
- Executed action/redirect/error reason fields where available.

Do not memorize field order. Know meaning.

### Client versus target fields

```text
client:port -> load balancer -> target:port
```

- Client address proves who reached the load balancer according to LB behavior.
- Target address proves which registered target was selected.
- Missing target value means the load balancer might not have selected/contacted a target.

### Status-code interpretation

**Load-balancer status code**

- What ALB returned to client.

**Target status code**

- What target returned to ALB.
- `-`/missing can mean no target response/status existed.

Examples:

```text
elb_status=503, target_status=-
```

Likely no healthy/available target or LB-generated failure.

```text
elb_status=500, target_status=500
```

Target/application returned `500`.

### Processing times

**Request processing time**

- Time before request is sent to target, according to LB log semantics.

**Target processing time**

- Time waiting for target response.

**Response processing time**

- Time from target response to completing response toward client.

Large target time points to application/target dependency. Large request/response time points elsewhere in the LB/client transfer path.

### Common ALB status clues

| Result | First checks |
|---|---|
| `503`, no target status | No healthy targets, target-group/listener action |
| `502`, no/invalid target response | Target reset/malformed response/TLS/backend protocol |
| `504`, no target response | Target timeout, SG/NACL, slow app/dependency |
| Target `4xx`/`5xx` present | Application/target returned it |
| Redirect status | Listener rule/action/application redirect |
| Fixed-response action | Executed ALB listener rule, target may be absent |

Exact cause needs `error_reason`, target health, and application logs.

### TLS/connection logs

Depending on load-balancer type/listener, connection/TLS logs can show:

- Client and listener addresses/ports.
- TLS protocol.
- Cipher.
- Handshake time/status.
- Certificate/client-certificate details where mutual TLS is used.
- Failure reason.

Useful when TCP reaches the load balancer but TLS handshake fails before an HTTP access log exists.

### ELB logging limitations

- Access log exists only when enabled and delivered successfully.
- A request that never reaches LB produces no LB access record.
- Log delivery is delayed/batched.
- NLB TCP flow evidence differs from ALB HTTP request evidence.
- Target/application internals require target logs.

### ELB failure map

| Symptom | Evidence chain |
|---|---|
| Client timeout; no ELB log | DNS/route/SG/NACL/listener before LB or logging delivery |
| ELB log; target missing | Listener rule, no healthy target, target selection/connectivity |
| Target status present | Investigate target/app response |
| High target processing time | App/dependency/target saturation |
| TLS failure before request | Connection/TLS log, listener policy/certificate/client capability |
| Only one target fails | Target IP, health, AZ, SG, app logs |

## WAF logs

### Purpose

Explain how a WAF web ACL evaluated an HTTP request.

Core fields:

- Timestamp.
- Web ACL ID.
- Action.
- Terminating rule ID/type.
- HTTP request: client IP, country, method, URI, query, headers.
- Rule-group match details.
- Non-terminating matches.
- Labels.
- Rate-based/CAPTCHA/challenge details where relevant.

### Terminating rule

The terminating rule decides the final web ACL action.

Examples:

- `BLOCK` rule terminates and blocks.
- `ALLOW` rule terminates and allows.
- `COUNT` records a match but normally continues.
- CAPTCHA/challenge can depend on token validity.
- If no rule terminates, default action wins.

Find the terminating rule before tuning unrelated rules.

### Managed rule-group evidence

Inspect:

- Managed rule group.
- Inner rule that matched.
- Override/excluded rule state.
- Labels added.
- Final terminating rule.

A managed rule can match/count while another later rule makes the final block.

### WAF false-positive workflow

```text
Find blocked request
  -> terminating rule ID/action
  -> matched field/value and labels
  -> confirm request legitimate
  -> add narrow scope-down/exception or count override
  -> retest
  -> monitor block/allow trend.
```

Do not disable the entire managed rule group for one URI/value.

### WAF log limitations

- Redacted fields may hide sensitive values.
- Oversize body/inspection limits can affect match evidence.
- Sampled requests are not complete logs.
- A request that bypasses the associated resource/WAF is absent.
- WAF log proves web-ACL action, not application result after allow.

### WAF failure map

| Evidence | Meaning |
|---|---|
| `BLOCK` + terminating rule | WAF caused denial |
| `ALLOW`, app returns `403` | WAF allowed; inspect origin/app/IAM |
| `COUNT` match | Rule observed but did not enforce |
| Default action terminates | No earlier terminating rule matched |
| No WAF record, ELB record exists | Wrong/no web ACL association or logging path |
| Unexpected managed-rule block | Inner rule/label/override and request field |

## CloudFront logs

### Purpose

Show viewer request handling at CloudFront edge.

Recognize standard and real-time logging models.

Useful fields can include:

- Date/time.
- Edge location.
- Viewer/client IP.
- Method.
- Host.
- URI path and query string.
- HTTP status.
- Bytes.
- User agent/referrer.
- Edge result/cache type.
- Detailed result/response result.
- Time taken.
- Request ID.
- TLS protocol/cipher.

### Edge result fields

Common result concepts:

- `Hit` — served from edge cache.
- `RefreshHit` — cached object revalidated/refreshed.
- `Miss` — origin request required.
- `Error` — edge/origin handling error.
- Redirect/limit/capacity result types where applicable.

Use detailed result type and HTTP status together. `Error` alone is too broad.

### Cache evidence

Combine:

- Edge result type.
- HTTP `Age` response header.
- `X-Cache` response header where observed.
- Cache behavior/path.
- Cache policy/TTL.
- Origin access logs.

`Hit` means edge served cached response. `Miss` does not mean origin is unhealthy.

### CloudFront status clues

| Status/evidence | First checks |
|---|---|
| `403` at edge | WAF, signed URL/cookie, geo restriction, alternate domain, S3/OAC origin response |
| `502` | Origin DNS/TLS/port/protocol/invalid response |
| `503` | Capacity/service/origin availability detail |
| `504` | Origin timeout/reachability/slow application |
| `Hit` with stale content | TTL/invalidation/versioning/cache key |
| Repeated `Miss` | Cache key cardinality, TTL, cacheability/method/headers |

CloudFront can cache some errors; inspect result type, `Age`, and error-caching policy.

### CloudFront log limitations

- Standard logs are delayed/batched.
- Real-time logs depend on sampling/configuration.
- Log fields do not contain full packet payload.
- A cache hit can produce no origin log.
- WAF logs are separate.
- Distribution configuration changes need deployment time.

### CloudFront-to-origin correlation

```text
CloudFront request ID/time/path
  -> WAF action if associated
  -> CloudFront result/status
  -> origin access log for misses
  -> application trace/request ID
```

No origin record on `Hit` is expected.

## Container and workload logs

### Why they matter

Infrastructure can accept traffic while the workload fails through:

- No listener.
- Wrong bind address/port.
- Application exception.
- Dependency timeout.
- DNS failure.
- Proxy/sidecar policy.
- Container restart or OOM.
- CNI/network plugin failure.

Flow Log `ACCEPT` plus no application record narrows the gap to host/container/listener or wrong target.

### ECS evidence

Use:

- Application `stdout`/`stderr` through configured log driver.
- ECS task/service events.
- Container exit reason/code.
- Health-check output.
- ECS agent logs for EC2 launch type where relevant.
- FireLens/router logs if used.
- Load-balancer target and task ENI Flow Logs.
- DNS and dependency logs.

Distinguish task role permission failure from network timeout.

### EKS evidence

Use:

- Pod/container logs.
- Previous container logs after restart.
- Pod events and readiness/liveness results.
- Ingress/controller logs.
- Service/endpoints/endpointslice state.
- CoreDNS logs/metrics.
- VPC CNI/network plugin logs and IP allocation.
- `kube-proxy`/data-plane logs where used.
- Control-plane API/audit/authenticator/controller/scheduler logs where enabled.
- Node OS/network logs.

Container log, Kubernetes event, and VPC network log show different layers.

### Proxy and sidecar evidence

Ingress proxies/service mesh/sidecars can show:

- Upstream cluster/target.
- Response flags.
- Connection timeout/reset.
- TLS/mTLS errors.
- Retry count.
- Upstream response time/status.

An application container can be healthy while sidecar policy blocks traffic.

### Container logging traps

- Container writes to file not collected by log driver.
- Multiline stack trace split incorrectly.
- Container restarts and old log disappears without centralized collection.
- Wrong task/pod/namespace/time window inspected.
- Sensitive headers/tokens logged.
- Log level too low during incident.
- Node clock/time-zone confusion.

Centralize before failure; retroactive logs cannot be collected if they never existed.

## Analysis destinations

### CloudWatch Logs Insights

Best for:

- Interactive recent operational investigation.
- Filter by IP, port, request ID, status, rule, path, or time.
- Aggregate counts/bytes/latency.
- Join mentally/correlate across log groups using IDs/time.

Use narrow time range and selected fields to reduce scan cost.

### S3 and Athena

Best for:

- Large historical datasets.
- Long retention.
- Cross-account/Region lake-style analysis.
- SQL aggregation over Flow/WAF/CloudFront/ELB logs.

Partition by time/account/Region/service where practical to reduce scan.

### Firehose

Best for:

- Managed streaming delivery.
- Transformation/buffering/compression.
- Delivery to supported analysis/storage destinations.

Firehose transports logs; it does not diagnose them by itself.

### Choosing destination

| Need | Choice |
|---|---|
| Fast recent interactive query | CloudWatch Logs Insights |
| Cheap long-term large history | S3 + Athena |
| Stream/transform to destination | Firehose |

## Cross-log correlation

### Correlation keys

Use:

- UTC timestamp/window.
- Client IP and port.
- Destination/target IP and port.
- Host and URI.
- CloudFront/ALB request or trace ID.
- Container request/trace ID.
- Resource/ENI/target ID.
- HTTP status.
- TLS details.

Allow for clock skew, aggregation windows, and delivery delay.

### HTTP request chain

```text
CloudFront: viewer path/result/status/request ID
  -> WAF: action/terminating rule
  -> ALB: client/target/LB status/target status/times
  -> Flow Log: target ENI five-tuple/action
  -> container: request/dependency/result
```

### Example diagnosis

```text
CloudFront: Miss, status 504
WAF: ALLOW
ALB: target selected, target_status=-, target_processing_time timeout
Flow Log: ALB-to-target ACCEPT
Container: no request
```

Likely inspect target listener/OS/container bind, NACL return, or wrong target port—not WAF.

### Layer ownership table

| Evidence | Proven layer | Not proven |
|---|---|---|
| Flow `ACCEPT` | ENI network controls accepted | Listener/application response |
| WAF `ALLOW` | WAF allowed web request | Origin/application allowed it |
| ALB target status `500` | Target returned `500` | Root cause inside app |
| CloudFront `Hit` | Edge cache served response | Origin contacted now |
| Container request log | App received request | Client received response |

## Troubleshooting workflow

### Evidence ladder

```text
1. Normalize UTC time and exact request/flow.
2. Confirm logging enabled, scope, filter, and destination.
3. Start at first expected layer.
4. Find last log that saw request.
5. Inspect next layer’s absence/error.
6. Correlate status, timing, IP/port, and request ID.
7. Confirm configuration with routes/SG/NACL/policies.
8. Make narrow fix.
9. Generate known test request.
10. Prove success across layers.
```

### Missing-log checklist

- Logging disabled.
- Wrong VPC/subnet/ENI/web ACL/distribution/LB/task scope.
- Filter captures only accept or reject.
- Destination policy/KMS permission broken.
- Delivery delayed.
- Query/request served by cache or alternate path.
- Traffic never reached layer.
- Resource was replaced; ID changed.
- `SKIPDATA` or service-specific sampling.
- Wrong time zone/window.

### Safe remediation

```text
Preserve evidence
  -> enable/repair logging narrowly
  -> reproduce known request
  -> identify last good/first bad layer
  -> change exact rule/path/listener/app
  -> reproduce
  -> confirm expected logs/status/timing
  -> remove temporary verbose/sensitive logging
  -> retain needed audit logs.
```

Do not log credentials or full sensitive payloads to debug connectivity.

### Governance

- Enable critical logs before incidents.
- Centralize cross-account delivery where appropriate.
- Encrypt destinations and limit readers.
- Set retention/lifecycle by evidence requirement.
- Redact/filter sensitive web fields.
- Alert on log-delivery failure and `SKIPDATA` trends.
- Use consistent UTC and request/trace IDs.
- Protect logs against deletion/modification.
- Control high-volume cost with scope, partitions, and filtering—not blind disablement.

### Exam traps

- Flow Logs contain metadata, not packet payload.
- `ACCEPT` does not prove application response or return path.
- `REJECT` does not directly name the exact SG/NACL rule.
- `NODATA` means no eligible traffic; `SKIPDATA` means incomplete logging.
- Flow Log direction is relative to the captured ENI.
- ALB status and target status are different fields.
- Missing target status can mean LB never received target response.
- High target processing time points toward target/application dependency.
- WAF terminating rule determines final action; `COUNT` is nonterminating observation.
- WAF `ALLOW` plus HTTP `403` means look after WAF.
- CloudFront cache hit normally creates no origin request/log.
- CloudFront result type and HTTP status must be read together.
- Container logs do not replace VPC/ELB evidence; VPC logs do not replace app logs.
- CloudTrail shows configuration changes, not network packets/web requests.
- Public/resolver DNS logs and network logs capture different layers.
- Log absence can mean disabled delivery, caching, bypass, or no traffic—not one guaranteed cause.

### Do not memorize

- Full field order for every log version.
- Every Flow Log custom field.
- Every ELB error reason.
- Every WAF JSON property.
- Every CloudFront result subtype.
- Exact delivery-delay guarantees.
- Complete Logs Insights/Athena syntax.
- Console click paths.

### Ready when

Given a network incident, you can:

1. Choose Flow, ELB, WAF, CloudFront, or container logs for the question.
2. Read five-tuple, protocol, packets/bytes, time, action, and log status.
3. Explain `ACCEPT`, `REJECT`, `NODATA`, and `SKIPDATA` without overclaiming.
4. Separate load-balancer status/timing from target status/timing.
5. Find the WAF terminating rule and distinguish `COUNT` from enforcement.
6. Read CloudFront edge/cache result, status, time, and origin correlation.
7. Correlate logs by UTC time, IP/port, resource, and request/trace ID.
8. Identify the last layer that saw the request and verify the fix end to end.

---

## Skill 5.3.3 — Identify and remediate CloudFront caching issues

### Official goal

Use cache evidence to explain misses, stale/wrong content, behavior mismatch, cached errors, and origin failures. Apply the smallest safe fix.

### What the exam tests

- Read cache result, `Age`, and cache-control headers.
- Find the matching behavior and cache policy.
- Understand cache-key cardinality.
- Explain minimum/default/maximum TTL.
- Distinguish edge cache failure from origin failure.
- Handle stale objects and cached errors.
- Choose versioning, invalidation, policy change, or origin repair.
- Improve hit ratio without sharing private/wrong content.

### Dimensions

**Primary:** evidence, diagnosis, remediation, optimization  
**Support:** configuration, behavior  
**Precision:** L3 — result fields, headers, behavior order, cache key, TTL, error caching, invalidation, and origin status matter.

### Core cache pipeline

```text
Viewer request
  -> first matching behavior
  -> build cache key
  -> edge cache lookup
      -> fresh object: HIT
      -> stale object: revalidate/refresh
      -> absent object: MISS -> origin
  -> decide whether/how long to cache origin response
  -> return viewer response
```

Every cache problem belongs to one stage in this pipeline.

### Diagnostic order

```text
1. Which behavior matched?
2. What exact cache key was built?
3. Was object cacheable and fresh?
4. What edge result/status/headers appeared?
5. If origin called, what did origin return?
6. Was error/content cached?
7. Is distribution/invalidation deployed?
```

Do not invalidate first without knowing why the wrong object was cached.

## Cache evidence

### Viewer response headers

Useful headers:

- `X-Cache` — CloudFront hit/miss/error clue.
- `Age` — seconds a cached response has resided in shared cache path.
- `Cache-Control` — origin/viewer caching directives.
- `Expires` — absolute expiry time.
- `ETag` — object version validator.
- `Last-Modified` — time validator.
- `Via` — proxy chain clue.
- `X-Amz-Cf-Pop` — edge location.
- `X-Amz-Cf-Id` — CloudFront request identifier.

Header names are case-insensitive. Values carry the behavior.

### Common `X-Cache` clues

- `Hit from cloudfront` — served from cache.
- `Miss from cloudfront` — origin path used because key absent/not usable.
- `RefreshHit from cloudfront` recognition — stale cached object revalidated/refreshed successfully.
- `Error from cloudfront` — CloudFront/origin path produced an error; inspect detailed logs/status.

`Miss` is normal for a cold cache and does not prove a fault.

### `Age`

```text
Age: 120
```

Means response has shared-cache age around 120 seconds.

- Increasing `Age` across repeated requests suggests a hit.
- Missing/zero `Age` can indicate miss, non-cacheable response, or fresh insertion.
- Compare with TTL and edge location.

Different edge locations can hold different cache state.

### CloudFront log result fields

Use:

- Edge result type.
- Response result type.
- Detailed result type.
- HTTP status.
- Edge location.
- Request ID.
- Time taken.
- Path/query/host.

Common result concepts:

- `Hit`.
- `Miss`.
- `RefreshHit`.
- `Error`.
- Redirect/limit/capacity detail where applicable.

Read result and status together.

## Behavior selection

### Ordered behavior rule

- Ordered behaviors are checked first.
- First path pattern that matches wins.
- Default `*` behavior catches the rest.
- Path matching is case-sensitive.

Example:

```text
/api/admin/*  -> auth/no cache
/api/*        -> API cache policy
default *     -> static site
```

Put `/api/admin/*` before `/api/*`.

### Behavior mismatch symptoms

- Wrong origin receives request.
- Dynamic API unexpectedly cached.
- Signed URL/cookie not required.
- Wrong allowed methods.
- Wrong viewer protocol policy.
- Cache policy seems ignored.
- `/Images/a.jpg` differs from `/images/a.jpg`.

Always inspect behavior order before editing TTL.

### Behavior objects to compare

- Path pattern.
- Target origin/origin group.
- Viewer protocol policy.
- Allowed and cached methods.
- Cache policy.
- Origin request policy.
- Response headers policy.
- Signed-content requirement.
- Function/Lambda@Edge associations.

Edge code can rewrite URI before later processing; include it in path diagnosis.

## Cache key

### Cache-key components

Can include:

- Request path.
- Selected query strings.
- Selected headers.
- Selected cookies.
- Compression variant.

CloudFront stores one object per unique cache key at each cache layer.

### High-cardinality cache key

Bad hit-ratio examples:

- Session cookie.
- Unique request ID header.
- Timestamp query parameter.
- Tracking parameters.
- Full `User-Agent`.
- Authorization/user-specific values.
- Query-string permutations/order.

If every request creates a new key, CloudFront behaves like a pass-through proxy.

### Too-small cache key

Danger:

```text
Origin response varies by tenant/language/auth cookie
but value is absent from cache key
```

Result:

- Wrong language/content.
- Cross-user/tenant data exposure.
- Incorrect API response.

Optimization rule:

```text
Cache key must be as small as possible,
but include every value that changes the response.
```

### Cache policy versus origin request policy

**Cache policy**

- Defines cache key.
- Controls TTL limits.
- Forwards included cache-key values to origin.

**Origin request policy**

- Forwards extra headers/cookies/query strings to origin.
- Does not add them to cache key.

If origin response varies on an origin-request-only value, cached content can be wrong.

### Query-string behavior

Check:

- None, allowlist, or all selected for cache key.
- Origin requires parameter but cache does not vary on it.
- Tracking parameters create unnecessary variants.
- Different parameter ordering creates separate cache-key behavior where normalization is absent.
- Application canonicalization/edge function rewrites.

Prefer an allowlist of response-relevant parameters.

### Cookie behavior

- Forward/cache only cookies that change response.
- Session/analytics cookies often destroy hit ratio.
- Personalized responses should not be shared without correct key/no-store design.
- Origin `Set-Cookie` handling can cause sensitive cookie behavior if response is cached carelessly.

### Header behavior

Headers commonly relevant:

- `Accept-Encoding` for compressed variants.
- `Origin` for CORS where response varies.
- `Authorization` for protected/dynamic content.
- Language/device/tenant custom headers.

Forwarding all viewer headers usually lowers cache reuse and can effectively disable useful caching patterns.

### Compression variants

When compression is enabled, CloudFront can normalize supported `Accept-Encoding` values and cache compressed/uncompressed variants.

Check:

- Viewer advertises encoding.
- Compression enabled in cache policy/behavior.
- Origin content type/size supports it.
- Cache key includes normalized encoding behavior.

## TTL and cache directives

### TTL hierarchy

CloudFront uses cache-policy limits with origin headers:

- Minimum TTL.
- Default TTL.
- Maximum TTL.
- `Cache-Control`.
- `Expires`.

Exact effective TTL depends on their interaction.

### `Cache-Control` directives

Recognize:

- `max-age=N` — freshness lifetime for caches/clients.
- `s-maxage=N` — shared-cache lifetime; can override `max-age` for CloudFront.
- `no-cache` — response may be stored but must be revalidated before reuse.
- `no-store` — do not store response.
- `private` — intended for private/client cache, not shared cache.
- `public` — explicitly shared-cacheable where other conditions allow.
- `must-revalidate` recognition.
- `stale-while-revalidate`/`stale-if-error` recognition where supported.

Do not interpret `no-cache` as identical to `no-store`.

### Minimum TTL trap

If cache-policy minimum TTL is greater than zero, CloudFront can retain/cache content for at least that minimum even when origin sends directives such as:

- `no-cache`.
- `no-store`.
- `private`.

For sensitive/dynamic responses, use a policy with minimum TTL `0` and correct cache-key/cache-control behavior.

### Default TTL

Used when origin provides no applicable freshness information, bounded by policy.

Unexpected caching can happen when origin omits `Cache-Control` and behavior default TTL is nonzero.

### Maximum TTL

Caps how long CloudFront uses a larger origin freshness value.

Origin `s-maxage=86400` does not exceed a lower policy maximum.

### Revalidation

CloudFront can send conditional requests using:

- `If-None-Match` with `ETag`.
- `If-Modified-Since` with `Last-Modified`.

Origin `304 Not Modified` lets cached object become fresh without retransmitting body.

`RefreshHit`/origin logs can reveal revalidation.

## Why an object is not cached

### Common causes

- First request/cold edge cache.
- Behavior uses caching-disabled policy/TTL zero.
- Origin sends `no-store`, `private`, or restrictive directives and policy minimum permits honoring them.
- Request method is not cacheable.
- Response status not cached under current behavior.
- `Authorization`, cookies, or headers force/differentiate requests.
- High-cardinality cache key.
- Object expired between tests.
- Repeated invalidations.
- Different POPs receive requests.
- Edge function changes path/key-related values.

### Cacheability investigation

```text
Same POP + same request twice
  -> compare X-Cache/Age
  -> inspect behavior/cache policy
  -> inspect origin Cache-Control/Expires
  -> inspect method/status
  -> compare cache-key values
  -> check invalidations/deployments.
```

Use identical host, path, query, headers, cookies, and compression during comparison.

## Low cache-hit ratio

### Evidence

- CloudWatch cache-hit-rate metric.
- High `Miss` count in logs.
- High origin request/byte volume.
- Low/missing `Age`.
- Many unique query/cookie/header combinations.
- Frequent invalidations.
- Short TTLs.

### Remediation

- Remove irrelevant query strings, headers, and cookies from cache key.
- Increase TTL for safe immutable/static content.
- Add correct origin `Cache-Control`.
- Version static object filenames.
- Separate dynamic and static behaviors.
- Enable compression.
- Consider Origin Shield for many POPs hitting one origin.
- Avoid blanket invalidations.

Never improve hit ratio by omitting a value that protects personalization/tenant separation.

### Cold-cache reality

- Each edge/regional cache has its own state.
- First request at a new location can miss.
- Low-volume global objects may show natural misses.
- Deployment/invalidation empties or bypasses prior cache state.

Judge over enough requests/time/POPs.

## Stale or wrong content

### Common causes

- Long TTL.
- Reused object key after deployment.
- Invalidation missing/wrong path/case.
- Invalidation still in progress.
- Request matches another behavior/key.
- Browser or recursive/proxy cache outside CloudFront.
- Origin updated in one place but behavior uses another origin.
- Cached error/custom error response.
- Edge deployment not complete.

### Versioned object names

Preferred for normal static releases:

```text
app.abc123.js
styles.2026-07-19.css
```

Benefits:

- New URL guarantees new key.
- Long immutable TTL safe.
- Old clients can still load old dependencies.
- Easy rollback by changing HTML reference.

Use invalidation for urgent same-key removal/correction.

### Invalidation

Invalidation:

- Marks matching cached paths for removal before normal expiry.
- Can target exact path or wildcard pattern.
- Is case-sensitive according to path behavior.
- Has `InProgress`/completed lifecycle.
- Propagates across edge caches.
- Does not edit/delete origin content.
- Has request/cost implications.

Check leading slash, wildcard placement, path case, and distribution ID.

### Invalidation traps

- Invalidated `/index.html`, but viewer requests `/` with default-root behavior.
- Invalidated wrong case/path.
- Query-string/cache variants not covered as expected.
- Distribution ID is wrong.
- Invalidation complete, but browser cache still serves old object.
- Origin still returns old content, so next miss recaches it.

## Error caching

### Model

CloudFront can cache configured error responses for an error-caching minimum TTL.

```text
Origin returns 404/500
  -> CloudFront caches error
  -> origin recovers
  -> viewers can still receive cached error until expiry/invalidation
```

Custom error responses can change viewer response page/code and cache duration.

### Error-cache evidence

- `X-Cache` hit/error wording.
- `Age` on error response.
- Edge result/detailed result.
- Origin log absent on repeated error hits.
- Error-caching TTL/custom error config.

### Error-cache remediation

- Fix origin first.
- Reduce error TTL for transient failures.
- Invalidate affected path when urgent.
- Use custom error response deliberately.
- Do not cache authentication/authorization failures broadly.
- Do not hide a persistent broken origin with a long friendly error cache.

## Origin failures mistaken for caching problems

### Origin status map

| Viewer symptom | First origin checks |
|---|---|
| `403` | WAF/signed content/geo, then OAC bucket/KMS policy or origin authorization |
| `404` | Object/key/path/case, origin path, behavior origin |
| `502` | Origin DNS, TLS hostname/chain/policy, port/protocol, invalid response |
| `503` | Origin/service capacity or no healthy backend |
| `504` | Route/SG/NACL, origin timeout, slow application/dependency |

### Origin evidence

Use:

- CloudFront detailed result/status/time.
- Origin access/application logs.
- ALB target status and processing time.
- S3 access/CloudTrail policy evidence.
- OAC and bucket/KMS policy.
- Origin DNS/TLS test.
- Origin health metrics.

A `Miss` followed by `504` is an origin path problem, not low cache hit by itself.

### Origin failover

Check:

- Origin group attached to matching behavior.
- Primary and secondary origins.
- Configured failover status codes.
- Request/method eligible for failover behavior.
- Secondary content and authorization.
- Cached error response after both attempts.

Origin group performs failover, not weighted balancing.

## Personalized and sensitive content

### Safe patterns

- Do not cache highly sensitive per-user responses unless key/policy is proven safe.
- Include all response-varying identity/tenant values in cache key, or disable caching.
- Use signed URLs/cookies for viewer access where applicable.
- Keep origin private with OAC/restricted access.
- Avoid forwarding/storing secrets in query strings.
- Inspect `Set-Cookie` behavior.

### Cache-leak clue

```text
User B receives User A content
```

Immediately inspect:

- Behavior matched.
- Cache policy key.
- Authorization/cookie/tenant headers.
- Origin response headers.
- Edge functions rewriting/removing identity.
- Minimum TTL overriding `private`/`no-store` intent.

Contain by disabling/invalidation of affected caching path, then correct policy.

## Troubleshooting playbooks

### Repeated miss

```text
Confirm same POP/request
  -> verify GET/HEAD and success status
  -> matched behavior/cache policy
  -> TTL > 0?
  -> origin Cache-Control/Expires?
  -> compare query/header/cookie key
  -> invalidation/deployment activity
  -> origin/edge function variation.
```

### Stale object

```text
Inspect X-Cache + Age
  -> effective TTL
  -> origin object/version
  -> behavior/origin path
  -> invalidation status/path
  -> browser/intermediate cache
  -> version object key for next release.
```

### Wrong object

```text
Check behavior order
  -> cache key missing variant?
  -> origin request-only value changes response?
  -> edge rewrite?
  -> origin host/path?
  -> purge affected key after policy fix.
```

### Cached error

```text
Check status + Age/result
  -> verify whether origin called
  -> fix origin
  -> reduce error TTL/invalidate
  -> monitor new misses and recovered hits.
```

### Safe policy change

```text
Capture hit ratio/errors/current policy
  -> clone/create new cache policy
  -> attach to narrow test behavior/path
  -> test variants and privacy
  -> compare hit ratio/origin load
  -> expand
  -> invalidate only affected keys if required
  -> retain rollback policy.
```

### Evidence hierarchy

```text
Viewer headers
  -> CloudFront standard/real-time log
  -> distribution behavior/policies
  -> WAF log
  -> origin access/application log
  -> CloudTrail config change
```

Correlate using time, POP, path, host, request ID, and origin status.

### Metrics

Watch:

- Cache hit rate.
- Requests.
- Bytes downloaded/uploaded.
- Viewer `4xx`/`5xx` rates.
- Origin latency/errors/requests.
- Invalidation activity.

Hit rate improvement with rising wrong-content errors is not success.

### Exam traps

- First matching behavior wins; path order can override expected cache policy.
- CloudFront cache key and origin request forwarding are different.
- Extra high-cardinality key values cause misses.
- Missing response-varying key values cause wrong/shared content.
- `no-cache` means revalidate; `no-store` means do not store.
- Positive minimum TTL can cache despite origin `no-cache`, `no-store`, or `private` directives.
- `s-maxage` controls shared-cache freshness and can override `max-age` for CloudFront.
- `Age` plus edge result is stronger evidence than one header alone.
- A miss is normal for cold/new POP cache.
- Cache hit creates no origin request for that viewer request.
- Invalidation removes cached copies; it does not fix origin or policy.
- Versioned filenames are better than repeated invalidations for normal static releases.
- Error responses can be cached after origin recovers.
- `502`/`504` often indicates origin TLS/connectivity/latency, not a cache-key defect.
- Origin failover requires matching status configuration and eligible request behavior.
- Better hit ratio must never weaken user/tenant isolation.

### Do not memorize

- Every CloudFront result subtype.
- Exact default TTL values for every managed policy.
- Exact invalidation pricing/free allowance.
- Every cacheable status-code rule.
- Every edge-cache propagation interval.
- Complete log-field order.
- Console click paths.

### Ready when

Given a CloudFront caching issue, you can:

1. Identify matched behavior and exact cache policy.
2. Read `X-Cache`, `Age`, result type, status, and origin logs.
3. Build the cache key from query strings, headers, cookies, and compression.
4. Explain minimum/default/maximum TTL and cache-control directives.
5. Diagnose repeated misses, stale/wrong content, cached errors, and origin failures.
6. Choose versioned keys, invalidation, policy tuning, error-TTL change, or origin repair.
7. Improve cache hit rate without caching personalized/sensitive responses incorrectly.

---

## Skill 5.3.4 — Identify and troubleshoot hybrid and private connectivity issues

### Official goal

Troubleshoot Site-to-Site VPN, Client VPN, Direct Connect recognition, PrivateLink/endpoints, peering, Transit Gateway, and private DNS paths.

### What the exam tests

- Separate tunnel/control-plane health from data-plane reachability.
- Find IKE/IPsec, BGP, static-route, or MTU failure.
- Check both Site-to-Site VPN tunnels.
- Separate Client VPN authentication, authorization, and routing.
- Diagnose endpoint state, private DNS, SG, and policy layers.
- Diagnose peering/TGW association, propagation, and return path.
- Test from the actual source network.

### Dimensions

**Primary:** evidence, diagnosis, remediation  
**Support:** configuration, behavior, governance  
**Precision:** L3 — tunnel/IKE/BGP/routes/MTU, Client VPN gates, endpoint DNS/policies, and TGW tables matter.

### Core troubleshooting layers

```text
1. DNS name and selected IP
2. Underlay/physical internet or private circuit
3. Tunnel/session/endpoint/attachment state
4. Routing control plane: BGP/static/propagation
5. Forward and return data-plane routes
6. SG/NACL/firewall/authorization/policy
7. MTU/TLS/application
```

“Connected” at one layer does not prove the next layer.

### Fast symptom selector

| Symptom | First layer |
|---|---|
| VPN tunnel `DOWN` | IKE/IPsec/underlay/PSK/parameters |
| VPN tunnel `UP`, no traffic | Routes, BGP/static prefixes, SG/NACL/firewall |
| Small packets work, large transfers stall | MTU/fragmentation/MSS |
| Client VPN connects, resource denied | Authorization rule/route/SG |
| Endpoint DNS resolves public IP | Private DNS/Resolver path |
| Endpoint returns `AccessDenied` | Endpoint/IAM/resource/KMS policy |
| A-B and B-C work, A-C fails | Peering non-transitivity |
| TGW one-way traffic | Return VPC/TGW association/route chain |

## Site-to-Site VPN

### Object model

```text
Customer gateway device/public IP
  -> customer gateway resource
  -> VPN connection
      -> tunnel 1
      -> tunnel 2
  -> virtual private gateway or Transit Gateway
  -> AWS routes
```

### Objects to inspect

- Customer gateway public IP.
- Customer gateway BGP ASN.
- VPN attachment: VGW or TGW.
- Tunnel outside and inside IP addresses.
- Pre-shared key.
- IKE/IPsec options.
- Tunnel state/last status change/status message.
- BGP peer/session and accepted/advertised routes.
- Static route configuration where used.
- Tunnel logging and CloudWatch metrics.

Both tunnels exist for redundancy. Configure both on the customer gateway device.

### Underlay requirements

Before IKE can work:

- Customer gateway public IP is correct and stable.
- Internet/provider path reaches AWS tunnel outside IPs.
- Customer firewall permits IKE/IPsec traffic.
- NAT traversal behavior is supported/configured where NAT exists.
- No upstream ACL/provider blocks required traffic.
- Device clock and software are healthy.

Common traffic includes UDP `500` for IKE and UDP `4500` for NAT traversal. IPsec behavior depends on NAT/device design.

### IKE and IPsec phases

Simplified:

```text
IKE phase 1
  -> authenticate peers and create secure management channel
IPsec phase 2
  -> negotiate data-plane security associations
```

Both sides must agree on supported:

- IKE version.
- Encryption algorithm.
- Integrity algorithm.
- Diffie-Hellman group.
- Lifetime/rekey behavior.
- Pre-shared key.
- Phase 2/PFS parameters.
- Traffic selectors where the device requires them.

Do not memorize every proposal. Compare AWS tunnel configuration with device configuration.

### Tunnel-down ladder

```text
1. Correct customer gateway public IP?
2. Underlay reaches AWS outside tunnel IP?
3. UDP 500/4500/IPsec permitted?
4. PSK identical?
5. IKE version/proposals overlap?
6. Phase 2/PFS/selectors/lifetimes overlap?
7. DPD/rekey/device logs show failure reason?
8. AWS tunnel log/status message agrees?
```

Use logs from both peers; one side often shows only a timeout while the other shows proposal mismatch.

### Dynamic routing with BGP

Need:

- Correct customer and AWS ASNs.
- Correct tunnel inside neighbor IPs.
- BGP session established over each tunnel.
- Intended prefixes advertised by both sides.
- Route filters/limits accept them.
- Best-path selection sends traffic through intended tunnel/link.
- AWS route propagation/attachment table installs routes.

Tunnel `UP` with BGP `DOWN` can still mean no dynamic routes.

### BGP symptom map

| Symptom | First checks |
|---|---|
| IKE/IPsec up, BGP down | Neighbor IP, ASN, BGP auth, inside routes/firewall |
| BGP up, no AWS route | Advertised prefix, filters, propagation/TGW table |
| AWS sends, on-prem does not return | On-prem best route/advertisement/filter |
| Wrong tunnel preferred | BGP attributes/AWS route priority/device policy |
| Session flaps | Underlay loss, timers, device CPU, rekey interaction |

### Static routing

Need:

- VPN connection static prefixes configured.
- VPC/TGW routes toward VPN attachment.
- On-premises static routes toward AWS CIDRs.
- Return prefixes include all VPC/secondary CIDRs.
- No overlapping/competing route wins incorrectly.

Static route does not adapt automatically when a new network is added.

### Tunnel up, no traffic

Check:

```text
AWS source subnet route -> VGW/TGW
  -> VPN route/BGP prefix
  -> customer device route
  -> on-prem firewall
  -> destination
  -> complete reverse path
```

Also check:

- VPC SG/NACL uses correct on-premises CIDR.
- On-premises firewall sees private AWS source, not tunnel outside IP.
- TGW association/propagation.
- Route with longer prefix points elsewhere.
- Appliance/NAT policy changes addresses.

### VPN tunnel metrics

Recognize:

- `TunnelState`.
- `TunnelDataIn`.
- `TunnelDataOut`.

Interpretation examples:

| Evidence | Meaning |
|---|---|
| State `0`/down | Tunnel control-plane failure |
| State up, data both zero | No routed traffic or app idle |
| Data out rises, data in zero | Return route/firewall/on-prem receive issue |
| One tunnel up only | Connectivity works but redundancy degraded |
| Data suddenly shifts tunnels | Rekey/failure/BGP path change |

Metrics are aggregate evidence; use device/VPN logs for reason.

### VPN logs

Where enabled, tunnel logs can reveal:

- IKE negotiation.
- Proposal mismatch.
- Authentication/PSK failure.
- Dead-peer detection.
- Rekey events.
- IPsec security-association status.
- BGP peer events where included.

Protect logs; they contain topology and security metadata. Do not log/share PSKs.

### Two-tunnel behavior

- AWS provides two tunnel endpoints.
- Configure and monitor both.
- Customer device should accept routing/failover on both as designed.
- Planned maintenance can move traffic.
- Alarm when one tunnel is down, even if application still works.

One tunnel up is service continuity, not full redundancy.

### Asymmetric VPN path

Forward and return can use different tunnels/links.

This may work for routing but fail when customer firewalls/NAT are stateful.

Check:

- BGP best path in both directions.
- ECMP behavior.
- Stateful device session ownership.
- Active/standby device synchronization.
- Route propagation changes.

### MTU and fragmentation

IPsec adds headers, reducing usable packet size.

Symptoms:

- Ping/small requests work.
- Large HTTPS/file transfer hangs.
- TCP connects but stalls after handshake.
- Retransmissions increase.
- Only some applications fail.

Check:

- Path MTU.
- “Do not fragment” behavior.
- ICMP messages allowed for path-MTU discovery.
- TCP MSS clamping on customer device.
- Fragment handling on firewall/tunnel.
- Application packet sizes.

Do not memorize one universal VPN MTU. Measure and use AWS/device guidance.

### Site-to-Site VPN failure map

| Symptom | First checks |
|---|---|
| Both tunnels down | Underlay, customer IP, firewall, common PSK/proposal/device issue |
| One tunnel down | Tunnel-specific config/path; redundancy alarm |
| Tunnels up, no routes | BGP/static/propagation/filters |
| Routes present, timeout | SG/NACL/on-prem firewall/return route/listener |
| Intermittent large transfers | MTU/MSS/fragmentation or asymmetric state |
| New VPC CIDR fails | Missing advertisement/route/filter/security range |
| Traffic uses wrong VPN | Longest prefix/BGP attributes/TGW route table |

## Direct Connect recognition and diagnosis

### Layer model

```text
Physical Direct Connect connection
  -> virtual interface (VIF)
  -> BGP session
  -> VGW/DX gateway/TGW association
  -> advertised routes
  -> VPC/on-premises data path
```

Physical connection up does not prove VIF/BGP/routes work.

### VIF types

Recognize:

- Private VIF for private VPC connectivity through supported gateway design.
- Transit VIF for Transit Gateway through Direct Connect gateway design.
- Public VIF for AWS public service prefixes.

Choose based on destination, not merely “private cable.”

### Direct Connect checks

- Physical connection state/light level/provider circuit.
- VLAN ID.
- VIF state.
- Customer/AWS BGP peer IPs.
- ASN and BGP authentication.
- Advertised/received prefixes and filters.
- Direct Connect gateway association/allowed prefixes.
- VGW/TGW attachment and route tables.
- Return route.
- Redundant connection/location/device.

Direct Connect is not encrypted by default merely because it is private. Add an approved encryption design where required.

### Direct Connect symptom map

| Symptom | First checks |
|---|---|
| Physical link down | Provider/cross-connect/port/device |
| Link up, VIF down | VLAN/VIF/provider handoff/config |
| VIF up, BGP down | Peer IP/ASN/auth/firewall |
| BGP up, no VPC reachability | Prefix filters, DXGW/VGW/TGW association/routes |
| Only one Region/VPC fails | Allowed prefixes/gateway association/TGW table |
| Planned resilience fails | Both circuits share device/location/provider path |

## Client VPN

### Object model

```text
Client
  -> Client VPN endpoint
  -> authentication
  -> authorization rule
  -> endpoint route
  -> target-network association
  -> SG/NACL/VPC route
  -> destination
```

Connected tunnel is only the first gate.

### Three gates

```text
Authentication  = who are you?
Authorization   = may you access this destination network?
Route           = where is that destination sent?
```

All three must succeed.

### Authentication checks

Depending on configuration:

- Mutual certificate validity/chain/expiry.
- Active Directory authentication.
- Federated/SAML identity provider.
- MFA/conditional access behavior.
- Client configuration file/endpoints.
- Endpoint state and server certificate.
- Client clock and TLS compatibility.

Connection logs and client logs give the failure stage.

### Authorization rules

- Grant access to destination network CIDR.
- Can apply to all users or an identity/group.
- Do not create routes.
- Do not change destination SG/NACL.

Authentication success plus missing authorization gives a connected client with denied destination access.

### Client VPN routes

- Route table needs destination network.
- Route targets a target-network association.
- Routes should be consistent across intended associations/AZs.
- Destination VPC/TGW/on-premises route must return traffic.

Authorization and route often use the same CIDR intent but are separate objects.

### Target-network association

- Associates endpoint with a VPC subnet.
- Provides entry into VPC/AZ.
- Associated security groups control path.
- Multiple associations improve availability.
- Association state must be available.

One failed/missing association can create zonal or route inconsistency.

### Client CIDR overlap

Client VPN client CIDR must not conflict with destination VPC/on-premises/client-local networks.

Overlap symptoms:

- Client sends traffic locally instead of tunnel.
- Ambiguous route.
- One user network works, another fails.
- Return route selects wrong network.

Use non-overlapping address pools and destination networks.

### Split tunnel versus full tunnel

**Split tunnel**

- Only configured destination routes use VPN.
- Other internet/local traffic stays outside VPN.

**Full tunnel**

- Broad/default traffic uses VPN when configured/authorized.
- Requires AWS egress route/NAT/security for internet access.

After route changes, clients may need reconnect/config refresh to receive the new route set.

### Client VPN DNS

Check:

- DNS server addresses configured for clients.
- Client has route to DNS server.
- Resolver inbound/private hosted-zone path where needed.
- Split-tunnel route includes DNS destination.
- Local DNS suffix/cache conflicts.

IP works but hostname fails = DNS path, not basic Client VPN authentication.

### Client VPN connection logs

Can show:

- Connection attempts.
- Client/username identity context.
- Connection established/terminated.
- Reason/status.
- Assigned client address and timestamps where available.

They do not prove every destination packet; combine with VPC Flow Logs and application logs.

### Client VPN failure map

| Symptom | First checks |
|---|---|
| Cannot establish tunnel | Endpoint state, auth/cert/IdP, client config, network/TLS |
| Connected, all resources fail | Target association, route, authorization, SG |
| One destination denied | Exact authorization CIDR/group and route |
| IP works, name fails | Client DNS/Resolver route/private zone |
| One client location fails | Local CIDR overlap/firewall/ISP |
| Internet fails in full tunnel | Default route, authorization, NAT/IGW return path |
| New route invisible | Reconnect client/split-tunnel route refresh |

## PrivateLink and VPC endpoints

### Endpoint status first

Inspect:

- Endpoint type.
- Service name and Region.
- Endpoint state.
- Acceptance state for endpoint service.
- Selected subnets/AZs and ENIs.
- Private DNS.
- Security groups.
- Endpoint policy.

An endpoint in `pendingAcceptance` is not ready for service traffic.

### Interface endpoint path

```text
Client resolves service name
  -> endpoint ENI private IP
  -> client SG/NACL
  -> endpoint SG inbound port
  -> endpoint policy
  -> IAM/resource/KMS policies
  -> provider service/target
```

Network timeout and API `AccessDenied` are different branches.

### Private DNS failure

Check:

- Private DNS enabled on endpoint where supported.
- VPC `enableDnsSupport`/`enableDnsHostnames`.
- Client uses VPC/Resolver path.
- Conflicting private hosted zone.
- On-premises conditional forwarding to Resolver inbound endpoint.
- DNS answer returns endpoint ENI IPs, not public service IPs.
- Certificate hostname matches normal/endpoint DNS name used.

Endpoint can be available while client still uses public DNS/NAT path.

### Interface endpoint network failure

Check:

- Endpoint SG inbound, commonly TCP `443`, from actual client source.
- Client SG outbound.
- NACL both directions.
- Routes from other VPC/on-premises to endpoint ENIs.
- Return route.
- ENI/AZ health and subnet IP capacity.
- Service listener/endpoint health.

Within same VPC, local route reaches ENI; no special route-table entry is expected.

### Endpoint authorization failure

Inspect all relevant gates:

```text
IAM identity policy
  + endpoint policy
  + service resource policy
  + KMS key policy
  + SCP/boundary/session policy
```

Endpoint policy can restrict but does not grant service permission.

### Gateway endpoint failure

For S3/DynamoDB:

- Correct VPC/Region/service.
- Source route table associated.
- Managed prefix-list route exists/wins.
- Endpoint policy permits request.
- IAM/bucket/table/KMS policy permits request.
- DNS resolves normal Regional service endpoint.

No endpoint ENI or endpoint SG exists.

### Endpoint service/provider failure

For private service through PrivateLink:

- Provider allowed consumer principal.
- Connection accepted if acceptance required.
- Endpoint service uses correct NLB.
- NLB listener and target group healthy.
- Supported AZs align.
- Provider application accepts traffic.
- Private DNS name verified/configured where used.

Consumer endpoint health does not prove provider targets are healthy.

### Endpoint failure map

| Symptom | First checks |
|---|---|
| `pendingAcceptance` | Provider acceptance/allowed principal |
| DNS returns public address | Private DNS/VPC Resolver/conflicting zone |
| DNS private, connection timeout | Endpoint SG/NACL/route/ENI/provider health |
| API `AccessDenied` | Endpoint + IAM + resource + KMS policies |
| One AZ fails | Endpoint ENI/subnet IP/NLB target/AZ support |
| Gateway endpoint ignored | Route-table association/prefix-list route |

## VPC peering

### Required evidence

- Connection `active`.
- Non-overlapping primary/secondary CIDRs.
- Source route to peer CIDR.
- Peer return route.
- Correct subnet route-table associations.
- SG/NACL allowance.
- DNS resolution options/private-zone association where required.

### Peering failure patterns

- Request not accepted.
- One-sided route.
- New secondary CIDR not routed.
- Overlapping CIDR.
- More-specific route sends traffic elsewhere.
- A-B-C attempted transit.
- Peer NAT/IGW/VPN expected as transit.
- Private DNS expected automatically.

Peering is one-to-one and non-transitive.

## Transit Gateway

### Packet path

```text
Source VPC route -> TGW
  -> source attachment
  -> associated TGW route table
  -> destination attachment route/propagation
  -> destination VPC route
  -> destination security
  -> reverse path based on reverse ingress table
```

### Association and propagation

- Association chooses the TGW route table used for traffic entering from an attachment.
- Propagation installs an attachment’s reachable prefixes into selected TGW route tables.
- Static route can override/shape propagated behavior according to route selection.
- Blackhole route intentionally/unintentionally drops matching traffic.

### TGW checks

- Attachment state.
- VPC attachment subnets in required AZs.
- Source workload subnet route.
- Source attachment association.
- Destination propagation/static route.
- Destination VPC route back to TGW.
- Reverse attachment’s associated TGW table.
- SG/NACL/firewall.
- Overlapping CIDR.
- Appliance mode and symmetric path.

### TGW one-way example

```text
VPC-A table routes B -> TGW
TGW-A-ingress table routes B -> attachment B
VPC-B receives packet

But VPC-B subnet lacks A -> TGW
```

Result: forward reaches B; response never returns.

### TGW failure map

| Symptom | First checks |
|---|---|
| No TGW route on ingress | Attachment association/propagation/static route |
| One-way | Reverse VPC route + reverse TGW associated table |
| Unexpected segmentation bypass | Wrong association/overbroad propagation |
| One AZ/appliance path fails | Attachment subnet, appliance mode, symmetry |
| Route `blackhole` | Deleted attachment or explicit blackhole |
| VPN routes absent from VPC | VPN attachment propagation into correct TGW table |

## Hybrid DNS

### Direction memory

```text
On premises -> AWS private DNS = Resolver inbound endpoint
AWS VPC -> on-premises DNS     = Resolver outbound endpoint + rule
```

### Hybrid DNS checks

- Correct conditional-forwarding domain.
- Most-specific Resolver rule.
- Rule associated with source VPC.
- Endpoint IPs/status/AZs.
- SG permits TCP and UDP `53`.
- VPN/DX/TGW route and return path.
- Target DNS server permits endpoint source IPs.
- Private hosted-zone VPC association.
- No forwarding loop or shadowing zone.
- Query logs and target DNS logs.

Connected hybrid routing does not automatically create name resolution.

## Common cross-layer failures

### DNS versus network versus TLS

```text
NXDOMAIN/SERVFAIL -> DNS zone/rule/upstream
Timeout to IP     -> route/security/tunnel/listener
TCP connects      -> basic network works
TLS error         -> certificate/hostname/chain/policy
HTTP error        -> proxy/app/IAM/resource policy
```

Do not reset a VPN tunnel to fix a proven certificate hostname mismatch.

### CIDR overlap

Overlap can affect:

- VPC peering creation.
- TGW route choice.
- VPN/on-premises routing.
- Client VPN local/client CIDRs.
- Private service reachability.

PrivateLink can avoid routed CIDR adjacency when only one service must be exposed.

### Return-path checklist

For any hybrid/private flow, prove:

- Destination knows source CIDR.
- Reverse VPC route exists.
- Reverse TGW/peering/VPN path exists.
- On-premises router advertises/installs source network.
- Stateful firewall sees both directions.
- NAT does not translate unexpectedly.
- NACL ephemeral traffic is allowed.

Most “one-way” problems are return-path problems.

## Evidence model

### Evidence sources

- Site-to-Site VPN tunnel status/metrics/logs.
- Customer gateway device IKE/IPsec/BGP logs.
- Direct Connect connection/VIF/BGP state.
- Client VPN connection logs and client logs.
- Route tables and TGW associations/propagations.
- Endpoint state, ENIs, SGs, private DNS, policies.
- Resolver query logs and DNS tests.
- VPC Flow Logs.
- Reachability Analyzer for supported AWS path.
- CloudTrail/Config for changes.
- Application/TLS tests from actual source.

### Correlation ladder

```text
1. Exact time/source/destination/protocol.
2. DNS answer from failing network.
3. Tunnel/VIF/endpoint/attachment state.
4. Learned/static route evidence.
5. Forward and return route tables.
6. Flow Logs on both AWS-side interfaces.
7. Customer/on-prem firewall and router logs.
8. TLS/application log.
```

### Change correlation

Look for:

- Customer public IP/device replacement.
- PSK/IKE proposal change.
- BGP ASN/filter change.
- New VPC/on-premises CIDR.
- TGW association/propagation change.
- Endpoint policy/private DNS change.
- Client VPN route/auth rule change.
- Certificate expiry/rotation.

“Worked yesterday” strongly suggests change, expiry, route advertisement, or renewed session behavior.

## Safe remediation

### VPN remediation

```text
Keep working tunnel active
  -> repair down tunnel parameters/underlay
  -> establish IKE/IPsec/BGP
  -> validate routes and test traffic
  -> confirm both tunnel metrics
  -> restore intended preference/failover
  -> document device config backup.
```

Do not restart both tunnels simultaneously when one still carries production.

### Private endpoint remediation

```text
Test endpoint-specific DNS/IP
  -> fix ENI SG/route if timeout
  -> fix endpoint/IAM/resource/KMS policy if denied
  -> enable/test private DNS
  -> test normal service name
  -> verify NAT/public path no longer used where intended.
```

### TGW remediation

```text
Capture attachments/tables/routes
  -> add narrow missing association/propagation/static route
  -> verify reverse table
  -> test one flow/AZ
  -> inspect Flow Logs
  -> remove temporary/bypass route.
```

### Governance

- Monitor both VPN tunnels and BGP state.
- Store PSKs/device configs securely and rotate through controlled process.
- Maintain current customer gateway public IP/ASN/contact ownership.
- Document advertised prefixes and route filters.
- Design redundant Direct Connect/VPN paths without shared failure domains.
- Centralize TGW/Resolver/endpoint ownership.
- Restrict endpoint and authorization policies.
- Log Client VPN connections and critical DNS/tunnel events.
- Test failover and MTU, not only tunnel state.

### Exam traps

- VPN tunnel `UP` does not prove BGP/routes/data traffic.
- BGP session `UP` does not prove correct prefixes or return routes.
- Two VPN tunnels exist; one down means degraded redundancy.
- IKE phase 1 and IPsec phase 2 can fail for different parameter mismatches.
- Small packets working while large transfers fail suggests MTU/MSS/fragmentation.
- Direct Connect physical link, VIF, BGP, and routing are separate layers.
- Direct Connect is not encrypted by default merely because it is private.
- Client VPN needs authentication + authorization + route + target association/security.
- Client VPN route change may require client reconnection in split-tunnel designs.
- Interface endpoint timeout points to DNS/SG/route; `AccessDenied` points to policy.
- Endpoint policy restricts; it does not grant IAM permission.
- Gateway endpoint has route-table association but no ENI/SG.
- PrivateLink consumer endpoint health does not prove provider NLB targets are healthy.
- VPC peering is non-transitive and cannot borrow peer NAT/IGW/VPN transit.
- TGW association chooses ingress table; propagation installs destinations.
- Forward path without reverse VPC/TGW/on-premises route is incomplete.
- Hybrid network connection does not automatically provide hybrid DNS.
- Test from the actual source network; a VPC test can miss on-premises DNS/firewall/MTU behavior.

### Do not memorize

- Every IKE/IPsec proposal value.
- Exact VPN MTU for every device/path.
- Every BGP route-selection tie breaker.
- Full customer gateway vendor commands.
- Exact Direct Connect optical values.
- Every Client VPN log field.
- Console click paths.

### Ready when

Given a hybrid/private failure, you can:

1. Separate underlay, tunnel/VIF, BGP/static route, data path, and application layers.
2. Diagnose both VPN tunnels using IKE/IPsec/BGP/status/metric evidence.
3. Recognize MTU/fragmentation symptoms and safe MSS/PMTU investigation.
4. Troubleshoot Client VPN authentication, authorization, routes, associations, DNS, and overlap.
5. Troubleshoot interface/gateway endpoint state, DNS, SG, provider, and policy layers.
6. Prove peering/TGW forward and return paths with association/propagation evidence.
7. Correlate AWS logs with customer router/firewall and application evidence.

---

## Skill 5.3.5 — Configure and analyze CloudWatch network monitoring services

### Official goal

Configure network monitoring, select useful metrics and alarms, localize path degradation, and combine monitoring with logs/configuration evidence.

### What the exam tests

- Choose Network Synthetic Monitor, Network Flow Monitor, Internet Monitor, or Synthetics canary.
- Configure monitors/probes/scopes at the right path.
- Interpret round-trip time, packet loss, and network health indicator.
- Analyze NAT, VPN, TGW, ELB, Route 53, Resolver, firewall, and accelerator metrics.
- Build useful alarms for sustained user impact and redundancy loss.
- Know that metrics show symptoms, not packet payload or exact route-rule cause.

### Dimensions

**Primary:** configuration, evidence, diagnosis, remediation  
**Support:** behavior  
**Precision:** L3 — product selection, monitor/probe, RTT/loss/health indicator, service metric names, dimensions, and alarm semantics matter.

### Fast monitor selector

| Need | Service |
|---|---|
| Continuous configured AWS-to-on-premises path probes | CloudWatch Network Synthetic Monitor |
| Observe actual supported TCP workload flows | CloudWatch Network Flow Monitor |
| See end-user internet availability/performance by geography/ASN | CloudWatch Internet Monitor |
| Run scripted DNS/TLS/HTTP/application transaction | CloudWatch Synthetics canary |
| Test configuration reachability without packets | VPC Reachability Analyzer |
| Inspect observed IP flow metadata | VPC Flow Logs |

### Core distinction

```text
Synthetic Monitor = “Can this configured path work now?”
Flow Monitor      = “How are real workload TCP flows behaving?”
Internet Monitor  = “How is the public internet affecting users?”
Synthetics canary = “Can this scripted application journey succeed?”
```

### Evidence hierarchy

```text
Monitor/metric detects symptom
  -> identifies path/resource/time scope
  -> logs show observed traffic/error
  -> configuration explains route/policy
  -> application evidence proves user result
```

Metric alarm is a starting point, not root-cause proof.

## CloudWatch Network Synthetic Monitor

### Purpose

Agentless, continuous synthetic monitoring between AWS-hosted sources and on-premises destinations across supported hybrid paths.

Useful for:

- Site-to-Site VPN path health.
- Direct Connect path health.
- AWS-to-on-premises latency/loss baselines.
- Detecting degradation before users report it.
- Comparing multiple probes/paths.

It sends configured probe traffic even when the application is idle.

### Object model

```text
Monitor
  -> probe 1: AWS source -> on-prem destination/protocol
  -> probe 2: AWS source -> on-prem destination/protocol
  -> metrics: RTT, packet loss, network health indicator
```

### Monitor

Logical container for related network probes.

Use one monitor to group paths for an application, site, or network objective.

Document:

- Owner/application.
- Source environment.
- On-premises site/destination.
- Expected path/VPN/DX.
- Alarm threshold and runbook.

### Probe

Defines a synthetic network test.

Recognize properties such as:

- AWS source/subnet or supported source resource.
- Destination IP.
- Protocol/port where applicable.
- Packet/test characteristics.
- Probe interval/status.

The destination must reply/permit the chosen probe traffic.

### Core metrics

**Round-trip time (RTT)**

- Time for probe to destination and response.
- Rising RTT means latency degradation somewhere on path.
- Does not alone identify which hop caused it.

**Packet loss**

- Percentage/ratio of probes without successful response.
- Sustained loss harms TCP/application performance.
- `100%` can mean route/firewall/destination stopped responding—not only provider failure.

**Network health indicator**

- Helps attribute whether detected degradation is associated with the AWS network portion.
- Read indicator state together with RTT/loss and path evidence.
- Do not infer numeric polarity without checking metric definition/dashboard label.

### Synthetic Monitor diagnosis

```text
RTT/loss alarm
  -> affected probe/source/destination
  -> network health indicator
  -> VPN/DX tunnel/circuit metrics
  -> route/BGP changes
  -> Flow Logs/customer router logs
  -> application test.
```

### Synthetic failure patterns

| Evidence | First checks |
|---|---|
| `100%` loss from probe creation | Destination/port response, SG/NACL/firewall, route/return route |
| All probes to one site degrade | Hybrid circuit/tunnel/site/provider path |
| One probe only degrades | Source subnet/AZ/route/destination host |
| RTT rises, health indicator suggests AWS issue | AWS path event plus service metrics/support evidence |
| RTT rises, AWS indicator normal | Customer/provider/destination/application path candidate |
| Probe healthy, app fails | DNS/TLS/application/auth path not represented by probe |

### Synthetic Monitor limits

- Probe covers configured source/destination/protocol only.
- Agentless probe does not inspect application payload/root cause.
- Healthy probe does not prove DNS, TLS, login, or business transaction.
- Destination may prioritize/drop probe traffic differently from real traffic.
- One probe cannot represent every AZ/user/path.

## CloudWatch Network Flow Monitor

### Purpose

Near-real-time performance visibility for actual supported TCP workload flows inside VPC networks and toward supported AWS services.

Useful for:

- Real application-flow RTT/latency.
- Packet-loss/retransmission symptoms.
- Top contributors to network degradation.
- AWS-network versus workload/external attribution.
- Finding which source/destination flow is affected.

It observes real flows; no application traffic means no flow evidence.

### Operating model

```text
Lightweight agent on supported compute
  -> observes TCP flow telemetry
  -> Network Flow Monitor scope/monitor
  -> flow metrics and network health indicator
  -> top contributors/path analysis
```

### Configuration concepts

Recognize:

- Supported compute/agent deployment.
- Monitoring scope/flow selection.
- Source and destination context.
- Actual TCP workload traffic.
- Permissions/service-linked role/telemetry delivery.
- Monitor/dashboard/metrics.

If agents or workload coverage are missing, the monitor can have an evidence gap.

### Flow Monitor evidence

Can help show:

- Source and destination workload/service.
- Round-trip time.
- Packet loss/retransmission-style degradation.
- Data/flow volume.
- Top contributors.
- Network health indicator for AWS attribution.
- Time and AZ/Region path context where available.

Use VPC Flow Logs for accept/reject/five-tuple evidence; use Flow Monitor for performance health of actual flows.

### Flow Monitor versus VPC Flow Logs

| Property | Network Flow Monitor | VPC Flow Logs |
|---|---|---|
| Main question | Is real TCP flow performing poorly? | Was IP flow accepted/rejected and what metadata? |
| Collection | Lightweight agent/flow telemetry | VPC/ENI service metadata capture |
| Evidence | RTT/loss/top contributors/health attribution | IPs/ports/protocol/bytes/action/status |
| Payload | No | No |
| Root cause alone | No | No |

They complement each other.

### Flow Monitor diagnosis

```text
Find degraded monitor/flow
  -> identify top source/destination contributor
  -> inspect RTT/loss and health indicator
  -> compare AZ/Region/service paths
  -> inspect Flow Logs/routes/SG/NACL
  -> inspect workload CPU/socket/app dependency
  -> verify after remediation.
```

### Flow Monitor failure patterns

| Evidence | First checks |
|---|---|
| No flows shown | Agent/support/scope/workload traffic/permissions |
| One destination has high RTT | Destination/service path, cross-AZ/Region, saturation |
| Many sources to one target degrade | Target/network bottleneck |
| One source degrades to all targets | Source host/ENI/AZ/node issue |
| AWS health indicator flags path | Correlate AWS network/service event and path |
| Indicator normal but retransmissions high | Workload, SG/NACL asymmetry, external network, receiver saturation |

### Flow Monitor limits

- Focuses on supported actual TCP flows.
- Needs compatible agent/compute coverage.
- Does not replace UDP/ICMP/application-specific tests.
- Does not provide packet payload.
- Metrics do not name the exact route/SG/NACL rule.
- No traffic means no real-flow sample.

## CloudWatch Internet Monitor

### Purpose

Shows how public internet conditions affect users of internet-facing AWS workloads.

Useful for:

- Internet availability degradation.
- Internet performance/latency degradation.
- Affected cities/regions/countries.
- Affected autonomous system/network provider (ASN).
- Health events and user-impact scope.
- Comparing/considering AWS Region/edge routing optimizations.

### Object model

```text
Internet Monitor monitor
  -> associated supported AWS resources
  -> observed internet traffic footprint
  -> availability/performance measurements
  -> geographic/network health events
```

### Core evidence

Recognize:

- Availability score/measurement.
- Performance score/measurement.
- Health event.
- Affected location.
- ASN/network provider.
- Traffic percentage/impact.
- Monitored resource/Region.
- Suggested optimization insight where available.

An issue limited to one ASN/city points away from a universal origin outage.

### Internet Monitor diagnosis

```text
Internet health event
  -> affected geography + ASN
  -> traffic/user percentage
  -> availability versus performance
  -> compare other geographies/providers
  -> CloudFront/GA/ELB/origin metrics
  -> application logs
  -> decide wait, route, accelerate, or remediate origin.
```

### Internet Monitor failure patterns

| Evidence | Likely direction |
|---|---|
| One ASN/location degrades | External ISP/local internet path |
| Many geographies degrade | AWS endpoint/origin/global app candidate |
| Availability drops, performance normal elsewhere | Regional/provider reachability event |
| Performance drops, availability remains | Latency/congestion rather than total outage |
| Internet healthy, app `5xx` rises | Origin/application issue |
| No monitor evidence | Resource/traffic coverage, monitor status, traffic percentage |

### Internet Monitor limits

- Focuses on public internet user paths.
- Does not test private VPC/VPN/DX routing.
- Aggregate health does not prove one user’s local device/Wi-Fi.
- It does not show packet payload or exact SG/NACL rule.
- Resource association/traffic coverage determines visibility.

## CloudWatch Synthetics canaries

### Purpose

Scheduled scripted tests of application paths.

Can validate:

- DNS resolution.
- TLS handshake/certificate.
- HTTP endpoint/status/content.
- API workflow.
- Browser/user journey.

Produces metrics, logs, screenshots/artifacts according to canary type/configuration.

### Canary versus network monitors

| Need | Tool |
|---|---|
| Hybrid packet RTT/loss without app transaction | Network Synthetic Monitor |
| Real TCP workload performance | Network Flow Monitor |
| Internet-user geographic impact | Internet Monitor |
| Scripted DNS/TLS/HTTP/login flow | Synthetics canary |

Canary failure can be DNS, TLS, app, dependency, or network. Inspect step logs/artifacts.

## Component metrics

### Metric-reading model

For every metric, identify:

- Namespace.
- Metric name.
- Dimensions/resource ID.
- Statistic.
- Period.
- Unit.
- Time window.
- Missing-data behavior.
- Baseline and correlated events.

Same metric name with wrong dimension can describe another resource/AZ.

## NAT gateway metrics

### High-value names

Recognize:

- `ActiveConnectionCount`.
- `ConnectionAttemptCount`.
- `ConnectionEstablishedCount`.
- `ErrorPortAllocation`.
- `IdleTimeoutCount`.
- `PacketsDropCount`.
- `BytesInFromSource`.
- `BytesOutToDestination`.
- `BytesInFromDestination`.
- `BytesOutToSource`.

### NAT interpretations

| Metric pattern | Likely meaning |
|---|---|
| `ErrorPortAllocation > 0` | Translation-port exhaustion/capacity issue |
| Rising `IdleTimeoutCount` | Connections idle longer than NAT state; app keepalive/pool pattern |
| High `PacketsDropCount` | NAT cannot process/drop condition; inspect load/path |
| Source bytes rise, destination bytes do not | Destination/route/connection problem |
| One AZ NAT abnormal | Zonal route/NAT dependency |
| Connections spike with errors | Connection churn/capacity/destination concentration |

NAT metrics do not prove private-subnet route is correct; inspect route tables too.

## Site-to-Site VPN metrics

Recognize:

- `TunnelState`.
- `TunnelDataIn`.
- `TunnelDataOut`.

Alarm separately for each tunnel.

```text
Tunnel 1 down + Tunnel 2 up = application may work, redundancy degraded
```

Data metric asymmetry suggests route/return/firewall direction. Tunnel logs/customer device logs explain negotiation.

## Transit Gateway metrics

Recognize concepts/names such as:

- Bytes/packets in and out.
- Attachment-level traffic.
- Packet drops due to no route.
- Packet drops due to blackhole.
- Other drop/error counters where exposed.

Interpret with:

- TGW and attachment dimensions.
- TGW route-table association/propagation.
- Source/destination VPC Flow Logs.

High traffic proves use; no-route drops point to TGW routing control.

## ELB metrics

### Shared high-value concepts

- `HealthyHostCount`.
- `UnHealthyHostCount`.
- Active/new connections or flows.
- Request count.
- Processed bytes.
- Target response time/latency.
- Load-balancer-generated error count.
- Target-generated error count.
- Rejected connections/resets.

Metric names vary by ALB/NLB/Classic LB.

### ALB clues

Recognize:

- `RequestCount`.
- `TargetResponseTime`.
- `HTTPCode_ELB_5XX_Count`.
- `HTTPCode_Target_5XX_Count`.
- `HealthyHostCount`/`UnHealthyHostCount`.
- `RejectedConnectionCount`.
- `ProcessedBytes`.

Interpretation:

| Pattern | First checks |
|---|---|
| ELB `5xx` rises, target `5xx` flat | LB/no-target/protocol/connectivity side |
| Target `5xx` rises | Application/target side |
| Response time rises, healthy count stable | App/dependency saturation |
| Healthy count falls | Health-check/path/target failure |
| Rejected connections rise | Capacity/connection limits/architecture |

### NLB clues

Recognize:

- Active/new flow counts.
- Client/LB/target TCP reset counts.
- Healthy/unhealthy target counts.
- Processed bytes.

Different reset counters help locate who reset the TCP connection.

Access/connection logs provide per-request/per-connection detail.

## Route 53 and Resolver metrics

### Route 53 health

Recognize:

- Health-check status.
- Percentage of health checkers reporting healthy.
- Connection/response timing metrics where configured.

Correlate with DNS routing policy and TTL. Health change does not instantly erase cached answers.

### Resolver endpoints and DNS Firewall

Monitor concepts such as:

- Inbound/outbound query volume.
- Endpoint IP/availability/capacity signals.
- DNS Firewall query/match/block/alert trends.
- Resolver query-log delivery.

Sharp block rise after rule change can be attack detection or false-positive outage; inspect query logs and rule priority/action.

## Network Firewall metrics

Monitor:

- Packets received/passed/dropped/rejected.
- Stateful/stateless processing signals.
- Firewall endpoint/AZ dimensions.
- Rule-group/capacity/update health where exposed.

High drop count is meaningful only when compared with rule/log/action and traffic baseline.

One AZ with no metrics can mean no traffic, missing route, or missing endpoint—not automatically healthy.

## Global Accelerator metrics

Monitor:

- Healthy/unhealthy endpoint count.
- New/active flow counts.
- Processed bytes in/out.
- Listener/endpoint group/endpoint dimensions.
- Traffic dial and endpoint weight configuration.

Unhealthy endpoint plus zero flows can be expected removal. Zero flows with healthy endpoint can be dial/weight/listener/client-path issue.

## Alarm design

### Alarm properties

Know:

- Metric and dimensions.
- Statistic.
- Period.
- Threshold.
- Comparison operator.
- Evaluation periods.
- Datapoints to alarm.
- Missing-data treatment.
- Alarm action.

One wrong dimension or statistic can make a correct-looking alarm useless.

### Good network alarms

- Sustained packet loss or RTT above baseline/SLO.
- One VPN tunnel down.
- Both VPN tunnels down/traffic stopped.
- NAT `ErrorPortAllocation > 0`.
- NAT drops above baseline.
- TGW no-route/blackhole drops.
- Load balancer healthy targets below safe count.
- Load balancer versus target `5xx` rise.
- Internet Monitor availability/performance health event with meaningful traffic impact.
- Network health indicator/path degradation.
- Endpoint/firewall/accelerator unhealthy count.

### Alarm on redundancy loss

Do not wait for total outage.

Examples:

- One of two VPN tunnels down.
- One AZ has zero healthy targets.
- One probe path fails while second works.
- One accelerator endpoint group becomes unhealthy.

Application can remain green while redundancy is already gone.

### Sustained versus transient

Use evaluation periods/datapoints to reduce noise from brief:

- Network jitter.
- Health-check transition.
- Deployment/restart.
- DNS/cache shift.

But do not smooth away fast, high-impact tunnel or all-target outages.

### Static threshold versus anomaly detection

**Static threshold**

- Good for hard limits: any NAT port-allocation error, tunnel down, no healthy targets.

**Anomaly detection/baseline**

- Good for traffic, latency, loss, and request patterns that vary by time.

Use service SLO and historical baseline, not one universal latency threshold.

### Composite alarm

Can combine signals to reduce noise or represent user impact.

Example:

```text
High RTT
AND packet loss
AND application latency/error rise
```

Keep separate alarm for redundancy loss even without current user errors.

### Missing data

Missing can mean:

- No traffic.
- Resource deleted/replaced.
- Agent/probe stopped.
- Metric dimension changed.
- Telemetry delivery failure.
- Real outage.

Choose `breaching`, `notBreaching`, `ignore`, or missing behavior according to metric meaning. Do not treat all missing network data as healthy.

## Dashboard and investigation design

### Path dashboard

Group by one user path:

```text
Internet/Hybrid path health
  -> DNS health
  -> accelerator/CloudFront/LB health
  -> NAT/TGW/VPN/firewall metrics
  -> target/application latency/errors
```

Show traffic volume beside error rate; zero errors with zero traffic is not success.

### Dimensions to preserve

- Account.
- Region.
- AZ.
- VPC/subnet.
- NAT/TGW attachment/VPN tunnel.
- Load balancer/target group.
- Monitor/probe/flow.
- Geography/ASN.

Aggregating everything can hide one-AZ or one-provider failure.

## Troubleshooting workflow

### Monitoring ladder

```text
1. Confirm alarm metric/dimension/time/statistic.
2. Determine scope: user, flow, probe, AZ, Region, ASN, site.
3. Compare RTT/loss/health indicator with traffic volume.
4. Check component metrics: NAT/VPN/TGW/ELB/firewall/GA.
5. Find last healthy layer and first abnormal layer.
6. Inspect Flow/access/tunnel/Resolver/application logs.
7. Inspect route/security/config changes.
8. Reproduce from actual source.
9. Remediate narrow cause.
10. Verify metrics, logs, and application SLO recover.
```

### Symptom-to-tool map

| Symptom | First tool/evidence |
|---|---|
| AWS-to-on-prem path degrades even when app idle | Network Synthetic Monitor |
| Real EC2 TCP flows show latency/loss | Network Flow Monitor |
| Users in one ISP/city report slowness | Internet Monitor |
| Login/API journey fails | Synthetics canary + app logs |
| NAT connections fail under load | NAT metrics + Flow Logs |
| One VPN tunnel down | Tunnel metrics/logs + device logs |
| LB `5xx` spike | ELB/target metrics + access logs |
| Route believed blocked | Reachability Analyzer + Flow Logs/config |

### Metric-to-log handoff

```text
NAT port error -> NAT metrics -> Flow Logs -> connection pattern
VPN down       -> TunnelState -> VPN/device logs -> IKE/BGP
ELB 5xx        -> metric split -> access log -> target log
Internet event -> geography/ASN -> CloudFront/GA/ELB/app logs
RTT/loss       -> monitor flow/probe -> route/path metrics -> packet/app evidence
```

### Safe remediation

```text
Preserve dashboard/alarm evidence
  -> identify exact affected dimension/path
  -> keep redundant healthy path active
  -> change narrow route/capacity/target/config
  -> run probe/canary/real request
  -> watch recovery over evaluation periods
  -> confirm logs and user SLO
  -> update threshold/runbook if needed.
```

Do not restart every network component because one aggregate graph is red.

### Governance

- Standardize path monitors for critical services/sites.
- Monitor both normal service and redundancy health.
- Tag monitors/probes and assign owners.
- Use dashboards across accounts/Regions/AZs.
- Store alarm actions/runbooks and escalation contacts.
- Review thresholds after architecture/traffic changes.
- Protect telemetry/log destinations.
- Control agent/probe deployment and permissions.
- Test alarms and failover paths periodically.
- Track monitor/alarm/config changes in CloudTrail/IaC.

### Exam traps

- Network Synthetic Monitor uses configured probes; it does not require real app traffic.
- Network Flow Monitor observes actual supported TCP flows and needs agent/coverage.
- Internet Monitor reports public internet user impact by geography/ASN, not private VPN health.
- Synthetics canary tests scripted application behavior, not only network RTT/loss.
- Reachability Analyzer models configuration and sends no packets.
- VPC Flow Logs show metadata/action, not latency root cause or payload.
- RTT increase does not alone prove AWS caused it; use network health indicator and other evidence.
- Healthy network indicator/probe does not prove DNS, TLS, authentication, or application success.
- NAT `ErrorPortAllocation` points to translation-port pressure.
- VPN tunnel `UP` does not prove data routes; one tunnel down is still an alarm-worthy degradation.
- ELB-generated `5xx` and target-generated `5xx` point to different layers.
- Zero errors with zero traffic is not health proof.
- Missing metric data is not automatically healthy.
- Aggregate Regional metric can hide one-AZ failure.
- Metrics detect/size a symptom; logs and configuration find the exact cause.

### Do not memorize

- Exact price per probe/metric/log.
- Every Network Flow Monitor agent limit.
- Every Internet Monitor supported resource.
- Every metric in each namespace.
- Universal RTT/loss thresholds.
- Exact NHI numeric encoding.
- Console click paths.

### Ready when

Given a network-monitoring scenario, you can:

1. Choose Network Synthetic Monitor, Network Flow Monitor, Internet Monitor, or Synthetics canary.
2. Explain monitor/probe versus real-flow/agent behavior.
3. Interpret RTT, packet loss, traffic volume, and network health indicator without overclaiming.
4. Read high-value NAT, VPN, TGW, ELB, Route 53, Resolver, firewall, and accelerator metrics.
5. Design alarms for user impact, capacity errors, and redundancy loss.
6. Correlate monitor metrics with Flow/access/tunnel/DNS/application logs and configuration.
7. Verify remediation through both network telemetry and application outcome.

---

# Skill-by-skill model complete

Coverage now runs from **1.1.1** through **5.3.5** in official guide order.

Next transformation, when requested:

```text
Compress repeated foundations
  -> link reusable knowledge nodes
  -> build service-selection tables
  -> build troubleshooting indexes
  -> produce exam-review/Kindle edition.
```
