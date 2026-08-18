for (let turn = 1; turn <= maxTurns; turn += 1) {
  const assistant = await this.completeAssistant(turn, {
    messages: [...this.messages],
    tools: this.tools.toLlmToolSpecs()
  });

  this.messages.push(assistant);

  if (assistant.toolCalls.length === 0) {
    return this.buildResult(assistant.content, turn, "final");
  }
}
