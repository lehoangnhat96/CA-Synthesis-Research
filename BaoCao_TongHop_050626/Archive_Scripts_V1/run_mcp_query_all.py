
import asyncio
import sys
sys.path.append(r'C:\Users\ADMIN\.gemini\antigravity\scratch')
import run_mcp_tool

notebooks = {
    'C.A - 1 2': '96fe8fe6-c92b-42fb-8f17-8353f7539906',
    'C.A - 2 3 4': 'ece9faaf-5bf1-460a-9d71-9510b1f79cc4',
    'C.A - 4 5 6': '8ae055dd-590e-4430-8afb-afcb31320320',
    'C.A - 7 8': 'c2f074f1-396a-4df0-a32e-938c2433e3e4'
}

query_text = 'Đánh giá tính logic và khả thi dựa trên các bài báo trong notebook này đối với 3 định hướng phát triển cho vật liệu Fe/N-CA dùng Composite Binder (Chitosan+Nafion): 1. Làm Cảm biến sinh học (Aptasensor) tận dụng nhóm -NH2 của Chitosan. 2. Phân tích đồng thời nhiều chất (Multiplexing) nhờ tâm xúc tác Fe-N4. 3. Làm cảm biến in lưới dẻo mang mặc (Wearable SPCE) nhờ độ bám dính của Chitosan. Hãy trích dẫn.'

async def main():
    for name, nid in notebooks.items():
        print(f'\n--- Querying {name} ---')
        args = {'notebook_id': nid, 'query': query_text}
        res = await run_mcp_tool.run_tool('notebook_query', args)
        for item in res.content:
            if hasattr(item, 'text'):
                print(item.text)
            else:
                print(item)

asyncio.run(main())

