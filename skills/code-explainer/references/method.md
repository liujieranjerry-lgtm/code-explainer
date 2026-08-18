# Code Explainer Method

## Narrative Template

A successful explanation follows this shape:

1. `角色句`: This code is the [role] of the [system]. It is responsible for [one-sentence job].
2. `入口句`: It starts by [first action], receiving [data], then [next action].
3. `机制句`: The key mechanism is [technical idea], meaning [plain-language version].
4. `流程句`: After [event A], it does [action B]; if [condition C], it returns [result D]; otherwise it continues to [action E].
5. `价值句`: So this code guarantees [behavior] and lets [system] [benefit].

Keep these five elements inside a flowing paragraph. Do not announce them as separate headings.

## Common Term Mappings

| Code concept | Plain-language role |
|---|---|
| `interface` | A contract that defines what an object must look like |
| `type` | A standard shape for a kind of object |
| `Map` | A dictionary that maps names to values |
| `Promise<T>` | A future value; "I promise this result will arrive later" |
| `AsyncIterable` | A stream you can read one item at a time while waiting |
| `await` | Pause here until the result is ready |
| `push()` | Append one item to the end of a list |
| `??` | Use the left value if it exists, otherwise use the right value |
| `?.` | Read the field only if the object exists |
| `...` | Spread or expand a collection into individual items |
| `for` loop | Repeat the same process a set number of times |
| `if` branch | Choose one path based on a condition |
| `try/catch` | Attempt the normal path, but catch errors instead of crashing |
| `isError: true` | Mark this result as a failure |
| `observation` | A tool result that becomes visible to the model |

## Worked Example: Interface

Target code:

```ts
export interface LlmClient {
  complete(request: LlmRequest): Promise<AssistantMessage>;
}
```

Good narrative:

`LlmClient` is a contract for the model-calling layer. It states that any model client must provide `complete(request: LlmRequest)`, which receives a unified request and returns a `Promise<AssistantMessage>`; that means "the final standard answer will arrive later." The Agent Loop depends only on this contract, not on provider-specific formats.

## Worked Example: Loop

Target code:

```ts
for (let turn = 1; turn <= maxTurns; turn += 1) {
  const assistant = await this.completeAssistant(turn, { ... });
  if (assistant.toolCalls.length === 0) {
    return this.buildResult(assistant.content, turn, "final");
  }
}
```

Good narrative:

The loop starts at `turn = 1` and continues until it reaches `maxTurns`. Each iteration calls `completeAssistant` to let the model think once. If `assistant.toolCalls.length === 0`, the model has given a final answer, so the program calls `buildResult(assistant.content, turn, "final")` and stops. If tools were requested, the loop continues after executing them, letting the model see the results.

## Worked Example: Two Snippets as One System

Target code:

```ts
new Agent({ onEvent(event) { /* ... */ } });

for await (const event of agent.runEvents(input)) {
  // ...
}
```

Good narrative:

Both snippets consume the same agent event stream. The first registers an `onEvent` callback, so the Agent pushes events to the external program. The second uses `for await` to pull events one at a time. They are two integration styles for the same event system, so external UIs and logs do not need to modify the Agent Loop.

## Word-by-Word Example

For a request like "解释每个代码词":

- `runInternal`: the main entry point of the Agent loop.
- `input`: the user's current message.
- `maxTurns`: the maximum number of rounds allowed.
- `this.messages.push(...)`: append a message to the conversation history.
- `toolCalls`: the list of tools the model requested.
- `executeToolCalls`: run the requested tools for real.
- `buildResult`: package the final answer, turn number, and end status.

## Style Guardrails

- Do not explain generic programming concepts unless they appear in the code.
- Do not invent names or types that are not in the user's snippet.
- Do not assume the user knows JavaScript, TypeScript, API jargon, or Agent internals.
- Do not use more than one analogy per paragraph unless the analogy genuinely helps.
- When the user says "继续" or "同样", keep the same narrative style instead of changing format.
