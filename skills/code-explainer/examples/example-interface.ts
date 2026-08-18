export interface LlmClient {
  complete(request: LlmRequest): Promise<AssistantMessage>;
}

export interface StreamingLlmClient extends LlmClient {
  stream(request: LlmRequest): AsyncIterable<LlmStreamEvent>;
}
