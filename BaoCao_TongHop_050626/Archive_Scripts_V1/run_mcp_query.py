
import asyncio
import sys
import json
sys.path.append(r'C:\Users\ADMIN\.gemini\antigravity\scratch')
import run_mcp_tool

async def main():
    args = {
        'notebook_id': '5834a479-1b89-49e4-8fff-29822f2005ae',
        'query': 'Dựa vào các bài báo và dữ liệu trong Notebook này, hãy đánh giá tính logic, khả thi và sự mạch lạc (Linear Thinking) của 3 định hướng phát triển sau cho hệ vật liệu Fe/N-CA dùng Composite Binder (Chitosan+Nafion): 1. Chuyển thành Cảm biến sinh học siêu chọn lọc (Aptasensor) tận dụng nhóm -NH2 của Chitosan. 2. Phân tích đồng thời nhiều chất (Multiplexing) nhờ khả năng phân giải quá thế của tâm Fe-N4. 3. Làm cảm biến in lưới dẻo mang mặc (Wearable SPCE) nhờ độ bám dính của Chitosan. Hãy trích dẫn cơ sở dữ liệu cụ thể.'
    }
    res = await run_mcp_tool.run_tool('notebook_query', args)
    for item in res.content:
        if hasattr(item, 'text'):
            print(item.text)
        else:
            print(item)

asyncio.run(main())

