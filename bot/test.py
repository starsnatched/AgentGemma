from src.utils.infer import OllamaInfer

async def main():
    infer = OllamaInfer(host="http://localhost:11434", model="smallthinker", num_ctx=8192)
    messages = [
        {"role": "user", "content": "Hello, how are you?"},
    ]
    async for msg in infer.infer(messages):
        print(msg)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())