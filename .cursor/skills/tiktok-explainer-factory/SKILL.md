---
name: tiktok-explainer-factory
description: Builds reusable Vietnamese TikTok AI explainer videos with local free HyperFrames. Use when creating, editing, previewing, or rendering a vertical explainer, episode template, caption, hook, or MP4 in this repo.
---

# TikTok explainer factory

Đọc `.cursor/rules/free-only.mdc` và `.cursor/rules/clip-loop.mdc` trước. Rule là cổng. Skill này là lệnh và thứ tự.

HyperFrames owns the render contract. Before editing a composition, read the installed `hyperframes` skill and follow its current files.

Mẫu đang giữ: `exports/previews/001-db-index-110-v7.mp4`. Episode sau đạt lời giảng, cú nhảy, bảng trước/sau, và nhịp của bản đó. Thêm ví dụ đời thường ở sân đầu và nền đổi theo sân. Không chép bài index sang chủ đề khác.

## Output

- 1080×1920, 60 fps. Duration follows the episode, not a fixed 20, 25, or 30 second slot. A clip stays at or under 5 minutes. A technical test may be about 5 seconds.
- Do not set a real episode's root `data-duration`, storyboard timestamps, or render length until the person approves a proposed duration.
- Vietnamese on screen. Diacritics must render. Font is Be Vietnam Pro in `video/assets/fonts/`.
- Portrait safe zone: no words in the top 168 px or below y=1330. Readable type is at least 28 px.
- Frame 0 is the hook beside an everyday object already doing the action. Follow `.cursor/rules/stage-picture.mdc`.

## Layout

```text
video/
├── index.html
├── compositions/
├── assets/
└── meta.json
episodes/
└── <id>/
    ├── brief.md
    ├── script.md
    ├── design.md
    ├── storyboard.md
    ├── research.md
    └── assets/
```

`video/` is the reusable composition. An episode folder holds the package and captures. Swap episode content. Do not clone the composition per episode.

## Closed loop

Giọng, bảng, cú nhảy, dải chữ, và vùng an toàn đã chốt. Không hỏi lại. Dừng để duyệt thời lượng, mọi bước tốn tiền, và bản draft.

1. Lập gói bằng skill `tiktok-idea-to-package`. Có một ví dụ đời thường. Đề xuất thời lượng. Dừng.
2. Sau khi có số giây, viết `storyboard.md`. Chạy skill `humanizer` lên mọi câu người xem đọc, theo `.cursor/rules/human-voice.mdc`.
3. Sửa HTML trong `video/`. Phần tử có giờ là `class="clip"` với `data-start` và `data-duration`. Mỗi composition một GSAP timeline đang pause. Một sub-composition một sân. Đổi sân thì đổi nền. Chỗ so sánh là cột trước/sau. Con trỏ nhảy.
4. Trong `video/`: `npx --yes hyperframes@0.8.207 check --json`. Sửa hết lỗi. Phiên bản này trùng `video/package.json`.
5. `npx --yes hyperframes@0.8.207 snapshot`. Nhìn frame: vùng an toàn, dấu tiếng Việt, cú nhảy, cả hai thanh nhìn ra, nền đã đổi, câu chữ còn trên hình trong lúc sơ đồ chạy.
6. Ghi phần tự đối chiếu trong `.cursor/rules/clip-loop.mdc` vào `video/REVIEW.md`. Chưa đạt thì sửa, chưa render.
7. Render bằng CLI trực tiếp, từ thư mục `video/`, đường ra tuyệt đối. `npm run render --` nuốt cờ.

```bash
npx --yes hyperframes@0.8.207 render --quality draft --output E:/RnDWork/AI_Video/exports/previews/<id>.mp4
```

`delivery` chỉ sau khi người duyệt nhận bản draft.

8. File không rỗng và `ffprobe` khớp `data-duration` đã duyệt. Đưa đường file. Chờ.

Không render cloud. Không publish. Test kỹ thuật khoảng 5 giây được render khi check và snapshot đã sạch.

## Dải chữ khi chưa có tiếng

Dải dưới là lời giảng. Một hoặc hai câu nói được, trên hình khoảng 5–6 giây. Trong lúc đó sơ đồ vẫn có dấu mới mỗi 2–4 giây. Một từ mang màu vai. Câu nói người xem đang hỏi gì, hệ thống làm gì, và số thuộc bảng nào.

Khi đã có tiếng:

```bash
npx hyperframes transcribe --model small --language vi
```

Người đọc transcript trước khi đưa lên hình. Model mặc định tiếng Anh sẽ dịch câu tiếng Việt.

## Cấm

HeyGen trả phí, cloud render, thêm một framework video, đăng TikTok tự động, và câu khẳng định một thiết lập xóa lịch sử chat hoặc ngừng mọi lưu dữ liệu.
